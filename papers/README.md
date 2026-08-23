# Embodied AI Conference Census · 具身智能顶会论文普查

> 3,724 conference papers · 21,411 recent arXiv papers · 7 directions · 40 subfields · 160 specialties · updated 2026-08-07

这是一份按明确规则生成的系统性会议普查：固定顶会、年份、检索词、标题分类规则和排除项均可审计。它覆盖规则边界内的全部命中记录，但不把主观的“具身智能”包装成不存在争议的数学全集。

This is a systematic conference census under explicit venue, year, query, title-taxonomy, and exclusion rules. It includes every record admitted by that reproducible boundary; it does not pretend that Embodied AI has a universally agreed semantic perimeter.

## Three-level taxonomy · 三级研究分类

Every record is organized as **research direction → subfield → specialty**. Open the [complete bilingual taxonomy and 200 leaf paper catalogs](taxonomy/README.md), or use any subfield link to open the exact interactive view.

每条记录均按**一级研究方向 → 二级子领域 → 三级专题**组织。可查看[完整双语分类图谱与 200 个最细论文目录](taxonomy/README.md)，并从任一子领域直接进入对应交互视图。

## Coverage

| Venue | Papers | Venue | Papers |
|---|---:|---|---:|
| RSS | 112 | CoRL | 282 |
| ICRA | 1,419 | IROS | 1,560 |
| ICLR | 72 | ICML | 38 |
| NeurIPS | 79 | CVPR | 87 |
| ICCV | 52 | ECCV | 23 |

## Direction coverage · 方向覆盖

| Research direction | Conference | arXiv 2024-01-01–2026-08-07 | Years | Direction catalogs |
|---|---:|---:|---|---|
| Foundation Models & VLA · 基础模型与 VLA | 318 | 3,276 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/foundation-models-vla.md) · [arXiv](arxiv/foundation-models-vla/README.md) |
| Manipulation & Imitation · 操作与模仿学习 | 941 | 3,817 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/manipulation-imitation.md) · [arXiv](arxiv/manipulation-imitation/README.md) |
| Dexterity & Teleoperation · 灵巧操作与遥操作 | 339 | 935 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/dexterity-teleoperation.md) · [arXiv](arxiv/dexterity-teleoperation/README.md) |
| Navigation & Embodied Agents · 导航与具身智能体 | 807 | 5,989 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/navigation-embodied-agents.md) · [arXiv](arxiv/navigation-embodied-agents/README.md) |
| Humanoids & Locomotion · 人形机器人与运动控制 | 670 | 2,317 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/humanoids-locomotion.md) · [arXiv](arxiv/humanoids-locomotion/README.md) |
| Perception & World Models · 感知与世界模型 | 317 | 2,154 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/perception-world-models.md) · [arXiv](arxiv/perception-world-models/README.md) |
| Simulation, Data & Evaluation · 仿真、数据与评测 | 332 | 2,923 | 2022 · 2023 · 2024 · 2025 · 2026 · arXiv 2024-01-01–2026-08-07 | [Conference](tracks/simulation-data-evaluation.md) · [arXiv](arxiv/simulation-data-evaluation/README.md) |

## Provenance · 来源层级

| Source tier | Records | Meaning |
|---|---:|---|
| Official | 74 | Manually verified proceedings or conference page |
| Publisher | 3,577 | DOI or publisher record |
| Bibliographic | 73 | DBLP or Semantic Scholar index when no publisher URL is exposed |
| arXiv | 21,411 | Official arXiv abstract and PDF pages; preprints are not presented as conference acceptances |

## Discovery ledger · 检索账本

| Venue | Query-matched | Taxonomy-admitted | Final catalog |
|---|---:|---:|---:|
| RSS | 223 | 104 | 112 |
| CoRL | 505 | 275 | 282 |
| ICRA | 3,599 | 1,418 | 1,419 |
| IROS | 3,923 | 1,561 | 1,560 |
| ICLR | 220 | 64 | 72 |
| ICML | 160 | 34 | 38 |
| NeurIPS | 379 | 77 | 79 |
| CVPR | 300 | 83 | 87 |
| ICCV | 174 | 52 | 52 |
| ECCV | 89 | 23 | 23 |

## Census boundary · 普查边界

- Window: 2022–2026, inclusive; the final year is an in-progress snapshot frozen at 2026-08-07.
- Venues: RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV.
- Discovery: Semantic Scholar bulk venue search with the query `robot`.
- Admission: deterministic title taxonomy in `scripts/sync_conference_census.py`; medical and rehabilitation terms are excluded.
- Deduplication: normalized title; the 74 manually verified seed records override discovered duplicates.
- Every entry has an online paper link and a provenance link. Provenance tiers are shown explicitly instead of calling every bibliographic index an official acceptance page.
- Recent arXiv layer: all 27,597 cs.RO candidates submitted from 2024-01-01 through 2026-08-07 were evaluated; 21,411 were admitted by the same seven-direction taxonomy.
- arXiv papers remain a separate preprint layer. A title appearing in both layers is not evidence of conference acceptance unless the conference record supplies that provenance.

---

Sources of truth: [`data/papers.json`](../data/papers.json) and [`data/arxiv_recent.json`](../data/arxiv_recent.json). Rebuild with the two sync scripts, then run `python scripts/audit_catalog.py`.
