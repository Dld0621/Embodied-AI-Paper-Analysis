# GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators

> Verified reading note · 已核验阅读笔记

## Metadata · 元信息

- **Authors**: Philipp Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, Pieter Abbeel
- **Formal venue**: IROS 2024
- **DOI**: [10.1109/IROS58592.2024.10801581](https://doi.org/10.1109/IROS58592.2024.10801581)
- **Preprint**: [arXiv:2309.13037](https://arxiv.org/abs/2309.13037)
- **Project**: [wuphilipp.github.io/gello](https://wuphilipp.github.io/gello/)
- **Track**: Dexterity & Teleoperation

The filename keeps the 2023 preprint year for stable links; the peer-reviewed conference record is IROS 2024.

## Core idea · 核心思路

GELLO builds a low-cost leader device with the same kinematic structure as the target robot arm. The operator directly moves this physical replica, and its joint configuration maps naturally to the follower robot.

GELLO 为目标机械臂构建同构、低成本的主端设备。操作者直接移动物理主端，其关节配置自然映射到从端机器人，从而降低遥操作数据采集门槛。

## Pipeline · 流程

`human moves kinematic replica → joint sensing and calibration → follower joint command → demonstration recording`

## Reported evidence · 论文报告

- The paper describes designs for Franka, UR5, and xArm.
- The reported bill of materials is below USD 300 per device.
- A user study compares GELLO with lower-cost alternatives such as VR controllers and 3D SpaceMouse devices.
- Demonstrations include bimanual and contact-rich tasks.

## Reading boundary · 阅读边界

- The evidence concerns teleoperation quality and demonstration collection, not autonomous task success by itself.
- Similar kinematics reduce mapping complexity but do not remove calibration, safety, or embodiment-specific control constraints.
- Exact user-study results should be quoted only from the paper tables, with task and participant counts.
