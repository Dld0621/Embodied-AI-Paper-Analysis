from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_catalog", ROOT / "scripts" / "audit_catalog.py"
)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class CatalogContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = json.loads(
            (ROOT / "data" / "papers.json").read_text(encoding="utf-8")
        )
        cls.papers = cls.catalog["papers"]
        cls.arxiv = json.loads(
            (ROOT / "data" / "arxiv_recent.json").read_text(encoding="utf-8")
        )
        cls.arxiv_papers = cls.arxiv["papers"]

    def test_full_audit(self) -> None:
        errors, _ = AUDIT.validate_catalog(self.catalog)
        self.assertEqual(errors, [])

    def test_catalog_is_a_large_bounded_census(self) -> None:
        self.assertGreaterEqual(len(self.papers), 3000)
        self.assertLessEqual(len(self.papers), 5000)

    def test_recent_arxiv_full_audit(self) -> None:
        errors, _ = AUDIT.validate_arxiv(self.catalog, self.arxiv)
        self.assertEqual(errors, [])

    def test_recent_arxiv_snapshot_contract(self) -> None:
        source = self.arxiv["source"]
        self.assertEqual(source["candidate_records"], 27597)
        self.assertEqual(len(self.arxiv_papers), 21411)
        self.assertEqual(source["unclassified_records"], 6186)
        self.assertEqual(source["conference_title_duplicates"], 1393)
        self.assertEqual(source["conference_unique_title_overlap"], 1392)
        self.assertEqual(source["arxiv_normalized_title_duplicates"], 8)
        self.assertEqual(source["combined_unique_records"], 23735)
        self.assertEqual(
            self.arxiv["window"],
            {"start": "2024-01-01", "end": "2026-08-07", "years": [2024, 2025, 2026]},
        )

    def test_recent_arxiv_covers_every_direction_and_year(self) -> None:
        expected_years = {2024, 2025, 2026}
        for track in self.catalog["tracks"]:
            years = {
                paper["year"]
                for paper in self.arxiv_papers
                if paper["track"] == track
            }
            self.assertEqual(years, expected_years, track)

    def test_combined_view_prefers_conference_records(self) -> None:
        conference_titles = {
            AUDIT._combined_title_key(paper["title"]) for paper in self.papers
        }
        arxiv_titles = {
            AUDIT._combined_title_key(paper["title"]) for paper in self.arxiv_papers
        }
        self.assertEqual(len(conference_titles | arxiv_titles), 23735)

    def test_generated_arxiv_indexes_remain_github_renderable(self) -> None:
        for path in (ROOT / "papers" / "arxiv").rglob("*.md"):
            self.assertLessEqual(path.stat().st_size, 400000, str(path.relative_to(ROOT)))

    def test_rolling_five_year_window(self) -> None:
        self.assertEqual(self.catalog["schema_version"], 4)
        self.assertEqual(self.arxiv["schema_version"], 2)
        self.assertEqual(self.catalog["window"], {"start": 2022, "end": 2026})
        self.assertEqual({paper["year"] for paper in self.papers}, set(range(2022, 2027)))

    def test_every_venue_and_track_is_represented(self) -> None:
        self.assertEqual(
            {paper["venue"] for paper in self.papers}, set(self.catalog["venues"])
        )
        self.assertEqual(
            {paper["track"] for paper in self.papers}, set(self.catalog["tracks"])
        )

    def test_three_level_taxonomy_contract(self) -> None:
        taxonomy = self.catalog["taxonomy"]
        self.assertEqual(taxonomy, self.arxiv["taxonomy"])
        self.assertEqual(taxonomy["subcategory_count"], 40)
        self.assertEqual(taxonomy["specialty_count"], 160)
        declared_level_2 = {
            (track, subcategory)
            for track, track_meta in taxonomy["tracks"].items()
            for subcategory in track_meta["subcategories"]
        }
        for layer in (self.papers, self.arxiv_papers):
            observed_level_2 = {
                (paper["track"], paper["subcategory"]) for paper in layer
            }
            self.assertEqual(observed_level_2, declared_level_2)
            for paper in layer:
                subcategory_meta = taxonomy["tracks"][paper["track"]]["subcategories"][paper["subcategory"]]
                self.assertIn(paper["specialty"], subcategory_meta["specialties"])
                self.assertTrue(paper["taxonomy_evidence"])

    def test_no_ambiguous_venue_labels(self) -> None:
        for paper in self.papers:
            self.assertNotIn("/", paper["venue"])
            self.assertFalse(paper["venue"].lower().startswith("arxiv"))

    def test_latest_year_uses_official_acceptance_sources(self) -> None:
        for paper in self.papers:
            if paper["year"] == 2026:
                self.assertNotIn("arxiv.org", paper["official_url"])

    def test_every_direction_spans_all_five_years(self) -> None:
        expected = set(range(2022, 2027))
        for track in self.catalog["tracks"]:
            years = {paper["year"] for paper in self.papers if paper["track"] == track}
            self.assertEqual(years, expected, track)

    def test_every_direction_spans_multiple_major_venues(self) -> None:
        for track in self.catalog["tracks"]:
            venues = {paper["venue"] for paper in self.papers if paper["track"] == track}
            self.assertGreaterEqual(len(venues), 3, track)

    def test_every_paper_has_online_paper_and_acceptance_links(self) -> None:
        for paper in self.papers:
            for field in ("paper_url", "official_url"):
                parsed = urlparse(paper[field])
                self.assertEqual(parsed.scheme, "https", f"{paper['title']} {field}")
                self.assertTrue(parsed.netloc, f"{paper['title']} {field}")

    def test_every_paper_declares_source_provenance(self) -> None:
        allowed = {"official", "publisher", "bibliographic"}
        for paper in self.papers:
            self.assertIn(paper["source_type"], allowed, paper["title"])
            self.assertTrue(paper["discovery_source"], paper["title"])

    def test_census_records_every_venue_query(self) -> None:
        census = self.catalog["census"]
        self.assertEqual(census["query"], "robot")
        self.assertEqual(set(census["venue_discovery"]), set(self.catalog["venues"]))
        for venue, stats in census["venue_discovery"].items():
            self.assertGreaterEqual(stats["matched_records"], stats["classified_records"], venue)
            self.assertGreater(stats["included_records"], 0, venue)

    def test_research_workbench_contract(self) -> None:
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        app = (ROOT / "assets" / "app.js").read_text(encoding="utf-8")
        for marker in (
            'id="research-workbench"',
            'id="corpus-filters"',
            'id="source-filters"',
            'id="subcategory-filters"',
            'id="specialty-filters"',
            'id="saved-count"',
            'id="export-markdown"',
            'id="export-csv"',
            'id="share-view"',
        ):
            self.assertIn(marker, index)
        for marker in (
            "data/arxiv_recent.json",
            "combinedUniquePapers",
            "data-corpus",
            "subcategoryName",
            "specialtyName",
            "taxonomy_evidence",
            "URLSearchParams",
            "localStorage",
            "exportMarkdown",
            "exportCsv",
            "navigator.clipboard",
        ):
            self.assertIn(marker, app)


if __name__ == "__main__":
    unittest.main()
