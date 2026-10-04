# Embodied AI Paper Analysis

**English · [简体中文](README.zh-CN.md)**

> An auditable research workbench for 4,365 five-year conference papers and 25,257 recent arXiv preprints, organized into 9 directions, 42 level-2 subfields, and 168 finest-grained paper catalogs.

[![Workbench](https://img.shields.io/badge/Research_workbench-open-2563eb?style=flat-square)](https://dld0621.github.io/Embodied-AI-Paper-Analysis/)
[![Conference](https://img.shields.io/badge/Conference-4%2C365-111827?style=flat-square)](data/papers.json)
[![arXiv](https://img.shields.io/badge/arXiv-25%2C257-b31b1b?style=flat-square)](data/arxiv_recent.json)
[![Taxonomy](https://img.shields.io/badge/Taxonomy-9%E2%86%9242%E2%86%92168-0891b2?style=flat-square)](papers/taxonomy/README.md)

## Start here

| Goal | Entry point |
|---|---|
| Search, filter, save, and export papers | [Interactive research workbench](https://dld0621.github.io/Embodied-AI-Paper-Analysis/#research-workbench) |
| Browse from nine directions to the finest specialty | [Three-level taxonomy](papers/taxonomy/README.md) |
| Browse the five-year conference layer | [Conference paper overview](papers/README.md) |
| Cross-topic retargeting, evidence and review | [Topic views](papers/topics/README.md) · [Classification guide](docs/taxonomy-guide.md) · [Review queue](papers/classification-review/README.md) |
| Use machine-readable data | [`papers.json`](data/papers.json) · [`arxiv_recent.json`](data/arxiv_recent.json) |

## What this project provides

This is not a flat list of paper links. It combines a systematic conference census with a reproducible literature-positioning system: every paper states its level-1 direction, level-2 subfield, level-3 specialty, and the title/abstract evidence supporting that assignment.

Conference records and arXiv preprints remain separate evidence layers. A duplicate title never implies conference acceptance; deduplication is used only for the combined reading view while both source records remain available.

## Two evidence layers

| Layer | Window | Records | Research meaning |
|---|---|---:|---|
| Conference census | 2022–2026 | 4,365 | RSS, CoRL, ICRA, IROS, ICLR, ICML, NeurIPS, CVPR, ICCV, and ECCV with explicit provenance tiers |
| arXiv preprints | 2023-10-03 to 2026-10-03 | 25,257 | Classified from the complete `cs.RO` candidate window; not evidence of conference acceptance |
| Combined unique view | Same windows | 27,637 | Normalized-title deduplication, preferring an available conference record for display |

## Nine-direction research map

Every paper receives one primary **direction → subfield → specialty** path. The ontology contains 126 named specialties plus one scoped Pending specialty review leaf for each of 42 subfields, producing 168 paper destinations. Expand any direction below to inspect every level-2 and level-3 category with live paper counts.

<details>
<summary><strong>01 · Policy Learning & Embodied Foundation Models · 策略学习与具身基础模型</strong><br><sub>268 conference · 3,903 arXiv · 5 subfields · 20 leaf catalogs</sub></summary>

What is the primary contribution to policy learning & embodied foundation models?

**Research pipeline:** Observations → Learning → Policy → Actions

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Policy%20Learning%20%26%20Embodied%20Foundation%20Models#research-workbench) · [Conference catalog](papers/tracks/policy-learning-embodied-foundation-models.md) · [arXiv catalog](papers/arxiv/policy-learning-embodied-foundation-models/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Imitation Learning<br><sub>模仿学习</sub> | 84 | 641 | [Behavior Cloning & Sequence Modeling](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/behavior-cloning-sequence-modeling/README.md) — C 14 · A 116<br>[Interactive Imitation & Correction](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/interactive-imitation-correction/README.md) — C 2 · A 19<br>[Demonstration Segmentation & Skill Discovery](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/demonstration-segmentation-skill-discovery/README.md) — C 0 · A 16<br>[Pending specialty review](papers/taxonomy/policy-learning-embodied-foundation-models/imitation-learning/pending-specialty-review/README.md) — C 68 · A 490 |
| Reinforcement Learning<br><sub>强化学习</sub> | 55 | 1,161 | [Online Reinforcement Learning](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/online-reinforcement-learning/README.md) — C 53 · A 1,134<br>[Offline Reinforcement Learning](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/offline-reinforcement-learning/README.md) — C 2 · A 12<br>[Combining Imitation & Reinforcement](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/combining-imitation-reinforcement/README.md) — C 0 · A 15<br>[Pending specialty review](papers/taxonomy/policy-learning-embodied-foundation-models/reinforcement-learning/pending-specialty-review/README.md) — C 0 · A 0 |
| Generative Action Policies<br><sub>生成式动作策略</sub> | 28 | 341 | [Diffusion Policies](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/diffusion-policies/README.md) — C 24 · A 221<br>[Flow-matching Policies](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/flow-matching-policies/README.md) — C 3 · A 110<br>[Autoregressive & Tokenized Actions](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/autoregressive-tokenized-actions/README.md) — C 1 · A 10<br>[Pending specialty review](papers/taxonomy/policy-learning-embodied-foundation-models/generative-action-policies/pending-specialty-review/README.md) — C 0 · A 0 |
| VLA & Generalist Robot Policies<br><sub>VLA 与通用机器人策略</sub> | 78 | 1,412 | [Vision-Language-Action Modeling](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/vision-language-action-modeling/README.md) — C 67 · A 1,335<br>[Multimodal Action Grounding](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/multimodal-action-grounding/README.md) — C 10 · A 39<br>[Hierarchical & Mixture Policies](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/hierarchical-mixture-policies/README.md) — C 0 · A 36<br>[Pending specialty review](papers/taxonomy/policy-learning-embodied-foundation-models/vla-generalist-robot-policies/pending-specialty-review/README.md) — C 1 · A 2 |
| Generalization & Adaptation<br><sub>泛化与适配</sub> | 23 | 348 | [Cross-robot Transfer](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/cross-robot-transfer/README.md) — C 1 · A 64<br>[Few-shot & Test-time Adaptation](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/few-shot-test-time-adaptation/README.md) — C 21 · A 266<br>[Pretraining & Scaling Laws](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/pretraining-scaling-laws/README.md) — C 1 · A 18<br>[Pending specialty review](papers/taxonomy/policy-learning-embodied-foundation-models/generalization-adaptation/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>02 · Arm & General Object Manipulation · 机械臂与通用物体操作</strong><br><sub>1,147 conference · 3,119 arXiv · 4 subfields · 16 leaf catalogs</sub></summary>

What is the primary contribution to arm & general object manipulation?

**Research pipeline:** Objects → Task constraints → Planning → Manipulation

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Arm%20%26%20General%20Object%20Manipulation#research-workbench) · [Conference catalog](papers/tracks/arm-general-object-manipulation.md) · [arXiv catalog](papers/arxiv/arm-general-object-manipulation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Grasping & Pick-place<br><sub>抓取与拾放</sub> | 727 | 1,772 | [Gripper & Suction Grasp Planning](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/gripper-suction-grasp-planning/README.md) — C 87 · A 149<br>[Grasp Stability](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/grasp-stability/README.md) — C 14 · A 43<br>[Pick-place & Rearrangement](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/pick-place-rearrangement/README.md) — C 91 · A 204<br>[Pending specialty review](papers/taxonomy/arm-general-object-manipulation/grasping-pick-place/pending-specialty-review/README.md) — C 535 · A 1,376 |
| Contact-rich Manipulation<br><sub>接触丰富操作</sub> | 228 | 664 | [Insertion & Assembly](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/insertion-assembly/README.md) — C 125 · A 348<br>[Pushing & Non-prehensile Manipulation](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/pushing-non-prehensile-manipulation/README.md) — C 48 · A 131<br>[Tools & Articulated Objects](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/tools-articulated-objects/README.md) — C 33 · A 117<br>[Pending specialty review](papers/taxonomy/arm-general-object-manipulation/contact-rich-manipulation/pending-specialty-review/README.md) — C 22 · A 68 |
| Deformable Object Manipulation<br><sub>可变形物体操作</sub> | 54 | 150 | [Cloth & Garments](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/cloth-garments/README.md) — C 22 · A 55<br>[Ropes & Cables](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/ropes-cables/README.md) — C 7 · A 12<br>[Flexible & Soft Objects](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/flexible-soft-objects/README.md) — C 15 · A 52<br>[Pending specialty review](papers/taxonomy/arm-general-object-manipulation/deformable-object-manipulation/pending-specialty-review/README.md) — C 10 · A 31 |
| Coordinated & Complex Manipulation<br><sub>协同与复杂操作</sub> | 138 | 533 | [Dual-arm Collaboration](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/dual-arm-collaboration/README.md) — C 46 · A 151<br>[Mobile Manipulation](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/mobile-manipulation/README.md) — C 50 · A 173<br>[Long-horizon & Task-motion Planning](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/long-horizon-task-motion-planning/README.md) — C 31 · A 196<br>[Pending specialty review](papers/taxonomy/arm-general-object-manipulation/coordinated-complex-manipulation/pending-specialty-review/README.md) — C 11 · A 13 |

</details>

<details>
<summary><strong>03 · Dexterous Hands, Retargeting & Teleoperation · 灵巧手、重定向与遥操作</strong><br><sub>269 conference · 1,012 arXiv · 5 subfields · 20 leaf catalogs</sub></summary>

What is the primary contribution to dexterous hands, retargeting & teleoperation?

**Research pipeline:** Human or robot observations → Interaction representation → Hand mapping and control → Dexterous execution

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Dexterous%20Hands%2C%20Retargeting%20%26%20Teleoperation#research-workbench) · [Conference catalog](papers/tracks/dexterous-hands-retargeting-teleoperation.md) · [arXiv catalog](papers/arxiv/dexterous-hands-retargeting-teleoperation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Dexterous Hand Retargeting<br><sub>灵巧手重定向</sub> | 3 | 22 | [Kinematic & Pose Retargeting](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/kinematic-pose-retargeting/README.md) — C 3 · A 7<br>[Contact & Functional Retargeting](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/contact-functional-retargeting/README.md) — C 0 · A 9<br>[Physics & Dynamics Retargeting](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/physics-dynamics-retargeting/README.md) — C 0 · A 5<br>[Pending specialty review](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/pending-specialty-review/README.md) — C 0 · A 1 |
| Multifinger Grasping & Control<br><sub>多指抓取与控制</sub> | 94 | 300 | [Multifinger Coordination & Grasp Generation](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/multifinger-coordination-grasp-generation/README.md) — C 29 · A 70<br>[Grasp Force & Impedance Control](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/grasp-force-impedance-control/README.md) — C 0 · A 6<br>[Cross-hand Generalization](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/cross-hand-generalization/README.md) — C 1 · A 3<br>[Pending specialty review](papers/taxonomy/dexterous-hands-retargeting-teleoperation/multifinger-grasping-control/pending-specialty-review/README.md) — C 64 · A 221 |
| In-hand Manipulation<br><sub>手内操作</sub> | 52 | 107 | [Object Rotation & Repositioning](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/object-rotation-repositioning/README.md) — C 36 · A 70<br>[Rolling, Sliding & Finger Gaiting](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/rolling-sliding-finger-gaiting/README.md) — C 2 · A 5<br>[Contact Stability & Slip Recovery](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/contact-stability-slip-recovery/README.md) — C 1 · A 15<br>[Pending specialty review](papers/taxonomy/dexterous-hands-retargeting-teleoperation/in-hand-manipulation/pending-specialty-review/README.md) — C 13 · A 17 |
| Teleoperation & Shared Control<br><sub>遥操作与共享控制</sub> | 94 | 421 | [Vision, Gloves & XR Input](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/vision-gloves-xr-input/README.md) — C 73 · A 308<br>[Shared Autonomy & Assistance](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/shared-autonomy-assistance/README.md) — C 7 · A 60<br>[Bilateral Feedback & Delay](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/bilateral-feedback-delay/README.md) — C 10 · A 47<br>[Pending specialty review](papers/taxonomy/dexterous-hands-retargeting-teleoperation/teleoperation-shared-control/pending-specialty-review/README.md) — C 4 · A 6 |
| Human Demonstrations to Dexterous Skills<br><sub>人类示教到灵巧技能</sub> | 26 | 162 | [Hand-object Reconstruction for Transfer](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/hand-object-reconstruction-for-transfer/README.md) — C 0 · A 1<br>[Video-to-robot Demonstrations](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/video-to-robot-demonstrations/README.md) — C 23 · A 138<br>[Demonstration Refinement & Skill Transfer](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/demonstration-refinement-skill-transfer/README.md) — C 1 · A 11<br>[Pending specialty review](papers/taxonomy/dexterous-hands-retargeting-teleoperation/human-demonstrations-to-dexterous-skills/pending-specialty-review/README.md) — C 2 · A 12 |

</details>

<details>
<summary><strong>04 · Navigation, Localization & Multi-robot Coordination · 导航、定位与多机器人协作</strong><br><sub>894 conference · 6,353 arXiv · 4 subfields · 16 leaf catalogs</sub></summary>

What is the primary contribution to navigation, localization & multi-robot coordination?

**Research pipeline:** Sensor data → Maps and goals → Planning → Navigation

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Navigation%2C%20Localization%20%26%20Multi-robot%20Coordination#research-workbench) · [Conference catalog](papers/tracks/navigation-localization-multi-robot-coordination.md) · [arXiv catalog](papers/arxiv/navigation-localization-multi-robot-coordination/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Localization & Mapping<br><sub>定位与建图</sub> | 312 | 2,872 | [Visual, LiDAR & Multisensor SLAM](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/visual-lidar-multisensor-slam/README.md) — C 14 · A 551<br>[Odometry & Relocalization](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/odometry-relocalization/README.md) — C 57 · A 1,042<br>[Semantic & Neural Maps](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/semantic-neural-maps/README.md) — C 46 · A 366<br>[Pending specialty review](papers/taxonomy/navigation-localization-multi-robot-coordination/localization-mapping/pending-specialty-review/README.md) — C 195 · A 913 |
| Goal & Language Navigation<br><sub>目标与语言导航</sub> | 83 | 462 | [Point-goal & Image-goal Navigation](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/point-goal-image-goal-navigation/README.md) — C 23 · A 106<br>[Object-goal & Semantic Navigation](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/object-goal-semantic-navigation/README.md) — C 27 · A 100<br>[Vision-Language Navigation](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/vision-language-navigation/README.md) — C 33 · A 256<br>[Pending specialty review](papers/taxonomy/navigation-localization-multi-robot-coordination/goal-language-navigation/pending-specialty-review/README.md) — C 0 · A 0 |
| Motion Planning & Exploration<br><sub>运动规划与探索</sub> | 365 | 2,344 | [Global Path Planning](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/global-path-planning/README.md) — C 178 · A 1,292<br>[Local Avoidance & Trajectory Optimization](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/local-avoidance-trajectory-optimization/README.md) — C 35 · A 481<br>[Active Exploration & Information Gain](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/active-exploration-information-gain/README.md) — C 152 · A 571<br>[Pending specialty review](papers/taxonomy/navigation-localization-multi-robot-coordination/motion-planning-exploration/pending-specialty-review/README.md) — C 0 · A 0 |
| Multi-robot & Social Navigation<br><sub>多机器人与社会导航</sub> | 134 | 675 | [Multi-robot Coordination](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/multi-robot-coordination/README.md) — C 67 · A 378<br>[Swarms & Formation](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/swarms-formation/README.md) — C 11 · A 117<br>[Human-aware & Social Navigation](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/human-aware-social-navigation/README.md) — C 56 · A 176<br>[Pending specialty review](papers/taxonomy/navigation-localization-multi-robot-coordination/multi-robot-social-navigation/pending-specialty-review/README.md) — C 0 · A 4 |

</details>

<details>
<summary><strong>05 · Legged Locomotion & Whole-body Control · 足式运动与全身控制</strong><br><sub>704 conference · 2,227 arXiv · 5 subfields · 20 leaf catalogs</sub></summary>

What is the primary contribution to legged locomotion & whole-body control?

**Research pipeline:** Motion references → Contact and terrain → Whole-body control → Locomotion

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Legged%20Locomotion%20%26%20Whole-body%20Control#research-workbench) · [Conference catalog](papers/tracks/legged-locomotion-whole-body-control.md) · [arXiv catalog](papers/arxiv/legged-locomotion-whole-body-control/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Bipedal & Humanoid Locomotion<br><sub>双足与人形运动</sub> | 367 | 987 | [Walking & Gaits](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/walking-gaits/README.md) — C 165 · A 347<br>[Running, Jumping & Agile Motion](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/running-jumping-agile-motion/README.md) — C 21 · A 103<br>[Terrain & Footstep Planning](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/terrain-footstep-planning/README.md) — C 12 · A 38<br>[Pending specialty review](papers/taxonomy/legged-locomotion-whole-body-control/bipedal-humanoid-locomotion/pending-specialty-review/README.md) — C 169 · A 499 |
| Quadruped & Multilegged Locomotion<br><sub>四足与多足运动</sub> | 241 | 515 | [Gaits & Locomotion Control](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/gaits-locomotion-control/README.md) — C 233 · A 476<br>[Terrain Adaptation](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/terrain-adaptation/README.md) — C 8 · A 35<br>[Dynamic Recovery & Agility](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/dynamic-recovery-agility/README.md) — C 0 · A 4<br>[Pending specialty review](papers/taxonomy/legged-locomotion-whole-body-control/quadruped-multilegged-locomotion/pending-specialty-review/README.md) — C 0 · A 0 |
| Whole-body Coordination & Balance<br><sub>全身协调与平衡</sub> | 56 | 284 | [Whole-body Optimization & Control](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/whole-body-optimization-control/README.md) — C 39 · A 184<br>[Balance & Contact Regulation](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/balance-contact-regulation/README.md) — C 10 · A 70<br>[Fall Prevention & Recovery](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/fall-prevention-recovery/README.md) — C 7 · A 30<br>[Pending specialty review](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-coordination-balance/pending-specialty-review/README.md) — C 0 · A 0 |
| Whole-body Motion Transfer<br><sub>全身动作迁移</sub> | 29 | 298 | [Human-to-robot Kinematic Retargeting](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/human-to-robot-kinematic-retargeting/README.md) — C 6 · A 32<br>[Contact & Dynamic Retargeting](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/contact-dynamic-retargeting/README.md) — C 0 · A 0<br>[Motion Imitation & Generation](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/motion-imitation-generation/README.md) — C 23 · A 266<br>[Pending specialty review](papers/taxonomy/legged-locomotion-whole-body-control/whole-body-motion-transfer/pending-specialty-review/README.md) — C 0 · A 0 |
| Locomotion-Manipulation Coordination<br><sub>移动与操作协同</sub> | 11 | 143 | [Humanoid Loco-manipulation](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/humanoid-loco-manipulation/README.md) — C 11 · A 135<br>[Multicontact Interaction](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/multicontact-interaction/README.md) — C 0 · A 4<br>[Leg-arm & Upper-body Coordination](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/leg-arm-upper-body-coordination/README.md) — C 0 · A 4<br>[Pending specialty review](papers/taxonomy/legged-locomotion-whole-body-control/locomotion-manipulation-coordination/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>06 · Perception, Representation & State Estimation · 感知、表征与状态估计</strong><br><sub>361 conference · 3,180 arXiv · 5 subfields · 20 leaf catalogs</sub></summary>

What is the primary contribution to perception, representation & state estimation?

**Research pipeline:** Sensor observations → Representations → State estimation → Task information

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Perception%2C%20Representation%20%26%20State%20Estimation#research-workbench) · [Conference catalog](papers/tracks/perception-representation-state-estimation.md) · [arXiv catalog](papers/arxiv/perception-representation-state-estimation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| 3D Environment Perception<br><sub>三维环境感知</sub> | 81 | 1,435 | [Depth & Point Clouds](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/depth-point-clouds/README.md) — C 15 · A 439<br>[3D Reconstruction](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/3d-reconstruction/README.md) — C 8 · A 232<br>[Occupancy & Scene Representation](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/occupancy-scene-representation/README.md) — C 31 · A 324<br>[Pending specialty review](papers/taxonomy/perception-representation-state-estimation/3d-environment-perception/pending-specialty-review/README.md) — C 27 · A 440 |
| Object & Interaction Perception<br><sub>物体与交互感知</sub> | 92 | 796 | [Detection & Segmentation](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/detection-segmentation/README.md) — C 23 · A 534<br>[6D Pose & Tracking](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/6d-pose-tracking/README.md) — C 38 · A 197<br>[Affordances & Interaction Relations](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/affordances-interaction-relations/README.md) — C 31 · A 65<br>[Pending specialty review](papers/taxonomy/perception-representation-state-estimation/object-interaction-perception/pending-specialty-review/README.md) — C 0 · A 0 |
| Human & Hand-object Perception<br><sub>人体与手—物感知</sub> | 12 | 88 | [Body & Hand Pose](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/body-hand-pose/README.md) — C 3 · A 47<br>[Hand-object Interaction Reconstruction](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/hand-object-interaction-reconstruction/README.md) — C 6 · A 12<br>[Contact & Motion Recovery](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/contact-motion-recovery/README.md) — C 3 · A 27<br>[Pending specialty review](papers/taxonomy/perception-representation-state-estimation/human-hand-object-perception/pending-specialty-review/README.md) — C 0 · A 2 |
| Tactile & Multimodal Perception<br><sub>触觉与多模态感知</sub> | 136 | 423 | [Tactile Representation](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/tactile-representation/README.md) — C 61 · A 127<br>[Force, Contact & Slip Estimation](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/force-contact-slip-estimation/README.md) — C 10 · A 39<br>[Visuotactile & Proprioceptive Fusion](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/visuotactile-proprioceptive-fusion/README.md) — C 21 · A 155<br>[Pending specialty review](papers/taxonomy/perception-representation-state-estimation/tactile-multimodal-perception/pending-specialty-review/README.md) — C 44 · A 102 |
| State Estimation & Active Perception<br><sub>状态估计与主动感知</sub> | 40 | 438 | [Multisensor State Estimation](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/multisensor-state-estimation/README.md) — C 26 · A 222<br>[Calibration & Time Alignment](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/calibration-time-alignment/README.md) — C 4 · A 156<br>[View Selection & Active Observation](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/view-selection-active-observation/README.md) — C 10 · A 60<br>[Pending specialty review](papers/taxonomy/perception-representation-state-estimation/state-estimation-active-perception/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>07 · World Models, Planning & Embodied Reasoning · 世界模型、规划与具身推理</strong><br><sub>144 conference · 1,635 arXiv · 4 subfields · 16 leaf catalogs</sub></summary>

What is the primary contribution to world models, planning & embodied reasoning?

**Research pipeline:** Experience → Predictive models and knowledge → Reasoning and planning → Closed-loop decisions

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=World%20Models%2C%20Planning%20%26%20Embodied%20Reasoning#research-workbench) · [Conference catalog](papers/tracks/world-models-planning-embodied-reasoning.md) · [arXiv catalog](papers/arxiv/world-models-planning-embodied-reasoning/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| World & Dynamics Modeling<br><sub>世界与动力学建模</sub> | 51 | 669 | [Latent Dynamics](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/latent-dynamics/README.md) — C 31 · A 489<br>[Object & Contact Dynamics](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/object-contact-dynamics/README.md) — C 3 · A 24<br>[Action-conditioned Video Prediction](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/action-conditioned-video-prediction/README.md) — C 3 · A 78<br>[Pending specialty review](papers/taxonomy/world-models-planning-embodied-reasoning/world-dynamics-modeling/pending-specialty-review/README.md) — C 14 · A 78 |
| Model-based Decision Making<br><sub>模型驱动决策</sub> | 16 | 357 | [Model Predictive Control](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/model-predictive-control/README.md) — C 11 · A 293<br>[Imagination & Model-based RL](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/imagination-model-based-rl/README.md) — C 4 · A 45<br>[World-model Planning](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/world-model-planning/README.md) — C 1 · A 19<br>[Pending specialty review](papers/taxonomy/world-models-planning-embodied-reasoning/model-based-decision-making/pending-specialty-review/README.md) — C 0 · A 0 |
| Task Reasoning & Planning<br><sub>任务推理与规划</sub> | 63 | 379 | [Task Decomposition & Symbolic Planning](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/task-decomposition-symbolic-planning/README.md) — C 47 · A 227<br>[Language-model Planning](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/language-model-planning/README.md) — C 4 · A 39<br>[Embodied QA & Spatial Reasoning](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/embodied-qa-spatial-reasoning/README.md) — C 12 · A 113<br>[Pending specialty review](papers/taxonomy/world-models-planning-embodied-reasoning/task-reasoning-planning/pending-specialty-review/README.md) — C 0 · A 0 |
| Memory & Autonomous Execution<br><sub>记忆与自主执行</sub> | 14 | 230 | [Episodic Memory & Retrieval](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/episodic-memory-retrieval/README.md) — C 3 · A 66<br>[Persistent Task Execution](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/persistent-task-execution/README.md) — C 1 · A 17<br>[Failure Detection & Replanning](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/failure-detection-replanning/README.md) — C 10 · A 147<br>[Pending specialty review](papers/taxonomy/world-models-planning-embodied-reasoning/memory-autonomous-execution/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>08 · Data, Simulation & Evaluation · 数据、仿真与评测</strong><br><sub>360 conference · 2,746 arXiv · 6 subfields · 24 leaf catalogs</sub></summary>

What is the primary contribution to data, simulation & evaluation?

**Research pipeline:** Data or environments → Generation and validation → Experiments → Evidence

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Data%2C%20Simulation%20%26%20Evaluation#research-workbench) · [Conference catalog](papers/tracks/data-simulation-evaluation.md) · [arXiv catalog](papers/arxiv/data-simulation-evaluation/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Datasets & Data Engineering<br><sub>数据集与数据工程</sub> | 148 | 810 | [Robot Demonstration Datasets](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/robot-demonstration-datasets/README.md) — C 14 · A 65<br>[Human Video & Motion Data](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/human-video-motion-data/README.md) — C 1 · A 33<br>[Data Curation & Quality](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/data-curation-quality/README.md) — C 11 · A 89<br>[Pending specialty review](papers/taxonomy/data-simulation-evaluation/datasets-data-engineering/pending-specialty-review/README.md) — C 122 · A 623 |
| Synthetic & Augmented Data<br><sub>合成与增强数据</sub> | 18 | 224 | [Simulated Trajectory Generation](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/simulated-trajectory-generation/README.md) — C 2 · A 63<br>[Generative Data Augmentation](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/generative-data-augmentation/README.md) — C 11 · A 110<br>[Cross-robot Data Conversion](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/cross-robot-data-conversion/README.md) — C 0 · A 14<br>[Pending specialty review](papers/taxonomy/data-simulation-evaluation/synthetic-augmented-data/pending-specialty-review/README.md) — C 5 · A 37 |
| Simulation & Digital Twins<br><sub>仿真与数字孪生</sub> | 53 | 405 | [Physics Engines & Parallel Simulation](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/physics-engines-parallel-simulation/README.md) — C 14 · A 116<br>[Differentiable Simulation](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/differentiable-simulation/README.md) — C 7 · A 35<br>[Real-to-sim & Digital Twins](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/real-to-sim-digital-twins/README.md) — C 6 · A 121<br>[Pending specialty review](papers/taxonomy/data-simulation-evaluation/simulation-digital-twins/pending-specialty-review/README.md) — C 26 · A 133 |
| Sim-to-real Transfer<br><sub>仿真到现实</sub> | 49 | 279 | [Domain Randomization](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/domain-randomization/README.md) — C 6 · A 11<br>[System Identification & Sim Calibration](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/system-identification-sim-calibration/README.md) — C 1 · A 17<br>[Domain Adaptation & Transfer](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/domain-adaptation-transfer/README.md) — C 42 · A 251<br>[Pending specialty review](papers/taxonomy/data-simulation-evaluation/sim-to-real-transfer/pending-specialty-review/README.md) — C 0 · A 0 |
| Benchmarks & Experimental Methods<br><sub>基准与实验方法</sub> | 79 | 714 | [Task & Capability Benchmarks](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/task-capability-benchmarks/README.md) — C 77 · A 644<br>[Generalization & Robustness Evaluation](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/generalization-robustness-evaluation/README.md) — C 0 · A 6<br>[Reproducibility & Statistical Comparison](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/reproducibility-statistical-comparison/README.md) — C 1 · A 58<br>[Pending specialty review](papers/taxonomy/data-simulation-evaluation/benchmarks-experimental-methods/pending-specialty-review/README.md) — C 1 · A 6 |
| Safety & Reliability Evaluation<br><sub>安全与可靠性评估</sub> | 13 | 314 | [Safety Tests & Constraint Verification](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/safety-tests-constraint-verification/README.md) — C 2 · A 75<br>[OOD & Uncertainty Evaluation](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/ood-uncertainty-evaluation/README.md) — C 8 · A 135<br>[Fault & Failure Analysis](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/fault-failure-analysis/README.md) — C 3 · A 104<br>[Pending specialty review](papers/taxonomy/data-simulation-evaluation/safety-reliability-evaluation/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

<details>
<summary><strong>09 · Robot Hardware & Systems · 机器人硬件与系统</strong><br><sub>218 conference · 1,082 arXiv · 4 subfields · 16 leaf catalogs</sub></summary>

What is the primary contribution to robot hardware & systems?

**Research pipeline:** Hardware and software requirements → Design → Integration → Deployment

[Open combined paper view](https://dld0621.github.io/Embodied-AI-Paper-Analysis/?track=Robot%20Hardware%20%26%20Systems#research-workbench) · [Conference catalog](papers/tracks/robot-hardware-systems.md) · [arXiv catalog](papers/arxiv/robot-hardware-systems/README.md)

| Level-2 subfield | Conference | arXiv | Level-3 specialty paper catalogs |
|---|---:|---:|---|
| Mechanisms & Actuation<br><sub>机器人机构与驱动</sub> | 136 | 588 | [Hands, Grippers & Arms](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/hands-grippers-arms/README.md) — C 2 · A 17<br>[Legged & Whole-body Mechanisms](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/legged-whole-body-mechanisms/README.md) — C 6 · A 38<br>[Actuators & Transmission](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/actuators-transmission/README.md) — C 47 · A 315<br>[Pending specialty review](papers/taxonomy/robot-hardware-systems/mechanisms-actuation/pending-specialty-review/README.md) — C 81 · A 218 |
| Sensors & Human Interfaces<br><sub>传感器与人机接口</sub> | 57 | 158 | [Tactile & Force Sensors](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/tactile-force-sensors/README.md) — C 46 · A 61<br>[Motion Capture & Wearables](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/motion-capture-wearables/README.md) — C 2 · A 46<br>[Haptic Feedback Devices](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/haptic-feedback-devices/README.md) — C 1 · A 7<br>[Pending specialty review](papers/taxonomy/robot-hardware-systems/sensors-human-interfaces/pending-specialty-review/README.md) — C 8 · A 44 |
| Soft & Specialized Robots<br><sub>软体与特殊机器人</sub> | 16 | 168 | [Soft Mechanisms & Actuation](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/soft-mechanisms-actuation/README.md) — C 4 · A 68<br>[Bio-inspired Robots](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/bio-inspired-robots/README.md) — C 9 · A 76<br>[Special-environment Robots](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/special-environment-robots/README.md) — C 3 · A 24<br>[Pending specialty review](papers/taxonomy/robot-hardware-systems/soft-specialized-robots/pending-specialty-review/README.md) — C 0 · A 0 |
| Computing & Deployment Systems<br><sub>计算与部署系统</sub> | 9 | 168 | [Real-time & On-device Inference](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/real-time-on-device-inference/README.md) — C 3 · A 55<br>[Control & Communication Architecture](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/control-communication-architecture/README.md) — C 2 · A 69<br>[Software Frameworks & Integration](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/software-frameworks-integration/README.md) — C 4 · A 44<br>[Pending specialty review](papers/taxonomy/robot-hardware-systems/computing-deployment-systems/pending-specialty-review/README.md) — C 0 · A 0 |

</details>

## How each paper is positioned

For example, `AnyDexRT` is positioned at:

> Dexterous Hands, Retargeting & Teleoperation → Dexterous Hand Retargeting → [Kinematic & Pose Retargeting](papers/taxonomy/dexterous-hands-retargeting-teleoperation/dexterous-hand-retargeting/kinematic-pose-retargeting/README.md)

| Field | Role |
|---|---|
| `track` | Level 1: one of the nine primary research directions |
| `subcategory` | Level 2: the research problem inside that direction |
| `specialty` | Level 3: the finest catalog where the paper is actually listed |
| `taxonomy_evidence` | Strongest matched location and phrase from title or abstract |
| `classification_status` | Reviewed title/abstract exception, rule assignment or needs-review; not full-paper certification |
| `method_tags / embodiment_tags / data_tags / related_topics` | Cross-category facets, not additional primary attachments |
| `source_type` | Official, publisher, bibliographic, or arXiv provenance |

Every workbench paper row exposes a clickable taxonomy breadcrumb and a direct leaf-catalog link. Markdown and CSV exports retain the three-level path and classification evidence.

## Classification and completeness boundary

- The conference layer uses fixed venues, years, the `robot` query, deterministic admission terms, and explicit exclusions.
- The arXiv layer audits 32,552 `cs.RO` candidates: 25,257 enter the nine directions and 7,295 remain outside the declared boundary.
- When evidence is insufficient, a paper remains Pending specialty review instead of receiving false fine-grained precision.
- Every conference record and every arXiv record appears exactly once in the leaf-catalog tree.
- Completeness is relative to the published operational boundary, not an undefined universal ontology of Embodied AI.

## Research workbench capabilities

- Progressive navigation across 9 directions, 42 subfields, and 168 leaf catalogs;
- conference, arXiv, and combined-unique research layers;
- joint filtering by title, author, year, venue, direction, subfield, specialty, and provenance;
- shareable URLs, local reading lists, Markdown / CSV export, English / Chinese, and light / dark themes;
- online paper and source links for every record, without inventing missing author metadata.

## Repository structure

```text
├── index.html                         # bilingual interactive workbench
├── README.md / README.zh-CN.md         # detailed English / Chinese homepages
├── data/                               # machine-readable conference and arXiv layers
├── papers/taxonomy/                    # 168 leaf catalogs with complete paper lists
├── papers/tracks/                      # nine conference direction catalogs
├── papers/arxiv/                       # nine directions × yearly arXiv indexes
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
