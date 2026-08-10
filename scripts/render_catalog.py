#!/usr/bin/env python3
"""Render conference and recent-arXiv direction catalogs from source data."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
ARXIV_PATH = ROOT / "data" / "arxiv_recent.json"
PAPERS_DIR = ROOT / "papers"
TRACK_DIR = PAPERS_DIR / "tracks"
ARXIV_DIR = PAPERS_DIR / "arxiv"
TAXONOMY_DIR = PAPERS_DIR / "taxonomy"


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def escape_cell(value: object) -> str:
    return str(value).replace("|", "&#124;").replace("\n", " ")


def source_label(paper: dict) -> str:
    return {
        "official": "Official",
        "publisher": "Publisher",
        "bibliographic": "Index",
        "arxiv": "arXiv",
    }[paper["source_type"]]


def taxonomy_subcategories(catalog: dict, track: str) -> dict:
    return catalog["taxonomy"]["tracks"][track]["subcategories"]


def specialty_list(subcategory_meta: dict) -> str:
    specialties = [
        f"{name} · {meta['name_zh']}"
        for name, meta in subcategory_meta["specialties"].items()
        if name != "General / Cross-cutting"
    ]
    return "<br>".join(escape_cell(item) for item in specialties)


def render_taxonomy(catalog: dict, arxiv: dict) -> str:
    conference = catalog["papers"]
    preprints = arxiv["papers"]
    taxonomy = catalog["taxonomy"]
    lines = [
        "# Three-level Research Taxonomy · 三级研究分类",
        "",
        "[← Paper index](../README.md) · [Interactive workbench](../../#research-workbench)",
        "",
        f"> 7 directions · {taxonomy['subcategory_count']} level-2 subfields · {taxonomy['specialty_count']} named level-3 specialties",
        "",
        "Every paper receives one primary `direction → subfield → specialty` path. Classification is deterministic and evidence-bearing. When the stored title, topic, or abstract does not justify a named level-3 topic, the record remains **General / Cross-cutting · 综合与交叉研究** instead of receiving false precision.",
        "",
        "每篇论文只有一条主要“一级方向 → 二级子领域 → 三级专题”路径。分类规则确定且保留证据；若现有标题、主题或摘要不足以支持具体三级专题，则诚实保留为“综合与交叉研究”，避免虚假精细化。",
        "",
    ]
    for track in catalog["tracks"]:
        meta = catalog["track_meta"][track]
        lines.extend([
            f"## {track} · {meta['name_zh']}",
            "",
            "| Level-2 subfield · 二级子领域 | Conference | arXiv | Named level-3 specialties · 三级专题 |",
            "|---|---:|---:|---|",
        ])
        for subcategory, subcategory_meta in taxonomy_subcategories(catalog, track).items():
            conference_count = sum(
                paper["track"] == track and paper["subcategory"] == subcategory
                for paper in conference
            )
            arxiv_count = sum(
                paper["track"] == track and paper["subcategory"] == subcategory
                for paper in preprints
            )
            params = f"track={quote(track)}&subcategory={quote(subcategory)}"
            name = f"[{subcategory} · {subcategory_meta['name_zh']}](../../?{params}#research-workbench)"
            lines.append(
                f"| {name} | {conference_count:,} | {arxiv_count:,} | {specialty_list(subcategory_meta)} |"
            )
        lines.append("")
    lines.extend([
        "## Classification contract · 分类契约",
        "",
        "- Level 1 follows each corpus layer's published admission rules.",
        "- Levels 2 and 3 use weighted title, topic, and abstract terms in [`scripts/taxonomy.py`](../../scripts/taxonomy.py).",
        "- `taxonomy_evidence` records the strongest source location and matched phrase for each paper.",
        "- Conference records and arXiv preprints remain separate provenance layers.",
        "",
        "Generated from [`data/papers.json`](../../data/papers.json) and [`data/arxiv_recent.json`](../../data/arxiv_recent.json).",
        "",
    ])
    return "\n".join(lines)


def render_overview(catalog: dict, arxiv: dict) -> str:
    papers = catalog["papers"]
    arxiv_papers = arxiv["papers"]
    start = catalog["window"]["start"]
    end = catalog["window"]["end"]
    venue_counts = Counter(paper["venue"] for paper in papers)
    source_counts = Counter(paper["source_type"] for paper in papers)
    lines = [
        "# Embodied AI Conference Census · 具身智能顶会论文普查",
        "",
        f"> {len(papers):,} conference papers · {len(arxiv_papers):,} recent arXiv papers · 7 directions · {catalog['taxonomy']['subcategory_count']} subfields · {catalog['taxonomy']['specialty_count']} specialties · updated {catalog['as_of']}",
        "",
        "这是一份按明确规则生成的系统性会议普查：固定顶会、年份、检索词、标题分类规则和排除项均可审计。它覆盖规则边界内的全部命中记录，但不把主观的“具身智能”包装成不存在争议的数学全集。",
        "",
        "This is a systematic conference census under explicit venue, year, query, title-taxonomy, and exclusion rules. It includes every record admitted by that reproducible boundary; it does not pretend that Embodied AI has a universally agreed semantic perimeter.",
        "",
        "## Three-level taxonomy · 三级研究分类",
        "",
        "Every record is organized as **research direction → subfield → specialty**. Open the [complete bilingual taxonomy](taxonomy/README.md), or use any subfield link to open the exact interactive view.",
        "",
        "每条记录均按**一级研究方向 → 二级子领域 → 三级专题**组织。可查看[完整双语分类图谱](taxonomy/README.md)，并从任一子领域直接进入对应交互视图。",
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
        "| Research direction | Conference | arXiv 2024–2026 | Years | Direction catalogs |",
        "|---|---:|---:|---|---|",
    ])
    for track in catalog["tracks"]:
        track_papers = [paper for paper in papers if paper["track"] == track]
        years = " · ".join(str(year) for year in sorted({paper["year"] for paper in track_papers}))
        venue_total = len({paper["venue"] for paper in track_papers})
        arxiv_total = sum(paper["track"] == track for paper in arxiv_papers)
        meta = catalog["track_meta"][track]
        path = f"tracks/{slugify(track)}.md"
        arxiv_path = f"arxiv/{slugify(track)}/README.md"
        lines.append(
            f"| {track} · {meta['name_zh']} | {len(track_papers):,} | {arxiv_total:,} | {years} · arXiv 2024–2026 | [Conference]({path}) · [arXiv]({arxiv_path}) |"
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
        f"| arXiv | {len(arxiv_papers):,} | Official arXiv abstract and PDF pages; preprints are not presented as conference acceptances |",
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
        f"- Recent arXiv layer: all {arxiv['source']['candidate_records']:,} cs.RO candidates submitted from 2024-01-01 through 2026-08-07 were evaluated; {len(arxiv_papers):,} were admitted by the same seven-direction taxonomy.",
        "- arXiv papers remain a separate preprint layer. A title appearing in both layers is not evidence of conference acceptance unless the conference record supplies that provenance.",
        "",
        "---",
        "",
        "Sources of truth: [`data/papers.json`](../data/papers.json) and [`data/arxiv_recent.json`](../data/arxiv_recent.json). Rebuild with the two sync scripts, then run `python scripts/audit_catalog.py`.",
        "",
    ])
    return "\n".join(lines)


def render_track(catalog: dict, arxiv: dict, track: str) -> str:
    meta = catalog["track_meta"][track]
    papers = sorted(
        (paper for paper in catalog["papers"] if paper["track"] == track),
        key=lambda paper: (-paper["year"], paper["venue"], paper["title"].casefold()),
    )
    venues = sorted({paper["venue"] for paper in papers})
    arxiv_papers = [paper for paper in arxiv["papers"] if paper["track"] == track]
    arxiv_path = f"../arxiv/{slugify(track)}/README.md"
    lines = [
        f"# {track} · {meta['name_zh']}",
        "",
        "[← Conference census](../README.md)",
        "",
        f"> {len(papers):,} conference papers · {len(arxiv_papers):,} recent arXiv papers · 2022–2026",
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
        "",
        f"**Recent arXiv layer:** [{len(arxiv_papers):,} papers from 2024–2026]({arxiv_path})",
    ]
    lines.extend([
        "",
        "## Subfield map · 二级子领域",
        "",
        "| Level-2 subfield | Conference | arXiv | Named level-3 specialties |",
        "|---|---:|---:|---|",
    ])
    for subcategory, subcategory_meta in taxonomy_subcategories(catalog, track).items():
        conference_count = sum(paper["subcategory"] == subcategory for paper in papers)
        arxiv_count = sum(paper["subcategory"] == subcategory for paper in arxiv_papers)
        params = f"track={quote(track)}&subcategory={quote(subcategory)}"
        name = f"[{subcategory} · {subcategory_meta['name_zh']}](../../?{params}#research-workbench)"
        lines.append(
            f"| {name} | {conference_count:,} | {arxiv_count:,} | {specialty_list(subcategory_meta)} |"
        )
    for year in range(catalog["window"]["end"], catalog["window"]["start"] - 1, -1):
        year_papers = [paper for paper in papers if paper["year"] == year]
        lines.extend([
            "",
            f"## {year} ({len(year_papers):,})",
            "",
            "| Paper | Venue | Subfield → specialty | Online links |",
            "|---|---|---|---|",
        ])
        for paper in year_papers:
            links = [
                f"[Paper]({paper['paper_url']})",
                f"[{source_label(paper)}]({paper['official_url']})",
            ]
            if paper.get("code_url"):
                links.append(f"[Code]({paper['code_url']})")
            lines.append(
                f"| {escape_cell(paper['title'])} | {paper['venue']} | {escape_cell(paper['subcategory'])} → {escape_cell(paper['specialty'])} | {' · '.join(links)} |"
            )
    lines.extend([
        "",
        "---",
        "",
        f"Conference records are generated from [`data/papers.json`](../../data/papers.json). The separate [{track} recent arXiv catalog]({arxiv_path}) is generated from [`data/arxiv_recent.json`](../../data/arxiv_recent.json).",
        "",
    ])
    return "\n".join(lines)


def display_authors(authors: list[str], limit: int = 6) -> str:
    shown = authors[:limit]
    suffix = " et al." if len(authors) > limit else ""
    return escape_cell(", ".join(shown) + suffix)


def render_arxiv_track(catalog: dict, arxiv: dict, track: str) -> str:
    meta = catalog["track_meta"][track]
    papers = [paper for paper in arxiv["papers"] if paper["track"] == track]
    year_counts = Counter(paper["year"] for paper in papers)
    slug = slugify(track)
    lines = [
        f"# {track} · {meta['name_zh']} · Recent arXiv",
        "",
        f"[← Direction conference catalog](../../tracks/{slug}.md) · [All directions](../../README.md)",
        "",
        f"> {len(papers):,} arXiv papers · 2024–2026 · frozen {arxiv['as_of']}",
        "",
        meta["question"],
        "",
        meta["question_zh"],
        "",
        "## Subfield coverage · 二级子领域覆盖",
        "",
        "| Level-2 subfield | Papers | Named level-3 specialties |",
        "|---|---:|---|",
    ]
    for subcategory, subcategory_meta in taxonomy_subcategories(catalog, track).items():
        subfield_count = sum(paper["subcategory"] == subcategory for paper in papers)
        params = f"corpus=arxiv&track={quote(track)}&subcategory={quote(subcategory)}"
        name = f"[{subcategory} · {subcategory_meta['name_zh']}](../../../?{params}#research-workbench)"
        lines.append(
            f"| {name} | {subfield_count:,} | {specialty_list(subcategory_meta)} |"
        )
    lines.extend([
        "",
        "## Year indexes · 年份索引",
        "",
        "| Year | Papers | Complete list |",
        "|---:|---:|---|",
    ])
    for year in (2026, 2025, 2024):
        lines.append(f"| {year} | {year_counts[year]:,} | [Open](./{year}.md) |")
    lines.extend([
        "",
        "## Scope · 范围",
        "",
        f"This direction is the deterministic subset of the {arxiv['source']['candidate_records']:,}-record arXiv cs.RO census submitted between {arxiv['window']['start']} and {arxiv['window']['end']}. It is a preprint index, not a conference-acceptance list.",
        "",
        f"本方向来自 arXiv cs.RO 近三年 {arxiv['source']['candidate_records']:,} 条候选的确定性分类结果；这是预印本索引，不代表顶会录用。",
        "",
        "Generated from [`data/arxiv_recent.json`](../../../data/arxiv_recent.json) with [`scripts/sync_arxiv_recent.py`](../../../scripts/sync_arxiv_recent.py).",
        "",
    ])
    return "\n".join(lines)


def render_arxiv_year(
    arxiv: dict,
    track: str,
    year: int,
    selected_papers: list[dict] | None = None,
    period: str | None = None,
    include_authors: bool = True,
) -> str:
    papers = sorted(
        selected_papers
        if selected_papers is not None
        else (paper for paper in arxiv["papers"] if paper["track"] == track and paper["year"] == year),
        key=lambda paper: (paper["published"], paper["title"].casefold()),
        reverse=True,
    )
    label = period or str(year)
    back_link = f"./{year}.md" if period else "./README.md"
    back_label = f"{year} index" if period else "Three-year direction index"
    lines = [
        f"# {track} · arXiv {label}",
        "",
        f"[← {back_label}]({back_link}) · [All directions](../../README.md)",
        "",
        f"> {len(papers):,} papers · official arXiv links · snapshot {arxiv['as_of']}",
        "",
    ]
    if include_authors:
        lines.extend([
            "| Paper | Authors | Date | Subfield → specialty | Links |",
            "|---|---|---|---|---|",
        ])
    else:
        lines.extend([
            "| Paper | Date | Subfield → specialty | Links |",
            "|---|---|---|---|",
        ])
    for paper in papers:
        taxonomy = f"{escape_cell(paper['subcategory'])} → {escape_cell(paper['specialty'])}"
        links = f"[Abstract]({paper['paper_url']}) · [PDF]({paper['pdf_url']})"
        if include_authors:
            lines.append(
                f"| {escape_cell(paper['title'])} | {display_authors(paper['authors'])} | {paper['published']} | {taxonomy} | {links} |"
            )
        else:
            lines.append(
                f"| {escape_cell(paper['title'])} | {paper['published']} | {taxonomy} | {links} |"
            )
    lines.extend([
        "",
        "---",
        "",
        "Preprints are indexed from arXiv and are not labeled as conference papers without separate acceptance provenance.",
        "",
    ])
    return "\n".join(lines)


def render_arxiv_year_index(
    arxiv: dict, track: str, year: int, halves: list[tuple[str, list[dict]]]
) -> str:
    lines = [
        f"# {track} · arXiv {year}",
        "",
        "[← Three-year direction index](./README.md) · [All directions](../../README.md)",
        "",
        f"> {sum(len(papers) for _, papers in halves):,} papers · split for reliable GitHub rendering · snapshot {arxiv['as_of']}",
        "",
        "| Period | Papers | Complete list |",
        "|---|---:|---|",
    ]
    for period, papers in halves:
        suffix = period.casefold()
        date_range = f"{year}-01-01 → {year}-06-30" if period == "H1" else f"{year}-07-01 → {year}-12-31"
        lines.append(f"| {period} · {date_range} | {len(papers):,} | [Open](./{year}-{suffix}.md) |")
    lines.extend([
        "",
        "Every record remains available in the interactive workbench and in `data/arxiv_recent.json`.",
        "",
    ])
    return "\n".join(lines)


def render_outputs() -> dict[Path, str]:
    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    arxiv = json.loads(ARXIV_PATH.read_text(encoding="utf-8"))
    outputs = {
        PAPERS_DIR / "README.md": render_overview(catalog, arxiv),
        TAXONOMY_DIR / "README.md": render_taxonomy(catalog, arxiv),
    }
    for track in catalog["tracks"]:
        slug = slugify(track)
        outputs[TRACK_DIR / f"{slug}.md"] = render_track(catalog, arxiv, track)
        outputs[ARXIV_DIR / slug / "README.md"] = render_arxiv_track(catalog, arxiv, track)
        for year in (2026, 2025, 2024):
            year_path = ARXIV_DIR / slug / f"{year}.md"
            rendered_year = render_arxiv_year(arxiv, track, year)
            if len(rendered_year.encode("utf-8")) <= 400_000:
                outputs[year_path] = rendered_year
                continue
            year_papers = [
                paper
                for paper in arxiv["papers"]
                if paper["track"] == track and paper["year"] == year
            ]
            halves = [
                ("H1", [paper for paper in year_papers if paper["published"] <= f"{year}-06-30"]),
                ("H2", [paper for paper in year_papers if paper["published"] >= f"{year}-07-01"]),
            ]
            outputs[year_path] = render_arxiv_year_index(arxiv, track, year, halves)
            for period, papers in halves:
                outputs[ARXIV_DIR / slug / f"{year}-{period.casefold()}.md"] = render_arxiv_year(
                    arxiv, track, year, papers, f"{year} {period}", include_authors=False
                )
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
