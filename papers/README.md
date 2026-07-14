# Embodied AI Paper Collection by Topic
> 按主题分类的论文索引，一级分类为大类，二级分类为子类，每个分类内按年份降序排列。
> 总计: 1021 篇论文 | 生成时间: 2026-07-14
> 标注: [arXiv] 在线论文 | [Code] 代码/项目页 | [Google Scholar] 搜索链接

## 快速导航

| 主题 | 主题 | 主题 |
|------|------|------|
| [Hand Retargeting](#hand-retargeting) | [Foundation Models](#foundation-models) | [VLA (Vision-Language-Action)](#vla-vision-language-action) |
| [3D Vision & Perception](#3d-vision--perception) | [Manipulation](#manipulation) | [Grasping](#grasping) |
| [Humanoid Robotics](#humanoid-robotics) | [Humanoid & Bimanual](#humanoid--bimanual) | [Locomotion](#locomotion) |
| [Policy Learning](#policy-learning) | [Simulation & World Models](#simulation--world-models) | [Navigation & Tracking](#navigation--tracking) |
| [Hardware & Sensing](#hardware--sensing) | [Data Generation](#data-generation) | [Video Generation](#video-generation) |
| [Others](#others) | [Uncategorized](#uncategorized) | |

<a id="hand-retargeting"></a>
## Hand Retargeting (38 篇)

### 核心结论

目前重定向最前沿已经不再是单纯追求"机器人姿态像人手"，而是追求：

> 在机器人结构不同、关节受限、存在碰撞和接触的情况下，仍能保持人的操作意图，并真正完成任务。

最强方案通常是混合架构：

**人体关键点/视频/VR → 快速几何映射 → 约束优化 → 接触与物体状态修正 → RL/残差策略补偿 → 视觉/触觉闭环**

### 三级分类标准

"级别"表示方法解决问题的深度，不等于论文质量。

| 等级 | 定义 | 能解决什么 | 主要局限 |
|------|------|-----------|---------|
| **L1** | 姿态/轨迹重定向 | 关节角、指尖位置、手掌姿态、身体关键点映射。 | 看起来像，但不一定接触稳定或完成任务。 |
| **L2** | 可执行重定向 | 加入关节限位、碰撞、接触、平滑、安全、物理可行性。 | 能执行，但通常仍依赖已知任务和环境。 |
| **L3** | 功能/意图重定向 | 保持物体运动、接触拓扑、旋拧轴、力、触觉、任务阶段和策略能力。 | 尚不能做到任意机器人、任意任务零样本迁移。 |

**分布：** L1：6 篇（平均覆盖度 70.8%）｜ L2：8 篇（平均覆盖度 81.6%）｜ L3：23 篇（平均覆盖度 85.5%）

### 覆盖度评分方法

`S = 0.20K + 0.20P + 0.15R + 0.15G + 0.20T + 0.10E`

| 因子 | 含义 |
|------|------|
| **K** | 运动学精度与平滑性 |
| **P** | 接触、物理可行性与安全性 |
| **R** | 实时、闭环和真机部署 |
| **G** | 跨机器人、免标定和跨形态能力 |
| **T** | 新物体、新任务、双手和长时序泛化 |
| **E** | 实验规模、真机数量和证据完整性 |

> 评分误差约为±5%；2026年尚未正式同行评审的工作约为±8%。

### 场景成熟度总览

| 场景 | 前沿成熟度 | 当前能力 |
|------|----------|---------|
| 受控环境下手部姿态实时映射 | **90–95%** | 已经非常成熟，可达到数百Hz至1kHz |
| 关节限位、自碰撞和基本安全 | **90–95%** | QP、CBF等方法可以提供显式约束 |
| 已知物体的抓取、搬运、开合 | **80–90%** | 结构化环境中较稳定 |
| 接触保持、旋拧、手内操作 | **70–85%** | 能处理特定接触模式，但仍需任务模型 |
| 双手协同和全身操作 | **65–82%** | 能完成长时序任务，但泛化和稳定性仍有限 |
| 新机器人形态的少样本迁移 | **65–80%** | 人形灵巧手较好，非人形手仍困难 |
| 单目视频到可执行机器人数据 | **55–75%** | 重建误差、遮挡和尺度误差仍明显 |
| 任意新任务、新物体零样本执行 | **35–55%** | 尚未真正解决 |
| 纯视觉开放环境持续遥操作 | **30–60%** | 遮挡仍是最大瓶颈之一 |

> 一个典型例子：视觉IK方案在结构化桌面任务中达到86.7%，但进入杂乱真实环境后，因为遮挡，成功率降至9.3%。
> 说明现在限制系统的往往已经不是IK本身，而是感知、接触和闭环修正。

### 重点研究路线

| 研究目标 | 最值得参考的论文 |
|---------|----------------|
| **高频实时姿态重定向** | GeoRT、AnyDexRT |
| **安全约束与碰撞处理** | Kilohertz-Safe |
| **接触保持** | TopoRetarget、DexFlow |
| **旋拧与手内操作** | DexTwist |
| **力和触觉重定向** | SoftAct、TactAlign |
| **可执行数据与策略迁移** | SPIDER、Physics-Driven Data Generation、DexH2R |

---

### 论文列表（按等级 & 覆盖度排序）

#### L1 姿态/轨迹重定向

| # | 论文 | 覆盖度 | 核心解法与效果 | 链接 |
|--:|------|-------:|---------------|------|
| 1 | Geometric Retargeting: A Principled, Ultrafast Neural Hand Retarget... | **85%** | 自监督几何网络，优化运动保真、C-space覆盖、捏合和自碰撞；达到1kHz，但主要解决运动学层面 | [arXiv](https://arxiv.org/abs/2503.07541) [Code](https://github.com/facebookresearch/GeoRT) |
| 2 | Tilde: Teleoperation for Dexterous In-Hand Manipulation Learning wi... | **73%** | 使用与机器人同构的TeleHand直接一对一控制；7个任务策略平均成功率90%，但跨形态能力弱 | [arXiv](https://arxiv.org/abs/2405.18804) [Code](https://github.com/iamlab-cmu/DeltaHands) |
| 3 | Analyzing Key Objectives in Human-to-Robot Retargeting for Dexterou... | **72%** | 系统分析指尖、方向、掌指距离等不同loss；研究价值高，但不是新的完整功能重定向框架 | [arXiv](https://arxiv.org/abs/2506.09384) [Code](https://mingrui-yu.github.io/retargeting/) |
| 4 | DexPilot: Vision-Based Teleoperation of Dexterous Robotic Hand-Arm ... | **72%** | 基于人手关键向量的优化式重定向，控制23-DoA臂手系统；奠基性强，但接触和跨形态能力有限 | [arXiv](https://arxiv.org/abs/1910.03135) [Code](https://yzqin.github.io/dexpilot/) |
| 5 | Unsupervised Neural Motion Retargeting for Humanoid Teleoperation | **65%** | 无配对GAN上肢重定向；验证动作数量和任务范围有限 | [arXiv](https://arxiv.org/abs/2406.00727) |
| 6 | Vision-Based Hand Shadowing for Robotic Manipulation via Inverse Ki... | **58%** | RGB-D 21点＋阻尼最小二乘IK；受控任务86.7%，开放环境受遮挡影响降至9.3% | [arXiv](https://arxiv.org/abs/2603.11383) |
#### L2 可执行重定向

| # | 论文 | 覆盖度 | 核心解法与效果 | 链接 |
|--:|------|-------:|---------------|------|
| 7 | Kilohertz-Safe: A Scalable Framework for Constrained Dexterous Reta... | **86%** | 差分空间凸QP＋控制障碍函数；平均9.05 ms，超过95%的帧满足安全条件 | [arXiv](https://arxiv.org/abs/2603.29213) |
| 8 | Retargeting Matters: General Motion Retargeting for Humanoid Motion... | **86%** | 解决足部滑动、自穿透和不可执行全身动作；策略追踪效果接近高质量闭源数据 | [arXiv](https://arxiv.org/abs/2510.02252) [Code](https://github.com/YanjieZe/GMR) |
| 9 | AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoper... | **82%** | 通用视觉遥操作框架，支持不同手、臂、相机、仿真与真机；RSS 2023 | [arXiv](https://arxiv.org/abs/2307.04577) [Code](https://github.com/dexsuite/dex-retargeting) |
| 10 | AnyDexRT: Calibration-Free Dexterous Hand Retargeting with Few-Shot... | **81%** | 自监督指尖对应＋少量人工引导＋捏合接触分类器；重点解决不同手型和坐标未标定问题 | [arXiv](https://arxiv.org/abs/2607.08341) [Code](https://chenxi-wang.github.io/projects/anydexrt/) |
| 11 | Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imi... | **80%** | 双手VR、触觉反馈、碰撞与奇异位形规避；提升遥操作成功率和数据质量 | [arXiv](https://arxiv.org/abs/2407.03162) [Code](https://github.com/Dingry/BunnyVisionPro) |
| 12 | DexFlow: A Unified Approach for Dexterous Hand Pose Retargeting and... | **80%** | 差分时间一致性loss＋接触图修正；改善穿透、自然度和跨手型数据生成 | [arXiv](https://arxiv.org/abs/2505.01083) |
| 13 | Kinematic Motion Retargeting for Contact-Rich Anthropomorphic Manip... | **79%** | 表面接触＋非等距形状匹配＋IK；验证5种手型、6种动作 | [arXiv](https://arxiv.org/abs/2402.04820) [Code](https://github.com/lakshmipathyarjun6/kinematic-motion-retargeting) |
| 14 | DOGlove: Dexterous Manipulation with a Low-Cost Open-Source Haptic ... | **79%** | 21-DoF动作捕捉＋力反馈＋动作/触觉重定向；硬件成本低于600美元 | [arXiv](https://arxiv.org/abs/2502.07730) [Code](https://github.com/TEA-Lab/DOGlove/) |
#### L3 功能/意图重定向

| # | 论文 | 覆盖度 | 核心解法与效果 | 链接 |
|--:|------|-------:|---------------|------|
| 15 | SPIDER: Scalable Physics-Informed Dexterous Retargeting | **92%** | 当前综合能力最强之一；物理采样＋虚拟接触课程，覆盖9种机器人、6个数据集，成功率提高18%，比RL基线快10倍 | [arXiv](https://arxiv.org/abs/2511.09484) [Code](https://jc-bao.github.io/spider-project/) |
| 16 | TopoRetarget Interaction-Preserving Retargeting for Dexterous Manip... | **90%** | 接触图＋拉普拉斯形变＋穿透处理；Pen-Spin训练成功率比基线提高40.6个百分点，并实现Wuji Hand零样本真机迁移 | [arXiv](https://arxiv.org/abs/2606.16272) |
| 17 | DexUMI: Using Human Hand as the Universal Manipulation Interface fo... | **89%** | 外骨骼减少运动学差距，图像修复减少视觉差距；两种灵巧手平均任务成功率86% | [arXiv](https://arxiv.org/abs/2505.21864) [Code](https://github.com/real-stanford/DexUMI) |
| 18 | Physics-Driven Data Generation for Contact-Rich Manipulation via Tr... | **89%** | 几何重定向＋轨迹优化＋物理参数变化；生成跨形态数据并零样本部署到双臂真机 | [arXiv](https://arxiv.org/abs/2502.20382) [Code](https://lujieyang.github.io/physicsgen/) |
| 19 | DexImit: Learning Bimanual Dexterous Manipulation from Monocular Hu... | **88%** | 单目视频重建、子任务分解、双手调度、机器人轨迹合成和数据增强一体化 | [arXiv](https://arxiv.org/abs/2602.10105) [Code](https://github.com/mujc2021/DexImit-Open) |
| 20 | DexH2R: Task-Oriented Dexterous Manipulation from Human to Robots | **88%** | 重定向基础动作＋任务残差策略＋测试时人手/物体轨迹引导；比此前方法提高约40% | [arXiv](https://arxiv.org/abs/2411.04428) |
| 21 | TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection S... | **88%** | 便携VR全身采集＋层级视觉策略；15分钟采集100次演示，遥操作采集成功率接近100% | [arXiv](https://arxiv.org/abs/2511.02832) [Code](https://twist-data.github.io/) |
| 22 | Functional Force-Aware Retargeting from Virtual Human Demos to Soft... | **87%** | 接触力分配＋几何接触修正；轨迹RMSE最高下降55%，方差最高下降69% | [arXiv](https://arxiv.org/abs/2604.01224) [Code](https://soft-act.github.io/) |
| 23 | TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment | **87%** | 用Rectified Flow对齐人手与机器人触觉潜空间；少于5分钟人类数据即可迁移到新物体和新任务 | [arXiv](https://arxiv.org/abs/2602.13579) |
| 24 | CLONE: Closed-Loop Whole-Body Humanoid Teleoperation with Long-Hori... | **87%** | MoE全身控制＋实时位置误差闭环；主要解决长距离、长时序漂移 | [arXiv](https://arxiv.org/abs/2506.08931) |
| 25 | DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies | **86%** | 人手数据与机器人数据联合训练；未知环境成功率68.5%，跨形态泛化提升5.8倍，RSS 2025 | [arXiv](https://arxiv.org/abs/2505.07813) [Code](https://github.com/dexwild/dexwild-training) |
| 26 | Beyond Mimicry: Learning Whole-Body Human-Humanoid Interaction from... | **85%** | 接触中心的物理重定向＋时空解耦策略；能保持人–人交互中的接触语义，但主要是仿真验证 | [arXiv](https://arxiv.org/abs/2601.09518) |
| 27 | TWIST: Teleoperated Whole-Body Imitation System | **85%** | MoCap重定向＋RL/BC全身控制器；统一完成行走、全身操作和表达动作 | [arXiv](https://arxiv.org/abs/2505.02833) [Code](https://humanoid-teleop.github.io/) |
| 28 | DexTwist: Dexterous Hand Retargeting for Twist Motion via Mixed Rea... | **84%** | 不直接复制手指轨迹，而是估计旋拧轴、角度和三指几何关系；适合开盖、拧钥匙和螺栓 | [arXiv](https://arxiv.org/abs/2605.12182) |
| 29 | DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation | **84%** | 虚拟物体控制器逐渐衰减，让策略逐步接管；面向双手、关节物体和长时序任务 | [arXiv](https://arxiv.org/abs/2505.24853) [Code](https://project-dexmachina.github.io/) |
| 30 | Cross-Hand Latent Representation for Vision-Language-Action Models | **84%** | 将不同机器人手动作编码进统一潜空间，使不同手型的数据可以共同训练VLA | [arXiv](https://arxiv.org/abs/2603.10158) [Code](https://xl-vla.github.io/) |
| 31 | HumDex: Humanoid Dexterous Manipulation Made Easy | **84%** | IMU全身追踪＋学习式手部重定向＋人类数据预训练/机器人数据微调 | [arXiv](https://arxiv.org/abs/2603.12260) [Code](https://github.com/physical-superintelligence-lab/HumDex) |
| 32 | ViViDex: Learning Vision-Based Dexterous Manipulation from Human Vi... | **84%** | 用轨迹引导RL把噪声视频轨迹修复为物理可行轨迹，再训练视觉策略；ICRA 2025 | [arXiv](https://arxiv.org/abs/2404.15709) [Code](https://github.com/zerchen/vividex_mujoco) |
| 33 | HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstra... | **83%** | 跨形态手眼表示＋全身控制器；将无机器人参与的人类演示迁移到移动操作机器人 | [arXiv](https://arxiv.org/abs/2603.03243) [Code](https://github.com/xxm19/hommi) |
| 34 | Learning to Transfer Human Hand Skills for Robot Manipulations | **82%** | 学习人手、机器人手和物体运动的联合流形；比单纯关键点重定向更关注交互合理性 | [arXiv](https://arxiv.org/abs/2501.04169) |
| 35 | Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body... | **81%** | 上肢IK保持精度，下肢RL保持稳定，CVAE预测运动先验协调全身；ICRA 2025 | [arXiv](https://arxiv.org/abs/2412.07773) [Code](https://mobile-tv.github.io/) |
| 36 | Mimic Intent, Not Just Trajectories | **80%** | 将低频任务意图与高频执行细节分开编码；实现一次示范技能迁移，但不是传统IK重定向 | [arXiv](https://arxiv.org/abs/2602.08602) [Code](https://github.com/RenMing-Huang/MINT) |
| 37 | Twisting Lids Off with Two Hands | **79%** | 双手开盖的接触建模、感知和RL；任务效果强，但重定向不是核心贡献 | [arXiv](https://arxiv.org/abs/2403.02338) [Code](https://github.com/ToruOwO/twisting-lids) |
#### 未评级

| # | 论文 | 覆盖度 | 核心解法与效果 | 链接 |
|--:|------|-------:|---------------|------|
| 38 | Robust and Expressive Humanoid Motion Retargeting via Optimization-... | **—** |  |  |


<a id="foundation-models"></a>
## Foundation Models (21 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | LiDAR Registration with Visual Foundation Models | [arXiv](https://arxiv.org/abs/2502.19374) |
| 2 | Meta Motivo Zero-Shot Whole-Body Humanoid Control via Behavioral Fo... | [arXiv](https://arxiv.org/abs/2504.11054) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Octo An Open-Source Generalist Robot Policy, websie | [arXiv](https://arxiv.org/abs/2405.12213) | [Code](https://github.com/octo-models/octo) |
| 2 | OpenVLA An Open-Source Vision-Language-Action Model | [arXiv](https://arxiv.org/abs/2406.09246) | [Code](https://github.com/openvla/openvla) |
| 3 | Predictive Inverse Dynamics Models are Scalable Learne | [arXiv](https://arxiv.org/abs/2412.15109) |
| 4 | RLDG Robotic Generalist Policy Distillation via Reinforcement Learning | [arXiv](https://arxiv.org/abs/2412.09858) |
| 5 | RoboMIND Benchmark on Multi-embodiment Intelligence No | [arXiv](https://arxiv.org/abs/2412.13877) | [Code](https://robomind.github.io) |
| 6 | Towards Generalist Robot Policies What Matters in Buil | [arXiv](https://arxiv.org/abs/2412.14058) |
| 7 | Video Prediction Policy A Generalist Robot Policy with | [arXiv](https://arxiv.org/abs/2412.14803) |
| 8 | OmniGlue Generalizable Feature Matching with Foundation Model Guidance | [arXiv](https://arxiv.org/abs/2405.12979) |
| 9 | articulate-anything Automatic Modeling of Articulated Objects via a... | [arXiv](https://arxiv.org/abs/2410.13882) |
| 10 | Theia: Distilling Diverse Vision Foundation Models for Robot Learning | [arXiv](https://arxiv.org/abs/2407.20179) |
| 11 | DecisionNCE: Embodied Multimodal Representations via Implicit Prefe... | [arXiv](https://arxiv.org/abs/2402.18137) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | InternVideo: General Video Foundation Models via Generative and Dis... | [arXiv](https://arxiv.org/abs/2212.03191) |

**2021**

| # | Title | Links |
|---|-------|-------|
| 1 | CLIP: Learning Transferable Visual Models From Natural Language Sup... | [arXiv](https://arxiv.org/abs/2103.00020) |
| 2 | HOP Hand-object interaction pretraining from videos | [arXiv](https://arxiv.org/abs/2409.08273) |

**2020**

| # | Title | Links |
|---|-------|-------|
| 1 | PointContrast: Unsupervised Pre-training for 3D Point Cloud Underst... | [arXiv](https://arxiv.org/abs/2007.10985) |
| 2 | DeiT: Training data-efficient image transformers & distillation thr... | [arXiv](https://arxiv.org/abs/2012.12877) |
| 3 | GPC Large-Scale Generative Pretraining for Transferable Motor Control | [arXiv](https://arxiv.org/abs/2606.29148) |
| 4 | SwAV: Unsupervised Learning of Visual Features by Contrasting Clust... | [arXiv](https://arxiv.org/abs/2006.09882) |
| 5 | Keypoints into the future Self-supervised correspondence in model-b... | [arXiv](https://arxiv.org/abs/2011.01975) |


<a id="vla-vision-language-action"></a>
## VLA (Vision-Language-Action) (6 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | Dexora Open-source VLA for High-DoF Bimanual Dexterity | [Google Scholar](https://scholar.google.com/scholar?q=Dexora%20Open-source%20VLA%20for%20High-DoF%20Bimanual%20Dexterity) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Chain-of-Modality: Learning Manipulation Programs from Multimodal H... | [arXiv](https://arxiv.org/abs/2504.13351) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | HandsOnVLM Vision-Language Models for Hand-Object Interaction Predi... | [arXiv](https://arxiv.org/abs/2412.13187) |
| 2 | Run-time Observation Interventions Make Vision-Language-Action Mode... | [arXiv](https://arxiv.org/abs/2410.01971) |
| 3 | RT-H: Action Hierarchies using Language | [arXiv](https://arxiv.org/abs/2403.01823) |
| 4 | ManipLLM: Embodied Multimodal Large Language Model for Object-Centr... | [arXiv](https://arxiv.org/abs/2312.16217) |


<a id="3d-vision--perception"></a>
## 3D Vision & Perception (78 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | GRAIL Generating Humanoid Loco-Manipulation from 3D Assets and Vide... | [arXiv](https://arxiv.org/abs/2606.05160) |
| 2 | Articraft An Agentic System for Scalable Articulated 3D Asset Gener... | [Google Scholar](https://scholar.google.com/scholar?q=Articraft%20An%20Agentic%20System%20for%20Scalable%20Articulated%203D%20Asset%20Generation) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | CuriousBot Interactive Mobile Exploration via Actionable 3D Relatio... | [arXiv](https://arxiv.org/abs/2501.13338) |
| 2 | Depth Any Camera Zero-Shot Metric Depth Estimation from Any Camera | [arXiv](https://arxiv.org/abs/2501.02464) |
| 3 | FP3 A 3D Foundation Policy for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2503.08950) | [Code](https://fp3.site) |
| 4 | Predicting 4D Hand Trajectory from Monocular Videos | [arXiv](https://arxiv.org/abs/2501.08329) |
| 5 | DAViD Modeling Dynamic Affordance of 3D Objects using Pre-trained V... | [arXiv](https://arxiv.org/abs/2501.08333) |
| 6 | Gamba Marry Gaussian Splatting with Mamba for single view 3D recons... | [arXiv](https://arxiv.org/abs/2404.01232) |
| 7 | RigAnything Template-Free Autoregressive Rigging for Diverse 3D Assets | [arXiv](https://arxiv.org/abs/2406.04572) |
| 8 | RoboGSim A Real2Sim2Real Robotic Gaussian Splatting Simulator | [arXiv](https://arxiv.org/abs/2411.11839) |
| 9 | SOLAMI Social Vision-Language-Action Modeling for Immersive Interac... | [arXiv](https://arxiv.org/abs/2412.07285) |
| 10 | AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vis... | [arXiv](https://arxiv.org/abs/2502.04981) |
| 11 | PHD: Personalized 3D Human Body Fitting with Diffusion Model Prior | [arXiv](https://arxiv.org/abs/2508.21257) |
| 12 | RobustSplat: Decoupling Densification and Dynamics for Transient-Fr... | [arXiv](https://arxiv.org/abs/2506.02751) |
| 13 | MVAR: Exploring Multi-View Autoregressive Generation | [arXiv](https://arxiv.org/abs/2506.18527) |
| 14 | CAST: Component-Aligned 3D Scene Reconstruction From an RGB Image | [arXiv](https://arxiv.org/abs/2502.12894) |
| 15 | LAM: Large Avatar Model for One-shot Animatable Gaussian Head | [arXiv](https://arxiv.org/abs/2502.17796) |
| 16 | DoRA: Facial Appearance Capture at Home with Patch-Level Reflectanc... | [arXiv](https://arxiv.org/abs/2506.03478) |
| 17 | VideoPainter: Plug-and-Play Context Control | [arXiv](https://arxiv.org/abs/2503.05639) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | 3D Diffusion Policy Generalizable Visuomotor Policy Le | [arXiv](https://arxiv.org/abs/2403.03954) | [Code](https://github.com/YanjieZe/3D-Diffusion-Policy) |
| 2 | Clio Real-time Task-Driven Open-Set 3D Scene Graphs | [arXiv](https://arxiv.org/abs/2404.13696) |
| 3 | DELTA Dense Efficient Long-range 3D Tracking for any video | [arXiv](https://arxiv.org/abs/2410.24211) |
| 4 | Reconstruction and Simulation of Elastic Objects with Spring-Mass 3... | [arXiv](https://arxiv.org/abs/2403.09434) |
| 5 | Robot See Robot Do Imitating Articulated Object Manipulation with M... | [arXiv](https://arxiv.org/abs/2409.18121) |
| 6 | Scaling 4D Representations | [Google Scholar](https://scholar.google.com/scholar?q=Scaling%204D%20Representations) |
| 7 | Splatt3R Zero-shot Gaussian Splatting from Uncalibrated Image Pairs | [arXiv](https://arxiv.org/abs/2408.13912) |
| 8 | CLAY A Controllable Large-scale Generative Model for Creating High-... | [arXiv](https://arxiv.org/abs/2306.09363) |
| 9 | ClearDepth Enhanced Stereo Perception of Transparent Objects for Ro... | [arXiv](https://arxiv.org/abs/2409.08926) |
| 10 | DSINE Rethinking Inductive Biases for Surface Normal Estimation | [arXiv](https://arxiv.org/abs/2403.00188) |
| 11 | Dynamic 3D Gaussian Tracking for Graph-Based Neural Dynamics Modeling | [arXiv](https://arxiv.org/abs/2410.18912) |
| 12 | GaussianGrasper 3D Language Gaussian Splatting for Open-vocabulary ... | [arXiv](https://arxiv.org/abs/2403.09637) |
| 13 | GenDP 3D Semantic Fields for Category-Level Generalizable Diffusion... | [arXiv](https://arxiv.org/abs/2410.17488) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 14 | GeoWizard Unleashing the Diffusion Priors for 3D Geometry Estimatio... | [arXiv](https://arxiv.org/abs/2303.09230) |
| 15 | Metric3Dv2 A Versatile Monocular Geometric Foundation Model for Zer... | [arXiv](https://arxiv.org/abs/2303.09230) |
| 16 | Physically Embodied Gaussian Splatting A Realtime Correctable World... | [arXiv](https://arxiv.org/abs/2403.23456) |
| 17 | RenderFormer Transformer-based Neural Rendering of Triangle Meshes ... | [arXiv](https://arxiv.org/abs/2505.21925) |
| 18 | Shape of Motion 4D Reconstruction from a Single Video | [arXiv](https://arxiv.org/abs/2407.13764) |
| 19 | SuGaR Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reco... | [arXiv](https://arxiv.org/abs/2303.11314) |
| 20 | Tactile DreamFusion Exploiting Tactile Sensing for 3D Generation | [arXiv](https://arxiv.org/abs/2412.06785) |
| 21 | Toon3D Seeing Cartoons from a New Perspective | [arXiv](https://arxiv.org/abs/2405.10320) |
| 22 | TutteNet Injective 3D Deformations by Composition of 2D Mesh Deform... | [arXiv](https://arxiv.org/abs/2309.09177) |
| 23 | Unifying 3D Representation and Control of Diverse Robots with a Sin... | [Google Scholar](https://scholar.google.com/scholar?q=Unifying%203D%20Representation%20and%20Control%20of%20Diverse%20Robots%20with%20a%20Single%20Camera) |
| 24 | VLM-Grounder A VLM Agent for Zero-Shot 3D Visual Grounding | [arXiv](https://arxiv.org/abs/2410.13860) |
| 25 | illusion3d 3D Multiview Illusion with 2D Diffusion Priors | [arXiv](https://arxiv.org/abs/2412.09625) |
| 26 | FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Ob... | [arXiv](https://arxiv.org/abs/2312.08344) |
| 27 | SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction | [arXiv](https://arxiv.org/abs/2311.12754) |
| 28 | GauHuman: Articulated Gaussian Splatting from Monocular Human Videos | [arXiv](https://arxiv.org/abs/2312.02973) |
| 29 | SurMo: Surface-based 4D Motion Modeling for Dynamic Human Rendering | [arXiv](https://arxiv.org/abs/2404.01225) |
| 30 | BiTT: Bi-directional Texture Reconstruction of Interacting Two Hand... | [arXiv](https://arxiv.org/abs/2403.08262) |
| 31 | UFORecon: Generalizable Sparse-View Surface Reconstruction | [arXiv](https://arxiv.org/abs/2403.05086) |
| 32 | RTG-SLAM: Real-time 3D Reconstruction at Scale Using Gaussian Splat... | [arXiv](https://arxiv.org/abs/2404.19706) |
| 33 | SMERF: Streamable Memory Efficient Radiance Fields for Real-Time La... | [arXiv](https://arxiv.org/abs/2312.07541) |
| 34 | DressCode: Autoregressively Sewing and Generating Garments From Tex... | [arXiv](https://arxiv.org/abs/2401.16465) |
| 35 | Motion-I2V: Consistent and Controllable Image-to-Video Generation w... | [arXiv](https://arxiv.org/abs/2401.15977) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene R... | [arXiv](https://arxiv.org/abs/2309.13101) |
| 2 | Flexible Techniques for Differentiable Rendering with 3D Gaussians | [arXiv](https://arxiv.org/abs/2308.14737) |
| 3 | GNFactor Multi-Task Real Robot Learning with Generaliz | [arXiv](https://arxiv.org/abs/2308.16891) |
| 4 | Real-time Photorealistic Dynamic Scene Representation and Rendering... | [arXiv](https://arxiv.org/abs/2310.10642) |
| 5 | SIGGRAPH Asia 2023 best paper, Fluid Simulation on Neural Flow Maps | [arXiv](https://arxiv.org/abs/2312.14635) |
| 6 | XCube Large-Scale 3D Generative Modeling using Sparse Voxel Hierarc... | [arXiv](https://arxiv.org/abs/2312.03806) |
| 7 | 3D-VisTA Pre-trained Transformer for 3D Vision and Text Alignment | [arXiv](https://arxiv.org/abs/2308.04352) |
| 8 | 3DShape2VecSet A 3D Shape Representation for Neural Fields and Gene... | [arXiv](https://arxiv.org/abs/2306.00308) |
| 9 | DreamGaussian Generative Gaussian Splatting for Efficient 3D Conten... | [arXiv](https://arxiv.org/abs/2309.16653) |
| 10 | GaussianDreamer Fast Generation from Text to 3D Gaussian Splatting ... | [arXiv](https://arxiv.org/abs/2310.08529) |
| 11 | HOLD Category-agnostic 3D Reconstruction of Interacting Hands and O... | [arXiv](https://arxiv.org/abs/2308.13725) |
| 12 | HyperFields Towards Zero-Shot Generation of NeRFs from Text | [arXiv](https://arxiv.org/abs/2304.02256) |
| 13 | OctFormer Octree-based Transformers for 3D Point Clouds | [arXiv](https://arxiv.org/abs/2305.03045) |
| 14 | Zero123++ a Single Image to Consistent Multi-view Diffusion Base Model | [arXiv](https://arxiv.org/abs/2310.15110) |
| 15 | Let 2D Diffusion Model Know 3D-Consistency for Robust Text-to-3D Ge... | [arXiv](https://arxiv.org/abs/2303.07937) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | Siggraph Asia 2022, Differentiable Point-Based Radiance Fields for ... | [arXiv](https://arxiv.org/abs/2205.14330) |
| 2 | GSGEN Text-to-3D using Gaussian Splatting | [arXiv](https://arxiv.org/abs/2309.16585) |
| 3 | Object-Aware Gaussian Splatting for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2411.11839) |
| 4 | PointNeXt Revisiting PointNet++ with Improved Training and Scaling ... | [arXiv](https://arxiv.org/abs/2206.04670) |
| 5 | NeRF2Real: Sim2real Transfer of Vision-guided Bipedal Motion Skills... | [arXiv](https://arxiv.org/abs/2210.04932) |

**2020**

| # | Title | Links |
|---|-------|-------|
| 1 | Vision Transformer An Image is Worth 16x16 Words Transformers for I... | [arXiv](https://arxiv.org/abs/2010.11929) |
| 2 | FrankMocap: A Monocular 3D Whole-Body Pose Estimation System via Re... | [arXiv](https://arxiv.org/abs/2008.08324) |

**2018**

| # | Title | Links |
|---|-------|-------|
| 1 | ChainQueen A Real-Time Differentiable Physical Simulator for Soft R... | [arXiv](https://arxiv.org/abs/1811.06020) |

**2017**

| # | Title | Links |
|---|-------|-------|
| 1 | PointNet: Deep Learning on Point Sets for 3D Classification and Seg... | [arXiv](https://arxiv.org/abs/1612.00593) |


<a id="manipulation"></a>
## Manipulation (29 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation | [arXiv](https://arxiv.org/abs/2502.10894) |
| 2 | ManipTrans Efficient Dexterous Bimanual Manipulation Transfer via R... | [arXiv](https://arxiv.org/abs/2503.21860) |
| 3 | BUMBLE Unifying Reasoning and Acting with Vision-Language Models fo... | [arXiv](https://arxiv.org/abs/2410.06237) |
| 4 | CogACT A Foundational Vision-Language-Action Model for Synergizing ... | [arXiv](https://arxiv.org/abs/2411.19650) |
| 5 | PolyTouch: A Robust Multi-Modal Tactile Sensor for Contact-Rich Man... | [arXiv](https://arxiv.org/abs/2504.19341) |
| 6 | Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integr... | [arXiv](https://arxiv.org/abs/2506.05168) |
| 7 | Learning from Imperfect Demonstrations with Self-Supervision for Ro... | [arXiv](https://arxiv.org/abs/2401.08957) |
| 8 | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and... | [arXiv](https://arxiv.org/abs/2409.20560) |
| 9 | OmniManip: Towards General Robotic Manipulation via Object-Centric ... | [arXiv](https://arxiv.org/abs/2501.03841) |
| 10 | G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizabl... | [arXiv](https://arxiv.org/abs/2411.18369) |
| 11 | AR-VRM: Imitating Human Motions for Visual Robot Manipulation with ... | [arXiv](https://arxiv.org/abs/2508.07626) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Evaluating Real-World Robot Manipulation Policies in Simulation | [arXiv](https://arxiv.org/abs/2405.05941) |
| 2 | Flow as the Cross-Domain Manipulation Interface | [arXiv](https://arxiv.org/abs/2407.15208) |
| 3 | Track2Act Predicting Point Tracks from Internet Videos enables Dive... | [arXiv](https://arxiv.org/abs/2405.01527) |
| 4 | Continuously Improving Mobile Manipulation with Autonomous Real-Wor... | [arXiv](https://arxiv.org/abs/2409.20568) |
| 5 | CrossFormer Scaling Cross-Embodied Learning for Manipulation | [arXiv](https://arxiv.org/abs/2408.11812) |
| 6 | HIL-SERL Precise and Dexterous Robotic Manipulation via Human-in-th... | [arXiv](https://arxiv.org/abs/2405.02287) |
| 7 | Learning to Transfer Human Hand Skills for Robot Manipulations | [Google Scholar](https://scholar.google.com/scholar?q=Learning%20to%20Transfer%20Human%20Hand%20Skills%20for%20Robot%20Manipulations) |
| 8 | MPI Learning Manipulation by Predicting Interaction | [arXiv](https://arxiv.org/abs/2406.00439) |
| 9 | Position Scaling Simulation is Neither Necessary Nor Sufficient for... | [Google Scholar](https://scholar.google.com/scholar?q=Position%20Scaling%20Simulation%20is%20Neither%20Necessary%20Nor%20Sufficient%20for%20In-the-Wild%20Robot%20Manipulation) |
| 10 | ReKep Spatio-Temporal Reasoning of Relational Keypoint Constraints ... | [arXiv](https://arxiv.org/abs/2409.01652) |
| 11 | GraspSplats: Efficient Manipulation with 3D Feature Splatting | [arXiv](https://arxiv.org/abs/2409.02084) |
| 12 | RiEMann: Near Real-Time SE(3)-Equivariant Robot Manipulation withou... | [arXiv](https://arxiv.org/abs/2403.19460) |
| 13 | SAGE: Bridging Semantic and Actionable Parts for Generalizable Arti... |  |
| 14 | RVT-2: Learning Precise Manipulation from Few Demonstrations |  |
| 15 | CooHOI: Learning Cooperative Human-Object Interaction with Manipula... | [arXiv](https://arxiv.org/abs/2406.14558) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | On Bringing Robots Home | [arXiv](https://arxiv.org/abs/2311.16098) |

**2018**

| # | Title | Links |
|---|-------|-------|
| 1 | QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robot... | [arXiv](https://arxiv.org/abs/1806.10293) |

**1968**

| # | Title | Links |
|---|-------|-------|
| 1 | The Kinematics of Manipulators Under Computer Control | [Google Scholar](https://scholar.google.com/scholar?q=The%20Kinematics%20of%20Manipulators%20Under%20Computer%20Control) |


<a id="grasping"></a>
## Grasping (23 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | Human Universal Grasping | [arXiv](https://arxiv.org/abs/2606.17054) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | A Careful Examination of Large Behavior Models for Multitask Dexter... | [arXiv](https://arxiv.org/abs/2507.05331) |
| 2 | D(R,O) Grasp: A Unified Representation of Robot and Object Interact... | [arXiv](https://arxiv.org/abs/2410.01702) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Complementarity-Free Multi-Contact Modeling and Optimization for De... | [arXiv](https://arxiv.org/abs/2408.07855) |
| 2 | Learning Time-Optimal and Speed-Adjustable Tactile In-Hand Manipula... | [arXiv](https://arxiv.org/abs/2411.13148) |
| 3 | Object-Centric Dexterous Manipulation from Human Motion Data | [arXiv](https://arxiv.org/abs/2411.04005) |
| 4 | SpringGrasp Synthesizing Compliant Dexterous Grasps under Shape Unc... | [arXiv](https://arxiv.org/abs/2404.13532) |
| 5 | AnyDexGrasp Learning General Dexterous Grasping for Any Hands with ... | [arXiv](https://arxiv.org/abs/2309.06038) |
| 6 | DexCatch Learning to Catch Arbitrary Objects with Dexterous Hands | [arXiv](https://arxiv.org/abs/2310.08809) |
| 7 | DexSinGrasp Learning a Unified Policy for Dexterous Object Singulat... | [arXiv](https://arxiv.org/abs/2504.04516) |
| 8 | DextrAH-RGB Visuomotor Policies to Grasp Anything with Dexterous Hands | [arXiv](https://arxiv.org/abs/2412.01791) |
| 9 | Do as I Do Dexterous Manipulation Data from Everyday Human Videos | [arXiv](https://arxiv.org/abs/2606.19333) |
| 10 | EyeSight Hand Design of a Fully-Actuated Dexterous Robot Hand with ... | [arXiv](https://arxiv.org/abs/2408.06265) |
| 11 | Grasp Multiple Objects with One Hand | [arXiv](https://arxiv.org/abs/2310.15599) |
| 12 | KODex On the Utility of Koopman Operator Theory in Learning Dextero... | [arXiv](https://arxiv.org/abs/2303.13446) |
| 13 | Omnigrasp Grasping Diverse Objects with Simulated Humanoids | [arXiv](https://arxiv.org/abs/2407.11385) |
| 14 | The GRASP Taxonomy of Human Grasp Types | [Google Scholar](https://scholar.google.com/scholar?q=The%20GRASP%20Taxonomy%20of%20Human%20Grasp%20Types) |
| 15 | DeliGrasp: Inferring Object Properties with LLMs for Adaptive Grasp... |  |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Learning a Universal Human Prior for Dexterous Manipulation from Hu... | [arXiv](https://arxiv.org/abs/2304.04602) |
| 2 | RA-L 2023, Learning Continuous Grasping Function with a Dexterous H... | [arXiv](https://arxiv.org/abs/2207.05053) |
| 3 | GraspGF Learning Score-based Grasping Primitive for Human-assisting... | [arXiv](https://arxiv.org/abs/2309.06038) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | Learning to use chopsticks in diverse gripping styles | [arXiv](https://arxiv.org/abs/2205.14313) |

**2020**

| # | Title | Links |
|---|-------|-------|
| 1 | DexRes Physics-Based Dexterous Manipulations with Estimated Hand Po... | [Google Scholar](https://scholar.google.com/scholar?q=DexRes%20Physics-Based%20Dexterous%20Manipulations%20with%20Estimated%20Hand%20Poses%20and%20Residual%20Reinforcement%20Le) |


<a id="humanoid-robotics"></a>
## Humanoid Robotics (17 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | OmniContact Chaining Meta-Skills via Contact Flow for Generalizable... | [arXiv](https://arxiv.org/abs/2606.26201) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation | [arXiv](https://arxiv.org/abs/2502.10894) |
| 2 | Versatile Loco-Manipulation through Flexible Interlimb Coordination | [arXiv](https://arxiv.org/abs/2506.07876) |
| 3 | ExtremControl Low-Latency Humanoid Teleoperation with Direct Extrem... | [arXiv](https://arxiv.org/abs/2602.11321) |
| 4 | I-CTRL Imitation to Control Humanoid Robots Through Constrained Rei... | [arXiv](https://arxiv.org/abs/2405.08726) |
| 5 | InterMimic Towards Universal Whole-Body Control for Physics-Based H... | [arXiv](https://arxiv.org/abs/2502.20390) |
| 6 | MotionDisco Motion Discovery for Extreme Humanoid Loco-Manipulation | [arXiv](https://arxiv.org/abs/2606.06139) |
| 7 | Opt2Skill Imitating Dynamically-feasible Whole-Body Trajectories fo... | [arXiv](https://arxiv.org/abs/2409.20514) |
| 8 | WildLMA Long Horizon Loco-MAnipulation in the Wild | [arXiv](https://arxiv.org/abs/2411.15131) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Fusing uncalibrated IMUs and handheld smartphone video to reconstru... | [arXiv](https://arxiv.org/abs/2405.17368) |
| 2 | Humanoid Locomotion as Next Token Prediction | [arXiv](https://arxiv.org/abs/2402.19469) |
| 3 | Humanoid Parkour Learning | [arXiv](https://arxiv.org/abs/2406.10759) |
| 4 | Learning Humanoid Locomotion over Challenging Terrain | [arXiv](https://arxiv.org/abs/2410.03654) |
| 5 | OKAMI Teaching Humanoid Robots Manipulation Skills through Single V... | [arXiv](https://arxiv.org/abs/2410.11792) |
| 6 | CoorDex Coordinating Body and Hand Priors for Continuous Dexterous ... | [arXiv](https://arxiv.org/abs/2606.23680) |
| 7 | WARP Whole-Body Retargeting for Learning from Offline Human Demonst... | [arXiv](https://arxiv.org/abs/2606.29940) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Sim-to-Real Learning for Humanoid Box Loco-Manipulation | [arXiv](https://arxiv.org/abs/2310.03191) |


<a id="humanoid--bimanual"></a>
## Humanoid & Bimanual (6 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Visual Imitation Enables Contextual Humanoid Control | [arXiv](https://arxiv.org/abs/2505.03729) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleo... | [arXiv](https://arxiv.org/abs/2406.08858) |
| 2 | HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomoti... | [arXiv](https://arxiv.org/abs/2403.10506) |
| 3 | WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts |  |
| 4 | Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation (H2O | [arXiv](https://arxiv.org/abs/2403.04436) |
| 5 | HumanPlus: Humanoid Shadowing and Imitation from Humans | [arXiv](https://arxiv.org/abs/2406.10454) |


<a id="locomotion"></a>
## Locomotion (20 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Generalized Animal Imitator Agile Locomotion with Versatile Motion ... | [arXiv](https://arxiv.org/abs/2310.01408) |
| 2 | NaVILA Legged Robot Vision-Language-Action Model for Navigation | [arXiv](https://arxiv.org/abs/2411.19650) |
| 3 | Gait-Conditioned Reinforcement Learning with Multi-Phase Curriculum... | [arXiv](https://arxiv.org/abs/2505.20619) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Full-Order Sampling-Based MPC for Torque-Level Locomotion Control v... | [arXiv](https://arxiv.org/abs/2409.15610) |
| 2 | Helpful DoggyBot Open-World Object Fetching using Legged Robots and... | [arXiv](https://arxiv.org/abs/2410.00231) |
| 3 | Learning Force Control for Legged Manipulation | [arXiv](https://arxiv.org/abs/2405.01402) |
| 4 | Learning Humanoid Locomotion over Challenging Terrain | [arXiv](https://arxiv.org/abs/2410.03654) |
| 5 | RA-L 2024, SLoMo A General System for Legged Robot Motion Imitation... | [arXiv](https://arxiv.org/abs/2304.14389) | [Code](https://slomo-legs.github.io) |
| 6 | Grow Your Limits Continuous Improvement with Real-World RL for Robo... | [arXiv](https://arxiv.org/abs/2310.17634) |
| 7 | Learning Robotic Locomotion Affordances and Photorealistic Simulato... | [Google Scholar](https://scholar.google.com/scholar?q=Learning%20Robotic%20Locomotion%20Affordances%20and%20Photorealistic%20Simulators%20from%20Human-Captured%20Data) |
| 8 | Learning coordinated badminton skills for legged manipulators | [Google Scholar](https://scholar.google.com/scholar?q=Learning%20coordinated%20badminton%20skills%20for%20legged%20manipulators) |
| 9 | LucidSim Learning Agile Visual Locomotion from Generated Images | [Google Scholar](https://scholar.google.com/scholar?q=LucidSim%20Learning%20Agile%20Visual%20Locomotion%20from%20Generated%20Images) |
| 10 | Advancing Humanoid Locomotion: Mastering Challenging Terrains with ... |  |
| 11 | Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion |  |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Extreme Parkour with Legged Robots | [arXiv](https://arxiv.org/abs/2309.14341) |
| 2 | Learning Vision-Based Bipedal Locomotion for Challenging Terrain  T... | [arXiv](https://arxiv.org/abs/2309.14594) |
| 3 | Learning Vision-based Pursuit-Evasion Robot Policies | [arXiv](https://arxiv.org/abs/2308.16185) |
| 4 | Prompt a Robot to Walk with Large Language Models | [arXiv](https://arxiv.org/abs/2309.09969) |
| 5 | Robust and Versatile Bipedal Jumping Control through Reinforcement ... | [arXiv](https://arxiv.org/abs/2302.09450) |
| 6 | Barkour Benchmarking Animal-level Agility with Quadruped Robots | [arXiv](https://arxiv.org/abs/2305.14654) |


<a id="policy-learning"></a>
## Policy Learning (95 篇)

<a id="policy-learning-diffusion-policy"></a>
### Diffusion Policy (58 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | MotionStreamer Streaming Motion Generation via Diffusion-based Auto... | [arXiv](https://arxiv.org/abs/2503.15451) |
| 2 | Discrete Policy: Learning Disentangled Action Space for Multi-Task ... | [arXiv](https://arxiv.org/abs/2409.18707) |
| 3 | This&That: Language-Gesture Controlled Video Generation for Robot P... | [arXiv](https://arxiv.org/abs/2407.05530) |
| 4 | ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy | [arXiv](https://arxiv.org/abs/2411.03990) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | EquiBot SIM(3)-Equivariant Diffusion Policy for Generalizable and D... | [arXiv](https://arxiv.org/abs/2407.01479) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 2 | D3RoMa Disparity Diffusion-based Depth Sensing for Material-Agnosti... | [arXiv](https://arxiv.org/abs/2406.13640) |
| 3 | DiMSam Diffusion Models as Samplers for Task and Motion Planning un... | [arXiv](https://arxiv.org/abs/2306.13196) |
| 4 | Learning to Read Braille Bridging the Tactile | [arXiv](https://arxiv.org/abs/2304.01182) |
| 5 | Diffusion Co-Policy for Synergistic Human-Robot Collab | [arXiv](https://arxiv.org/abs/2406.05216) |
| 6 | Sparse Diffusion Policy A Sparse | [arXiv](https://arxiv.org/abs/2307.01531) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 7 | Equivariant Diffusion Policy | [arXiv](https://arxiv.org/abs/2407.01812) |
| 8 | Render and Diffuse: Aligning Image and Action Spaces for Diffusion-... |  |
| 9 | Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning |  |
| 10 | Learning an Actionable Discrete Diffusion Policy via Large-Scale Ac... | [arXiv](https://arxiv.org/abs/2402.14407) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | EDGI Equivariant Diffusion for Planning with Embodied Agents.](http... | [arXiv](https://arxiv.org/abs/2303.12410) |
| 2 | Diffusion Policy Visuomotor Policy Learning via Action Diffusion.](... | [arXiv](https://arxiv.org/abs/2303.04137) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 3 | ControlNet Adding Conditional Control to Text-to-Image Diffusion Mo... | [arXiv](https://arxiv.org/abs/2302.05543) |
| 4 | Learning Universal Policies via Text-Guided Video Generation.](http... | [arXiv](https://arxiv.org/abs/2302.00111) |
| 5 | Scaling Up and Distilling Down Language-Guided Robot Skill | [arXiv](https://arxiv.org/abs/2307.14535) |
| 6 | IDQL Implicit Q-Learning as an Actor-Critic Method with Diffusion | [arXiv](https://arxiv.org/abs/2304.10573) |
| 7 | Diffusion Model is an Effective Planner and Data Synthesizer for Mu... | [arXiv](https://arxiv.org/abs/2305.14590) |
| 8 | Generating Behaviorally Diverse Policies with Latent Diffusion Mode... | [arXiv](https://arxiv.org/abs/2302.01288) |
| 9 | Instructed Diffuser with Temporal Condition Guidance for Offline Re... | [arXiv](https://arxiv.org/abs/2305.12413) |
| 10 | Efficient Diffusion Policies for Offline Reinforcement Learning.](h... | [arXiv](https://arxiv.org/abs/2305.20081) |
| 11 | Crossway Diffusion Improving Diffusion-based Visuomotor Policy via ... | [arXiv](https://arxiv.org/abs/2311.01458) |
| 12 | AdaptDiffuser Diffusion Models as Adaptive Self-evolving Planners.]... | [arXiv](https://arxiv.org/abs/2305.08786) |
| 13 | Value function estimation using conditional diffusion models for co... | [arXiv](https://arxiv.org/abs/2306.07290) |
| 14 | ReorientDiff Diffusion Model based Reorientation for Object M | [arXiv](https://arxiv.org/abs/2303.12774) |
| 15 | MetaDiffuser Diffusion Model as Conditional Planner for Offline Met... | [arXiv](https://arxiv.org/abs/2303.04607) |
| 16 | Extracting Reward Functions from Diffusion Mod | [arXiv](https://arxiv.org/abs/2306.01804) |
| 17 | Goal-Conditioned Imitation Learning using Score-based Diffusion Pol... | [arXiv](https://arxiv.org/abs/2307.02909) |
| 18 | Shelving, Stacking, Hanging Relational Pose Diffusion for Multi-mod... | [arXiv](https://arxiv.org/abs/2307.04751) |
| 19 | SafeDiffuser Safe Planning with Diffusion Probabilistic Models.](ht... | [arXiv](https://arxiv.org/abs/2306.00148) |
| 20 | Policy Representation via Diffusion Probability Model for Reinforce... | [arXiv](https://arxiv.org/abs/2306.08122) |
| 21 | httpsarxiv.orgpdf2302 | [arXiv](https://scholar.google.com/scholar?q=Yoneda%2C%20Takuma%2C%20et%20al.%20%5BTo%20the%20Noise%20and%20Back%20Diffusion%20for%20Shared%20Autonomy.%5D%28httpsarxiv.orgpdf2302.) |
| 22 | Scaling robot learning with semantically imagined experience.](http... | [arXiv](https://arxiv.org/abs/2302.11550) |
| 23 | LAD Language Augmented Diffusion for Reinforcement Learning.](https... | [arXiv](https://arxiv.org/abs/2305.18278) |
| 24 | MADiff Offline Multi-agent Learning with Diffusion Models.](httpsar... | [arXiv](https://arxiv.org/abs/2305.12322) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | Classifier-Free Diffusion Guidance | [arXiv](https://arxiv.org/abs/2207.12598) |
| 2 | Diffusion-LM Improves Controllable Text Generation | [arXiv](https://arxiv.org/abs/2205.14217) |
| 3 | Is Conditional Generative Modeling all you need for Decision-Making... | [arXiv](https://arxiv.org/abs/2211.15657) |
| 4 | Imagen Photorealistic Text-to-Image Diffusion Models with Deep Lang... | [arXiv](https://arxiv.org/abs/2205.11487) |
| 5 | Planning with Diffusion for Flexible Behavior Synthesis.](httpsarxi... | [arXiv](https://arxiv.org/abs/2205.09991) |
| 6 | StructDiffusion Object-centric diffusion for semantic rearrangement... | [arXiv](https://arxiv.org/abs/2304.08968) |
| 7 | Contrastive Energy Prediction for Exact Energy-Guided Diffusion Sam... | [arXiv](https://arxiv.org/abs/2304.03759) |
| 8 | NFD 3D Neural Field Generation using Triplane Diffusion | [arXiv](https://arxiv.org/abs/2211.16677) |
| 9 | Point-E A System for Generating 3D Point Clouds from Complex Prompt... | [arXiv](https://arxiv.org/abs/2212.08751) |
| 10 | Prompt-to-Prompt Image Editing with Cross-Attention Control | [arXiv](https://arxiv.org/abs/2208.01626) |
| 11 | Stable Diffusion High-Resolution Image Synthesis with Latent Diffus... | [arXiv](https://arxiv.org/abs/2112.10752) |
| 12 | SE (3)-DiffusionFields Learning cost functions for joint grasp and ... | [arXiv](https://arxiv.org/abs/2209.11703) |
| 13 | Diffusion policies as an expressive policy class for offline reinfo... | [arXiv](https://arxiv.org/abs/2204.06191) |
| 14 | dpm-solver | [arXiv](https://arxiv.org/abs/2206.00927) |
| 15 | k-diffusion Elucidating the Design Space of Diffusion-Based Generat... | [arXiv](https://arxiv.org/abs/2206.00364) |

**2021**

| # | Title | Links |
|---|-------|-------|
| 1 | Guided Diffusion Diffusion Models Beat GANS on Image Synthesis | [arXiv](https://arxiv.org/abs/2105.05233) |
| 2 | iDDPM Improved Denoising Diffusion Probabilistic Models | [arXiv](https://arxiv.org/abs/2006.11239) |

**2020**

| # | Title | Links |
|---|-------|-------|
| 1 | Score-Based Generative Modeling through Stochastic Differential Equ... | [arXiv](https://arxiv.org/abs/2011.13456) |
| 2 | Denoising Diffusion Probabilistic Models | [arXiv](https://arxiv.org/abs/2006.11239) |
| 3 | DDIM Denoising Diffusion Implicit Models | [arXiv](https://arxiv.org/abs/2010.02502) |

<a id="policy-learning-reinforcement-learning"></a>
### Reinforcement Learning (37 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Reinforcement Learning with Action Chunking | [arXiv](https://arxiv.org/abs/2507.07969) |
| 2 | TD-M(PC)2 Improving Temporal Difference MPC Through Policy Constraint | [arXiv](https://arxiv.org/abs/2502.03550) |
| 3 | BAKU An Efficient Transformer for Multi-Task Policy Learning | [arXiv](https://arxiv.org/abs/2406.07539) |
| 4 | Body Transformer Leveraging Robot Embodiment for Policy Learning | [arXiv](https://arxiv.org/abs/2408.06316) |
| 5 | FACTR Force-Attending Curriculum Training for Contact-Rich Policy L... | [arXiv](https://arxiv.org/abs/2502.17432) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Continuous Control with Coarse-to-fine Reinforcement Learning | [arXiv](https://arxiv.org/abs/2407.07787) |
| 2 | Dreamitate Real-World Visuomotor Policy Learning via Video Generation | [arXiv](https://arxiv.org/abs/2406.16862) |
| 3 | From Imitation to Refinement -- Residual RL for Precise Assembly | [arXiv](https://arxiv.org/abs/2407.16677) |
| 4 | In-Context Imitation Learning via Next-Token Prediction | [arXiv](https://arxiv.org/abs/2408.15980) |
| 5 | Reinforcement Learning from Wild Animal Videos | [arXiv](https://arxiv.org/abs/2412.04273) |
| 6 | Unsupervised-to-Online Reinforcement Learning | [arXiv](https://arxiv.org/abs/2408.14785) |
| 7 | CBIL Collective Behavior Imitation Learning for Fish from Real Videos | [arXiv](https://arxiv.org/abs/2504.00234) |
| 8 | DigiRL Training In-The-Wild Device-Control Agents with Autonomous R... | [arXiv](https://arxiv.org/abs/2406.11896) |
| 9 | From Imitation to Refinement Residual RL for Precise Visual Assembl... | [arXiv](https://arxiv.org/abs/2407.16677) |
| 10 | HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers | [arXiv](https://arxiv.org/abs/2410.05273) |
| 11 | Learning to Manipulate Anywhere: A Visual Generalizable Framework F... | [arXiv](https://arxiv.org/abs/2407.15815) |
| 12 | Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning | [arXiv](https://arxiv.org/abs/2408.14037) |
| 13 | List-wise Reward Estimation for Offline Preference-Based Reinforcem... | [arXiv](https://arxiv.org/abs/2408.04190) |
| 14 | RIME: Robust Preference-based Reinforcement Learning with Noisy Pre... | [arXiv](https://arxiv.org/abs/2402.17257) |
| 15 | TRACER: Uncertainty-based Offline Variational Bayesian Reinforcemen... | [arXiv](https://arxiv.org/abs/2411.00465) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Reward-Directed Conditional Diffusion Provable Distribution Estimat... | [arXiv](https://arxiv.org/abs/2307.07055) |
| 2 | The Wisdom of Hindsight Makes Language Models Better Instruction Fo... | [arXiv](https://arxiv.org/abs/2302.05206) |
| 3 | Action Space Design in Reinforcement Learning for Robot Motor Skills | [Google Scholar](https://scholar.google.com/scholar?q=Action%20Space%20Design%20in%20Reinforcement%20Learning%20for%20Robot%20Motor%20Skills) |
| 4 | DreamerV3 Mastering Diverse Domains through World Models | [arXiv](https://arxiv.org/abs/2301.04104) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | Does Self-supervised Learning Really Improve Reinforcement Learning... | [arXiv](https://arxiv.org/abs/2206.05266) |
| 2 | MJPC Predictive Sampling Real-time Behaviour Synthesis with MuJoCo | [arXiv](https://arxiv.org/abs/2212.00541) |
| 3 | R3M A Universal Visual Representation for Robot Manipulation | [arXiv](https://arxiv.org/abs/2203.12601) |
| 4 | VRL3 A Data-Driven Framework for Visual Deep Reinforcement Learning | [arXiv](https://arxiv.org/abs/2202.10324) |

**2021**

| # | Title | Links |
|---|-------|-------|
| 1 | CARE: Multi-Task Reinforcement Learning with Context-based Represen... | [arXiv](https://arxiv.org/abs/2102.06177) |
| 2 | REDQ: Randomized Ensembled Double Q-Learning: Learning Fast Without... | [arXiv](https://arxiv.org/abs/2101.05982) |
| 3 | Reinforcement Learning with Prototypical Representations | [arXiv](https://arxiv.org/abs/2102.11271) |
| 4 | Coarse-to-Fine Q-attention Efficient Learning for Visual Robotic Ma... | [arXiv](https://arxiv.org/abs/2205.02714) |
| 5 | DrQ-v2 Mastering Visual Continuous Control Improved Data-Augmented ... | [arXiv](https://arxiv.org/abs/2107.09645) |
| 6 | IQL Offline Reinforcement Learning with Implicit Q-Learning | [arXiv](https://arxiv.org/abs/2110.06169) |
| 7 | RRL Resnet as representation for Reinforcement Learning | [arXiv](https://arxiv.org/abs/2107.03316) |

**2019**

| # | Title | Links |
|---|-------|-------|
| 1 | Self-Supervised Correspondence in Visuomotor Policy Learning | [arXiv](https://arxiv.org/abs/1909.06933) |

**2017**

| # | Title | Links |
|---|-------|-------|
| 1 | DDPGfD Leveraging Demonstrations for Deep Reinforcement Learning on... | [arXiv](https://arxiv.org/abs/1707.08817) |


<a id="simulation--world-models"></a>
## Simulation & World Models (16 篇)

<a id="simulation--world-models-simulation"></a>
### Simulation (10 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Scalable Real2Sim Physics-Aware Asset Generation Via Robotic Pick-a... | [arXiv](https://arxiv.org/abs/2503.00370) |
| 2 | Genesis A Generative and Universal Physics Engine for Robotics and ... | [Google Scholar](https://scholar.google.com/scholar?q=Genesis%20A%20Generative%20and%20Universal%20Physics%20Engine%20for%20Robotics%20and%20Beyond) |
| 3 | UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI | [arXiv](https://arxiv.org/abs/2412.20977) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | DrEureka Language Model Guided Sim-To-Real Transfer | [arXiv](https://arxiv.org/abs/2406.01967) |
| 2 | RoboCasa Large-Scale Simulation of Everyday Tasks for Generalist Ro... | [arXiv](https://arxiv.org/abs/2306.14426) |
| 3 | TRANSIC Sim-to-Real Policy Transfer by Learning from Online Correction | [arXiv](https://arxiv.org/abs/2404.13026) |
| 4 | GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoni... | [arXiv](https://arxiv.org/abs/2410.03645) |
| 5 | RoboGen: Towards Unleashing Infinite Data for Automated Robot Learn... | [arXiv](https://arxiv.org/abs/2311.01455) |
| 6 | GarmentLab: A Unified Simulation and Benchmark for Garment Manipula... | [arXiv](https://arxiv.org/abs/2411.01200) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | IndustReal Transferring Contact-Rich Assembly Tasks from Simulation... | [arXiv](https://arxiv.org/abs/2305.17110) |

<a id="simulation--world-models-world-models"></a>
### World Models (6 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Cosmos 3 Omnimodal World Models for Physical AI | [arXiv](https://arxiv.org/abs/2606.02800) |
| 2 | Strengthening Generative Robot Policies through Predictive World Mo... | [Google Scholar](https://scholar.google.com/scholar?q=Strengthening%20Generative%20Robot%20Policies%20through%20Predictive%20World%20Modeling) |
| 3 | The Matrix Infinite-Horizon World Generation with Real-Time Moving ... | [arXiv](https://arxiv.org/abs/2412.03568) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Generative World Explorer | [arXiv](https://arxiv.org/abs/2411.11844) |
| 2 | Pandora Towards General World Model with Natural Language Actions a... | [arXiv](https://arxiv.org/abs/2406.09455) |
| 3 | PIVOT-R: Waypoint-Aware World Model for Language-Guided Robotic Man... | [arXiv](https://arxiv.org/abs/2410.10394) |


<a id="navigation--tracking"></a>
## Navigation & Tracking (7 篇)

<a id="navigation--tracking-motion-tracking"></a>
### Motion Tracking (3 篇)

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Learning-based Trajectory Tracking for Bird-inspired Flapping-Wing ... | [arXiv](https://arxiv.org/abs/2411.15130) |
| 2 | Model-based Diffusion for Trajectory Optimization | [arXiv](https://arxiv.org/abs/2407.01573) |
| 3 | Motion Prompting Controlling Video Generation with Motion Trajectories | [Google Scholar](https://scholar.google.com/scholar?q=Motion%20Prompting%20Controlling%20Video%20Generation%20with%20Motion%20Trajectories) |

<a id="navigation--tracking-navigation"></a>
### Navigation (3 篇)

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Vid2Sim Realistic and Interactive Simulation from Video for Urban N... | [Google Scholar](https://scholar.google.com/scholar?q=Vid2Sim%20Realistic%20and%20Interactive%20Simulation%20from%20Video%20for%20Urban%20Navigation) |
| 2 | LeLaN: Learning A Language-Conditioned Navigation Policy from In-th... |  |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | High-speed control and navigation for quadrupedal robots on complex... | [Google Scholar](https://scholar.google.com/scholar?q=High-speed%20control%20and%20navigation%20for%20quadrupedal%20robots%20on%20complex%20and%20discrete%20terrain) |

<a id="navigation--tracking-teleoperation"></a>
### Teleoperation (1 篇)

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | Open-TeleVision Teleoperation with Immersive Active Visual Feedback | [arXiv](https://arxiv.org/abs/2407.01512) |


<a id="hardware--sensing"></a>
## Hardware & Sensing (11 篇)

<a id="hardware--sensing-hardware"></a>
### Hardware (6 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | Universal Manipulation Exoskeleton Learning Compliant Whole-body Po... | [arXiv](https://arxiv.org/abs/2606.14218) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Shape Your Body Value Gradients for Multi-Embodiment Robot Design | [Google Scholar](https://scholar.google.com/scholar?q=Shape%20Your%20Body%20Value%20Gradients%20for%20Multi-Embodiment%20Robot%20Design) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | ART-Glove Articulated Tactile Glove for Contact-Grounded Dexterous ... | [Google Scholar](https://scholar.google.com/scholar?q=ART-Glove%20Articulated%20Tactile%20Glove%20for%20Contact-Grounded%20Dexterous%20Interaction%20Capture) |
| 2 | DexWrist A Robotic Wrist for Constrained and Dynamic Manipulation | [Google Scholar](https://scholar.google.com/scholar?q=DexWrist%20A%20Robotic%20Wrist%20for%20Constrained%20and%20Dynamic%20Manipulation) |
| 3 | HATO Learning Visuotactile Skills with Two Multifingered Hands | [Google Scholar](https://scholar.google.com/scholar?q=HATO%20Learning%20Visuotactile%20Skills%20with%20Two%20Multifingered%20Hands) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Dynamic Pen Spinning Using a High-speed Multifingered Hand with Hig... | [Google Scholar](https://scholar.google.com/scholar?q=Dynamic%20Pen%20Spinning%20Using%20a%20High-speed%20Multifingered%20Hand%20with%20High-speed%20Tactile%20Sensor) |

<a id="hardware--sensing-tactile-sensing"></a>
### Tactile Sensing (5 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Feel the Force Contact-Driven Learning from Humans | [arXiv](https://arxiv.org/abs/2506.01944) |
| 2 | UniT Unified Tactile Representation for Robot Learning | [arXiv](https://arxiv.org/abs/2502.12191) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | AnySkin Plug-and-play Skin Sensing for Robotic Touch | [Google Scholar](https://scholar.google.com/scholar?q=AnySkin%20Plug-and-play%20Skin%20Sensing%20for%20Robotic%20Touch) |
| 2 | Intrinsic sense of touch for intuitive physical human-robot interac... | [Google Scholar](https://scholar.google.com/scholar?q=Intrinsic%20sense%20of%20touch%20for%20intuitive%20physical%20human-robot%20interaction) |
| 3 | RoboPack Learning Tactile-Informed Dynamics Models for Dense Packing | [Google Scholar](https://scholar.google.com/scholar?q=RoboPack%20Learning%20Tactile-Informed%20Dynamics%20Models%20for%20Dense%20Packing) |


<a id="data-generation"></a>
## Data Generation (12 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | VLK Learning Humanoid Loco-Manipulation from Synthetic Interactions... | [arXiv](https://arxiv.org/abs/2606.30645) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Physics IQ Benchmark Do generative video models learn physical prin... | [arXiv](https://arxiv.org/abs/2501.09038) |
| 2 | DiffuseLoco Real-Time Legged Locomotion Control with Diffusion from... | [Google Scholar](https://scholar.google.com/scholar?q=DiffuseLoco%20Real-Time%20Legged%20Locomotion%20Control%20with%20Diffusion%20from%20Offline%20Datasets) |
| 3 | HumanoidMimicGen Data Generation for Loco-Manipulation via Whole-Bo... | [Google Scholar](https://scholar.google.com/scholar?q=HumanoidMimicGen%20Data%20Generation%20for%20Loco-Manipulation%20via%20Whole-Body%20Planning%20and%20Adaptation) |
| 4 | IntervenGen Interventional Data Generation for Robust and Data-Effi... | [Google Scholar](https://scholar.google.com/scholar?q=IntervenGen%20Interventional%20Data%20Generation%20for%20Robust%20and%20Data-Efficient%20Robot%20Imitation%20Learning) |
| 5 | ManiBox Enhancing Spatial Grasping Generalization via Scalable Simu... | [Google Scholar](https://scholar.google.com/scholar?q=ManiBox%20Enhancing%20Spatial%20Grasping%20Generalization%20via%20Scalable%20Simulation%20Data%20Generation) |
| 6 | Robot Data Curation with Mutual Information Estimators | [Google Scholar](https://scholar.google.com/scholar?q=Robot%20Data%20Curation%20with%20Mutual%20Information%20Estimators) |
| 7 | VLABench A Large-Scale Benchmark for Language-Conditioned Robotics ... | [Google Scholar](https://scholar.google.com/scholar?q=VLABench%20A%20Large-Scale%20Benchmark%20for%20Language-Conditioned%20Robotics%20Manipulation%20with%20Long-Horizon%20Re) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | A Simulation Benchmark for Autonomous Racing with Large-Scale Human... | [Google Scholar](https://scholar.google.com/scholar?q=A%20Simulation%20Benchmark%20for%20Autonomous%20Racing%20with%20Large-Scale%20Human%20Data) |
| 2 | BiGym A Demo-Driven Mobile Bi-Manual Manipulation Benchmark | [Google Scholar](https://scholar.google.com/scholar?q=BiGym%20A%20Demo-Driven%20Mobile%20Bi-Manual%20Manipulation%20Benchmark) |
| 3 | DemoGen Synthetic Demonstration Generation for Data-Efficient Visuo... | [Google Scholar](https://scholar.google.com/scholar?q=DemoGen%20Synthetic%20Demonstration%20Generation%20for%20Data-Efficient%20Visuomotor%20Policy%20Learning) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | ARCTIC A Dataset for Dexterous Bimanual Hand-Object Manipulation | [Google Scholar](https://scholar.google.com/scholar?q=ARCTIC%20A%20Dataset%20for%20Dexterous%20Bimanual%20Hand-Object%20Manipulation) |


<a id="video-generation"></a>
## Video Generation (5 篇)

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | CAT4D Create Anything in 4D with Multi-View Video Diffusion Models | [Google Scholar](https://scholar.google.com/scholar?q=CAT4D%20Create%20Anything%20in%204D%20with%20Multi-View%20Video%20Diffusion%20Models) |
| 2 | Generative Image as Action Models | [Google Scholar](https://scholar.google.com/scholar?q=Generative%20Image%20as%20Action%20Models) |
| 3 | One-Minute Video Generation with Test-Time Training | [Google Scholar](https://scholar.google.com/scholar?q=One-Minute%20Video%20Generation%20with%20Test-Time%20Training) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Generative Image Dynamics | [arXiv](https://arxiv.org/abs/2309.07906) |

**2018**

| # | Title | Links |
|---|-------|-------|
| 1 | StyleGAN A Style-Based Generator Architecture for Generative Advers... | [arXiv](https://arxiv.org/abs/1812.04948) |


<a id="others"></a>
## Others (202 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | CaP-X A Framework for Benchmarking and Improving Codin | [arXiv](https://arxiv.org/abs/2603.22435) |
| 2 | DexJoCo A Benchmark and Toolkit for Task-Oriented Dext | [arXiv](https://arxiv.org/abs/2605.16257) | [Code](https://dexjoco.github.io) |
| 3 | Dexora Open-source VLA for High-DoF Bimanual Dexterity | [arXiv](https://arxiv.org/abs/2605.18722) |
| 4 | ENPIRE Agentic Robot Policy Self-Improvement in the Real World | [arXiv](https://arxiv.org/abs/2606.19980) |
| 5 | Generating Robot Hands from Human Demonstrations | [arXiv](https://arxiv.org/abs/2606.20549) |
| 6 | Generating Robot Hands from Human Demonstrations | [arXiv](https://arxiv.org/abs/2606.20549) |
| 7 | Human Universal Grasping | [arXiv](https://arxiv.org/abs/2606.17054) |
| 8 | ORCA Open-Source | [arXiv](https://arxiv.org/abs/2606.14561) |
| 9 | Text2CAD-Bench A Benchmark for LLM-based Text-to-Param | [arXiv](https://arxiv.org/abs/2605.18430) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Beyond Sight Finetuning Generalist Robot Policies with Heterogeneou... | [arXiv](https://arxiv.org/abs/2501.04693) |
| 2 | Fast-FoundationStereo Real-Time Zero-Shot Stereo Match | [arXiv](https://arxiv.org/abs/2512.11130) |
| 3 | Feel the Force Contact-Driven Learning from Humans | [arXiv](https://arxiv.org/abs/2506.01944) |
| 4 | Improving Vision-Language-Action Model with Online Reinforcement Le... | [arXiv](https://arxiv.org/abs/2501.16664) |
| 5 | Psychologically Enhanced AI Agents | [arXiv](https://arxiv.org/abs/2509.04343) |
| 6 | Psychologically Enhanced AI Agents | [arXiv](https://arxiv.org/abs/2509.04343) |
| 7 | Reinforcement Learning with Action Chunking | [arXiv](https://arxiv.org/abs/2507.07969) |
| 8 | Unified Video Action Model | [arXiv](https://arxiv.org/abs/2503.00200) |
| 9 | CASHER Robot Learning with Super-Linear Scaling | [Google Scholar](https://scholar.google.com/scholar?q=CASHER%20Robot%20Learning%20with%20Super-Linear%20Scaling) |
| 10 | DexterityGen Foundation Controller for Unprecedented Dexterity | [Google Scholar](https://scholar.google.com/scholar?q=DexterityGen%20Foundation%20Controller%20for%20Unprecedented%20Dexterity) |
| 11 | LocoMan Advancing Versatile Quadrupedal Dexterity with Lightweight ... | [Google Scholar](https://scholar.google.com/scholar?q=LocoMan%20Advancing%20Versatile%20Quadrupedal%20Dexterity%20with%20Lightweight%20Loco-Manipulators) |
| 12 | MonST3R A Simple Approach for Estimating Geometry in the Presence o... | [Google Scholar](https://scholar.google.com/scholar?q=MonST3R%20A%20Simple%20Approach%20for%20Estimating%20Geometry%20in%20the%20Presence%20of%20Motion) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | A Vision Check-up for Language Models | [arXiv](https://arxiv.org/abs/2401.01862) |
| 2 | Actor-Critic Model Predictive Control | [arXiv](https://arxiv.org/abs/2406.03995) |
| 3 | Bidirectional Decoding Improving Action Chunking via Closed-Loop Re... | [arXiv](https://arxiv.org/abs/2408.17355) |
| 4 | Blox-Net Generative Design-for-Robot-Assembly using VLM Supervision | [arXiv](https://arxiv.org/abs/2409.17126) |
| 5 | Complementarity-Free Multi-Contact Modeling and Optimi | [arXiv](https://arxiv.org/abs/2408.07855) |
| 6 | Consistency Policy Accelerated Visuomotor Policies via Consistency ... | [arXiv](https://arxiv.org/abs/2405.07503) |
| 7 | Dexterous Legged Locomotion in Confined 3D Spaces with Reinforcemen... | [arXiv](https://arxiv.org/abs/2403.03848) |
| 8 | Editable Image Elements for Controllable Synthesis | [arXiv](https://arxiv.org/abs/2404.16029) |
| 9 | Estimating Body and Hand Motion in an Ego-sensed World | [arXiv](https://arxiv.org/abs/2410.03665) |
| 10 | Generative Expressive Robot Behaviors using Large Language Models | [arXiv](https://arxiv.org/abs/2401.14673) |
| 11 | Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robot... | [arXiv](https://arxiv.org/abs/2403.03890) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 12 | Image Neural Field Diffusion Models | [arXiv](https://arxiv.org/abs/2406.07480) |
| 13 | Inference-Time Policy Steering through Human Interactions | [arXiv](https://arxiv.org/abs/2411.16627) |
| 14 | Learning Generalizable Feature Fields for Mobile Manipulation | [arXiv](https://arxiv.org/abs/2403.07563) |
| 15 | Learning to walk in confined spaces using 3D representation | [arXiv](https://arxiv.org/abs/2403.00187) |
| 16 | Leveraging Symmetry in RL-based Legged Locomotion Control | [arXiv](https://arxiv.org/abs/2403.17320) |
| 17 | Moving Off-the-Grid Scene-Grounded Video Representations | [arXiv](https://arxiv.org/abs/2411.05927) |
| 18 | Multimodal Visual-Tactile Representation Learning through Self-Supe... | [arXiv](https://arxiv.org/abs/2401.12024) |
| 19 | Natural Language Can Help Bridge the Sim2Real Gap | [arXiv](https://arxiv.org/abs/2405.10020) |
| 20 | Neural Gaussian Scale-Space Fields | [arXiv](https://arxiv.org/abs/2405.20980) |
| 21 | Offline Imitation Learning Through Graph Search and Retrieval | [arXiv](https://arxiv.org/abs/2407.15403) |
| 22 | On Pretraining Data Diversity for Self-Supervised Learning | [arXiv](https://arxiv.org/abs/2403.13808) |
| 23 | One Step Diffusion via Shortcut Models | [arXiv](https://arxiv.org/abs/2410.12557) |
| 24 | Policy-Guided Diffusion | [arXiv](https://arxiv.org/abs/2404.06356) |
| 25 | Probing the 3D Awareness of Visual Foundation Models | [arXiv](https://arxiv.org/abs/2404.08636) |
| 26 | Radiance Fields for Robotic Teleoperation | [arXiv](https://arxiv.org/abs/2407.20194) |
| 27 | Rethinking Few-shot 3D Point Cloud Semantic Segmentation | [arXiv](https://arxiv.org/abs/2403.00592) |
| 28 | SATO Stable Text-to-Motion Framework | [arXiv](https://arxiv.org/abs/2405.01461) |
| 29 | SPIN Simultaneous Perception | [arXiv](https://arxiv.org/abs/2405.07991) |
| 30 | ScrewMimic Bimanual Imitation from Human Videos with Screw Space Pr... | [arXiv](https://arxiv.org/abs/2405.03666) |
| 31 | So You Think You Can Scale Up Autonomous Robot Data Collection | [arXiv](https://arxiv.org/abs/2411.01813) |
| 32 | Soft Robotic Dynamic In-Hand Pen Spinning | [arXiv](https://arxiv.org/abs/2411.12734) |
| 33 | The Platonic Representation Hypothesis | [arXiv](https://arxiv.org/abs/2405.07987) |
| 34 | Transparent Image Layer Diffusion using Latent Transparency | [arXiv](https://arxiv.org/abs/2402.17113) |
| 35 | Visual Whole-Body Control for Legged Loco-Manipulation | [arXiv](https://arxiv.org/abs/2403.16967) |
| 36 | best manipulation paper, SARA-RT Scaling up Robotics Transformers w... | [arXiv](https://arxiv.org/abs/2312.01990) | [Code](https://robotics-transformer-x.github.io) |
| 37 | best paper, Goal Masked Diffusion Policies for Unified Navigation a... | [arXiv](https://arxiv.org/abs/2310.07896) | [Code](https://gmdp-navigation.github.io) |
| 38 | best paper, Open X-Embodiment Robotic Learning Datasets and RT-X | [arXiv](https://arxiv.org/abs/2310.08864) | [Code](https://github.com/google-deepmind/open_x_embodiment) |
| 39 | best paper, PoliFormer Scaling On-Policy RL with Transformers Resul... | [arXiv](https://arxiv.org/abs/2406.20083) | [Code](https://poliformer.github.io) |
| 40 | ALOHA Unleashed A Simple Recipe for Robot Dexterity | [Google Scholar](https://scholar.google.com/scholar?q=ALOHA%20Unleashed%20A%20Simple%20Recipe%20for%20Robot%20Dexterity) |
| 41 | AMAGO Scalable In-Context Reinforcement Learning for Adaptive Agents | [Google Scholar](https://scholar.google.com/scholar?q=AMAGO%20Scalable%20In-Context%20Reinforcement%20Learning%20for%20Adaptive%20Agents) |
| 42 | Awesome UMI | [Google Scholar](https://scholar.google.com/scholar?q=Awesome%20UMI) |
| 43 | BridgeData V2 A Dataset for Robot Learning at Scale | [arXiv](https://arxiv.org/abs/2308.12952) |
| 44 | Canonical Factors for Hybrid Neural Fields | [Google Scholar](https://scholar.google.com/scholar?q=Canonical%20Factors%20for%20Hybrid%20Neural%20Fields) |
| 45 | CyberDemo Augmenting Simulated Human Demonstration for Real-World D... | [arXiv](https://arxiv.org/abs/2402.14795) |
| 46 | DAE Deconstructing Denoising Diffusion Models for Self-Supervised L... | [arXiv](https://arxiv.org/abs/2306.13196) |
| 47 | DexCap Scalable and Portable Mocap Data Collection System for Dexte... | [Google Scholar](https://scholar.google.com/scholar?q=DexCap%20Scalable%20and%20Portable%20Mocap%20Data%20Collection%20System%20for%20Dexterous%20Manipulation) |
| 48 | DexPBT Scaling up Dexterous Manipulation for Hand-Arm Systems with ... | [arXiv](https://arxiv.org/abs/2408.11812) |
| 49 | DiffusionGPT LLM-Driven Text-to-Image Generation System | [arXiv](https://arxiv.org/abs/2401.01234) |
| 50 | EgoPet Egomotion and Interaction Data from an Animal's Perspective | [Google Scholar](https://scholar.google.com/scholar?q=EgoPet%20Egomotion%20and%20Interaction%20Data%20from%20an%20Animal%27s%20Perspective) |
| 51 | FAST Efficient Robot Action Tokenization | [Google Scholar](https://scholar.google.com/scholar?q=FAST%20Efficient%20Robot%20Action%20Tokenization) |
| 52 | FeatUp A Model-Agnostic Framework for Features at Any Resolution | [arXiv](https://arxiv.org/abs/2202.10324) |
| 53 | For SALE State-Action Representation Learning for Deep Reinforcemen... | [arXiv](https://arxiv.org/abs/2205.02714) |
| 54 | GameNGen Diffusion Models Are Real-Time Game Engines | [arXiv](https://arxiv.org/abs/2408.14837) |
| 55 | Is ImageNet worth 1 video Learning strong image encoders from 1 lon... | [Google Scholar](https://scholar.google.com/scholar?q=Is%20ImageNet%20worth%201%20video%20Learning%20strong%20image%20encoders%20from%201%20long%20unlabelled%20video) |
| 56 | LEGENT Open Platform for Embodied Agents | [Google Scholar](https://scholar.google.com/scholar?q=LEGENT%20Open%20Platform%20for%20Embodied%20Agents) |
| 57 | Learning to Play Piano in the Real World | [arXiv](https://arxiv.org/abs/2304.01182) |
| 58 | ManiGaussian Dynamic Gaussian Splatting for Multi-task Robotic Mani... | [arXiv](https://arxiv.org/abs/2410.18912) |
| 59 | Neural MP A Generalist Neural Motion Planner | [Google Scholar](https://scholar.google.com/scholar?q=Neural%20MP%20A%20Generalist%20Neural%20Motion%20Planner) |
| 60 | OPEN TEACH A Versatile Teleoperation System for Robotic Manipulation | [Google Scholar](https://scholar.google.com/scholar?q=OPEN%20TEACH%20A%20Versatile%20Teleoperation%20System%20for%20Robotic%20Manipulation) |
| 61 | PIE-NeRF Physics-based Interactive Elastodynamics with NeRF | [Google Scholar](https://scholar.google.com/scholar?q=PIE-NeRF%20Physics-based%20Interactive%20Elastodynamics%20with%20NeRF) |
| 62 | PaperBot Learning to Design Real-World Tools Using Paper | [Google Scholar](https://scholar.google.com/scholar?q=PaperBot%20Learning%20to%20Design%20Real-World%20Tools%20Using%20Paper) |
| 63 | Pedipulate Enabling Manipulation Skills using a Quadruped Robot's Leg | [Google Scholar](https://scholar.google.com/scholar?q=Pedipulate%20Enabling%20Manipulation%20Skills%20using%20a%20Quadruped%20Robot%27s%20Leg) |
| 64 | Point Could Mamba Point Cloud Learning via State Space Model | [Google Scholar](https://scholar.google.com/scholar?q=Point%20Could%20Mamba%20Point%20Cloud%20Learning%20via%20State%20Space%20Model) |
| 65 | REFLECT Summarizing Robot Experiences for FaiLure Explanation and C... | [Google Scholar](https://scholar.google.com/scholar?q=REFLECT%20Summarizing%20Robot%20Experiences%20for%20FaiLure%20Explanation%20and%20CorrecTion) |
| 66 | RLIF Interactive Imitation Learning as Reinforcement Learning | [Google Scholar](https://scholar.google.com/scholar?q=RLIF%20Interactive%20Imitation%20Learning%20as%20Reinforcement%20Learning) |
| 67 | Reconstructing Hand-Held Objects in 3D | [Google Scholar](https://scholar.google.com/scholar?q=Reconstructing%20Hand-Held%20Objects%20in%203D) |
| 68 | RoboDuet A Framework Affording Mobile-Manipulation and Cross-Embodi... | [Google Scholar](https://scholar.google.com/scholar?q=RoboDuet%20A%20Framework%20Affording%20Mobile-Manipulation%20and%20Cross-Embodiment) |
| 69 | Robot Utility Models General Policies for Zero-Shot Deployment in N... | [Google Scholar](https://scholar.google.com/scholar?q=Robot%20Utility%20Models%20General%20Policies%20for%20Zero-Shot%20Deployment%20in%20New%20Environments) |
| 70 | Seal Segment Any Point Cloud Sequences by Distilling Vision Foundat... | [Google Scholar](https://scholar.google.com/scholar?q=Seal%20Segment%20Any%20Point%20Cloud%20Sequences%20by%20Distilling%20Vision%20Foundation%20Models) |
| 71 | See to Touch Learning Tactile Dexterity through Visual Incentives | [Google Scholar](https://scholar.google.com/scholar?q=See%20to%20Touch%20Learning%20Tactile%20Dexterity%20through%20Visual%20Incentives) |
| 72 | SkillMimic Learning Reusable Basketball Skills from Demonstrations | [Google Scholar](https://scholar.google.com/scholar?q=SkillMimic%20Learning%20Reusable%20Basketball%20Skills%20from%20Demonstrations) |
| 73 | Sparse Diffusion Policy A Sparse, Reusable, and Flexible Policy for... | [arXiv](https://arxiv.org/abs/2307.01531) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 74 | TeleMoMa A Modular and Versatile Teleoperation System for Mobile Ma... | [Google Scholar](https://scholar.google.com/scholar?q=TeleMoMa%20A%20Modular%20and%20Versatile%20Teleoperation%20System%20for%20Mobile%20Manipulation) |
| 75 | UnSAM Segment Anything without Supervision | [Google Scholar](https://scholar.google.com/scholar?q=UnSAM%20Segment%20Anything%20without%20Supervision) |
| 76 | VISTA View-Invariant Policy Learning via Zero-Shot Novel View Synth... | [Google Scholar](https://scholar.google.com/scholar?q=VISTA%20View-Invariant%20Policy%20Learning%20via%20Zero-Shot%20Novel%20View%20Synthesis) |
| 77 | Vid2Robot End-to-end Video-conditioned Policy Learning with Cross-A... | [Google Scholar](https://scholar.google.com/scholar?q=Vid2Robot%20End-to-end%20Video-conditioned%20Policy%20Learning%20with%20Cross-Attention%20Transformers) |
| 78 | Vila On pretraining for visual language models | [Google Scholar](https://scholar.google.com/scholar?q=Vila%20On%20pretraining%20for%20visual%20language%20models) |
| 79 | Yell At Your Robot Improving On-the-Fly from Language Corrections | [Google Scholar](https://scholar.google.com/scholar?q=Yell%20At%20Your%20Robot%20Improving%20On-the-Fly%20from%20Language%20Corrections) |
| 80 | Source Code Repository |  |
| 81 | Awesome Robot Learning Resources | [Google Scholar](https://scholar.google.com/scholar?q=website%20%20github) |
| 82 | π0 A Vision-Language-Action Flow Model for General Robot Control | [arXiv](https://arxiv.org/abs/2410.24164) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | Consistency Models as a Rich and Efficient Policy Class for Reinfor... | [arXiv](https://arxiv.org/abs/2309.16984) |
| 2 | Cumulative Reasoning with Large Language Models | [arXiv](https://arxiv.org/abs/2308.04371) |
| 3 | Data-Free Learning of Reduced-Order Kinematics | [arXiv](https://arxiv.org/abs/2305.03846) |
| 4 | Detector-Free Structure from Motion | [arXiv](https://arxiv.org/abs/2306.15669) |
| 5 | Diffusion Models Beat GANs on Image Classification | [arXiv](https://arxiv.org/abs/2307.08702) |
| 6 | Explaining the Decisions of Deep Policy Networks for Robotic Manipu... | [arXiv](https://arxiv.org/abs/2310.19432) |
| 7 | For Pre-Trained Vision Models in Motor Control, Not All Policy Lear... | [Google Scholar](https://scholar.google.com/scholar?q=For%20Pre-Trained%20Vision%20Models%20in%20Motor%20Control%2C%20Not%20All%20Policy%20Learning%20Methods%20are%20Created%20Equal) |
| 8 | Frozen Transformers in Language Models are Effective Visual Encoder... | [Google Scholar](https://scholar.google.com/scholar?q=Frozen%20Transformers%20in%20Language%20Models%20are%20Effective%20Visual%20Encoder%20Layers) |
| 9 | Human-Assisted Continual Robot Learning with Foundation Models | [arXiv](https://arxiv.org/abs/2309.14321) |
| 10 | Imitation Bootstrapped Reinforcement Learning | [arXiv](https://arxiv.org/abs/2311.02198) |
| 11 | Improved Techniques for Training Consistency Models | [arXiv](https://arxiv.org/abs/2310.14189) |
| 12 | Improving Long-Horizon Imitation Through Instruction Prediction | [arXiv](https://arxiv.org/abs/2306.12554) |
| 13 | Initializing Models with Larger Ones | [arXiv](https://arxiv.org/abs/2311.18823) |
| 14 | L4DC 2023, Agile Catching with Whole-Body MPC and Blackbox Policy L... | [arXiv](https://arxiv.org/abs/2306.08205) |
| 15 | Learning Vision from Models Rivals Learning Vision from Data | [arXiv](https://arxiv.org/abs/2312.17742) |
| 16 | Learning from One Continuous Video Stream | [arXiv](https://arxiv.org/abs/2312.00598) |
| 17 | Learning to (Learn at Test Time | [arXiv](https://arxiv.org/abs/2407.04620) |
| 18 | Learning to Model the World with Language | [arXiv](https://arxiv.org/abs/2308.01399) |
| 19 | Learning to Walk and Fly with Adversarial Motion Priors | [arXiv](https://arxiv.org/abs/2309.12784) |
| 20 | MPPI Model Predictive Path Integral Control using Covariance Variab... | [arXiv](https://arxiv.org/abs/2309.13201) |
| 21 | Mastering Robot Manipulation with Multimodal Prompts through Pretra... | [arXiv](https://arxiv.org/abs/2210.03094) |
| 22 | Mosaic-SDF for 3D Generative Models | [arXiv](https://arxiv.org/abs/2312.09222) |
| 23 | Ponymation Learning 3D Animal Motions from Unlabeled Online Videos | [arXiv](https://arxiv.org/abs/2312.13604) |
| 24 | Robot Learning with Sensorimotor Pre-training | [arXiv](https://arxiv.org/abs/2306.10007) |
| 25 | Robotic Offline RL from Internet Videos via Value-Function Pre-Trai... | [arXiv](https://arxiv.org/abs/2309.13041) |
| 26 | SPRING GPT-4 Out-performs RL Algorithms by Studying Papers and Reas... | [arXiv](https://arxiv.org/abs/2305.15486) |
| 27 | Sampling-based Model Predictive Control Leveraging Parallelizable P... | [arXiv](https://arxiv.org/abs/2307.09105) |
| 28 | Scaling Laws of Synthetic Images for Model Training ... for Now | [arXiv](https://arxiv.org/abs/2312.04567) |
| 29 | The dormant neuron phenomenon in deep reinforcement learning | [arXiv](https://arxiv.org/abs/2302.12902) |
| 30 | Towards Stable Test-Time Adaptation in Dynamic Wild World | [arXiv](https://arxiv.org/abs/2302.12400) |
| 31 | Video Prediction Models as Rewards for Reinforcement Learning | [arXiv](https://arxiv.org/abs/2305.14343) |
| 32 | Visual Point Cloud Forecasting enables Scalable Autonomous Driving | [arXiv](https://arxiv.org/abs/2312.17655) |
| 33 | Non-parametric regression for robot learning on manifolds | [arXiv](https://arxiv.org/abs/2310.19561) |
| 34 | An Image is Worth More Than 16x16 Patches Exploring Transformers on... | [arXiv](https://arxiv.org/abs/2303.02106) |
| 35 | Customizing Text-to-Image Models with a Single Image Pair | [Google Scholar](https://scholar.google.com/scholar?q=Customizing%20Text-to-Image%20Models%20with%20a%20Single%20Image%20Pair) |
| 36 | DDAE Denoising Diffusion Autoencoders are Unified Self-supervised L... | [Google Scholar](https://scholar.google.com/scholar?q=DDAE%20Denoising%20Diffusion%20Autoencoders%20are%20Unified%20Self-supervised%20Learners) |
| 37 | Deep Learning on 3D Neural Fields | [Google Scholar](https://scholar.google.com/scholar?q=Deep%20Learning%20on%203D%20Neural%20Fields) |
| 38 | DiffiT Diffusion Vision Transformers for Image Generation | [arXiv](https://arxiv.org/abs/2312.02139) |
| 39 | Dr2Net Dynamic Reversible Dual-Residual Networks for Memory-Efficie... | [Google Scholar](https://scholar.google.com/scholar?q=Dr2Net%20Dynamic%20Reversible%20Dual-Residual%20Networks%20for%20Memory-Efficient%20Finetuning) |
| 40 | DreamSim Learning New Dimensions of Human Visual Similarity using S... | [arXiv](https://arxiv.org/abs/2306.09344) |
| 41 | DreamTeacher Pretraining Image Backbones with Deep Generative Models | [Google Scholar](https://scholar.google.com/scholar?q=DreamTeacher%20Pretraining%20Image%20Backbones%20with%20Deep%20Generative%20Models) |
| 42 | Foundation Models for Decision Making Problems, Methods, and Opport... | [arXiv](https://arxiv.org/abs/2303.04129) |
| 43 | Foundation Reinforcement Learning towards Embodied Generalist Agent... | [Google Scholar](https://scholar.google.com/scholar?q=Foundation%20Reinforcement%20Learning%20towards%20Embodied%20Generalist%20Agents%20with%20Foundation%20Prior%20Assistanc) |
| 44 | From Word Models to World Models Translating from Natural Language ... | [arXiv](https://arxiv.org/abs/2606.02800) |
| 45 | GELLO A General, Low-Cost, and Intuitive Teleoperation Framework fo... | [arXiv](https://arxiv.org/abs/2309.13037) |
| 46 | Gen2Sim Scaling up Robot Learning in Simulation with Generative Models | [Google Scholar](https://scholar.google.com/scholar?q=Gen2Sim%20Scaling%20up%20Robot%20Learning%20in%20Simulation%20with%20Generative%20Models) |
| 47 | Generative Agents Interactive Simulacra of Human Behavior | [arXiv](https://arxiv.org/abs/2304.03442) |
| 48 | Generative Omnimatte Learning to Decompose Video into Layers | [Google Scholar](https://scholar.google.com/scholar?q=Generative%20Omnimatte%20Learning%20to%20Decompose%20Video%20into%20Layers) |
| 49 | Grounding DINO Marrying DINO with Grounded Pre-Training for Open-Se... | [arXiv](https://arxiv.org/abs/2303.05499) |
| 50 | Images that Sound Composing Images and Sounds on a Single Canvas | [Google Scholar](https://scholar.google.com/scholar?q=Images%20that%20Sound%20Composing%20Images%20and%20Sounds%20on%20a%20Single%20Canvas) |
| 51 | KITE Keypoint-Conditioned Policies for Semantic Manipulation | [Google Scholar](https://scholar.google.com/scholar?q=KITE%20Keypoint-Conditioned%20Policies%20for%20Semantic%20Manipulation) |
| 52 | LAMP Language Reward Modulation for Pretraining Reinforcement Learning | [Google Scholar](https://scholar.google.com/scholar?q=LAMP%20Language%20Reward%20Modulation%20for%20Pretraining%20Reinforcement%20Learning) |
| 53 | LLaMA Open and Efficient Foundation Language Models | [arXiv](https://arxiv.org/abs/2302.13971) |
| 54 | Latent Graph Diffusion A Unified Framework for Generation and Predi... | [arXiv](https://arxiv.org/abs/2302.08368) |
| 55 | Lessons from Learning to Spin Pens | [Google Scholar](https://scholar.google.com/scholar?q=Lessons%20from%20Learning%20to%20Spin%20Pens) |
| 56 | Mamba Linear-Time Sequence Modeling with Selective State Spaces | [arXiv](https://arxiv.org/abs/2312.00752) |
| 57 | PLEX Making the Most of the Available Data for Robotic Manipulation... | [arXiv](https://arxiv.org/abs/2303.08782) |
| 58 | PointOdyssey A Large-Scale Synthetic Dataset for Long-Term Point Tr... | [Google Scholar](https://scholar.google.com/scholar?q=PointOdyssey%20A%20Large-Scale%20Synthetic%20Dataset%20for%20Long-Term%20Point%20Tracking) |
| 59 | Retentive Network A Successor to Transformer for Large Language Models | [arXiv](https://arxiv.org/abs/2307.08621) |
| 60 | SAPG Split and Aggregate Policy Gradients | [Google Scholar](https://scholar.google.com/scholar?q=SAPG%20Split%20and%20Aggregate%20Policy%20Gradients) |
| 61 | SEEM Segment Everything Everywhere All at Once  code | [arXiv](https://arxiv.org/abs/2304.06718) |
| 62 | SoM Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding ... | [arXiv](https://arxiv.org/abs/2310.11441) |
| 63 | TD-MPC2 Scalable, Robust World Models for Continuous Control | [arXiv](https://arxiv.org/abs/2310.16828) |
| 64 | Text-to-Vector Generation with Neural Path Representation | [Google Scholar](https://scholar.google.com/scholar?q=Text-to-Vector%20Generation%20with%20Neural%20Path%20Representation) |
| 65 | Text2Reward Automated Dense Reward Function Generation for Reinforc... | [arXiv](https://arxiv.org/abs/2309.11489) |
| 66 | True Self-Supervised Novel View Synthesis is Transferable | [Google Scholar](https://scholar.google.com/scholar?q=True%20Self-Supervised%20Novel%20View%20Synthesis%20is%20Transferable) |
| 67 | VQ-BeT Behavior Generation with Latent Actions | [Google Scholar](https://scholar.google.com/scholar?q=VQ-BeT%20Behavior%20Generation%20with%20Latent%20Actions) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | In-Hand Object Rotation via Rapid Motor Adaptation | [arXiv](https://arxiv.org/abs/2210.04887) |
| 2 | On the power of foundation models | [arXiv](https://arxiv.org/abs/2211.16327) |
| 3 | Simplicial Embeddings in Self-Supervised Learning and Downstream Cl... | [arXiv](https://arxiv.org/abs/2204.00616) |
| 4 | The primacy bias in deep reinforcement learning | [arXiv](https://arxiv.org/abs/2205.07802) |
| 5 | Training Compute-Optimal Large Language Models | [arXiv](https://arxiv.org/abs/2203.15556) |
| 6 | Visual Prompting via Image Inpainting | [arXiv](https://arxiv.org/abs/2209.00647) |
| 7 | best paper, Iterative Residual Policy for Goal-Conditioned Dynamic ... | [arXiv](https://arxiv.org/abs/2203.00663) |
| 8 | best student paper, AK Attentive Kernel for Information Gathering | [arXiv](https://arxiv.org/abs/2205.06426) |
| 9 | best system paper, Autonomously Untangling Long Cables | [arXiv](https://arxiv.org/abs/2207.07813) |
| 10 | CoT Chain-of-Thought Prompting Elicits Reasoning in Large Language ... | [arXiv](https://arxiv.org/abs/2201.11903) |
| 11 | FlashAttention Fast and Memory-Efficient Exact Attention with IO-Aw... | [arXiv](https://arxiv.org/abs/2205.14135) |
| 12 | PartSLIP Low-Shot Part Segmentation for 3D Point Clouds via Pretrai... | [Google Scholar](https://scholar.google.com/scholar?q=PartSLIP%20Low-Shot%20Part%20Segmentation%20for%203D%20Point%20Clouds%20via%20Pretrained%20Image-Language%20Models) |
| 13 | RoboTAP Tracking Arbitrary Points for Few-Shot Visual Imitation | [Google Scholar](https://scholar.google.com/scholar?q=RoboTAP%20Tracking%20Arbitrary%20Points%20for%20Few-Shot%20Visual%20Imitation) |
| 14 | Data-driven Feature Tracking for Event Cameras | [arXiv](https://arxiv.org/abs/2302.01234) |
| 15 | On Distillation of Guided Diffusion Models | [Google Scholar](https://scholar.google.com/scholar?q=candidate%2C%20On%20Distillation%20of%20Guided%20Diffusion%20Models) |

**2021**

| # | Title | Links |
|---|-------|-------|
| 1 | DPT Vision Transformers for Dense Prediction | [arXiv](https://arxiv.org/abs/2103.13413) |
| 2 | DroQ Dropout Q-Functions for Doubly Efficient Reinforcement Learning | [arXiv](https://arxiv.org/abs/2110.02034) |
| 3 | GIGA Synergies Between Affordance and Geometry 6-DoF Grasp Detectio... | [Google Scholar](https://scholar.google.com/scholar?q=GIGA%20Synergies%20Between%20Affordance%20and%20Geometry%206-DoF%20Grasp%20Detection%20via%20Implicit%20Representations) |
| 4 | RvS What is Essential for Offline RL via Supervised Learning | [Google Scholar](https://scholar.google.com/scholar?q=RvS%20What%20is%20Essential%20for%20Offline%20RL%20via%20Supervised%20Learning) |
| 5 | S4 Efficiently Modeling Long Sequences with Structured State Spaces | [arXiv](https://arxiv.org/abs/2111.00396) |
| 6 | StARformer Transformer with State-Action-Reward Representations for... | [Google Scholar](https://scholar.google.com/scholar?q=StARformer%20Transformer%20with%20State-Action-Reward%20Representations%20for%20Visual%20Reinforcement%20Learning) |
| 7 | paper, Deep Reinforcement Learning at the Edge of the Statistical P... | [arXiv](https://arxiv.org/abs/2108.13264) |

**2020**

| # | Title | Links |
|---|-------|-------|
| 1 | RCG Self-conditioned Image Generation via Generating Representations | [arXiv](https://arxiv.org/abs/2006.10728) |
| 2 | Scaling Laws for Neural Language Models | [arXiv](https://arxiv.org/abs/2001.08361) |
| 3 | Stochastic Solutions for Linear Inverse Problems using the Prior Im... | [arXiv](https://arxiv.org/abs/2006.09011) |

**2019**

| # | Title | Links |
|---|-------|-------|
| 1 | Neural-Guided RANSAC Learning Where to Sample Model Hypotheses | [Google Scholar](https://scholar.google.com/scholar?q=Neural-Guided%20RANSAC%20Learning%20Where%20to%20Sample%20Model%20Hypotheses) |
| 2 | T5 Exploring the Limits of Transfer Learning with a Unified Text-to... | [arXiv](https://arxiv.org/abs/1910.10683) |

**2018**

| # | Title | Links |
|---|-------|-------|
| 1 | Geometric Fabrics Generalizing Classical Mechanics to Capture the P... | [Google Scholar](https://scholar.google.com/scholar?q=Geometric%20Fabrics%20Generalizing%20Classical%20Mechanics%20to%20Capture%20the%20Physics%20of%20Behavior) |

**2017**

| # | Title | Links |
|---|-------|-------|
| 1 | Asymmetric Actor Critic for Image-Based Robot Learning | [arXiv](https://arxiv.org/abs/1710.06542) |
| 2 | Third-Person Imitation Learning | [arXiv](https://arxiv.org/abs/1703.01703) |
| 3 | FiLM Visual Reasoning with a General Conditioning Layer | [arXiv](https://arxiv.org/abs/1709.07871) |
| 4 | Network Dissection Quantifying Interpretability of Deep Visual Repr... | [arXiv](https://arxiv.org/abs/1704.05796) |


<a id="uncategorized"></a>
## Uncategorized (435 篇)

**2026**

| # | Title | Links |
|---|-------|-------|
| 1 | ART-Glove: Articulated Tactile Glove for Contact-Grounded Dexterous... | [arXiv](https://arxiv.org/abs/2606.16370) |
| 2 | CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous... | [arXiv](https://arxiv.org/abs/2606.23680) |
| 3 | Cosmos 3: Omnimodal World Models for Physical AI | [arXiv](https://arxiv.org/abs/2606.02800) |
| 4 | Do as I Do: Dexterous Manipulation Data from Everyday Human Videos | [arXiv](https://arxiv.org/abs/2606.19333) |
| 5 | MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation | [arXiv](https://arxiv.org/abs/2606.06139) |
| 6 | OmniContact: Chaining Meta-Skills via Contact Flow for Generalizabl... | [arXiv](https://arxiv.org/abs/2606.26201) |
| 7 | VLK: Learning Humanoid Loco-Manipulation from Synthetic Interaction... | [arXiv](https://arxiv.org/abs/2606.30645) |
| 8 | Value Bonuses using Ensemble Errors for Exploration in Reinforcemen... | [arXiv](https://arxiv.org/abs/2602.12375) |
| 9 | WARP: Whole-Body Retargeting for Learning from Offline Human Demons... | [arXiv](https://arxiv.org/abs/2606.29940) |

**2025**

| # | Title | Links |
|---|-------|-------|
| 1 | Discrete-Time Hybrid Automata Learning: Legged Locomotion Meets Ska... | [arXiv](https://arxiv.org/abs/2503.01842) |
| 2 | GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Mo... | [arXiv](https://arxiv.org/abs/2501.01428) |
| 3 | Improving Vision-Language-Action Model with Online Reinforcement Le... | [arXiv](https://arxiv.org/abs/2501.16664) |
| 4 | InterMimic: Towards Universal Whole-Body Control for Physics-Based ... | [arXiv](https://arxiv.org/abs/2502.20390) |
| 5 | RigAnything: Template-Free Autoregressive Rigging for Diverse 3D As... | [arXiv](https://arxiv.org/abs/2502.09615) |
| 6 | Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models | [arXiv](https://arxiv.org/abs/2504.11054) |

**2024**

| # | Title | Links |
|---|-------|-------|
| 1 | $π_0$: A Vision-Language-Action Flow Model for General Robot Control | [arXiv](https://arxiv.org/abs/2410.24164) |
| 2 | A Decade's Battle on Dataset Bias: Are We There Yet? | [arXiv](https://arxiv.org/abs/2403.08632) |
| 3 | A Vision Check-up for Language Models | [arXiv](https://arxiv.org/abs/2401.01862) |
| 4 | An Image is Worth More Than 16x16 Patches: Exploring Transformers o... | [arXiv](https://arxiv.org/abs/2406.09415) |
| 5 | AnySkin: Plug-and-play Skin Sensing for Robotic Touch | [arXiv](https://arxiv.org/abs/2409.08276) |
| 6 | Articulate-Anything: Automatic Modeling of Articulated Objects via ... | [arXiv](https://arxiv.org/abs/2410.13882) |
| 7 | BAKU: An Efficient Transformer for Multi-Task Policy Learning | [arXiv](https://arxiv.org/abs/2406.07539) |
| 8 | BUMBLE: Unifying Reasoning and Acting with Vision-Language Models f... | [arXiv](https://arxiv.org/abs/2410.06237) |
| 9 | Behavior Generation with Latent Actions | [arXiv](https://arxiv.org/abs/2403.03181) |
| 10 | Bidirectional Decoding: Improving Action Chunking via Guided Test-T... | [arXiv](https://arxiv.org/abs/2408.17355) |
| 11 | Blox-Net: Generative Design-for-Robot-Assembly Using VLM Supervisio... | [arXiv](https://arxiv.org/abs/2409.17126) |
| 12 | Body Transformer: Leveraging Robot Embodiment for Policy Learning | [arXiv](https://arxiv.org/abs/2408.06316) |
| 13 | CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models | [arXiv](https://arxiv.org/abs/2411.18613) |
| 14 | Can Transformers Capture Spatial Relations between Objects? | [arXiv](https://arxiv.org/abs/2403.00729) |
| 15 | ClearDepth: Enhanced Stereo Perception of Transparent Objects for R... | [arXiv](https://arxiv.org/abs/2409.08926) |
| 16 | Clio: Real-time Task-Driven Open-Set 3D Scene Graphs | [arXiv](https://arxiv.org/abs/2404.13696) |
| 17 | CoFie: Learning Compact Neural Surface Representations with Coordin... | [arXiv](https://arxiv.org/abs/2406.03417) |
| 18 | Continuous Control with Coarse-to-fine Reinforcement Learning | [arXiv](https://arxiv.org/abs/2407.07787) |
| 19 | Controlling diverse robots by inferring Jacobian fields with deep n... | [arXiv](https://arxiv.org/abs/2407.08722) |
| 20 | CyberDemo: Augmenting Simulated Human Demonstration for Real-World ... | [arXiv](https://arxiv.org/abs/2402.14795) |
| 21 | DELTA: Dense Efficient Long-range 3D Tracking for any video | [arXiv](https://arxiv.org/abs/2410.24211) |
| 22 | Deconstructing Denoising Diffusion Models for Self-Supervised Learning | [arXiv](https://arxiv.org/abs/2401.14404) |
| 23 | DexCap: Scalable and Portable Mocap Data Collection System for Dext... | [arXiv](https://arxiv.org/abs/2403.07788) |
| 24 | Dexterous Legged Locomotion in Confined 3D Spaces with Reinforcemen... | [arXiv](https://arxiv.org/abs/2403.03848) |
| 25 | DextrAH-RGB: Visuomotor Policies to Grasp Anything with Dexterous H... | [arXiv](https://arxiv.org/abs/2412.01791) |
| 26 | DiffuseLoco: Real-Time Legged Locomotion Control with Diffusion fro... | [arXiv](https://arxiv.org/abs/2404.19264) |
| 27 | DiffusionAgent: Navigating Expert Models for Agentic Image Generation | [arXiv](https://arxiv.org/abs/2401.10061) |
| 28 | DigiRL: Training In-The-Wild Device-Control Agents with Autonomous ... | [arXiv](https://arxiv.org/abs/2406.11896) |
| 29 | Dr$^2$Net: Dynamic Reversible Dual-Residual Networks for Memory-Eff... | [arXiv](https://arxiv.org/abs/2401.04105) |
| 30 | DrEureka: Language Model Guided Sim-To-Real Transfer | [arXiv](https://arxiv.org/abs/2406.01967) |
| 31 | Dreamitate: Real-World Visuomotor Policy Learning via Video Generation | [arXiv](https://arxiv.org/abs/2406.16862) |
| 32 | Editable Image Elements for Controllable Synthesis | [arXiv](https://arxiv.org/abs/2404.16029) |
| 33 | EgoPet: Egomotion and Interaction Data from an Animal's Perspective | [arXiv](https://arxiv.org/abs/2404.09991) |
| 34 | EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and ... | [arXiv](https://arxiv.org/abs/2407.01479) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 35 | Estimating Body and Hand Motion in an Ego-sensed World | [arXiv](https://arxiv.org/abs/2410.03665) |
| 36 | Evaluating Real-World Robot Manipulation Policies in Simulation | [arXiv](https://arxiv.org/abs/2405.05941) |
| 37 | EyeSight Hand: Design of a Fully-Actuated Dexterous Robot Hand with... | [arXiv](https://arxiv.org/abs/2408.06265) |
| 38 | FeatUp: A Model-Agnostic Framework for Features at Any Resolution | [arXiv](https://arxiv.org/abs/2403.10516) |
| 39 | Finding Visual Task Vectors | [arXiv](https://arxiv.org/abs/2404.05729) |
| 40 | Flow as the Cross-Domain Manipulation Interface | [arXiv](https://arxiv.org/abs/2407.15208) |
| 41 | From Imitation to Refinement -- Residual RL for Precise Assembly | [arXiv](https://arxiv.org/abs/2407.16677) |
| 42 | Full-Order Sampling-Based MPC for Torque-Level Locomotion Control v... | [arXiv](https://arxiv.org/abs/2409.15610) |
| 43 | Fusing uncalibrated IMUs and handheld smartphone video to reconstru... | [arXiv](https://arxiv.org/abs/2405.17368) |
| 44 | Gamba: Marry Gaussian Splatting with Mamba for single view 3D recon... | [arXiv](https://arxiv.org/abs/2403.18795) |
| 45 | GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary... | [arXiv](https://arxiv.org/abs/2403.09637) |
| 46 | Generative Expressive Robot Behaviors using Large Language Models | [arXiv](https://arxiv.org/abs/2401.14673) |
| 47 | Generative Omnimatte: Learning to Decompose Video into Layers | [arXiv](https://arxiv.org/abs/2411.16683) |
| 48 | Generative World Explorer | [arXiv](https://arxiv.org/abs/2411.11844) |
| 49 | Genie: Generative Interactive Environments | [arXiv](https://arxiv.org/abs/2402.15391) |
| 50 | Hand-Object Interaction Pretraining from Videos | [arXiv](https://arxiv.org/abs/2409.08273) |
| 51 | HandsOnVLM: Vision-Language Models for Hand-Object Interaction Pred... | [arXiv](https://arxiv.org/abs/2412.13187) |
| 52 | Helpful DoggyBot: Open-World Object Fetching using Legged Robots an... | [arXiv](https://arxiv.org/abs/2410.00231) |
| 53 | Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robot... | [arXiv](https://arxiv.org/abs/2403.03890) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 54 | Humanoid Locomotion as Next Token Prediction | [arXiv](https://arxiv.org/abs/2402.19469) |
| 55 | Humanoid Parkour Learning | [arXiv](https://arxiv.org/abs/2406.10759) |
| 56 | I-CTRL: Imitation to Control Humanoid Robots Through Constrained Re... | [arXiv](https://arxiv.org/abs/2405.08726) |
| 57 | Illusion3D: 3D Multiview Illusion with 2D Diffusion Priors | [arXiv](https://arxiv.org/abs/2412.09625) |
| 58 | In-Context Imitation Learning via Next-Token Prediction | [arXiv](https://arxiv.org/abs/2408.15980) |
| 59 | Inference-Time Policy Steering through Human Interactions | [arXiv](https://arxiv.org/abs/2411.16627) |
| 60 | IntervenGen: Interventional Data Generation for Robust and Data-Eff... | [arXiv](https://arxiv.org/abs/2405.01472) |
| 61 | KAN: Kolmogorov-Arnold Networks | [arXiv](https://arxiv.org/abs/2404.19756) |
| 62 | LEGENT: Open Platform for Embodied Agents | [arXiv](https://arxiv.org/abs/2404.18243) |
| 63 | Learning Force Control for Legged Manipulation | [arXiv](https://arxiv.org/abs/2405.01402) |
| 64 | Learning Generalizable Feature Fields for Mobile Manipulation | [arXiv](https://arxiv.org/abs/2403.07563) |
| 65 | Learning Humanoid Locomotion over Challenging Terrain | [arXiv](https://arxiv.org/abs/2410.03654) |
| 66 | Learning Time-Optimal and Speed-Adjustable Tactile In-Hand Manipula... | [arXiv](https://arxiv.org/abs/2411.13148) |
| 67 | Learning Visuotactile Skills with Two Multifingered Hands | [arXiv](https://arxiv.org/abs/2404.16823) |
| 68 | Learning to walk in confined spaces using 3D representation | [arXiv](https://arxiv.org/abs/2403.00187) |
| 69 | Learning-based Trajectory Tracking for Bird-inspired Flapping-Wing ... | [arXiv](https://arxiv.org/abs/2411.15130) |
| 70 | Lessons from Learning to Spin "Pens" | [arXiv](https://arxiv.org/abs/2407.18902) |
| 71 | Leveraging Symmetry in RL-based Legged Locomotion Control | [arXiv](https://arxiv.org/abs/2403.17320) |
| 72 | LocoMan: Advancing Versatile Quadrupedal Dexterity with Lightweight... | [arXiv](https://arxiv.org/abs/2403.18197) |
| 73 | ManiBox: Enhancing Embodied Spatial Generalization via Scalable Sim... | [arXiv](https://arxiv.org/abs/2411.01850) |
| 74 | ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Man... | [arXiv](https://arxiv.org/abs/2403.08321) |
| 75 | Model-Based Diffusion for Trajectory Optimization | [arXiv](https://arxiv.org/abs/2407.01573) |
| 76 | Motion Prompting: Controlling Video Generation with Motion Trajecto... | [arXiv](https://arxiv.org/abs/2412.02700) |
| 77 | Moving Off-the-Grid: Scene-Grounded Video Representations | [arXiv](https://arxiv.org/abs/2411.05927) |
| 78 | Multimodal Visual-Tactile Representation Learning through Self-Supe... | [arXiv](https://arxiv.org/abs/2401.12024) |
| 79 | NaVILA: Legged Robot Vision-Language-Action Model for Navigation | [arXiv](https://arxiv.org/abs/2412.04453) |
| 80 | Natural Language Can Help Bridge the Sim2Real Gap | [arXiv](https://arxiv.org/abs/2405.10020) |
| 81 | OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2403.07870) |
| 82 | Offline Actor-Critic Reinforcement Learning Scales to Large Models | [arXiv](https://arxiv.org/abs/2402.05546) |
| 83 | Offline Imitation Learning Through Graph Search and Retrieval | [arXiv](https://arxiv.org/abs/2407.15403) |
| 84 | Omnigrasp: Grasping Diverse Objects with Simulated Humanoids | [arXiv](https://arxiv.org/abs/2407.11385) |
| 85 | On Pretraining Data Diversity for Self-Supervised Learning | [arXiv](https://arxiv.org/abs/2403.13808) |
| 86 | One Step Diffusion via Shortcut Models | [arXiv](https://arxiv.org/abs/2410.12557) |
| 87 | Open-TeleVision: Teleoperation with Immersive Active Visual Feedback | [arXiv](https://arxiv.org/abs/2407.01512) |
| 88 | Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories f... | [arXiv](https://arxiv.org/abs/2409.20514) |
| 89 | Pandora: Towards General World Model with Natural Language Actions ... | [arXiv](https://arxiv.org/abs/2406.09455) |
| 90 | PaperBot: Learning to Design Real-World Tools Using Paper | [arXiv](https://arxiv.org/abs/2403.09566) |
| 91 | Pedipulate: Enabling Manipulation Skills using a Quadruped Robot's Leg | [arXiv](https://arxiv.org/abs/2402.10837) |
| 92 | Physically Embodied Gaussian Splatting: A Realtime Correctable Worl... | [arXiv](https://arxiv.org/abs/2406.10788) |
| 93 | Point Cloud Mamba: Point Cloud Learning via State Space Model | [arXiv](https://arxiv.org/abs/2403.00762) |
| 94 | PoliFormer: Scaling On-Policy RL with Transformers Results in Maste... | [arXiv](https://arxiv.org/abs/2406.20083) | [Code](https://poliformer.github.io) |
| 95 | Policy-Guided Diffusion | [arXiv](https://arxiv.org/abs/2404.06356) |
| 96 | Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Re... | [arXiv](https://arxiv.org/abs/2410.21845) |
| 97 | Probing the 3D Awareness of Visual Foundation Models | [arXiv](https://arxiv.org/abs/2404.08636) |
| 98 | RLDG: Robotic Generalist Policy Distillation via Reinforcement Lear... | [arXiv](https://arxiv.org/abs/2412.09858) |
| 99 | Radiance Fields for Robotic Teleoperation | [arXiv](https://arxiv.org/abs/2407.20194) |
| 100 | ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints... | [arXiv](https://arxiv.org/abs/2409.01652) |
| 101 | Reconstructing Hand-Held Objects in 3D from Images and Videos | [arXiv](https://arxiv.org/abs/2404.06507) |
| 102 | Reconstruction and Simulation of Elastic Objects with Spring-Mass 3... | [arXiv](https://arxiv.org/abs/2403.09434) |
| 103 | Reinforcement Learning from Wild Animal Videos | [arXiv](https://arxiv.org/abs/2412.04273) |
| 104 | Rethinking Few-shot 3D Point Cloud Semantic Segmentation | [arXiv](https://arxiv.org/abs/2403.00592) |
| 105 | RoboDuet: Learning a Cooperative Policy for Whole-body Legged Loco-... | [arXiv](https://arxiv.org/abs/2403.17367) |
| 106 | Robot See Robot Do: Imitating Articulated Object Manipulation with ... | [arXiv](https://arxiv.org/abs/2409.18121) |
| 107 | Robot Utility Models: General Policies for Zero-Shot Deployment in ... | [arXiv](https://arxiv.org/abs/2409.05865) |
| 108 | Run-time Observation Interventions Make Vision-Language-Action Mode... | [arXiv](https://arxiv.org/abs/2410.01971) |
| 109 | SATO: Stable Text-to-Motion Framework | [arXiv](https://arxiv.org/abs/2405.01461) |
| 110 | SOLAMI: Social Vision-Language-Action Modeling for Immersive Intera... | [arXiv](https://arxiv.org/abs/2412.00174) |
| 111 | SPIN: Simultaneous Perception, Interaction and Navigation | [arXiv](https://arxiv.org/abs/2405.07991) |
| 112 | Scaling 4D Representations | [arXiv](https://arxiv.org/abs/2412.15212) |
| 113 | Scaling Cross-Embodied Learning: One Policy for Manipulation, Navig... | [arXiv](https://arxiv.org/abs/2408.11812) |
| 114 | ScrewMimic: Bimanual Imitation from Human Videos with Screw Space P... | [arXiv](https://arxiv.org/abs/2405.03666) |
| 115 | Segment Anything without Supervision | [arXiv](https://arxiv.org/abs/2406.20081) |
| 116 | SkillMimic: Learning Basketball Interaction Skills from Demonstrations | [arXiv](https://arxiv.org/abs/2408.15270) |
| 117 | Soft Robotic Dynamic In-Hand Pen Spinning | [arXiv](https://arxiv.org/abs/2411.12734) |
| 118 | Sparse Diffusion Policy: A Sparse, Reusable, and Flexible Policy fo... | [arXiv](https://arxiv.org/abs/2407.01531) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 119 | Splat-MOVER: Multi-Stage, Open-Vocabulary Robotic Manipulation via ... | [arXiv](https://arxiv.org/abs/2405.04378) |
| 120 | Splatt3R: Zero-shot Gaussian Splatting from Uncalibrated Image Pairs | [arXiv](https://arxiv.org/abs/2408.13912) |
| 121 | SpringGrasp: Synthesizing Compliant, Dexterous Grasps under Shape U... | [arXiv](https://arxiv.org/abs/2404.13532) |
| 122 | TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correc... | [arXiv](https://arxiv.org/abs/2405.10315) |
| 123 | Tactile DreamFusion: Exploiting Tactile Sensing for 3D Generation | [arXiv](https://arxiv.org/abs/2412.06785) |
| 124 | TeleMoMa: A Modular and Versatile Teleoperation System for Mobile M... | [arXiv](https://arxiv.org/abs/2403.07869) |
| 125 | The Matrix: Infinite-Horizon World Generation with Real-Time Moving... | [arXiv](https://arxiv.org/abs/2412.03568) |
| 126 | The Platonic Representation Hypothesis | [arXiv](https://arxiv.org/abs/2405.07987) |
| 127 | Track2Act: Predicting Point Tracks from Internet Videos enables Gen... | [arXiv](https://arxiv.org/abs/2405.01527) |
| 128 | Transparent Image Layer Diffusion using Latent Transparency | [arXiv](https://arxiv.org/abs/2402.17113) |
| 129 | TutteNet: Injective 3D Deformations by Composition of 2D Mesh Defor... | [arXiv](https://arxiv.org/abs/2406.12121) |
| 130 | Unifying Generation and Prediction on Graphs with Latent Graph Diff... | [arXiv](https://arxiv.org/abs/2402.02518) |
| 131 | VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding | [arXiv](https://arxiv.org/abs/2410.13860) |
| 132 | Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-... | [arXiv](https://arxiv.org/abs/2403.12943) |
| 133 | View-Invariant Policy Learning via Zero-Shot Novel View Synthesis | [arXiv](https://arxiv.org/abs/2409.03685) |
| 134 | Visual Whole-Body Control for Legged Loco-Manipulation | [arXiv](https://arxiv.org/abs/2403.16967) |
| 135 | Wav-KAN: Wavelet Kolmogorov-Arnold Networks | [arXiv](https://arxiv.org/abs/2405.12832) |
| 136 | When Do We Not Need Larger Vision Models? | [arXiv](https://arxiv.org/abs/2403.13043) |
| 137 | Whole-body Humanoid Robot Locomotion with Human Reference | [arXiv](https://arxiv.org/abs/2402.18294) |
| 138 | WildLMa: Long Horizon Loco-Manipulation in the Wild | [arXiv](https://arxiv.org/abs/2411.15131) |
| 139 | Yell At Your Robot: Improving On-the-Fly from Language Corrections | [arXiv](https://arxiv.org/abs/2403.12910) |
| 140 | Download Log | [Google Scholar](https://scholar.google.com/scholar?q=download_log) |
| 141 | Download Log v2 | [Google Scholar](https://scholar.google.com/scholar?q=download_log_v2) |

**2023**

| # | Title | Links |
|---|-------|-------|
| 1 | 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment | [arXiv](https://arxiv.org/abs/2308.04352) |
| 2 | 3DShape2VecSet: A 3D Shape Representation for Neural Fields and Gen... | [arXiv](https://arxiv.org/abs/2301.11445) |
| 3 | A Universal Semantic-Geometric Representation for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2306.10474) |
| 4 | AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents | [arXiv](https://arxiv.org/abs/2310.09971) |
| 5 | Actor-Critic Model Predictive Control: Differentiable Optimization ... | [arXiv](https://arxiv.org/abs/2306.09852) |
| 6 | AdaptDiffuser: Diffusion Models as Adaptive Self-evolving Planners | [arXiv](https://arxiv.org/abs/2302.01877) |
| 7 | Adding Conditional Control to Text-to-Image Diffusion Models | [arXiv](https://arxiv.org/abs/2302.05543) |
| 8 | Agile Catching with Whole-Body MPC and Blackbox Policy Learning | [arXiv](https://arxiv.org/abs/2306.08205) |
| 9 | Barkour: Benchmarking Animal-level Agility with Quadruped Robots | [arXiv](https://arxiv.org/abs/2305.14654) |
| 10 | BridgeData V2: A Dataset for Robot Learning at Scale | [arXiv](https://arxiv.org/abs/2308.12952) |
| 11 | CLIP$^2$: Contrastive Language-Image-Point Pretraining from Real-Wo... | [arXiv](https://arxiv.org/abs/2303.12417) |
| 12 | Consistency Models | [arXiv](https://arxiv.org/abs/2303.01469) |
| 13 | Consistency Models as a Rich and Efficient Policy Class for Reinfor... | [arXiv](https://arxiv.org/abs/2309.16984) |
| 14 | Contrastive Energy Prediction for Exact Energy-Guided Diffusion Sam... | [arXiv](https://arxiv.org/abs/2304.12824) |
| 15 | Crossway Diffusion: Improving Diffusion-based Visuomotor Policy via... | [arXiv](https://arxiv.org/abs/2307.01849) |
| 16 | Cumulative Reasoning with Large Language Models | [arXiv](https://arxiv.org/abs/2308.04371) |
| 17 | DINOv2: Learning Robust Visual Features without Supervision | [arXiv](https://arxiv.org/abs/2304.07193) |
| 18 | Data-Free Learning of Reduced-Order Kinematics | [arXiv](https://arxiv.org/abs/2305.03846) |
| 19 | Deep Learning on Object-centric 3D Neural Fields | [arXiv](https://arxiv.org/abs/2312.13277) |
| 20 | Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene R... | [arXiv](https://arxiv.org/abs/2309.13101) |
| 21 | Denoising Diffusion Autoencoders are Unified Self-supervised Learners | [arXiv](https://arxiv.org/abs/2303.09769) |
| 22 | Detector-Free Structure from Motion | [arXiv](https://arxiv.org/abs/2306.15669) |
| 23 | DexCatch: Learning to Catch Arbitrary Objects with Dexterous Hands | [arXiv](https://arxiv.org/abs/2310.08809) |
| 24 | DexPBT: Scaling up Dexterous Manipulation for Hand-Arm Systems with... | [arXiv](https://arxiv.org/abs/2305.12127) |
| 25 | DiMSam: Diffusion Models as Samplers for Task and Motion Planning u... | [arXiv](https://arxiv.org/abs/2306.13196) |
| 26 | Differentiable Blocks World: Qualitative 3D Decomposition by Render... | [arXiv](https://arxiv.org/abs/2307.05473) |
| 27 | DiffiT: Diffusion Vision Transformers for Image Generation | [arXiv](https://arxiv.org/abs/2312.02139) |
| 28 | Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks | [arXiv](https://arxiv.org/abs/2305.12171) |
| 29 | Diffusion Model is an Effective Planner and Data Synthesizer for Mu... | [arXiv](https://arxiv.org/abs/2305.18459) |
| 30 | Diffusion Models Beat GANs on Image Classification | [arXiv](https://arxiv.org/abs/2307.08702) |
| 31 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | [arXiv](https://arxiv.org/abs/2303.04137) | [Code](https://github.com/real-stanford/diffusion_policy) |
| 32 | DreamGaussian: Generative Gaussian Splatting for Efficient 3D Conte... | [arXiv](https://arxiv.org/abs/2309.16653) |
| 33 | DreamSim: Learning New Dimensions of Human Visual Similarity using ... | [arXiv](https://arxiv.org/abs/2306.09344) |
| 34 | DreamTeacher: Pretraining Image Backbones with Deep Generative Models | [arXiv](https://arxiv.org/abs/2307.07487) |
| 35 | EDGI: Equivariant Diffusion for Planning with Embodied Agents | [arXiv](https://arxiv.org/abs/2303.12410) |
| 36 | Efficient Diffusion Policies for Offline Reinforcement Learning | [arXiv](https://arxiv.org/abs/2305.20081) |
| 37 | Efficient Online Reinforcement Learning with Offline Data | [arXiv](https://arxiv.org/abs/2302.02948) |
| 38 | Ego-Exo4D: Understanding Skilled Human Activity from First- and Thi... | [arXiv](https://arxiv.org/abs/2311.18259) |
| 39 | Explaining the Decisions of Deep Policy Networks for Robotic Manipu... | [arXiv](https://arxiv.org/abs/2310.19432) |
| 40 | Extracting Reward Functions from Diffusion Models | [arXiv](https://arxiv.org/abs/2306.01804) |
| 41 | Extreme Parkour with Legged Robots | [arXiv](https://arxiv.org/abs/2309.14341) |
| 42 | Flexible Techniques for Differentiable Rendering with 3D Gaussians | [arXiv](https://arxiv.org/abs/2308.14737) |
| 43 | Fluid Simulation on Neural Flow Maps | [arXiv](https://arxiv.org/abs/2312.14635) |
| 44 | For Pre-Trained Vision Models in Motor Control, Not All Policy Lear... | [arXiv](https://arxiv.org/abs/2304.04591) |
| 45 | For SALE: State-Action Representation Learning for Deep Reinforceme... | [arXiv](https://arxiv.org/abs/2306.02451) |
| 46 | Foundation Models for Decision Making: Problems, Methods, and Oppor... | [arXiv](https://arxiv.org/abs/2303.04129) |
| 47 | From Word Models to World Models: Translating from Natural Language... | [arXiv](https://arxiv.org/abs/2306.12672) |
| 48 | Frozen Transformers in Language Models Are Effective Visual Encoder... | [arXiv](https://arxiv.org/abs/2310.12973) |
| 49 | GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework f... | [arXiv](https://arxiv.org/abs/2309.13037) |
| 50 | GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridg... | [arXiv](https://arxiv.org/abs/2310.08529) |
| 51 | Gen2Sim: Scaling up Robot Learning in Simulation with Generative Mo... | [arXiv](https://arxiv.org/abs/2310.18308) |
| 52 | Generalized Animal Imitator: Agile Locomotion with Versatile Motion... | [arXiv](https://arxiv.org/abs/2310.01408) |
| 53 | Generating Behaviorally Diverse Policies with Latent Diffusion Models | [arXiv](https://arxiv.org/abs/2305.18738) |
| 54 | Generative Agents: Interactive Simulacra of Human Behavior | [arXiv](https://arxiv.org/abs/2304.03442) |
| 55 | Goal-Conditioned Imitation Learning using Score-based Diffusion Pol... | [arXiv](https://arxiv.org/abs/2304.02532) |
| 56 | GraspGF: Learning Score-based Grasping Primitive for Human-assistin... | [arXiv](https://arxiv.org/abs/2309.06038) |
| 57 | Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-S... | [arXiv](https://arxiv.org/abs/2303.05499) |
| 58 | Grow Your Limits: Continuous Improvement with Real-World RL for Rob... | [arXiv](https://arxiv.org/abs/2310.17634) |
| 59 | HomeRobot: Open-Vocabulary Mobile Manipulation | [arXiv](https://arxiv.org/abs/2306.11565) |
| 60 | HyperFields: Towards Zero-Shot Generation of NeRFs from Text | [arXiv](https://arxiv.org/abs/2310.17075) |
| 61 | IDQL: Implicit Q-Learning as an Actor-Critic Method with Diffusion ... | [arXiv](https://arxiv.org/abs/2304.10573) |
| 62 | Imitation Bootstrapped Reinforcement Learning | [arXiv](https://arxiv.org/abs/2311.02198) |
| 63 | Improved Techniques for Training Consistency Models | [arXiv](https://arxiv.org/abs/2310.14189) |
| 64 | Improving Long-Horizon Imitation Through Instruction Prediction | [arXiv](https://arxiv.org/abs/2306.12554) |
| 65 | Initializing Models with Larger Ones | [arXiv](https://arxiv.org/abs/2311.18823) |
| 66 | Instructed Diffuser with Temporal Condition Guidance for Offline Re... | [arXiv](https://arxiv.org/abs/2306.04875) |
| 67 | Is ImageNet worth 1 video? Learning strong image encoders from 1 lo... | [arXiv](https://arxiv.org/abs/2310.08584) |
| 68 | KITE: Keypoint-Conditioned Policies for Semantic Manipulation | [arXiv](https://arxiv.org/abs/2306.16605) |
| 69 | LISA: Reasoning Segmentation via Large Language Model | [arXiv](https://arxiv.org/abs/2308.00692) |
| 70 | LLaMA: Open and Efficient Foundation Language Models | [arXiv](https://arxiv.org/abs/2302.13971) |
| 71 | Language Reward Modulation for Pretraining Reinforcement Learning | [arXiv](https://arxiv.org/abs/2308.12270) |
| 72 | Learning Universal Policies via Text-Guided Video Generation | [arXiv](https://arxiv.org/abs/2302.00111) |
| 73 | Learning Vision from Models Rivals Learning Vision from Data | [arXiv](https://arxiv.org/abs/2312.17742) |
| 74 | Learning Vision-Based Bipedal Locomotion for Challenging Terrain | [arXiv](https://arxiv.org/abs/2309.14594) |
| 75 | Learning Vision-based Pursuit-Evasion Robot Policies | [arXiv](https://arxiv.org/abs/2308.16185) |
| 76 | Learning a Universal Human Prior for Dexterous Manipulation from Hu... | [arXiv](https://arxiv.org/abs/2304.04602) |
| 77 | Learning from One Continuous Video Stream | [arXiv](https://arxiv.org/abs/2312.00598) |
| 78 | Learning to (Learn at Test Time | [arXiv](https://arxiv.org/abs/2310.13807) |
| 79 | Learning to Model the World with Language | [arXiv](https://arxiv.org/abs/2308.01399) |
| 80 | Learning to Read Braille: Bridging the Tactile Reality Gap with Dif... | [arXiv](https://arxiv.org/abs/2304.01182) |
| 81 | Learning to Walk and Fly with Adversarial Motion Priors | [arXiv](https://arxiv.org/abs/2309.12784) |
| 82 | Let 2D Diffusion Model Know 3D-Consistency for Robust Text-to-3D Ge... | [arXiv](https://arxiv.org/abs/2303.07937) |
| 83 | Lifelong Robot Learning with Human Assisted Language Planners | [arXiv](https://arxiv.org/abs/2309.14321) |
| 84 | MADiff: Offline Multi-agent Learning with Diffusion Models | [arXiv](https://arxiv.org/abs/2305.17330) |
| 85 | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [arXiv](https://arxiv.org/abs/2312.00752) |
| 86 | Mastering Diverse Domains through World Models | [arXiv](https://arxiv.org/abs/2301.04104) |
| 87 | Mastering Robot Manipulation with Multimodal Prompts through Pretra... | [arXiv](https://arxiv.org/abs/2310.09676) |
| 88 | Matryoshka Diffusion Models | [arXiv](https://arxiv.org/abs/2310.15111) |
| 89 | MetaDiffuser: Diffusion Model as Conditional Planner for Offline Me... | [arXiv](https://arxiv.org/abs/2305.19923) |
| 90 | MoDem-V2: Visuo-Motor World Models for Real-World Robot Manipulation | [arXiv](https://arxiv.org/abs/2309.14236) |
| 91 | Mosaic-SDF for 3D Generative Models | [arXiv](https://arxiv.org/abs/2312.09222) |
| 92 | Multimodal Chain-of-Thought Reasoning in Language Models | [arXiv](https://arxiv.org/abs/2302.00923) |
| 93 | Neural Radiance Field Codebooks | [arXiv](https://arxiv.org/abs/2301.04101) |
| 94 | NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration | [arXiv](https://arxiv.org/abs/2310.07896) | [Code](https://gmdp-navigation.github.io) |
| 95 | Non-parametric regression for robot learning on manifolds | [arXiv](https://arxiv.org/abs/2310.19561) |
| 96 | On Bringing Robots Home | [arXiv](https://arxiv.org/abs/2311.16098) |
| 97 | On the Utility of Koopman Operator Theory in Learning Dexterous Man... | [arXiv](https://arxiv.org/abs/2303.13446) |
| 98 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | [arXiv](https://arxiv.org/abs/2310.08864) | [Code](https://github.com/google-deepmind/open_x_embodiment) |
| 99 | PAPR: Proximity Attention Point Rendering | [arXiv](https://arxiv.org/abs/2307.11086) |
| 100 | PIE-NeRF: Physics-based Interactive Elastodynamics with NeRF | [arXiv](https://arxiv.org/abs/2311.13099) |
| 101 | PLEX: Making the Most of the Available Data for Robotic Manipulatio... | [arXiv](https://arxiv.org/abs/2303.08789) |
| 102 | Parallel $Q$-Learning: Scaling Off-policy Reinforcement Learning un... | [arXiv](https://arxiv.org/abs/2307.12983) |
| 103 | Point Transformer V3: Simpler, Faster, Stronger | [arXiv](https://arxiv.org/abs/2312.10035) |
| 104 | PointOdyssey: A Large-Scale Synthetic Dataset for Long-Term Point T... | [arXiv](https://arxiv.org/abs/2307.15055) |
| 105 | Policy Representation via Diffusion Probability Model for Reinforce... | [arXiv](https://arxiv.org/abs/2305.13122) |
| 106 | Ponder: Point Cloud Pre-training via Neural Rendering | [arXiv](https://arxiv.org/abs/2301.00157) |
| 107 | Ponymation: Learning Articulated 3D Animal Motions from Unlabeled O... | [arXiv](https://arxiv.org/abs/2312.13604) |
| 108 | Prompt a Robot to Walk with Large Language Models | [arXiv](https://arxiv.org/abs/2309.09969) |
| 109 | R-MAE: Regions Meet Masked Autoencoders | [arXiv](https://arxiv.org/abs/2306.05411) |
| 110 | REFLECT: Summarizing Robot Experiences for Failure Explanation and ... | [arXiv](https://arxiv.org/abs/2306.15724) |
| 111 | RLIF: Interactive Imitation Learning as Reinforcement Learning | [arXiv](https://arxiv.org/abs/2311.12996) |
| 112 | Real-time Photorealistic Dynamic Scene Representation and Rendering... | [arXiv](https://arxiv.org/abs/2310.10642) |
| 113 | Reinforcement Learning with Foundation Priors: Let the Embodied Age... | [arXiv](https://arxiv.org/abs/2310.02635) |
| 114 | ReorientDiff: Diffusion Model based Reorientation for Object Manipu... | [arXiv](https://arxiv.org/abs/2303.12700) |
| 115 | Retentive Network: A Successor to Transformer for Large Language Mo... | [arXiv](https://arxiv.org/abs/2307.08621) |
| 116 | Return of Unconditional Generation: A Self-supervised Representatio... | [arXiv](https://arxiv.org/abs/2312.03701) |
| 117 | Reward-Directed Conditional Diffusion: Provable Distribution Estima... | [arXiv](https://arxiv.org/abs/2307.07055) |
| 118 | RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation | [arXiv](https://arxiv.org/abs/2308.15975) |
| 119 | Robot Learning with Sensorimotor Pre-training | [arXiv](https://arxiv.org/abs/2306.10007) |
| 120 | Robotic Offline RL from Internet Videos via Value-Function Pre-Trai... | [arXiv](https://arxiv.org/abs/2309.13041) |
| 121 | Robust and Versatile Bipedal Jumping Control through Reinforcement ... | [arXiv](https://arxiv.org/abs/2302.09450) |
| 122 | SAM-CLIP: Merging Vision Foundation Models towards Semantic and Spa... | [arXiv](https://arxiv.org/abs/2310.15308) |
| 123 | SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust... | [arXiv](https://arxiv.org/abs/2312.01990) | [Code](https://robotics-transformer-x.github.io) |
| 124 | SLoMo: A General System for Legged Robot Motion Imitation from Casu... | [arXiv](https://arxiv.org/abs/2304.14389) | [Code](https://slomo-legs.github.io) |
| 125 | SPRING: Studying the Paper and Reasoning to Play Games | [arXiv](https://arxiv.org/abs/2305.15486) |
| 126 | SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | [arXiv](https://arxiv.org/abs/2306.00148) |
| 127 | Sampling-based Model Predictive Control Leveraging Parallelizable P... | [arXiv](https://arxiv.org/abs/2307.09105) |
| 128 | Scaling Laws of Synthetic Images for Model Training ... for Now | [arXiv](https://arxiv.org/abs/2312.04567) |
| 129 | Scaling Robot Learning with Semantically Imagined Experience | [arXiv](https://arxiv.org/abs/2302.11550) |
| 130 | Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisi... | [arXiv](https://arxiv.org/abs/2307.14535) |
| 131 | See to Touch: Learning Tactile Dexterity through Visual Incentives | [arXiv](https://arxiv.org/abs/2309.12300) |
| 132 | Segment Any Point Cloud Sequences by Distilling Vision Foundation M... | [arXiv](https://arxiv.org/abs/2306.09347) |
| 133 | Segment Everything Everywhere All at Once | [arXiv](https://arxiv.org/abs/2304.06718) |
| 134 | Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in G... | [arXiv](https://arxiv.org/abs/2310.11441) |
| 135 | Shelving, Stacking, Hanging: Relational Pose Diffusion for Multi-mo... | [arXiv](https://arxiv.org/abs/2307.04751) |
| 136 | Sim-to-Real Learning for Humanoid Box Loco-Manipulation | [arXiv](https://arxiv.org/abs/2310.03191) |
| 137 | SparseDFF: Sparse-View Feature Distillation for One-Shot Dexterous ... | [arXiv](https://arxiv.org/abs/2310.16838) |
| 138 | SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Rec... | [arXiv](https://arxiv.org/abs/2311.12775) |
| 139 | TD-MPC2: Scalable, Robust World Models for Continuous Control | [arXiv](https://arxiv.org/abs/2310.16828) |
| 140 | Text-to-3D using Gaussian Splatting | [arXiv](https://arxiv.org/abs/2309.16585) |
| 141 | Text2Reward: Reward Shaping with Language Models for Reinforcement ... | [arXiv](https://arxiv.org/abs/2309.11489) |
| 142 | The Dormant Neuron Phenomenon in Deep Reinforcement Learning | [arXiv](https://arxiv.org/abs/2302.12902) |
| 143 | The Wisdom of Hindsight Makes Language Models Better Instruction Fo... | [arXiv](https://arxiv.org/abs/2302.05206) |
| 144 | To the Noise and Back: Diffusion for Shared Autonomy | [arXiv](https://arxiv.org/abs/2302.12244) |
| 145 | Towards Stable Test-Time Adaptation in Dynamic Wild World | [arXiv](https://arxiv.org/abs/2302.12400) |
| 146 | UniTeam: Open Vocabulary Mobile Manipulation Challenge | [arXiv](https://arxiv.org/abs/2312.08611) |
| 147 | VILA: On Pre-training for Visual Language Models | [arXiv](https://arxiv.org/abs/2312.07533) |
| 148 | Value function estimation using conditional diffusion models for co... | [arXiv](https://arxiv.org/abs/2306.07290) |
| 149 | Video Prediction Models as Rewards for Reinforcement Learning | [arXiv](https://arxiv.org/abs/2305.14343) |
| 150 | Visual Point Cloud Forecasting enables Scalable Autonomous Driving | [arXiv](https://arxiv.org/abs/2312.17655) |
| 151 | What's the Magic Word? A Control Theory of LLM Prompting | [arXiv](https://arxiv.org/abs/2310.04444) |
| 152 | XSkill: Cross Embodiment Skill Discovery | [arXiv](https://arxiv.org/abs/2307.09955) |
| 153 | Zero-1-to-3: Zero-shot One Image to 3D Object | [arXiv](https://arxiv.org/abs/2303.11328) |
| 154 | Zero123++: a Single Image to Consistent Multi-view Diffusion Base M... | [arXiv](https://arxiv.org/abs/2310.15110) |
| 155 | pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Genera... | [arXiv](https://arxiv.org/abs/2312.12337) |

**2022**

| # | Title | Links |
|---|-------|-------|
| 1 | 3D Neural Field Generation using Triplane Diffusion | [arXiv](https://arxiv.org/abs/2211.16677) |
| 2 | AK: Attentive Kernel for Information Gathering | [arXiv](https://arxiv.org/abs/2205.06426) |
| 3 | ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physical... | [arXiv](https://arxiv.org/abs/2205.01906) |
| 4 | Aug-NeRF: Training Stronger Neural Radiance Fields with Triple-Leve... | [arXiv](https://arxiv.org/abs/2207.01164) |
| 5 | Autonomously Untangling Long Cables | [arXiv](https://arxiv.org/abs/2207.07813) |
| 6 | Can Wikipedia Help Offline Reinforcement Learning? | [arXiv](https://arxiv.org/abs/2201.12122) |
| 7 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | [arXiv](https://arxiv.org/abs/2201.11903) |
| 8 | Classifier-Free Diffusion Guidance | [arXiv](https://arxiv.org/abs/2207.12598) |
| 9 | CodeRL: Mastering Code Generation through Pretrained Models and Dee... | [arXiv](https://arxiv.org/abs/2207.01780) |
| 10 | DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sam... | [arXiv](https://arxiv.org/abs/2206.00927) |
| 11 | Data-Driven Feature Tracking for Event Cameras With and Without Frames | [arXiv](https://arxiv.org/abs/2211.12826) |
| 12 | Differentiable Point-Based Radiance Fields for Efficient View Synth... | [arXiv](https://arxiv.org/abs/2205.14330) |
| 13 | Diffusion Policies as an Expressive Policy Class for Offline Reinfo... | [arXiv](https://arxiv.org/abs/2208.06193) |
| 14 | Diffusion-LM Improves Controllable Text Generation | [arXiv](https://arxiv.org/abs/2205.14217) |
| 15 | Does Self-supervised Learning Really Improve Reinforcement Learning... | [arXiv](https://arxiv.org/abs/2206.05266) |
| 16 | Elucidating the Design Space of Diffusion-Based Generative Models | [arXiv](https://arxiv.org/abs/2206.00364) |
| 17 | Emergent Abilities of Large Language Models | [arXiv](https://arxiv.org/abs/2206.07682) |
| 18 | Fast Sampling of Diffusion Models with Exponential Integrator | [arXiv](https://arxiv.org/abs/2204.13902) |
| 19 | Flamingo: a Visual Language Model for Few-Shot Learning | [arXiv](https://arxiv.org/abs/2204.14198) |
| 20 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-A... | [arXiv](https://arxiv.org/abs/2205.14135) |
| 21 | Imagen Video: High Definition Video Generation with Diffusion Models | [arXiv](https://arxiv.org/abs/2210.02303) |
| 22 | In-Hand Object Rotation via Rapid Motor Adaptation | [arXiv](https://arxiv.org/abs/2210.04887) |
| 23 | InternVideo: General Video Foundation Models via Generative and Dis... | [arXiv](https://arxiv.org/abs/2212.03191) |
| 24 | Is Conditional Generative Modeling all you need for Decision-Making? | [arXiv](https://arxiv.org/abs/2211.15657) |
| 25 | Iterative Residual Policy: for Goal-Conditioned Dynamic Manipulatio... | [arXiv](https://arxiv.org/abs/2203.00663) |
| 26 | Language Control Diffusion: Efficiently Scaling through Space, Time... | [arXiv](https://arxiv.org/abs/2210.15629) |
| 27 | Language-driven Semantic Segmentation | [arXiv](https://arxiv.org/abs/2201.03546) |
| 28 | Learning Continuous Grasping Function with a Dexterous Hand from Hu... | [arXiv](https://arxiv.org/abs/2207.05053) |
| 29 | Learning to Use Chopsticks in Diverse Gripping Styles | [arXiv](https://arxiv.org/abs/2205.14313) |
| 30 | MoDem: Accelerating Visual Model-Based Reinforcement Learning with ... | [arXiv](https://arxiv.org/abs/2212.05698) |
| 31 | NeRF2Real: Sim2real Transfer of Vision-guided Bipedal Motion Skills... | [arXiv](https://arxiv.org/abs/2210.04932) |
| 32 | On Distillation of Guided Diffusion Models | [arXiv](https://arxiv.org/abs/2210.03142) |
| 33 | On the Power of Foundation Models | [arXiv](https://arxiv.org/abs/2211.16327) |
| 34 | PartSLIP: Low-Shot Part Segmentation for 3D Point Clouds via Pretra... | [arXiv](https://arxiv.org/abs/2212.01558) |
| 35 | Photorealistic Text-to-Image Diffusion Models with Deep Language Un... | [arXiv](https://arxiv.org/abs/2205.11487) |
| 36 | Planning with Diffusion for Flexible Behavior Synthesis | [arXiv](https://arxiv.org/abs/2205.09991) |
| 37 | Point Transformer V2: Grouped Vector Attention and Partition-based ... | [arXiv](https://arxiv.org/abs/2210.05666) |
| 38 | Point-E: A System for Generating 3D Point Clouds from Complex Prompts | [arXiv](https://arxiv.org/abs/2212.08751) |
| 39 | PointCLIP V2: Prompting CLIP and GPT for Powerful 3D Open-world Lea... | [arXiv](https://arxiv.org/abs/2211.11682) |
| 40 | PointNeXt: Revisiting PointNet++ with Improved Training and Scaling... | [arXiv](https://arxiv.org/abs/2206.04670) |
| 41 | Pre-Trained Language Models for Interactive Decision-Making | [arXiv](https://arxiv.org/abs/2202.01771) |
| 42 | Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo | [arXiv](https://arxiv.org/abs/2212.00541) |
| 43 | Prompt-to-Prompt Image Editing with Cross Attention Control | [arXiv](https://arxiv.org/abs/2208.01626) |
| 44 | R3M: A Universal Visual Representation for Robot Manipulation | [arXiv](https://arxiv.org/abs/2203.12601) |
| 45 | SAM-RL: Sensing-Aware Model-Based Reinforcement Learning via Differ... | [arXiv](https://arxiv.org/abs/2210.15185) |
| 46 | SE(3)-DiffusionFields: Learning smooth cost functions for joint gra... | [arXiv](https://arxiv.org/abs/2209.03855) |
| 47 | SeedFormer: Patch Seeds based Point Cloud Completion with Upsample ... | [arXiv](https://arxiv.org/abs/2207.10315) |
| 48 | Simplicial Embeddings in Self-Supervised Learning and Downstream Cl... | [arXiv](https://arxiv.org/abs/2204.00616) |
| 49 | SparsePose: Sparse-View Camera Pose Regression and Refinement | [arXiv](https://arxiv.org/abs/2211.16991) |
| 50 | StructDiffusion: Language-Guided Creation of Physically-Valid Struc... | [arXiv](https://arxiv.org/abs/2211.04604) |
| 51 | Temporal Difference Learning for Model Predictive Control | [arXiv](https://arxiv.org/abs/2203.04955) |
| 52 | The Primacy Bias in Deep Reinforcement Learning | [arXiv](https://arxiv.org/abs/2205.07802) |
| 53 | Training Compute-Optimal Large Language Models | [arXiv](https://arxiv.org/abs/2203.15556) |
| 54 | Understanding Diffusion Models: A Unified Perspective | [arXiv](https://arxiv.org/abs/2208.11970) |
| 55 | VRL3: A Data-Driven Framework for Visual Deep Reinforcement Learning | [arXiv](https://arxiv.org/abs/2202.10324) |
| 56 | Visual Prompting via Image Inpainting | [arXiv](https://arxiv.org/abs/2209.00647) |
| 57 | gDDIM: Generalized denoising diffusion implicit models | [arXiv](https://arxiv.org/abs/2206.05564) |

**2021**

| # | Title | Links |
|---|-------|-------|
| 1 | Coarse-to-Fine Q-attention: Efficient Learning for Visual Robotic M... | [arXiv](https://arxiv.org/abs/2106.12534) |
| 2 | Deep Reinforcement Learning at the Edge of the Statistical Precipice | [arXiv](https://arxiv.org/abs/2108.13264) |
| 3 | Diffusion Models Beat GANs on Image Synthesis | [arXiv](https://arxiv.org/abs/2105.05233) |
| 4 | Dropout Q-Functions for Doubly Efficient Reinforcement Learning | [arXiv](https://arxiv.org/abs/2110.02034) |
| 5 | Efficiently Modeling Long Sequences with Structured State Spaces | [arXiv](https://arxiv.org/abs/2111.00396) |
| 6 | Emerging Properties in Self-Supervised Vision Transformers | [arXiv](https://arxiv.org/abs/2104.14294) |
| 7 | FrankMocap: A Monocular 3D Whole-Body Pose Estimation System via Re... | [arXiv](https://arxiv.org/abs/2108.06428) |
| 8 | Geometric Fabrics: Generalizing Classical Mechanics to Capture the ... | [arXiv](https://arxiv.org/abs/2109.10443) |
| 9 | High-Resolution Image Synthesis with Latent Diffusion Models | [arXiv](https://arxiv.org/abs/2112.10752) |
| 10 | Improved Denoising Diffusion Probabilistic Models | [arXiv](https://arxiv.org/abs/2102.09672) |
| 11 | Learning Transferable Visual Models From Natural Language Supervision | [arXiv](https://arxiv.org/abs/2103.00020) |
| 12 | Masked Autoencoders Are Scalable Vision Learners | [arXiv](https://arxiv.org/abs/2111.06377) |
| 13 | Mastering Visual Continuous Control: Improved Data-Augmented Reinfo... | [arXiv](https://arxiv.org/abs/2107.09645) |
| 14 | Multi-Task Reinforcement Learning with Context-based Representations | [arXiv](https://arxiv.org/abs/2102.06177) |
| 15 | Offline Reinforcement Learning with Implicit Q-Learning | [arXiv](https://arxiv.org/abs/2110.06169) |
| 16 | Perceiver IO: A General Architecture for Structured Inputs & Outputs | [arXiv](https://arxiv.org/abs/2107.14795) |
| 17 | Perceiver: General Perception with Iterative Attention | [arXiv](https://arxiv.org/abs/2103.03206) |
| 18 | PointCLIP: Point Cloud Understanding by CLIP | [arXiv](https://arxiv.org/abs/2112.02413) |
| 19 | Pri3D: Can 3D Priors Help 2D Representation Learning? | [arXiv](https://arxiv.org/abs/2104.11225) |
| 20 | RRL: Resnet as representation for Reinforcement Learning | [arXiv](https://arxiv.org/abs/2107.03380) |
| 21 | Randomized Ensembled Double Q-Learning: Learning Fast Without a Model | [arXiv](https://arxiv.org/abs/2101.05982) |
| 22 | Reinforcement Learning with Prototypical Representations | [arXiv](https://arxiv.org/abs/2102.11271) |
| 23 | RvS: What is Essential for Offline RL via Supervised Learning? | [arXiv](https://arxiv.org/abs/2112.10751) |
| 24 | StARformer: Transformer with State-Action-Reward Representations fo... | [arXiv](https://arxiv.org/abs/2110.06206) |
| 25 | Synergies Between Affordance and Geometry: 6-DoF Grasp Detection vi... | [arXiv](https://arxiv.org/abs/2104.01542) |
| 26 | Vision Transformers for Dense Prediction | [arXiv](https://arxiv.org/abs/2103.13413) |

**2020**

| # | Title | Links |
|---|-------|-------|
| 1 | An Image is Worth 16x16 Words: Transformers for Image Recognition a... | [arXiv](https://arxiv.org/abs/2010.11929) |
| 2 | Denoising Diffusion Implicit Models | [arXiv](https://arxiv.org/abs/2010.02502) |
| 3 | Denoising Diffusion Probabilistic Models | [arXiv](https://arxiv.org/abs/2006.11239) |
| 4 | Improved Baselines with Momentum Contrastive Learning | [arXiv](https://arxiv.org/abs/2003.04297) |
| 5 | Keypoints into the Future: Self-Supervised Correspondence in Model-... | [arXiv](https://arxiv.org/abs/2009.05085) |
| 6 | Object-Centric Learning with Slot Attention | [arXiv](https://arxiv.org/abs/2006.15055) |
| 7 | Physics-Based Dexterous Manipulations with Estimated Hand Poses and... | [arXiv](https://arxiv.org/abs/2008.03285) |
| 8 | Point Transformer | [arXiv](https://arxiv.org/abs/2012.09164) |
| 9 | PointContrast: Unsupervised Pre-training for 3D Point Cloud Underst... | [arXiv](https://arxiv.org/abs/2007.10985) |
| 10 | Scaling Laws for Neural Language Models | [arXiv](https://arxiv.org/abs/2001.08361) |
| 11 | Score-Based Generative Modeling through Stochastic Differential Equ... | [arXiv](https://arxiv.org/abs/2011.13456) |
| 12 | Solving Linear Inverse Problems Using the Prior Implicit in a Denoiser | [arXiv](https://arxiv.org/abs/2007.13640) |
| 13 | Training data-efficient image transformers & distillation through a... | [arXiv](https://arxiv.org/abs/2012.12877) |
| 14 | Unsupervised Learning of Visual Features by Contrasting Cluster Ass... | [arXiv](https://arxiv.org/abs/2006.09882) |

**2019**

| # | Title | Links |
|---|-------|-------|
| 1 | A Topology Layer for Machine Learning | [arXiv](https://arxiv.org/abs/1905.12200) |
| 2 | Exploring the Limits of Transfer Learning with a Unified Text-to-Te... | [arXiv](https://arxiv.org/abs/1910.10683) |
| 3 | Neural-Guided RANSAC: Learning Where to Sample Model Hypotheses | [arXiv](https://arxiv.org/abs/1905.04132) |
| 4 | Normalized Object Coordinate Space for Category-Level 6D Object Pos... | [arXiv](https://arxiv.org/abs/1901.02970) |
| 5 | Self-Supervised Correspondence in Visuomotor Policy Learning | [arXiv](https://arxiv.org/abs/1909.06933) |

**2018**

| # | Title | Links |
|---|-------|-------|
| 1 | A Style-Based Generator Architecture for Generative Adversarial Net... | [arXiv](https://arxiv.org/abs/1812.04948) |
| 2 | ChainQueen: A Real-Time Differentiable Physical Simulator for Soft ... | [arXiv](https://arxiv.org/abs/1810.01054) |
| 3 | Plan Online, Learn Offline: Efficient Learning and Exploration via ... | [arXiv](https://arxiv.org/abs/1811.01848) |
| 4 | QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robot... | [arXiv](https://arxiv.org/abs/1806.10293) |
| 5 | Videos as Space-Time Region Graphs | [arXiv](https://arxiv.org/abs/1806.01810) |

**2017**

| # | Title | Links |
|---|-------|-------|
| 1 | Asymmetric Actor Critic for Image-Based Robot Learning | [arXiv](https://arxiv.org/abs/1710.06542) |
| 2 | Distral: Robust Multitask Reinforcement Learning | [arXiv](https://arxiv.org/abs/1707.04175) |
| 3 | FiLM: Visual Reasoning with a General Conditioning Layer | [arXiv](https://arxiv.org/abs/1709.07871) |
| 4 | Graph Attention Networks | [arXiv](https://arxiv.org/abs/1710.10903) |
| 5 | Hindsight Experience Replay | [arXiv](https://arxiv.org/abs/1707.01495) |
| 6 | Leveraging Demonstrations for Deep Reinforcement Learning on Roboti... | [arXiv](https://arxiv.org/abs/1707.08817) |
| 7 | Network Dissection: Quantifying Interpretability of Deep Visual Rep... | [arXiv](https://arxiv.org/abs/1704.05796) |
| 8 | Neural Discrete Representation Learning | [arXiv](https://arxiv.org/abs/1711.00937) |
| 9 | One-Shot Reinforcement Learning for Robot Navigation with Interacti... | [arXiv](https://arxiv.org/abs/1711.10137) |
| 10 | Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset | [arXiv](https://arxiv.org/abs/1705.07750) |
| 11 | Self-Normalizing Neural Networks | [arXiv](https://arxiv.org/abs/1706.02515) |
| 12 | Third-Person Imitation Learning | [arXiv](https://arxiv.org/abs/1703.01703) |

**2016**

| # | Title | Links |
|---|-------|-------|
| 1 | OctNet: Learning Deep 3D Representations at High Resolutions | [arXiv](https://arxiv.org/abs/1611.05009) |
| 2 | Perceptual Losses for Real-Time Style Transfer and Super-Resolution | [arXiv](https://arxiv.org/abs/1603.08155) |
| 3 | PointNet: Deep Learning on Point Sets for 3D Classification and Seg... | [arXiv](https://arxiv.org/abs/1612.00593) |
| 4 | Variational Graph Auto-Encoders | [arXiv](https://arxiv.org/abs/1611.07308) |

**2015**

| # | Title | Links |
|---|-------|-------|
| 1 | Model Predictive Path Integral Control using Covariance Variable Im... | [arXiv](https://arxiv.org/abs/1509.01149) |

