from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


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

    def test_full_audit(self) -> None:
        errors, _ = AUDIT.validate_catalog(self.catalog)
        self.assertEqual(errors, [])

    def test_catalog_is_deliberately_curated(self) -> None:
        self.assertGreaterEqual(len(self.papers), 50)
        self.assertLessEqual(len(self.papers), 100)

    def test_rolling_five_year_window(self) -> None:
        self.assertEqual(self.catalog["window"], {"start": 2022, "end": 2026})
        self.assertEqual({paper["year"] for paper in self.papers}, set(range(2022, 2027)))

    def test_every_venue_and_track_is_represented(self) -> None:
        self.assertEqual(
            {paper["venue"] for paper in self.papers}, set(self.catalog["venues"])
        )
        self.assertEqual(
            {paper["track"] for paper in self.papers}, set(self.catalog["tracks"])
        )

    def test_no_ambiguous_venue_labels(self) -> None:
        for paper in self.papers:
            self.assertNotIn("/", paper["venue"])
            self.assertFalse(paper["venue"].lower().startswith("arxiv"))

    def test_latest_year_uses_official_acceptance_sources(self) -> None:
        for paper in self.papers:
            if paper["year"] == 2026:
                self.assertNotIn("arxiv.org", paper["official_url"])


if __name__ == "__main__":
    unittest.main()
