"""Offline transport and calendar checks; no live API calls."""

from datetime import date
from io import BytesIO
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync_arxiv_recent as sync


def feed(total="0", entries=""):
    return (
        f'<feed xmlns="{sync.ATOM}" xmlns:o="{sync.OPEN_SEARCH}">'
        f"<o:totalResults>{total}</o:totalResults>{entries}</feed>"
    ).encode()


class ArxivTransportTests(unittest.TestCase):
    def test_request_identifies_project_without_personal_contact(self):
        with patch.object(sync, "urlopen", return_value=BytesIO(feed())) as request:
            result = sync.fetch_xml({"search_query": "cat:cs.RO", "max_results": 1})
        sent = request.call_args.args[0]
        self.assertEqual(sent.get_header("User-agent"), "Embodied-AI-Paper-Analysis/1.0")
        self.assertEqual(sent.get_header("Accept"), "application/atom+xml")
        self.assertEqual(result.tag, f"{{{sync.ATOM}}}feed")

    def test_valid_zero_result_feed_is_allowed(self):
        sync.validate_feed(ET.fromstring(feed()))

    def test_error_feed_is_not_an_empty_success(self):
        entry = "<entry><id>http://arxiv.org/api/errors#x</id><summary>Bad query</summary></entry>"
        with self.assertRaisesRegex(ValueError, "Bad query"):
            sync.validate_feed(ET.fromstring(feed(entries=entry)))

    def test_non_atom_response_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "non-Atom"):
            sync.validate_feed(ET.fromstring("<html/>"))

    def test_missing_or_invalid_total_is_rejected(self):
        for content in (feed("-1"), feed("unknown"), f'<feed xmlns="{sync.ATOM}"/>'.encode()):
            with self.subTest(content=content), self.assertRaisesRegex(ValueError, "totalResults"):
                sync.validate_feed(ET.fromstring(content))

    def test_invalid_feed_from_transport_fails_closed(self):
        with patch.object(sync, "urlopen", return_value=BytesIO(b"<html/>")):
            with self.assertRaises(ValueError):
                sync.fetch_xml({"search_query": "cat:cs.RO"})

    def test_leap_day_window_and_segments(self):
        self.assertEqual(sync.subtract_years(date(2024, 2, 29), 3), date(2021, 2, 28))
        self.assertEqual(
            sync.half_year_segments(date(2026, 6, 30), date(2026, 7, 1)),
            (("2026-06-30", "2026-06-30"), ("2026-07-01", "2026-07-01")),
        )


if __name__ == "__main__":
    unittest.main()
