# 顶会与 arXiv 来源刷新记录 · 2026-11-16

基准提交：`6be80486d4736c2cc354d85ff9ced926ba5d5906`。本次分别刷新顶会索引与 arXiv 两个来源层，不通过改日期制造更新或完整性证明。

| 指标 | 刷新前 | 刷新后 |
|---|---:|---:|
| arXiv 快照 | 2026-11-13 | 2026-11-16 |
| 原始提交日期窗口（含首尾） | 2023-11-13 至 2026-11-13 | 2023-11-16 至 2026-11-16 |
| 顶会索引快照（非论文发表日期） | 2026-11-13 | 2026-11-16 |
| 顶会来源记录 | 4,535 | 4,535 |
| 实际候选 | 34545 | 34518 |
| API 声明候选 | 34545 | 34518 |
| 规则纳入 | 27027 | 27016 |
| 未满足纳入规则 | 7518 | 7502 |
| 与顶会标题重合的预印本记录 | 2015 | 2009 |
| 与顶会重合的唯一标题 | 2014 | 2008 |
| arXiv 内部标准化标题重复 | 8 | 8 |
| 合并标题去重阅读记录 | 29540 | 29535 |
| 最新已纳入原始发表日期 | 2026-11-12 | 2026-11-13 |

## 实际变化与数量核对

- API 数量校验：刷新后实际 34,518 条，与 API 声明 34,518 条一致。
- 新增 32 条，移出 43 条；其中滚动窗口移出 43 条，仍在新窗口但本次未出现 0 条。
- 新增收录中，0 条原始发表于旧快照之后；32 条原始发表于旧快照截止日或更早。新增收录不等于全部是本周新发表。
- 保留 26,984 条；完整记录字段发生变化的保留记录 12 条。数量变化不是新增数量，元数据变化也不等于新论文。
- 顶会来源快照由 2026-11-13 更新为 2026-11-16；记录由 4,535 变为 4,535，新增 0、移出 0，保留记录元数据变化 13 条。
- 窗口内未收录中，0 条已核对为来源元数据修订后不再满足现有纳入规则；0 条原因待核实。窗口移出不表示撤稿，规则排除也不证明论文无关。

## arXiv 新增与移出明细

新增使用刷新后当前三级分类；移出展示基准中最后已观察分类，不冒充本次重新核实。

### 新增（32 条）

