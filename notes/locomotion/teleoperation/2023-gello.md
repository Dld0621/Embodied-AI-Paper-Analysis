# GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators

## 元信息

- **标题**：GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators
- **作者**：Philip Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, Jimmy Yang, et al.
- **机构**：UC Berkeley, Stanford
- **会议/期刊**：CoRL 2023 Workshop
- **年份**：2023
- **arXiv**：https://arxiv.org/abs/2309.13099
- **项目页**：https://berkeleyopenarms.github.io/gello-site/
- **代码**：https://github.com/wuphilipp/gello_mechanical_design
- **主题标签**：`#遥操作 #低成本硬件 #模仿学习 #数据收集`

## 一句话总结

用 3D 打印零件 + 同构机械结构把廉价入门级机械臂改造成主从遥操作设备，单臂成本 $<\$300$，兼容多种从臂形态，实现高质量模仿学习数据采集。

## 研究问题

模仿学习需要大量高质量专家示教数据，但现有遥操作方案要么昂贵（$10K+$ 的工业主手），要么精度/直观性不足（VR 手柄、键盘鼠标）。如何以极低成本获得专业级遥操作体验，从而规模化采集机器人数据？

## 核心方法

### 输入与输出

- 输入：操作员直接握持同构主手，通过物理运动传递意图
- 输出：从臂关节角目标值（位置控制），经平滑滤波后下发

### 方法概述

GELLO 的核心是同构主从设计：主手与从臂具有相同的运动学结构（或近似结构），操作员直接握住主手末端，其运动通过连杆/同步带传递至编码器，经线性映射后直接驱动从臂。无需复杂的运动学解算，人类的空间运动直觉自然对应机器人运动。3D 打印零件使单臂主手成本压到 300 美元以内。

### 关键模块

- **同构机械主手**：根据从臂关节数定制 3D 打印连杆，保留相同自由度排布
- **低成本编码器**：使用 AMS AS5048A 磁编码器，单关节成本 $<\$5$
- **软件接口**：ROS2 节点读取编码器值，经平滑滤波后发布到从臂控制器

### 损失函数 / 目标

无学习成分，纯运动学映射：$q_{slave} = q_{master} + offset$，其中 offset 用于初始姿态对齐。

### 训练流程

无需训练。首次使用时进行零点标定，日常操作无需额外计算资源。

## 关键创新

1. 以机械同构性替代电子/算法补偿，把遥操作成本降低两个数量级
2. 开源完整机械设计文件，社区可快速适配新机器人平台

## 实验与结果

### 基准与指标

| 基准 | 指标 | 本文 | 最强基线 | 提升 |
| --- | --- | --- | --- | --- |
| 抽屉打开 | 成功率 | 95% | VR 手柄 70% | +25% |
| 杯子倒水 | 成功率 | 90% | VR 手柄 55% | +35% |
| 积木堆叠 | 成功率 | 85% | VR 手柄 60% | +25% |

### 消融实验

- 非同构主手（不同关节结构）成功率下降 20%，证明同构设计的重要性
- 去掉编码器平滑滤波，高频抖动导致抓取失败率上升

### 失败案例

- 主手与从臂工作空间差异大时，某些姿态无法复现
- 长时间操作（>30min）机械磨损导致零点漂移

## 局限与未来工作

- **作者承认的**：目前仅限位置控制，力反馈缺失；双臂协调操作需要两把主手
- **读者发现的**：3D 打印件强度有限，工业场景耐久性存疑；没有抓握力映射，精细力控任务受限

## 与本项目的关联

- **可借鉴**：GELLO 的同构遥操作思路可直接用于 O10 灵巧手的数据采集——设计一套与人手自由度对应的主手手套，通过 IMU/弯曲传感器实现低成本灵巧手遥操作
- **迁移障碍**：GELLO 面向关节空间同构，人手与 O10 灵巧手自由度差异大，需要额外的 retargeting 链路
- **待验证想法**：将 GELLO 的低成本编码器方案与 21 点视觉捕捉结合，主手用视觉估计人手姿态，从臂用 IK 驱动 O10，中间用 GELLO 的平滑滤波处理 jitter

## 复现笔记

- [x] 硬件：3D 打印件 + AS5048A 编码器 + Arduino/STM32 读取，总成本 ~$300/臂
- [ ] 关键超参：平滑滤波窗口 5-10 帧，控制频率 50Hz
- [ ] 踩坑记录：编码器零点标定需在每次上电后进行；同步带张力影响读数精度

## 引用

```bibtex
@article{wu2023gello,
  title={GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators},
  author={Wu, Philip and Shentu, Yide and Yi, Zhongke and Lin, Xingyu and Yang, Jimmy and and others},
  journal={arXiv preprint arXiv:2309.13099},
  year={2023}
}
```
