# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> Verified reading note · 已核验阅读笔记

## Metadata · 元信息

- **Authors**: Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin C. M. Burchfiel, Shuran Song
- **Venue**: RSS 2023
- **Official record**: [RSS XIX](https://roboticsproceedings.org/rss19/p026.html)
- **Track**: Manipulation & Imitation

## Core idea · 核心思路

Diffusion Policy represents a visuomotor policy as a conditional denoising diffusion process over action sequences. Receding-horizon execution repeatedly conditions on observations, predicts an action horizon, executes a prefix, and replans.

Diffusion Policy 将视觉运动策略表示为条件去噪扩散过程，以动作序列为生成对象。系统通过滚动时域不断读取观测、预测一段动作、执行前缀并重新规划。

## Pipeline · 流程

`observation history → visual encoder → conditional action denoising → action sequence → execute prefix → re-observe`

## Reported evidence · 论文报告

- Evaluated across 12 tasks from four manipulation benchmarks.
- The official abstract reports an average improvement of 46.9% over the compared state-of-the-art methods.
- The paper identifies multimodal action modeling, high-dimensional action sequences, and training stability as key benefits of the formulation.

The 46.9% figure is an aggregate under the paper's benchmark definitions; it should not be reused as a generic expected gain.

## Reading boundary · 阅读边界

- Diffusion Policy is a policy representation and training recipe, not a complete perception, safety, or task-planning stack.
- Sampling cost, horizon choices, and control latency remain deployment variables.
- Fair reproduction should report architecture, observation/action horizons, inference steps, dataset, and evaluation protocol.
