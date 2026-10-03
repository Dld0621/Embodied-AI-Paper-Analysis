# Embodied AI Paper Analysis · 具身智能论文研究地图

**[English](README.md) · 简体中文**

> 面向科研工作者的可审计论文工作台：4,365 篇近五年顶会论文、25,257 篇近三年 arXiv 预印本，按 9 个一级方向、42 个二级子领域和 168 个最细论文目录组织。

[![在线工作台](https://img.shields.io/badge/在线科研工作台-打开-2563eb?style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?lang=zh)
[![顶会论文](https://img.shields.io/badge/顶会论文-4%2C365-111827?style=flat-square)](data/papers.json)
[![arXiv](https://img.shields.io/badge/arXiv-25%2C257-b31b1b?style=flat-square)](data/arxiv_recent.json)
[![三级分类](https://img.shields.io/badge/分类-9%E2%86%9242%E2%86%92168-0891b2?style=flat-square)](papers/taxonomy/README.md)

## 快速入口

| 目标 | 入口 |
|---|---|
| 搜索、筛选、保存与导出论文 | [在线科研工作台](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?lang=zh#research-workbench) |
| 从 9 个方向逐级浏览到最细专题 | [三级研究分类图](papers/taxonomy/README.md) |
| 浏览近五年顶会层 | [顶会论文总览](papers/README.md) |
| 跨分类重定向检索、分类依据与待审 | [关联主题](papers/topics/README.md) · [分类说明](docs/taxonomy-guide.md) · [待审清单](papers/classification-review/README.md) |
| 使用机器可读数据 | [`papers.json`](data/papers.json) · [`arxiv_recent.json`](data/arxiv_recent.json) |

## 项目解决什么问题

本项目不是简单的论文链接集合，而是一套可复现的具身智能文献定位系统。每篇论文同时回答四个问题：它属于哪个一级研究方向、位于哪个二级子领域、落在哪个三级专题，以及这一判断来自标题、摘要或核查例外中的什么证据。

顶会记录与 arXiv 预印本严格分层。标题重复不会被解释为会议录用；合并视图只用于阅读去重，原始来源仍分别保留。

## 两个证据层

| 层级 | 时间窗口 | 记录数 | 学术含义 |
|---|---|---:|---|
| 顶会普查 | 2022–2026 | 4,365 | RSS、CoRL、ICRA、IROS、ICLR、ICML、NeurIPS、CVPR、ICCV、ECCV；记录附正式来源层级 |
| arXiv 预印本 | 2023-10-03 至 2026-10-03 | 25,257 | 对完整 `cs.RO` 候选窗口进行分类；不代表顶会录用 |
| 合并去重视图 | 同上 | 27,637 | 按归一化标题去重，优先显示已有会议来源的记录 |

## 九方向三级研究地图

每篇论文只拥有一条主要的 **一级方向 → 二级子领域 → 三级专题** 路径。当前分类包含 126 个明确专题，并为 42 个二级子领域各保留一个“待审专题”落点，共 168 个最细目录。展开下方任一方向即可查看全部二级、三级分类及其论文数量。

<details>
<summary><strong>01 · 策略学习与具身基础模型 · Policy Learning & Embodied Foundation Models</strong><br><sub>270 篇顶会 · 3,867 篇 arXiv · 5 个二级子领域 · 20 个最细目录</sub></summary>

论文主要如何推进策略学习与具身基础模型？

**研究流程：** 观测 → 策略学习 → 动作策略 → 机器人执行

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Policy%20Learning%20%26%20Embodied%20Foundation%20Models#research-workbench) · [顶会目录](papers/tracks/policy-learning-embodied-foundation-models.md) · [arXiv 目录](papers/arxiv/policy-learning-embodied-foundation-models/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 模仿学习<br><sub>Imitation Learning</sub> | 71 | 587 | [行为克隆与序列建模](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/behavior-cloning-sequence-modeling/README.md) — C 15 · A 120<br>[交互式模仿与纠错](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/interactive-imitation-correction/README.md) — C 4 · A 20<br>[示教分段与技能发现](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/demonstration-segmentation-skill-discovery/README.md) — C 0 · A 17<br>[待审专题](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/pending-specialty-review/README.md) — C 52 · A 430 |
| 强化学习<br><sub>Reinforcement Learning</sub> | 66 | 1,175 | [在线强化学习](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/online-reinforcement-learning/README.md) — C 59 · A 1,126<br>[离线强化学习](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/offline-reinforcement-learning/README.md) — C 7 · A 31<br>[模仿与强化学习结合](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/combining-imitation-reinforcement/README.md) — C 0 · A 18<br>[待审专题](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/pending-specialty-review/README.md) — C 0 · A 0 |
| 生成式动作策略<br><sub>Generative Action Policies</sub> | 32 | 353 | [扩散策略](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/diffusion-policies/README.md) — C 26 · A 227<br>[Flow Matching 策略](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/flow-matching-policies/README.md) — C 4 · A 113<br>[自回归与动作标记化](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/autoregressive-tokenized-actions/README.md) — C 2 · A 13<br>[待审专题](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/pending-specialty-review/README.md) — C 0 · A 0 |
| VLA 与通用机器人策略<br><sub>VLA & Generalist Robot Policies</sub> | 71 | 1,376 | [视觉语言动作建模](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/vision-language-action-modeling/README.md) — C 61 · A 1,296<br>[多模态动作对齐](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/multimodal-action-grounding/README.md) — C 10 · A 40<br>[分层策略与专家混合](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/hierarchical-mixture-policies/README.md) — C 0 · A 40<br>[待审专题](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/pending-specialty-review/README.md) — C 0 · A 0 |
| 泛化与适配<br><sub>Generalization & Adaptation</sub> | 30 | 376 | [跨机器人迁移](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/cross-robot-transfer/README.md) — C 1 · A 62<br>[少样本与测试时适配](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/few-shot-test-time-adaptation/README.md) — C 26 · A 289<br>[预训练与规模化规律](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/pretraining-scaling-laws/README.md) — C 3 · A 25<br>[待审专题](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>02 · 机械臂与通用物体操作 · Arm & General Object Manipulation</strong><br><sub>1,187 篇顶会 · 3,215 篇 arXiv · 4 个二级子领域 · 16 个最细目录</sub></summary>

论文主要如何推进机械臂与通用物体操作？

**研究流程：** 物体 → 任务约束 → 规划 → 操作

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Arm%20%26%20General%20Object%20Manipulation#research-workbench) · [顶会目录](papers/tracks/arm-general-object-manipulation.md) · [arXiv 目录](papers/arxiv/arm-general-object-manipulation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 抓取与拾放<br><sub>Grasping & Pick-place</sub> | 765 | 1,906 | [夹爪与吸盘抓取规划](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/gripper-suction-grasp-planning/README.md) — C 96 · A 159<br>[抓取稳定性](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/grasp-stability/README.md) — C 15 · A 45<br>[拾放与物体重排](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/pick-place-rearrangement/README.md) — C 93 · A 220<br>[待审专题](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/pending-specialty-review/README.md) — C 561 · A 1,482 |
| 接触丰富操作<br><sub>Contact-rich Manipulation</sub> | 234 | 638 | [插入与装配](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/insertion-assembly/README.md) — C 135 · A 371<br>[推滑与非抓取操作](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/pushing-non-prehensile-manipulation/README.md) — C 66 · A 151<br>[工具与关节物体操作](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/tools-articulated-objects/README.md) — C 33 · A 116<br>[待审专题](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/pending-specialty-review/README.md) — C 0 · A 0 |
| 可变形物体操作<br><sub>Deformable Object Manipulation</sub> | 55 | 126 | [布料与衣物](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/cloth-garments/README.md) — C 31 · A 61<br>[绳索与线缆](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/ropes-cables/README.md) — C 8 · A 13<br>[柔性与软体物体](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/flexible-soft-objects/README.md) — C 16 · A 52<br>[待审专题](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/pending-specialty-review/README.md) — C 0 · A 0 |
| 协同与复杂操作<br><sub>Coordinated & Complex Manipulation</sub> | 133 | 545 | [双臂协作](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/dual-arm-collaboration/README.md) — C 51 · A 160<br>[移动操作](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/mobile-manipulation/README.md) — C 49 · A 177<br>[长时程操作与任务运动规划](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/long-horizon-task-motion-planning/README.md) — C 33 · A 208<br>[待审专题](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>03 · 灵巧手、重定向与遥操作 · Dexterous Hands, Retargeting & Teleoperation</strong><br><sub>299 篇顶会 · 1,090 篇 arXiv · 5 个二级子领域 · 20 个最细目录</sub></summary>

论文主要如何推进灵巧手、重定向与遥操作？

**研究流程：** 人类或机器人观测 → 交互表征 → 手部映射与控制 → 灵巧执行

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Dexterous%20Hands%2C%20Retargeting%20%26%20Teleoperation#research-workbench) · [顶会目录](papers/tracks/dexterous-hands-retargeting-teleoperation.md) · [arXiv 目录](papers/arxiv/dexterous-hands-retargeting-teleoperation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 灵巧手重定向<br><sub>Dexterous Hand Retargeting</sub> | 87 | 288 | [运动学与姿态重定向](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/kinematic-pose-retargeting/README.md) — C 3 · A 11<br>[接触与功能重定向](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/contact-functional-retargeting/README.md) — C 0 · A 9<br>[物理与动力学重定向](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/physics-dynamics-retargeting/README.md) — C 0 · A 5<br>[待审专题](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/pending-specialty-review/README.md) — C 84 · A 263 |
| 多指抓取与控制<br><sub>Multifinger Grasping & Control</sub> | 32 | 88 | [多指协调与抓取生成](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/multifinger-coordination-grasp-generation/README.md) — C 31 · A 78<br>[抓取力与阻抗控制](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/grasp-force-impedance-control/README.md) — C 0 · A 6<br>[跨手形态泛化](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/cross-hand-generalization/README.md) — C 1 · A 4<br>[待审专题](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/pending-specialty-review/README.md) — C 0 · A 0 |
| 手内操作<br><sub>In-hand Manipulation</sub> | 43 | 100 | [物体旋转与重定位](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/object-rotation-repositioning/README.md) — C 40 · A 81<br>[滚动、滑动与换指](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/rolling-sliding-finger-gaiting/README.md) — C 2 · A 5<br>[稳定接触与滑移恢复](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/contact-stability-slip-recovery/README.md) — C 1 · A 14<br>[待审专题](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/pending-specialty-review/README.md) — C 0 · A 0 |
| 遥操作与共享控制<br><sub>Teleoperation & Shared Control</sub> | 108 | 450 | [视觉／手套／XR 输入](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/vision-gloves-xr-input/README.md) — C 91 · A 338<br>[共享自主与辅助控制](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/shared-autonomy-assistance/README.md) — C 6 · A 63<br>[双向力反馈与延迟处理](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/bilateral-feedback-delay/README.md) — C 11 · A 49<br>[待审专题](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/pending-specialty-review/README.md) — C 0 · A 0 |
| 人类示教到灵巧技能<br><sub>Human Demonstrations to Dexterous Skills</sub> | 29 | 164 | [手—物交互重建](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/hand-object-reconstruction-for-transfer/README.md) — C 0 · A 1<br>[视频到机器人示教](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/video-to-robot-demonstrations/README.md) — C 27 · A 151<br>[示教精炼与技能迁移](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/demonstration-refinement-skill-transfer/README.md) — C 2 · A 12<br>[待审专题](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>04 · 导航、定位与多机器人协作 · Navigation, Localization & Multi-robot Coordination</strong><br><sub>905 篇顶会 · 6,386 篇 arXiv · 4 个二级子领域 · 16 个最细目录</sub></summary>

论文主要如何推进导航、定位与多机器人协作？

**研究流程：** 传感数据 → 地图与目标 → 规划 → 导航

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Navigation%2C%20Localization%20%26%20Multi-robot%20Coordination#research-workbench) · [顶会目录](papers/tracks/navigation-localization-multi-robot-coordination.md) · [arXiv 目录](papers/arxiv/navigation-localization-multi-robot-coordination/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 定位与建图<br><sub>Localization & Mapping</sub> | 320 | 2,904 | [视觉／激光／多传感器 SLAM](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/visual-lidar-multisensor-slam/README.md) — C 16 · A 547<br>[里程计与重定位](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/odometry-relocalization/README.md) — C 59 · A 1,046<br>[语义与神经地图](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/semantic-neural-maps/README.md) — C 50 · A 383<br>[待审专题](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/pending-specialty-review/README.md) — C 195 · A 928 |
| 目标与语言导航<br><sub>Goal & Language Navigation</sub> | 88 | 477 | [点目标与图像目标导航](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/point-goal-image-goal-navigation/README.md) — C 21 · A 89<br>[物体目标与语义导航](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/object-goal-semantic-navigation/README.md) — C 33 · A 125<br>[视觉语言导航](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/vision-language-navigation/README.md) — C 34 · A 263<br>[待审专题](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/pending-specialty-review/README.md) — C 0 · A 0 |
| 运动规划与探索<br><sub>Motion Planning & Exploration</sub> | 367 | 2,341 | [全局路径规划](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/global-path-planning/README.md) — C 176 · A 1,272<br>[局部避障与轨迹优化](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/local-avoidance-trajectory-optimization/README.md) — C 37 · A 485<br>[主动探索与信息增益](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/active-exploration-information-gain/README.md) — C 154 · A 584<br>[待审专题](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/pending-specialty-review/README.md) — C 0 · A 0 |
| 多机器人与社会导航<br><sub>Multi-robot & Social Navigation</sub> | 130 | 664 | [多机器人协调](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/multi-robot-coordination/README.md) — C 61 · A 358<br>[群体与编队](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/swarms-formation/README.md) — C 11 · A 124<br>[人群交互与社会规范导航](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/human-aware-social-navigation/README.md) — C 58 · A 182<br>[待审专题](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>05 · 足式运动与全身控制 · Legged Locomotion & Whole-body Control</strong><br><sub>753 篇顶会 · 2,365 篇 arXiv · 5 个二级子领域 · 20 个最细目录</sub></summary>

论文主要如何推进足式运动与全身控制？

**研究流程：** 参考动作 → 接触与地形 → 全身控制 → 运动

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Legged%20Locomotion%20%26%20Whole-body%20Control#research-workbench) · [顶会目录](papers/tracks/legged-locomotion-whole-body-control.md) · [arXiv 目录](papers/arxiv/legged-locomotion-whole-body-control/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 双足与人形运动<br><sub>Bipedal & Humanoid Locomotion</sub> | 413 | 1,115 | [行走与步态](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/walking-gaits/README.md) — C 187 · A 414<br>[跑跳与敏捷运动](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/running-jumping-agile-motion/README.md) — C 28 · A 123<br>[复杂地形与落脚规划](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/terrain-footstep-planning/README.md) — C 15 · A 43<br>[待审专题](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/pending-specialty-review/README.md) — C 183 · A 535 |
| 四足与多足运动<br><sub>Quadruped & Multilegged Locomotion</sub> | 238 | 507 | [步态与运动控制](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/gaits-locomotion-control/README.md) — C 229 · A 470<br>[地形适应](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/terrain-adaptation/README.md) — C 9 · A 36<br>[动态恢复与敏捷技能](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/dynamic-recovery-agility/README.md) — C 0 · A 1<br>[待审专题](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/pending-specialty-review/README.md) — C 0 · A 0 |
| 全身协调与平衡<br><sub>Whole-body Coordination & Balance</sub> | 57 | 285 | [全身优化控制](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/whole-body-optimization-control/README.md) — C 39 · A 181<br>[平衡与接触调节](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/balance-contact-regulation/README.md) — C 10 · A 74<br>[跌倒预防与恢复](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/fall-prevention-recovery/README.md) — C 8 · A 30<br>[待审专题](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/pending-specialty-review/README.md) — C 0 · A 0 |
| 全身动作迁移<br><sub>Whole-body Motion Transfer</sub> | 31 | 305 | [人体到机器人运动学重定向](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/human-to-robot-kinematic-retargeting/README.md) — C 5 · A 29<br>[接触与动力学重定向](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/contact-dynamic-retargeting/README.md) — C 0 · A 0<br>[动作模仿与生成](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/motion-imitation-generation/README.md) — C 26 · A 276<br>[待审专题](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/pending-specialty-review/README.md) — C 0 · A 0 |
| 移动与操作协同<br><sub>Locomotion-Manipulation Coordination</sub> | 14 | 153 | [人形移动操作](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/humanoid-loco-manipulation/README.md) — C 14 · A 145<br>[多接触交互](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/multicontact-interaction/README.md) — C 0 · A 4<br>[腿臂协同与上肢任务](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/leg-arm-upper-body-coordination/README.md) — C 0 · A 4<br>[待审专题](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>06 · 感知、表征与状态估计 · Perception, Representation & State Estimation</strong><br><sub>361 篇顶会 · 3,116 篇 arXiv · 5 个二级子领域 · 20 个最细目录</sub></summary>

论文主要如何推进感知、表征与状态估计？

**研究流程：** 传感观测 → 表征 → 状态估计 → 任务信息

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Perception%2C%20Representation%20%26%20State%20Estimation#research-workbench) · [顶会目录](papers/tracks/perception-representation-state-estimation.md) · [arXiv 目录](papers/arxiv/perception-representation-state-estimation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 三维环境感知<br><sub>3D Environment Perception</sub> | 133 | 1,578 | [深度与点云](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/depth-point-clouds/README.md) — C 17 · A 461<br>[三维重建](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/3d-reconstruction/README.md) — C 10 · A 229<br>[占据与场景表达](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/occupancy-scene-representation/README.md) — C 32 · A 341<br>[待审专题](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/pending-specialty-review/README.md) — C 74 · A 547 |
| 物体与交互感知<br><sub>Object & Interaction Perception</sub> | 90 | 779 | [物体检测与分割](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/detection-segmentation/README.md) — C 26 · A 520<br>[六维姿态与跟踪](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/6d-pose-tracking/README.md) — C 33 · A 194<br>[可供性与交互关系](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/affordances-interaction-relations/README.md) — C 31 · A 65<br>[待审专题](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/pending-specialty-review/README.md) — C 0 · A 0 |
| 人体与手—物感知<br><sub>Human & Hand-object Perception</sub> | 11 | 84 | [人体与手部姿态](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/body-hand-pose/README.md) — C 3 · A 45<br>[手—物交互重建](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/hand-object-interaction-reconstruction/README.md) — C 5 · A 13<br>[接触与运动恢复](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/contact-motion-recovery/README.md) — C 3 · A 26<br>[待审专题](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/pending-specialty-review/README.md) — C 0 · A 0 |
| 触觉与多模态感知<br><sub>Tactile & Multimodal Perception</sub> | 81 | 239 | [触觉表征](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/tactile-representation/README.md) — C 62 · A 126<br>[力、接触与滑移估计](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/force-contact-slip-estimation/README.md) — C 7 · A 29<br>[视觉触觉与本体感知融合](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/visuotactile-proprioceptive-fusion/README.md) — C 12 · A 84<br>[待审专题](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/pending-specialty-review/README.md) — C 0 · A 0 |
| 状态估计与主动感知<br><sub>State Estimation & Active Perception</sub> | 46 | 436 | [多传感器状态估计](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/multisensor-state-estimation/README.md) — C 27 · A 213<br>[标定与时间对齐](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/calibration-time-alignment/README.md) — C 10 · A 159<br>[视角选择与主动观测](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/view-selection-active-observation/README.md) — C 9 · A 64<br>[待审专题](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>07 · 世界模型、规划与具身推理 · World Models, Planning & Embodied Reasoning</strong><br><sub>146 篇顶会 · 1,674 篇 arXiv · 4 个二级子领域 · 16 个最细目录</sub></summary>

论文主要如何推进世界模型、规划与具身推理？

**研究流程：** 经验 → 预测模型与知识 → 推理与规划 → 闭环决策

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=World%20Models%2C%20Planning%20%26%20Embodied%20Reasoning#research-workbench) · [顶会目录](papers/tracks/world-models-planning-embodied-reasoning.md) · [arXiv 目录](papers/arxiv/world-models-planning-embodied-reasoning/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 世界与动力学建模<br><sub>World & Dynamics Modeling</sub> | 38 | 622 | [潜空间动力学](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/latent-dynamics/README.md) — C 22 · A 457<br>[物体与接触动力学](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/object-contact-dynamics/README.md) — C 4 · A 25<br>[动作条件视频预测](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/action-conditioned-video-prediction/README.md) — C 3 · A 81<br>[待审专题](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/pending-specialty-review/README.md) — C 9 · A 59 |
| 模型驱动决策<br><sub>Model-based Decision Making</sub> | 28 | 417 | [模型预测控制](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/model-predictive-control/README.md) — C 13 · A 322<br>[想象训练与模型式 RL](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/imagination-model-based-rl/README.md) — C 14 · A 72<br>[世界模型辅助规划](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/world-model-planning/README.md) — C 1 · A 23<br>[待审专题](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/pending-specialty-review/README.md) — C 0 · A 0 |
| 任务推理与规划<br><sub>Task Reasoning & Planning</sub> | 63 | 391 | [任务分解与符号规划](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/task-decomposition-symbolic-planning/README.md) — C 46 · A 233<br>[语言模型辅助规划](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/language-model-planning/README.md) — C 5 · A 40<br>[具身问答与空间推理](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/embodied-qa-spatial-reasoning/README.md) — C 12 · A 118<br>[待审专题](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/pending-specialty-review/README.md) — C 0 · A 0 |
| 记忆与自主执行<br><sub>Memory & Autonomous Execution</sub> | 17 | 244 | [情景记忆与经验检索](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/episodic-memory-retrieval/README.md) — C 4 · A 67<br>[持续任务执行](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/persistent-task-execution/README.md) — C 1 · A 17<br>[失败检测、纠错与重规划](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/failure-detection-replanning/README.md) — C 12 · A 160<br>[待审专题](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>08 · 数据、仿真与评测 · Data, Simulation & Evaluation</strong><br><sub>311 篇顶会 · 2,563 篇 arXiv · 6 个二级子领域 · 24 个最细目录</sub></summary>

论文主要如何推进数据、仿真与评测？

**研究流程：** 数据或环境 → 生成与验证 → 实验 → 证据

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Data%2C%20Simulation%20%26%20Evaluation#research-workbench) · [顶会目录](papers/tracks/data-simulation-evaluation.md) · [arXiv 目录](papers/arxiv/data-simulation-evaluation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 数据集与数据工程<br><sub>Datasets & Data Engineering</sub> | 103 | 669 | [机器人示教数据集](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/robot-demonstration-datasets/README.md) — C 10 · A 64<br>[人类视频与动作数据](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/human-video-motion-data/README.md) — C 1 · A 35<br>[数据清洗、标注与质量评估](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/data-curation-quality/README.md) — C 10 · A 76<br>[待审专题](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/pending-specialty-review/README.md) — C 82 · A 494 |
| 合成与增强数据<br><sub>Synthetic & Augmented Data</sub> | 13 | 190 | [仿真轨迹生成](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/simulated-trajectory-generation/README.md) — C 2 · A 64<br>[生成模型辅助数据](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/generative-data-augmentation/README.md) — C 11 · A 111<br>[跨机器人数据转换](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/cross-robot-data-conversion/README.md) — C 0 · A 15<br>[待审专题](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/pending-specialty-review/README.md) — C 0 · A 0 |
| 仿真与数字孪生<br><sub>Simulation & Digital Twins</sub> | 31 | 271 | [物理引擎与并行仿真](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/physics-engines-parallel-simulation/README.md) — C 16 · A 106<br>[可微仿真](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/differentiable-simulation/README.md) — C 7 · A 35<br>[现实场景重建与数字孪生](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/real-to-sim-digital-twins/README.md) — C 8 · A 130<br>[待审专题](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/pending-specialty-review/README.md) — C 0 · A 0 |
| 仿真到现实<br><sub>Sim-to-real Transfer</sub> | 55 | 301 | [域随机化](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/domain-randomization/README.md) — C 5 · A 9<br>[系统辨识与仿真校准](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/system-identification-sim-calibration/README.md) — C 1 · A 19<br>[域适配与迁移](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/domain-adaptation-transfer/README.md) — C 49 · A 273<br>[待审专题](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/pending-specialty-review/README.md) — C 0 · A 0 |
| 基准与实验方法<br><sub>Benchmarks & Experimental Methods</sub> | 94 | 802 | [任务与能力基准](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/task-capability-benchmarks/README.md) — C 92 · A 720<br>[泛化与鲁棒性评测](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/generalization-robustness-evaluation/README.md) — C 0 · A 7<br>[复现协议与统计比较](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/reproducibility-statistical-comparison/README.md) — C 2 · A 75<br>[待审专题](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/pending-specialty-review/README.md) — C 0 · A 0 |
| 安全与可靠性评估<br><sub>Safety & Reliability Evaluation</sub> | 15 | 330 | [安全测试与约束验证](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/safety-tests-constraint-verification/README.md) — C 3 · A 74<br>[分布外与不确定性评估](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/ood-uncertainty-evaluation/README.md) — C 9 · A 143<br>[故障与失效分析](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/fault-failure-analysis/README.md) — C 3 · A 113<br>[待审专题](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>09 · 机器人硬件与系统 · Robot Hardware & Systems</strong><br><sub>133 篇顶会 · 981 篇 arXiv · 4 个二级子领域 · 16 个最细目录</sub></summary>

论文主要如何推进机器人硬件与系统？

**研究流程：** 软硬件需求 → 设计 → 集成 → 部署

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Robot%20Hardware%20%26%20Systems#research-workbench) · [顶会目录](papers/tracks/robot-hardware-systems.md) · [arXiv 目录](papers/arxiv/robot-hardware-systems/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 机器人机构与驱动<br><sub>Mechanisms & Actuation</sub> | 65 | 540 | [手、夹爪与机械臂设计](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/hands-grippers-arms/README.md) — C 1 · A 15<br>[腿式与全身机构](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/legged-whole-body-mechanisms/README.md) — C 4 · A 34<br>[执行器与传动](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/actuators-transmission/README.md) — C 33 · A 267<br>[待审专题](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/pending-specialty-review/README.md) — C 27 · A 224 |
| 传感器与人机接口<br><sub>Sensors & Human Interfaces</sub> | 44 | 108 | [触觉与力传感器](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/tactile-force-sensors/README.md) — C 41 · A 60<br>[动作捕捉与可穿戴设备](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/motion-capture-wearables/README.md) — C 2 · A 41<br>[触觉反馈设备](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/haptic-feedback-devices/README.md) — C 1 · A 7<br>[待审专题](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/pending-specialty-review/README.md) — C 0 · A 0 |
| 软体与特殊机器人<br><sub>Soft & Specialized Robots</sub> | 14 | 155 | [软体机构与驱动](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/soft-mechanisms-actuation/README.md) — C 2 · A 63<br>[仿生机器人](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/bio-inspired-robots/README.md) — C 7 · A 70<br>[特殊环境机器人](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/special-environment-robots/README.md) — C 5 · A 22<br>[待审专题](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/pending-specialty-review/README.md) — C 0 · A 0 |
| 计算与部署系统<br><sub>Computing & Deployment Systems</sub> | 10 | 178 | [实时与端侧推理](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/real-time-on-device-inference/README.md) — C 3 · A 59<br>[控制与通信架构](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/control-communication-architecture/README.md) — C 4 · A 72<br>[软件框架与系统集成](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/software-frameworks-integration/README.md) — C 3 · A 47<br>[待审专题](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

## 每篇论文如何定位

以 `AnyDexRT` 为例，其主要路径为：

> 灵巧手、重定向与遥操作 → 灵巧手重定向 → [运动学与姿态重定向](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/kinematic-pose-retargeting/README.md)

| 字段 | 作用 |
|---|---|
| `track` | 一级方向，决定论文处于九方向中的哪一条主线 |
| `subcategory` | 二级子领域，用于区分该方向内的研究问题 |
| `specialty` | 三级专题，也是论文实际挂载的最细目录 |
| `taxonomy_evidence` | 记录最强匹配来自标题或摘要以及对应短语 |
| `classification_status` | 区分标题/摘要核查例外、规则归类与待审；不代表全文精读 |
| `method_tags / embodiment_tags / data_tags / related_topics` | 跨分类检索标签，不重复计入主分类数量 |
| `source_type` | 区分官方、出版社、文献索引或 arXiv 来源 |

在线工作台的每一行论文都显示可点击的完整分类路径，并提供“最细目录”入口。CSV 与 Markdown 导出也保留三级分类和分类证据。

## 分类与完整性边界

- 顶会层在固定会议、年份、`robot` 检索词、确定性纳入词表和排除规则下构建。
- arXiv 层审计 32,552 条 `cs.RO` 候选，其中 25,257 条按既有纳入边界保留并重组为九方向，7,295 条未满足分类边界。
- 证据不足时使用“待审专题”，不制造虚假的三级精度。
- 每篇顶会论文和每篇 arXiv 论文在最细目录树中恰好出现一次。
- “完整”指覆盖公开、可复现的操作性边界，不声称具身智能存在无争议的语义全集。

## 科研工作台能力

- 9 个一级方向、42 个二级子领域和 168 个最细目录逐级导航；
- 顶会、arXiv 与合并去重三种研究层切换；
- 标题、作者、年份、会议、方向、子领域、专题与来源联合筛选；
- 可分享 URL、阅读清单、Markdown / CSV 导出、中英文与深浅主题；
- 每篇论文均提供在线论文页和来源链接，缺失作者信息不会被推测。

## 仓库结构

```text
├── index.html                         # 双语在线科研工作台
├── README.md / README.zh-CN.md         # 详细英文 / 中文首页
├── data/                               # 顶会层与 arXiv 层机器可读数据
├── papers/taxonomy/                    # 168 个最细目录及完整论文列表
├── papers/tracks/                      # 九方向顶会目录
├── papers/arxiv/                       # 九方向 × 年份 arXiv 目录
├── scripts/taxonomy.py                 # 二级/三级确定性分类规则
├── scripts/render_catalog.py           # README 与论文目录生成器
└── scripts/audit_catalog.py            # 数据、来源与挂载完整性审计
```

## 复现与验证

```bash
python scripts/apply_taxonomy.py --check
python scripts/render_catalog.py
python scripts/audit_catalog.py
python scripts/render_catalog.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
```

## 贡献与许可

提交数据或分类改进前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。仓库自有内容采用 [CC BY-NC-SA 4.0](LICENSE)；论文版权归作者和出版方所有，本项目仅提供在线链接，不重新分发 PDF。
