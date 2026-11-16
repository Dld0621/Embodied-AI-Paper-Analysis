"""Keep verified conference provenance from regressing to a preprint index."""

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class October30SourceReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "data/papers.json").read_text())
        cls.records = {p["title"]: p for p in cls.catalog["papers"]}
        cls.review = json.loads(
            (ROOT / "data/catalog-refresh-2026-10-30-source-review.json").read_text()
        )

    def test_new_conference_admission_keeps_its_original_publication_year(self):
        additions = self.review["conference_additions"]
        self.assertEqual(len(additions), 1)
        for evidence in additions:
            paper = self.records[evidence["title"]]
            for field in ("title", "venue", "year", "official_url"):
                self.assertEqual(paper[field], evidence[field])
            self.assertEqual(paper["year"], 2024)
            self.assertEqual(paper["venue"], "RSS")
            self.assertEqual(evidence["primary_evidence"]["url"],
                             "https://www.roboticsproceedings.org/rss20/p017.html")
            self.assertNotEqual(str(paper["year"]), self.review["checked_on"][:4])

    def test_verified_acceptance_link_is_not_replaced_with_arxiv_bibliography(self):
        corrections = self.review["provenance_corrections"]
        self.assertEqual(len(corrections), 1)
        for evidence in corrections:
            paper = self.records[evidence["title"]]
            self.assertEqual(paper["year"], evidence["year"])
            self.assertEqual(paper["venue"], evidence["venue"])
            self.assertEqual(paper["official_url"], evidence["verified_official_url"])
            self.assertTrue(paper["official_url"].startswith("https://proceedings.neurips.cc/"))
            self.assertNotIn("journals/corr", paper["official_url"])
            self.assertEqual(paper["source_type"], "official")
            self.assertEqual(paper["discovery_source"], "hand-verified seed")
            self.assertEqual(paper["source_verified_on"], evidence["source_verified_on"])
            self.assertIn(paper["official_url"], paper["verification_urls"])
            self.assertEqual(evidence["action"], "promote_existing_record_to_hand_verified_seed")

    def test_source_review_reconciles_its_own_historical_snapshot(self):
        review = self.review
        self.assertEqual(review["checked_on"], "2026-10-30")
        self.assertEqual(review["checked_on"], review["snapshot_date"])
        self.assertEqual(review["conference_records_after"],
                         review["conference_records_before"] + len(review["conference_additions"])
                         - len(review["conference_removals"]))
        self.assertEqual(review["conference_records_after"],
                         review["final_seed_records"] + review["final_bulk_records"])
        self.assertIn("not full-paper review", review["scope"])


if __name__ == "__main__":
    unittest.main()
