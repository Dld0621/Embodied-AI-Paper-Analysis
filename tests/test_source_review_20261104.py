"""Historical evidence boundaries for the rate-limited 2026-11-04 refresh."""

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class November4SourceReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = json.loads(
            (ROOT / "data/catalog-refresh-2026-11-04-source-review.json").read_text()
        )
        cls.records = {
            paper["arxiv_id"]: paper
            for paper in json.loads((ROOT / "data/arxiv_recent.json").read_text())["papers"]
        }

    def test_partial_conference_attempts_do_not_claim_complete_freshness(self):
        review = self.review
        conference = review["conference_refresh"]
        self.assertEqual(review["refresh_scope"], "arxiv-only")
        self.assertFalse(conference["completed"])
        self.assertEqual(len(conference["attempts"]), 2)
        for attempt in conference["attempts"]:
            self.assertEqual(attempt["http_status"], 429)
            self.assertFalse(attempt["complete_source_snapshot_written"])
        self.assertEqual(conference["snapshot_before"], "2026-10-30")
        self.assertEqual(conference["snapshot_before"], conference["snapshot_after"])
        self.assertLess(conference["snapshot_after"], review["checked_on"])
        self.assertEqual(conference["records_before"], conference["records_after"])
        self.assertEqual(conference["baseline_file_sha256"], conference["current_file_sha256"])
        self.assertEqual(len(conference["baseline_file_sha256"]), 64)
        self.assertTrue(conference["source_bytes_unchanged"])
        self.assertTrue(conference["historical_seed_verification_dates_unchanged"])

    def test_successful_arxiv_review_reconciles_its_own_snapshot_ledger(self):
        arxiv = self.review["arxiv_refresh"]
        self.assertTrue(arxiv["completed"])
        self.assertTrue(arxiv["candidate_count_verified"])
        self.assertEqual(arxiv["snapshot_on"], self.review["checked_on"])
        self.assertEqual(arxiv["candidate_records"], arxiv["api_declared_candidate_records"])
        self.assertEqual(arxiv["candidate_records"],
                         arxiv["admitted_records"] + arxiv["outside_admission_rules"])

    def test_conflicting_journal_metadata_does_not_rewrite_arxiv_submission(self):
        evidence = self.review["submission_publication_distinctions"][0]
        paper = self.records[evidence["arxiv_id"]]
        self.assertEqual(paper["published"], evidence["arxiv_first_submission_on"])
        self.assertEqual(paper["published"], evidence["catalog_published_field"])
        self.assertEqual(paper["year"], evidence["catalog_year_field"])
        self.assertEqual(evidence["action"], "retain_observed_arxiv_source_fields_and_record_conflict")
        self.assertEqual(evidence["status"],
                         "journal_reference_year_conflicts_with_publisher_deposited_doi_metadata")
        self.assertIn("2006", evidence["arxiv_journal_reference_as_observed"])
        deposited = evidence["publisher_deposited_metadata"]
        self.assertEqual(deposited["published_year"], 2026)
        self.assertLess(deposited["crossref_record_created_on"], evidence["arxiv_first_submission_on"])


if __name__ == "__main__":
    unittest.main()
