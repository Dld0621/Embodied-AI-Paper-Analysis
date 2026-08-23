#!/usr/bin/env python3
"""Build the rolling three-year arXiv layer from the complete cs.RO window.

The discovery boundary is every arXiv record whose primary or cross-listed
category matches cs.RO and whose original submission date falls in the three
years ending on the execution date. Records are assigned to one of the seven
research directions by a deterministic title/abstract taxonomy.

The arXiv API is paged conservatively and requests are separated by at least
three seconds, following the API manual. This script is intentionally separate
from the formal-conference census so preprints are never presented as accepted
conference papers.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, timedelta
from http.client import IncompleteRead
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from sync_conference_census import EXCLUDED_TERMS, TRACK_RULES, normalized_title
from taxonomy import annotate_paper, hierarchy_counts, taxonomy_metadata


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data" / "arxiv_recent.json"
CACHE_PATH = ROOT / "data" / "arxiv_recent.sync.tmp"
CONFERENCE_PATH = ROOT / "data" / "papers.json"
API = "https://export.arxiv.org/api/query"


def subtract_years(value: date, years: int) -> date:
    """Return the same calendar date ``years`` earlier, clamping leap day."""
    try:
        return value.replace(year=value.year - years)
    except ValueError:
        return value.replace(year=value.year - years, day=28)


def half_year_segments(start: date, end: date) -> tuple[tuple[str, str], ...]:
    """Split an inclusive date window into bounded ascending API slices."""
    segments: list[tuple[str, str]] = []
    cursor = start
    while cursor <= end:
        boundary = date(cursor.year, 6, 30) if cursor.month <= 6 else date(cursor.year, 12, 31)
        segment_end = min(boundary, end)
        segments.append((cursor.isoformat(), segment_end.isoformat()))
        cursor = segment_end + timedelta(days=1)
    return tuple(segments)


SNAPSHOT_DATE = date.today()
WINDOW_START = subtract_years(SNAPSHOT_DATE, 3)
START_DATE = WINDOW_START.isoformat()
END_DATE = SNAPSHOT_DATE.isoformat()
WINDOW_YEARS = list(range(WINDOW_START.year, SNAPSHOT_DATE.year + 1))
PAGE_SIZE = 2000
REQUEST_DELAY_SECONDS = 10.0
SEGMENTS = half_year_segments(WINDOW_START, SNAPSHOT_DATE)

ATOM = "http://www.w3.org/2005/Atom"
OPEN_SEARCH = "http://a9.com/-/spec/opensearch/1.1/"
ARXIV = "http://arxiv.org/schemas/atom"
NS = {"atom": ATOM, "open": OPEN_SEARCH, "arxiv": ARXIV}

EXTRA_TRACK_RULES: dict[str, tuple[str, ...]] = {
    "Foundation Models & VLA": (
        "generalist robot", "general-purpose robot", "robot foundation",
        "robotic foundation", "large multimodal model", "multimodal language model",
        "language-guided robot", "language guided robot", "language-conditioned policy",
        "language conditioned policy", "reasoning for robots", "robot reasoning",
        "embodied reasoning", "action model", "world-action model", "world action model",
    ),
    "Manipulation & Imitation": (
        "robot manipulation", "robotic manipulation", "object manipulation",
        "grasping", "gripper", "insertion", "rearrangement", "tool use",
        "deformable object", "cloth folding", "object-centric skill", "policy learning",
        "reinforcement learning for manipulation", "learning from demonstration",
        "learning from demonstrations", "diffusion policy", "action diffusion",
    ),
    "Dexterity & Teleoperation": (
        "dexterity", "dexterous hand", "multi-fingered", "multifingered",
        "anthropomorphic hand", "tactile hand", "tactile sensing", "tactile feedback",
        "touch sensing", "hand pose retargeting", "motion retargeting", "human demonstration",
        "tele-operated", "telepresence", "bilateral teleoperation", "haptic feedback",
    ),
    "Navigation & Embodied Agents": (
        "visual navigation", "robot navigation", "autonomous navigation", "indoor navigation",
        "outdoor navigation", "motion planning", "trajectory planning", "task planning",
        "path planner", "path-planning", "slam", "localization", "mapping",
        "visual odometry", "place recognition", "embodied question answering",
        "embodied instruction", "mobile manipulation", "multi-robot planning",
    ),
    "Humanoids & Locomotion": (
        "humanoid robot", "humanoid control", "bipedal", "quadrupedal", "walking",
        "running", "whole-body control", "whole body control", "loco manipulation",
        "loco-manipulation", "motion tracking", "motion generation", "human motion",
        "legged locomotion", "agile locomotion", "terrain locomotion",
    ),
    "Perception & World Models": (
        "robot vision", "visual perception", "3d perception", "scene understanding",
        "scene reconstruction", "point cloud", "depth estimation", "pose estimation",
        "object detection", "object tracking", "semantic segmentation", "scene flow",
        "neural rendering", "occupancy prediction", "spatial perception", "sensor fusion",
        "state representation", "predictive model", "visual dynamics",
    ),
    "Simulation, Data & Evaluation": (
        "robotics dataset", "robot dataset", "large-scale dataset", "benchmarking",
        "evaluation benchmark", "simulation benchmark", "robot simulator",
        "physics simulation", "synthetic dataset", "data generation", "data engine",
        "data scaling", "sim to real", "real to sim", "digital twins",
        "domain adaptation", "domain transfer", "reproducibility", "evaluation metric",
    ),
}

TRACK_PRIORITY = (
    "Dexterity & Teleoperation",
    "Humanoids & Locomotion",
    "Foundation Models & VLA",
    "Navigation & Embodied Agents",
    "Simulation, Data & Evaluation",
    "Manipulation & Imitation",
    "Perception & World Models",
)

WEAK_ABSTRACT_TERMS = {
    "benchmark", "dataset", "evaluation", "simulation", "grasp", "exploration",
    "localization", "mapping", "tracking", "segmentation", "calibration",
    "policy learning", "representation learning", "language model", "human motion",
    "motion generation", "world model", "dynamics model", "object pose",
}


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def terms_for(track: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys((*TRACK_RULES[track], *EXTRA_TRACK_RULES[track])))


def matched_terms(text: str, terms: tuple[str, ...]) -> list[str]:
    return [term for term in terms if term in text]


def classify(title: str, abstract: str) -> tuple[str, str, str] | None:
    title_lower = title.casefold()
    abstract_lower = abstract.casefold()
    combined = f"{title_lower} {abstract_lower}"
    if not title_lower or any(term in combined for term in EXCLUDED_TERMS):
        return None

    ranked: list[tuple[int, int, str, str, str]] = []
    for priority, track in enumerate(TRACK_PRIORITY):
        terms = terms_for(track)
        title_matches = matched_terms(title_lower, terms)
        abstract_matches = matched_terms(abstract_lower, terms)
        distinct_abstract = list(dict.fromkeys(abstract_matches))
        strong_abstract = [term for term in distinct_abstract if term not in WEAK_ABSTRACT_TERMS]
        if not title_matches and len(distinct_abstract) < 2 and not strong_abstract:
            continue
        evidence = title_matches[0] if title_matches else distinct_abstract[0]
        evidence_location = "title" if title_matches else "abstract"
        score = 7 * len(set(title_matches)) + min(len(distinct_abstract), 6)
        ranked.append((score, -priority, track, evidence, evidence_location))
    if not ranked:
        return None
    _, _, track, evidence, location = max(ranked)
    topic = evidence.replace("-", " ").title()
    return track, topic, f"{location}:{evidence}"


def query_string() -> str:
    start = START_DATE.replace("-", "") + "0000"
    end = END_DATE.replace("-", "") + "2359"
    return f"cat:cs.RO AND submittedDate:[{start} TO {end}]"


def segment_query(start_date: str) -> str:
    start = start_date.replace("-", "") + "0000"
    end = END_DATE.replace("-", "") + "2359"
    return f"cat:cs.RO AND submittedDate:[{start} TO {end}]"


def fetch_xml(params: dict[str, str | int], retries: int = 12) -> ET.Element:
    url = f"{API}?{urlencode(params)}"
    for attempt in range(retries):
        retry_delay = min(10 * (attempt + 1), 60)
        try:
            request = Request(
                url,
                headers={
                    "User-Agent": "Embodied-AI-Paper-Analysis/1.0 (mailto:Steven.LI@connect.hku.hk)",
                    "Accept": "application/atom+xml",
                },
            )
            with urlopen(request, timeout=240) as response:
                return ET.fromstring(response.read())
        except HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == retries - 1:
                raise
            if error.code == 429:
                retry_after = error.headers.get("Retry-After")
                retry_delay = (
                    max(float(retry_after), 60.0)
                    if retry_after and retry_after.replace(".", "", 1).isdigit()
                    else min(60 * (attempt + 1), 180)
                )
        except (ET.ParseError, IncompleteRead, TimeoutError, URLError):
            if attempt == retries - 1:
                raise
        print(
            f"arXiv request retry {attempt + 1}/{retries} after {retry_delay:.0f}s",
            flush=True,
        )
        time.sleep(retry_delay)
    raise RuntimeError("unreachable")


def parse_entry(entry: ET.Element) -> dict[str, Any] | None:
    raw_id = clean_text(entry.findtext("atom:id", namespaces=NS))
    match = re.search(r"/abs/([^/]+?)(?:v\d+)?$", raw_id)
    if not match:
        return None
    arxiv_id = match.group(1)
    title = clean_text(entry.findtext("atom:title", namespaces=NS)).rstrip(".")
    abstract = clean_text(entry.findtext("atom:summary", namespaces=NS))
    published = clean_text(entry.findtext("atom:published", namespaces=NS))
    if not published or not START_DATE <= published[:10] <= END_DATE:
        return None
    classification = classify(title, abstract)
    if not classification:
        return None
    track, topic, _ = classification
    authors = [
        clean_text(author.findtext("atom:name", namespaces=NS))
        for author in entry.findall("atom:author", NS)
    ]
    primary = entry.find("arxiv:primary_category", NS)
    primary_category = primary.attrib.get("term", "") if primary is not None else ""
    abs_url = f"https://arxiv.org/abs/{arxiv_id}"
    return annotate_paper({
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": [author for author in authors if author],
        "published": published[:10],
        "year": int(published[:4]),
        "venue": "arXiv",
        "track": track,
        "topic": topic,
        "paper_url": abs_url,
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
        "official_url": abs_url,
        "source_type": "arxiv",
        "discovery_source": "arXiv API cs.RO census",
        "primary_category": primary_category,
    }, abstract)


def save_cache(
    segment_index: int,
    page_start: int,
    candidate_count: int,
    records: list[dict[str, Any]],
) -> None:
    payload = {
        "version": 2,
        "query": query_string(),
        "segment_index": segment_index,
        "page_start": page_start,
        "candidate_count": candidate_count,
        "records": records,
    }
    CACHE_PATH.write_text(
        json.dumps(payload, ensure_ascii=False), encoding="utf-8", newline="\n"
    )


def load_cache() -> tuple[int, int, int, list[dict[str, Any]]]:
    if not CACHE_PATH.exists():
        return 0, 0, 0, []
    try:
        payload = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return 0, 0, 0, []
    if payload.get("version") != 2 or payload.get("query") != query_string():
        return 0, 0, 0, []
    records = payload.get("records")
    if not isinstance(records, list):
        return 0, 0, 0, []
    return (
        int(payload.get("segment_index", 0)),
        int(payload.get("page_start", 0)),
        int(payload.get("candidate_count", 0)),
        records,
    )


def fetch_records(page_size: int, max_records: int | None = None) -> tuple[list[dict[str, Any]], int]:
    if max_records:
        segment_index, page_start, candidate_count, records = 0, 0, 0, []
    else:
        segment_index, page_start, candidate_count, records = load_cache()
    seen_ids = {paper["arxiv_id"] for paper in records}
    if segment_index or page_start:
        print(
            f"Resuming arXiv segment {segment_index + 1}/{len(SEGMENTS)} "
            f"at page offset {page_start:,}; candidates {candidate_count:,}; "
            f"classified {len(records):,}",
            flush=True,
        )
    for current_segment in range(segment_index, len(SEGMENTS)):
        segment_start, segment_end = SEGMENTS[current_segment]
        start = page_start if current_segment == segment_index else 0
        reached_end = False
        while not reached_end:
            requested = page_size
            if max_records:
                requested = min(page_size, max_records - candidate_count)
            if requested <= 0:
                return records, candidate_count
            root = fetch_xml(
                {
                    "search_query": segment_query(segment_start),
                    "start": start,
                    "max_results": requested,
                    "sortBy": "submittedDate",
                    "sortOrder": "ascending",
                }
            )
            entries = root.findall("atom:entry", NS)
            for entry in entries:
                published = clean_text(entry.findtext("atom:published", namespaces=NS))[:10]
                if published > segment_end:
                    reached_end = True
                    break
                if published < segment_start:
                    continue
                candidate_count += 1
                paper = parse_entry(entry)
                if paper and paper["arxiv_id"] not in seen_ids:
                    seen_ids.add(paper["arxiv_id"])
                    records.append(paper)
                if max_records and candidate_count >= max_records:
                    return records, candidate_count
            start += len(entries)
            if not max_records:
                if reached_end:
                    save_cache(current_segment + 1, 0, candidate_count, records)
                else:
                    save_cache(current_segment, start, candidate_count, records)
            print(
                f"arXiv {segment_start}..{segment_end}: offset {start:,}; "
                f"candidates {candidate_count:,}; classified {len(records):,}",
                flush=True,
            )
            if not entries:
                reached_end = True
            if not reached_end:
                time.sleep(REQUEST_DELAY_SECONDS)
        page_start = 0
    return records, candidate_count


def build_payload(records: list[dict[str, Any]], candidate_count: int) -> dict[str, Any]:
    for paper in records:
        if not all(paper.get(field) for field in ("subcategory", "specialty", "taxonomy_evidence")):
            annotate_paper(paper)
    conference = json.loads(CONFERENCE_PATH.read_text(encoding="utf-8"))
    conference_titles = {normalized_title(paper["title"]) for paper in conference["papers"]}
    arxiv_titles = [normalized_title(paper["title"]) for paper in records]
    arxiv_unique_titles = set(arxiv_titles)
    conference_overlap_records = sum(
        normalized_title(paper["title"]) in conference_titles for paper in records
    )
    conference_unique_overlap = len(arxiv_unique_titles & conference_titles)
    arxiv_title_duplicates = len(arxiv_titles) - len(arxiv_unique_titles)
    combined_unique_records = len(conference_titles | arxiv_unique_titles)
    records.sort(key=lambda paper: (-paper["year"], paper["track"], paper["title"].casefold()))
    track_counts = Counter(paper["track"] for paper in records)
    year_counts = Counter(paper["year"] for paper in records)
    return {
        "schema_version": 2,
        "as_of": END_DATE,
        "window": {"start": START_DATE, "end": END_DATE, "years": WINDOW_YEARS},
        "scope": (
            f"Every arXiv cs.RO record submitted from {START_DATE} through {END_DATE} "
            "that is admitted by the repository's deterministic seven-direction title/abstract taxonomy."
        ),
        "source": {
            "name": "arXiv API",
            "api": API,
            "api_documentation": "https://info.arxiv.org/help/api/user-manual.html",
            "query": query_string(),
            "category": "cs.RO",
            "harvest_strategy": (
                f"{len(SEGMENTS)} ascending half-year slices to remain below "
                "arXiv's unstable deep-pagination boundary"
            ),
            "candidate_records": candidate_count,
            "classified_records": len(records),
            "unclassified_records": candidate_count - len(records),
            "conference_title_duplicates": conference_overlap_records,
            "conference_unique_title_overlap": conference_unique_overlap,
            "arxiv_normalized_title_duplicates": arxiv_title_duplicates,
            "combined_unique_records": combined_unique_records,
            "classification": (
                "Level 1 uses the title/abstract admission rules in "
                "scripts/sync_arxiv_recent.py; levels 2 and 3 use scripts/taxonomy.py."
            ),
            "taxonomy_version": taxonomy_metadata()["version"],
            "snapshot_date": END_DATE,
            "track_counts": dict(sorted(track_counts.items())),
            "year_counts": {str(year): count for year, count in sorted(year_counts.items())},
        },
        "tracks": conference["tracks"],
        "taxonomy": taxonomy_metadata(),
        "taxonomy_counts": hierarchy_counts(records),
        "papers": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fetch and compare without writing")
    parser.add_argument("--page-size", type=int, default=PAGE_SIZE)
    parser.add_argument("--max-records", type=int, help="limit candidates for a development sample")
    args = parser.parse_args()
    if not 1 <= args.page_size <= 2000:
        parser.error("--page-size must be between 1 and 2000")

    records, candidate_count = fetch_records(args.page_size, args.max_records)
    payload = build_payload(records, candidate_count if not args.max_records else min(candidate_count, args.max_records))
    rendered = json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print("Recent arXiv snapshot is stale")
            return 1
    else:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        CACHE_PATH.unlink(missing_ok=True)
    print(json.dumps(payload["source"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
