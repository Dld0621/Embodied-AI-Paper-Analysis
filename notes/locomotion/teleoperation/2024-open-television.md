# Open-TeleVision: Teleoperation with Immersive Active Visual Feedback

> Verified reading note · 已核验阅读笔记

## Metadata · 元信息

- **Authors**: Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang
- **Venue**: CoRL 2024
- **Official record**: [PMLR 270](https://proceedings.mlr.press/v270/cheng25b.html)
- **Preprint**: [arXiv:2407.01512](https://arxiv.org/abs/2407.01512)
- **Project**: [robot-tv.github.io](https://robot-tv.github.io/)
- **Code**: [OpenTeleVision/TeleVision](https://github.com/OpenTeleVision/TeleVision)
- **Track**: Dexterity & Teleoperation

PMLR published the proceedings in 2025; the conference edition represented here is CoRL 2024.

## Core idea · 核心思路

Open-TeleVision gives an operator stereoscopic, immersive visual feedback while mirroring arm and hand motion to a humanoid robot. The design targets intuitive collection of robot demonstrations rather than autonomous decision-making.

Open-TeleVision 为操作者提供立体、沉浸式视觉反馈，同时把手臂与手部运动映射到人形机器人。其目标是提升真实机器人示范数据采集的直观性，而非直接解决自主决策。

## Pipeline · 流程

`stereo robot video + headset tracking + hand/arm motion → retargeting → humanoid commands → synchronized demonstration data`

## Reported evidence · 论文报告

- Data were collected for four long-horizon, precise tasks: can sorting, can insertion, folding, and unloading.
- The paper reports experiments with two humanoid robots.
- Policies trained from the collected demonstrations were deployed in the real world.

## Reading boundary · 阅读边界

- Teleoperation usability, imitation-policy performance, and autonomous generalization are different claims.
- The official abstract does not support generic latency or task-success numbers; this note therefore does not invent them.
- Reproduction should document headset, network, calibration, retargeting, robot embodiment, and policy-training choices separately.
