# Embodied AI Paper Analysis

> 1099 篇具身智能论文 · 7 大研究方向 · 20 个子方向 · 2015–2026 · arXiv 覆盖率 88%

[![Papers](https://img.shields.io/badge/Papers-1099-blue?style=flat-square)](papers/README.md)
[![Directions](https://img.shields.io/badge/Directions-7-green?style=flat-square)](#方向地图)
[![Topics](https://img.shields.io/badge/Topics-20-green?style=flat-square)](papers/README.md)
[![arXiv](https://img.shields.io/badge/arXiv%20Coverage-88%25-red?style=flat-square)](papers/README.md)
[![Website](https://img.shields.io/badge/Live%20Site-Online-brightgreen?logo=github&style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](LICENSE)

**[中文](#中文) | [English](#english)**

---

<a id="中文"></a>

## 中文

系统化收录和分类具身智能领域的前沿论文，覆盖感知表征、操作抓取、移动导航、策略学习、仿真数据、世界模型与硬件系统七大方向，提供两级分类导航、交互式搜索和深度分析文档。

### 在线访问

**[dld0621.github.io/Embodied-AI-Paper-Analysis](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)** — 支持方向导航、子方向筛选、年份分布图、关键词搜索和深色模式。

### 数据概览

| 指标 | 数值 |
|------|------|
| 论文总数 | 1,099 |
| arXiv 链接 | 976 篇（88%） |
| 代码开源 | 74 篇 |
| 研究方向 | 7 个一级 · 20 个二级 |
| 年份跨度 | 2015–2026 |
| 顶会覆盖 | RSS · CoRL · ICRA · ICLR · ICML · CVPR · NeurIPS · SIGGRAPH |

### 方向地图

| 一级方向 | 二级方向 | 论文数 | 主要问题 |
|---------|---------|-------|---------|
| **Perception & Representation** 感知与表征 | Foundation Models · 3D Vision · Gaussian Splatting · Motion Tracking · Tactile Sensing | 132 | 从通用视觉语义、三维结构、动态跟踪到触觉表征，为后续规划与控制提供可迁移的状态表示 |
| **Manipulation & Grasping** 操作与抓取 | Manipulation · Grasping · Retargeting | 102 | 从语言与几何约束的操作，走向接触丰富抓取、跨形态迁移和功能保持重定向 |
| **Locomotion & Navigation** 移动与导航 | Humanoid Robotics · Locomotion · Navigation · Teleoperation | 54 | 从全身模仿与敏捷运动，连接到开放环境导航和语言条件目标搜索 |
| **Policy Learning** 策略学习 | Diffusion Policy · Reinforcement Learning · VLA | 124 | 覆盖扩散策略、强化学习和 VLA 三条主线 |
| **Simulation & Data** 仿真与数据 | Simulation · Data Generation | 27 | 通过可扩展仿真、任务基准和真实多机器人数据降低训练与评测成本 |
| **World Models & Generation** 世界模型与生成 | World Models · Video Generation | 14 | 用可交互世界模型预测未来、规划动作，并通过视频生成学习物理与时序先验 |
| **Hardware & Systems** 硬件与系统 | Hardware | 9 | 灵巧手、传感器、硬件平台与遥操作系统 |

> 另有 637 篇待分类论文（Uncategorized / Others），持续整理中。

### 特色内容

**Hand Retargeting 专题分析**（45 篇）— 对灵巧手重定向领域进行三级分类（L1 姿态重定向 / L2 可执行重定向 / L3 功能意图重定向），包含覆盖度评分、成熟度总览和重点研究路线。详见 [`papers/README.md`](papers/README.md) 和 [`docs/tactile-paper-analysis.md`](docs/tactile-paper-analysis.md)。

**触觉与接触优化论文深度分析**（11 篇）— 按 5 个维度（现有问题 → 根因 → 提出方法 → 与 baseline 区别 → 效果提升）分析 SpringGrasp、Dexonomy、GraspQP、DexGrasp Anything、Complementarity-Free Multi-Contact、IMPACT、Semantic Contact Fields、Contact-Grounded Policy、Force Policy、TACTIC 等 RSS/CVPR/CoRL 顶会论文。详见 [`docs/tactile-paper-analysis.md`](docs/tactile-paper-analysis.md)。

### 仓库结构

```
├── index.html              # 交互式论文索引（GitHub Pages）
├── papers/
│   ├── README.md           # 按主题分类的完整论文列表
│   └── index.md            # 年份索引
├── notes/                  # 21 个主题目录的阅读笔记
├── docs/
│   ├── paper-analysis-template.md   # 论文分析模板（9 维度）
│   ├── reading-methodology.md       # 阅读方法论
│   ├── taxonomy.md                  # 分类体系说明
│   └── tactile-paper-analysis.md    # 触觉论文深度分析
├── scripts/                # 索引生成脚本
├── summaries/              # 一句话论文摘要
├── .github/workflows/      # GitHub Pages 自动部署
└── assets/                 # 图片资源
```

### 阅读路线

围绕 **感知 → 操作 → 运动 → 策略 → 世界模型** 的能力栈：

1. **打地基** — Foundation Models → 3D Vision → Gaussian Splatting
2. **进操作** — Manipulation → Grasping → Hand Retargeting → Diffusion Policy
3. **上身体** — Humanoid Robotics → Locomotion → Navigation
4. **学策略** — Reinforcement Learning → VLA
5. **看未来** — World Models → Video Generation → Simulation

### 快速开始

```bash
git clone https://github.com/Dld0621/Embodied-AI-Paper-Analysis.git
cd Embodied-AI-Paper-Analysis

# 在线浏览论文索引
open index.html

# 按主题查看论文列表
cat papers/README.md

# 使用论文分析模板
cp docs/paper-analysis-template.md notes/06-manipulation/2025-xxx.md
```

---

<a id="english"></a>

## English

A systematic collection of frontier papers in Embodied AI, organized across 7 research directions and 20 sub-topics — from perception and manipulation to world models and hardware systems, with interactive search, filtering, and in-depth analysis.

### Live Site

**[dld0621.github.io/Embodied-AI-Paper-Analysis](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)** — Features direction navigation, sub-topic filtering, year distribution charts, keyword search, and dark mode.

### Key Stats

| Metric | Value |
|--------|-------|
| Total Papers | 1,099 |
| arXiv Links | 976 (88%) |
| Open Code | 74 |
| Directions | 7 L1 · 20 L2 |
| Year Range | 2015–2026 |
| Top Venues | RSS · CoRL · ICRA · ICLR · ICML · CVPR · NeurIPS · SIGGRAPH |

### Direction Map

| Direction | Sub-topics | Papers | Focus |
|-----------|-----------|--------|-------|
| **Perception & Representation** | Foundation Models · 3D Vision · Gaussian Splatting · Motion Tracking · Tactile Sensing | 132 | Transferable state representations for planning and control |
| **Manipulation & Grasping** | Manipulation · Grasping · Retargeting | 102 | Contact-rich grasping, cross-embodiment transfer, function-preserving retargeting |
| **Locomotion & Navigation** | Humanoid Robotics · Locomotion · Navigation · Teleoperation | 54 | Whole-body imitation, agile locomotion, open-world navigation |
| **Policy Learning** | Diffusion Policy · Reinforcement Learning · VLA | 124 | Three mainlines: diffusion, RL, and vision-language-action models |
| **Simulation & Data** | Simulation · Data Generation | 27 | Scalable simulation, benchmarks, and real multi-robot data |
| **World Models & Generation** | World Models · Video Generation | 14 | Interactive world models and video generation for physical priors |
| **Hardware & Systems** | Hardware | 9 | Dexterous hands, sensors, and teleoperation platforms |

### Featured Analysis

- **Hand Retargeting Special** (45 papers) — Three-level taxonomy (L1 pose / L2 executable / L3 functional), coverage scoring, and maturity assessment. See [`papers/README.md`](papers/README.md).
- **Tactile & Contact Optimization Deep Dive** (11 papers) — Structured analysis of RSS/CVPR/CoRL papers across 5 dimensions. See [`docs/tactile-paper-analysis.md`](docs/tactile-paper-analysis.md).

### Analysis Template

Each paper is analyzed using a 9-dimension unified template (see [`docs/paper-analysis-template.md`](docs/paper-analysis-template.md)):

1. Metadata · 2. One-sentence Summary · 3. Research Question · 4. Core Method · 5. Key Innovation · 6. Experiments · 7. Limitations & Future Work · 8. Transferability · 9. Reproduction Notes

---

## Contributing

Contributions are welcome! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting a PR.

### How to Contribute

- Add new papers to the collection
- Write analysis notes using the template
- Improve classification and metadata
- Fix broken links or incorrect venues

## License

Content is licensed under [CC BY-NC-SA 4.0](LICENSE). Paper copyrights belong to their respective authors; this repository does not distribute PDFs.

## Acknowledgments

Paper metadata is sourced from arXiv, Google Scholar, and official conference proceedings. Classification taxonomy is inspired by the Embodied AI literature guide covering 2023–2026 top-tier venues.
