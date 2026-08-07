# Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning

> Journal note · 期刊论文笔记（不计入顶会核心目录）

## Metadata · 元信息

- **Authors**: Jianlan Luo, Charles Xu, Jeffrey Wu, Sergey Levine
- **Formal publication**: Science Robotics, 2025
- **DOI**: [10.1126/scirobotics.ads5033](https://doi.org/10.1126/scirobotics.ads5033)
- **Preprint**: [arXiv:2410.21845](https://arxiv.org/abs/2410.21845)
- **Project**: [hil-serl.github.io](https://hil-serl.github.io/)
- **Track**: Manipulation & Imitation

The filename keeps the 2024 preprint year for stable links. This work is a journal paper and is intentionally outside the conference-only core catalog.

## Core idea · 核心思路

HIL-SERL combines demonstrations, human interventions/corrections, and sample-efficient real-world reinforcement learning. The system targets dynamic manipulation, precision assembly, and dual-arm coordination directly on physical robots.

HIL-SERL 将示范、人类干预/纠正与高样本效率的真实机器人强化学习结合，用于动态操作、精密装配与双臂协同。

## Pipeline · 流程

`demonstrations → initial policy/replay data → autonomous rollout → human intervention and correction → off-policy RL update → repeated real-world evaluation`

## Reported evidence · 论文报告

- The preprint reports training times of roughly 1 to 2.5 hours for its task suite.
- It reports an average 2× success-rate improvement and 1.8× faster execution relative to the compared baselines.
- These aggregates depend on the paper's tasks, interventions, rewards, hardware, and evaluation protocol.

## Reading boundary · 阅读边界

- Human intervention is part of the learning system and its cost should be reported, not hidden.
- Journal publication status is distinct from inclusion in this repository's selected top-conference set.
- Claims about exact success rates for individual tasks should cite the corresponding paper table rather than a secondary summary.
