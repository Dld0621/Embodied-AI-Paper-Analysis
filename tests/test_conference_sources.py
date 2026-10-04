"""Source-tier regressions for harvested conference metadata."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_conference_census import online_links, fetch_venue


class ConferenceSourceTests(unittest.TestCase):
    def test_arxiv_doi_does_not_prove_publisher_acceptance(self):
        paper, source, tier = online_links({
            "externalIds": {"DOI": "10.48550/arXiv.2501.12345", "ArXiv": "2501.12345"},
            "url": "https://www.semanticscholar.org/paper/example",
        })
        self.assertEqual(paper, "https://arxiv.org/abs/2501.12345")
        self.assertEqual(source, "https://www.semanticscholar.org/paper/example")
        self.assertEqual(tier, "bibliographic")

    def test_arxiv_doi_can_fall_back_to_dblp(self):
        _, source, tier = online_links({
            "externalIds": {"DOI": "10.48550/arxiv.2501.12345", "DBLP": "conf/example/paper"},
        })
        self.assertEqual(source, "https://dblp.org/rec/conf/example/paper")
        self.assertEqual(tier, "bibliographic")

    def test_real_publisher_doi_preserves_tier(self):
        _, source, tier = online_links({"externalIds": {"DOI": "10.1109/example"}})
        self.assertEqual(source, "https://doi.org/10.1109/example")
        self.assertEqual(tier, "publisher")

    def test_source_error_is_not_treated_as_an_empty_complete_census(self):
        with patch("sync_conference_census.get_json", return_value={"error": "rate limited"}):
            with self.assertRaisesRegex(ValueError, "census was not updated"):
                fetch_venue("RSS", "RSS", ("robotics: science and systems",), 2022, 2026)


if __name__ == "__main__":
    unittest.main()
