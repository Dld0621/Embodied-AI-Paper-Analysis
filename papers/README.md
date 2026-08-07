# Curated Embodied AI Papers · 具身智能精选论文

> 74 curated papers · 2022–2026 · formally accepted at 10 major venues · updated 2026-08-07

这是一份精选导航，不是无边界的论文堆积。会议年份以正式会议为准；预印本日期不会替代录用年份。

This is a selective research map, not an exhaustive census. Conference year follows the formal venue record, not the preprint date.

## Coverage

| Venue | Papers | Venue | Papers |
|---|---:|---|---:|
| RSS | 15 | CoRL | 19 |
| ICRA | 1 | IROS | 1 |
| ICLR | 13 | ICML | 9 |
| NeurIPS | 4 | CVPR | 9 |
| ICCV | 2 | ECCV | 1 |

## Direction coverage · 方向覆盖

| Research direction | Papers | Years | Major venues |
|---|---:|---|---|
| Foundation Models & VLA · 基础模型与 VLA | 21 | 2022, 2023, 2024, 2025, 2026 | CVPR · CoRL · ICLR · ICML · ICRA · RSS |
| Manipulation & Imitation · 操作与模仿学习 | 11 | 2022, 2023, 2024, 2025, 2026 | CVPR · CoRL · ECCV · ICCV · RSS |
| Dexterity & Teleoperation · 灵巧操作与遥操作 | 10 | 2022, 2023, 2024, 2025, 2026 | CVPR · CoRL · IROS · RSS |
| Navigation & Embodied Agents · 导航与具身智能体 | 7 | 2022, 2023, 2024, 2025, 2026 | CVPR · CoRL · ICLR · NeurIPS |
| Humanoids & Locomotion · 人形机器人与运动控制 | 6 | 2022, 2023, 2024, 2025, 2026 | CoRL · ICLR · RSS |
| Perception & World Models · 感知与世界模型 | 9 | 2022, 2023, 2024, 2025, 2026 | CVPR · CoRL · ICML |
| Simulation, Data & Evaluation · 仿真、数据与评测 | 10 | 2022, 2023, 2024, 2025, 2026 | CoRL · ICLR · ICML · NeurIPS · RSS |

## Selection boundary · 收录边界

- Core window: 2022–2026, inclusive.
- Main-conference or official conference-track acceptance only.
- Workshops, withdrawn submissions, under-review papers, ambiguous multi-venue labels, and arXiv-only work are excluded from the core count.
- Every entry includes an official venue source; links marked `Paper` may point to arXiv or the official paper page.
- 2026 coverage is frozen at 2026-08-07 and only includes decisions already visible on official proceedings or conference pages.

## Foundation Models & VLA · 基础模型与 VLA (21)

How do multimodal foundation models turn perception and language into general robot actions?

多模态基础模型如何把感知与语言转化为可泛化的机器人动作？

**Pipeline:** `Images + language + state → Multimodal representation → Action generation → Robot execution`

