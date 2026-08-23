<div align="center">
<h1>Embodied AI Paper Analysis</h1>
<p><strong>构建文献地图，追溯研究证据。</strong></p>
<p>面向具身智能科研工作者的双语、可审计文献基础设施</p>
<p><strong><a href="README.md">English</a> · 简体中文</strong></p>
</div>

<p align="center"><img src="assets/research-map.svg" width="100%" alt="具身智能双层证据与七方向研究地图"></p>

> 面向科研工作者的可审计论文工作台：3,724 篇近五年顶会论文、23,823 篇近三年 arXiv 预印本，按 7 个一级方向、40 个二级子领域和 200 个最细论文目录组织。

<p align="center">
<a href="https://dld0621.github.io/Embodied-AI-Paper-Analysis/?lang=zh"><img src="https://img.shields.io/badge/在线科研工作台-打开-2563eb?style=flat-square" alt="在线科研工作台"></a>
<a href="data/papers.json"><img src="https://img.shields.io/badge/顶会论文-3%2C724-111827?style=flat-square" alt="顶会论文"></a>
<a href="data/arxiv_recent.json"><img src="https://img.shields.io/badge/arXiv-23%2C823-b31b1b?style=flat-square" alt="arXiv 预印本"></a>
<a href="papers/taxonomy/README.md"><img src="https://img.shields.io/badge/分类-7%E2%86%9240%E2%86%92200-0891b2?style=flat-square" alt="三级分类"></a>
</p>

## 快速入口

