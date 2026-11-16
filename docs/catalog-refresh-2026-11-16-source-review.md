# 重点论文来源与分类审查 · 2026-11-16

本次核对 11 条贡献分类，并复查 VOKE 修订版。范围是**标题、摘要与 TouchTwin 局部全文**，不等于逐篇完整精读或复现实验。下表日期是 arXiv 提交历史中的 **UTC 原始提交日**；11 月 16 日是检索核对日，不能把这些论文都称为当天新发表。

完整标题、版本日期、分类理由和证据边界见[同日来源审查 JSON](../data/catalog-refresh-2026-11-16-source-review.json)。下表使用缩写；完整三级名称以 JSON 为准。

| 一手来源 / 原始提交日 | 主贡献与分类落点 |
|---|---|
| [TouchTwin](https://arxiv.org/abs/2611.17619) · 11/13 | 数据 → 合成增强 → 仿真轨迹生成 |
| [IORA](https://arxiv.org/abs/2610.30969) · 10/22 | 灵巧手 → 多指抓控 → 多指协同与抓取生成 |
| [Objectives as Policies](https://arxiv.org/abs/2611.18298) · 11/13 | 世界模型与规划 → 模型决策 → MPC |
| [Learning Latent Goal Costs](https://arxiv.org/abs/2611.17529) · 11/12 | 世界模型与规划 → 模型决策 → 世界模型规划 |
| [LASR](https://arxiv.org/abs/2611.17775) · 11/13 | 数据与评测 → 实验方法 → 可复现性与统计比较 |
| [Agentic-Teacher](https://arxiv.org/abs/2611.17394) · 11/12 | 数据 → 合成增强 → 仿真轨迹生成 |
| [ESI](https://arxiv.org/abs/2611.18176) · 11/13 | 策略学习 → VLA → 分层策略与专家混合 |
| [PEAR / Robot-use RL](https://arxiv.org/abs/2611.18562) · 11/13 | 策略学习 → 强化学习 → 在线强化学习 |
| [VLA Life-Cycle Survey](https://arxiv.org/abs/2611.18372) · 11/13 | 策略学习 → VLA → 视觉语言动作建模 |
| [Contact-rich Insertion Representations](https://arxiv.org/abs/2611.17631) · 11/13 | 数据与评测 → 实验方法 → 泛化与鲁棒性评估 |
| [Continuum Robot Frictional Contact](https://arxiv.org/abs/2611.18546) · 11/13 | 世界模型与规划 → 动力学建模 → 物体与接触动力学 |

[VOKE](https://arxiv.org/abs/2611.16423) 原始提交于 11/12，v2 更新于 11/13；继续归入“感知 → 物体与交互感知 → 6D 位姿与跟踪”，不将下游操作实验误作重定向贡献。IORA 的 v2 同样更新于 11/13，保留 10/22 原始日期。

需要区分的证据：

- **TouchTwin** 用实测触觉驱动人手模型重放及数据增强；仿真策略和真实接触预测，不等于已验证机器人手重定向或实机策略迁移。
- **IORA** 研究受限驱动条件下的支撑感知抓取合成，修正原“执行器设计”分类。
- **两篇残差工作**调整潜在表征或规划代价，不等于给灵巧手动作叠加残差控制。
- **期刊与会议分层**：连续体摩擦论文和既有 [DexRemo](https://arxiv.org/abs/2611.15981) 的 arXiv 页面分别声明 IJRR、T-RO 接收；这是作者提供的期刊状态，未据此增加十会议普查层记录，也未冒充本次独立出版方核验。

本审查不证明全库分类正确或全站检索无遗漏；来源快照日期与收录数量须由实际抓取记录另行确认。
