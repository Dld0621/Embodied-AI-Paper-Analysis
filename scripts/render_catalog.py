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
MAX_RENDER_BYTES = 390_000
WORKBENCH_URL = "https://dld0621.github.io/Embodied-AI-Paper-Analysis/"


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def arxiv_years(arxiv: dict) -> list[int]:
    """Return every calendar year touched by the rolling date window, newest first."""
    return sorted((int(year) for year in arxiv["window"]["years"]), reverse=True)


def arxiv_window_label(arxiv: dict) -> str:
    return f"{arxiv['window']['start']}–{arxiv['window']['end']}"


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


def taxonomy_leaf_path(
    track: str, subcategory: str, specialty: str, prefix: str = ""
) -> str:
    return (
        f"{prefix}{slugify(track)}/{slugify(subcategory)}/"
        f"{slugify(specialty)}/README.md"
    )


def taxonomy_query(track: str, subcategory: str, specialty: str) -> str:
    return (
        f"track={quote(track)}&subcategory={quote(subcategory)}&"
        f"specialty={quote(specialty)}"
    )


def specialty_list(
    track: str,
    subcategory: str,
    subcategory_meta: dict,
    conference_papers: list[dict],
    arxiv_papers: list[dict],
    prefix: str = "",
) -> str:
    rendered: list[str] = []
    for specialty, specialty_meta in subcategory_meta["specialties"].items():
        conference_count = sum(
            paper["track"] == track
            and paper["subcategory"] == subcategory
            and paper["specialty"] == specialty
            for paper in conference_papers
        )
        arxiv_count = sum(
            paper["track"] == track
            and paper["subcategory"] == subcategory
            and paper["specialty"] == specialty
            for paper in arxiv_papers
        )
        path = taxonomy_leaf_path(track, subcategory, specialty, prefix)
        label = escape_cell(f"{specialty} · {specialty_meta['name_zh']}")
        rendered.append(
            f"[{label}]({path}) — C {conference_count:,} · A {arxiv_count:,}"
        )
    return "<br>".join(rendered)


def taxonomy_leaf_header(
    catalog: dict,
    track: str,
    subcategory: str,
    specialty: str,
    conference_count: int,
    arxiv_count: int,
) -> list[str]:
    track_zh = catalog["track_meta"][track]["name_zh"]
    subcategory_meta = taxonomy_subcategories(catalog, track)[subcategory]
    specialty_meta = subcategory_meta["specialties"][specialty]
    query = taxonomy_query(track, subcategory, specialty)
    return [
        f"# {specialty} · {specialty_meta['name_zh']}",
        "",
        "[← Three-level taxonomy](../../../README.md)"
        f" · [Interactive workbench](../../../../../?{query}#research-workbench)",
        "",
        f"> {conference_count:,} conference papers · {arxiv_count:,} recent arXiv papers",
        "",
        "| Level | Classification |",
        "|---|---|",
        f"| 1 · Direction | {escape_cell(track)} · {escape_cell(track_zh)} |",
        f"| 2 · Subfield | {escape_cell(subcategory)} · {escape_cell(subcategory_meta['name_zh'])} |",
        f"| 3 · Specialty | {escape_cell(specialty)} · {escape_cell(specialty_meta['name_zh'])} |",
        "",
        "Conference records and arXiv preprints remain separate provenance layers. "
        "Every paper below is assigned to this single primary taxonomy path.",
        "",
        "顶会记录与 arXiv 预印本继续严格分层；下列每篇论文都只挂载到这一条主要三级分类路径。",
        "",
    ]


def render_leaf_conference_rows(papers: list[dict]) -> list[str]:
    if not papers:
        return ["No conference papers currently map to this specialty.", ""]
    lines = [
        "| Year | Paper | Venue / topic | Online links |",
        "|---:|---|---|---|",
    ]
    for paper in sorted(
        papers,
        key=lambda item: (-item["year"], item["venue"], item["title"].casefold()),
    ):
        links = [
            f"[Paper]({paper['paper_url']})",
            f"[{source_label(paper)}]({paper['official_url']})",
        ]
        if paper.get("code_url"):
            links.append(f"[Code]({paper['code_url']})")
        lines.append(
            f"| {paper['year']} | {escape_cell(paper['title'])} | "
            f"{paper['venue']} · {escape_cell(paper['topic'])} | {' · '.join(links)} |"
        )
    lines.append("")
    return lines


def render_leaf_arxiv_rows(papers: list[dict]) -> list[str]:
    if not papers:
        return ["No recent arXiv papers currently map to this specialty.", ""]
    lines = [
        "| Date | Paper | Authors | Online links |",
        "|---|---|---|---|",
    ]
    for paper in sorted(
        papers,
        key=lambda item: (item["published"], item["title"].casefold()),
        reverse=True,
    ):
        lines.append(
            f"| {paper['published']} | {escape_cell(paper['title'])} | "
            f"{display_authors(paper['authors'], limit=4)} | "
            f"[Abstract]({paper['paper_url']}) · [PDF]({paper['pdf_url']}) |"
        )
    lines.append("")
    return lines