| 目标 | 入口 |
|---|---|
| 搜索、筛选、保存与导出论文 | [在线科研工作台](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?lang=zh#research-workbench) |
| 从 7 个方向逐级浏览到最细专题 | [三级研究分类图](papers/taxonomy/README.md) |
| 浏览近五年顶会层 | [顶会论文总览](papers/README.md) |
| 使用机器可读数据 | [`papers.json`](data/papers.json) · [`arxiv_recent.json`](data/arxiv_recent.json) |

## 项目解决什么问题

本项目不是简单的论文链接集合，而是一套可复现的具身智能文献定位系统。每篇论文同时回答四个问题：它属于哪个一级研究方向、位于哪个二级子领域、落在哪个三级专题，以及这一判断来自标题、主题还是摘要中的什么证据。

顶会记录与 arXiv 预印本严格分层。标题重复不会被解释为会议录用；合并视图只用于阅读去重，原始来源仍分别保留。

## 两个证据层

| 层级 | 时间窗口 | 记录数 | 学术含义 |
|---|---|---:|---|
| 顶会普查 | 2022–2026 | 3,724 | RSS、CoRL、ICRA、IROS、ICLR、ICML、NeurIPS、CVPR、ICCV、ECCV；记录附正式来源层级 |
| arXiv 预印本 | 2023-08-23 至 2026-08-23 | 23,823 | 对完整 `cs.RO` 候选窗口进行分类；不代表顶会录用 |
| 合并去重视图 | 同上 | 25,877 | 按归一化标题去重，优先显示已有会议来源的记录 |

## 七方向三级研究地图

每篇论文只拥有一条主要的 **一级方向 → 二级子领域 → 三级专题** 路径。当前分类包含 160 个明确专题，并为 40 个二级子领域各保留一个“综合与交叉研究”落点，共 200 个最细目录。展开下方任一方向即可查看全部二级、三级分类及其论文数量。

<details>
<summary><strong>01 · 基础模型与 VLA · Foundation Models & VLA</strong><br><sub>318 篇顶会 · 3,536 篇 arXiv · 5 个二级子领域 · 25 个最细目录</sub></summary>

多模态基础模型如何把感知与语言转化为可泛化的机器人动作？

**研究流程：** 图像、语言与状态 → 多模态表征 → 动作生成 → 机器人执行

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Foundation%20Models%20%26%20VLA#research-workbench) · [顶会目录](papers/tracks/foundation-models-vla.md) · [arXiv 目录](papers/arxiv/foundation-models-vla/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| VLA 架构<br><sub>VLA Architectures</sub> | 107 | 1,242 | [动作标记化与解码](papers/taxonomy/foundation-models-vla/vla-architectures/action-tokenization-decoding/README.md) — C 0 · A 63<br>[扩散与流策略](papers/taxonomy/foundation-models-vla/vla-architectures/diffusion-flow-policies/README.md) — C 0 · A 109<br>[分层与混合专家策略](papers/taxonomy/foundation-models-vla/vla-architectures/hierarchical-mixture-policies/README.md) — C 1 · A 22<br>[实时与端侧 VLA](papers/taxonomy/foundation-models-vla/vla-architectures/real-time-on-device-vla/README.md) — C 4 · A 249<br>[综合与交叉研究](papers/taxonomy/foundation-models-vla/vla-architectures/general-cross-cutting/README.md) — C 102 · A 799 |
| 多模态具身对齐<br><sub>Multimodal Grounding</sub> | 108 | 849 | [视觉语言对齐](papers/taxonomy/foundation-models-vla/multimodal-grounding/vision-language-grounding/README.md) — C 62 · A 574<br>[语言条件控制](papers/taxonomy/foundation-models-vla/multimodal-grounding/language-conditioned-control/README.md) — C 18 · A 73<br>[三维与空间对齐](papers/taxonomy/foundation-models-vla/multimodal-grounding/3d-spatial-grounding/README.md) — C 4 · A 33<br>[音频、触觉与多感官模型](papers/taxonomy/foundation-models-vla/multimodal-grounding/audio-touch-multisensory-models/README.md) — C 1 · A 71<br>[综合与交叉研究](papers/taxonomy/foundation-models-vla/multimodal-grounding/general-cross-cutting/README.md) — C 23 · A 98 |
| 推理、规划与智能体<br><sub>Reasoning, Planning & Agents</sub> | 53 | 772 | [任务与长时程规划](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/task-long-horizon-planning/README.md) — C 29 · A 228<br>[智能体机器人系统](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/agentic-robot-systems/README.md) — C 3 · A 177<br>[具身推理与问答](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/embodied-reasoning-question-answering/README.md) — C 2 · A 92<br>[失败检测与自纠正](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/failure-detection-self-correction/README.md) — C 1 · A 67<br>[综合与交叉研究](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/general-cross-cutting/README.md) — C 18 · A 208 |
| 预训练、规模化与迁移<br><sub>Pretraining, Scaling & Transfer</sub> | 44 | 457 | [机器人预训练与基础策略](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/robot-pretraining-foundation-policies/README.md) — C 3 · A 59<br>[跨本体与形态迁移](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/cross-embodiment-morphology-transfer/README.md) — C 3 · A 24<br>[数据规模化与混合设计](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/data-scaling-mixture-design/README.md) — C 0 · A 4<br>[微调、少样本与适配](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/fine-tuning-few-shot-adaptation/README.md) — C 7 · A 189<br>[综合与交叉研究](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/general-cross-cutting/README.md) — C 31 · A 181 |
| 记忆与世界知识<br><sub>Memory & World Knowledge</sub> | 6 | 216 | [情景与语义记忆](papers/taxonomy/foundation-models-vla/memory-world-knowledge/episodic-semantic-memory/README.md) — C 1 · A 13<br>[世界动作与预测模型](papers/taxonomy/foundation-models-vla/memory-world-knowledge/world-action-predictive-models/README.md) — C 1 · A 50<br>[检索增强机器人](papers/taxonomy/foundation-models-vla/memory-world-knowledge/retrieval-augmented-robotics/README.md) — C 2 · A 50<br>[知识图谱与结构化知识](papers/taxonomy/foundation-models-vla/memory-world-knowledge/knowledge-graphs-structured-knowledge/README.md) — C 0 · A 24<br>[综合与交叉研究](papers/taxonomy/foundation-models-vla/memory-world-knowledge/general-cross-cutting/README.md) — C 2 · A 79 |

</details>

<details>
<summary><strong>02 · 操作与模仿学习 · Manipulation & Imitation</strong><br><sub>941 篇顶会 · 4,238 篇 arXiv · 5 个二级子领域 · 25 个最细目录</sub></summary>

机器人如何从示范与交互中获得精确、稳健的操作技能？

**研究流程：** 示范与观测 → 策略学习 → 动作序列 → 闭环执行

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Manipulation%20%26%20Imitation#research-workbench) · [顶会目录](papers/tracks/manipulation-imitation.md) · [arXiv 目录](papers/arxiv/manipulation-imitation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 抓取与物体交互<br><sub>Grasping & Object Interaction</sub> | 254 | 948 | [抓取检测与生成](papers/taxonomy/manipulation-imitation/grasping-object-interaction/grasp-detection-synthesis/README.md) — C 49 · A 168<br>[抓取稳定性与力控制](papers/taxonomy/manipulation-imitation/grasping-object-interaction/grasp-stability-force-control/README.md) — C 6 · A 59<br>[夹爪、吸盘与末端执行器](papers/taxonomy/manipulation-imitation/grasping-object-interaction/grippers-suction-end-effectors/README.md) — C 22 · A 299<br>[拾放与物体重排](papers/taxonomy/manipulation-imitation/grasping-object-interaction/pick-place-object-rearrangement/README.md) — C 36 · A 163<br>[综合与交叉研究](papers/taxonomy/manipulation-imitation/grasping-object-interaction/general-cross-cutting/README.md) — C 141 · A 259 |
| 接触丰富与可变形操作<br><sub>Contact-rich & Deformable Manipulation</sub> | 160 | 758 | [插入、装配与精密任务](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/insertion-assembly-precision-tasks/README.md) — C 77 · A 329<br>[推、滑与非抓取技能](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/pushing-sliding-non-prehensile-skills/README.md) — C 21 · A 86<br>[工具使用与关节物体](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/tool-use-articulated-objects/README.md) — C 5 · A 64<br>[布料、绳索与软体物体](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/cloth-rope-soft-objects/README.md) — C 23 · A 121<br>[综合与交叉研究](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/general-cross-cutting/README.md) — C 34 · A 158 |
| 模仿与示范学习<br><sub>Imitation & Demonstration Learning</sub> | 96 | 668 | [行为克隆与序列建模](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/behavior-cloning-sequence-modeling/README.md) — C 6 · A 97<br>[从示范中学习](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/learning-from-demonstration/README.md) — C 2 · A 127<br>[单样本、少样本与技能迁移](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/one-shot-few-shot-skill-transfer/README.md) — C 16 · A 74<br>[技能发现与示范分段](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/skill-discovery-demonstration-segmentation/README.md) — C 2 · A 10<br>[综合与交叉研究](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/general-cross-cutting/README.md) — C 70 · A 360 |
| 操作策略学习<br><sub>Manipulation Policy Learning</sub> | 393 | 1,543 | [强化学习与离线强化学习](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/reinforcement-offline-rl/README.md) — C 21 · A 318<br>[视觉运动与闭环策略](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/visuomotor-closed-loop-policies/README.md) — C 19 · A 238<br>[生成式与扩散策略](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/generative-diffusion-policies/README.md) — C 12 · A 248<br>[基于模型的控制与轨迹优化](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/model-based-control-trajectory-optimization/README.md) — C 8 · A 137<br>[综合与交叉研究](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/general-cross-cutting/README.md) — C 333 · A 602 |
| 长时程与移动操作<br><sub>Long-horizon & Mobile Manipulation</sub> | 38 | 321 | [长时程任务执行](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/long-horizon-task-execution/README.md) — C 10 · A 143<br>[移动操作](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/mobile-manipulation/README.md) — C 3 · A 53<br>[任务与运动规划](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/task-and-motion-planning/README.md) — C 5 · A 18<br>[家居、工业与开放世界任务](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/household-industrial-open-world-tasks/README.md) — C 3 · A 37<br>[综合与交叉研究](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/general-cross-cutting/README.md) — C 17 · A 70 |

</details>

<details>
<summary><strong>03 · 灵巧操作与遥操作 · Dexterity & Teleoperation</strong><br><sub>339 篇顶会 · 1,049 篇 arXiv · 6 个二级子领域 · 30 个最细目录</sub></summary>

灵巧手、触觉信号与遥操作接口如何支撑接触丰富的控制？

**研究流程：** 人体、视觉与触觉 → 重定向或接触模型 → 手臂协同控制 → 任务结果

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Dexterity%20%26%20Teleoperation#research-workbench) · [顶会目录](papers/tracks/dexterity-teleoperation.md) · [arXiv 目录](papers/arxiv/dexterity-teleoperation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 灵巧手控制<br><sub>Dexterous Hand Control</sub> | 133 | 354 | [多指控制与协调](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/multifinger-control-coordination/README.md) — C 14 · A 33<br>[手部设计、驱动与形态](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/hand-design-actuation-morphology/README.md) — C 5 · A 61<br>[灵巧抓取](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/dexterous-grasping/README.md) — C 7 · A 21<br>[跨手型泛化](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/cross-hand-generalization/README.md) — C 0 · A 4<br>[综合与交叉研究](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/general-cross-cutting/README.md) — C 107 · A 235 |
| 手内操作<br><sub>In-hand Manipulation</sub> | 61 | 133 | [物体重定向与旋转](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/object-reorientation-rotation/README.md) — C 3 · A 27<br>[滚动、滑动与手指步态](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/rolling-sliding-finger-gaiting/README.md) — C 1 · A 7<br>[滑移、稳定与接触保持](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/slip-stability-contact-maintenance/README.md) — C 1 · A 4<br>[手内感知与状态估计](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/in-hand-sensing-state-estimation/README.md) — C 1 · A 1<br>[综合与交叉研究](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/general-cross-cutting/README.md) — C 55 · A 94 |
| 双手协同<br><sub>Bimanual Coordination</sub> | 45 | 101 | [双手操作](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/bimanual-manipulation/README.md) — C 16 · A 36<br>[双臂规划与控制](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/dual-arm-planning-control/README.md) — C 0 · A 1<br>[交接与协作任务](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/handovers-collaborative-tasks/README.md) — C 6 · A 12<br>[双手装配与可变形操作](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/bimanual-assembly-deformables/README.md) — C 4 · A 3<br>[综合与交叉研究](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/general-cross-cutting/README.md) — C 19 · A 49 |
| 遥操作与共享自主<br><sub>Teleoperation & Shared Autonomy</sub> | 66 | 229 | [VR、XR 与沉浸式遥操作](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/vr-xr-immersive-teleoperation/README.md) — C 7 · A 43<br>[双边与主从控制](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/bilateral-master-slave-control/README.md) — C 4 · A 18<br>[共享自主与辅助](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/shared-autonomy-assistance/README.md) — C 8 · A 25<br>[远程临场、时延与通信](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/remote-presence-delay-communication/README.md) — C 1 · A 37<br>[综合与交叉研究](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/general-cross-cutting/README.md) — C 46 · A 106 |
| 重定向与人体动作<br><sub>Retargeting & Human Motion</sub> | 18 | 119 | [手部姿态重定向](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/hand-pose-retargeting/README.md) — C 2 · A 4<br>[全身与动作重定向](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/whole-body-motion-retargeting/README.md) — C 3 · A 20<br>[动作捕捉与可穿戴输入](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/motion-capture-wearable-input/README.md) — C 0 · A 5<br>[跨本体示范迁移](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/cross-embodiment-demonstration-transfer/README.md) — C 8 · A 81<br>[综合与交叉研究](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/general-cross-cutting/README.md) — C 5 · A 9 |
| 触觉与力觉接口<br><sub>Tactile & Haptic Interfaces</sub> | 16 | 113 | [触觉感知与表征](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/tactile-sensing-representation/README.md) — C 7 · A 55<br>[力触觉反馈与渲染](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/haptic-feedback-rendering/README.md) — C 4 · A 54<br>[接触与力估计](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/contact-force-estimation/README.md) — C 0 · A 1<br>[可穿戴与人机接口](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/wearable-human-interfaces/README.md) — C 2 · A 1<br>[综合与交叉研究](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/general-cross-cutting/README.md) — C 3 · A 2 |

</details>

<details>
<summary><strong>04 · 导航与具身智能体 · Navigation & Embodied Agents</strong><br><sub>807 篇顶会 · 6,728 篇 arXiv · 6 个二级子领域 · 30 个最细目录</sub></summary>

智能体如何在开放环境中建立空间记忆、规划并完成长时程行动？

**研究流程：** 第一视角感知与目标 → 世界状态与记忆 → 规划 → 导航与交互

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Navigation%20%26%20Embodied%20Agents#research-workbench) · [顶会目录](papers/tracks/navigation-embodied-agents.md) · [arXiv 目录](papers/arxiv/navigation-embodied-agents/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 视觉与语言导航<br><sub>Visual & Language Navigation</sub> | 18 | 198 | [视觉语言导航](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/vision-language-navigation/README.md) — C 4 · A 103<br>[物体目标与语义导航](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/object-goal-semantic-navigation/README.md) — C 7 · A 52<br>[图像目标、点目标与检索导航](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/image-goal-point-goal-retrieval-navigation/README.md) — C 4 · A 29<br>[具身问答与交互导航](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/embodied-qa-interactive-navigation/README.md) — C 2 · A 14<br>[综合与交叉研究](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/general-cross-cutting/README.md) — C 1 · A 0 |
| 建图与定位<br><sub>Mapping & Localization</sub> | 42 | 1,653 | [视觉、激光与多传感器 SLAM](papers/taxonomy/navigation-embodied-agents/mapping-localization/visual-lidar-multi-sensor-slam/README.md) — C 3 · A 603<br>[视觉惯性与激光里程计](papers/taxonomy/navigation-embodied-agents/mapping-localization/visual-inertial-lidar-odometry/README.md) — C 7 · A 254<br>[地点识别与回环检测](papers/taxonomy/navigation-embodied-agents/mapping-localization/place-recognition-loop-closure/README.md) — C 1 · A 220<br>[语义、度量与神经地图](papers/taxonomy/navigation-embodied-agents/mapping-localization/semantic-metric-neural-maps/README.md) — C 8 · A 58<br>[综合与交叉研究](papers/taxonomy/navigation-embodied-agents/mapping-localization/general-cross-cutting/README.md) — C 23 · A 518 |
| 运动与路径规划<br><sub>Motion & Path Planning</sub> | 546 | 3,767 | [全局搜索与路径规划](papers/taxonomy/navigation-embodied-agents/motion-path-planning/global-search-path-planning/README.md) — C 81 · A 602<br>[局部规划与避障](papers/taxonomy/navigation-embodied-agents/motion-path-planning/local-planning-obstacle-avoidance/README.md) — C 12 · A 365<br>[轨迹优化与模型预测控制](papers/taxonomy/navigation-embodied-agents/motion-path-planning/trajectory-optimization-mpc/README.md) — C 16 · A 400<br>[采样、学习与安全感知规划](papers/taxonomy/navigation-embodied-agents/motion-path-planning/sampling-learning-safety-aware-planning/README.md) — C 9 · A 234<br>[综合与交叉研究](papers/taxonomy/navigation-embodied-agents/motion-path-planning/general-cross-cutting/README.md) — C 428 · A 2,166 |
| 探索与主动建图<br><sub>Exploration & Active Mapping</sub> | 117 | 401 | [前沿与覆盖探索](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/frontier-coverage-exploration/README.md) — C 3 · A 49<br>[下一最佳视角与信息增益](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/next-best-view-information-gain/README.md) — C 4 · A 35<br>[主动建图与重建](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/active-mapping-reconstruction/README.md) — C 0 · A 11<br>[搜索、巡检与发现](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/search-inspection-discovery/README.md) — C 2 · A 75<br>[综合与交叉研究](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/general-cross-cutting/README.md) — C 108 · A 231 |
| 多智能体与社会导航<br><sub>Multi-agent & Social Navigation</sub> | 68 | 372 | [多机器人协同](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/multi-robot-coordination/README.md) — C 54 · A 251<br>[集群导航与编队](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/swarm-navigation-formation/README.md) — C 3 · A 44<br>[社会与人类感知导航](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/social-human-aware-navigation/README.md) — C 8 · A 37<br>[多智能体避碰](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/multi-agent-collision-avoidance/README.md) — C 0 · A 3<br>[综合与交叉研究](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/general-cross-cutting/README.md) — C 3 · A 37 |
| 野外、空中与海洋机器人<br><sub>Field, Aerial & Marine Robotics</sub> | 16 | 337 | [空中与无人机导航](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/aerial-uav-navigation/README.md) — C 0 · A 99<br>[自动驾驶与地面车辆](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/autonomous-driving-ground-vehicles/README.md) — C 9 · A 138<br>[海洋与水下自主](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/marine-underwater-autonomy/README.md) — C 2 · A 39<br>[户外、农业与配送机器人](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/outdoor-agricultural-delivery-robots/README.md) — C 4 · A 7<br>[综合与交叉研究](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/general-cross-cutting/README.md) — C 1 · A 54 |

</details>

<details>
<summary><strong>05 · 人形机器人与运动控制 · Humanoids & Locomotion</strong><br><sub>670 篇顶会 · 2,577 篇 arXiv · 6 个二级子领域 · 30 个最细目录</sub></summary>

全身策略如何实现敏捷、稳定且可迁移的运动？

**研究流程：** 动作参考与指令 → 重定向或强化学习 → 全身控制 → 仿真到现实部署

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Humanoids%20%26%20Locomotion#research-workbench) · [顶会目录](papers/tracks/humanoids-locomotion.md) · [arXiv 目录](papers/arxiv/humanoids-locomotion/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 人形全身控制<br><sub>Humanoid Whole-body Control</sub> | 223 | 1,011 | [全身跟踪与控制](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/whole-body-tracking-control/README.md) — C 15 · A 197<br>[人形移动操作](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/humanoid-loco-manipulation/README.md) — C 22 · A 155<br>[上肢技能与协调](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/upper-body-skills-coordination/README.md) — C 2 · A 30<br>[人形遥操作与交互](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/humanoid-teleoperation-interaction/README.md) — C 3 · A 25<br>[综合与交叉研究](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/general-cross-cutting/README.md) — C 181 · A 604 |
| 双足与人形运动<br><sub>Bipedal & Humanoid Locomotion</sub> | 130 | 493 | [行走与步态控制](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/walking-gait-control/README.md) — C 62 · A 265<br>[跑跳与敏捷技能](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/running-jumping-agile-skills/README.md) — C 18 · A 141<br>[楼梯、地形与崎岖地面通行](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/stairs-terrain-rough-ground-traversal/README.md) — C 12 · A 63<br>[落脚点与接触规划](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/footstep-contact-planning/README.md) — C 6 · A 9<br>[综合与交叉研究](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/general-cross-cutting/README.md) — C 32 · A 15 |
| 四足与多足运动<br><sub>Quadruped & Legged Locomotion</sub> | 294 | 663 | [四足运动](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/quadruped-locomotion/README.md) — C 144 · A 355<br>[通用腿式与多足控制](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/general-legged-multi-legged-control/README.md) — C 140 · A 292<br>[地形适应与通行](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/terrain-adaptation-traversal/README.md) — C 2 · A 5<br>[敏捷、恢复与动态机动](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/agility-recovery-dynamic-maneuvers/README.md) — C 8 · A 11<br>[综合与交叉研究](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/general-cross-cutting/README.md) — C 0 · A 0 |
| 动作模仿与生成<br><sub>Motion Imitation & Generation</sub> | 1 | 121 | [参考动作模仿](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/reference-motion-imitation/README.md) — C 0 · A 18<br>[语言条件动作生成](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/language-conditioned-motion-generation/README.md) — C 0 · A 58<br>[风格化、表现性与类人动作](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/style-expressive-human-like-motion/README.md) — C 1 · A 12<br>[动作先验与行为模型](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/motion-priors-behavioral-models/README.md) — C 0 · A 3<br>[综合与交叉研究](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/general-cross-cutting/README.md) — C 0 · A 30 |
| 平衡、动力学与恢复<br><sub>Balance, Dynamics & Recovery</sub> | 15 | 155 | [平衡与稳定控制](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/balance-stability-control/README.md) — C 2 · A 34<br>[动力学、MPC 与全身优化](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/dynamics-mpc-whole-body-optimization/README.md) — C 5 · A 52<br>[防跌倒与恢复](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/fall-prevention-recovery/README.md) — C 3 · A 12<br>[状态、接触与力估计](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/state-contact-force-estimation/README.md) — C 1 · A 11<br>[综合与交叉研究](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/general-cross-cutting/README.md) — C 4 · A 46 |
| 硬件与机器人形态<br><sub>Hardware & Morphology</sub> | 7 | 134 | [驱动器、关节与传动](papers/taxonomy/humanoids-locomotion/hardware-morphology/actuators-joints-transmission/README.md) — C 0 · A 28<br>[足部、腿部与机械设计](papers/taxonomy/humanoids-locomotion/hardware-morphology/feet-legs-mechanical-design/README.md) — C 0 · A 11<br>[肌骨与仿生机器人](papers/taxonomy/humanoids-locomotion/hardware-morphology/musculoskeletal-bio-inspired-robots/README.md) — C 5 · A 53<br>[形态与协同设计](papers/taxonomy/humanoids-locomotion/hardware-morphology/morphology-co-design/README.md) — C 2 · A 26<br>[综合与交叉研究](papers/taxonomy/humanoids-locomotion/hardware-morphology/general-cross-cutting/README.md) — C 0 · A 16 |

</details>

<details>
<summary><strong>06 · 感知与世界模型 · Perception & World Models</strong><br><sub>317 篇顶会 · 2,426 篇 arXiv · 6 个二级子领域 · 30 个最细目录</sub></summary>

机器人如何估计任务相关状态并预测动作后果？

**研究流程：** 视觉、触觉与本体感知 → 状态表征 → 世界预测 → 策略条件

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Perception%20%26%20World%20Models#research-workbench) · [顶会目录](papers/tracks/perception-world-models.md) · [arXiv 目录](papers/arxiv/perception-world-models/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 三维场景感知<br><sub>3D Scene Perception</sub> | 44 | 831 | [点云与激光感知](papers/taxonomy/perception-world-models/3d-scene-perception/point-cloud-lidar-perception/README.md) — C 1 · A 356<br>[深度、双目与 RGB-D](papers/taxonomy/perception-world-models/3d-scene-perception/depth-stereo-rgb-d/README.md) — C 1 · A 111<br>[三维重建、NeRF 与高斯泼溅](papers/taxonomy/perception-world-models/3d-scene-perception/3d-reconstruction-nerf-gaussian-splatting/README.md) — C 2 · A 107<br>[占据与场景表征](papers/taxonomy/perception-world-models/3d-scene-perception/occupancy-scene-representation/README.md) — C 1 · A 73<br>[综合与交叉研究](papers/taxonomy/perception-world-models/3d-scene-perception/general-cross-cutting/README.md) — C 39 · A 184 |
| 物体、姿态与可供性感知<br><sub>Object, Pose & Affordance Perception</sub> | 53 | 560 | [物体检测与分割](papers/taxonomy/perception-world-models/object-pose-affordance-perception/object-detection-segmentation/README.md) — C 0 · A 256<br>[六维姿态与关键点估计](papers/taxonomy/perception-world-models/object-pose-affordance-perception/6d-pose-keypoint-estimation/README.md) — C 21 · A 223<br>[可供性与交互预测](papers/taxonomy/perception-world-models/object-pose-affordance-perception/affordance-interaction-prediction/README.md) — C 31 · A 72<br>[关节物体与物体中心感知](papers/taxonomy/perception-world-models/object-pose-affordance-perception/articulated-object-centric-perception/README.md) — C 1 · A 3<br>[综合与交叉研究](papers/taxonomy/perception-world-models/object-pose-affordance-perception/general-cross-cutting/README.md) — C 0 · A 6 |
| 状态估计与跟踪<br><sub>State Estimation & Tracking</sub> | 27 | 376 | [物体与多目标跟踪](papers/taxonomy/perception-world-models/state-estimation-tracking/object-multi-target-tracking/README.md) — C 1 · A 82<br>[机器人状态与视觉里程计](papers/taxonomy/perception-world-models/state-estimation-tracking/robot-state-visual-odometry/README.md) — C 6 · A 75<br>[标定与传感器融合](papers/taxonomy/perception-world-models/state-estimation-tracking/calibration-sensor-fusion/README.md) — C 1 · A 81<br>[场景流与动态状态估计](papers/taxonomy/perception-world-models/state-estimation-tracking/scene-flow-dynamic-state-estimation/README.md) — C 1 · A 28<br>[综合与交叉研究](papers/taxonomy/perception-world-models/state-estimation-tracking/general-cross-cutting/README.md) — C 18 · A 110 |
| 触觉与多模态感知<br><sub>Tactile & Multimodal Perception</sub> | 148 | 258 | [触觉识别与表征](papers/taxonomy/perception-world-models/tactile-multimodal-perception/tactile-recognition-representation/README.md) — C 6 · A 21<br>[力、接触与滑移感知](papers/taxonomy/perception-world-models/tactile-multimodal-perception/force-contact-slip-perception/README.md) — C 7 · A 12<br>[视触觉与多感官融合](papers/taxonomy/perception-world-models/tactile-multimodal-perception/visuotactile-multisensory-fusion/README.md) — C 9 · A 34<br>[本体感知与具身传感](papers/taxonomy/perception-world-models/tactile-multimodal-perception/proprioception-embodied-sensing/README.md) — C 5 · A 14<br>[综合与交叉研究](papers/taxonomy/perception-world-models/tactile-multimodal-perception/general-cross-cutting/README.md) — C 121 · A 177 |
| 世界与动力学模型<br><sub>World & Dynamics Models</sub> | 32 | 357 | [潜空间世界模型](papers/taxonomy/perception-world-models/world-dynamics-models/latent-world-models/README.md) — C 25 · A 285<br>[物体中心与结构化动力学](papers/taxonomy/perception-world-models/world-dynamics-models/object-centric-structured-dynamics/README.md) — C 1 · A 3<br>[视频与未来预测](papers/taxonomy/perception-world-models/world-dynamics-models/video-future-prediction/README.md) — C 1 · A 3<br>[物理先验与神经动力学](papers/taxonomy/perception-world-models/world-dynamics-models/physics-informed-neural-dynamics/README.md) — C 5 · A 46<br>[综合与交叉研究](papers/taxonomy/perception-world-models/world-dynamics-models/general-cross-cutting/README.md) — C 0 · A 20 |
| 主动与多视角感知<br><sub>Active & Multiview Perception</sub> | 13 | 44 | [下一最佳视角与视角规划](papers/taxonomy/perception-world-models/active-multiview-perception/next-best-view-view-planning/README.md) — C 0 · A 6<br>[主动感知与信息采集](papers/taxonomy/perception-world-models/active-multiview-perception/active-perception-information-gathering/README.md) — C 7 · A 25<br>[多视角融合与一致性](papers/taxonomy/perception-world-models/active-multiview-perception/multiview-fusion-consistency/README.md) — C 1 · A 6<br>[遮挡感知与交互式感知](papers/taxonomy/perception-world-models/active-multiview-perception/occlusion-aware-interactive-perception/README.md) — C 5 · A 7<br>[综合与交叉研究](papers/taxonomy/perception-world-models/active-multiview-perception/general-cross-cutting/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>07 · 仿真、数据与评测 · Simulation, Data & Evaluation</strong><br><sub>332 篇顶会 · 3,269 篇 arXiv · 6 个二级子领域 · 30 个最细目录</sub></summary>

如何可复现地训练、压力测试并比较具身智能系统？

**研究流程：** 资产与任务定义 → 仿真与数据生成 → 评测协议 → 指标与误差分析

[打开合并论文视图](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Simulation%2C%20Data%20%26%20Evaluation#research-workbench) · [顶会目录](papers/tracks/simulation-data-evaluation.md) · [arXiv 目录](papers/arxiv/simulation-data-evaluation/README.md)

| 二级子领域 | 顶会 | arXiv | 三级专题与论文目录 |
|---|---:|---:|---|
| 仿真与数字孪生<br><sub>Simulation & Digital Twins</sub> | 108 | 1,457 | [物理引擎与机器人仿真器](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/physics-engines-robot-simulators/README.md) — C 7 · A 165<br>[可微与神经仿真](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/differentiable-neural-simulation/README.md) — C 6 · A 41<br>[数字孪生与现实到仿真重建](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/digital-twins-real-to-sim-reconstruction/README.md) — C 11 · A 214<br>[大规模并行仿真](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/large-scale-parallel-simulation/README.md) — C 3 · A 21<br>[综合与交叉研究](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/general-cross-cutting/README.md) — C 81 · A 1,016 |
| 仿真到现实与域适配<br><sub>Sim-to-real & Domain Adaptation</sub> | 62 | 293 | [域随机化](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/domain-randomization/README.md) — C 8 · A 27<br>[系统辨识与校准](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/system-identification-calibration/README.md) — C 0 · A 14<br>[域适配与迁移](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/domain-adaptation-transfer/README.md) — C 14 · A 163<br>[现实差距评估](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/reality-gap-evaluation/README.md) — C 0 · A 10<br>[综合与交叉研究](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/general-cross-cutting/README.md) — C 40 · A 79 |
| 数据集与数据引擎<br><sub>Datasets & Data Engines</sub> | 104 | 821 | [机器人数据集与语料库](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/robot-datasets-corpora/README.md) — C 90 · A 635<br>[示范与轨迹数据](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/demonstration-trajectory-data/README.md) — C 0 · A 4<br>[合成数据生成](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/synthetic-data-generation/README.md) — C 7 · A 118<br>[数据整理、标注与质量](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/data-curation-annotation-quality/README.md) — C 0 · A 7<br>[综合与交叉研究](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/general-cross-cutting/README.md) — C 7 · A 57 |
| 基准与评测<br><sub>Benchmarks & Evaluation</sub> | 52 | 426 | [任务与能力基准](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/task-capability-benchmarks/README.md) — C 23 · A 231<br>[指标与评测协议](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/metrics-evaluation-protocols/README.md) — C 1 · A 57<br>[稳健性与压力测试](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/robustness-stress-testing/README.md) — C 0 · A 9<br>[真实世界与跨平台评测](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/real-world-cross-platform-evaluation/README.md) — C 0 · A 8<br>[综合与交叉研究](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/general-cross-cutting/README.md) — C 28 · A 121 |
| 训练基础设施与工具<br><sub>Training Infrastructure & Tools</sub> | 5 | 154 | [训练框架与强化学习环境](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/training-frameworks-rl-environments/README.md) — C 0 · A 17<br>[分布式、GPU 与数据系统](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/distributed-gpu-data-systems/README.md) — C 2 · A 13<br>[开源库与工具包](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/open-source-libraries-toolkits/README.md) — C 0 · A 42<br>[部署、运行时与中间件](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/deployment-runtime-middleware/README.md) — C 1 · A 34<br>[综合与交叉研究](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/general-cross-cutting/README.md) — C 2 · A 48 |
| 安全、稳健与可复现性<br><sub>Safety, Robustness & Reproducibility</sub> | 1 | 118 | [安全约束与验证](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/safety-constraints-verification/README.md) — C 0 · A 20<br>[不确定性与分布外测试](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/uncertainty-out-of-distribution-testing/README.md) — C 0 · A 40<br>[失败分析与可靠性](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/failure-analysis-reliability/README.md) — C 0 · A 9<br>[可复现性与标准化](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/reproducibility-standardization/README.md) — C 0 · A 20<br>[综合与交叉研究](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/general-cross-cutting/README.md) — C 1 · A 29 |

</details>

## 每篇论文如何定位

以 `AnyDexRT` 为例，其主要路径为：

> 灵巧操作与遥操作 → 重定向与人体动作 → [手部姿态重定向](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/hand-pose-retargeting/README.md)

| 字段 | 作用 |
|---|---|
| `track` | 一级方向，决定论文处于七方向中的哪一条主线 |
| `subcategory` | 二级子领域，用于区分该方向内的研究问题 |
| `specialty` | 三级专题，也是论文实际挂载的最细目录 |
| `taxonomy_evidence` | 记录最强匹配来自标题、主题或摘要以及对应短语 |
| `source_type` | 区分官方、出版社、文献索引或 arXiv 来源 |

在线工作台的每一行论文都显示可点击的完整分类路径，并提供“最细目录”入口。CSV 与 Markdown 导出也保留三级分类和分类证据。

## 分类与完整性边界

- 顶会层在固定会议、年份、`robot` 检索词、确定性纳入词表和排除规则下构建。
- arXiv 层审计 30,954 条 `cs.RO` 候选，其中 23,823 条进入七方向，7,131 条未满足分类边界。
- 证据不足时使用“综合与交叉研究”，不制造虚假的三级精度。
- 每篇顶会论文和每篇 arXiv 论文在最细目录树中恰好出现一次。
- “完整”指覆盖公开、可复现的操作性边界，不声称具身智能存在无争议的语义全集。

## 科研工作台能力

- 7 个一级方向、40 个二级子领域和 200 个最细目录逐级导航；
- 顶会、arXiv 与合并去重三种研究层切换；
- 标题、作者、年份、会议、方向、子领域、专题与来源联合筛选；
- 可分享 URL、阅读清单、Markdown / CSV 导出、中英文与深浅主题；
- 每篇论文均提供在线论文页和来源链接，缺失作者信息不会被推测。

## 仓库结构

```text
├── index.html                         # 双语在线科研工作台
├── README.md / README.zh-CN.md         # 详细英文 / 中文首页
├── data/                               # 顶会层与 arXiv 层机器可读数据
├── papers/taxonomy/                    # 200 个最细目录及完整论文列表
├── papers/tracks/                      # 七方向顶会目录
├── papers/arxiv/                       # 七方向 × 年份 arXiv 目录
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

## 每周自动更新

[`.github/workflows/arxiv-weekly.yml`](.github/workflows/arxiv-weekly.yml) 每周一 02:10 UTC（北京时间 10:10）重新采集截至执行日的滚动三年 `cs.RO` 窗口。同步器在限流后保留逐页缓存并恢复抓取；仅当数据审计、分类检查、生成一致性、链接检查、单元测试和 `git diff --check` 全部通过时才提交到 `main`。arXiv 预印本始终与顶会录用层分开。

## 贡献与许可

提交数据或分类改进前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。仓库自有内容采用 [CC BY-NC-SA 4.0](LICENSE)；论文版权归作者和出版方所有，本项目仅提供在线链接，不重新分发 PDF。
