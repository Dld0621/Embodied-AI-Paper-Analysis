#!/usr/bin/env python3
"""Render the overview and seven direction catalogs from data/papers.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
PAPERS_DIR = ROOT / "papers"
TRACK_DIR = PAPERS_DIR / "tracks"


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def escape_cell(value: object) -> str:
    return str(value).replace("|", "&#124;").replace("\n", " ")


def source_label(paper: dict) -> str:
    return {
        "official": "Official",
        "publisher": "Publisher",
        "bibliographic": "Index",
    }[paper["source_type"]]


def render_overview(catalog: dict) -> str:
    papers = catalog["papers"]
    start = catalog["window"]["start"]
    end = catalog["window"]["end"]
    venue_counts = Counter(paper["venue"] for paper in papers)
    source_counts = Counter(paper["source_type"] for paper in papers)
    lines = [
        "# Embodied AI Conference Census · 具身智能顶会论文普查",
        "",
        f"> {len(papers):,} papers · {start}–{end} · 10 major venues · 7 research directions · updated {catalog['as_of']}",
        "",
        "这是一份按明确规则生成的系统性会议普查：固定顶会、年份、检索词、标题分类规则和排除项均可审计。它覆盖规则边界内的全部命中记录，但不把主观的“具身智能”包装成不存在争议的数学全集。",
        "",
        "This is a systematic conference census under explicit venue, year, query, title-taxonomy, and exclusion rules. It includes every record admitted by that reproducible boundary; it does not pretend that Embodied AI has a universally agreed semantic perimeter.",
        "",
        "## Coverage",
        "",
        "| Venue | Papers | Venue | Papers |",
        "|---|---:|---|---:|",
    ]
    venues = catalog["venues"]
    for index in range(0, len(venues), 2):
        left, right = venues[index], venues[index + 1]
        lines.append(f"| {left} | {venue_counts[left]:,} | {right} | {venue_counts[right]:,} |")

    lines.extend([
        "",
        "## Direction coverage · 方向覆盖",
        "",
        "| Research direction | Papers | Years | Venues | Complete catalog |",
        "|---|---:|---|---:|---|",
    ])
    for track in catalog["tracks"]:
        track_papers = [paper for paper in papers if paper["track"] == track]
        years = " · ".join(str(year) for year in sorted({paper["year"] for paper in track_papers}))
        venue_total = len({paper["venue"] for paper in track_papers})
        meta = catalog["track_meta"][track]
        path = f"tracks/{slugify(track)}.md"
        lines.append(
            f"| {track} · {meta['name_zh']} | {len(track_papers):,} | {years} | {venue_total} | [Open]({path}) |"
        )

    lines.extend([
        "",
        "## Provenance · 来源层级",
        "",
        "| Source tier | Records | Meaning |",
        "|---|---:|---|",
        f"| Official | {source_counts['official']:,} | Manually verified proceedings or conference page |",
        f"| Publisher | {source_counts['publisher']:,} | DOI or publisher record |",
        f"| Bibliographic | {source_counts['bibliographic']:,} | DBLP or Semantic Scholar index when no publisher URL is exposed |",
        "",
        "## Discovery ledger · 检索账本",
        "",
        "| Venue | Query-matched | Taxonomy-admitted | Final catalog |",
        "|---|---:|---:|---:|",
    ])
    for venue in venues:
        stats = catalog["census"]["venue_discovery"][venue]
        lines.append(
            f"| {venue} | {stats['matched_records']:,} | {stats['classified_records']:,} | {stats['included_records']:,} |"
        )

    lines.extend([
        "",
        "## Census boundary · 普查边界",
        "",
        "- Window: 2022–2026, inclusive; 2026 is an in-progress snapshot frozen at 2026-08-07.",
        "- Venues: RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV.",
        "- Discovery: Semantic Scholar bulk venue search with the query `robot`.",
        "- Admission: deterministic title taxonomy in `scripts/sync_conference_census.py`; medical and rehabilitation terms are excluded.",
        "- Deduplication: normalized title; the 74 manually verified seed records override discovered duplicates.",
        "- Every entry has an online paper link and a provenance link. Provenance tiers are shown explicitly instead of calling every bibliographic index an official acceptance page.",
        "",
        "---",
        "",
        "Source of truth: [`data/papers.json`](../data/papers.json). Rebuild with `python scripts/sync_conference_census.py`, then run `python scripts/audit_catalog.py`.",
        "",
    ])
    return "\n".join(lines)


def render_track(catalog: dict, track: str) -> str:
    meta = catalog["track_meta"][track]
    papers = sorted(
        (paper for paper in catalog["papers"] if paper["track"] == track),
        key=lambda paper: (-paper["year"], paper["venue"], paper["title"].casefold()),
    )
    venues = sorted({paper["venue"] for paper in papers})
    lines = [
        f"# {track} · {meta['name_zh']}",
        "",
        "[← Conference census](../README.md)",
        "",
        f"> {len(papers):,} papers · 2022–2026 · {len(venues)} venues",
        "",
        meta["question"],
        "",
        meta["question_zh"],
        "",
        f"**Pipeline:** `{' → '.join(meta['pipeline'])}`",
        "",
        f"**流程：** `{' → '.join(meta['pipeline_zh'])}`",
        "",
        f"**Venues:** {' · '.join(venues)}",
    ]
    for year in range(catalog["window"]["end"], catalog["window"]["start"] - 1, -1):
        year_papers = [paper for paper in papers if paper["year"] == year]
        lines.extend([
            "",
            f"## {year} ({len(year_papers):,})",
            "",
            "| Paper | Venue / topic | Online links |",
            "|---|---|---|",
        ])
        for paper in year_papers:
            links = [
                f"[Paper]({paper['paper_url']})",
                f"[{source_label(paper)}]({paper['official_url']})",
            ]
            if paper.get("code_url"):
                links.append(f"[Code]({paper['code_url']})")
            lines.append(
                f"| {escape_cell(paper['title'])} | {paper['venue']} · {escape_cell(paper['topic'])} | {' · '.join(links)} |"
            )
    lines.extend([
        "",
        "---",
        "",
        "Generated from [`data/papers.json`](../../data/papers.json). Inclusion rules are defined in [`scripts/sync_conference_census.py`](../../scripts/sync_conference_census.py).",
        "",
    ])
    return "\n".join(lines)


def render_outputs() -> dict[Path, str]:
    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    outputs = {PAPERS_DIR / "README.md": render_overview(catalog)}
    for track in catalog["tracks"]:
        outputs[TRACK_DIR / f"{slugify(track)}.md"] = render_track(catalog, track)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = render_outputs()
    stale = [path for path, rendered in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != rendered]
    if args.check:
        if stale:
            print("Generated catalogs are stale:")
            for path in stale:
                print(f"- {path.relative_to(ROOT)}")
            return 1
        print(f"Generated catalog is current ({len(outputs)} files).")
        return 0
    for path, rendered in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Rendered {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
