# 接触方法、灵巧操作与重定向

<!-- catalog-freshness:start -->
> 文档同步 / Docs synced: **2026-11-16** · 顶会快照 / Conference: **2026-11-16** · arXiv 快照: **2026-11-16** · Asia/Hong_Kong
<!-- catalog-freshness:end -->

按可交叉的研究方向整理所有本体的接触方法，以及灵巧操作、重定向与示教迁移；覆盖机械臂、夹爪、多指手、足式／全身、物理人机交互、感知、仿真与规划，并单设相关对照／范围待定附录。

范围：会议快照 **2026-11-16**，arXiv 快照 **2026-11-16**；人工来源核查日期 **2026-11-16**。

当前共 **6,470 条规范标题去重阅读记录**，保留 **7,055 条会议／预印本来源记录**。这不是全网论文总数；不同标题仍可能属于同一工作。

其中会议层 **1,359 条来源记录**，arXiv 层 **5,696 条来源记录**；**581 条规范标题**同时出现在两层。两层来源数量可相加，标题阅读数量不可直接相加。

[完整会议目录](conference/README.md) · [完整 arXiv 目录](arxiv/README.md) · [在线筛选](https://dld0621.github.io/Embodied-AI-Paper-Analysis/dexterous-retargeting-contact.html)

[下载完整 JSON](../../../data/dexterous-retargeting-contact.json) · [下载完整 CSV](../../../data/dexterous-retargeting-contact.csv) · [回到全库分类](../../taxonomy/README.md)

## 阅读层级

| 层级 | 阅读记录 | 含义 |
|---|---:|---|
| 已核查 | 56 | 有明确的一手来源核查记录；仍须查看其审核基础与实验边界。 |
| 明确元数据候选 | 2,378 | 标题或已有分类明确命中相应领域，尚不等于人工确认主要贡献。 |
| 宽范围待审候选 | 4,036 | 摘要、一般力／力矩或关联语境命中，可能只是背景／比较，需进一步复核。 |

分组允许交叉，下面数量不可相加。一般抓取不自动等于接触力学；触觉不自动等于多指手；人手交互数据不自动等于机器人重定向。

## 按问题进入

**口径区别：**原有手部重定向索引（既有 Hand Retargeting 标签或手部重定向主类）为 **41 条来源记录／39 条规范标题去重记录**。本专题“重定向与示教迁移”分组的 **782 条**还包含全身／跨本体示教迁移和待审候选，**不等于 782 篇已核实手部重定向论文**；原有索引数量也不是语义完整性或全文审阅证明。

| 专题 | 阅读记录 | 范围 |
|---|---:|---|
| [重定向与示教迁移](retargeting/README.md) | 782 | 手部、全身与跨本体运动／接触／功能迁移；参考跟踪与示教迁移候选按实际贡献区分。 |
| [接触、力与阻抗控制](contact-control/README.md) | 4,507 | 接触维持、力／阻抗／导纳、柔顺与滑移控制候选；一般力／力矩线索也保留为待审，不能自动认定接触机制。 |
| [触觉、接触感知与交互重建](contact-perception/README.md) | 1,526 | 触觉、接触／力估计、传感器、手物及机器人环境交互重建；感知支撑与策略证据分开。 |
| [数据集、仿真与数据生成](datasets-simulation/README.md) | 589 | 接触与交互数据、接触仿真、仿真重放及示教生成；与实机迁移证据分开。 |
| [接触力学与物理可行性](contact-mechanics/README.md) | 791 | 接触动力学、摩擦、力闭合、接触扳手与稳定性；一般抓取关键词不自动等于接触力学。 |
| [残差方法与执行修正](residual/README.md) | 110 | 标明残差实际作用位置；动作／控制残差与特征适配器、模型误差或规划代价分开。 |
| [机械臂接触操作与装配](arm-contact/README.md) | 1,747 | 机械臂／夹爪接触操作、插入装配、打磨擦拭、工具使用和柔顺操作；不自动等于多指手实验。 |
| [接触规划、优化与 MPC](contact-planning/README.md) | 995 | 接触隐式规划、模式／序列选择、轨迹优化与接触感知预测控制。 |
| [足式与全身多接触](legged-contact/README.md) | 968 | 步行、足地接触、落足规划、全身及多接触协调；保留本体与任务边界。 |
| [物理人机交互与触觉交互](physical-hri/README.md) | 368 | 物理协作、交接、可穿戴／康复、触觉反馈与人机接触安全。 |
| [灵巧操作与手内任务](dexterous-manipulation/README.md) | 1,411 | 多指手、手内旋转／重定向、指步、灵巧抓取及其他明确灵巧操作；非手本体的灵巧任务不能冒充多指手成果。 |
| [相关对照与范围待定](related-comparisons/README.md) | 565 | 否定式对照、仅一般力／力矩或旧索引关联；未确认具体接触机制、重定向贡献或多指手任务。 |

## 优先阅读：已核查条目

| 论文 | 年份／优先来源 | 层级 | 关联专题 |
|---|---|---|---|
| [Active Tactile Exploration for Rigid Body Pose and Shape Estimation](https://arxiv.org/pdf/2510.13595) | 2026 · ICRA | 已核查 | 触觉、接触感知与交互重建、接触力学与物理可行性、机械臂接触操作与装配 |
| [AnyDexRT: Calibration-Efficient Dexterous Hand Retargeting with Few-Shot Human Guidance](https://arxiv.org/abs/2607.08341) | 2026 · arXiv | 已核查 | 重定向与示教迁移、触觉、接触感知与交互重建 |
| [C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video](https://arxiv.org/abs/2608.07045) | 2026 · arXiv | 已核查 | 重定向与示教迁移、触觉、接触感知与交互重建、残差方法与执行修正、灵巧操作与手内任务 |
| [CARD: Contact-Anchored Retargeting for Dexterous Manipulation](https://arxiv.org/abs/2610.36539) | 2026 · arXiv | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、触觉、接触感知与交互重建、灵巧操作与手内任务 |
| [Contact-Aware Imitation Learning Through Contact Factorization](https://arxiv.org/abs/2610.09533) | 2026 · arXiv | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、机械臂接触操作与装配 |
| [DexRemo: A Force-Sensing Hand Platform and Task Suite for Contact-Rich Removal Manipulation](https://arxiv.org/abs/2611.15981) | 2026 · arXiv | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、数据集、仿真与数据生成、灵巧操作与手内任务 |
| [Dexterous Robot Manipulation from Human Demonstrations via Contact-Anchored Retargeting and Residual Policy Learning](https://arxiv.org/abs/2609.24093) | 2026 · arXiv | 已核查 | 重定向与示教迁移、接触力学与物理可行性、残差方法与执行修正、灵巧操作与手内任务 |
| [FAR-Dex: Few-shot Data Augmentation and Adaptive Residual Policy Refinement for Dexterous Manipulation](https://arxiv.org/pdf/2603.10451) | 2026 · ICRA | 已核查 | 接触、力与阻抗控制、数据集、仿真与数据生成、残差方法与执行修正、灵巧操作与手内任务 |
| [FlashDexRetarget: Accelerating Dexterous Manipulation Data Generation through Multi-Motion Retargeting](https://arxiv.org/abs/2610.01849) | 2026 · arXiv | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、灵巧操作与手内任务 |
| [IORA: Irregular Object Immobilization under Restricted Actuation](https://arxiv.org/abs/2610.30969) | 2026 · arXiv | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、灵巧操作与手内任务 |
| [Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration](https://arxiv.org/abs/2607.00033) | 2026 · arXiv | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、接触力学与物理可行性、灵巧操作与手内任务 |
| [TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real](https://arxiv.org/abs/2611.17619) | 2026 · arXiv | 已核查 | 触觉、接触感知与交互重建、数据集、仿真与数据生成 |
| [ContactDexNet: Multi-fingered Robotic Hand Grasping in Cluttered Environments through Hand-Object Contact Semantic Mapping](https://arxiv.org/pdf/2404.08844) | 2025 · IROS | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、灵巧操作与手内任务 |
| [DexFlow: A Unified Approach for Dexterous Hand Pose Retargeting and Interaction](https://arxiv.org/abs/2505.01083) | 2025 · arXiv | 已核查 | 重定向与示教迁移、触觉、接触感知与交互重建 |
| [DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2505.24853) | 2025 · arXiv | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、灵巧操作与手内任务 |
| [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](https://arxiv.org/pdf/2410.24185) | 2025 · ICRA | 已核查 | 数据集、仿真与数据生成、灵巧操作与手内任务 |
| [Dexterous Contact-Rich Manipulation via the Contact Trust Region](https://arxiv.org/abs/2505.02291) | 2025 · arXiv | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、接触规划、优化与 MPC、灵巧操作与手内任务 |
| [DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References](https://arxiv.org/abs/2502.09614) | 2025 · ICLR | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、灵巧操作与手内任务 |
| [Efficient Residual Learning with Mixture-of-Experts for Universal Dexterous Grasping](https://arxiv.org/abs/2410.02475) | 2025 · ICLR | 已核查 | 接触、力与阻抗控制、残差方法与执行修正、灵巧操作与手内任务 |
| [ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation](https://arxiv.org/pdf/2410.07554) | 2025 · ICRA | 已核查 | 接触、力与阻抗控制、数据集、仿真与数据生成、机械臂接触操作与装配 |
| [Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm](https://arxiv.org/abs/2503.07541) | 2025 · IROS | 已核查 | 重定向与示教迁移 |
| [Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?](https://arxiv.org/pdf/2411.06542) | 2025 · ICRA | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、接触规划、优化与 MPC |
| [Learning In-Hand Translation Using Tactile Skin with Shear and Normal Force Sensing](https://arxiv.org/pdf/2407.07885) | 2025 · ICRA | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、灵巧操作与手内任务 |
| [ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning](https://arxiv.org/abs/2503.21860) | 2025 · CVPR | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、残差方法与执行修正、灵巧操作与手内任务 |
| [PolyTouch: A Robust Multi-Modal Tactile Sensor for Contact-Rich Manipulation Using Tactile-Diffusion Policies](https://arxiv.org/pdf/2504.19341) | 2025 · ICRA | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、机械臂接触操作与装配 |
| [Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC](https://arxiv.org/abs/2510.19974) | 2025 · arXiv | 已核查 | 接触、力与阻抗控制、机械臂接触操作与装配、接触规划、优化与 MPC |
| [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](https://www.roboticsproceedings.org/rss21/p052.html) | 2025 · RSS | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、机械臂接触操作与装配 |
| [REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly](https://arxiv.org/abs/2502.05086) | 2025 · arXiv | 已核查 | 触觉、接触感知与交互重建、数据集、仿真与数据生成、机械臂接触操作与装配 |
| [SPIDER: Scalable Physics-Informed Dexterous Retargeting](https://arxiv.org/abs/2511.09484) | 2025 · arXiv | 已核查 | 重定向与示教迁移、数据集、仿真与数据生成、接触力学与物理可行性、灵巧操作与手内任务 |
| [Trajectory Optimization for In-Hand Manipulation with Tactile Force Control](https://arxiv.org/pdf/2503.08222) | 2025 · IROS | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、灵巧操作与手内任务 |
| [A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand](https://arxiv.org/abs/2409.12339) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、灵巧操作与手内任务 |
| [APriCoT: Action Primitives based on Contact-state Transition for In-Hand Tool Manipulation](https://arxiv.org/abs/2407.11436) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、灵巧操作与手内任务 |
| [Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation](https://arxiv.org/abs/2408.07855) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、灵巧操作与手内任务 |
| [Contact-Implicit Model Predictive Control for Dexterous In-hand Manipulation: A Long-Horizon and Robust Approach](https://arxiv.org/pdf/2402.18897) | 2024 · IROS | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、接触规划、优化与 MPC、灵巧操作与手内任务 |
| [ContactSDF: Signed Distance Functions as Multi-Contact Models for Dexterous Manipulation](https://arxiv.org/abs/2408.09612) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、接触力学与物理可行性、灵巧操作与手内任务 |
| [CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation](https://arxiv.org/pdf/2402.14795) | 2024 · CVPR | 已核查 | 重定向与示教迁移、数据集、仿真与数据生成、灵巧操作与手内任务 |
| [DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788) | 2024 · RSS | 已核查 | 重定向与示教迁移、数据集、仿真与数据生成、灵巧操作与手内任务 |
| [DexTouch: Learning to Seek and Manipulate Objects with Tactile Dexterity](https://arxiv.org/abs/2401.12496) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、灵巧操作与手内任务 |
| [DIFFTACTILE: A Physics-based Differentiable Tactile Simulator for Contact-rich Robotic Manipulation](https://arxiv.org/abs/2403.08716) | 2024 · ICLR | 已核查 | 触觉、接触感知与交互重建、数据集、仿真与数据生成、接触力学与物理可行性 |
| [Efficient and Safe Contact-rich pHRI via Subtask Detection and Motion Estimation using Deep Learning](https://arxiv.org/abs/2407.14161) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、机械臂接触操作与装配、物理人机交互与触觉交互 |
| [Explicit Contact Optimization in Whole-Body Contact-Rich Manipulation](https://arxiv.org/abs/2408.15726) | 2024 · arXiv | 已核查 | 接触力学与物理可行性、接触规划、优化与 MPC、足式与全身多接触 |
| [FoAR: Force-Aware Reactive Policy for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2411.15753) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、触觉、接触感知与交互重建、机械臂接触操作与装配 |
| [FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty](https://arxiv.org/abs/2408.04587) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、数据集、仿真与数据生成、机械臂接触操作与装配 |
| [HOT3D: Hand and Object Tracking in 3D from Egocentric Multi-View Videos](https://arxiv.org/abs/2411.19167) | 2024 · arXiv | 已核查 | 触觉、接触感知与交互重建、数据集、仿真与数据生成 |
| [Just Add Force for Contact-Rich Robot Policies](https://arxiv.org/abs/2410.13124) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、数据集、仿真与数据生成、机械臂接触操作与装配 |
| [MimicTouch: Leveraging Multi-modal Human Tactile Demonstrations for Contact-rich Manipulation](https://arxiv.org/abs/2310.16917) | 2024 · CoRL | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、触觉、接触感知与交互重建、残差方法与执行修正、机械臂接触操作与装配 |
| [ResPilot: Teleoperated Finger Gaiting via Gaussian Process Residual Learning](https://arxiv.org/abs/2409.09140) | 2024 · CoRL | 已核查 | 重定向与示教迁移、接触、力与阻抗控制、残差方法与执行修正、灵巧操作与手内任务 |
| [RESPRECT: Speeding-up Multi-fingered Grasping with Residual Reinforcement Learning](https://arxiv.org/abs/2401.14858) | 2024 · arXiv | 已核查 | 接触、力与阻抗控制、残差方法与执行修正、灵巧操作与手内任务 |
| [Towards Tight Convex Relaxations for Contact-Rich Manipulation](https://arxiv.org/abs/2402.10312) | 2024 · RSS | 已核查 | 接触力学与物理可行性、机械臂接触操作与装配、接触规划、优化与 MPC |
| [Contact-Implicit Model Predictive Control: Controlling Diverse Quadruped Motions Without Pre-Planned Contact Modes or Trajectories](https://arxiv.org/abs/2312.08961) | 2023 · arXiv | 已核查 | 接触力学与物理可行性、接触规划、优化与 MPC、足式与全身多接触 |
| [Efficient Sim-to-real Transfer of Contact-Rich Manipulation Skills with Online Admittance Residual Learning](https://arxiv.org/abs/2310.10509) | 2023 · CoRL | 已核查 | 接触、力与阻抗控制、残差方法与执行修正、机械臂接触操作与装配 |
| [Fast-Grasp'D: Dexterous Multi-finger Grasp Generation Through Differentiable Simulation](https://arxiv.org/pdf/2306.08132) | 2023 · ICRA | 已核查 | 数据集、仿真与数据生成、接触力学与物理可行性、灵巧操作与手内任务 |
| [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](https://arxiv.org/abs/2305.17110) | 2023 · RSS | 已核查 | 接触、力与阻抗控制、数据集、仿真与数据生成、机械臂接触操作与装配 |
| [DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video](https://arxiv.org/abs/2202.00164) | 2022 · CoRL | 已核查 | 重定向与示教迁移、灵巧操作与手内任务 |
| [Grasp'D: Differentiable Contact-rich Grasp Synthesis for Multi-fingered Hands](https://arxiv.org/abs/2208.12250) | 2022 · ECCV | 已核查 | 数据集、仿真与数据生成、接触力学与物理可行性、灵巧操作与手内任务 |
| [Learning Preconditions of Hybrid Force-Velocity Controllers for Contact-Rich Manipulation](https://arxiv.org/pdf/2206.12728) | 2022 · CoRL | 已核查 | 接触、力与阻抗控制、机械臂接触操作与装配、接触规划、优化与 MPC |

## 完整候选目录

以下分页保留全部宽范围待审候选；每页最多 100 条，JSON 和 CSV 提供逐条证据与全部来源。

- [完整清单 1：1–100](all-001.md)
- [完整清单 2：101–200](all-002.md)
- [完整清单 3：201–300](all-003.md)
- [完整清单 4：301–400](all-004.md)
- [完整清单 5：401–500](all-005.md)
- [完整清单 6：501–600](all-006.md)
- [完整清单 7：601–700](all-007.md)
- [完整清单 8：701–800](all-008.md)
- [完整清单 9：801–900](all-009.md)
- [完整清单 10：901–1000](all-010.md)
- [完整清单 11：1001–1100](all-011.md)
- [完整清单 12：1101–1200](all-012.md)
- [完整清单 13：1201–1300](all-013.md)
- [完整清单 14：1301–1400](all-014.md)
- [完整清单 15：1401–1500](all-015.md)
- [完整清单 16：1501–1600](all-016.md)
- [完整清单 17：1601–1700](all-017.md)
- [完整清单 18：1701–1800](all-018.md)
- [完整清单 19：1801–1900](all-019.md)
- [完整清单 20：1901–2000](all-020.md)
- [完整清单 21：2001–2100](all-021.md)
- [完整清单 22：2101–2200](all-022.md)
- [完整清单 23：2201–2300](all-023.md)
- [完整清单 24：2301–2400](all-024.md)
- [完整清单 25：2401–2500](all-025.md)
- [完整清单 26：2501–2600](all-026.md)
- [完整清单 27：2601–2700](all-027.md)
- [完整清单 28：2701–2800](all-028.md)
- [完整清单 29：2801–2900](all-029.md)
- [完整清单 30：2901–3000](all-030.md)
- [完整清单 31：3001–3100](all-031.md)
- [完整清单 32：3101–3200](all-032.md)
- [完整清单 33：3201–3300](all-033.md)
- [完整清单 34：3301–3400](all-034.md)
- [完整清单 35：3401–3500](all-035.md)
- [完整清单 36：3501–3600](all-036.md)
- [完整清单 37：3601–3700](all-037.md)
- [完整清单 38：3701–3800](all-038.md)
- [完整清单 39：3801–3900](all-039.md)
- [完整清单 40：3901–4000](all-040.md)
- [完整清单 41：4001–4100](all-041.md)
- [完整清单 42：4101–4200](all-042.md)
- [完整清单 43：4201–4300](all-043.md)
- [完整清单 44：4301–4400](all-044.md)
- [完整清单 45：4401–4500](all-045.md)
- [完整清单 46：4501–4600](all-046.md)
- [完整清单 47：4601–4700](all-047.md)
- [完整清单 48：4701–4800](all-048.md)
- [完整清单 49：4801–4900](all-049.md)
- [完整清单 50：4901–5000](all-050.md)
- [完整清单 51：5001–5100](all-051.md)
- [完整清单 52：5101–5200](all-052.md)
- [完整清单 53：5201–5300](all-053.md)
- [完整清单 54：5301–5400](all-054.md)
- [完整清单 55：5401–5500](all-055.md)
- [完整清单 56：5501–5600](all-056.md)
- [完整清单 57：5601–5700](all-057.md)
- [完整清单 58：5701–5800](all-058.md)
- [完整清单 59：5801–5900](all-059.md)
- [完整清单 60：5901–6000](all-060.md)
- [完整清单 61：6001–6100](all-061.md)
- [完整清单 62：6101–6200](all-062.md)
- [完整清单 63：6201–6300](all-063.md)
- [完整清单 64：6301–6400](all-064.md)
- [完整清单 65：6401–6470](all-065.md)

## 库外经典与补充来源

下面是独立补充表，不进入上述库内候选、来源或分组数量；原始发表年份保留，不冒充本次窗口新增。

| 论文 | 原始年份 | 用途与边界 |
|---|---:|---|
| [GRAB: A Dataset of Whole-Body Human Grasping of Objects](https://arxiv.org/abs/2008.11200) | 2020 | 全身动捕拟合的人手与物体网格序列，支持接触/功能示范研究。 网格计算接触不是力传感真值；旧年/cs.CV 基础参考，不计入当前三年 cs.RO 来源层。 |
| [OakInk: A Large-scale Knowledge Repository for Understanding Hand-Object Interaction](https://arxiv.org/abs/2203.15709) | 2022 | 提供物体 affordance 知识及人手交互图像/形状数据，关联抓取与重建。 并非机器人控制示范或力真值；标题不应误配数学论文2203.15715。 |
| [OAKINK2: A Dataset of Bimanual Hands-Object Manipulation in Complex Task Completion](https://arxiv.org/abs/2403.19417) | 2024 | 以 affordance、primitive、complex task 层次组织双手复杂操作及多物体位姿。 人类位姿与任务结构不等于机器人动作/力真值；当前源库未收录，独立补充。 |
| [DexYCB: A Benchmark for Capturing Hand Grasping of Objects](https://arxiv.org/abs/2104.04631) | 2021 | 手与物体位姿、检测及安全交接抓取的视觉评测数据。 不是完整动作控制或接触力数据集；旧年/cs.CV 独立基础参考。 |
| [ContactOpt: Optimizing Contact to Improve Grasps](https://arxiv.org/abs/2104.07267) | 2021 | 预测期望接触并用可微接触模型优化手姿，可借鉴接触损失设计。 为近似人手软组织，模型允许/鼓励一定网格穿透；不可直接当机器人无穿透或物理可行性保证。 |
| [ContactPose: A Dataset of Grasps with Object Contact and Hand Pose](https://arxiv.org/abs/2007.09545) | 2020 | 将物体接触、手姿、物体姿态与 RGB-D 图像配对，适合接触推断监督。 接触区域标注不是法向/切向接触力真值；静态抓姿样本不等于动态重定向示范。 |
| [ARCTIC: A Dataset for Dexterous Bimanual Hand-Object Manipulation](https://arxiv.org/abs/2204.13662) | 2022 | 同步双手与关节物体网格及动态接触信息，适合复杂双手交互参考。 arXiv 初稿2022、CVPR论文2023；几何接触/交互距离不是实测接触力。 |
| [TACO: Benchmarking Generalizable Bimanual Tool-ACtion-Object Understanding](https://arxiv.org/abs/2401.08399) | 2024 | 多视角及动捕构成双手、工具和物体组合数据，支持动作、预测与协同抓取评测。 必须按全标题/ID区分同名触觉压缩、SLAM、四旋翼 TACO；不是这些同名记录。 |
| [DexPilot: Vision Based Teleoperation of Dexterous Robotic Hand-Arm System](https://arxiv.org/abs/1910.03135) | 2019 | 视觉观测裸手并控制多指手臂系统的遥操作基础，连接手姿态映射、任务执行和示范采集。 arXiv首发2019；作者机构页与IEEE记录为ICRA2020，均在本次滚动窗口外。遥操作系统不是自主策略学习结果。 |
| [DexMV: Imitation Learning for Dexterous Manipulation from Human Videos](https://arxiv.org/abs/2108.05877) | 2021 | 从视频估计人手与物体三维姿态，再将人类运动转为机器人示范并比较模仿学习算法。 arXiv首发2021；作者项目页标注ECCV2022。模拟任务收益不等于不经适配即可实机部署。此工作未被当前来源检索规则收入，作为独立补充。 |
| [Compliance and Force Control for Computer-Controlled Manipulators](https://publications.ri.cmu.edu/compliance-and-force-control-for-computer-controlled-manipulators) | 1981 | Mason 将任务几何约束、柔顺运动与主动控制形式化，是理解接触操作约束方向和力位控制语义的基础。 IEEE Transactions on Systems, Man, and Cybernetics 1981 期刊基础；不纳入当前会议/近三年 arXiv 来源行数，也不是神经重定向。 |
| [Hybrid Position/Force Control of Manipulators](https://fab.cba.mit.edu/classes/865.15/classes/measurement/hybrid-position-force.pdf) | 1981 | Raibert 与 Craig 在任务坐标系内结合位置与力反馈，处理同时存在的位置和力轨迹约束。 ASME Journal of Dynamic Systems, Measurement, and Control 1981 期刊；混合指受约束方向的控制分工，不等于训练时混合策略专家。 |
| [Impedance Control: An Approach to Manipulation: Part I—Theory](https://newmanlab.mit.edu/wp-content/uploads/2017/09/1985-impedance-control-an-approach-to-manipulation-part-I-theory.pdf) | 1985 | Hogan 从机械耦合解释为何应控制力与运动的动态关系，并区分阻抗与导纳；是学习柔顺、刚度和交互稳定性的基础。 ASME 1985 理论篇；动态关系不是单纯力跟踪，阻抗与导纳不能当同义词。此条不计入当前来源快照。 |
| [MuJoCo: A physics engine for model-based control](https://roboti.us/lab/papers/TodorovIROS12.pdf) | 2012 | Todorov、Erez、Tassa 为模型控制设计多关节接触物理引擎，使用广义坐标动力学与速度步进式接触求解。 IROS2012 基础论文；求解器中的接触近似及参数需明确，仿真稳定不等于机器人实机物理正确。 |
| [A Direct Method for Trajectory Optimization of Rigid Bodies Through Contact](https://dair.seas.upenn.edu/assets/pdf/Posa2014.pdf) | 2014 | Posa、Cantu、Tedrake 用互补约束同时优化状态、控制与接触力，避免预先指定接触模式顺序。 IJRR2014 期刊版；作者稿日期为2013、WAFR前身为2012，应区分版本。属于局部非线性优化，不保证任意场景全局最优。 |
| [Learning to Slide Unknown Objects with Differentiable Physics Simulations](https://www.roboticsproceedings.org/rss16/p099.html) | 2020 | 用可微物理的预测误差梯度辨识未知物体质量分布与摩擦，并规划满足稳定约束的推动。 RSS2020 官方会议页；平面推动与系统辨识不能直接泛化为灵巧手全部接触模式。窗口外经典单列。 |

## 筛选与证据边界

- 仅在当前会议与 arXiv 两层元数据中按规范完整词组筛选，或按确切标题／arXiv ID 纳入有来源的人工例外；不按 SPIDER、TACO 等裸缩写子串匹配。
- 同一规范标题合并为阅读条目，但会议与预印本来源记录全部保留。标题去重不是严格论文实体识别，也不证明 arXiv 版本获得会议录用。
- 全身／四足、双指夹爪、机械臂装配、连续体接触模型等属于接触研究覆盖范围，但不能自动成为多指手实验成果；本体与技术贡献分别核查。
- 力／力矩词组不自动证明接触力学贡献；否定式或比较语境仍可能作为待审相关文献保留，不能据此认定论文采用被否定的机制。
- 残差适配器／网络、规划代价和动作残差属于不同作用位置；未核查条目不能仅因 residual 一词认定为动作残差。
- 自动候选可能漏检或误检；已核查只对应各条所列的标题／摘要、局部全文或其他来源核对，不代表全库全文精读、成功复现或实机验证。