def render_taxonomy_leaf_full(
    catalog: dict,
    track: str,
    subcategory: str,
    specialty: str,
    conference_papers: list[dict],
    arxiv_papers: list[dict],
) -> str:
    lines = taxonomy_leaf_header(
        catalog,
        track,
        subcategory,
        specialty,
        len(conference_papers),
        len(arxiv_papers),
    )
    lines.extend([
        f"## Conference papers ({len(conference_papers):,})",
        "",
    ])
    lines.extend(render_leaf_conference_rows(conference_papers))
    lines.extend([
        f"## Recent arXiv papers ({len(arxiv_papers):,})",
        "",
    ])
    lines.extend(render_leaf_arxiv_rows(arxiv_papers))
    lines.extend([
        "---",
        "",
        "Generated from the repository's audited conference and arXiv data layers.",
        "",
    ])
    return "\n".join(lines)


def render_taxonomy_leaf_partition(
    catalog: dict,
    track: str,
    subcategory: str,
    specialty: str,
    layer: str,
    period: str,
    papers: list[dict],
    part_label: str = "",
) -> str:
    specialty_meta = taxonomy_subcategories(catalog, track)[subcategory]["specialties"][specialty]
    suffix = f" · {part_label}" if part_label else ""
    lines = [
        f"# {specialty} · {specialty_meta['name_zh']} · {layer} {period}{suffix}",
        "",
        "[← Specialty index](README.md) · [Three-level taxonomy](../../../README.md)",
        "",
        f"> {len(papers):,} papers · complete list for this taxonomy leaf",
        "",
    ]
    if layer == "Conference":
        lines.extend(render_leaf_conference_rows(papers))
    else:
        lines.extend(render_leaf_arxiv_rows(papers))
    return "\n".join(lines)


def partition_leaf_page(
    catalog: dict,
    track: str,
    subcategory: str,
    specialty: str,
    layer: str,
    period: str,
    papers: list[dict],
) -> list[tuple[str, str, list[dict], str]]:
    chunks = [papers]
    while True:
        next_chunks: list[list[dict]] = []
        changed = False
        for chunk in chunks:
            preview = render_taxonomy_leaf_partition(
                catalog, track, subcategory, specialty, layer, period, chunk
            )
            if len(preview.encode("utf-8")) > MAX_RENDER_BYTES and len(chunk) > 1:
                midpoint = len(chunk) // 2
                next_chunks.extend((chunk[:midpoint], chunk[midpoint:]))
                changed = True
            else:
                next_chunks.append(chunk)
        chunks = next_chunks
        if not changed:
            break

    stem = f"{layer.casefold()}-{slugify(period)}"
    rendered_pages: list[tuple[str, str, list[dict], str]] = []
    for index, chunk in enumerate(chunks, start=1):
        part_label = f"Part {index}" if len(chunks) > 1 else ""
        filename = f"{stem}-part-{index}.md" if part_label else f"{stem}.md"
        display = f"{layer} {period}" + (f" · {part_label}" if part_label else "")
        rendered = render_taxonomy_leaf_partition(
            catalog,
            track,
            subcategory,
            specialty,
            layer,
            period,
            chunk,
            part_label,
        )
        if len(rendered.encode("utf-8")) > MAX_RENDER_BYTES:
            raise ValueError(f"Taxonomy leaf page remains too large: {filename}")
        rendered_pages.append((filename, display, chunk, rendered))
    return rendered_pages


def render_taxonomy_leaf_index(
    catalog: dict,
    track: str,
    subcategory: str,
    specialty: str,
    conference_count: int,
    arxiv_count: int,
    partitions: list[tuple[str, str, int]],
) -> str:
    lines = taxonomy_leaf_header(
        catalog,
        track,
        subcategory,
        specialty,
        conference_count,
        arxiv_count,
    )
    lines.extend([
        "This high-volume specialty is split into smaller complete lists so every page remains reliably renderable on GitHub.",
        "",
        "该专题论文较多，已拆分为多个完整列表，确保每个 GitHub 页面均可稳定渲染。",
        "",
        "## Complete paper lists · 完整论文列表",
        "",
        "| Layer / period | Papers | List |",
        "|---|---:|---|",
    ])
    for filename, display, count in partitions:
        lines.append(f"| {display} | {count:,} | [Open](./{filename}) |")
    lines.append("")
    return "\n".join(lines)