| arXiv ID | 论文 | 原始发表日期 | 一级 → 二级 → 三级 | 分类状态 | 变化原因 |
|---|---|---|---|---|---|
| 2611.17394 | [Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training](https://arxiv.org/abs/2611.17394) | 2026-11-12 | Data, Simulation & Evaluation → Synthetic & Augmented Data → Simulated Trajectory Generation | reviewed | 本次新增纳入 |
| 2611.17442 | [Racing the Clock: Teaching VLNs Budget-Conditioned Object Search](https://arxiv.org/abs/2611.17442) | 2026-11-12 | Navigation, Localization & Multi-robot Coordination → Goal & Language Navigation → Vision-Language Navigation | rule-assigned | 本次新增纳入 |
| 2611.17529 | [Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum](https://arxiv.org/abs/2611.17529) | 2026-11-12 | World Models, Planning & Embodied Reasoning → Model-based Decision Making → World-model Planning | reviewed | 本次新增纳入 |
| 2611.17549 | [Talk to Act: A Synthetic Multi-Turn Dialogue Benchmark for Human Intent Extraction and Action Planning in Robotics](https://arxiv.org/abs/2611.17549) | 2026-11-12 | Data, Simulation & Evaluation → Benchmarks & Experimental Methods → Task & Capability Benchmarks | rule-assigned | 本次新增纳入 |
| 2611.17566 | [Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety](https://arxiv.org/abs/2611.17566) | 2026-11-12 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Local Avoidance & Trajectory Optimization | rule-assigned | 本次新增纳入 |
| 2611.17598 | [X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot](https://arxiv.org/abs/2611.17598) | 2026-11-12 | Legged Locomotion & Whole-body Control → Bipedal & Humanoid Locomotion → Walking & Gaits | rule-assigned | 本次新增纳入 |
| 2611.17619 | [TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real](https://arxiv.org/abs/2611.17619) | 2026-11-13 | Data, Simulation & Evaluation → Synthetic & Augmented Data → Simulated Trajectory Generation | reviewed | 本次新增纳入 |
| 2611.17631 | [On the Utility of Pre-Trained Visual Representations for Policy Learning of Contact-Rich Insertion Tasks](https://arxiv.org/abs/2611.17631) | 2026-11-13 | Data, Simulation & Evaluation → Benchmarks & Experimental Methods → Generalization & Robustness Evaluation | reviewed | 本次新增纳入 |
| 2611.17638 | [AI-guided robotic in situ fabrication of curvature- and tissue-adaptive wireless bioelectronics](https://arxiv.org/abs/2611.17638) | 2026-11-13 | Data, Simulation & Evaluation → Synthetic & Augmented Data → Simulated Trajectory Generation | rule-assigned | 本次新增纳入 |
| 2611.17658 | [Imitation Policies Learn a Proprioceptive Anchor: A Predictive Law for Perception Noise and Its Closed Loop Cost](https://arxiv.org/abs/2611.17658) | 2026-11-13 | Perception, Representation & State Estimation → 3D Environment Perception → Pending specialty review | needs-review | 本次新增纳入 |
| 2611.17660 | [EViDS: An Environment--Vehicle Dynamics Integrated Simulation Platform for Intelligent Chassis Development](https://arxiv.org/abs/2611.17660) | 2026-11-13 | Data, Simulation & Evaluation → Simulation & Digital Twins → Physics Engines & Parallel Simulation | rule-assigned | 本次新增纳入 |
| 2611.17720 | [Ego2Flow: Benchmarking the Traffic-System Impact of Autonomous Driving on Maps Distilled from Real-World Roads](https://arxiv.org/abs/2611.17720) | 2026-11-13 | Data, Simulation & Evaluation → Benchmarks & Experimental Methods → Task & Capability Benchmarks | rule-assigned | 本次新增纳入 |
| 2611.17730 | [ERA: Error-Resistant Autonomous Object Navigation with Predicted Depth](https://arxiv.org/abs/2611.17730) | 2026-11-13 | Navigation, Localization & Multi-robot Coordination → Goal & Language Navigation → Object-goal & Semantic Navigation | rule-assigned | 本次新增纳入 |
| 2611.17751 | [When Does Cross-View Consistency Matter in Multi-View Appearance Augmentation? A Controlled Study for Visuomotor Policies](https://arxiv.org/abs/2611.17751) | 2026-11-13 | Policy Learning & Embodied Foundation Models → Generative Action Policies → Diffusion Policies | rule-assigned | 本次新增纳入 |
| 2611.17775 | [Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models](https://arxiv.org/abs/2611.17775) | 2026-11-13 | Data, Simulation & Evaluation → Benchmarks & Experimental Methods → Reproducibility & Statistical Comparison | reviewed | 本次新增纳入 |
| 2611.17859 | [Per-Agent-Safe Navigation of Globally Driven Robot Collectives via Affine Field Design](https://arxiv.org/abs/2611.17859) | 2026-11-13 | Robot Hardware & Systems → Mechanisms & Actuation → Actuators & Transmission | rule-assigned | 本次新增纳入 |
| 2611.18003 | [Reusing Locomotion Training Recipes Across Humanoids via Body-Aligned Virtual Joints](https://arxiv.org/abs/2611.18003) | 2026-11-13 | Legged Locomotion & Whole-body Control → Bipedal & Humanoid Locomotion → Pending specialty review | needs-review | 本次新增纳入 |
| 2611.18026 | [A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space](https://arxiv.org/abs/2611.18026) | 2026-11-13 | Policy Learning & Embodied Foundation Models → Generalization & Adaptation → Few-shot & Test-time Adaptation | rule-assigned | 本次新增纳入 |
| 2611.18110 | [PoliMop: Policy-in-the-Loop Motion Planning in 3D Spaces for Mobile Robots](https://arxiv.org/abs/2611.18110) | 2026-11-13 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 本次新增纳入 |
| 2611.18123 | [Evaluating Language Models as Spatial Priors for Object-Goal Navigation](https://arxiv.org/abs/2611.18123) | 2026-11-13 | Navigation, Localization & Multi-robot Coordination → Goal & Language Navigation → Point-goal & Image-goal Navigation | rule-assigned | 本次新增纳入 |
| 2611.18176 | [ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents](https://arxiv.org/abs/2611.18176) | 2026-11-13 | Policy Learning & Embodied Foundation Models → VLA & Generalist Robot Policies → Hierarchical & Mixture Policies | reviewed | 本次新增纳入 |
| 2611.18298 | [Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation](https://arxiv.org/abs/2611.18298) | 2026-11-13 | World Models, Planning & Embodied Reasoning → Model-based Decision Making → Model Predictive Control | reviewed | 本次新增纳入 |
| 2611.18305 | [PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion](https://arxiv.org/abs/2611.18305) | 2026-11-13 | Legged Locomotion & Whole-body Control → Quadruped & Multilegged Locomotion → Gaits & Locomotion Control | rule-assigned | 本次新增纳入 |
| 2611.18359 | [Envisioning Agentic Robotics: A New Era of Robotic Systems](https://arxiv.org/abs/2611.18359) | 2026-11-13 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Active Exploration & Information Gain | rule-assigned | 本次新增纳入 |
| 2611.18365 | [Heavy Metal Acrobatics: Learning Dynamic Control for Skid-Steer Loaders](https://arxiv.org/abs/2611.18365) | 2026-11-13 | Data, Simulation & Evaluation → Sim-to-real Transfer → Domain Adaptation & Transfer | rule-assigned | 本次新增纳入 |
| 2611.18372 | [Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment](https://arxiv.org/abs/2611.18372) | 2026-11-13 | Policy Learning & Embodied Foundation Models → VLA & Generalist Robot Policies → Vision-Language-Action Modeling | reviewed | 本次新增纳入 |
| 2611.18484 | [From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration](https://arxiv.org/abs/2611.18484) | 2026-11-13 | Data, Simulation & Evaluation → Datasets & Data Engineering → Pending specialty review | needs-review | 本次新增纳入 |
| 2611.18491 | [When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners](https://arxiv.org/abs/2611.18491) | 2026-11-13 | Arm & General Object Manipulation → Grasping & Pick-place → Pending specialty review | needs-review | 本次新增纳入 |
| 2611.18496 | [Toward Resilient Self-Driving Laboratories through Telerobotic Interventions](https://arxiv.org/abs/2611.18496) | 2026-11-13 | Dexterous Hands, Retargeting & Teleoperation → Teleoperation & Shared Control → Shared Autonomy & Assistance | rule-assigned | 本次新增纳入 |
| 2611.18501 | [In Situ Monitoring and Predictive Modeling of Harmful Algal Blooms with Autonomous Surface Vehicles](https://arxiv.org/abs/2611.18501) | 2026-11-13 | Perception, Representation & State Estimation → 3D Environment Perception → Pending specialty review | needs-review | 本次新增纳入 |
| 2611.18546 | [Modeling the Frictional Contact of Continuum Robots with Environments through Linear Complementarity Problem](https://arxiv.org/abs/2611.18546) | 2026-11-13 | World Models, Planning & Embodied Reasoning → World & Dynamics Modeling → Object & Contact Dynamics | reviewed | 本次新增纳入 |
| 2611.18562 | [Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562) | 2026-11-13 | Policy Learning & Embodied Foundation Models → Reinforcement Learning → Online Reinforcement Learning | reviewed | 本次新增纳入 |

### 移出（43 条）

| arXiv ID | 论文 | 原始发表日期 | 一级 → 二级 → 三级 | 分类状态 | 变化原因 |
|---|---|---|---|---|---|
| 2311.07082 | [A Survey on Passing-through Control of Multi-Robot Systems in Cluttered Environments](https://arxiv.org/abs/2311.07082) | 2023-11-13 | Navigation, Localization & Multi-robot Coordination → Multi-robot & Social Navigation → Multi-robot Coordination | rule-assigned | 滚动窗口外 |
| 2311.07100 | [Collaborative Planning for Catching and Transporting Objects in Unstructured Environments](https://arxiv.org/abs/2311.07100) | 2023-11-13 | Navigation, Localization & Multi-robot Coordination → Multi-robot & Social Navigation → Multi-robot Coordination | rule-assigned | 滚动窗口外 |
| 2311.07105 | [Collaborative Goal Tracking of Multiple Mobile Robots Based on Geometric Graph Neural Network](https://arxiv.org/abs/2311.07105) | 2023-11-13 | Perception, Representation & State Estimation → 3D Environment Perception → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.07132 | [Understanding Path Planning Explanations](https://arxiv.org/abs/2311.07132) | 2023-11-13 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.07150 | [Interaction is all You Need? A Study of Robots Ability to Understand and Execute](https://arxiv.org/abs/2311.07150) | 2023-11-13 | Data, Simulation & Evaluation → Benchmarks & Experimental Methods → Task & Capability Benchmarks | rule-assigned | 滚动窗口外 |
| 2311.07226 | [Large Language Models for Robotics: A Survey](https://arxiv.org/abs/2311.07226) | 2023-11-13 | Policy Learning & Embodied Foundation Models → Imitation Learning → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.07239 | [RESenv: A Realistic Earthquake Simulation Environment based on Unreal Engine](https://arxiv.org/abs/2311.07239) | 2023-11-13 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.07245 | [Towards Transferring Tactile-based Continuous Force Control Policies from Simulation to Robot](https://arxiv.org/abs/2311.07245) | 2023-11-13 | Perception, Representation & State Estimation → Tactile & Multimodal Perception → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.07257 | [Bio-Inspired Grasping Controller for Sensorized 2-DoF Grippers](https://arxiv.org/abs/2311.07257) | 2023-11-13 | Arm & General Object Manipulation → Grasping & Pick-place → Gripper & Suction Grasp Planning | rule-assigned | 滚动窗口外 |
| 2311.07260 | [TIAGo RL: Simulated Reinforcement Learning Environments with Tactile Data for Mobile Robots](https://arxiv.org/abs/2311.07260) | 2023-11-13 | Perception, Representation & State Estimation → Tactile & Multimodal Perception → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.07268 | [ViKi-HyCo: A Hybrid-Control approach for complex car-like maneuvers](https://arxiv.org/abs/2311.07268) | 2023-11-13 | Perception, Representation & State Estimation → Object & Interaction Perception → 6D Pose & Tracking | rule-assigned | 滚动窗口外 |
| 2311.07291 | [LiLO: Lightweight and low-bias LiDAR Odometry method based on spherical range image filtering](https://arxiv.org/abs/2311.07291) | 2023-11-13 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |
| 2311.07301 | [Geo-Localization Based on Dynamically Weighted Factor-Graph](https://arxiv.org/abs/2311.07301) | 2023-11-13 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |
| 2311.07377 | [Testing learning-enabled cyber-physical systems with Large-Language Models: A Formal Approach](https://arxiv.org/abs/2311.07377) | 2023-11-13 | World Models, Planning & Embodied Reasoning → Memory & Autonomous Execution → Failure Detection & Replanning | rule-assigned | 滚动窗口外 |
| 2311.07395 | [Predicting Continuous Locomotion Modes via Multidimensional Feature Learning from sEMG](https://arxiv.org/abs/2311.07395) | 2023-11-13 | Legged Locomotion & Whole-body Control → Bipedal & Humanoid Locomotion → Walking & Gaits | rule-assigned | 滚动窗口外 |
| 2311.07479 | [Towards Robotic Tree Manipulation: Leveraging Graph Representations](https://arxiv.org/abs/2311.07479) | 2023-11-13 | Arm & General Object Manipulation → Grasping & Pick-place → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.07499 | [Bridging the Sim-to-Real Gap with Dynamic Compliance Tuning for Industrial Insertion](https://arxiv.org/abs/2311.07499) | 2023-11-13 | Arm & General Object Manipulation → Contact-rich Manipulation → Insertion & Assembly | rule-assigned | 滚动窗口外 |
| 2311.07558 | [Data-Efficient Task Generalization via Probabilistic Model-based Meta Reinforcement Learning](https://arxiv.org/abs/2311.07558) | 2023-11-13 | Policy Learning & Embodied Foundation Models → Reinforcement Learning → Online Reinforcement Learning | rule-assigned | 滚动窗口外 |
| 2311.07913 | [Roadside LiDAR Assisted Cooperative Localization for Connected Autonomous Vehicles](https://arxiv.org/abs/2311.07913) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |
| 2311.07992 | [Probable Object Location (POLo) Score Estimation for Efficient Object Goal Navigation](https://arxiv.org/abs/2311.07992) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Goal & Language Navigation → Point-goal & Image-goal Navigation | rule-assigned | 滚动窗口外 |
| 2311.08013 | [CP-SLAM: Collaborative Neural Point-based SLAM System](https://arxiv.org/abs/2311.08013) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Visual, LiDAR & Multisensor SLAM | rule-assigned | 滚动窗口外 |
| 2311.08100 | [PPAD: Iterative Interactions of Prediction and Planning for End-to-end Autonomous Driving](https://arxiv.org/abs/2311.08100) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.08206 | [Human-Centric Autonomous Systems With LLMs for User Command Reasoning](https://arxiv.org/abs/2311.08206) | 2023-11-14 | Policy Learning & Embodied Foundation Models → Generalization & Adaptation → Few-shot & Test-time Adaptation | rule-assigned | 滚动窗口外 |
| 2311.08244 | [Language and Sketching: An LLM-driven Interactive Multimodal Multitask Robot Navigation Framework](https://arxiv.org/abs/2311.08244) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.08333 | [Calibration of an Elastic Humanoid Upper Body and Efficient Compensation for Motion Planning](https://arxiv.org/abs/2311.08333) | 2023-11-14 | Legged Locomotion & Whole-body Control → Bipedal & Humanoid Locomotion → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.08338 | [Self-Contained Calibration of an Elastic Humanoid Upper Body Using Only a Head-Mounted RGB Camera](https://arxiv.org/abs/2311.08338) | 2023-11-14 | Legged Locomotion & Whole-body Control → Bipedal & Humanoid Locomotion → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.08345 | [Speeding Up Optimization-based Motion Planning through Deep Learning](https://arxiv.org/abs/2311.08345) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.08354 | [Hierarchical Experience-informed Navigation for Multi-modal Quadrupedal Rebar Grid Traversal](https://arxiv.org/abs/2311.08354) | 2023-11-14 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.08608 | [Multi-Radar Inertial Odometry for 3D State Estimation using mmWave Imaging Radar](https://arxiv.org/abs/2311.08608) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |
| 2311.08674 | [High-Precision Fruit Localization Using Active Laser-Camera Scanning: Robust Laser Line Extraction for 2D-3D Transformation](https://arxiv.org/abs/2311.08674) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |
| 2311.08740 | [AdVENTR: Autonomous Robot Navigation in Complex Outdoor Environments](https://arxiv.org/abs/2311.08740) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |
| 2311.08787 | [Polygonal Cone Control Barrier Functions (PolyC2BF) for safe navigation in cluttered environments](https://arxiv.org/abs/2311.08787) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.08880 | [Motion Control of Two Mobile Robots under Allowable Collisions](https://arxiv.org/abs/2311.08880) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.08952 | [A novel concept for Titan robotic exploration based on soft morphing aerial robots](https://arxiv.org/abs/2311.08952) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Active Exploration & Information Gain | rule-assigned | 滚动窗口外 |
| 2311.08957 | [I Was Blind but Now I See: Implementing Vision-Enabled Dialogue in Social Robots](https://arxiv.org/abs/2311.08957) | 2023-11-15 | Legged Locomotion & Whole-body Control → Whole-body Coordination & Balance → Balance & Contact Regulation | rule-assigned | 滚动窗口外 |
| 2311.08983 | [Edge Accelerated Robot Navigation With Collaborative Motion Planning](https://arxiv.org/abs/2311.08983) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Motion Planning & Exploration → Global Path Planning | rule-assigned | 滚动窗口外 |
| 2311.09056 | [Range-Visual-Inertial Sensor Fusion for Micro Aerial Vehicle Localization and Navigation](https://arxiv.org/abs/2311.09056) | 2023-11-15 | Perception, Representation & State Estimation → Tactile & Multimodal Perception → Visuotactile & Proprioceptive Fusion | rule-assigned | 滚动窗口外 |
| 2311.09093 | [Why Autonomous Vehicles Are Not Ready Yet: A Multi-Disciplinary Review of Problems, Attempted Solutions, and Future Directions](https://arxiv.org/abs/2311.09093) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Pending specialty review | needs-review | 滚动窗口外 |
| 2311.09195 | [Self-Supervised Curriculum Generation for Autonomous Reinforcement Learning without Task-Specific Knowledge](https://arxiv.org/abs/2311.09195) | 2023-11-15 | Policy Learning & Embodied Foundation Models → Reinforcement Learning → Online Reinforcement Learning | rule-assigned | 滚动窗口外 |
| 2311.09346 | [Nothing Stands Still: A Spatiotemporal Benchmark on 3D Point Cloud Registration Under Large Geometric and Temporal Change](https://arxiv.org/abs/2311.09346) | 2023-11-15 | Data, Simulation & Evaluation → Benchmarks & Experimental Methods → Task & Capability Benchmarks | rule-assigned | 滚动窗口外 |
| 2311.09350 | [Generalizable Imitation Learning Through Pre-Trained Representations](https://arxiv.org/abs/2311.09350) | 2023-11-15 | Arm & General Object Manipulation → Grasping & Pick-place → Pending specialty review | needs-review | 滚动窗口外 |
| 2312.04570 | [Deep Reinforcement Learning for 2D Physics-Based Object Manipulation in Clutter](https://arxiv.org/abs/2312.04570) | 2023-11-14 | Arm & General Object Manipulation → Grasping & Pick-place → Pending specialty review | needs-review | 滚动窗口外 |
| 2312.04571 | [SwarMer: A Decentralized Localization Framework for Flying Light Specks](https://arxiv.org/abs/2312.04571) | 2023-11-15 | Navigation, Localization & Multi-robot Coordination → Localization & Mapping → Odometry & Relocalization | rule-assigned | 滚动窗口外 |

## 顶会来源变化

- 索引年份范围：刷新前 {'start': 2022, 'end': 2026}，刷新后 {'start': 2022, 'end': 2026}；具体检索会议和纳入边界以来源数据及覆盖报告为准。
- 本仓库来源目录已经按标题去重；身份匹配优先使用来源 ID，否则使用标准化标题与 venue 的确定性书目键。year 和 URL 是可更新元数据，纠正年份或换链接不是新增论文；同题匹配不是全文版本认证。
- 以下 year、venue、阅读及来源链接均保留索引原值；本次新增收录不表示新近发表或录用，移出也不表示撤稿。保留记录明细展示刷新后元数据。

### 顶会新增（0 条）

无。

### 顶会移出（0 条）

无。

### 顶会保留记录的元数据变化（13 条）

本节共 13 条，当前展示前 13 条；未截断。完整明细保留在[同日 JSON 收据](../data/catalog-refresh-2026-11-16.json)。

| 记录 ID | 标题 | year | venue | 来源链接 | 身份策略 |
|---|---|---:|---|---|---|
| bibliographic:0a00947a88d4c956030e2a4912a176a67c35072d30c593ecd3285827beaf580d | [Tree Instance Segmentation and Traits Estimation for Forestry Environments Exploiting LiDAR Data Collected by Mobile Robots](https://ora.ox.ac.uk/objects/uuid:d29224bc-f133-484f-b8eb-f99fb34b6eb3/files/sx920fz468) | 2024 | ICRA | [来源](https://doi.org/10.1109/ICRA57147.2024.10611169) | normalized_title+venue |
| bibliographic:1f5fe238a8e61ecf3f088dfbab93c75af199c78bb04295c9b17d8df526c27709 | [RP1M: A Large-Scale Motion Dataset for Piano Playing with Bi-Manual Dexterous Robot Hands](https://arxiv.org/abs/2408.11048) | 2024 | CoRL | [来源](https://dblp.org/rec/conf/corl/ZhaoCSGKSPB24) | normalized_title+venue |
| bibliographic:2b69a9709cd725bde64bf87f0538c2aac5ab194952f27f21a1fd03640f6effec | [Can Real-to-Sim Approaches Capture Dynamic Fabric Behavior for Robotic Fabric Manipulation?](https://eprints.gla.ac.uk/360594/) | 2025 | IROS | [来源](https://doi.org/10.1109/IROS60139.2025.11245811) | normalized_title+venue |
| bibliographic:4638543bb3ad10fb22dc9794724a717521a7ba0ce4acea6e14df9fdf93b52b88 | [SpecTac: A Visual-Tactile Dual-Modality Sensor Using UV Illumination](https://doi.org/10.1109/icra46639.2022.9812348) | 2022 | ICRA | [来源](https://doi.org/10.1109/icra46639.2022.9812348) | normalized_title+venue |
| bibliographic:4f211922aaf8a9f2a66a25e5405dd716299b16bf7d132df39b3ffb687d6daec8 | [Offline Reinforcement Learning for Visual Navigation](https://arxiv.org/abs/2212.08244) | 2022 | CoRL | [来源](https://dblp.org/rec/conf/corl/ShahBLKRL22) | normalized_title+venue |
| bibliographic:5b3c5d089f5db901655ab956e01665df0146860e607b9f1b3b31a4009180d407 | [Learning Generalizable Manipulation Policy with Adapter-Based Parameter Fine-Tuning](https://ora.ox.ac.uk/objects/uuid:f08f03ed-6d9b-4440-8580-3c9662c61991/files/sqv33rz87f) | 2024 | IROS | [来源](https://doi.org/10.1109/IROS58592.2024.10801544) | normalized_title+venue |
| bibliographic:5c02a48a55e0c99cc339ffd0240d0a4d0ae58205ad3de3c6e9e8859f64e4832d | [Jacta: A Versatile Planner for Learning Dexterous and Whole-body Manipulation](https://arxiv.org/abs/2408.01258) | 2024 | CoRL | [来源](https://dblp.org/rec/conf/corl/BrudigamASFHGSW24) | normalized_title+venue |
| bibliographic:89913718551f41e52ba445cca2e2bd9e73bd905043b7f8af99504fa0af906c9b | [Causal Policy Gradient for Whole-Body Mobile Manipulation](https://arxiv.org/pdf/2305.04866) | 2023 | RSS | [来源](https://dblp.org/rec/journals/corr/abs-2305-04866) | normalized_title+venue |
| bibliographic:8d288fd16a2947944d05f2f386acb9a751eb7dfd91c737983fb27178c22e2e87 | [SPEAR: A Simulator for Photorealistic Embodied AI Research](https://arxiv.org/abs/2607.06701) | 2026 | ECCV | [来源](https://dblp.org/rec/journals/corr/abs-2607-06701) | normalized_title+venue |
| bibliographic:acfc3bbded156d0c93f5973685562b1ca493313eeaa65129c7b87bec06ecfa80 | [6D Object Pose Tracking in Internet Videos for Robotic Manipulation](https://arxiv.org/abs/2503.10307) | 2025 | ICLR | [来源](https://dblp.org/rec/conf/iclr/PonimatkinCSFLP25) | normalized_title+venue |
| bibliographic:d1df228dba6f5d7bfd002ca837d95127a563a0648b8065340f91a8e816eb5c34 | [Exploring 3D Human Pose Estimation and Forecasting from the Robot’s Perspective: The HARPER Dataset](https://eprints.gla.ac.uk/330442/) | 2024 | IROS | [来源](https://doi.org/10.1109/IROS58592.2024.10802238) | normalized_title+venue |
| bibliographic:d9b60e10498b59edd01ada90a9fec9d371ec27f8017cc5d66997b4e9cfb96661 | [Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305) | 2025 | NeurIPS | [来源](https://dblp.org/rec/conf/nips/ShiLWLSZSBL25) | normalized_title+venue |
| bibliographic:e6ab253ee1dd6cb8a4e723b8a59bd87a0589ee4e151a08534662258b09337cca | [Natural Language Can Help Bridge the Sim2Real Gap](https://arxiv.org/abs/2405.10020) | 2024 | RSS | [来源](https://dblp.org/rec/conf/rss/0002FMM24) | normalized_title+venue |

## 分类、覆盖与发布边界

- 现有分类版本：4；刷新后状态计数：{'needs-review': 5644, 'reviewed': 101, 'rule-assigned': 21271}。
- 新增收录中有 10 条使用标题/摘要审核例外；其 arXiv ID 为 ['2611.17394', '2611.17529', '2611.17619', '2611.17631', '2611.17775', '2611.18176', '2611.18298', '2611.18372', '2611.18546', '2611.18562']。这些例外不代表全文精读或实验认证。
- 检索范围仅为 cs.RO（含交叉分类）与声明的滚动三年窗口；未纳入不证明论文不相关，不宣称“全网最全”。
- API 候选数量一致只说明数量核对通过，不能证明纳入规则、分页身份或语义分类完美。
- 使用现有分类与标题/摘要审核例外，不代表每篇已经人工全文精读或完成实验复现。
- 论文原始发表日期、既有分析审核日期和历史收据保留；当前文档同步不等于正文重新精读。
- 本收据的生成不会合并 PR #1，也不会发布主分支或公开网站；PR 未合并期间这些内容仍仅在更新分支上，远端状态需另行核验。

[机器可读刷新收据](../data/catalog-refresh-2026-11-16.json) · [日期与覆盖报告](coverage-report.md) · [分类图谱](../papers/taxonomy/README.md)
