"""Small, offline contracts for immutable arXiv-only refresh receipts."""
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import record_arxiv_refresh as refresh

SHA = "a" * 40


def paper(identifier, published, title=None):
    return {
        "arxiv_id": identifier, "title": title or f"Robot {identifier}",
        "published": published, "paper_url": f"https://arxiv.org/abs/{identifier}",
        "track": "Dexterity & Teleoperation", "subcategory": "Dexterous Hand Retargeting",
        "specialty": "Physics & Dynamics", "classification_status": "needs-review",
        "abstract": "A robot hand motion method.",
    }


def snapshot(day, records):
    return {
        "as_of": day,
        "window": {"start": f"2023{day[4:]}", "end": day, "years": [2023, 2024, 2025, 2026]},
        "source": {"candidate_records": len(records) + 2,
                   "classified_records": len(records), "unclassified_records": 2,
                   "candidate_coverage_verified": True,
                   "api_declared_candidate_records": len(records) + 2,
                   "snapshot_date": day},
        "taxonomy": {"version": 4}, "papers": records,
    }


class ArxivRefreshReceiptTests(unittest.TestCase):
    def setUp(self):
        self.retained = paper("2401.00001", "2024-01-01", "Shared Robot Title")
        self.before = snapshot("2026-10-04", [
            paper("2310.00001", "2023-10-04"),
            paper("2501.00001", "2025-01-01"), self.retained,
        ])
        changed = deepcopy(self.retained)
        changed["abstract"] = "A revised abstract, not a newly published paper."
        self.after = snapshot("2026-10-08", [changed, paper("2610.00001", "2026-10-07")])
        self.conference = {"as_of": "2026-10-04", "papers": [{"title": "Shared Robot Title"}]}

    def build(self, before=None, after=None, conference=None, day="2026-10-08"):
        return refresh.build_receipt(
            before if before is not None else self.before,
            after if after is not None else self.after,
            conference if conference is not None else (self.conference, deepcopy(self.conference)),
            SHA, day,
        )

    def test_added_removed_and_retained_changes_reconcile(self):
        evidence = self.build()["layers"]["arxiv_recent.json"]
        self.assertEqual([p["id"] for p in evidence["added"]], ["2610.00001"])
        self.assertEqual(len(evidence["removed"]), 2)
        reasons = {p["id"]: p["reason"] for p in evidence["removed"]}
        self.assertEqual(reasons["2310.00001"], "outside_new_window")
        self.assertEqual(reasons["2501.00001"], "missing_within_new_window")
        self.assertEqual(evidence["removed_outside_new_window"], 1)
        self.assertEqual(evidence["missing_within_new_window"], 1)
        self.assertEqual(evidence["retained_records"], 1)
        self.assertEqual(evidence["retained_metadata_changes"], 1)
        self.assertEqual(evidence["retained_metadata_change_ids"], ["2401.00001"])
        self.assertEqual(evidence["records_before"] + len(evidence["added"]) - len(evidence["removed"]), evidence["records_after"])
        self.assertEqual(evidence["added_published_after_previous_snapshot"], 1)
        self.assertEqual(evidence["added_published_on_or_before_previous_snapshot"], 0)
        self.assertEqual(evidence["added_publication_date_counts"], {"2026-10-07": 1})
        self.assertEqual(evidence["title_abstract_reviewed_added_ids"], [])

    def test_summary_has_provenance_date_link_and_three_levels(self):
        evidence = self.build()["layers"]["arxiv_recent.json"]
        added = evidence["added"][0]
        for key in ("id", "title", "published", "paper_url", "track", "subcategory", "specialty"):
            self.assertTrue(added[key])
        self.assertEqual(added["classification_source"], "refreshed_snapshot")
        self.assertTrue(all(p["classification_source"] == "baseline_last_observed" for p in evidence["removed"]))

    def test_counts_are_derived_without_latest_repository_data(self):
        receipt = self.build()
        evidence = receipt["layers"]["arxiv_recent.json"]
        self.assertEqual(evidence["counts_before"]["candidate_records"], 5)
        self.assertEqual(evidence["counts_after"]["candidate_records"], 4)
        self.assertEqual(evidence["counts_after"]["classified_records"], 2)
        self.assertEqual(evidence["counts_after"]["unclassified_records"], 2)
        self.assertEqual(evidence["counts_after"]["combined_unique_records"], 2)
        self.assertEqual(evidence["counts_after"]["conference_unique_title_overlap"], 1)
        self.assertEqual(receipt["layers"]["papers.json"]["snapshot_after"], "2026-10-04")

    def test_verified_admission_review_distinguishes_known_from_unresolved_absences(self):
        review = {"snapshot_date": "2026-10-08", "checked_on": "2026-10-08", "records": [{
            "id": "2501.00001", "paper_url": "https://arxiv.org/abs/2501.00001",
            "cs_ro_present": True, "current_admission_result": None,
            "updated_on": "2026-10-06", "reason": "Revised abstract no longer meets admission rules.",
        }]}
        receipt = refresh.build_receipt(self.before, self.after, (self.conference, deepcopy(self.conference)),
                                        SHA, "2026-10-08", review)
        evidence = receipt["layers"]["arxiv_recent.json"]
        self.assertEqual(evidence["missing_within_new_window"], 1)
        self.assertEqual(evidence["verified_no_longer_admitted"], 1)
        self.assertEqual(evidence["unresolved_in_window_absences"], 0)
        self.assertIn("元数据修订后未满足现有纳入规则", refresh.render_receipt(receipt))
        for invalid in ({**review, "snapshot_date": "2026-10-07"},
                        {**review, "records": [{**review["records"][0], "id": "2310.00001"}]},
                        {**review, "records": [{**review["records"][0], "cs_ro_present": False}]}):
            with self.subTest(review=invalid), self.assertRaises(ValueError):
                refresh.build_receipt(self.before, self.after, (self.conference, self.conference),
                                      SHA, "2026-10-08", invalid)

    def test_unverified_or_mismatched_api_total_is_rejected(self):
        for key, value in (("candidate_coverage_verified", False),
                           ("api_declared_candidate_records", 99),
                           ("api_declared_candidate_records", True)):
            after = deepcopy(self.after)
            after["source"][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                self.build(after=after)

    def test_source_date_and_window_are_checked(self):
        with self.assertRaisesRegex(ValueError, "receipt date"):
            self.build(day="2026-10-07")
        after = deepcopy(self.after)
        after["source"]["snapshot_date"] = "2026-10-07"
        with self.assertRaisesRegex(ValueError, "window dates"):
            self.build(after=after)
        with self.assertRaises(ValueError):
            self.build(day="20261008")

    def test_conference_edits_are_rejected(self):
        changed = deepcopy(self.conference)
        changed["as_of"] = "2026-10-08"
        with self.assertRaisesRegex(ValueError, "conference source changed"):
            self.build(conference=(self.conference, changed))
        changed = deepcopy(self.conference)
        changed["papers"][0]["title"] = "Unrelated edit"
        with self.assertRaises(ValueError):
            self.build(conference=(self.conference, changed))

    def test_duplicate_ids_and_inconsistent_ledgers_are_rejected(self):
        after = snapshot("2026-10-08", [deepcopy(self.retained), deepcopy(self.retained)])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.build(after=after)
        after = deepcopy(self.after)
        after["source"]["combined_unique_records"] = 99
        with self.assertRaisesRegex(ValueError, "combined_unique_records"):
            self.build(after=after)
        after = deepcopy(self.after)
        after["source"]["unclassified_records"] = 0
        with self.assertRaisesRegex(ValueError, "unclassified"):
            self.build(after=after)

    def test_pure_build_is_deterministic_and_does_not_mutate_inputs(self):
        before, after = deepcopy(self.before), deepcopy(self.after)
        first = self.build()
        self.assertEqual(first, self.build())
        self.assertEqual(self.before, before)
        self.assertEqual(self.after, after)
        self.assertEqual(refresh.render_receipt(first), refresh.render_receipt(self.build()))

    def test_markdown_reports_limits_without_false_withdrawal_or_merge_claims(self):
        content = refresh.render_receipt(self.build())
        for text in ("API 声明", "2023-10-04", "2023-10-08", "2026-10-04", "窗口内未出现，原因未确认",
                     "不表示撤稿", "人工全文精读", "PR 未合并期间", "Robot 2610.00001"):
            self.assertIn(text, content)
        self.assertNotIn("已撤稿", content)
        self.assertIn("catalog-refresh-2026-10-08.json", content)

    def test_existing_receipts_are_immutable_and_identical_content_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            refresh.save_outputs({path: "first\n"})
            refresh.save_outputs({path: "first\n"})
            refresh.save_outputs({path: "first\n"}, check=True)
            with self.assertRaisesRegex(ValueError, "immutable receipt differs"):
                refresh.save_outputs({path: "replacement\n"})
            self.assertEqual(path.read_text(), "first\n")

    def test_missing_or_conflicting_check_writes_nothing_and_preflights_both_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "new.md"
            conflict = Path(directory) / "existing.json"
            with self.assertRaisesRegex(ValueError, "receipt is missing"):
                refresh.save_outputs({missing: "content"}, check=True)
            self.assertFalse(missing.exists())
            conflict.write_text("existing")
            with self.assertRaises(ValueError):
                refresh.save_outputs({missing: "new", conflict: "different"})
            self.assertFalse(missing.exists())
            self.assertEqual(conflict.read_text(), "existing")

    def test_cli_resolves_commit_and_rejects_even_conference_format_only_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            conference_bytes = json.dumps(self.conference).encode()
            (root / refresh.CONFERENCE_SOURCE).write_bytes(conference_bytes + b"\n")
            outputs = [SHA + "\n", json.dumps(self.before).encode(), conference_bytes]
            with patch.object(refresh, "ROOT", root), patch.object(refresh.subprocess, "check_output", side_effect=outputs) as git, patch("sys.stderr", new_callable=StringIO):
                self.assertEqual(refresh.main(["--baseline", "HEAD", "--date", "2026-10-08"]), 1)
            self.assertEqual(git.call_args_list[0].args[0],
                             ["git", "rev-parse", "--verify", "--end-of-options", "HEAD^{commit}"])
            self.assertFalse((root / "docs").exists())


if __name__ == "__main__":
    unittest.main()