**流程：** `图像、语言与状态 → 多模态表征 → 动作生成 → 机器人执行`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation | ICLR · Spatial reasoning | [Paper](https://openreview.net/forum?id=yngvAamNQi) · [Official](https://openreview.net/forum?id=yngvAamNQi) |
| 2026 | Hybrid Training for Vision-Language-Action Models | ICLR · Reasoning and action | [Paper](https://openreview.net/forum?id=IBJtOltTbx) · [Official](https://openreview.net/forum?id=IBJtOltTbx) |
| 2026 | MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation | ICLR · Memory-augmented VLA | [Paper](https://proceedings.iclr.cc/papers/search?q=MemoryVLA) · [Official](https://proceedings.iclr.cc/papers/search?q=MemoryVLA) |
| 2026 | Vision-Language-Action Instruction Tuning: From Understanding to Manipulation | ICLR · Instruction tuning | [Paper](https://proceedings.iclr.cc/papers/search?q=Vision-Language-Action+Instruction+Tuning) · [Official](https://proceedings.iclr.cc/papers/search?q=Vision-Language-Action+Instruction+Tuning) |
| 2026 | LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein Alignment | ICML · Representation alignment | [Paper](https://openreview.net/forum?id=gIkOQkb4fU) · [Official](https://openreview.net/forum?id=gIkOQkb4fU) |
| 2025 | RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete | CVPR · Robot multimodal model | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ji_RoboBrain_A_Unified_Brain_Model_for_Robotic_Manipulation_from_Abstract_CVPR_2025_paper.html) · [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Ji_RoboBrain_A_Unified_Brain_Model_for_Robotic_Manipulation_from_Abstract_CVPR_2025_paper.html) |
| 2025 | π0.5: a Vision-Language-Action Model with Open-World Generalization | CoRL · Open-world VLA | [Paper](https://proceedings.mlr.press/v305/black25a.html) · [Official](https://proceedings.mlr.press/v305/black25a.html) · [Code](https://github.com/Physical-Intelligence/openpi) |
| 2025 | HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation | ICLR · Hierarchical VLA | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html) · [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html) |
| 2025 | Latent Action Pretraining from Videos | ICLR · Learning from video | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html) · [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html) |
| 2025 | RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation | ICLR · Bimanual foundation model | [Paper](https://arxiv.org/abs/2410.07864) · [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html) · [Code](https://github.com/thu-ml/RoboticsDiffusionTransformer) |
| 2024 | CrossFormer: Scaling Cross-Embodied Learning for Manipulation | CoRL · Cross-embodiment learning | [Paper](https://arxiv.org/abs/2408.11812) · [Official](https://proceedings.mlr.press/v270/) |
| 2024 | OpenVLA: An Open-Source Vision-Language-Action Model | CoRL · Vision-language-action | [Paper](https://arxiv.org/abs/2406.09246) · [Official](https://proceedings.mlr.press/v270/) · [Code](https://github.com/openvla/openvla) |
| 2024 | Vision-Language Foundation Models as Effective Robot Imitators | ICLR · Vision-language imitation | [Paper](https://arxiv.org/abs/2311.13840) · [Official](https://proceedings.iclr.cc/paper_files/paper/2024/hash/71639c317fb0bf398835627b4418693e-Abstract-Conference.html) |
| 2024 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | ICRA · Cross-embodiment data | [Paper](https://arxiv.org/abs/2310.08864) · [Official](https://ieeexplore.ieee.org/abstract/document/10611477) · [Code](https://github.com/google-deepmind/open_x_embodiment) |
| 2024 | Octo: An Open-Source Generalist Robot Policy | RSS · Generalist robot policy | [Paper](https://arxiv.org/abs/2405.12213) · [Official](https://doi.org/10.15607/RSS.2024.XX.090) · [Code](https://github.com/octo-models/octo) |
| 2024 | RT-H: Action Hierarchies using Language | RSS · Action hierarchy | [Paper](https://arxiv.org/abs/2403.01823) · [Official](https://roboticsproceedings.org/rss20/index.html) |
| 2023 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | CoRL · Vision-language-action | [Paper](https://arxiv.org/abs/2307.15818) · [Official](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| 2023 | PaLM-E: An Embodied Multimodal Language Model | ICML · Embodied multimodal model | [Paper](https://arxiv.org/abs/2303.03378) · [Official](https://proceedings.mlr.press/v202/driess23a.html) |
| 2023 | VIMA: Robot Manipulation with Multimodal Prompts | ICML · Multimodal prompting | [Paper](https://arxiv.org/abs/2210.03094) · [Official](https://proceedings.mlr.press/v202/jiang23b.html) · [Code](https://github.com/vimalabs/VIMA) |
| 2023 | RT-1: Robotics Transformer for Real-World Control at Scale | RSS · Generalist robot policy | [Paper](https://arxiv.org/abs/2212.06817) · [Official](https://roboticsproceedings.org/rss19/p025.html) |
| 2022 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | CoRL · Language-grounded planning | [Paper](https://arxiv.org/abs/2204.01691) · [Official](https://proceedings.mlr.press/v205/ichter23a.html) · [Code](https://say-can.github.io/) |

## Manipulation & Imitation · 操作与模仿学习 (11)

How can robots acquire precise, robust manipulation skills from demonstrations and interaction?

机器人如何从示范与交互中获得精确、稳健的操作技能？

**Pipeline:** `Demonstrations + observations → Policy learning → Action sequence → Closed-loop execution`

**流程：** `示范与观测 → 策略学习 → 动作序列 → 闭环执行`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising | CVPR · Test-time policy steering | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html) · [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html) · [Code](https://hume-vla.github.io/) |
| 2025 | G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation | CVPR · 3D semantic flow | [Paper](https://arxiv.org/abs/2411.18369) · [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object_CVPR_2025_paper.html) |
| 2025 | OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints | CVPR · Open-vocabulary manipulation | [Paper](https://arxiv.org/abs/2501.03841) · [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Pan_OmniManip_Towards_General_Robotic_Manipulation_via_Object-Centric_Interaction_Primitives_as_CVPR_2025_paper.html) |
| 2025 | AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning | ICCV · Human-video transfer | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_AR-VRM_Imitating_Human_Motions_for_Visual_Robot_Manipulation_with_Analogical_ICCV_2025_paper.html) · [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_AR-VRM_Imitating_Human_Motions_for_Visual_Robot_Manipulation_with_Analogical_ICCV_2025_paper.html) · [Code](https://github.com/idejie/ar) |
| 2025 | EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow | ICCV · Learning from video | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) · [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) |
| 2025 | Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | RSS · Visual-tactile policy | [Paper](https://www.roboticsproceedings.org/rss21/p052.html) · [Official](https://www.roboticsproceedings.org/rss21/p052.html) |
| 2024 | ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation | CoRL · Constraint-based manipulation | [Paper](https://arxiv.org/abs/2409.01652) · [Official](https://proceedings.mlr.press/v270/) · [Code](https://github.com/huangwl18/ReKep) |
| 2024 | Track2Act: Predicting Point Tracks from Internet Videos enables Generalizable Robot Manipulation | ECCV · Learning from video | [Paper](https://arxiv.org/abs/2405.01527) · [Official](https://eccv.ecva.net/virtual/2024/poster/2120) |
| 2024 | 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations | RSS · 3D diffusion policy | [Paper](https://arxiv.org/abs/2403.03954) · [Official](https://www.roboticsproceedings.org/rss20/p067.html) · [Code](https://github.com/YanjieZe/3D-Diffusion-Policy) |
| 2023 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | RSS · Diffusion policy | [Paper](https://arxiv.org/abs/2303.04137) · [Official](https://roboticsproceedings.org/rss19/p026.html) · [Code](https://github.com/real-stanford/diffusion_policy) |
| 2022 | Human-to-Robot Imitation in the Wild | RSS · Learning from human video | [Paper](https://www.roboticsproceedings.org/rss18/p026.pdf) · [Official](https://www.roboticsproceedings.org/rss18/p026.html) |

## Dexterity & Teleoperation · 灵巧操作与遥操作 (10)

How do hands, tactile signals, and teleoperation interfaces support contact-rich control?

灵巧手、触觉信号与遥操作接口如何支撑接触丰富的控制？

**Pipeline:** `Human / vision / touch → Retargeting or contact model → Hand-arm control → Task outcome`

**流程：** `人体、视觉与触觉 → 重定向或接触模型 → 手臂协同控制 → 任务结果`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos | CVPR · Cross-hand dexterous control | [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.pdf) · [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.html) |
| 2025 | ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning | CVPR · Bimanual skill transfer | [Paper](https://arxiv.org/abs/2503.21860) · [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html) |
| 2025 | FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset | CoRL · Scalable data collection | [Paper](https://proceedings.mlr.press/v305/zhaxizhuoma25a.html) · [Official](https://proceedings.mlr.press/v305/zhaxizhuoma25a.html) |
| 2024 | Open-TeleVision: Teleoperation with Immersive Active Visual Feedback | CoRL · Immersive teleoperation | [Paper](https://arxiv.org/abs/2407.01512) · [Official](https://proceedings.mlr.press/v270/) · [Code](https://github.com/OpenTeleVision/TeleVision) |
| 2024 | GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators | IROS · Low-cost teleoperation | [Paper](https://arxiv.org/abs/2309.13037) · [Official](https://doi.org/10.1109/IROS58592.2024.10801581) · [Code](https://github.com/wuphilipp/gello_software) |
| 2024 | Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots | RSS · Portable data collection | [Paper](https://arxiv.org/abs/2402.10329) · [Official](https://roboticsproceedings.org/rss20/index.html) · [Code](https://github.com/real-stanford/universal_manipulation_interface) |
| 2023 | AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System | RSS · Teleoperation | [Paper](https://arxiv.org/abs/2307.04577) · [Official](https://roboticsproceedings.org/rss19/p015.html) · [Code](https://github.com/dexsuite/dex-retargeting) |
| 2023 | LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning | RSS · Dexterous hardware | [Paper](https://arxiv.org/abs/2309.06440) · [Official](https://roboticsproceedings.org/rss19/index.html) · [Code](https://github.com/leap-hand/LEAP_Hand_API) |
| 2023 | Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | RSS · Bimanual imitation | [Paper](https://arxiv.org/abs/2304.13705) · [Official](https://roboticsproceedings.org/rss19/index.html) · [Code](https://github.com/tonyzhaozh/aloha) |
| 2022 | In-Hand Object Rotation via Rapid Motor Adaptation | CoRL · Dexterous control | [Paper](https://arxiv.org/abs/2210.04887) · [Official](https://proceedings.mlr.press/v205/qi23a.html) · [Code](https://haozhi.io/hora/) |

## Navigation & Embodied Agents · 导航与具身智能体 (7)

How do agents build spatial memory, plan, and act over long horizons in open environments?

智能体如何在开放环境中建立空间记忆、规划并完成长时程行动？

**Pipeline:** `Egocentric sensing + goal → World state / memory → Planning → Navigation and interaction`

**流程：** `第一视角感知与目标 → 世界状态与记忆 → 规划 → 导航与交互`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | RoboAgent: Chaining Basic Capabilities for Embodied Task Planning | CVPR · Embodied planning | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_RoboAgent_Chaining_Basic_Capabilities_for_Embodied_Task_Planning_CVPR_2026_paper.html) · [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_RoboAgent_Chaining_Basic_Capabilities_for_Embodied_Task_Planning_CVPR_2026_paper.html) |
| 2025 | ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination | ICLR · Visual navigation | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb261df4322a8bd0a73093c4d8a0d02d-Paper-Conference.pdf) · [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eb261df4322a8bd0a73093c4d8a0d02d-Abstract-Conference.html) |
| 2024 | OpenEQA: Embodied Question Answering in the Era of Foundation Models | CVPR · Embodied question answering | [Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.pdf) · [Official](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html) |
| 2023 | HomeRobot: Open-Vocabulary Mobile Manipulation | CoRL · Mobile manipulation | [Paper](https://arxiv.org/abs/2306.11565) · [Official](https://proceedings.mlr.press/v229/) · [Code](https://github.com/facebookresearch/home-robot) |
| 2023 | Grounded Decoding: Guiding Text Generation with Grounded Models for Embodied Agents | NeurIPS · Grounded planning | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/bb3cfcb0284642a973dd631ec9184f2f-Abstract-Conference.html) · [Official](https://proceedings.neurips.cc/paper_files/paper/2023/hash/bb3cfcb0284642a973dd631ec9184f2f-Abstract-Conference.html) |
| 2022 | MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge | NeurIPS · Open-ended agents | [Paper](https://arxiv.org/abs/2206.08853) · [Official](https://proceedings.neurips.cc/paper_files/paper/2022/hash/74a67268c5cc5910f64938cac4526a90-Abstract.html) · [Code](https://github.com/MineDojo/MineDojo) |
| 2022 | ProcTHOR: Large-Scale Embodied AI Using Procedural Generation | NeurIPS · Procedural environments | [Paper](https://arxiv.org/abs/2206.06994) · [Official](https://proceedings.neurips.cc/paper_files/paper/2022/hash/27c546ab1e4f1d7d638e6a8dfbad9a07-Abstract-Conference.html) · [Code](https://github.com/allenai/procthor) |

## Humanoids & Locomotion · 人形机器人与运动控制 (6)

How can whole-body policies achieve agile, stable, and transferable motion?

全身策略如何实现敏捷、稳定且可迁移的运动？

**Pipeline:** `Motion reference + command → Retargeting / reinforcement learning → Whole-body control → Sim-to-real deployment`

**流程：** `动作参考与指令 → 重定向或强化学习 → 全身控制 → 仿真到现实部署`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | ICLR · Whole-body VLA | [Paper](https://proceedings.iclr.cc/papers/search?q=WholeBodyVLA) · [Official](https://proceedings.iclr.cc/papers/search?q=WholeBodyVLA) |
| 2025 | ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills | RSS · Humanoid sim-to-real | [Paper](https://www.roboticsproceedings.org/rss21/p066.pdf) · [Official](https://www.roboticsproceedings.org/rss21/p066.html) · [Code](https://github.com/LeCAR-Lab/ASAP) |
| 2024 | HumanPlus: Humanoid Shadowing and Imitation from Humans | CoRL · Humanoid imitation | [Paper](https://arxiv.org/abs/2406.10454) · [Official](https://proceedings.mlr.press/v270/) · [Code](https://github.com/MarkFzp/humanplus) |
| 2024 | OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning | CoRL · Whole-body teleoperation | [Paper](https://arxiv.org/abs/2406.08858) · [Official](https://proceedings.mlr.press/v270/) · [Code](https://github.com/LeCAR-Lab/human2humanoid) |
| 2023 | Learning and Adapting Agile Locomotion Skills by Transferring Experience | RSS · Agile locomotion | [Paper](https://www.roboticsproceedings.org/rss19/p051.pdf) · [Official](https://www.roboticsproceedings.org/rss19/p051.html) |
| 2022 | Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior | CoRL · Legged locomotion | [Paper](https://proceedings.mlr.press/v205/margolis23a/margolis23a.pdf) · [Official](https://proceedings.mlr.press/v205/margolis23a.html) · [Code](https://gmargo11.github.io/walk-these-ways) |

## Perception & World Models · 感知与世界模型 (9)

How do robots estimate task-relevant state and predict the consequences of action?

机器人如何估计任务相关状态并预测动作后果？

**Pipeline:** `Vision + touch + proprioception → State representation → World prediction → Policy conditioning`

**流程：** `视觉、触觉与本体感知 → 状态表征 → 世界预测 → 策略条件`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics | CVPR · Active perception | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html) · [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html) |
| 2025 | Tactile Beyond Pixels: Multisensory Touch Representations for Robot Manipulation | CoRL · Tactile representation | [Paper](https://proceedings.mlr.press/v305/) · [Official](https://proceedings.mlr.press/v305/) |
| 2024 | Theia: Distilling Diverse Vision Foundation Models for Robot Learning | CoRL · Representation distillation | [Paper](https://arxiv.org/abs/2407.20179) · [Official](https://proceedings.mlr.press/v270/) · [Code](https://github.com/bdaiinstitute/theia) |
| 2024 | 3D-VLA: A 3D Vision-Language-Action Generative World Model | ICML · 3D world model | [Paper](https://arxiv.org/abs/2403.01288) · [Official](https://proceedings.mlr.press/v235/zhen24a.html) |
| 2024 | DecisionNCE: Embodied Multimodal Representations via Implicit Preference Learning | ICML · Multimodal representation | [Paper](https://arxiv.org/abs/2402.18137) · [Official](https://proceedings.mlr.press/v235/) |
| 2024 | RoboDreamer: Learning Compositional World Models for Robot Imagination | ICML · Robot world models | [Paper](https://arxiv.org/abs/2404.12377) · [Official](https://proceedings.mlr.press/v235/) |
| 2023 | Multi-View Masked World Models for Visual Robotic Manipulation | ICML · Multi-view world models | [Paper](https://proceedings.mlr.press/v202/seo23a.html) · [Official](https://proceedings.mlr.press/v202/seo23a.html) |
| 2022 | Masked World Models for Visual Control | CoRL · Visual world models | [Paper](https://proceedings.mlr.press/v205/seo23a.html) · [Official](https://proceedings.mlr.press/v205/seo23a.html) |
| 2022 | R3M: A Universal Visual Representation for Robot Manipulation | CoRL · Visual representation | [Paper](https://arxiv.org/abs/2203.12601) · [Official](https://proceedings.mlr.press/v205/nair23a.html) · [Code](https://github.com/facebookresearch/r3m) |

## Simulation, Data & Evaluation · 仿真、数据与评测 (10)

How should embodied systems be trained, stress-tested, and compared reproducibly?

如何可复现地训练、压力测试并比较具身智能系统？

**Pipeline:** `Assets + task definitions → Simulation / data generation → Benchmark protocol → Metrics and error analysis`

**流程：** `资产与任务定义 → 仿真与数据生成 → 评测协议 → 指标与误差分析`

| Year | Paper | Venue / topic | Online links |
|---:|---|---|---|
| 2026 | FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects | ICML · Manipulation benchmark | [Paper](https://openreview.net/forum?id=1dWG9PJSVp) · [Official](https://openreview.net/forum?id=1dWG9PJSVp) |
| 2026 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | ICML · Synthetic data benchmark | [Paper](https://openreview.net/forum?id=itonej9GIV) · [Official](https://openreview.net/forum?id=itonej9GIV) |
| 2025 | MetaUrban: An Embodied AI Simulation Platform for Urban Micromobility | ICLR · Urban simulation | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad63cdaffe7c95c5f9c12276cdd893f9-Paper-Conference.pdf) · [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ad63cdaffe7c95c5f9c12276cdd893f9-Abstract-Conference.html) |
| 2024 | Eureka: Human-Level Reward Design via Coding Large Language Models | ICLR · Reward generation | [Paper](https://arxiv.org/abs/2310.12931) · [Official](https://openreview.net/forum?id=IEduRUO55F) · [Code](https://github.com/eureka-research/Eureka) |
| 2024 | DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset | RSS · Robot dataset | [Paper](https://arxiv.org/abs/2403.12945) · [Official](https://doi.org/10.15607/RSS.2024.XX.120) · [Code](https://github.com/droid-dataset/droid) |
| 2024 | RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots | RSS · Household simulation | [Paper](https://arxiv.org/abs/2306.14426) · [Official](https://roboticsproceedings.org/rss20/index.html) · [Code](https://github.com/ARISE-Initiative/robocasa) |
| 2023 | MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | CoRL · Demonstration generation | [Paper](https://arxiv.org/abs/2310.17596) · [Official](https://proceedings.mlr.press/v229/) · [Code](https://github.com/NVlabs/mimicgen) |
| 2023 | ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills | ICLR · Manipulation benchmark | [Paper](https://arxiv.org/abs/2302.04659) · [Official](https://openreview.net/forum?id=b_CQDy9vrD1) · [Code](https://github.com/haosulab/ManiSkill) |
| 2022 | BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation | CoRL · Household benchmark | [Paper](https://proceedings.mlr.press/v205/li23a.html) · [Official](https://proceedings.mlr.press/v205/li23a.html) · [Code](https://github.com/StanfordVL/OmniGibson) |
| 2022 | VLMbench: A Compositional Benchmark for Vision-and-Language Manipulation | NeurIPS · Language manipulation benchmark | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/04543a88eae2683133c1acbef5a6bf77-Abstract-Datasets_and_Benchmarks.html) · [Official](https://proceedings.neurips.cc/paper_files/paper/2022/hash/04543a88eae2683133c1acbef5a6bf77-Abstract-Datasets_and_Benchmarks.html) |

---

Source of truth: [`data/papers.json`](../data/papers.json). Run `python scripts/audit_catalog.py` before proposing changes.
