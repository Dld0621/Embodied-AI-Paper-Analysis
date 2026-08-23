#!/usr/bin/env python3
"""Build the five-year Embodied AI conference census from bibliographic metadata.

The script queries Semantic Scholar's bulk search once per declared venue, keeps
main-venue records in the active year window, applies the repository's explicit
Embodied AI taxonomy, and merges them with the hand-verified seed catalog.

This is a discovery pipeline, not a claim that a semantic research field has a
single universally accepted boundary. Its deterministic rules are intentionally
kept in this file so additions and exclusions can be audited and reproduced.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from taxonomy import annotate_paper, hierarchy_counts, taxonomy_metadata


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "papers.json"
API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "title,abstract,year,venue,url,externalIds,openAccessPdf"

VENUE_QUERIES = {
    "RSS": ("RSS", ("robotics: science and systems",)),
    "CoRL": ("CoRL", ("conference on robot learning", "corl")),
    "ICRA": ("ICRA", ("international conference on robotics and automation", "icra")),
    "IROS": ("IROS", ("intelligent robots and systems", "iros")),
    "ICLR": ("ICLR", ("international conference on learning representations", "iclr")),
    "ICML": ("ICML", ("international conference on machine learning", "icml")),
    "NeurIPS": ("NeurIPS", ("neural information processing systems", "neurips", "nips")),
    "CVPR": ("CVPR", ("computer vision and pattern recognition", "cvpr")),
    "ICCV": ("ICCV", ("international conference on computer vision", "iccv")),
    "ECCV": ("ECCV", ("european conference on computer vision", "eccv")),
}

TRACK_RULES = {
    "Dexterity & Teleoperation": (
        "dexterous", "in-hand", "in hand", "multifinger", "multi-finger",
        "bimanual", "teleoperation", "tele-operated", "retargeting",
        "robot hand", "robotic hand", "hand-object", "haptic glove",
    ),
    "Humanoids & Locomotion": (
        "humanoid", "locomotion", "legged", "quadruped", "biped",
        "gait", "parkour", "loco-manipulation", "whole-body", "whole body",
        "terrain traversal", "motion imitation",
    ),
    "Navigation & Embodied Agents": (
        "navigation", "embodied agent", "mobile robot", "mobile manipulation",
        "object-goal", "object goal", "visual-language navigation", "vln",
        "exploration", "spatial memory", "path planning", "semantic mapping",
    ),
    "Foundation Models & VLA": (
        "vision-language-action", "vision language action", "vla", "foundation model",
        "large language model", "language model", "llm", "vision-language model",
        "vision language model", "vlm", "language-conditioned", "instruction following",
        "multimodal policy", "in-context learning", "robot reasoning",
    ),
    "Simulation, Data & Evaluation": (
        "simulation", "simulator", "sim-to-real", "sim2real", "synthetic data",
        "dataset", "benchmark", "data collection", "digital twin", "physics engine",
        "domain randomization", "evaluation protocol", "demonstration dataset",
    ),
    "Manipulation & Imitation": (
        "manipulation", "grasp", "pick-and-place", "pick and place", "assembly",
        "imitation learning", "behavior cloning", "behaviour cloning", "visuomotor",
        "contact-rich", "contact rich", "object rearrangement", "skill learning",
    ),
    "Perception & World Models": (
        "tactile", "robot perception", "active perception", "world model",
        "dynamics model", "affordance", "object pose", "3d scene", "scene graph",
        "state estimation", "visual representation",
    ),
}

EXCLUDED_TERMS = (
    "surgical", "surgery", "endoscopic", "endoscopy", "catheter", "ultrasound",
    "rehabilitation", "prosthetic", "prosthesis", "dental", "biopsy",
)

GENERAL_AI_VENUES = {"ICLR", "ICML", "NeurIPS", "CVPR", "ICCV", "ECCV"}
PHYSICAL_TITLE_ANCHORS = (
    "robot", "robotic", "embodied", "manipulation", "navigation", "locomotion",
    "humanoid", "tactile", "visuomotor", "grasp", "hand-object", "hand object",
    "sim-to-real", "sim2real", "world model", "affordance", "mobile agent",
)


def normalized_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.casefold().replace("π", "pi")).strip()


def venue_matches(value: str, aliases: tuple[str, ...]) -> bool:
    normalized = value.casefold().replace("ieee/rsj ", "").replace("ieee ", "")
    return any(alias in normalized for alias in aliases)


def infer_year(record: dict[str, Any]) -> int | None:
    external = record.get("externalIds") or {}
    dblp = external.get("DBLP") or ""
    if dblp.startswith("conf/"):
        match = re.search(r"(22|23|24|25|26)[a-z]?\d*$", dblp)
        if match:
            return 2000 + int(match.group(1))
    doi = external.get("DOI") or ""
    match = re.search(r"(?:^|[./_-])(202[2-6])(?:[./_-]|$)", doi)
    if match:
        return int(match.group(1))
    year = record.get("year")
    return year if isinstance(year, int) else None


def term_score(text: str, terms: tuple[str, ...]) -> tuple[int, str | None]:
    matches = [term for term in terms if term in text]
    return len(matches), matches[0] if matches else None


def classify(record: dict[str, Any], venue: str) -> tuple[str, str] | None:
    title = (record.get("title") or "").casefold()
    abstract = (record.get("abstract") or "").casefold()
    combined = f"{title} {abstract}"
    if not title or any(term in combined for term in EXCLUDED_TERMS):
        return None

    if venue in GENERAL_AI_VENUES and not any(term in title for term in PHYSICAL_TITLE_ANCHORS):
        return None

    ranked: list[tuple[int, int, str, str]] = []
    for priority, (track, terms) in enumerate(TRACK_RULES.items()):
        title_score, title_term = term_score(title, terms)
        score = title_score
        matched = title_term
        if matched:
            ranked.append((score, -priority, track, matched))
    if not ranked:
        return None
    score, _, track, matched = max(ranked)
    return track, matched.replace("-", " ").title()


def online_links(record: dict[str, Any]) -> tuple[str, str, str]:
    external = record.get("externalIds") or {}
    doi = external.get("DOI")
    arxiv = external.get("ArXiv")
    dblp = external.get("DBLP")
    semantic = record.get("url") or "https://www.semanticscholar.org/"
    pdf = (record.get("openAccessPdf") or {}).get("url") or ""
    if pdf.startswith("https://"):
        paper_url = pdf
    elif arxiv:
        paper_url = f"https://arxiv.org/abs/{arxiv}"
    elif doi:
        paper_url = f"https://doi.org/{doi}"
    else:
        paper_url = semantic

    if doi:
        source_url = f"https://doi.org/{doi}"
        source_type = "publisher"
    elif dblp:
        source_url = f"https://dblp.org/rec/{dblp}"
        source_type = "bibliographic"
    else:
        source_url = semantic
        source_type = "bibliographic"
    return paper_url, source_url, source_type


def get_json(params: dict[str, str], retries: int = 5) -> dict[str, Any]:
    url = f"{API}?{urlencode(params)}"
    for attempt in range(retries):
        try:
            request = Request(url, headers={"User-Agent": "Embodied-AI-Paper-Analysis/1.0"})
            with urlopen(request, timeout=60) as response:
                return json.load(response)
        except HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == retries - 1:
                raise
            time.sleep(min(2 ** attempt * 2, 30))
        except (TimeoutError, URLError):
            if attempt == retries - 1:
                raise
            time.sleep(min(2 ** attempt * 2, 30))
    raise RuntimeError("unreachable")


def fetch_venue(venue: str, query: str, aliases: tuple[str, ...], start: int, end: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    token: str | None = None
    while True:
        params = {
            "query": "robot",
            "venue": query,
            "year": f"{start}-{end}",
            "fields": FIELDS,
        }
        if token:
            params["token"] = token
        payload = get_json(params)
        page = payload.get("data") or []
        records.extend(
            record for record in page
            if venue_matches(record.get("venue") or "", aliases)
        )
        token = payload.get("token")
        if not token:
            break
        time.sleep(0.8)
    print(f"{venue}: {len(records)} venue-matched records")
    return records


def build_catalog(catalog: dict[str, Any]) -> tuple[dict[str, Any], dict[str, int]]:
    start = catalog["window"]["start"]
    end = catalog["window"]["end"]
    seeds = [
        paper for paper in catalog["papers"]
        if paper.get("discovery_source") != "Semantic Scholar bulk API"
        and start <= paper["year"] <= end
    ]
    for paper in seeds:
        paper.setdefault("source_type", "official")
        paper.setdefault("discovery_source", "hand-verified seed")

    by_title = {normalized_title(paper["title"]): paper for paper in seeds}
    stats = {"discovered": 0, "classified": 0, "added": 0}
    venue_discovery: dict[str, dict[str, int]] = {}
    seen_ids: set[str] = set()

    for venue, (query, aliases) in VENUE_QUERIES.items():
        venue_records = fetch_venue(venue, query, aliases, start, end)
        venue_classified = 0
        venue_added = 0
        for record in venue_records:
            paper_id = record.get("paperId") or ""
            if paper_id in seen_ids:
                continue
            seen_ids.add(paper_id)
            stats["discovered"] += 1
            classification = classify(record, venue)
            if not classification:
                continue
            year = infer_year(record)
            if year is None or not start <= year <= end:
                continue
            stats["classified"] += 1
            venue_classified += 1
            title = (record.get("title") or "").strip().rstrip(".")
            key = normalized_title(title)
            if not key or key in by_title:
                continue
            track, topic = classification
            paper_url, source_url, source_type = online_links(record)
            paper = annotate_paper({
                "title": title,
                "year": year,
                "venue": venue,
                "track": track,
                "topic": topic,
                "paper_url": paper_url,
                "official_url": source_url,
                "source_type": source_type,
                "discovery_source": "Semantic Scholar bulk API",
            }, record.get("abstract") or "")
            by_title[key] = paper
            stats["added"] += 1
            venue_added += 1
        venue_discovery[venue] = {
            "matched_records": len(venue_records),
            "classified_records": venue_classified,
            "new_records": venue_added,
        }

    for paper in by_title.values():
        if not all(paper.get(field) for field in ("subcategory", "specialty", "taxonomy_evidence")):
            annotate_paper(paper)
    papers = sorted(
        by_title.values(),
        key=lambda paper: (-paper["year"], paper["track"], paper["venue"], paper["title"].casefold()),
    )
    included_by_venue = Counter(paper["venue"] for paper in papers)
    for venue in venue_discovery:
        venue_discovery[venue]["included_records"] = included_by_venue[venue]
    catalog.update(
        {
            "schema_version": 4,
            "scope": (
                "Systematic conference census under the repository's explicit venue, year, "
                "Embodied AI keyword, and exclusion rules; semantically bounded rather than universal."
            ),
            "census": {
                "discovery_source": "Semantic Scholar bulk search API",
                "query": "robot",
                "classification": "Level 1 uses the title/abstract admission rules in scripts/sync_conference_census.py; levels 2 and 3 use scripts/taxonomy.py.",
                "taxonomy_version": taxonomy_metadata()["version"],
                "seed_policy": "Hand-verified records override discovered duplicates",
                "snapshot_date": catalog["as_of"],
                "venue_discovery": venue_discovery,
            },
            "taxonomy": taxonomy_metadata(),
            "taxonomy_counts": hierarchy_counts(papers),
            "papers": papers,
        }
    )
    return catalog, stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="build and compare without writing")
    parser.add_argument(
        "--as-of",
        type=date.fromisoformat,
        default=date.today(),
        help="snapshot date in YYYY-MM-DD form (defaults to today)",
    )
    args = parser.parse_args()
    original = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    original["as_of"] = args.as_of.isoformat()
    original["window"] = {"start": args.as_of.year - 4, "end": args.as_of.year}
    catalog, stats = build_catalog(original)
    rendered = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if rendered != CATALOG_PATH.read_text(encoding="utf-8"):
            print("Conference census snapshot is stale")
            return 1
    else:
        CATALOG_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(json.dumps({**stats, "total": len(catalog["papers"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
