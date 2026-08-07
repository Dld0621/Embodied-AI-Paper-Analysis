# Embodied AI Paper Analysis

> 3,724 papers · 10 major venues · 7 research directions · systematic conference census · 2022–2026

[![Catalog](https://img.shields.io/badge/Conference%20census-3%2C724-111827?style=flat-square)](papers/README.md)
[![Window](https://img.shields.io/badge/Window-2022--2026-2563eb?style=flat-square)](data/papers.json)
[![Method](https://img.shields.io/badge/Method-reproducible-16a34a?style=flat-square)](scripts/sync_conference_census.py)
[![Website](https://img.shields.io/badge/Live%20index-open-7c3aed?style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-64748b?style=flat-square)](LICENSE)

**[中文](#中文) · [English](#english)**

---

## 中文

这是一个面向具身智能研究的 **近五年顶会论文系统性普查**。目录不再只挑选少量代表论文，而是固定顶会、年份、检索词、标题分类规则和排除规则，收录该操作性边界内的全部命中记录。

“全部”必须有可验证的定义。本仓库中的完整性具体指：

1. 固定 10 个顶会：RSS、CoRL、ICRA、IROS、ICLR、ICML、NeurIPS、CVPR、ICCV、ECCV。
2. 固定会议窗口：2022–2026。
3. 通过 Semantic Scholar 会议索引，以 `robot` 查询完整会议元数据。
4. 使用仓库内公开的标题分类词表映射到七个研究方向，并排除医学、手术和康复类记录。
5. 对标题归一化去重；74 篇人工核验种子优先覆盖自动发现的同名记录。

这意味着仓库覆盖 **上述规则下的全部论文**，但不会把有争议的“什么算具身智能”包装成不存在的绝对全集。任何漏收或误收都可以通过 [同步脚本](scripts/sync_conference_census.py) 和 [`census.venue_discovery`](data/papers.json) 复现、定位和修正。

### 数据概览

| 指标 | 当前状态 |
|---|---:|
| 论文总数 | 3,724 |
| 会议索引候选 | 9,572 |
| 年份窗口 | 2022–2026 |
| 顶会 | 10 |
| 研究方向 | 7 |
| 在线论文链接 | 100% |
| 在线来源链接 | 100% |
| 2026 论文 | 12（截至 2026-08-07） |

### 七个完整方向

| 研究方向 | 论文 | 年份 | 顶会覆盖 |
|---|---:|---|---:|
| Foundation Models & VLA | 318 | 2022–2026 | 10 |
| Manipulation & Imitation | 941 | 2022–2026 | 10 |
| Dexterity & Teleoperation | 339 | 2022–2026 | 10 |
| Navigation & Embodied Agents | 807 | 2022–2026 | 9 |
| Humanoids & Locomotion | 670 | 2022–2026 | 8 |
| Perception & World Models | 317 | 2022–2026 | 10 |
| Simulation, Data & Evaluation | 332 | 2022–2026 | 10 |

每个方向都有独立 GitHub 目录，按 2026 → 2022 排列全部论文，并提供 `Paper` 与来源链接。来源被明确区分为人工核验的 `Official`、出版社/DOI 的 `Publisher` 和文献数据库的 `Index`，不会把所有数据库页面误称为官方录用页。

### 入口

- **[交互式论文普查](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)**：搜索全部 3,724 篇论文，按年份、会议和方向筛选。
- **[方向总览与检索账本](papers/README.md)**：查看每个顶会从候选到最终收录的数量。
- **[七个方向完整目录](papers/tracks/)**：拆分后的 GitHub 友好目录。
- **[同步与分类规则](scripts/sync_conference_census.py)**：完整性定义的可执行来源。
- **[论文分析模板](docs/paper-analysis-template.md)**：区分论文主张、实验证据、限制与个人判断。

---

<a id="english"></a>

## English

This repository is a **systematic five-year conference census for Embodied AI**. It no longer means “a small representative reading list.” It includes every record admitted by a fixed and reproducible operational boundary:

1. Ten venues: RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV.
2. Conference years 2022–2026.
3. Semantic Scholar bulk venue discovery with the query `robot`.
4. Deterministic title taxonomy into seven research directions, with medical, surgical, and rehabilitation exclusions.
5. Normalized-title deduplication, with 74 manually verified seed records taking precedence.

Under that published boundary, the census is exhaustive. It does not claim that the research community has a universally agreed semantic definition of Embodied AI. The discovery ledger and classifier make disagreements inspectable instead of hiding them behind a vague “all papers” claim.

### Provenance

| Tier | Records | Meaning |
|---|---:|---|
| Official | 74 | Manually verified proceedings or conference pages |
| Publisher | 3,577 | DOI or publisher records |
| Bibliographic | 73 | DBLP or Semantic Scholar records when no publisher URL is exposed |

Every record includes an online paper link and a provenance link. The UI displays the provenance tier explicitly.

### Repository structure

```text
├── index.html                         # responsive bilingual census UI
├── assets/
│   ├── app.js                         # full-corpus search, filters and incremental rendering
│   └── styles.css                     # visual system
├── data/
│   └── papers.json                    # schema v3 source of truth + discovery ledger
├── papers/
│   ├── README.md                      # generated overview
│   └── tracks/                        # seven generated complete direction catalogs
├── scripts/
│   ├── sync_conference_census.py      # venue discovery, classification and deduplication
│   ├── audit_catalog.py               # schema, coverage, provenance and scope validation
│   ├── check_local_links.py           # repository-link validation
│   └── render_catalog.py              # deterministic split-catalog renderer
└── tests/
    └── test_catalog.py                # census contracts
```

### Rebuild and validate

```bash
python scripts/sync_conference_census.py
python scripts/render_catalog.py
python scripts/audit_catalog.py
python scripts/render_catalog.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
```

## Census policy · 普查规则

- The census is complete relative to its declared venue/query/taxonomy boundary, not relative to an undefined universal ontology.
- One normalized title appears once and is assigned one primary venue and one primary research direction.
- 2026 is an in-progress snapshot frozen at **2026-08-07**; unpublished future proceedings are never projected.
- New records must keep both `paper_url` and provenance `official_url` as HTTPS links and declare `source_type`.
- Workshops or records not represented as papers in the selected venue index are outside this snapshot.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). For systematic updates, change the declared rules and rerun the census rather than manually inserting untraceable bulk records.

## License

Repository-authored content is licensed under [CC BY-NC-SA 4.0](LICENSE). Paper copyrights remain with their authors and publishers; this repository links to papers and does not redistribute PDFs.
