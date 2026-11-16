"""Guard the 2026-10-24 recovery of verified conference-index omissions."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from render_catalog import render_overview


class SeedProvenanceRefreshTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conference = json.loads((ROOT / "data/papers.json").read_text())
        cls.arxiv = json.loads((ROOT / "data/arxiv_recent.json").read_text())
        cls.review = json.loads(
            (ROOT / "data/catalog-refresh-2026-10-24-source-review.json").read_text()
        )

    def test_recovered_papers_retain_publisher_identity_and_primary_evidence(self):
        records = {p["official_url"]: p for p in self.conference["papers"]}
        self.assertEqual(self.review["recovered_records"], 3)
        for evidence in self.review["conference_recoveries"]:
            with self.subTest(title=evidence["title"]):
                paper = records[evidence["official_url"]]
                for field in ("title", "venue", "year"):
                    self.assertEqual(paper[field], evidence[field])
                self.assertEqual(paper["discovery_source"], "hand-verified seed")
                self.assertEqual(paper["source_verified_on"], self.review["checked_on"])
                self.assertIn(evidence["primary_evidence"]["url"], paper["verification_urls"])
                self.assertTrue(all(url.startswith("https://") for url in paper["verification_urls"]))
                self.assertEqual(evidence["s2_doi_check"]["http_status"], 404)
                self.assertEqual(evidence["action"], "retained_as_hand_verified_seed")
                self.assertIsNotNone(evidence["baseline_admission_result"])

    def test_overview_seed_count_is_computed_not_hardcoded(self):
        original = deepcopy(self.conference)
        count = sum(p.get("discovery_source") == "hand-verified seed" for p in original["papers"])
        self.assertIn(f"the {count:,} manually verified seed records", render_overview(original, self.arxiv))
        recovered = next(p for p in original["papers"] if p.get("discovery_source") == "hand-verified seed")
        recovered["discovery_source"] = "Semantic Scholar bulk API"
        self.assertIn(f"the {count - 1:,} manually verified seed records", render_overview(original, self.arxiv))


if __name__ == "__main__":
    unittest.main()
