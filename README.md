# Embodied AI Paper Analysis

> 一个系统化拆解具身智能（Embodied AI）前沿论文的阅读笔记仓库：从感知、操作、运动到世界模型，用统一的框架沉淀每一篇论文的问题、方法、创新与可复现细节。

具身智能研究正以前所未有的速度膨胀——视觉-语言-动作模型、人形机器人全身控制、灵巧手抓取、可微仿真与世界模型彼此交织，单篇论文往往横跨多个子领域。仅靠逐篇通读很难建立结构化的认知，读完即忘是常态。本仓库的目标是为这个难题提供一个落地的解法：用一套固定的分析框架逐篇拆解论文，再把拆解结果按主题归档，最终拼出一张可检索、可对照、可复用的知识地图。

## 论文索引

本仓库收录 **970 篇** 具身智能领域论文，所有论文已整理并去重，按**七条主线**分类：

| 主线 | 主题 | 论文数 |
| --- | --- | --- |
| **感知与表示** | [基础模型](papers/README.md#foundation-models) | 20 |
| | [3D 视觉与感知](papers/README.md#3d-vision--perception) | 68 |
| | [高斯泼溅](papers/README.md#gaussian-splatting) | 17 |
| | [运动追踪](papers/README.md#motion-tracking) | 9 |
| | [触觉感知](papers/README.md#tactile-sensing) | 31 |
| **操作与抓取** | [操作](papers/README.md#manipulation) | 64 |
| | [抓取](papers/README.md#grasping) | 26 |
| | [重定向/运动映射](papers/README.md#retargeting) | 2 |
| **运动与导航** | [人形机器人](papers/README.md#humanoid-robotics) | 30 |
| | [运动控制](papers/README.md#locomotion) | 20 |
| | [导航](papers/README.md#navigation) | 9 |
| **策略学习** | [扩散策略](papers/README.md#diffusion-policy) | 60 |
| | [强化学习](papers/README.md#reinforcement-learning) | 93 |
| | [VLA (视觉-语言-动作)](papers/README.md#vla-vision-language-action) | 4 |
| **仿真与数据** | [仿真](papers/README.md#simulation) | 14 |
| | [数据生成](papers/README.md#data-generation) | 17 |
| **世界模型与生成** | [世界模型](papers/README.md#world-models) | 5 |
| | [视频生成](papers/README.md#video-generation) | 10 |
| **遥操作与硬件** | [遥操作](papers/README.md#teleoperation) | 12 |
| | [硬件](papers/README.md#hardware) | 16 |
| **其他** | [Uncategorized](papers/README.md#uncategorized) | 455 |

**完整索引：[papers/README.md](papers/README.md)** — 按主题组织，每个主题内按年份降序排列，每篇带 arXiv 链接和 GitHub 代码链接（如果能找到）。

## 这个仓库适合谁

- 正在做具身智能方向研究、需要快速建立领域全局观的研究者与研究生
- 希望把"读过"变成"读懂并能用上"的工程师
- 想要在灵巧操作、人形机器人、遥操作等子方向之间寻找技术迁移机会的人

仓库的核心产出不是论文 PDF 本身，而是每一篇论文的**分析笔记**——回答"它解决了什么问题、用了什么方法、为什么有效、我能借用什么"。

## 话题分类

为兼顾覆盖度与可检索性，笔记按七条主线组织，下设细分主题。这套分类刻意与常见的论文收集目录对齐，便于把原始 PDF 与分析笔记一一对应。

| 主线 | 细分主题 | 关注的核心问题 |
| --- | --- | --- |
| 感知与表示 | 基础模型 · 3D视觉 · 高斯泼溅 · 运动追踪 · 触觉 | 智能体如何理解场景、物体与自身状态 |
| 操作与抓取 | 操作 · 抓取 · 重定向/运动映射 | 机械臂与灵巧手如何作用于物体 |
| 运动与导航 | 人形机器人 · 运动控制 · 导航 | 腿式与轮式本体如何移动与定位 |
| 策略学习 | 扩散策略 · 强化学习 · VLA | 如何从数据/交互中习得行动策略 |
| 仿真与数据 | 仿真 · 数据生成 | 如何低成本地制造训练信号与闭环验证 |
| 世界模型与生成 | 世界模型 · 视频生成 | 如何预测未来、为决策提供想象空间 |
| 遥操作与硬件 | 遥操作 · 硬件 | 人如何介入、本体与传感器如何落地 |

每个细分主题对应 `notes/` 下的一个目录，命名形如 `06-manipulation`、`08-retargeting`，编号仅用于排序，不暗含阅读顺序。

## 分析方法

每篇论文用同一份模板拆解，确保不同论文、不同主题之间可横向对照。完整模板见 [`docs/paper-analysis-template.md`](docs/paper-analysis-template.md)，其骨架如下：

1. **元信息** — 标题、作者、会议/期刊、年份、arXiv 与项目页链接
2. **一句话总结** — 用一句话说清"做了什么、凭什么有效"
3. **研究问题** — 它针对什么痛点，现有方法差在哪里
4. **核心方法** — 输入输出、网络结构、损失函数、训练流程
5. **关键创新** — 相比前人真正新增的那一两点
6. **实验与结果** — 基准、指标、消融、基线对比
7. **局限与未来工作** — 作者承认的与读者发现的
8. **与本项目的关联** — 能否迁移到灵巧操作/人形/遥操作链路，具体卡在哪
9. **复现笔记** — 关键超参、数据集、踩坑记录

这套框架刻意把"与本项目的关联"单列一节。读论文的最终目的不是写摘要，而是判断哪些设计可以搬进自己的系统——把这一步显式化，才能避免"读了一百篇，用不上半篇"。

阅读方法论与三遍阅读法（速读抓主旨→精读啃方法→批判读找启发）的实践细节见 [`docs/reading-methodology.md`](docs/reading-methodology.md)。

## 仓库结构

```
Embodied-AI-Paper-Analysis/
├── README.md                  # 本文件（含论文索引总览）
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── papers/                    # 按主题分类的论文索引（970 篇）
│   ├── README.md              # 主题分类索引，含 arXiv 与代码链接
│   └── index.md               # 按年份分类索引
├── docs/
│   ├── paper-analysis-template.md   # 论文分析模板
│   ├── reading-methodology.md       # 阅读方法论
│   └── taxonomy.md                  # 话题分类说明
├── notes/                     # 论文分析笔记（按主题归档）
│   ├── README.md              # 自动生成的笔记索引
│   ├── 01-foundation-models/
│   ├── 06-manipulation/
│   ├── 08-retargeting/
│   └── ...                    # 共 21 个主题目录
├── summaries/                 # 单页速览（每篇一段话，用于快速检索）
│   └── README.md
├── scripts/
│   └── generate_index.py      # 自动扫描 notes/ 生成索引
└── assets/                    # 图表与示意图
```

笔记文件命名统一为 `YYYY-简短标题.md`，例如 `2025-diffusion-policy.md`。同名论文若有多篇分析，以作者首字母区分。

## 阅读路线

下面给出一条从地基到前沿的推荐路线，可按自身背景跳读。路线围绕"感知→操作→运动→策略→世界模型"的能力栈展开，与本仓库的主线分类一致。

**第一阶段：打地基。** 先读基础模型与表示类工作，理解 CLIP/DINO 等视觉表征如何为下游策略提供条件信号；再读 3D 视觉与高斯泼溅，建立对场景几何与可微渲染的直觉。这一阶段决定后续能否看懂策略网络到底"看"到了什么。

**第二阶段：进操作。** 进入操作、抓取与重定向主题。重点理解接触建模、运动映射（retargeting）与逆运动学——这三者是把人类/仿真动作搬到真实灵巧手的关键桥梁。扩散策略作为通用 visuomotor backbone 放在此阶段收尾。

**第三阶段：上身体。** 转向人形机器人与运动控制，关注全身 loco-manipulation 与地形适应。此时可回头把第二阶段的操作技能挂到运动基座上，体会"手-身协同"的工程难点。

**第四阶段：学策略。** 系统过一遍强化学习与 VLA，理清从 RL 到大规模动作模型的演进脉络，以及它们在泛化性、数据效率上的取舍。

**第五阶段：看未来。** 用世界模型与视频生成收尾，理解"预测即规划"的范式如何为上述策略提供想象与数据增广。

遥操作与硬件主题贯穿始终——它既是数据采集手段，也是验证策略的真人评测接口，建议在第二、三阶段穿插阅读。

## 论文来源与会议

笔记覆盖的论文主要来自以下来源，按权重排列：

- **顶会**：CoRL、RSS、ICRA、IROS（机器人与具身智能主战场）；CVPR、ICCV、ECCV、NeurIPS、ICLR、SIGGRAPH（视觉、学习与图形学交叉）
- **期刊**：T-RO、RA-L、IJRR
- **预印本**：arXiv（机器人 cs.RO、计算机视觉 cs.CV、人工智能 cs.AI 分类）

arXiv 链接统一记录在每篇笔记的元信息区，便于追溯版本。会议与年份信息用于判断工作的成熟度与影响力，但**不**作为是否精读的唯一标准——不少高影响力的工作首发于 arXiv。

## 快速开始

```bash
git clone <your-repo-url>
cd Embodied-AI-Paper-Analysis

# 用模板新建一篇笔记
cp docs/paper-analysis-template.md notes/06-manipulation/2025-xxx.md

# 扫描所有笔记，更新索引
python scripts/generate_index.py
```

新增一篇笔记后，在对应主题目录的 `README.md` 中补一行链接，保持索引与文件同步。`scripts/generate_index.py` 可自动完成这一步。

## 贡献

欢迎以 Issue 或 Pull Request 的形式补充笔记、修正错误或扩展分类。新增笔记请遵循模板，并在文件头填写完整元信息。详细的命名、提交与审阅约定见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## License

本仓库的笔记与文档以 [CC BY-NC-SA 4.0](LICENSE) 协议开源，供学习与研究使用。论文版权归各自原作者所有，仓库不分发论文 PDF，仅记录分析。
