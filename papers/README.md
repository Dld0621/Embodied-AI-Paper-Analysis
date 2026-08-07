# Embodied AI Conference Census · 具身智能顶会论文普查

> 3,724 papers · 2022–2026 · 10 major venues · 7 research directions · updated 2026-08-07

这是一份按明确规则生成的系统性会议普查：固定顶会、年份、检索词、标题分类规则和排除项均可审计。它覆盖规则边界内的全部命中记录，但不把主观的“具身智能”包装成不存在争议的数学全集。

This is a systematic conference census under explicit venue, year, query, title-taxonomy, and exclusion rules. It includes every record admitted by that reproducible boundary; it does not pretend that Embodied AI has a universally agreed semantic perimeter.

## Coverage

| Venue | Papers | Venue | Papers |
|---|---:|---|---:|
| RSS | 112 | CoRL | 282 |
| ICRA | 1,419 | IROS | 1,560 |
| ICLR | 72 | ICML | 38 |
| NeurIPS | 79 | CVPR | 87 |
| ICCV | 52 | ECCV | 23 |

## Direction coverage · 方向覆盖

| Research direction | Papers | Years | Venues | Complete catalog |
|---|---:|---|---:|---|
| Foundation Models & VLA · 基础模型与 VLA | 318 | 2022 · 2023 · 2024 · 2025 · 2026 | 10 | [Open](tracks/foundation-models-vla.md) |
| Manipulation & Imitation · 操作与模仿学习 | 941 | 2022 · 2023 · 2024 · 2025 · 2026 | 10 | [Open](tracks/manipulation-imitation.md) |
| Dexterity & Teleoperation · 灵巧操作与遥操作 | 339 | 2022 · 2023 · 2024 · 2025 · 2026 | 10 | [Open](tracks/dexterity-teleoperation.md) |
| Navigation & Embodied Agents · 导航与具身智能体 | 807 | 2022 · 2023 · 2024 · 2025 · 2026 | 9 | [Open](tracks/navigation-embodied-agents.md) |
| Humanoids & Locomotion · 人形机器人与运动控制 | 670 | 2022 · 2023 · 2024 · 2025 · 2026 | 8 | [Open](tracks/humanoids-locomotion.md) |
| Perception & World Models · 感知与世界模型 | 317 | 2022 · 2023 · 2024 · 2025 · 2026 | 10 | [Open](tracks/perception-world-models.md) |
| Simulation, Data & Evaluation · 仿真、数据与评测 | 332 | 2022 · 2023 · 2024 · 2025 · 2026 | 10 | [Open](tracks/simulation-data-evaluation.md) |

## Provenance · 来源层级

| Source tier | Records | Meaning |
|---|---:|---|
| Official | 74 | Manually verified proceedings or conference page |
| Publisher | 3,577 | DOI or publisher record |
| Bibliographic | 73 | DBLP or Semantic Scholar index when no publisher URL is exposed |

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

- Window: 2022–2026, inclusive; 2026 is an in-progress snapshot frozen at 2026-08-07.
- Venues: RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV.
- Discovery: Semantic Scholar bulk venue search with the query `robot`.
- Admission: deterministic title taxonomy in `scripts/sync_conference_census.py`; medical and rehabilitation terms are excluded.
- Deduplication: normalized title; the 74 manually verified seed records override discovered duplicates.
- Every entry has an online paper link and a provenance link. Provenance tiers are shown explicitly instead of calling every bibliographic index an official acceptance page.

---

Source of truth: [`data/papers.json`](../data/papers.json). Rebuild with `python scripts/sync_conference_census.py`, then run `python scripts/audit_catalog.py`.
