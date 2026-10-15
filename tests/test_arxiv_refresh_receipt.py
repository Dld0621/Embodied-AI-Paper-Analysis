"""Small, offline contracts for immutable, explicitly scoped refresh receipts."""
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


def conference_paper(title, *, year=2026, venue="ICRA", **fields):
    return {"title": title, "year": year, "venue": venue,
            "paper_url": f"https://example.org/papers/{title.replace(' ', '-')}",
            "official_url": f"https://example.org/official/{title.replace(' ', '-')}", **fields}


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
        self.conference = {"as_of": "2026-10-04", "census": {"snapshot_date": "2026-10-04"},
                           "window": {"start": 2022, "end": 2026},
                           "papers": [conference_paper("Shared Robot Title")]}

    def build(self, before=None, after=None, conference=None, day="2026-10-08",
              allow_conference_refresh=False):
        return refresh.build_receipt(
            before if before is not None else self.before,
            after if after is not None else self.after,
            conference if conference is not None else (self.conference, deepcopy(self.conference)),
            SHA, day, allow_conference_refresh=allow_conference_refresh,
        )

    def conference_pair(self):
        before = deepcopy(self.conference)
        before["papers"].append(conference_paper("Removed index record", year=2025, venue="RSS"))
        after = deepcopy(self.conference)
        after["as_of"] = after["census"]["snapshot_date"] = "2026-10-08"
        after["papers"][0]["paper_url"] = "https://example.org/new-open-access-location"
        after["papers"].append(conference_paper("Newly indexed record", year=2024, venue="CoRL"))
        return before, after

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

    def test_explicit_dual_refresh_records_conference_delta_and_hashes(self):
        before, after = self.conference_pair()
        receipt = self.build(conference=(before, after), allow_conference_refresh=True)
        layer = receipt["layers"]["papers.json"]
        self.assertEqual(receipt["refresh_scope"], "conference-and-arxiv")
        self.assertEqual((layer["snapshot_before"], layer["snapshot_after"]), ("2026-10-04", "2026-10-08"))
        self.assertFalse(layer["source_unchanged"])
        self.assertEqual(layer["source_before_sha256"], refresh.canonical_hash(before))
        self.assertEqual(layer["source_after_sha256"], refresh.canonical_hash(after))
        self.assertEqual(layer["records_before"], 2)
        self.assertEqual(layer["records_after"], 2)
        self.assertEqual(len(layer["added"]), 1)
        self.assertEqual(len(layer["removed"]), 1)
        self.assertEqual(layer["retained_records"], 1)
        self.assertEqual(layer["retained_metadata_changes"], 1)
        self.assertEqual(layer["added"][0]["title"], "Newly indexed record")
        self.assertEqual(layer["removed"][0]["title"], "Removed index record")
        for entry in layer["added"] + layer["removed"] + layer["retained_metadata_changed_records"]:
            for field in ("id", "title", "year", "venue", "paper_url", "official_url", "identity_strategy"):
                self.assertTrue(entry[field])
        self.assertEqual(receipt, self.build(conference=(before, after), allow_conference_refresh=True))

    def test_conference_oa_url_change_is_retained_metadata_not_new_identity(self):
        before, after = self.conference_pair()
        after["papers"] = after["papers"][:1]
        before["papers"] = before["papers"][:1]
        layer = self.build(conference=(before, after), allow_conference_refresh=True)["layers"]["papers.json"]
        self.assertEqual(layer["added"], [])
        self.assertEqual(layer["removed"], [])
        self.assertEqual(layer["retained_records"], 1)
        self.assertEqual(layer["retained_metadata_changes"], 1)
        self.assertEqual(layer["retained_metadata_changed_records"][0]["identity_strategy"], "normalized_title+venue")
        self.assertEqual(layer["retained_metadata_changed_records"][0]["paper_url"], after["papers"][0]["paper_url"])

    def test_conference_year_and_source_url_corrections_are_retained_metadata(self):
        before, after = self.conference_pair()
        before["papers"] = [conference_paper("Corrected conference record", year=2025)]
        after["papers"] = [conference_paper("Corrected conference record", year=2026,
                                           official_url="https://doi.org/10.0000/corrected-conference")]
        layer = self.build(conference=(before, after), allow_conference_refresh=True)["layers"]["papers.json"]
        self.assertEqual(layer["added"], [])
        self.assertEqual(layer["removed"], [])
        self.assertEqual(layer["retained_records"], 1)
        self.assertEqual(layer["retained_metadata_changes"], 1)
        self.assertEqual(layer["retained_metadata_changed_records"][0]["year"], 2026)
        self.assertEqual(layer["retained_metadata_changed_records"][0]["official_url"], after["papers"][0]["official_url"])
        self.assertIn("year and URLs are mutable metadata", layer["identity_strategy"])

    def test_conference_year_must_be_integer_under_both_identity_strategies(self):
        for source_id in ({}, {"paperId": "native-id"}):
            for invalid_year in ("2026", True, None):
                before, after = self.conference_pair()
                after["papers"] = [conference_paper("Invalid year", year=invalid_year, **source_id)]
                with self.subTest(source_id=source_id, year=invalid_year), self.assertRaisesRegex(ValueError, "integer year"):
                    self.build(conference=(before, after), allow_conference_refresh=True)

    def test_conference_source_id_survives_title_and_url_revisions(self):
        before, after = self.conference_pair()
        before["papers"] = [conference_paper("Original title", paperId="source-123")]
        after["papers"] = [conference_paper("Revised title", paperId="source-123")]
        layer = self.build(conference=(before, after), allow_conference_refresh=True)["layers"]["papers.json"]
        self.assertEqual(layer["added"], [])
        self.assertEqual(layer["removed"], [])
        self.assertEqual(layer["retained_metadata_change_ids"], ["paperId:source-123"])
        self.assertEqual(layer["retained_metadata_changed_records"][0]["identity_strategy"], "source:paperId")

    def test_duplicate_conference_source_or_bibliographic_keys_are_rejected(self):
        for records in (
            [conference_paper("One", id="same"), conference_paper("Two", id="same")],
            [conference_paper("Same: Title"), conference_paper("Same Title")],
        ):
            for target in (0, 1):
                pair = list(self.conference_pair())
                pair[target]["papers"] = records
                with self.subTest(records=records, target=target), self.assertRaisesRegex(ValueError, "duplicate conference identity"):
                    self.build(conference=tuple(pair), allow_conference_refresh=True)

    def test_dual_refresh_rejects_stale_or_inconsistent_conference_dates(self):
        for missing_census in (False, True):
            before, after = self.conference_pair()
            if missing_census:
                after.pop("census")
            else:
                after["census"]["snapshot_date"] = "2026-10-07"
            with self.subTest(missing_census=missing_census), self.assertRaisesRegex(ValueError, "census date"):
                self.build(conference=(before, after), allow_conference_refresh=True)
        with self.assertRaisesRegex(ValueError, "refresh date"):
            self.build(conference=(self.conference, self.conference), allow_conference_refresh=True)
        before, after = self.conference_pair()
        before["as_of"] = "2026-10-09"
        with self.assertRaisesRegex(ValueError, "backwards"):
            self.build(conference=(before, after), allow_conference_refresh=True)

    def test_dual_markdown_separates_source_dates_and_does_not_claim_publication(self):
        content = refresh.render_receipt(self.build(conference=self.conference_pair(), allow_conference_refresh=True))
        for text in ("顶会与 arXiv", "顶会索引快照", "2026-10-04", "2026-10-08",
                     "## arXiv 新增与移出明细", "## 顶会来源变化", "Newly indexed record",
                     "Removed index record", "保留记录的元数据变化", "不表示新近发表或录用", "换链接不是新增论文"):
            self.assertIn(text, content)
        self.assertNotIn("本次只刷新 arXiv", content)
        self.assertNotIn("顶会来源内容保持不变", content)

    def test_dual_markdown_caps_only_retained_metadata_at_twenty_without_mutating_json(self):
        for count in (0, 20, 21):
            before, after = self.conference_pair()
            retained = [conference_paper(f"Retained changed {index:02}") for index in range(count)]
            before["papers"] = retained + [conference_paper(f"All removed {index:02}") for index in range(21)]
            after["papers"] = [{**p, "paper_url": p["paper_url"] + "?updated"} for p in retained]
            after["papers"] += [conference_paper(f"All added {index:02}") for index in range(21)]
            receipt = self.build(conference=(before, after), allow_conference_refresh=True)
            saved = deepcopy(receipt)
            content = refresh.render_receipt(receipt)
            with self.subTest(count=count):
                self.assertIn(f"本节共 {count} 条，当前展示前 {min(count, 20)} 条", content)
                self.assertIn("同日 JSON 收据](../data/catalog-refresh-2026-10-08.json)", content)
                self.assertIn("其余 1 条已截断" if count == 21 else "未截断", content)
                section = content.split("### 顶会保留记录的元数据变化", 1)[1].split("## 分类、覆盖与发布边界", 1)[0]
                self.assertEqual(section.count("| bibliographic:"), min(count, 20))
                self.assertEqual(receipt, saved)
                self.assertEqual(len(receipt["layers"]["papers.json"]["retained_metadata_changed_records"]), count)
                for index in range(21):
                    self.assertIn(f"All removed {index:02}", content)
                    self.assertIn(f"All added {index:02}", content)

    def conference_admission_review(self):
        removed = self.conference_pair()[0]["papers"][-1]
        return {"snapshot_date": "2026-10-08", "checked_on": "2026-10-08", "records": [],
                "conference_records": [{key: removed[key] for key in ("title", "venue", "year", "official_url")}
                                       | {"current_admission_result": None,
                                          "reason": "Verified source abstract now contains an existing excluded application term."}]}

    def test_conference_removal_review_is_explicit_and_preserves_supplied_evidence(self):
        review = self.conference_admission_review()
        receipt = refresh.build_receipt(self.before, self.after, self.conference_pair(), SHA, "2026-10-08",
                                        review, allow_conference_refresh=True)
        self.assertEqual(receipt["layers"]["papers.json"]["removal_admission_review"], review["conference_records"])
        content = refresh.render_receipt(receipt)
        self.assertIn("摘要补全后不满足现有纳入条件（触发现有排除规则），非撤稿", content)
        self.assertIn(review["conference_records"][0]["reason"], content)
        self.assertIn(review["conference_records"][0]["official_url"], content)
        without_extra = {key: value for key, value in review.items() if key != "conference_records"}
        unchanged = refresh.build_receipt(self.before, self.after, self.conference_pair(), SHA, "2026-10-08",
                                          without_extra, allow_conference_refresh=True)
        self.assertNotIn("removal_admission_review", unchanged["layers"]["papers.json"])
        self.assertEqual(unchanged, self.build(conference=self.conference_pair(), allow_conference_refresh=True))

    def test_conference_removal_review_rejects_duplicates_nonremovals_and_missing_evidence(self):
        valid = self.conference_admission_review()
        first = valid["conference_records"][0]
        invalid = [
            {**valid, "conference_records": None},
            {**valid, "conference_records": [first, deepcopy(first)]},
            {**valid, "conference_records": [{**first, "title": "Not removed"}]},
            {**valid, "conference_records": [{**first, "venue": "ICML"}]},
            {**valid, "conference_records": [{**first, "year": 2026}]},
            {**valid, "conference_records": [{**first, "official_url": "https://example.org/not-evidence"}]},
            {**valid, "conference_records": [{**first, "reason": "  "}]},
            {**valid, "conference_records": [{**first, "current_admission_result": "admitted"}]},
        ]
        for missing in ("official_url", "reason", "current_admission_result"):
            invalid.append({**valid, "conference_records": [{key: value for key, value in first.items() if key != missing}]})
        for review in invalid:
            with self.subTest(review=review), self.assertRaises(ValueError):
                refresh.build_receipt(self.before, self.after, self.conference_pair(), SHA, "2026-10-08",
                                      review, allow_conference_refresh=True)

    def test_conference_review_requires_dual_mode_even_when_the_array_is_empty(self):
        for records in ([], self.conference_admission_review()["conference_records"]):
            review = {**self.conference_admission_review(), "conference_records": records}
            with self.subTest(records=records), self.assertRaisesRegex(ValueError, "explicit conference refresh"):
                refresh.build_receipt(self.before, self.after, (self.conference, self.conference),
                                      SHA, "2026-10-08", review)

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

    def test_cli_explicit_dual_refresh_can_write_then_check_immutable_receipts(self):
        before, after = self.conference_pair()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / refresh.CONFERENCE_SOURCE).write_text(json.dumps(after))
            (root / refresh.ARXIV_SOURCE).write_text(json.dumps(self.after))
            git_outputs = [SHA + "\n", json.dumps(self.before).encode(), json.dumps(before).encode()]
            argv = ["--baseline", "HEAD", "--date", "2026-10-08", "--allow-conference-refresh"]
            for suffix in ([], ["--check"]):
                with patch.object(refresh, "ROOT", root), patch.object(refresh.subprocess, "check_output", side_effect=git_outputs), patch("sys.stdout", new_callable=StringIO):
                    self.assertEqual(refresh.main(argv + suffix), 0)
            receipt_path = root / "data" / "catalog-refresh-2026-10-08.json"
            self.assertEqual(json.loads(receipt_path.read_text())["refresh_scope"], "conference-and-arxiv")
            changed = deepcopy(after)
            changed["papers"][0]["paper_url"] += "?new-metadata"
            (root / refresh.CONFERENCE_SOURCE).write_text(json.dumps(changed))
            saved = receipt_path.read_bytes()
            with patch.object(refresh, "ROOT", root), patch.object(refresh.subprocess, "check_output", side_effect=git_outputs), patch("sys.stderr", new_callable=StringIO):
                self.assertEqual(refresh.main(argv), 1)
            self.assertEqual(receipt_path.read_bytes(), saved)


if __name__ == "__main__":
    unittest.main()
