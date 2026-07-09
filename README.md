# Embodied AI Paper Analysis

> A systematic paper reading repository for Embodied AI — covering 920+ papers across 21 topics, from perception and manipulation to world models and humanoid robotics.

[![Papers](https://img.shields.io/badge/Papers-920%2B-blue?style=flat-square)](papers/README.md)
[![Topics](https://img.shields.io/badge/Topics-21-green?style=flat-square)](papers/README.md)
[![Years](https://img.shields.io/badge/Years-2015--2026-orange?style=flat-square)](papers/index.md)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](LICENSE)

**[English](#overview) | [中文](#概览)**

---

## Overview

This repository provides a structured framework for analyzing frontier papers in Embodied AI. Each paper is broken down using a unified template covering motivation, method, innovation, experiments, and reproducibility notes.

### Paper Index

All 920+ papers are organized by topic in [`papers/README.md`](papers/README.md), with each entry including arXiv links and GitHub code links where available. An interactive web version is available at [`index.html`](index.html).

| Category | Topics | Link |
| :--- | :--- | :--- |
| **Perception & Representation** | Foundation Models · 3D Vision · Gaussian Splatting · Motion Tracking · Tactile Sensing | [Browse](papers/README.md#3d-vision--perception) |
| **Manipulation & Grasping** | Manipulation · Grasping · Retargeting | [Browse](papers/README.md#manipulation) |
| **Locomotion & Navigation** | Humanoid Robotics · Locomotion · Navigation | [Browse](papers/README.md#humanoid-robotics) |
| **Policy Learning** | Diffusion Policy · Reinforcement Learning · VLA | [Browse](papers/README.md#diffusion-policy) |
| **Simulation & Data** | Simulation · Data Generation | [Browse](papers/README.md#simulation) |
| **World Models & Generation** | World Models · Video Generation | [Browse](papers/README.md#world-models) |
| **Teleoperation & Hardware** | Teleoperation · Hardware | [Browse](papers/README.md#teleoperation) |
| **Others** | Others · Uncategorized | [Browse](papers/README.md#others) |

### Repository Structure

```
├── index.html          # Interactive paper index (web)
├── papers/             # Paper index by topic & year
├── notes/              # Analysis notes (21 topic dirs)
├── docs/               # Templates & methodology
├── scripts/            # Index generator (Node.js)
└── summaries/          # One-line paper summaries
```

### Quick Start

```bash
git clone https://github.com/Dld0621/Embodied-AI-Paper-Analysis.git
cd Embodied-AI-Paper-Analysis

# Create a new note from template
cp docs/paper-analysis-template.md notes/06-manipulation/2025-xxx.md

# Regenerate the notes index
npm run generate
```

---

## 概览

系统化拆解具身智能前沿论文的阅读笔记仓库，覆盖感知、操作、运动、策略学习到世界模型，用统一框架沉淀每篇论文的问题、方法、创新与复现细节。

### 论文索引

共收录 **920+ 篇**论文，按主题归档于 [`papers/README.md`](papers/README.md)，每个主题内按年份降序排列，每篇附 arXiv 链接与代码链接。交互式网页版见 [`index.html`](index.html)。

### 分析方法

每篇论文使用统一模板拆解（见 [`docs/paper-analysis-template.md`](docs/paper-analysis-template.md)），覆盖 9 个维度：元信息、一句话总结、研究问题、核心方法、关键创新、实验结果、局限与未来工作、可迁移性、复现笔记。

### 阅读路线

围绕 **感知 → 操作 → 运动 → 策略 → 世界模型** 的能力栈：

1. **打地基** — 基础模型与视觉表征 → 3D 视觉与高斯泼溅
2. **进操作** — 操作与抓取 → 重定向 → 扩散策略
3. **上身体** — 人形机器人与运动控制
4. **学策略** — 强化学习 → VLA
5. **看未来** — 世界模型与视频生成

---

## Contributing

Contributions are welcome! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting a PR.

## License

Content is licensed under [CC BY-NC-SA 4.0](LICENSE). Paper copyrights belong to their respective authors; this repository does not distribute PDFs.
