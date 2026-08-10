# Embodied AI Paper Analysis

> 3,724 conference papers · 21,411 recent arXiv papers · 23,735 unique research records · 7 directions · 40 subfields · 160 specialties

[![Conference](https://img.shields.io/badge/Conference%20census-3%2C724-111827?style=flat-square)](data/papers.json)
[![arXiv](https://img.shields.io/badge/arXiv%202024--2026-21%2C411-b31b1b?style=flat-square)](data/arxiv_recent.json)
[![Directions](https://img.shields.io/badge/Directions-7-2563eb?style=flat-square)](papers/README.md)
[![Taxonomy](https://img.shields.io/badge/Taxonomy-7%20%E2%86%92%2040%20%E2%86%92%20160-0891b2?style=flat-square)](papers/taxonomy/README.md)
[![Website](https://img.shields.io/badge/Research%20workbench-open-7c3aed?style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-64748b?style=flat-square)](LICENSE)

**[中文](#中文) · [English](#english)**

---

## 中文

这是一个面向具身智能科研工作的双层论文索引：

1. **近五年顶会普查**：3,724 篇，覆盖 RSS、CoRL、ICRA、IROS、ICLR、ICML、NeurIPS、CVPR、ICCV、ECCV，会议年份为 2022–2026。
2. **近三年 arXiv 层**：对 2024-01-01 至 2026-08-07 的全部 27,597 条 `cs.RO` 候选执行确定性标题/摘要分类，七方向共纳入 21,411 篇。

两个层级严格分开。arXiv 条目始终标记为预印本；即使它与顶会层标题相同，也不会被当成会议录用证据。合并工作台优先保留具有正式会议来源的记录，按归一化标题得到 23,735 条去重结果。

### 三级研究分类

全部论文均采用一条主要的 **一级方向 → 二级子领域 → 三级专题** 路径组织：

- 7 个一级研究方向；
- 40 个二级子领域；
- 160 个明确三级专题；
- 每个二级领域另设“综合与交叉研究”，只用于现有标题、主题或摘要不足以支持更细判断的记录。

分类规则集中在 [`scripts/taxonomy.py`](scripts/taxonomy.py)，每条记录包含 `subcategory`、`specialty` 与 `taxonomy_evidence`。可直接浏览[完整中英双语分类图谱](papers/taxonomy/README.md)，或在首页按三级条件级联筛选。

### 七个方向

| 研究方向 | 顶会 2022–2026 | arXiv 2024–2026 | 方向入口 |
|---|---:|---:|---|
| Foundation Models & VLA | 318 | 3,276 | [顶会](papers/tracks/foundation-models-vla.md) · [arXiv](papers/arxiv/foundation-models-vla/README.md) |
| Manipulation & Imitation | 941 | 3,817 | [顶会](papers/tracks/manipulation-imitation.md) · [arXiv](papers/arxiv/manipulation-imitation/README.md) |
| Dexterity & Teleoperation | 339 | 935 | [顶会](papers/tracks/dexterity-teleoperation.md) · [arXiv](papers/arxiv/dexterity-teleoperation/README.md) |
| Navigation & Embodied Agents | 807 | 5,989 | [顶会](papers/tracks/navigation-embodied-agents.md) · [arXiv](papers/arxiv/navigation-embodied-agents/README.md) |
| Humanoids & Locomotion | 670 | 2,317 | [顶会](papers/tracks/humanoids-locomotion.md) · [arXiv](papers/arxiv/humanoids-locomotion/README.md) |
| Perception & World Models | 317 | 2,154 | [顶会](papers/tracks/perception-world-models.md) · [arXiv](papers/arxiv/perception-world-models/README.md) |
| Simulation, Data & Evaluation | 332 | 2,923 | [顶会](papers/tracks/simulation-data-evaluation.md) · [arXiv](papers/arxiv/simulation-data-evaluation/README.md) |

每个 arXiv 方向继续拆分为 2024、2025、2026 三个完整年份目录，避免超长页面影响 GitHub 阅读。

### 完整性的可审计定义

- 顶会层是固定会议、年份、`robot` 检索词、标题分类和排除规则下的 **systematic conference census**。
- arXiv 层从官方 [arXiv API](https://info.arxiv.org/help/api/user-manual.html) 收集完整 `cs.RO` 日期窗口，再使用公开词表进行标题/摘要分类。
- 27,597 条候选中，21,411 条进入七方向，6,186 条未满足分类边界；所有数字均写入数据检索账本。
- 医学、手术与康复类术语被明确排除；每篇论文只分配一条主要三级路径。
- “最全”指完整覆盖上述可复现边界，不代表学术界对“具身智能”存在无争议的语义全集。

### 科研工作台

[在线工作台](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)支持：

- 首页七方向直接进入顶会层、arXiv 层或合并去重层。
- 标题、作者、主题、年份、会议、一级方向、二级子领域、三级专题与来源层级联合检索。
- 可分享 URL、本地阅读清单、Markdown / CSV 导出、中英文和深浅主题。
- arXiv 作者与精确提交日期可见；顶会层缺失的作者信息不会被推测。

---

<a id="english"></a>

## English

This repository is a two-layer research index for Embodied AI:

1. A **systematic conference census** of 3,724 papers from ten major venues, 2022–2026.
2. A recent arXiv layer built from every `cs.RO` candidate submitted from 2024-01-01 through 2026-08-07: 27,597 candidates evaluated and 21,411 admitted by the published seven-direction taxonomy.

The layers remain provenance-safe. An arXiv paper is a preprint, not evidence of conference acceptance. The combined workbench prefers formal conference records for normalized-title duplicates and exposes 23,735 unique records.

### Three-level taxonomy

Every paper receives one primary **direction → subfield → specialty** path: 7 level-1 directions, 40 level-2 subfields, and 160 named level-3 specialties. A scoped General / Cross-cutting leaf is retained when the available title, topic, or abstract does not support a narrower claim.

The bilingual ontology is published in the [taxonomy map](papers/taxonomy/README.md). Each record exposes `subcategory`, `specialty`, and `taxonomy_evidence`; the homepage provides cascading filters and direct subfield entry.

### Operational boundary

- Conference discovery: Semantic Scholar bulk venue metadata with the query `robot`, followed by deterministic title admission and explicit exclusions.
- arXiv discovery: the official [arXiv API](https://info.arxiv.org/help/api/user-manual.html), complete `cs.RO` date-window harvesting, and deterministic title/abstract classification.
- Deduplication: normalized title in the combined view; both source records remain available in their separate layers.
- Coverage claims are relative to these declared rules, not to an undefined universal ontology of Embodied AI.

### Provenance

| Layer / tier | Records | Meaning |
|---|---:|---|
| Conference · Official | 74 | Manually verified proceedings or conference pages |
| Conference · Publisher | 3,577 | DOI or publisher records |
| Conference · Bibliographic | 73 | DBLP or Semantic Scholar when no publisher URL is exposed |
| arXiv | 21,411 | Official arXiv abstract and PDF pages; not labeled as conference acceptances |

### Repository structure

```text
├── index.html                         # bilingual research workbench
├── assets/
│   ├── app.js                         # direction entry, corpus switching, search and exports
│   └── styles.css                     # responsive research UI
├── data/
│   ├── papers.json                    # schema v4 conference census + three-level taxonomy
│   └── arxiv_recent.json              # schema v2 recent-arXiv layer + three-level taxonomy
├── papers/
│   ├── README.md                      # generated cross-layer overview
│   ├── taxonomy/                      # bilingual 7 → 40 → 160 research map
│   ├── tracks/                        # seven conference direction catalogs
│   └── arxiv/                         # seven directions × three year indexes
├── scripts/
│   ├── sync_conference_census.py      # conference discovery and classification
│   ├── sync_arxiv_recent.py           # rate-limited, resumable arXiv synchronization
│   ├── taxonomy.py                    # deterministic level-2/level-3 classifier
│   ├── apply_taxonomy.py              # reproducible annotation migration/check
│   ├── render_catalog.py              # deterministic split-catalog renderer
│   └── audit_catalog.py               # schema, coverage, ledger and provenance audit
└── tests/
    └── test_catalog.py                # conference, arXiv and UI contracts
```

### Rebuild and validate

```bash
python scripts/sync_conference_census.py
python scripts/sync_arxiv_recent.py
python scripts/apply_taxonomy.py --check
python scripts/render_catalog.py
python scripts/audit_catalog.py
python scripts/render_catalog.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
```

The arXiv synchronizer follows the API paging guidance, waits between requests, retries transient failures, and resumes from an ignored local checkpoint.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Change declared discovery or taxonomy rules and rerun the pipeline instead of inserting untraceable bulk records.

## License

Repository-authored content is licensed under [CC BY-NC-SA 4.0](LICENSE). Paper copyrights remain with their authors and publishers; this repository links to papers and does not redistribute PDFs.
