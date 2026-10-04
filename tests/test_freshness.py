from datetime import date
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from freshness import BEGIN, END, build_status, stamp_markdown
from render_catalog import render_outputs


class FreshnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "data/papers.json").read_text())
        cls.arxiv = json.loads((ROOT / "data/arxiv_recent.json").read_text())
        cls.status = json.loads((ROOT / "data/catalog_status.json").read_text())

    def test_status_is_derived_from_current_sources_not_just_today(self):
        expected = build_status(self.catalog, self.arxiv, self.status["documents_updated_on"])
        self.assertEqual(expected, self.status)
        self.assertEqual(self.status["conference_snapshot_on"], self.catalog["as_of"])
        self.assertEqual(self.status["arxiv_snapshot_on"], self.arxiv["as_of"])

    def test_every_active_markdown_page_has_one_synchronized_date_block(self):
        outputs = render_outputs()
        for path, content in outputs.items():
            if path.suffix != ".md":
                continue
            with self.subTest(path=path):
                self.assertEqual(content.count(BEGIN), 1)
                self.assertEqual(content.count(END), 1)
                self.assertIn(f"**{self.status['documents_updated_on']}**", content)
                self.assertIn(f"**{self.catalog['as_of']}**", content)
                self.assertIn(f"**{self.arxiv['as_of']}**", content)
                self.assertEqual(path.read_text(), content)

    def test_stamping_is_idempotent_and_preserves_publication_dates(self):
        content = "# Paper\n\nPublished: 2024-01-01\n\nReviewed: 2024-02-01\n"
        stamped = stamp_markdown(content, self.status)
        self.assertEqual(stamped, stamp_markdown(stamped, self.status))
        self.assertIn("Published: 2024-01-01", stamped)
        self.assertIn("Reviewed: 2024-02-01", stamped)

    def test_history_receipts_are_not_regenerated_or_redated(self):
        outputs = render_outputs()
        for pattern in ("catalog-refresh-*.md", "taxonomy-migration-*.md"):
            for path in (ROOT / "docs").glob(pattern):
                self.assertNotIn(path, outputs)

    def test_all_nonhistorical_repository_markdown_is_date_synchronized(self):
        outputs = render_outputs()
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts or path.name.startswith(("catalog-refresh-", "taxonomy-migration-")):
                continue
            self.assertIn(path, outputs, f"active document omitted: {path.relative_to(ROOT)}")

    def test_date_cannot_hide_a_newer_source_snapshot(self):
        too_old = min(self.catalog["as_of"], self.arxiv["as_of"])
        value = date.fromisoformat(too_old)
        old = value.replace(year=value.year - 1).isoformat()
        with self.assertRaises(ValueError):
            build_status(self.catalog, self.arxiv, old)

    def test_coverage_claim_is_explicitly_bounded(self):
        report = (ROOT / "docs/coverage-report.md").read_text()
        self.assertIn("不宣称", report)
        self.assertIn("cs.RO", report)
        self.assertIn("未满足现有纳入规则", report)
        if self.status["api_candidate_count_verified"]:
            self.assertEqual(self.status["api_declared_candidate_records"], self.status["arxiv_candidates"])
