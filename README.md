# Embodied AI Paper Analysis

**English · [简体中文](README.zh-CN.md)**

> An auditable research workbench for 3,724 five-year conference papers and 21,411 recent arXiv preprints, organized into 7 directions, 40 level-2 subfields, and 200 finest-grained paper catalogs.

[![Workbench](https://img.shields.io/badge/Research_workbench-open-2563eb?style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)
[![Conference](https://img.shields.io/badge/Conference-3%2C724-111827?style=flat-square)](data/papers.json)
[![arXiv](https://img.shields.io/badge/arXiv-21%2C411-b31b1b?style=flat-square)](data/arxiv_recent.json)
[![Taxonomy](https://img.shields.io/badge/Taxonomy-7%E2%86%9240%E2%86%92200-0891b2?style=flat-square)](papers/taxonomy/README.md)

## Start here

| Goal | Entry point |
|---|---|
| Search, filter, save, and export papers | [Interactive research workbench](https://dld0621.github.io/Embodied-AI-Paper-Analysis/#research-workbench) |
| Browse from seven directions to the finest specialty | [Three-level taxonomy](papers/taxonomy/README.md) |
| Browse the five-year conference layer | [Conference paper overview](papers/README.md) |
| Use machine-readable data | [`papers.json`](data/papers.json) · [`arxiv_recent.json`](data/arxiv_recent.json) |

## What this project provides

This is not a flat list of paper links. It combines a systematic conference census with a reproducible literature-positioning system: every paper states its level-1 direction, level-2 subfield, level-3 specialty, and the title/topic/abstract evidence supporting that assignment.

Conference records and arXiv preprints remain separate evidence layers. A duplicate title never implies conference acceptance; deduplication is used only for the combined reading view while both source records remain available.

## Two evidence layers

| Layer | Window | Records | Research meaning |
|---|---|---:|---|
| Conference census | 2022–2026 | 3,724 | RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV with explicit provenance tiers |
| arXiv preprints | 2024-01-01 to 2026-08-07 | 21,411 | Classified from the complete `cs.RO` candidate window; not evidence of conference acceptance |
| Combined unique view | Same windows | 23,735 | Normalized-title deduplication, preferring an available conference record for display |

## Seven-direction research map

Every paper receives one primary **direction → subfield → specialty** path. The ontology contains 160 named specialties plus one scoped General / Cross-cutting leaf for each of 40 subfields, producing 200 paper destinations. Expand any direction below to inspect every level-2 and level-3 category with live paper counts.

<details>
<summary><strong>01 · Foundation Models & VLA · 基础模型与 VLA</strong><br><sub>318 conference · 3,276 arXiv · 5 subfields · 25 leaf catalogs</sub></summary>

How do multimodal foundation models turn perception and language into general robot actions?

**Research pipeline:** Images + language + state → Multimodal representation → Action generation → Robot execution

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Foundation%20Models%20%26%20VLA#research-workbench) · [Conference catalog](papers/tracks/foundation-models-vla.md) · [arXiv catalog](papers/arxiv/foundation-models-vla/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| VLA Architectures<br><sub>VLA 架构</sub> | 107 | 1,704 | [Action Tokenization & Decoding](papers/taxonomy/foundation-models-vla/vla-architectures/action-tokenization-decoding/README.md) — C 0 · A 8<br>[Diffusion & Flow Policies](papers/taxonomy/foundation-models-vla/vla-architectures/diffusion-flow-policies/README.md) — C 0 · A 29<br>[Hierarchical & Mixture Policies](papers/taxonomy/foundation-models-vla/vla-architectures/hierarchical-mixture-policies/README.md) — C 1 · A 10<br>[Real-time & On-device VLA](papers/taxonomy/foundation-models-vla/vla-architectures/real-time-on-device-vla/README.md) — C 4 · A 66<br>[General / Cross-cutting](papers/taxonomy/foundation-models-vla/vla-architectures/general-cross-cutting/README.md) — C 102 · A 1,591 |
| Multimodal Grounding<br><sub>多模态具身对齐</sub> | 108 | 639 | [Vision-Language Grounding](papers/taxonomy/foundation-models-vla/multimodal-grounding/vision-language-grounding/README.md) — C 62 · A 429<br>[Language-conditioned Control](papers/taxonomy/foundation-models-vla/multimodal-grounding/language-conditioned-control/README.md) — C 18 · A 58<br>[3D & Spatial Grounding](papers/taxonomy/foundation-models-vla/multimodal-grounding/3d-spatial-grounding/README.md) — C 4 · A 14<br>[Audio, Touch & Multisensory Models](papers/taxonomy/foundation-models-vla/multimodal-grounding/audio-touch-multisensory-models/README.md) — C 1 · A 30<br>[General / Cross-cutting](papers/taxonomy/foundation-models-vla/multimodal-grounding/general-cross-cutting/README.md) — C 23 · A 108 |
| Reasoning, Planning & Agents<br><sub>推理、规划与智能体</sub> | 53 | 436 | [Task & Long-horizon Planning](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/task-long-horizon-planning/README.md) — C 29 · A 91<br>[Agentic Robot Systems](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/agentic-robot-systems/README.md) — C 3 · A 94<br>[Embodied Reasoning & Question Answering](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/embodied-reasoning-question-answering/README.md) — C 2 · A 40<br>[Failure Detection & Self-correction](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/failure-detection-self-correction/README.md) — C 1 · A 25<br>[General / Cross-cutting](papers/taxonomy/foundation-models-vla/reasoning-planning-agents/general-cross-cutting/README.md) — C 18 · A 186 |
| Pretraining, Scaling & Transfer<br><sub>预训练、规模化与迁移</sub> | 44 | 363 | [Robot Pretraining & Foundation Policies](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/robot-pretraining-foundation-policies/README.md) — C 3 · A 44<br>[Cross-embodiment & Morphology Transfer](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/cross-embodiment-morphology-transfer/README.md) — C 3 · A 18<br>[Data Scaling & Mixture Design](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/data-scaling-mixture-design/README.md) — C 0 · A 0<br>[Fine-tuning, Few-shot & Adaptation](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/fine-tuning-few-shot-adaptation/README.md) — C 7 · A 75<br>[General / Cross-cutting](papers/taxonomy/foundation-models-vla/pretraining-scaling-transfer/general-cross-cutting/README.md) — C 31 · A 226 |
| Memory & World Knowledge<br><sub>记忆与世界知识</sub> | 6 | 134 | [Episodic & Semantic Memory](papers/taxonomy/foundation-models-vla/memory-world-knowledge/episodic-semantic-memory/README.md) — C 1 · A 7<br>[World-Action & Predictive Models](papers/taxonomy/foundation-models-vla/memory-world-knowledge/world-action-predictive-models/README.md) — C 1 · A 28<br>[Retrieval-augmented Robotics](papers/taxonomy/foundation-models-vla/memory-world-knowledge/retrieval-augmented-robotics/README.md) — C 2 · A 19<br>[Knowledge Graphs & Structured Knowledge](papers/taxonomy/foundation-models-vla/memory-world-knowledge/knowledge-graphs-structured-knowledge/README.md) — C 0 · A 5<br>[General / Cross-cutting](papers/taxonomy/foundation-models-vla/memory-world-knowledge/general-cross-cutting/README.md) — C 2 · A 75 |

</details>

<details>
<summary><strong>02 · Manipulation & Imitation · 操作与模仿学习</strong><br><sub>941 conference · 3,817 arXiv · 5 subfields · 25 leaf catalogs</sub></summary>

How can robots acquire precise, robust manipulation skills from demonstrations and interaction?

**Research pipeline:** Demonstrations + observations → Policy learning → Action sequence → Closed-loop execution

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Manipulation%20%26%20Imitation#research-workbench) · [Conference catalog](papers/tracks/manipulation-imitation.md) · [arXiv catalog](papers/arxiv/manipulation-imitation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Grasping & Object Interaction<br><sub>抓取与物体交互</sub> | 254 | 654 | [Grasp Detection & Synthesis](papers/taxonomy/manipulation-imitation/grasping-object-interaction/grasp-detection-synthesis/README.md) — C 49 · A 66<br>[Grasp Stability & Force Control](papers/taxonomy/manipulation-imitation/grasping-object-interaction/grasp-stability-force-control/README.md) — C 6 · A 7<br>[Grippers, Suction & End-effectors](papers/taxonomy/manipulation-imitation/grasping-object-interaction/grippers-suction-end-effectors/README.md) — C 22 · A 118<br>[Pick-place & Object Rearrangement](papers/taxonomy/manipulation-imitation/grasping-object-interaction/pick-place-object-rearrangement/README.md) — C 36 · A 89<br>[General / Cross-cutting](papers/taxonomy/manipulation-imitation/grasping-object-interaction/general-cross-cutting/README.md) — C 141 · A 374 |
| Contact-rich & Deformable Manipulation<br><sub>接触丰富与可变形操作</sub> | 160 | 534 | [Insertion, Assembly & Precision Tasks](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/insertion-assembly-precision-tasks/README.md) — C 77 · A 229<br>[Pushing, Sliding & Non-prehensile Skills](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/pushing-sliding-non-prehensile-skills/README.md) — C 21 · A 50<br>[Tool Use & Articulated Objects](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/tool-use-articulated-objects/README.md) — C 5 · A 33<br>[Cloth, Rope & Soft Objects](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/cloth-rope-soft-objects/README.md) — C 23 · A 72<br>[General / Cross-cutting](papers/taxonomy/manipulation-imitation/contact-rich-deformable-manipulation/general-cross-cutting/README.md) — C 34 · A 150 |
| Imitation & Demonstration Learning<br><sub>模仿与示范学习</sub> | 96 | 482 | [Behavior Cloning & Sequence Modeling](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/behavior-cloning-sequence-modeling/README.md) — C 6 · A 36<br>[Learning from Demonstration](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/learning-from-demonstration/README.md) — C 2 · A 44<br>[One-shot, Few-shot & Skill Transfer](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/one-shot-few-shot-skill-transfer/README.md) — C 16 · A 44<br>[Skill Discovery & Demonstration Segmentation](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/skill-discovery-demonstration-segmentation/README.md) — C 2 · A 5<br>[General / Cross-cutting](papers/taxonomy/manipulation-imitation/imitation-demonstration-learning/general-cross-cutting/README.md) — C 70 · A 353 |
| Manipulation Policy Learning<br><sub>操作策略学习</sub> | 393 | 1,976 | [Reinforcement & Offline RL](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/reinforcement-offline-rl/README.md) — C 21 · A 145<br>[Visuomotor & Closed-loop Policies](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/visuomotor-closed-loop-policies/README.md) — C 19 · A 141<br>[Generative & Diffusion Policies](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/generative-diffusion-policies/README.md) — C 12 · A 171<br>[Model-based Control & Trajectory Optimization](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/model-based-control-trajectory-optimization/README.md) — C 8 · A 59<br>[General / Cross-cutting](papers/taxonomy/manipulation-imitation/manipulation-policy-learning/general-cross-cutting/README.md) — C 333 · A 1,460 |
| Long-horizon & Mobile Manipulation<br><sub>长时程与移动操作</sub> | 38 | 171 | [Long-horizon Task Execution](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/long-horizon-task-execution/README.md) — C 10 · A 56<br>[Mobile Manipulation](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/mobile-manipulation/README.md) — C 3 · A 33<br>[Task-and-motion Planning](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/task-and-motion-planning/README.md) — C 5 · A 8<br>[Household, Industrial & Open-world Tasks](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/household-industrial-open-world-tasks/README.md) — C 3 · A 15<br>[General / Cross-cutting](papers/taxonomy/manipulation-imitation/long-horizon-mobile-manipulation/general-cross-cutting/README.md) — C 17 · A 59 |

</details>

<details>
<summary><strong>03 · Dexterity & Teleoperation · 灵巧操作与遥操作</strong><br><sub>339 conference · 935 arXiv · 6 subfields · 30 leaf catalogs</sub></summary>

How do hands, tactile signals, and teleoperation interfaces support contact-rich control?

**Research pipeline:** Human / vision / touch → Retargeting or contact model → Hand-arm control → Task outcome

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Dexterity%20%26%20Teleoperation#research-workbench) · [Conference catalog](papers/tracks/dexterity-teleoperation.md) · [arXiv catalog](papers/arxiv/dexterity-teleoperation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Dexterous Hand Control<br><sub>灵巧手控制</sub> | 133 | 331 | [Multifinger Control & Coordination](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/multifinger-control-coordination/README.md) — C 14 · A 18<br>[Hand Design, Actuation & Morphology](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/hand-design-actuation-morphology/README.md) — C 5 · A 25<br>[Dexterous Grasping](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/dexterous-grasping/README.md) — C 7 · A 13<br>[Cross-hand Generalization](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/cross-hand-generalization/README.md) — C 0 · A 1<br>[General / Cross-cutting](papers/taxonomy/dexterity-teleoperation/dexterous-hand-control/general-cross-cutting/README.md) — C 107 · A 274 |
| In-hand Manipulation<br><sub>手内操作</sub> | 61 | 107 | [Object Reorientation & Rotation](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/object-reorientation-rotation/README.md) — C 3 · A 7<br>[Rolling, Sliding & Finger Gaiting](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/rolling-sliding-finger-gaiting/README.md) — C 1 · A 2<br>[Slip, Stability & Contact Maintenance](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/slip-stability-contact-maintenance/README.md) — C 1 · A 2<br>[In-hand Sensing & State Estimation](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/in-hand-sensing-state-estimation/README.md) — C 1 · A 1<br>[General / Cross-cutting](papers/taxonomy/dexterity-teleoperation/in-hand-manipulation/general-cross-cutting/README.md) — C 55 · A 95 |
| Bimanual Coordination<br><sub>双手协同</sub> | 45 | 90 | [Bimanual Manipulation](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/bimanual-manipulation/README.md) — C 16 · A 13<br>[Dual-arm Planning & Control](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/dual-arm-planning-control/README.md) — C 0 · A 0<br>[Handovers & Collaborative Tasks](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/handovers-collaborative-tasks/README.md) — C 6 · A 7<br>[Bimanual Assembly & Deformables](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/bimanual-assembly-deformables/README.md) — C 4 · A 2<br>[General / Cross-cutting](papers/taxonomy/dexterity-teleoperation/bimanual-coordination/general-cross-cutting/README.md) — C 19 · A 68 |
| Teleoperation & Shared Autonomy<br><sub>遥操作与共享自主</sub> | 66 | 209 | [VR, XR & Immersive Teleoperation](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/vr-xr-immersive-teleoperation/README.md) — C 7 · A 27<br>[Bilateral & Master-slave Control](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/bilateral-master-slave-control/README.md) — C 4 · A 10<br>[Shared Autonomy & Assistance](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/shared-autonomy-assistance/README.md) — C 8 · A 12<br>[Remote Presence, Delay & Communication](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/remote-presence-delay-communication/README.md) — C 1 · A 20<br>[General / Cross-cutting](papers/taxonomy/dexterity-teleoperation/teleoperation-shared-autonomy/general-cross-cutting/README.md) — C 46 · A 140 |
| Retargeting & Human Motion<br><sub>重定向与人体动作</sub> | 18 | 106 | [Hand-pose Retargeting](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/hand-pose-retargeting/README.md) — C 2 · A 4<br>[Whole-body & Motion Retargeting](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/whole-body-motion-retargeting/README.md) — C 3 · A 17<br>[Motion Capture & Wearable Input](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/motion-capture-wearable-input/README.md) — C 0 · A 3<br>[Cross-embodiment Demonstration Transfer](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/cross-embodiment-demonstration-transfer/README.md) — C 8 · A 68<br>[General / Cross-cutting](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/general-cross-cutting/README.md) — C 5 · A 14 |
| Tactile & Haptic Interfaces<br><sub>触觉与力觉接口</sub> | 16 | 92 | [Tactile Sensing & Representation](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/tactile-sensing-representation/README.md) — C 7 · A 38<br>[Haptic Feedback & Rendering](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/haptic-feedback-rendering/README.md) — C 4 · A 42<br>[Contact & Force Estimation](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/contact-force-estimation/README.md) — C 0 · A 1<br>[Wearable & Human Interfaces](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/wearable-human-interfaces/README.md) — C 2 · A 1<br>[General / Cross-cutting](papers/taxonomy/dexterity-teleoperation/tactile-haptic-interfaces/general-cross-cutting/README.md) — C 3 · A 10 |

</details>

<details>
<summary><strong>04 · Navigation & Embodied Agents · 导航与具身智能体</strong><br><sub>807 conference · 5,989 arXiv · 6 subfields · 30 leaf catalogs</sub></summary>

How do agents build spatial memory, plan, and act over long horizons in open environments?

**Research pipeline:** Egocentric sensing + goal → World state / memory → Planning → Navigation and interaction

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Navigation%20%26%20Embodied%20Agents#research-workbench) · [Conference catalog](papers/tracks/navigation-embodied-agents.md) · [arXiv catalog](papers/arxiv/navigation-embodied-agents/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Visual & Language Navigation<br><sub>视觉与语言导航</sub> | 18 | 166 | [Vision-language Navigation](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/vision-language-navigation/README.md) — C 4 · A 89<br>[Object-goal & Semantic Navigation](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/object-goal-semantic-navigation/README.md) — C 7 · A 46<br>[Image-goal, Point-goal & Retrieval Navigation](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/image-goal-point-goal-retrieval-navigation/README.md) — C 4 · A 18<br>[Embodied QA & Interactive Navigation](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/embodied-qa-interactive-navigation/README.md) — C 2 · A 13<br>[General / Cross-cutting](papers/taxonomy/navigation-embodied-agents/visual-language-navigation/general-cross-cutting/README.md) — C 1 · A 0 |
| Mapping & Localization<br><sub>建图与定位</sub> | 42 | 1,412 | [Visual, LiDAR & Multi-sensor SLAM](papers/taxonomy/navigation-embodied-agents/mapping-localization/visual-lidar-multi-sensor-slam/README.md) — C 3 · A 464<br>[Visual-inertial & LiDAR Odometry](papers/taxonomy/navigation-embodied-agents/mapping-localization/visual-inertial-lidar-odometry/README.md) — C 7 · A 153<br>[Place Recognition & Loop Closure](papers/taxonomy/navigation-embodied-agents/mapping-localization/place-recognition-loop-closure/README.md) — C 1 · A 142<br>[Semantic, Metric & Neural Maps](papers/taxonomy/navigation-embodied-agents/mapping-localization/semantic-metric-neural-maps/README.md) — C 8 · A 16<br>[General / Cross-cutting](papers/taxonomy/navigation-embodied-agents/mapping-localization/general-cross-cutting/README.md) — C 23 · A 637 |
| Motion & Path Planning<br><sub>运动与路径规划</sub> | 546 | 3,454 | [Global Search & Path Planning](papers/taxonomy/navigation-embodied-agents/motion-path-planning/global-search-path-planning/README.md) — C 81 · A 376<br>[Local Planning & Obstacle Avoidance](papers/taxonomy/navigation-embodied-agents/motion-path-planning/local-planning-obstacle-avoidance/README.md) — C 12 · A 101<br>[Trajectory Optimization & MPC](papers/taxonomy/navigation-embodied-agents/motion-path-planning/trajectory-optimization-mpc/README.md) — C 16 · A 168<br>[Sampling, Learning & Safety-aware Planning](papers/taxonomy/navigation-embodied-agents/motion-path-planning/sampling-learning-safety-aware-planning/README.md) — C 9 · A 103<br>[General / Cross-cutting](papers/taxonomy/navigation-embodied-agents/motion-path-planning/general-cross-cutting/README.md) — C 428 · A 2,706 |
| Exploration & Active Mapping<br><sub>探索与主动建图</sub> | 117 | 364 | [Frontier & Coverage Exploration](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/frontier-coverage-exploration/README.md) — C 3 · A 13<br>[Next-best-view & Information Gain](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/next-best-view-information-gain/README.md) — C 4 · A 14<br>[Active Mapping & Reconstruction](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/active-mapping-reconstruction/README.md) — C 0 · A 5<br>[Search, Inspection & Discovery](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/search-inspection-discovery/README.md) — C 2 · A 47<br>[General / Cross-cutting](papers/taxonomy/navigation-embodied-agents/exploration-active-mapping/general-cross-cutting/README.md) — C 108 · A 285 |
| Multi-agent & Social Navigation<br><sub>多智能体与社会导航</sub> | 68 | 314 | [Multi-robot Coordination](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/multi-robot-coordination/README.md) — C 54 · A 197<br>[Swarm Navigation & Formation](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/swarm-navigation-formation/README.md) — C 3 · A 38<br>[Social & Human-aware Navigation](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/social-human-aware-navigation/README.md) — C 8 · A 28<br>[Multi-agent Collision Avoidance](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/multi-agent-collision-avoidance/README.md) — C 0 · A 1<br>[General / Cross-cutting](papers/taxonomy/navigation-embodied-agents/multi-agent-social-navigation/general-cross-cutting/README.md) — C 3 · A 50 |
| Field, Aerial & Marine Robotics<br><sub>野外、空中与海洋机器人</sub> | 16 | 279 | [Aerial & UAV Navigation](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/aerial-uav-navigation/README.md) — C 0 · A 62<br>[Autonomous Driving & Ground Vehicles](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/autonomous-driving-ground-vehicles/README.md) — C 9 · A 109<br>[Marine & Underwater Autonomy](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/marine-underwater-autonomy/README.md) — C 2 · A 25<br>[Outdoor, Agricultural & Delivery Robots](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/outdoor-agricultural-delivery-robots/README.md) — C 4 · A 2<br>[General / Cross-cutting](papers/taxonomy/navigation-embodied-agents/field-aerial-marine-robotics/general-cross-cutting/README.md) — C 1 · A 81 |

</details>

<details>
<summary><strong>05 · Humanoids & Locomotion · 人形机器人与运动控制</strong><br><sub>670 conference · 2,317 arXiv · 6 subfields · 30 leaf catalogs</sub></summary>

How can whole-body policies achieve agile, stable, and transferable motion?

**Research pipeline:** Motion reference + command → Retargeting / reinforcement learning → Whole-body control → Sim-to-real deployment

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Humanoids%20%26%20Locomotion#research-workbench) · [Conference catalog](papers/tracks/humanoids-locomotion.md) · [arXiv catalog](papers/arxiv/humanoids-locomotion/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Humanoid Whole-body Control<br><sub>人形全身控制</sub> | 223 | 1,159 | [Whole-body Tracking & Control](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/whole-body-tracking-control/README.md) — C 15 · A 101<br>[Humanoid Loco-manipulation](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/humanoid-loco-manipulation/README.md) — C 22 · A 110<br>[Upper-body Skills & Coordination](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/upper-body-skills-coordination/README.md) — C 2 · A 8<br>[Humanoid Teleoperation & Interaction](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/humanoid-teleoperation-interaction/README.md) — C 3 · A 20<br>[General / Cross-cutting](papers/taxonomy/humanoids-locomotion/humanoid-whole-body-control/general-cross-cutting/README.md) — C 181 · A 920 |
| Bipedal & Humanoid Locomotion<br><sub>双足与人形运动</sub> | 130 | 364 | [Walking & Gait Control](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/walking-gait-control/README.md) — C 62 · A 167<br>[Running, Jumping & Agile Skills](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/running-jumping-agile-skills/README.md) — C 18 · A 108<br>[Stairs, Terrain & Rough-ground Traversal](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/stairs-terrain-rough-ground-traversal/README.md) — C 12 · A 37<br>[Footstep & Contact Planning](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/footstep-contact-planning/README.md) — C 6 · A 8<br>[General / Cross-cutting](papers/taxonomy/humanoids-locomotion/bipedal-humanoid-locomotion/general-cross-cutting/README.md) — C 32 · A 44 |
| Quadruped & Legged Locomotion<br><sub>四足与多足运动</sub> | 294 | 543 | [Quadruped Locomotion](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/quadruped-locomotion/README.md) — C 144 · A 301<br>[General Legged & Multi-legged Control](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/general-legged-multi-legged-control/README.md) — C 140 · A 230<br>[Terrain Adaptation & Traversal](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/terrain-adaptation-traversal/README.md) — C 2 · A 6<br>[Agility, Recovery & Dynamic Maneuvers](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/agility-recovery-dynamic-maneuvers/README.md) — C 8 · A 6<br>[General / Cross-cutting](papers/taxonomy/humanoids-locomotion/quadruped-legged-locomotion/general-cross-cutting/README.md) — C 0 · A 0 |
| Motion Imitation & Generation<br><sub>动作模仿与生成</sub> | 1 | 97 | [Reference-motion Imitation](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/reference-motion-imitation/README.md) — C 0 · A 8<br>[Language-conditioned Motion Generation](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/language-conditioned-motion-generation/README.md) — C 0 · A 51<br>[Style, Expressive & Human-like Motion](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/style-expressive-human-like-motion/README.md) — C 1 · A 9<br>[Motion Priors & Behavioral Models](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/motion-priors-behavioral-models/README.md) — C 0 · A 1<br>[General / Cross-cutting](papers/taxonomy/humanoids-locomotion/motion-imitation-generation/general-cross-cutting/README.md) — C 0 · A 28 |
| Balance, Dynamics & Recovery<br><sub>平衡、动力学与恢复</sub> | 15 | 85 | [Balance & Stability Control](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/balance-stability-control/README.md) — C 2 · A 10<br>[Dynamics, MPC & Whole-body Optimization](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/dynamics-mpc-whole-body-optimization/README.md) — C 5 · A 27<br>[Fall Prevention & Recovery](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/fall-prevention-recovery/README.md) — C 3 · A 10<br>[State, Contact & Force Estimation](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/state-contact-force-estimation/README.md) — C 1 · A 5<br>[General / Cross-cutting](papers/taxonomy/humanoids-locomotion/balance-dynamics-recovery/general-cross-cutting/README.md) — C 4 · A 33 |
| Hardware & Morphology<br><sub>硬件与机器人形态</sub> | 7 | 69 | [Actuators, Joints & Transmission](papers/taxonomy/humanoids-locomotion/hardware-morphology/actuators-joints-transmission/README.md) — C 0 · A 14<br>[Feet, Legs & Mechanical Design](papers/taxonomy/humanoids-locomotion/hardware-morphology/feet-legs-mechanical-design/README.md) — C 0 · A 6<br>[Musculoskeletal & Bio-inspired Robots](papers/taxonomy/humanoids-locomotion/hardware-morphology/musculoskeletal-bio-inspired-robots/README.md) — C 5 · A 33<br>[Morphology & Co-design](papers/taxonomy/humanoids-locomotion/hardware-morphology/morphology-co-design/README.md) — C 2 · A 11<br>[General / Cross-cutting](papers/taxonomy/humanoids-locomotion/hardware-morphology/general-cross-cutting/README.md) — C 0 · A 5 |

</details>

<details>
<summary><strong>06 · Perception & World Models · 感知与世界模型</strong><br><sub>317 conference · 2,154 arXiv · 6 subfields · 30 leaf catalogs</sub></summary>

How do robots estimate task-relevant state and predict the consequences of action?

**Research pipeline:** Vision + touch + proprioception → State representation → World prediction → Policy conditioning

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Perception%20%26%20World%20Models#research-workbench) · [Conference catalog](papers/tracks/perception-world-models.md) · [arXiv catalog](papers/arxiv/perception-world-models/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| 3D Scene Perception<br><sub>三维场景感知</sub> | 44 | 763 | [Point-cloud & LiDAR Perception](papers/taxonomy/perception-world-models/3d-scene-perception/point-cloud-lidar-perception/README.md) — C 1 · A 273<br>[Depth, Stereo & RGB-D](papers/taxonomy/perception-world-models/3d-scene-perception/depth-stereo-rgb-d/README.md) — C 1 · A 72<br>[3D Reconstruction, NeRF & Gaussian Splatting](papers/taxonomy/perception-world-models/3d-scene-perception/3d-reconstruction-nerf-gaussian-splatting/README.md) — C 2 · A 78<br>[Occupancy & Scene Representation](papers/taxonomy/perception-world-models/3d-scene-perception/occupancy-scene-representation/README.md) — C 1 · A 53<br>[General / Cross-cutting](papers/taxonomy/perception-world-models/3d-scene-perception/general-cross-cutting/README.md) — C 39 · A 287 |
| Object, Pose & Affordance Perception<br><sub>物体、姿态与可供性感知</sub> | 53 | 460 | [Object Detection & Segmentation](papers/taxonomy/perception-world-models/object-pose-affordance-perception/object-detection-segmentation/README.md) — C 0 · A 209<br>[6D Pose & Keypoint Estimation](papers/taxonomy/perception-world-models/object-pose-affordance-perception/6d-pose-keypoint-estimation/README.md) — C 21 · A 179<br>[Affordance & Interaction Prediction](papers/taxonomy/perception-world-models/object-pose-affordance-perception/affordance-interaction-prediction/README.md) — C 31 · A 64<br>[Articulated & Object-centric Perception](papers/taxonomy/perception-world-models/object-pose-affordance-perception/articulated-object-centric-perception/README.md) — C 1 · A 2<br>[General / Cross-cutting](papers/taxonomy/perception-world-models/object-pose-affordance-perception/general-cross-cutting/README.md) — C 0 · A 6 |
| State Estimation & Tracking<br><sub>状态估计与跟踪</sub> | 27 | 325 | [Object & Multi-target Tracking](papers/taxonomy/perception-world-models/state-estimation-tracking/object-multi-target-tracking/README.md) — C 1 · A 64<br>[Robot State & Visual Odometry](papers/taxonomy/perception-world-models/state-estimation-tracking/robot-state-visual-odometry/README.md) — C 6 · A 38<br>[Calibration & Sensor Fusion](papers/taxonomy/perception-world-models/state-estimation-tracking/calibration-sensor-fusion/README.md) — C 1 · A 61<br>[Scene Flow & Dynamic-state Estimation](papers/taxonomy/perception-world-models/state-estimation-tracking/scene-flow-dynamic-state-estimation/README.md) — C 1 · A 21<br>[General / Cross-cutting](papers/taxonomy/perception-world-models/state-estimation-tracking/general-cross-cutting/README.md) — C 18 · A 141 |
| Tactile & Multimodal Perception<br><sub>触觉与多模态感知</sub> | 148 | 239 | [Tactile Recognition & Representation](papers/taxonomy/perception-world-models/tactile-multimodal-perception/tactile-recognition-representation/README.md) — C 6 · A 9<br>[Force, Contact & Slip Perception](papers/taxonomy/perception-world-models/tactile-multimodal-perception/force-contact-slip-perception/README.md) — C 7 · A 5<br>[Visuotactile & Multisensory Fusion](papers/taxonomy/perception-world-models/tactile-multimodal-perception/visuotactile-multisensory-fusion/README.md) — C 9 · A 20<br>[Proprioception & Embodied Sensing](papers/taxonomy/perception-world-models/tactile-multimodal-perception/proprioception-embodied-sensing/README.md) — C 5 · A 2<br>[General / Cross-cutting](papers/taxonomy/perception-world-models/tactile-multimodal-perception/general-cross-cutting/README.md) — C 121 · A 203 |
| World & Dynamics Models<br><sub>世界与动力学模型</sub> | 32 | 330 | [Latent World Models](papers/taxonomy/perception-world-models/world-dynamics-models/latent-world-models/README.md) — C 25 · A 262<br>[Object-centric & Structured Dynamics](papers/taxonomy/perception-world-models/world-dynamics-models/object-centric-structured-dynamics/README.md) — C 1 · A 1<br>[Video & Future Prediction](papers/taxonomy/perception-world-models/world-dynamics-models/video-future-prediction/README.md) — C 1 · A 2<br>[Physics-informed & Neural Dynamics](papers/taxonomy/perception-world-models/world-dynamics-models/physics-informed-neural-dynamics/README.md) — C 5 · A 45<br>[General / Cross-cutting](papers/taxonomy/perception-world-models/world-dynamics-models/general-cross-cutting/README.md) — C 0 · A 20 |
| Active & Multiview Perception<br><sub>主动与多视角感知</sub> | 13 | 37 | [Next-best-view & View Planning](papers/taxonomy/perception-world-models/active-multiview-perception/next-best-view-view-planning/README.md) — C 0 · A 4<br>[Active Perception & Information Gathering](papers/taxonomy/perception-world-models/active-multiview-perception/active-perception-information-gathering/README.md) — C 7 · A 21<br>[Multiview Fusion & Consistency](papers/taxonomy/perception-world-models/active-multiview-perception/multiview-fusion-consistency/README.md) — C 1 · A 5<br>[Occlusion-aware & Interactive Perception](papers/taxonomy/perception-world-models/active-multiview-perception/occlusion-aware-interactive-perception/README.md) — C 5 · A 7<br>[General / Cross-cutting](papers/taxonomy/perception-world-models/active-multiview-perception/general-cross-cutting/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>07 · Simulation, Data & Evaluation · 仿真、数据与评测</strong><br><sub>332 conference · 2,923 arXiv · 6 subfields · 30 leaf catalogs</sub></summary>

How should embodied systems be trained, stress-tested, and compared reproducibly?

**Research pipeline:** Assets + task definitions → Simulation / data generation → Benchmark protocol → Metrics and error analysis

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Simulation%2C%20Data%20%26%20Evaluation#research-workbench) · [Conference catalog](papers/tracks/simulation-data-evaluation.md) · [arXiv catalog](papers/arxiv/simulation-data-evaluation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Simulation & Digital Twins<br><sub>仿真与数字孪生</sub> | 108 | 1,359 | [Physics Engines & Robot Simulators](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/physics-engines-robot-simulators/README.md) — C 7 · A 41<br>[Differentiable & Neural Simulation](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/differentiable-neural-simulation/README.md) — C 6 · A 26<br>[Digital Twins & Real-to-sim Reconstruction](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/digital-twins-real-to-sim-reconstruction/README.md) — C 11 · A 131<br>[Large-scale Parallel Simulation](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/large-scale-parallel-simulation/README.md) — C 3 · A 7<br>[General / Cross-cutting](papers/taxonomy/simulation-data-evaluation/simulation-digital-twins/general-cross-cutting/README.md) — C 81 · A 1,154 |
| Sim-to-real & Domain Adaptation<br><sub>仿真到现实与域适配</sub> | 62 | 217 | [Domain Randomization](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/domain-randomization/README.md) — C 8 · A 13<br>[System Identification & Calibration](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/system-identification-calibration/README.md) — C 0 · A 1<br>[Domain Adaptation & Transfer](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/domain-adaptation-transfer/README.md) — C 14 · A 66<br>[Reality-gap Evaluation](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/reality-gap-evaluation/README.md) — C 0 · A 4<br>[General / Cross-cutting](papers/taxonomy/simulation-data-evaluation/sim-to-real-domain-adaptation/general-cross-cutting/README.md) — C 40 · A 133 |
| Datasets & Data Engines<br><sub>数据集与数据引擎</sub> | 104 | 740 | [Robot Datasets & Corpora](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/robot-datasets-corpora/README.md) — C 90 · A 575<br>[Demonstration & Trajectory Data](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/demonstration-trajectory-data/README.md) — C 0 · A 1<br>[Synthetic Data Generation](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/synthetic-data-generation/README.md) — C 7 · A 102<br>[Data Curation, Annotation & Quality](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/data-curation-annotation-quality/README.md) — C 0 · A 2<br>[General / Cross-cutting](papers/taxonomy/simulation-data-evaluation/datasets-data-engines/general-cross-cutting/README.md) — C 7 · A 60 |
| Benchmarks & Evaluation<br><sub>基准与评测</sub> | 52 | 380 | [Task & Capability Benchmarks](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/task-capability-benchmarks/README.md) — C 23 · A 147<br>[Metrics & Evaluation Protocols](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/metrics-evaluation-protocols/README.md) — C 1 · A 21<br>[Robustness & Stress Testing](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/robustness-stress-testing/README.md) — C 0 · A 3<br>[Real-world & Cross-platform Evaluation](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/real-world-cross-platform-evaluation/README.md) — C 0 · A 1<br>[General / Cross-cutting](papers/taxonomy/simulation-data-evaluation/benchmarks-evaluation/general-cross-cutting/README.md) — C 28 · A 208 |
| Training Infrastructure & Tools<br><sub>训练基础设施与工具</sub> | 5 | 126 | [Training Frameworks & RL Environments](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/training-frameworks-rl-environments/README.md) — C 0 · A 13<br>[Distributed, GPU & Data Systems](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/distributed-gpu-data-systems/README.md) — C 2 · A 12<br>[Open-source Libraries & Toolkits](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/open-source-libraries-toolkits/README.md) — C 0 · A 21<br>[Deployment, Runtime & Middleware](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/deployment-runtime-middleware/README.md) — C 1 · A 17<br>[General / Cross-cutting](papers/taxonomy/simulation-data-evaluation/training-infrastructure-tools/general-cross-cutting/README.md) — C 2 · A 63 |
| Safety, Robustness & Reproducibility<br><sub>安全、稳健与可复现性</sub> | 1 | 101 | [Safety Constraints & Verification](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/safety-constraints-verification/README.md) — C 0 · A 11<br>[Uncertainty & Out-of-distribution Testing](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/uncertainty-out-of-distribution-testing/README.md) — C 0 · A 29<br>[Failure Analysis & Reliability](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/failure-analysis-reliability/README.md) — C 0 · A 4<br>[Reproducibility & Standardization](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/reproducibility-standardization/README.md) — C 0 · A 16<br>[General / Cross-cutting](papers/taxonomy/simulation-data-evaluation/safety-robustness-reproducibility/general-cross-cutting/README.md) — C 1 · A 41 |

</details>

## How each paper is positioned

For example, `AnyDexRT` is positioned at:

> Dexterity & Teleoperation → Retargeting & Human Motion → [Hand-pose Retargeting](papers/taxonomy/dexterity-teleoperation/retargeting-human-motion/hand-pose-retargeting/README.md)

| Field | Role |
|---|---|
| `track` | Level 1: one of the seven primary research directions |
| `subcategory` | Level 2: the research problem inside that direction |
| `specialty` | Level 3: the finest catalog where the paper is actually listed |
| `taxonomy_evidence` | Strongest matched location and phrase from title, topic, or abstract |
| `source_type` | Official, publisher, bibliographic, or arXiv provenance |

Every workbench paper row exposes a clickable taxonomy breadcrumb and a direct leaf-catalog link. Markdown and CSV exports retain the three-level path and classification evidence.

## Classification and completeness boundary

- The conference layer uses fixed venues, years, the `robot` query, deterministic admission terms, and explicit exclusions.
- The arXiv layer audits 27,597 `cs.RO` candidates: 21,411 enter the seven directions and 6,186 remain outside the declared boundary.
- When evidence is insufficient, a paper remains General / Cross-cutting instead of receiving false fine-grained precision.
- Every conference record and every arXiv record appears exactly once in the leaf-catalog tree.
- Completeness is relative to the published operational boundary, not an undefined universal ontology of Embodied AI.

## Research workbench capabilities

- Progressive navigation across 7 directions, 40 subfields, and 200 leaf catalogs;
- conference, arXiv, and combined-unique research layers;
- joint filtering by title, author, year, venue, direction, subfield, specialty, and provenance;
- shareable URLs, local reading lists, Markdown / CSV export, English / Chinese, and light / dark themes;
- online paper and source links for every record, without inventing missing author metadata.

## Repository structure

```text
├── index.html                         # bilingual interactive workbench
├── README.md / README.zh-CN.md         # detailed English / Chinese homepages
├── data/                               # machine-readable conference and arXiv layers
├── papers/taxonomy/                    # 200 leaf catalogs with complete paper lists
├── papers/tracks/                      # seven conference direction catalogs
├── papers/arxiv/                       # seven directions × yearly arXiv indexes
├── scripts/taxonomy.py                 # deterministic level-2/level-3 rules
├── scripts/render_catalog.py           # README and catalog generator
└── scripts/audit_catalog.py            # data, provenance, and attachment audit
```

## Rebuild and validate

```bash
python scripts/apply_taxonomy.py --check
python scripts/render_catalog.py
python scripts/audit_catalog.py
python scripts/render_catalog.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
```

## Contributing and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing data or taxonomy rules. Repository-authored content uses [CC BY-NC-SA 4.0](LICENSE); paper copyrights remain with their authors and publishers, and this project links to papers without redistributing PDFs.
