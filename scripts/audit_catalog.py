#!/usr/bin/env python3
"""Validate the systematic five-year Embodied AI conference census."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "papers.json"

OFFICIAL_HOSTS = {
    "2024.ieee-icra.org",
    "doi.org",
    "eccv.ecva.net",
    "ecva.net",
    "iclr.cc",
    "ieeexplore.ieee.org",
    "openaccess.thecvf.com",
    "openreview.net",
    "proceedings.iclr.cc",
    "proceedings.mlr.press",
    "proceedings.neurips.cc",
    "roboticsproceedings.org",
    "www.ecva.net",
    "www.roboticsproceedings.org",
}
BIBLIOGRAPHIC_HOSTS = {"dblp.org", "www.semanticscholar.org"}
SOURCE_TYPES = {"official", "publisher", "bibliographic"}


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def _normalized_title(title: str) -> str:
    return " ".join(title.casefold().replace("π", "pi").split())


def validate_catalog(catalog: dict) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    papers = catalog.get("papers", [])
    venues = catalog.get("venues", [])
    tracks = catalog.get("tracks", [])
    track_meta = catalog.get("track_meta", {})
    window = catalog.get("window", {})
    start = window.get("start")
    end = window.get("end")

    if catalog.get("schema_version") != 3:
        errors.append("schema_version must be 3")
    if not isinstance(start, int) or not isinstance(end, int) or start > end:
        errors.append("window must define a valid integer start/end")
    if not isinstance(papers, list) or not papers:
        errors.append("papers must be a non-empty list")
        return errors, {}
    census = catalog.get("census", {})
    for field in ("discovery_source", "query", "classification", "taxonomy_version", "snapshot_date", "venue_discovery"):
        if not census.get(field):
            errors.append(f"census missing metadata field {field}")
    if set(census.get("venue_discovery", {})) != set(venues):
        errors.append("census venue_discovery must cover every declared venue")
    if set(track_meta) != set(tracks):
        errors.append("track_meta must define every research track exactly once")
    for track in tracks:
        meta = track_meta.get(track, {})
        for field in ("name_zh", "question", "question_zh", "pipeline", "pipeline_zh"):
            if not meta.get(field):
                errors.append(f"{track}: missing track metadata field {field}")
        if len(meta.get("pipeline", [])) != 4 or len(meta.get("pipeline_zh", [])) != 4:
            errors.append(f"{track}: pipelines must contain exactly four stages")

    title_counts: Counter[str] = Counter()
    venue_counts: Counter[str] = Counter()
    track_counts: Counter[str] = Counter()
    year_counts: Counter[int] = Counter()
    source_type_counts: Counter[str] = Counter()

    required = {
        "title", "year", "venue", "track", "topic", "paper_url",
        "official_url", "source_type", "discovery_source",
    }
    for index, paper in enumerate(papers, start=1):
        label = f"paper {index}"
        missing = sorted(required - set(paper))
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue

        title = paper["title"].strip()
        year = paper["year"]
        venue = paper["venue"]
        track = paper["track"]
        title_counts[_normalized_title(title)] += 1
        venue_counts[venue] += 1
        track_counts[track] += 1
        year_counts[year] += 1
        source_type = paper["source_type"]
        source_type_counts[source_type] += 1

        if not title or title.endswith("...") or title.endswith("…"):
            errors.append(f"{label} has an empty or truncated title")
        if not isinstance(year, int) or not (start <= year <= end):
            errors.append(f"{title}: year {year!r} is outside {start}-{end}")
        if venue not in venues:
            errors.append(f"{title}: unsupported venue {venue!r}")
        if "/" in venue or venue.lower().startswith("arxiv"):
            errors.append(f"{title}: venue must be one formal conference")
        if track not in tracks:
            errors.append(f"{title}: unsupported track {track!r}")

        for field in ("paper_url", "official_url", "code_url"):
            url = paper.get(field)
            if not url:
                continue
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{title}: {field} must be an absolute HTTPS URL")

        source_host = urlparse(paper["official_url"]).hostname or ""
        if source_type not in SOURCE_TYPES:
            errors.append(f"{title}: unsupported source_type {source_type!r}")
        elif source_type in {"official", "publisher"} and source_host not in OFFICIAL_HOSTS:
            errors.append(f"{title}: non-publisher source {source_host!r}")
        elif source_type == "bibliographic" and source_host not in BIBLIOGRAPHIC_HOSTS:
            errors.append(f"{title}: unsupported bibliographic source {source_host!r}")
        if year == end and source_host == "arxiv.org":
            errors.append(f"{title}: newest-year entry cannot use arXiv as venue evidence")

    for title, count in title_counts.items():
        if count > 1:
            errors.append(f"duplicate title: {title} ({count})")

    missing_years = [year for year in range(start, end + 1) if year_counts[year] == 0]
    if missing_years:
        errors.append(f"years without coverage: {missing_years}")
    missing_venues = [venue for venue in venues if venue_counts[venue] == 0]
    if missing_venues:
        errors.append(f"venues without coverage: {missing_venues}")
    missing_tracks = [track for track in tracks if track_counts[track] == 0]
    if missing_tracks:
        errors.append(f"tracks without coverage: {missing_tracks}")
    for venue, discovery in census.get("venue_discovery", {}).items():
        required_discovery = {"matched_records", "classified_records", "new_records", "included_records"}
        if set(discovery) != required_discovery:
            errors.append(f"{venue}: incomplete venue discovery ledger")
            continue
        if discovery["matched_records"] < discovery["classified_records"]:
            errors.append(f"{venue}: classified records exceed query matches")
        if discovery["included_records"] != venue_counts[venue]:
            errors.append(f"{venue}: discovery ledger does not match final catalog count")
    expected_years = set(range(start, end + 1))
    for track in tracks:
        track_papers = [paper for paper in papers if paper.get("track") == track]
        track_years = {paper["year"] for paper in track_papers}
        track_venues = {paper["venue"] for paper in track_papers}
        if track_years != expected_years:
            errors.append(f"{track}: must cover every year from {start} through {end}")
        if len(track_venues) < 3:
            errors.append(f"{track}: must include papers from at least three major venues")

    for relative, markers in {
        "README.md": ("2022–2026", "3,724", "systematic conference census"),
        "index.html": (
            "data/papers.json",
            "direction-grid",
            "Systematic census",
            "3724",
            "research-workbench",
            "source-filters",
            "saved-count",
            "export-markdown",
            "share-view",
        ),
        "papers/README.md": ("2022–2026", "3,724 papers", "Direction coverage"),
    }.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{relative} missing catalog marker: {marker}")

    stats: dict[str, object] = {
        "papers": len(papers),
        "years": dict(sorted(year_counts.items())),
        "venues": dict(sorted(venue_counts.items())),
        "tracks": dict(sorted(track_counts.items())),
        "official_source_hosts": len(
            {urlparse(paper["official_url"]).hostname for paper in papers}
        ),
        "source_types": dict(sorted(source_type_counts.items())),
        "discovery_records": sum(
            stats.get("matched_records", 0)
            for stats in census.get("venue_discovery", {}).values()
        ),
        "direction_year_coverage": {
            track: len({paper["year"] for paper in papers if paper["track"] == track})
            for track in tracks
        },
    }
    return errors, stats


def main() -> int:
    errors, stats = validate_catalog(load_catalog())
    if errors:
        print("Catalog audit: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Catalog audit: OK")
    for key, value in stats.items():
        print(f"- {key}: {value}")
    print("Boundary: systematic census under explicit venue, query, title-taxonomy, and exclusion rules; not a universal semantic definition.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
