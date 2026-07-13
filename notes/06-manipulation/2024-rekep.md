# ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

## 元信息

- **标题**：ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation
- **作者**：Wenlong Huang, Chen Wang, Yunzhu Li, Ruohan Zhang, Li Fei-Fei
- **机构**：Stanford University
- **会议/期刊**：CoRL 2024
- **年份**：2024
- **arXiv**：https://arxiv.org/abs/2409.01652
- **项目页**：https://rekep-robot.github.io/
- **代码**：https://github.com/huangwl18/ReKep
- **主题标签**：`#关键点约束 #时空推理 #语言引导操作 #3D视觉 #灵巧手`

## 一句话总结

用视觉语言模型（VLM）在 3D 场景图上自动生成 relational keypoint constraints（ReKep），把复杂长程操作任务分解为可优化的子目标序列，在双臂/灵巧手系统上实现语言引导的精细操作。

## 研究问题

现有 VLA 方法直接把像素/语言映射到动作，缺乏显式的中间表示，导致：
1. 长程任务中误差累积，难以恢复
2. 语言指令到动作的映射是黑盒，不可解释
3. 对需要精确几何约束的任务（如"把杯子放在碟子正上方 2cm 处"）难以保证精度

如何把语言指令显式转换为可优化的 3D 几何约束序列？

## 核心方法

### 输入与输出

- 输入：当前 RGB-D 观测 + 语言指令（如"把茶包放进杯子并倒水"）
- 输出：末端执行器（或手指）的关键点目标位置序列 + 优化后的关节轨迹

### 方法概述

ReKep 定义了一组 relational keypoint constraints：在 3D 场景中选取语义关键点（如杯口中心、茶壶嘴、手指尖端），用 VLM（GPT-4V）根据语言指令自动生成这些关键点之间的时空约束（如"手指关键点应接触杯柄"、"茶壶嘴关键点应在杯口中心上方 5cm"）。这些约束构成一个因子图，通过非线性优化求解器实时优化机器人动作。

### 关键模块

- **关键点检测与跟踪**：DINOv2 + SAM 提取并跟踪场景中的语义关键点
- **VLM 约束生成**：GPT-4V 根据语言指令和关键点标注图，输出 Python 形式的约束函数
- **时空因子图优化**：把约束编码为优化目标，用 Levenberg-Marquardt 求解关节角序列

### 损失函数 / 目标

对于每个阶段 $k$ 的约束集合 $\mathcal{C}_k$，优化目标为：
$$\min_{\mathbf{q}} \sum_{c \in \mathcal{C}_k} w_c \cdot \|c(\mathbf{p}(\mathbf{q}))\|^2 + \lambda_{smooth} \|\Delta \mathbf{q}\|^2$$
其中 $\mathbf{p}(\mathbf{q})$ 是关键点的前向运动学位置，$w_c$ 是 VLM 分配的约束权重。

### 训练流程

- 无需策略网络训练
- VLM 作为 zero-shot 约束生成器（冻结）
- 关键点检测器使用预训练 DINOv2 + SAM（冻结）
- 在线优化求解关节轨迹

## 关键创新

1. 首次将 VLM 用于自动生成可执行的 3D 几何约束，把语言指令显式转换为优化问题
2. 关键点约束作为中间表示，天然支持长程任务分解与误差恢复

## 实验与结果

### 基准与指标

| 基准 | 指标 | 本文 | 最强基线 | 提升 |
| --- | --- | --- | --- | --- |
| 语言引导桌面整理 | 成功率 | 85% | VLA 端到端 55% | +30% |
| 双臂协作泡茶 | 成功率 | 75% | 无基线 | — |
| 灵巧手抓取不规则物体 | 成功率 | 70% | 启发式抓取 40% | +30% |

### 消融实验

- 去掉 VLM 约束生成改用人工预设约束，泛化到新任务成功率从 85% 降到 35%
- 去掉关键点跟踪改用静态检测，动态场景成功率下降 25%

### 失败案例

- VLM 对细粒度几何关系理解不足（如"把螺丝拧入螺纹孔"的旋入深度）
- 严重遮挡时关键点跟踪丢失，导致约束失效

## 局限与未来工作

- **作者承认的**：VLM 约束生成偶尔出现幻觉约束；优化求解频率 5-10Hz，实时性受限
- **读者发现的**：对透明/反光物体关键点检测不稳定；约束权重由 VLM 分配但无自适应调整机制

## 与本项目的关联

- **可借鉴**：ReKep 的关键点约束表示可直接对接 21 点视觉捕捉系统——人手关键点作为约束源，灵巧手关键点作为约束目标，用同样的因子图优化实现跨手型 retargeting
- **迁移障碍**：ReKep 假设已知场景 3D 结构，实时高斯泼溅重建的计算开销与 retargeting 的 p95≤40ms 要求冲突
- **待验证想法**：把 ReKep 的约束生成模块接入当前遥操作链路，操作员用语言描述目标（"把 cube 放到蓝色区域"），系统自动生成手指关键点约束并通过 IK 驱动 O10

## 复现笔记

- [x] 数据集：无需预训练，使用预训练 VLM 和检测器
- [ ] 关键超参：约束优化迭代次数 50，平滑权重 λ=0.1
- [ ] 踩坑记录：VLM API 调用延迟影响实时性；关键点跟踪对快速运动鲁棒性不足

## 引用

```bibtex
@inproceedings{huang2024rekep,
  title={ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation},
  author={Huang, Wenlong and Wang, Chen and Li, Yunzhu and Zhang, Ruohan and Fei-Fei, Li},
  booktitle={CoRL},
  year={2024}
}
```
