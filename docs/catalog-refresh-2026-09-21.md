# 论文目录刷新记录 · 2026-09-21

本次是索引与来源元数据刷新，不是对所有论文重新精读或复现实验。原快照为 2026-08-31（提交 `441cbf1`）；七方向、40 个二级领域、200 个末级分类及分类规则保持不变。

## 本次结果

| 数据层 | 上次记录数 | 本次记录数 | 实际范围 |
| --- | ---: | ---: | --- |
| 会议目录 | 3,746 | 3,750 | 2022–2026；原有十个会议与 `robot` 书目检索规则 |
| arXiv 预印本 | 23,973 | 24,511 | 2023-09-21 至 2026-09-21，含 `cs.RO` 交叉分类 |
| 合并阅读视图 | 26,045 | 26,641 | 按规范化标题去重，仅用于阅读展示 |

arXiv 共处理 31,697 条候选，24,511 条满足分类规则，7,186 条未纳入。预印本中有 1,613 条记录的标题与会议目录重叠，对应 1,612 个不同标题；arXiv 层另有 8 条规范化标题重复。两层源记录保留，重叠不构成录用证明。

## 新增、移出与来源边界

- arXiv 按 ID 比较：新增 943 条、移出 405 条，净增 538 条；398 条移出记录已在新的三年窗口之外，另 7 条未出现在本轮分类结果中。新增不等于全部于本周发表，移出也不等于撤稿。
- 会议按标题比较：新增 10 条、移出 6 条，净增 4 条。书目数据库结果会变化，不把本轮未返回的条目宣称为撤稿或错误论文。历史内容可从上述基准提交恢复。
- 会议目录的 `official`、`publisher`、`bibliographic` 是不同证据级别；本次 74 / 3,113 / 563 条分别属于这三类。不是 3,750 条都逐一查过会议官网。
- 修正自动来源选择：`10.48550/arXiv.*` DOI 只指向预印本，不再充当会议出版社来源；有 DBLP 标识时用 DBLP，否则保留 Semantic Scholar 书目来源。
- 2026 年会议记录仍受当前官方种子与书目检索覆盖限制，不代表完整收录所有 2026 年录用论文。

本轮未返回的六个旧会议标题：

1. Dynamic Handover: Throw and Catch with Bimanual Hands
2. HAT: Head-Worn Assistive Teleoperation of Mobile Manipulators
3. OmniLRS: A Photorealistic Simulator for Lunar Robotics
4. Real2Sim2Real Transfer for Control of Cable-Driven Robots Via a Differentiable Physics Engine
5. Sim2Real2: Actively Building Explicit Physics Model for Precise Articulated Object Manipulation
6. VERN: Vegetation-Aware Robot Navigation in Dense Unstructured Outdoor Environments

仍在日期窗口内但未出现在本轮分类结果中的七个旧 arXiv 标题：

1. LE-PAVD: Learning-Enhanced Physics-Aware Vehicle Dynamics for High-Speed Autonomous Navigation
2. RoboGPU: Accelerating GPU Collision Detection for Robotics
3. Learning Without Losing Identity: Capability Evolution for Embodied Agents
4. Rectify, Don't Regret: Avoiding Pitfalls of Differentiable Simulation in Trajectory Prediction
5. Octopus Protocol: One-Shot Hardware Discovery and Control for AI Agents via Infrastructure-as-Prompts
6. End2Race: Efficient End-to-End Imitation Learning for Real-Time F1Tenth Racing
7. Optimal Solutions for the Moving Target Vehicle Routing Problem with Obstacles via Lazy Branch and Price

## 刷新故障与修订

最近三次定时刷新失败。本次查阅的 [2026-09-21 GitHub 运行日志](https://github.com/Dld0621/Embodied-AI-Paper-Analysis/actions/runs/35574734265) 在 arXiv 请求阶段报 HTTP 406，未发布新快照。

本地不含个人邮箱的项目 User-Agent 请求成功，完整抓取随后完成。请求不再对外携带个人邮箱；但未做旧标识的对照复测，不能断言邮箱就是 406 的唯一原因，也不能据此宣称 GitHub 定时刷新已经恢复。

新增 Atom 根节点、API 错误项及 totalResults 校验，防止错误页面被当作空结果成功发布。该防护在本次抓取运行过程中补入，因此完整抓取回执证明的是无邮箱标识的请求路径；新增响应校验另由离线测试验证。没有修改定时工作流、关闭审计、替换数据源或调整分类阈值。

请求仍遵循 [arXiv 官方 API 手册](https://info.arxiv.org/help/api/user-manual.html) 的查询和限速原则，使用原有十秒页间隔与断点缓存。没有下载论文 PDF。

## 验证

- 完整测试：36 项通过，含新增 10 项传输/来源回归。
- 分类注释、目录数据审计、确定性生成和本地链接检查通过。
- 重建 269 份生成文件；200 个末级分类可按大小拆页，因此页面数不等于分类数。
- README 与全部分类页使用真实新快照计数；不是仅修改更新时间。
- 没有重新精读全部摘要、逐篇核验录用、运行论文实验或做浏览器视觉验收。

本记录描述已生成且本地验证的内容；是否已进入 main、网站是否已部署，要另以 GitHub 提交和部署回执为准。
