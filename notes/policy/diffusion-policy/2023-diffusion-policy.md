# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

## 元信息

- **标题**：Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- **作者**：Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song
- **机构**：Columbia University, MIT, Toyota Research Institute
- **会议/期刊**：RSS 2023
- **年份**：2023
- **arXiv**：https://arxiv.org/abs/2303.04137
- **项目页**：https://diffusion-policy.cs.columbia.edu/
- **代码**：https://github.com/real-stanford/diffusion_policy
- **主题标签**：`#扩散策略 #visuomotor #操作`

## 一句话总结

把去噪扩散模型用作 visuomotor 策略的动作生成器，以"预测未来一段动作序列"替代"预测单步动作"，从而获得多模态动作分布表达力与训练稳定性。

## 研究问题

模仿学习里最常用的行为克隆假设动作分布是单峰的，但真实操作任务的动作天然多模态——同一个目标往往有多条可行轨迹。直接回归单步动作会被多模态平均化拖垮，而高斯混合等显式多模态模型又难训练、易不稳定。本文要解决的是：如何让策略网络稳定地表达多模态动作分布。

## 核心方法

### 输入与输出

- 输入：当前观测（RGB-D 图像或点云）+ 本体感知（关节角/位姿）
- 输出：未来一段动作序列（receding horizon），而非单步动作

### 方法概述

策略不再回归动作，而是去噪一个随机噪声，逐步生成一段动作序列。条件信号是当前观测经视觉编码器提取的特征。每一步执行序列的第一个动作，随后用新观测重新生成，形成 receding horizon 控制。两种变体：基于 CNN 的 1D 时序卷积版本（速度快）与基于 Transformer 的版本（性能略好）。

### 关键模块

- **视觉编码器**：ResNet-18 提取图像特征，冻结预训练权重以减少过拟合
- **条件注入**：观测特征通过 cross-attention 或 FiLM 注入去噪网络
- **receding horizon**：预测未来 T_p 步，仅执行前 T_a 步，平衡规划范围与反应速度

### 损失函数 / 目标

去噪扩散的标准 ELBO 目标：在加噪动作序列上预测所加噪声，等价于分数匹配。

### 训练流程

离线行为克隆：从专家示教数据集采样 (观测, 动作序列) 对，对动作序列加噪训练去噪网络。无需在线交互。

## 关键创新

1. 把"动作"建模为扩散对象而非回归目标，天然支持多模态分布，无需显式混合模型
2. 预测动作序列而非单步，隐式引入轨迹平滑性与时序一致性，减少高频抖动

## 实验与结果

### 基准与指标

| 基准 | 指标 | 本文 | 最强基线 | 提升 |
| --- | --- | --- | --- | --- |
| Robomimic / PushT | 成功率 | 显著领先 | IBC / BCRNN | 多任务平均提升 20%+ |

### 消融实验

去掉动作序列预测改为单步，成功率明显下降，说明 receding horizon 是关键；视觉编码器冻结比端到端微调更稳，说明小数据下预训练特征更重要。

### 失败案例

扩散步数过少导致动作质量退化；观测延迟大时 receding horizon 的开环段会累积误差。

## 局限与未来工作

- **作者承认的**：推理速度受扩散步数制约，实时性在低成本硬件上吃紧
- **读者发现的**：对观测频率敏感，频率不稳时序列对齐困难；多模态优势在窄分布任务上体现不明显

## 与本项目的关联

- **可借鉴**：把"序列预测 + receding horizon"思路用于灵巧手遥操作的轨迹平滑，缓解 21 点 landmark 跳变导致的动作抖动；扩散作为动作滤波器可能比 Savitzky-Golay 更能保留多模态手势
- **迁移障碍**：扩散步数与实时性矛盾，当前 retargeting 需 p95≤40ms，需用 DDIM 把步数压到 5 步以内并验证精度损失
- **待验证想法**：用扩散策略替代现有 IK 优化后的直接角度输出，在指尖向量层面做去噪，看能否同时解决拇指 MCP 校准与四指过驱动

## 复现笔记

- [x] 数据集：PushT、Robomimic（官方提供，可直接下载）
- [ ] 关键超参：预测步数 T_p=16，执行步数 T_a=8，扩散步数 100（推理可用 DDIM 降至 10）
- [ ] 踩坑记录：待复现

## 引用

```bibtex
@inproceedings{chi2023diffusion,
  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
  booktitle={RSS},
  year={2023}
}
```
