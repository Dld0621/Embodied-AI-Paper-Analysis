#!/usr/bin/env python3
"""Render papers/README.md from the audited JSON source of truth."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
OUTPUT_PATH = ROOT / "papers" / "README.md"


def render() -> str:
    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    papers = catalog["papers"]
    start = catalog["window"]["start"]
    end = catalog["window"]["end"]
    lines = [
        "# Curated Embodied AI Papers · 具身智能精选论文",
        "",
        f"> {len(papers)} curated papers · {start}–{end} · formally accepted at 10 major venues · updated {catalog['as_of']}",
        "",
        "这是一份精选导航，不是无边界的论文堆积。会议年份以正式会议为准；预印本日期不会替代录用年份。",
        "",
        "This is a selective research map, not an exhaustive census. Conference year follows the formal venue record, not the preprint date.",
        "",
        "## Coverage",
        "",
        "| Venue | Papers | Venue | Papers |",
        "|---|---:|---|---:|",
    ]
    venue_counts = Counter(paper["venue"] for paper in papers)
    venues = catalog["venues"]
    for index in range(0, len(venues), 2):
        left = venues[index]
        right = venues[index + 1]
        lines.append(
            f"| {left} | {venue_counts[left]} | {right} | {venue_counts[right]} |"
        )

    lines.extend(
        [
            "",
            "## Selection boundary · 收录边界",
            "",
            "- Core window: 2022–2026, inclusive.",
            "- Main-conference or official conference-track acceptance only.",
            "- Workshops, withdrawn submissions, under-review papers, ambiguous multi-venue labels, and arXiv-only work are excluded from the core count.",
            "- Every entry includes an official venue source; links marked `Paper` may point to arXiv or the official paper page.",
            "- 2026 coverage is frozen at 2026-08-07 and only includes decisions already visible on official proceedings or conference pages.",
        ]
    )

    for year in range(end, start - 1, -1):
        year_papers = sorted(
            (paper for paper in papers if paper["year"] == year),
            key=lambda paper: (paper["venue"], paper["title"].casefold()),
        )
        lines.extend(
            [
                "",
                f"## {year} ({len(year_papers)})",
                "",
                "| Paper | Venue | Research track | Links |",
                "|---|---|---|---|",
            ]
        )
        for paper in year_papers:
            links = [f"[Paper]({paper['paper_url']})", f"[Official]({paper['official_url']})"]
            if paper.get("code_url"):
                links.append(f"[Code]({paper['code_url']})")
            lines.append(
                f"| {paper['title']} | {paper['venue']} | {paper['track']} · {paper['topic']} | {' · '.join(links)} |"
            )

    lines.extend(
        [
            "",
            "---",
            "",
            "Source of truth: [`data/papers.json`](../data/papers.json). Run `python scripts/audit_catalog.py` before proposing changes.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = render()
    current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
    if args.check:
        if current != rendered:
            print("papers/README.md is stale; run python scripts/render_catalog.py")
            return 1
        print("Generated catalog is current.")
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Rendered {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
