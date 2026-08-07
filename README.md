# Embodied AI Paper Analysis

> 74 curated papers · 10 major venues · 7 research tracks · every direction covers 2022–2026

[![Catalog](https://img.shields.io/badge/Core%20catalog-74-111827?style=flat-square)](papers/README.md)
[![Window](https://img.shields.io/badge/Window-2022--2026-2563eb?style=flat-square)](data/papers.json)
[![Policy](https://img.shields.io/badge/Policy-formally%20accepted-16a34a?style=flat-square)](#selection-policy--收录规则)
[![Website](https://img.shields.io/badge/Live%20index-open-7c3aed?style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-64748b?style=flat-square)](LICENSE)

**[中文](#中文) · [English](#english)**

---

## 中文

这是一个面向研究入门和方向判断的 **近五年具身智能顶会论文导航**。仓库从宽泛的千篇聚合收敛为 74 篇正式录用论文，以官方会议或出版页面作为 venue 证据，并将预印本日期与正式会议年份分开。七个研究方向现在都覆盖 2022–2026，每篇论文都提供在线论文与正式录用来源。

### 为什么收敛

原目录规模大，但包含重复标题、旧年份、仅 arXiv 论文、模糊的多会标签以及会议年份错误。新版优先解决三个问题：

1. **能否确认被哪一个会议正式录用？**
2. **是否属于当前 2022–2026 五年窗口？**
3. **是否直接服务于具身智能的感知、决策、控制或系统研究？**

### 数据概览

| 指标 | 当前状态 |
|---|---:|
| 精选论文 | 74 |
| 年份窗口 | 2022–2026 |
| 正式会议 | 10 |
| 研究主线 | 7 |
| 2026 论文 | 12（截至 2026-08-07） |
| 官方来源 | 每篇必填 |
| 方向年份覆盖 | 7 个方向均为 5/5 年 |

### 顶会范围

- **Robotics**：RSS · CoRL · ICRA · IROS
- **Machine Learning**：ICLR · ICML · NeurIPS
- **Computer Vision**：CVPR · ICCV · ECCV

这是一份精选研究地图，不是会议论文全集。会议覆盖不代表每个会议都按相同数量收录。

### 七条研究主线

| 主线 | 数量 | 年份 | 关注问题 |
|---|---:|---|---|
| Foundation Models & VLA | 21 | 2022–2026 | 通用策略、VLA、多模态推理、跨本体学习 |
| Manipulation & Imitation | 11 | 2022–2026 | 模仿学习、扩散策略、约束与视频动作迁移 |
| Dexterity & Teleoperation | 10 | 2022–2026 | 灵巧手、双臂操作、遥操作与数据采集接口 |
| Navigation & Embodied Agents | 7 | 2022–2026 | 开放世界、移动操作与具身任务规划 |
| Humanoids & Locomotion | 6 | 2022–2026 | 人形全身控制、模仿与 loco-manipulation |
| Perception & World Models | 9 | 2022–2026 | 表征学习、触觉、三维状态与世界模型 |
| Simulation, Data & Evaluation | 10 | 2022–2026 | 仿真、数据生成、基准与评测协议 |

### 推荐阅读顺序

1. **表征与环境**：R3M → BEHAVIOR-1K → ManiSkill2 → DROID
2. **策略学习**：RT-1 → Diffusion Policy → Octo → OpenVLA
3. **语言与行动**：SayCan → PaLM-E → RT-2 → π0.5
4. **灵巧与数据采集**：ALOHA → AnyTeleop → UMI → FastUMI
5. **最新前沿**：RDT-1B → HAMSTER → MemoryVLA → SaPaVe → LAST

### 入口

- **[交互式论文索引](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)**：按年份、会议、主线和关键词筛选。
- **[完整精选目录](papers/README.md)**：由 JSON 自动生成，适合 GitHub 内浏览。
- **[论文分析模板](docs/paper-analysis-template.md)**：统一记录问题、方法、证据与限制。
- **[阅读方法](docs/reading-methodology.md)**：建立可复现、可对比的阅读习惯。
- **[深度笔记](notes/README.md)**：少量重点论文的结构化分析。

---

<a id="english"></a>

## English

This repository is a **curated five-year map of Embodied AI research**, centered on 74 formally accepted papers from major robotics, machine-learning, and vision venues. Every research direction now spans 2022–2026, and every paper includes a direct online paper link plus an official acceptance source.

### What this repository optimizes for

- **Precision over volume** — every core entry has one unambiguous venue.
- **Recency with context** — the rolling window is 2022–2026.
- **Embodied relevance** — papers must connect perception or reasoning to action, control, evaluation, or physical systems.
- **Auditable provenance** — official venue evidence is required separately from the paper or arXiv link.

### Coverage

| Area | Venues |
|---|---|
| Robotics | RSS · CoRL · ICRA · IROS |
| Machine Learning | ICLR · ICML · NeurIPS |
| Computer Vision | CVPR · ICCV · ECCV |

The catalog is selective rather than exhaustive. 2026 coverage is frozen at **2026-08-07** and only includes acceptances already visible on official sources.

### Repository structure

```text
├── index.html                 # responsive bilingual research index
├── assets/
│   ├── app.js                 # search, filters, language and theme
│   └── styles.css             # visual system
├── data/
│   └── papers.json            # single source of truth
├── papers/
│   └── README.md              # generated human-readable catalog
├── notes/                     # selected deep-dive notes
├── docs/                      # methodology and analysis templates
├── scripts/
│   ├── audit_catalog.py       # schema, source and scope validation
│   ├── check_local_links.py   # repository-link validation
│   └── render_catalog.py      # deterministic catalog renderer
└── tests/
    └── test_catalog.py        # repository contracts
```

### Local validation

```bash
python scripts/audit_catalog.py
python scripts/render_catalog.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
```

## Selection policy · 收录规则

Core entries must satisfy all of the following:

1. Conference year is between 2022 and 2026, inclusive.
2. The paper is formally accepted to a listed venue or official conference track.
3. An official proceedings, conference, OpenReview acceptance, IEEE, CVF, ECVA, RSS, or PMLR link verifies the venue.
4. The title is complete and unique, and the venue is a single conference rather than an ambiguous label such as `RSS/CoRL/ICRA`.
5. Workshops, withdrawn submissions, under-review work, generic non-embodied papers, and arXiv-only preprints are excluded from the core count.

Older classics and important preprints may be discussed in notes, but they must be labeled outside the core catalog.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Add catalog data to [`data/papers.json`](data/papers.json), regenerate the Markdown index, and run all three local checks before opening a pull request.

## License

Repository-authored content is licensed under [CC BY-NC-SA 4.0](LICENSE). Paper copyrights remain with their authors and publishers; this repository links to papers and does not redistribute PDFs.
