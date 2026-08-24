#!/usr/bin/env python3
"""Validate the systematic five-year Embodied AI conference census."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from taxonomy import GENERAL_SPECIALTY, hierarchy_counts, taxonomy_metadata


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "papers.json"
ARXIV_PATH = ROOT / "data" / "arxiv_recent.json"
TAXONOMY_DIR = ROOT / "papers" / "taxonomy"
CONFERENCE_LEAF_LINK = re.compile(r"\[Paper\]\((https://[^)]+)\)")
ARXIV_LEAF_LINK = re.compile(r"\[Abstract\]\((https://[^)]+)\)")

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


def load_arxiv() -> dict:
    return json.loads(ARXIV_PATH.read_text(encoding="utf-8"))


def _normalized_title(title: str) -> str:
    return " ".join(title.casefold().replace("π", "pi").split())


def _combined_title_key(title: str) -> str:
    """Mirror the browser's punctuation-insensitive combined-view key."""
    return re.sub(r"[^a-z0-9]+", " ", title.casefold().replace("π", "pi")).strip()


def _taxonomy_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def validate_taxonomy_leaf_catalogs(
    catalog: dict, arxiv: dict
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    taxonomy = catalog["taxonomy"]
    expected_leaf_paths: set[Path] = set()
    for track, track_meta in taxonomy["tracks"].items():
        for subcategory, subcategory_meta in track_meta["subcategories"].items():
            for specialty in subcategory_meta["specialties"]:
                expected_leaf_paths.add(
                    TAXONOMY_DIR
                    / _taxonomy_slug(track)
                    / _taxonomy_slug(subcategory)
                    / _taxonomy_slug(specialty)
                    / "README.md"
                )
    missing = sorted(path for path in expected_leaf_paths if not path.exists())
    if missing:
        errors.append(f"taxonomy leaf catalogs missing: {len(missing)}")

    markdown_files = sorted(TAXONOMY_DIR.rglob("*.md"))
    oversized = [path for path in markdown_files if path.stat().st_size > 400_000]
    if oversized:
        errors.append(f"taxonomy Markdown files over 400 KB: {len(oversized)}")

    conference_links: Counter[str] = Counter()
    arxiv_links: Counter[str] = Counter()
    for path in markdown_files:
        if path == TAXONOMY_DIR / "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        conference_links.update(CONFERENCE_LEAF_LINK.findall(text))
        arxiv_links.update(ARXIV_LEAF_LINK.findall(text))
    expected_conference = Counter(
        paper["paper_url"] for paper in catalog["papers"]
    )
    expected_arxiv = Counter(paper["paper_url"] for paper in arxiv["papers"])
    if conference_links != expected_conference:
        errors.append("conference papers are not attached exactly once to taxonomy leaves")
    if arxiv_links != expected_arxiv:
        errors.append("arXiv papers are not attached exactly once to taxonomy leaves")

    expected_count = (
        taxonomy["specialty_count"] + taxonomy["fallback_specialty_count"]
    )
    if len(expected_leaf_paths) != expected_count:
        errors.append("taxonomy leaf path count does not match published metadata")
    return errors, {
        "leaf_catalogs": len(expected_leaf_paths),
        "taxonomy_markdown_files": len(markdown_files),
        "conference_leaf_attachments": sum(conference_links.values()),
        "arxiv_leaf_attachments": sum(arxiv_links.values()),
        "max_taxonomy_page_bytes": max(
            (path.stat().st_size for path in markdown_files), default=0
        ),
    }


def validate_taxonomy_layer(layer: dict, label: str) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    papers = layer.get("papers", [])
    expected = taxonomy_metadata()
    if layer.get("taxonomy") != expected:
        errors.append(f"{label}: published taxonomy metadata differs from scripts/taxonomy.py")
    if layer.get("taxonomy_counts") != hierarchy_counts(papers):
        errors.append(f"{label}: taxonomy count ledger is inconsistent")

    declared_level_2 = {
        (track, subcategory)
        for track, track_meta in expected["tracks"].items()
        for subcategory in track_meta["subcategories"]
    }
    observed_level_2: set[tuple[str, str]] = set()
    general_count = 0
    fallback_count = 0
    for index, paper in enumerate(papers, start=1):
        path_label = f"{label} paper {index}"
        track = paper.get("track")
        subcategory = paper.get("subcategory")
        specialty = paper.get("specialty")
        evidence = paper.get("taxonomy_evidence")
        subcategory_meta = expected["tracks"].get(track, {}).get("subcategories", {}).get(subcategory)
        if not subcategory_meta:
            errors.append(f"{path_label}: unsupported level-2 taxonomy path")
            continue
        if specialty not in subcategory_meta["specialties"]:
            errors.append(f"{path_label}: unsupported level-3 taxonomy path")
        if not isinstance(evidence, str) or not evidence:
            errors.append(f"{path_label}: missing taxonomy evidence")
        elif evidence.split(":", 1)[0] not in {"title", "topic", "abstract", "fallback"}:
            errors.append(f"{path_label}: unsupported taxonomy evidence source")
        observed_level_2.add((track, subcategory))
        general_count += specialty == GENERAL_SPECIALTY
        fallback_count += evidence == "fallback"
    if observed_level_2 != declared_level_2:
        missing = sorted(declared_level_2 - observed_level_2)
        errors.append(f"{label}: level-2 subfields without records: {missing}")
    if papers and general_count / len(papers) > 0.65:
        errors.append(f"{label}: more than 65% of papers lack named level-3 evidence")
    return errors, {
        "level_2_subfields": len(observed_level_2),
        "named_level_3_specialties": expected["specialty_count"],
        "general_cross_cutting_records": general_count,
        "fallback_records": fallback_count,
    }


def validate_catalog(catalog: dict) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    papers = catalog.get("papers", [])
    venues = catalog.get("venues", [])
    tracks = catalog.get("tracks", [])
    track_meta = catalog.get("track_meta", {})
    window = catalog.get("window", {})
    start = window.get("start")
    end = window.get("end")

    if catalog.get("schema_version") != 4:
        errors.append("schema_version must be 4")
    if not isinstance(start, int) or not isinstance(end, int) or start > end:
        errors.append("window must define a valid integer start/end")
    elif end - start != 4:
        errors.append("conference window must span exactly five calendar years")
    try:
        snapshot_date = date.fromisoformat(catalog["as_of"])
        if snapshot_date.year != end:
            errors.append("conference snapshot year must match the window end year")
    except (KeyError, TypeError, ValueError):
        errors.append("conference as_of must be a valid ISO date")
    if not isinstance(papers, list) or not papers:
        errors.append("papers must be a non-empty list")
        return errors, {}
    census = catalog.get("census", {})
    for field in ("discovery_source", "query", "classification", "taxonomy_version", "snapshot_date", "venue_discovery"):
        if not census.get(field):
            errors.append(f"census missing metadata field {field}")
    if set(census.get("venue_discovery", {})) != set(venues):
        errors.append("census venue_discovery must cover every declared venue")
    if census.get("snapshot_date") != catalog.get("as_of"):
        errors.append("conference census snapshot date must match catalog as_of")
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
        "subcategory", "specialty", "taxonomy_evidence",
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

    # The current calendar year is an in-progress conference snapshot and may
    # legitimately be empty before official programs are published.
    missing_years = [year for year in range(start, end) if year_counts[year] == 0]
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
    expected_completed_years = set(range(start, end))
    for track in tracks:
        track_papers = [paper for paper in papers if paper.get("track") == track]
        track_years = {paper["year"] for paper in track_papers}
        track_venues = {paper["venue"] for paper in track_papers}
        if not expected_completed_years.issubset(track_years):
            errors.append(f"{track}: must cover every completed year from {start} through {end - 1}")
        if len(track_venues) < 3:
            errors.append(f"{track}: must include papers from at least three major venues")

    conference_window = f"{start}–{end}"
    conference_count = f"{len(papers):,}"
    for relative, markers in {
        "README.md": (conference_window, conference_count, "systematic conference census"),
        "index.html": (
            "data/papers.json",
            "direction-grid",
            "Research the field",
            "research-workbench",
            "corpus-filters",
            "source-filters",
            "subcategory-filters",
            "specialty-filters",
            "saved-count",
            "export-markdown",
            "share-view",
        ),
        "papers/README.md": (
            conference_window,
            f"{conference_count} conference papers",
            "Direction coverage",
            "Three-level taxonomy",
        ),
        "papers/taxonomy/README.md": ("7 directions", "40 level-2 subfields", "160 named level-3 specialties", "200 leaf paper catalogs"),
    }.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{relative} missing catalog marker: {marker}")

    app = (ROOT / "assets" / "app.js").read_text(encoding="utf-8")
    for marker in ("data/arxiv_recent.json", "combinedUniquePapers", "data-corpus", "subcategoryName", "specialtyName", "taxonomy_evidence"):
        if marker not in app:
            errors.append(f"assets/app.js missing dual-layer marker: {marker}")

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
    taxonomy_errors, taxonomy_stats = validate_taxonomy_layer(catalog, "conference")
    errors.extend(taxonomy_errors)
    stats["taxonomy"] = taxonomy_stats
    return errors, stats


def validate_arxiv(catalog: dict, arxiv: dict) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    papers = arxiv.get("papers", [])
    source = arxiv.get("source", {})
    window = arxiv.get("window", {})
    tracks = catalog.get("tracks", [])
    if arxiv.get("schema_version") != 2:
        errors.append("arXiv schema_version must be 2")
    try:
        start_date = date.fromisoformat(window["start"])
        end_date = date.fromisoformat(window["end"])
        try:
            expected_start = end_date.replace(year=end_date.year - 3)
        except ValueError:
            expected_start = end_date.replace(year=end_date.year - 3, day=28)
        expected_years = set(range(start_date.year, end_date.year + 1))
        if start_date != expected_start:
            errors.append("arXiv window must span exactly three rolling years")
        if end_date > date.today() or date.today() - end_date > timedelta(days=8):
            errors.append("arXiv snapshot must be no more than eight days old")
        if window.get("years") != sorted(expected_years):
            errors.append("arXiv window years must match its inclusive calendar years")
        if arxiv.get("as_of") != window["end"] or source.get("snapshot_date") != window["end"]:
            errors.append("arXiv snapshot dates must match the rolling-window end")
    except (KeyError, TypeError, ValueError):
        start_date = end_date = date.min
        expected_years = set()
        errors.append("arXiv window must contain valid ISO start/end dates and years")
    if arxiv.get("tracks") != tracks:
        errors.append("arXiv tracks must match the conference catalog")
    if source.get("category") != "cs.RO" or "submittedDate" not in source.get("query", ""):
        errors.append("arXiv source must declare the cs.RO submitted-date query")
    if not isinstance(source.get("candidate_records"), int) or source.get("candidate_records", 0) < len(papers):
        errors.append("arXiv candidate ledger must contain at least all classified papers")
    if source.get("classified_records") != len(papers):
        errors.append("arXiv classified ledger must match papers")
    if source.get("unclassified_records") != source.get("candidate_records", 0) - len(papers):
        errors.append("arXiv unclassified ledger is inconsistent")

    conference_titles = {
        _combined_title_key(paper["title"]) for paper in catalog.get("papers", [])
    }
    arxiv_title_keys = [_combined_title_key(paper["title"]) for paper in papers]
    arxiv_unique_titles = set(arxiv_title_keys)
    expected_overlap_records = sum(key in conference_titles for key in arxiv_title_keys)
    expected_unique_overlap = len(conference_titles & arxiv_unique_titles)
    expected_arxiv_duplicates = len(arxiv_title_keys) - len(arxiv_unique_titles)
    expected_combined = len(conference_titles | arxiv_unique_titles)
    for field, expected in {
        "conference_title_duplicates": expected_overlap_records,
        "conference_unique_title_overlap": expected_unique_overlap,
        "arxiv_normalized_title_duplicates": expected_arxiv_duplicates,
        "combined_unique_records": expected_combined,
    }.items():
        if source.get(field) != expected:
            errors.append(f"arXiv {field} ledger mismatch")

    ids: Counter[str] = Counter()
    track_counts: Counter[str] = Counter()
    year_counts: Counter[int] = Counter()
    required = {
        "arxiv_id", "title", "authors", "abstract", "published", "year", "venue", "track",
        "topic", "paper_url", "pdf_url", "official_url", "source_type",
        "discovery_source", "primary_category", "subcategory", "specialty",
        "taxonomy_evidence",
    }
    for index, paper in enumerate(papers, start=1):
        label = f"arXiv paper {index}"
        missing = sorted(required - set(paper))
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue
        ids[paper["arxiv_id"]] += 1
        track_counts[paper["track"]] += 1
        year_counts[paper["year"]] += 1
        if paper["track"] not in tracks:
            errors.append(f"{paper['title']}: unsupported arXiv track")
        if paper["year"] not in expected_years:
            errors.append(f"{paper['title']}: arXiv year outside recent window")
        if not window["start"] <= paper["published"] <= window["end"]:
            errors.append(f"{paper['title']}: arXiv published date outside window")
        if paper["year"] != int(paper["published"][:4]):
            errors.append(f"{paper['title']}: arXiv year does not match published date")
        if paper["venue"] != "arXiv" or paper["source_type"] != "arxiv":
            errors.append(f"{paper['title']}: preprint must be labeled arXiv")
        if not paper["authors"] or not all(isinstance(author, str) and author for author in paper["authors"]):
            errors.append(f"{paper['title']}: arXiv authors must be declared")
        if not isinstance(paper["abstract"], str) or not paper["abstract"].strip():
            errors.append(f"{paper['title']}: arXiv abstract must be declared")
        for field in ("paper_url", "pdf_url", "official_url"):
            parsed = urlparse(paper[field])
            if parsed.scheme != "https" or parsed.hostname != "arxiv.org":
                errors.append(f"{paper['title']}: {field} must use arxiv.org HTTPS")
    duplicate_ids = [arxiv_id for arxiv_id, count in ids.items() if count > 1]
    if duplicate_ids:
        errors.append(f"duplicate arXiv ids: {len(duplicate_ids)}")
    for track in tracks:
        years = {paper["year"] for paper in papers if paper.get("track") == track}
        if years != expected_years:
            errors.append(f"{track}: recent arXiv layer must cover {sorted(expected_years)}")
        if track_counts[track] != source.get("track_counts", {}).get(track):
            errors.append(f"{track}: arXiv track ledger mismatch")
    for year in expected_years:
        if year_counts[year] != source.get("year_counts", {}).get(str(year)):
            errors.append(f"{year}: arXiv year ledger mismatch")

    stats: dict[str, object] = {
        "arxiv_candidates": source.get("candidate_records"),
        "arxiv_papers": len(papers),
        "arxiv_unclassified": source.get("unclassified_records"),
        "arxiv_conference_title_duplicates": source.get("conference_title_duplicates"),
        "combined_unique_records": source.get("combined_unique_records"),
        "arxiv_years": dict(sorted(year_counts.items())),
        "arxiv_tracks": dict(sorted(track_counts.items())),
    }
    taxonomy_errors, taxonomy_stats = validate_taxonomy_layer(arxiv, "arXiv")
    errors.extend(taxonomy_errors)
    stats["arxiv_taxonomy"] = taxonomy_stats
    return errors, stats


def main() -> int:
    catalog = load_catalog()
    errors, stats = validate_catalog(catalog)
    arxiv = load_arxiv()
    arxiv_errors, arxiv_stats = validate_arxiv(catalog, arxiv)
    errors.extend(arxiv_errors)
    stats.update(arxiv_stats)
    leaf_errors, leaf_stats = validate_taxonomy_leaf_catalogs(catalog, arxiv)
    errors.extend(leaf_errors)
    stats["taxonomy_leaf_catalogs"] = leaf_stats
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
