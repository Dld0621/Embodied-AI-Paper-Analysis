import json
from collections import Counter
from pathlib import Path
import unittest
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from record_taxonomy_migration import source_hash


class MigrationContractTests(unittest.TestCase):
    def test_transfer_ledger_reconciles_every_record_and_new_path(self):
        ledger = json.loads(sorted((ROOT / "data").glob("taxonomy-migration-*.json"))[-1].read_text())
        self.assertFalse(ledger["source_refresh"])
        self.assertEqual(ledger["organization_version"], 4)
        for filename, evidence in ledger["layers"].items():
            records = json.loads((ROOT / "data" / filename).read_text())["papers"]
            self.assertEqual(evidence["records_before"], evidence["records_after"])
            self.assertTrue(evidence["source_fields_unchanged"])
            totals = Counter()
            for entry in evidence["path_transfers"]:
                self.assertEqual(len(entry["from"]), 3)
                self.assertEqual(len(entry["to"]), 3)
                totals[tuple(entry["to"])] += entry["records"]
            self.assertEqual(sum(totals.values()), evidence["records_after"])
            self.assertEqual(sum(evidence["classification_status_counts"].values()), evidence["records_after"])
            new_tracks = Counter()
            for path, count in totals.items():
                new_tracks[path[0]] += count
            self.assertEqual(new_tracks, evidence["new_track_counts"])
            # An immutable migration receipt applies to its source snapshot, not
            # later legitimate source refreshes. Compare live paths only if identical.
            if source_hash(records) == evidence["source_fields_sha256"]:
                self.assertEqual(totals, Counter(tuple(p[f] for f in ("track", "subcategory", "specialty")) for p in records))
                self.assertEqual(evidence["classification_status_counts"], dict(Counter(p["classification_status"] for p in records)))

    def test_supplementary_views_are_renderable_and_do_not_count_as_primary(self):
        for folder in ("classification-review", "topics"):
            documents = list((ROOT / "papers" / folder).glob("*.md"))
            self.assertTrue(documents)
            for path in documents:
                self.assertLessEqual(path.stat().st_size, 400_000, str(path))

    def test_fallback_does_not_pollute_hand_retargeting(self):
        for filename in ("papers.json", "arxiv_recent.json"):
            for p in json.loads((ROOT / "data" / filename).read_text())["papers"]:
                if p["taxonomy_evidence"] == "fallback":
                    self.assertNotEqual(p["subcategory"], "Dexterous Hand Retargeting")
                if p["subcategory"] == "Dexterous Hand Retargeting":
                    self.assertIn("Hand Retargeting", p["related_topics"])
                    self.assertEqual(p["subcategory_status"], "rule-supported")


if __name__ == "__main__":
    unittest.main()