def render_taxonomy_leaf_outputs(catalog: dict, arxiv: dict) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for track in catalog["tracks"]:
        for subcategory, subcategory_meta in taxonomy_subcategories(catalog, track).items():
            for specialty in subcategory_meta["specialties"]:
                conference_papers = [
                    paper
                    for paper in catalog["papers"]
                    if paper["track"] == track
                    and paper["subcategory"] == subcategory
                    and paper["specialty"] == specialty
                ]
                arxiv_papers = [
                    paper
                    for paper in arxiv["papers"]
                    if paper["track"] == track
                    and paper["subcategory"] == subcategory
                    and paper["specialty"] == specialty
                ]
                leaf_dir = (
                    TAXONOMY_DIR
                    / slugify(track)
                    / slugify(subcategory)
                    / slugify(specialty)
                )
                full = render_taxonomy_leaf_full(
                    catalog,
                    track,
                    subcategory,
                    specialty,
                    conference_papers,
                    arxiv_papers,
                )
                if len(full.encode("utf-8")) <= MAX_RENDER_BYTES:
                    outputs[leaf_dir / "README.md"] = full
                    continue

                partition_links: list[tuple[str, str, int]] = []
                for layer, papers, years in (
                    ("Conference", conference_papers, range(catalog["window"]["end"], catalog["window"]["start"] - 1, -1)),
                    ("arXiv", arxiv_papers, arxiv_years(arxiv)),
                ):
                    for year in years:
                        year_papers = [paper for paper in papers if paper["year"] == year]
                        if not year_papers:
                            continue
                        for filename, display, chunk, rendered in partition_leaf_page(
                            catalog,
                            track,
                            subcategory,
                            specialty,
                            layer,
                            str(year),
                            year_papers,
                        ):
                            outputs[leaf_dir / filename] = rendered
                            partition_links.append((filename, display, len(chunk)))
                outputs[leaf_dir / "README.md"] = render_taxonomy_leaf_index(
                    catalog,
                    track,
                    subcategory,
                    specialty,
                    len(conference_papers),
                    len(arxiv_papers),
                    partition_links,
                )
    return outputs


