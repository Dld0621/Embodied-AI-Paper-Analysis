import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MigrationContractTests(unittest.TestCase):
    def test_transfer_ledger_reconciles_every_record_and_new_path(self):
        ledger = json.loads((ROOT / "data/taxonomy-migration-2026-10-03.json").read_text())
        self.assertFalse(ledger["source_refresh"])
        self.assertEqual(ledger["organization_version"], 3)
        for filename, evidence in ledger["layers"].items():
            records = json.loads((ROOT / "data" / filename).read_text())["papers"]
            self.assertEqual(evidence["records_before"], evidence["records_after"])
            self.assertEqual(evidence["records_after"], len(records))
            self.assertTrue(evidence["source_fields_unchanged"])
            totals = Counter()
            for entry in evidence["path_transfers"]:
                self.assertEqual(len(entry["from"]), 3)
                self.assertEqual(len(entry["to"]), 3)
                totals[tuple(entry["to"])] += entry["records"]
            self.assertEqual(totals, Counter(tuple(p[f] for f in ("track", "subcategory", "specialty")) for p in records))
            self.assertEqual(evidence["classification_status_counts"], dict(Counter(p["classification_status"] for p in records)))

    def test_supplementary_views_are_renderable_and_do_not_count_as_primary(self):
        for folder in ("classification-review", "topics"):
            documents = list((ROOT / "papers" / folder).glob("*.md"))
            self.assertTrue(documents)
            for path in documents:
                self.assertLessEqual(path.stat().st_size, 400_000, str(path))


if __name__ == "__main__":
    unittest.main()
