# ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

> Verified reading note · 已核验阅读笔记

## Metadata · 元信息

- **Authors**: Wenlong Huang, Chen Wang, Yunzhu Li, Ruohan Zhang, Li Fei-Fei
- **Venue**: CoRL 2024
- **Official record**: [PMLR 270](https://proceedings.mlr.press/v270/huang25g.html)
- **Track**: Foundation Models & VLA

PMLR published the proceedings in 2025; the conference edition represented here is CoRL 2024.

## Core idea · 核心思路

ReKep represents manipulation objectives as Python cost functions over 3D relational keypoints. Large vision and vision-language models propose keypoints and constraints from an RGB-D observation and a free-form instruction; a hierarchical optimizer then produces end-effector poses.

ReKep 将操作目标表示为作用于三维关系关键点的 Python 代价函数。大型视觉模型与视觉语言模型根据 RGB-D 观测和自然语言指令生成关键点与约束，再由分层优化器求解末端位姿。

## Pipeline · 流程

`language + RGB-D → keypoints → relational constraints → subgoal/path optimization → SE(3) end-effector actions → feedback`

## Reported evidence · 论文报告

- Implemented on a mobile single-arm platform and a stationary dual-arm platform.
- Demonstrations cover multi-stage, in-the-wild, bimanual, and reactive behaviors.
- The official abstract describes operation without task-specific data or environment models.

## Reading boundary · 阅读边界

- “No task-specific data” does not mean no pretrained-model dependency, calibration, perception error, or hand-engineered system component.
- ReKep is an optimization-based system using foundation models for constraint generation; it is not an end-to-end VLA policy.
- Quantitative success rates must remain attached to the paper's exact task suite and evaluation conditions.