def render_taxonomy(catalog: dict, arxiv: dict) -> str:
    conference = catalog["papers"]
    preprints = arxiv["papers"]
    taxonomy = catalog["taxonomy"]
    lines = [
        "# Three-level Research Taxonomy · 三级研究分类",
        "",
        "[← Paper index](../README.md) · [Interactive workbench](../../#research-workbench)",
        "",
        f"> 7 directions · {taxonomy['subcategory_count']} level-2 subfields · {taxonomy['specialty_count']} named level-3 specialties · {taxonomy['specialty_count'] + taxonomy['fallback_specialty_count']} leaf paper catalogs",
        "",
        "Every paper receives one primary `direction → subfield → specialty` path. Classification is deterministic and evidence-bearing. When the stored title, topic, or abstract does not justify a named level-3 topic, the record remains **General / Cross-cutting · 综合与交叉研究** instead of receiving false precision.",
        "",
        "每篇论文只有一条主要“一级方向 → 二级子领域 → 三级专题”路径。分类规则确定且保留证据；若现有标题、主题或摘要不足以支持具体三级专题，则诚实保留为“综合与交叉研究”，避免虚假精细化。",
        "",
        "Every level-3 label below opens a leaf catalog containing all conference and arXiv papers assigned to that exact path.",
        "",
        "下方每个三级专题均可点击，并进入包含该路径下全部顶会与 arXiv 论文的最细目录。",
        "",
    ]
    for track in catalog["tracks"]:
        meta = catalog["track_meta"][track]
        lines.extend([
            f"## {track} · {meta['name_zh']}",
            "",
            "| Level-2 subfield · 二级子领域 | Conference | arXiv | Level-3 leaf catalogs · 三级论文目录 |",
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
                f"| {name} | {conference_count:,} | {arxiv_count:,} | "
                f"{specialty_list(track, subcategory, subcategory_meta, conference, preprints)} |"
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
        "Every record is organized as **research direction → subfield → specialty**. Open the [complete bilingual taxonomy and 200 leaf paper catalogs](taxonomy/README.md), or use any subfield link to open the exact interactive view.",
        "",
        "每条记录均按**一级研究方向 → 二级子领域 → 三级专题**组织。可查看[完整双语分类图谱与 200 个最细论文目录](taxonomy/README.md)，并从任一子领域直接进入对应交互视图。",
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
        f"| Research direction | Conference | arXiv {arxiv_window_label(arxiv)} | Years | Direction catalogs |",
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
            f"| {track} · {meta['name_zh']} | {len(track_papers):,} | {arxiv_total:,} | {years} · arXiv {arxiv_window_label(arxiv)} | [Conference]({path}) · [arXiv]({arxiv_path}) |"
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
        f"- Window: {catalog['window']['start']}–{catalog['window']['end']}, inclusive; the final year is an in-progress snapshot frozen at {catalog['as_of']}.",
        "- Venues: RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV.",
        "- Discovery: Semantic Scholar bulk venue search with the query `robot`.",
        "- Admission: deterministic title taxonomy in `scripts/sync_conference_census.py`; medical and rehabilitation terms are excluded.",
        "- Deduplication: normalized title; the 74 manually verified seed records override discovered duplicates.",
        "- Every entry has an online paper link and a provenance link. Provenance tiers are shown explicitly instead of calling every bibliographic index an official acceptance page.",
        f"- Recent arXiv layer: all {arxiv['source']['candidate_records']:,} cs.RO candidates submitted from {arxiv['window']['start']} through {arxiv['window']['end']} were evaluated; {len(arxiv_papers):,} were admitted by the same seven-direction taxonomy.",
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
        f"**Recent arXiv layer:** [{len(arxiv_papers):,} papers from {arxiv_window_label(arxiv)}]({arxiv_path})",
    ]
    lines.extend([
        "",
        "## Subfield map · 二级子领域",
        "",
        "| Level-2 subfield | Conference | arXiv | Level-3 leaf catalogs |",
        "|---|---:|---:|---|",
    ])
    for subcategory, subcategory_meta in taxonomy_subcategories(catalog, track).items():
        conference_count = sum(paper["subcategory"] == subcategory for paper in papers)
        arxiv_count = sum(paper["subcategory"] == subcategory for paper in arxiv_papers)
        params = f"track={quote(track)}&subcategory={quote(subcategory)}"
        name = f"[{subcategory} · {subcategory_meta['name_zh']}](../../?{params}#research-workbench)"
        lines.append(
            f"| {name} | {conference_count:,} | {arxiv_count:,} | "
            f"{specialty_list(track, subcategory, subcategory_meta, papers, arxiv_papers, '../taxonomy/')} |"
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
    conference_papers = [
        paper for paper in catalog["papers"] if paper["track"] == track
    ]
    year_counts = Counter(paper["year"] for paper in papers)
    slug = slugify(track)
    lines = [
        f"# {track} · {meta['name_zh']} · Recent arXiv",
        "",
        f"[← Direction conference catalog](../../tracks/{slug}.md) · [All directions](../../README.md)",
        "",
        f"> {len(papers):,} arXiv papers · {arxiv_window_label(arxiv)} · frozen {arxiv['as_of']}",
        "",
        meta["question"],
        "",
        meta["question_zh"],
        "",
        "## Subfield coverage · 二级子领域覆盖",
        "",
        "| Level-2 subfield | Papers | Level-3 leaf catalogs |",
        "|---|---:|---|",
    ]
    for subcategory, subcategory_meta in taxonomy_subcategories(catalog, track).items():
        subfield_count = sum(paper["subcategory"] == subcategory for paper in papers)
        params = f"corpus=arxiv&track={quote(track)}&subcategory={quote(subcategory)}"
        name = f"[{subcategory} · {subcategory_meta['name_zh']}](../../../?{params}#research-workbench)"
        lines.append(
            f"| {name} | {subfield_count:,} | "
            f"{specialty_list(track, subcategory, subcategory_meta, conference_papers, papers, '../../taxonomy/')} |"
        )
    lines.extend([
        "",
        "## Year indexes · 年份索引",
        "",
        "| Year | Papers | Complete list |",
        "|---:|---:|---|",
    ])
    for year in arxiv_years(arxiv):
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


def root_specialty_links(
    catalog: dict,
    arxiv: dict,
    track: str,
    subcategory: str,
    language: str,
) -> str:
    subcategory_meta = taxonomy_subcategories(catalog, track)[subcategory]
    links: list[str] = []
    for specialty, specialty_meta in subcategory_meta["specialties"].items():
        conference_count = sum(
            paper["track"] == track
            and paper["subcategory"] == subcategory
            and paper["specialty"] == specialty
            for paper in catalog["papers"]
        )
        arxiv_count = sum(
            paper["track"] == track
            and paper["subcategory"] == subcategory
            and paper["specialty"] == specialty
            for paper in arxiv["papers"]
        )
        label = specialty_meta["name_zh"] if language == "zh" else specialty
        path = taxonomy_leaf_path(
            track, subcategory, specialty, "papers/taxonomy/"
        )
        links.append(
            f"[{escape_cell(label)}]({path}) — C {conference_count:,} · A {arxiv_count:,}"
        )
    return "<br>".join(links)


def render_root_taxonomy_sections(
    catalog: dict, arxiv: dict, language: str
) -> list[str]:
    is_zh = language == "zh"
    lines: list[str] = []
    for index, track in enumerate(catalog["tracks"], start=1):
        meta = catalog["track_meta"][track]
        conference_papers = [
            paper for paper in catalog["papers"] if paper["track"] == track
        ]
        arxiv_papers = [
            paper for paper in arxiv["papers"] if paper["track"] == track
        ]
        subcategories = taxonomy_subcategories(catalog, track)
        leaf_count = sum(
            len(subcategory_meta["specialties"])
            for subcategory_meta in subcategories.values()
        )
        title = (
            f"{meta['name_zh']} · {track}" if is_zh else f"{track} · {meta['name_zh']}"
        )
        summary = (
            f"{len(conference_papers):,} 篇顶会 · {len(arxiv_papers):,} 篇 arXiv · "
            f"{len(subcategories)} 个二级子领域 · {leaf_count} 个最细目录"
            if is_zh
            else f"{len(conference_papers):,} conference · {len(arxiv_papers):,} arXiv · "
            f"{len(subcategories)} subfields · {leaf_count} leaf catalogs"
        )
        question = meta["question_zh"] if is_zh else meta["question"]
        pipeline = meta["pipeline_zh"] if is_zh else meta["pipeline"]
        combined_query = f"?track={quote(track)}#research-workbench"
        direction_slug = slugify(track)
        lines.extend([
            "<details>",
            f"<summary><strong>{index:02d} · {title}</strong><br><sub>{summary}</sub></summary>",
            "",
            question,
            "",
            ("**研究流程：** " if is_zh else "**Research pipeline:** ")
            + " → ".join(pipeline),
            "",
            (
                f"[打开合并论文视图]({WORKBENCH_URL}{combined_query}) · "
                f"[顶会目录](papers/tracks/{direction_slug}.md) · "
                f"[arXiv 目录](papers/arxiv/{direction_slug}/README.md)"
                if is_zh
                else f"[Open combined paper view]({WORKBENCH_URL}{combined_query}) · "
                f"[Conference catalog](papers/tracks/{direction_slug}.md) · "
                f"[arXiv catalog](papers/arxiv/{direction_slug}/README.md)"
            ),
            "",
            (
                "| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |"
                if is_zh
                else "| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |"
            ),
            "|---|---:|---:|---|",
        ])
        for subcategory, subcategory_meta in subcategories.items():
            conference_count = sum(
                paper["subcategory"] == subcategory for paper in conference_papers
            )
            arxiv_count = sum(
                paper["subcategory"] == subcategory for paper in arxiv_papers
            )
            subcategory_label = (
                f"{subcategory_meta['name_zh']}<br><sub>{subcategory}</sub>"
                if is_zh
                else f"{subcategory}<br><sub>{subcategory_meta['name_zh']}</sub>"
            )
            lines.append(
                f"| {subcategory_label} | {conference_count:,} | {arxiv_count:,} | "
                f"{root_specialty_links(catalog, arxiv, track, subcategory, language)} |"
            )
        lines.extend(["", "</details>", ""])
    return lines


def render_root_readme(catalog: dict, arxiv: dict, language: str) -> str:
    is_zh = language == "zh"
    conference_count = len(catalog["papers"])
    arxiv_count = len(arxiv["papers"])
    unique_count = arxiv["source"]["combined_unique_records"]
    taxonomy = catalog["taxonomy"]
    leaf_count = taxonomy["specialty_count"] + taxonomy["fallback_specialty_count"]
    arxiv_start = arxiv["window"]["start"]
    arxiv_end = arxiv["window"]["end"]
    conference_badge = f"{conference_count:,}".replace(",", "%2C")
    arxiv_badge = f"{arxiv_count:,}".replace(",", "%2C")
    taxonomy_badge = f"7%E2%86%92{taxonomy['subcategory_count']}%E2%86%92{leaf_count}"

    if is_zh:
        lines = [
            "<div align=\"center\">",
            "<h1>Embodied AI Paper Analysis</h1>",
            "<p><strong>构建文献地图，追溯研究证据。</strong></p>",
            "<p>面向具身智能科研工作者的双语、可审计文献基础设施</p>",
            "<p><strong><a href=\"README.md\">English</a> · 简体中文</strong></p>",
            "</div>",
            "",
            "<p align=\"center\"><img src=\"assets/research-map.svg\" width=\"100%\" alt=\"具身智能双层证据与七方向研究地图\"></p>",
            "",
            f"> 面向科研工作者的可审计论文工作台：{conference_count:,} 篇近五年顶会论文、{arxiv_count:,} 篇近三年 arXiv 预印本，按 7 个一级方向、{taxonomy['subcategory_count']} 个二级子领域和 {leaf_count} 个最细论文目录组织。",
            "",
            "<p align=\"center\">",
            "<a href=\"https://dld0621.github.io/Embodied-AI-Paper-Analysis/?lang=zh\"><img src=\"https://img.shields.io/badge/在线科研工作台-打开-2563eb?style=flat-square\" alt=\"在线科研工作台\"></a>",
            f"<a href=\"data/papers.json\"><img src=\"https://img.shields.io/badge/顶会论文-{conference_badge}-111827?style=flat-square\" alt=\"顶会论文\"></a>",
            f"<a href=\"data/arxiv_recent.json\"><img src=\"https://img.shields.io/badge/arXiv-{arxiv_badge}-b31b1b?style=flat-square\" alt=\"arXiv 预印本\"></a>",
            f"<a href=\"papers/taxonomy/README.md\"><img src=\"https://img.shields.io/badge/分类-{taxonomy_badge}-0891b2?style=flat-square\" alt=\"三级分类\"></a>",
            "</p>",
            "",
            "## 快速入口",
            "",
            "| 目标 | 入口 |",
            "|---|---|",
            "| 搜索、筛选、保存与导出论文 | [在线科研工作台](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?lang=zh#research-workbench) |",
            "| 从 7 个方向逐级浏览到最细专题 | [三级研究分类图](papers/taxonomy/README.md) |",
            "| 浏览近五年顶会层 | [顶会论文总览](papers/README.md) |",
            "| 使用机器可读数据 | [`papers.json`](data/papers.json) · [`arxiv_recent.json`](data/arxiv_recent.json) |",
            "",
            "## 项目解决什么问题",
            "",
            "本项目不是简单的论文链接集合，而是一套可复现的具身智能文献定位系统。每篇论文同时回答四个问题：它属于哪个一级研究方向、位于哪个二级子领域、落在哪个三级专题，以及这一判断来自标题、主题还是摘要中的什么证据。",
            "",
            "顶会记录与 arXiv 预印本严格分层。标题重复不会被解释为会议录用；合并视图只用于阅读去重，原始来源仍分别保留。",
            "",
            "## 两个证据层",
            "",
            "| 层级 | 时间窗口 | 记录数 | 学术含义 |",
            "|---|---|---:|---|",
            f"| 顶会普查 | {catalog['window']['start']}–{catalog['window']['end']} | {conference_count:,} | RSS、CoRL、ICRA、IROS、ICLR、ICML、NeurIPS、CVPR、ICCV、ECCV；记录附正式来源层级 |",
            f"| arXiv 预印本 | {arxiv_start} 至 {arxiv_end} | {arxiv_count:,} | 对完整 `cs.RO` 候选窗口进行分类；不代表顶会录用 |",
            f"| 合并去重视图 | 同上 | {unique_count:,} | 按归一化标题去重，优先显示已有会议来源的记录 |",
            "",
            "## 七方向三级研究地图",
            "",
            f"每篇论文只拥有一条主要的 **一级方向 → 二级子领域 → 三级专题** 路径。当前分类包含 160 个明确专题，并为 40 个二级子领域各保留一个“综合与交叉研究”落点，共 {leaf_count} 个最细目录。展开下方任一方向即可查看全部二级、三级分类及其论文数量。",
            "",
        ]
        lines.extend(render_root_taxonomy_sections(catalog, arxiv, language))
        lines.extend([
            "## 每篇论文如何定位",
            "",
            "以 `AnyDexRT` 为例，其主要路径为：",
            "",
            "> 灵巧操作与遥操作 → 重定向与人体动作 → [手部姿态重定向](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/hand-pose-retargeting/README.md)",
            "",
            "| 字段 | 作用 |",
            "|---|---|",
            "| `track` | 一级方向，决定论文处于七方向中的哪一条主线 |",
            "| `subcategory` | 二级子领域，用于区分该方向内的研究问题 |",
            "| `specialty` | 三级专题，也是论文实际挂载的最细目录 |",
            "| `taxonomy_evidence` | 记录最强匹配来自标题、主题或摘要以及对应短语 |",
            "| `source_type` | 区分官方、出版社、文献索引或 arXiv 来源 |",
            "",
            "在线工作台的每一行论文都显示可点击的完整分类路径，并提供“最细目录”入口。CSV 与 Markdown 导出也保留三级分类和分类证据。",
            "",
            "## 分类与完整性边界",
            "",
            f"- 顶会层在固定会议、年份、`robot` 检索词、确定性纳入词表和排除规则下构建。",
            f"- arXiv 层审计 {arxiv['source']['candidate_records']:,} 条 `cs.RO` 候选，其中 {arxiv_count:,} 条进入七方向，{arxiv['source']['unclassified_records']:,} 条未满足分类边界。",
            "- 证据不足时使用“综合与交叉研究”，不制造虚假的三级精度。",
            "- 每篇顶会论文和每篇 arXiv 论文在最细目录树中恰好出现一次。",
            "- “完整”指覆盖公开、可复现的操作性边界，不声称具身智能存在无争议的语义全集。",
            "",
            "## 科研工作台能力",
            "",
            "- 7 个一级方向、40 个二级子领域和 200 个最细目录逐级导航；",
            "- 顶会、arXiv 与合并去重三种研究层切换；",
            "- 标题、作者、年份、会议、方向、子领域、专题与来源联合筛选；",
            "- 可分享 URL、阅读清单、Markdown / CSV 导出、中英文与深浅主题；",
            "- 每篇论文均提供在线论文页和来源链接，缺失作者信息不会被推测。",
            "",
            "## 仓库结构",
            "",
            "```text",
            "├── index.html                         # 双语在线科研工作台",
            "├── README.md / README.zh-CN.md         # 详细英文 / 中文首页",
            "├── data/                               # 顶会层与 arXiv 层机器可读数据",
            "├── papers/taxonomy/                    # 200 个最细目录及完整论文列表",
            "├── papers/tracks/                      # 七方向顶会目录",
            "├── papers/arxiv/                       # 七方向 × 年份 arXiv 目录",
            "├── scripts/taxonomy.py                 # 二级/三级确定性分类规则",
            "├── scripts/render_catalog.py           # README 与论文目录生成器",
            "└── scripts/audit_catalog.py            # 数据、来源与挂载完整性审计",
            "```",
            "",
            "## 复现与验证",
            "",
            "```bash",
            "python scripts/apply_taxonomy.py --check",
            "python scripts/render_catalog.py",
            "python scripts/audit_catalog.py",
            "python scripts/render_catalog.py --check",
            "python scripts/check_local_links.py",
            "python -m unittest discover -s tests -v",
            "```",
            "",
            "## 每周自动更新",
            "",
            "[`.github/workflows/arxiv-weekly.yml`](.github/workflows/arxiv-weekly.yml) 每周一 02:10 UTC（北京时间 10:10）重新采集截至执行日的滚动三年 `cs.RO` 窗口。同步器在限流后保留逐页缓存并恢复抓取；仅当数据审计、分类检查、生成一致性、链接检查、单元测试和 `git diff --check` 全部通过时才提交到 `main`。arXiv 预印本始终与顶会录用层分开。",
            "",
            "## 贡献与许可",
            "",
            "提交数据或分类改进前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。仓库自有内容采用 [CC BY-NC-SA 4.0](LICENSE)；论文版权归作者和出版方所有，本项目仅提供在线链接，不重新分发 PDF。",
            "",
        ])
    else:
        lines = [
            "<div align=\"center\">",
            "<h1>Embodied AI Paper Analysis</h1>",
            "<p><strong>Map the literature. Trace the evidence.</strong></p>",
            "<p>Bilingual, auditable literature infrastructure for Embodied AI researchers</p>",
            "<p><strong>English · <a href=\"README.zh-CN.md\">简体中文</a></strong></p>",
            "</div>",
            "",
            "<p align=\"center\"><img src=\"assets/research-map.svg\" width=\"100%\" alt=\"Two evidence layers connected to a seven-direction Embodied AI research map\"></p>",
            "",
            f"> An auditable research workbench for {conference_count:,} five-year conference papers and {arxiv_count:,} recent arXiv preprints, organized into 7 directions, {taxonomy['subcategory_count']} level-2 subfields, and {leaf_count} finest-grained paper catalogs.",
            "",
            "<p align=\"center\">",
            "<a href=\"https://dld0621.github.io/Embodied-AI-Paper-Analysis/\"><img src=\"https://img.shields.io/badge/Research_workbench-open-2563eb?style=flat-square\" alt=\"Research workbench\"></a>",
            f"<a href=\"data/papers.json\"><img src=\"https://img.shields.io/badge/Conference-{conference_badge}-111827?style=flat-square\" alt=\"Conference papers\"></a>",
            f"<a href=\"data/arxiv_recent.json\"><img src=\"https://img.shields.io/badge/arXiv-{arxiv_badge}-b31b1b?style=flat-square\" alt=\"arXiv preprints\"></a>",
            f"<a href=\"papers/taxonomy/README.md\"><img src=\"https://img.shields.io/badge/Taxonomy-{taxonomy_badge}-0891b2?style=flat-square\" alt=\"Three-level taxonomy\"></a>",
            "</p>",
            "",
            "## Start here",
            "",
            "| Goal | Entry point |",
            "|---|---|",
            "| Search, filter, save, and export papers | [Interactive research workbench](https://dld0621.github.io/Embodied-AI-Paper-Analysis/#research-workbench) |",
            "| Browse from seven directions to the finest specialty | [Three-level taxonomy](papers/taxonomy/README.md) |",
            "| Browse the five-year conference layer | [Conference paper overview](papers/README.md) |",
            "| Use machine-readable data | [`papers.json`](data/papers.json) · [`arxiv_recent.json`](data/arxiv_recent.json) |",
            "",
            "## What this project provides",
            "",
            "This is not a flat list of paper links. It combines a systematic conference census with a reproducible literature-positioning system: every paper states its level-1 direction, level-2 subfield, level-3 specialty, and the title/topic/abstract evidence supporting that assignment.",
            "",
            "Conference records and arXiv preprints remain separate evidence layers. A duplicate title never implies conference acceptance; deduplication is used only for the combined reading view while both source records remain available.",
            "",
            "## Two evidence layers",
            "",
            "| Layer | Window | Records | Research meaning |",
            "|---|---|---:|---|",
            f"| Conference census | {catalog['window']['start']}–{catalog['window']['end']} | {conference_count:,} | RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV with explicit provenance tiers |",
            f"| arXiv preprints | {arxiv_start} to {arxiv_end} | {arxiv_count:,} | Classified from the complete `cs.RO` candidate window; not evidence of conference acceptance |",
            f"| Combined unique view | Same windows | {unique_count:,} | Normalized-title deduplication, preferring an available conference record for display |",
            "",
            "## Seven-direction research map",
            "",
            f"Every paper receives one primary **direction → subfield → specialty** path. The ontology contains 160 named specialties plus one scoped General / Cross-cutting leaf for each of 40 subfields, producing {leaf_count} paper destinations. Expand any direction below to inspect every level-2 and level-3 category with live paper counts.",
            "",
        ]
        lines.extend(render_root_taxonomy_sections(catalog, arxiv, language))
        lines.extend([
            "## How each paper is positioned",
            "",
            "For example, `AnyDexRT` is positioned at:",
            "",
            "> Dexterity & Teleoperation → Retargeting & Human Motion → [Hand-pose Retargeting](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/hand-pose-retargeting/README.md)",
            "",
            "| Field | Role |",
            "|---|---|",
            "| `track` | Level 1: one of the seven primary research directions |",
            "| `subcategory` | Level 2: the research problem inside that direction |",
            "| `specialty` | Level 3: the finest catalog where the paper is actually listed |",
            "| `taxonomy_evidence` | Strongest matched location and phrase from title, topic, or abstract |",
            "| `source_type` | Official, publisher, bibliographic, or arXiv provenance |",
            "",
            "Every workbench paper row exposes a clickable taxonomy breadcrumb and a direct leaf-catalog link. Markdown and CSV exports retain the three-level path and classification evidence.",
            "",
            "## Classification and completeness boundary",
            "",
            "- The conference layer uses fixed venues, years, the `robot` query, deterministic admission terms, and explicit exclusions.",
            f"- The arXiv layer audits {arxiv['source']['candidate_records']:,} `cs.RO` candidates: {arxiv_count:,} enter the seven directions and {arxiv['source']['unclassified_records']:,} remain outside the declared boundary.",
            "- When evidence is insufficient, a paper remains General / Cross-cutting instead of receiving false fine-grained precision.",
            "- Every conference record and every arXiv record appears exactly once in the leaf-catalog tree.",
            "- Completeness is relative to the published operational boundary, not an undefined universal ontology of Embodied AI.",
            "",
            "## Research workbench capabilities",
            "",
            "- Progressive navigation across 7 directions, 40 subfields, and 200 leaf catalogs;",
            "- conference, arXiv, and combined-unique research layers;",
            "- joint filtering by title, author, year, venue, direction, subfield, specialty, and provenance;",
            "- shareable URLs, local reading lists, Markdown / CSV export, English / Chinese, and light / dark themes;",
            "- online paper and source links for every record, without inventing missing author metadata.",
            "",
            "## Repository structure",
            "",
            "```text",
            "├── index.html                         # bilingual interactive workbench",
            "├── README.md / README.zh-CN.md         # detailed English / Chinese homepages",
            "├── data/                               # machine-readable conference and arXiv layers",
            "├── papers/taxonomy/                    # 200 leaf catalogs with complete paper lists",
            "├── papers/tracks/                      # seven conference direction catalogs",
            "├── papers/arxiv/                       # seven directions × yearly arXiv indexes",
            "├── scripts/taxonomy.py                 # deterministic level-2/level-3 rules",
            "├── scripts/render_catalog.py           # README and catalog generator",
            "└── scripts/audit_catalog.py            # data, provenance, and attachment audit",
            "```",
            "",
            "## Rebuild and validate",
            "",
            "```bash",
            "python scripts/apply_taxonomy.py --check",
            "python scripts/render_catalog.py",
            "python scripts/audit_catalog.py",
            "python scripts/render_catalog.py --check",
            "python scripts/check_local_links.py",
            "python -m unittest discover -s tests -v",
            "```",
            "",
            "## Weekly automation",
            "",
            "[`.github/workflows/arxiv-weekly.yml`](.github/workflows/arxiv-weekly.yml) rebuilds the execution-date-driven three-year `cs.RO` window every Monday at 02:10 UTC. The harvester resumes from a page cache after rate limits, and writes to `main` only after the data audit, taxonomy check, generated-output check, link audit, unit tests, and `git diff --check` all pass. arXiv preprints remain separate from conference-acceptance provenance.",
            "",
            "## Contributing and license",
            "",
            "Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing data or taxonomy rules. Repository-authored content uses [CC BY-NC-SA 4.0](LICENSE); paper copyrights remain with their authors and publishers, and this project links to papers without redistributing PDFs.",
            "",
        ])

    return "\n".join(lines)


def render_outputs() -> dict[Path, str]:
    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    arxiv = json.loads(ARXIV_PATH.read_text(encoding="utf-8"))
    outputs = {
        ROOT / "README.md": render_root_readme(catalog, arxiv, "en"),
        ROOT / "README.zh-CN.md": render_root_readme(catalog, arxiv, "zh"),
        PAPERS_DIR / "README.md": render_overview(catalog, arxiv),
        TAXONOMY_DIR / "README.md": render_taxonomy(catalog, arxiv),
    }
    outputs.update(render_taxonomy_leaf_outputs(catalog, arxiv))
    for track in catalog["tracks"]:
        slug = slugify(track)
        outputs[TRACK_DIR / f"{slug}.md"] = render_track(catalog, arxiv, track)
        outputs[ARXIV_DIR / slug / "README.md"] = render_arxiv_track(catalog, arxiv, track)
        for year in arxiv_years(arxiv):
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
    generated_roots = (TAXONOMY_DIR, ARXIV_DIR)
    expected_generated = {
        path
        for path in outputs
        if any(path.is_relative_to(root) for root in generated_roots)
    }
    extra_generated = [
        path
        for root in generated_roots
        if root.exists()
        for path in root.rglob("*.md")
        if path not in expected_generated
    ]
    if args.check:
        if stale or extra_generated:
            print("Generated catalogs are stale:")
            for path in stale:
                print(f"- {path.relative_to(ROOT)}")
            for path in extra_generated:
                print(f"- unexpected {path.relative_to(ROOT)}")
            return 1
        print(f"Generated catalog is current ({len(outputs)} files).")
        return 0
    for path, rendered in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8", newline="\n")
    for path in extra_generated:
        path.unlink()
    for directory in sorted(
        (path for path in TAXONOMY_DIR.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        try:
            directory.rmdir()
        except OSError:
            pass
    print(
        f"Rendered {len(outputs)} files "
        f"({len(expected_taxonomy) - 1} level-3 taxonomy pages)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
