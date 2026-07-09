# Embodied AI Paper Analysis

> 系统化拆解具身智能前沿论文的阅读笔记仓库——从感知、操作、运动到世界模型，用统一框架沉淀每篇论文的问题、方法、创新与复现细节。

## 论文索引

共收录 **20 个主题**，所有论文按主题归档于 [`papers/README.md`](papers/README.md)，每个主题内按年份降序排列，每篇附 arXiv 链接与代码链接（如有）。

| 分类 | 主题 | 链接 |
| :--- | :--- | :--- |
| **感知与表示** | Foundation Models · 3D Vision & Perception · Gaussian Splatting · Motion Tracking · Tactile Sensing | [papers/README.md](papers/README.md#3d-vision--perception) |
| **操作与抓取** | Manipulation · Grasping · Retargeting | [papers/README.md](papers/README.md#manipulation) |
| **运动与导航** | Humanoid Robotics · Locomotion · Navigation | [papers/README.md](papers/README.md#humanoid-robotics) |
| **策略学习** | Diffusion Policy · Reinforcement Learning · VLA | [papers/README.md](papers/README.md#diffusion-policy) |
| **仿真与数据** | Simulation · Data Generation | [papers/README.md](papers/README.md#simulation) |
| **世界模型与生成** | World Models · Video Generation | [papers/README.md](papers/README.md#world-models) |
| **遥操作与硬件** | Teleoperation · Hardware | [papers/README.md](papers/README.md#teleoperation) |
| **其他** | Others · Uncategorized | [papers/README.md](papers/README.md#others) |

## 分析方法

每篇论文使用统一模板拆解（完整模板见 [`docs/paper-analysis-template.md`](docs/paper-analysis-template.md)），覆盖以下维度：

1. **元信息** — 标题、作者、会议、年份、arXiv 与项目页
2. **一句话总结** — 做了什么、凭什么有效
3. **研究问题** — 针对的痛点与现有方法的不足
4. **核心方法** — 输入输出、网络结构、损失函数、训练流程
5. **关键创新** — 相比前人真正新增的设计
6. **实验与结果** — 基准、指标、消融
7. **局限与未来工作** — 作者承认的与读者发现的
8. **可迁移性** — 能否复用到自己的系统中，具体卡在哪里
9. **复现笔记** — 关键超参、数据集、踩坑记录

> 阅读方法论与三遍阅读法的实践细节见 [`docs/reading-methodology.md`](docs/reading-methodology.md)。

## 仓库结构

```
Embodied-AI-Paper-Analysis/
├── papers/          # 论文索引（按主题分类，含 arXiv/代码链接）
├── notes/           # 论文分析笔记（21 个主题目录）
├── summaries/       # 单页速览（每篇一段话，用于快速检索）
├── docs/            # 分析模板、阅读方法、分类说明
├── scripts/         # 自动扫描生成索引的工具脚本
└── assets/          # 图表与示意图
```

笔记文件统一命名为 `YYYY-简短标题.md`（如 `2025-diffusion-policy.md`），同名论文以作者首字母区分。

## 阅读路线

围绕 **感知 → 操作 → 运动 → 策略 → 世界模型** 的能力栈，建议按以下顺序展开：

1. **打地基** — 基础模型与视觉表征 → 3D 视觉与高斯泼溅。理解智能体"看"到什么。
2. **进操作** — 操作与抓取 → 重定向与逆运动学 → 扩散策略。掌握灵巧手控制链路。
3. **上身体** — 人形机器人与运动控制。体会手-身协同的工程难点。
4. **学策略** — 强化学习 → VLA。理清从 RL 到大规模动作模型的演进。
5. **看未来** — 世界模型与视频生成。理解"预测即规划"范式。

> 遥操作与硬件贯穿 2-3 阶段，建议穿插阅读。

## 快速开始

```bash
git clone <your-repo-url>
cd Embodied-AI-Paper-Analysis

# 用模板新建一篇笔记
cp docs/paper-analysis-template.md notes/06-manipulation/2025-xxx.md

# 扫描所有笔记，更新索引
python scripts/generate_index.py
```

## 贡献

欢迎通过 Issue 或 PR 补充笔记、修正错误或扩展分类。新增笔记请遵循模板，详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## License

笔记与文档以 [CC BY-NC-SA 4.0](LICENSE) 协议开源，供学习与研究使用。论文版权归各自原作者所有，仓库不分发 PDF。
