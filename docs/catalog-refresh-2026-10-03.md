# 论文目录刷新记录 · 2026-10-03

本次是论文索引与来源元数据更新，不是逐篇精读或论文实验复现。基准为 2026-09-21 快照（提交 `6fe373f`）；分类规则、七方向、40 个二级领域和 200 个末级分类保持不变。

## 数据结果

| 数据层 | 上次 | 本次 | 实际范围 |
| --- | ---: | ---: | --- |
| 会议目录 | 3,750 | 4,365 | 2022–2026；十个会议及原有 robot 书目检索规则 |
| arXiv 预印本 | 24,511 | 25,257 | 2023-10-03 至 2026-10-03；含 cs.RO 交叉分类 |
| 合并阅读视图 | 26,641 | 27,637 | 按规范化标题去重，仅用于阅读展示 |

arXiv 完整查询处理 32,552 条候选，25,257 条满足分类规则，7,295 条未纳入。本轮收录记录中最晚的原始提交日期为 **2026-10-01**；10 月 3 日是查询窗口截止日，不是所有数据的发表日，也不保证该日尚未发布或尚未索引的记录已可获取。

## 新增、移出与证据边界

- 会议目录新增 615 条，无旧条目移出：ICRA 608、RSS 4、IROS 2、CoRL 1。其中 601 条归属 2026 年，其余为较早年份的书目补录；不是 615 篇都在这两周发表。
- 当前会议来源层级为 official 74、publisher 3,720、bibliographic 571。层级表示来源类型，不代表本轮逐篇访问了全部会议官网，也不代表完整收录所有会议论文。
- arXiv 按 ID 比较新增 1,031 条、移出 285 条，净增 746 条。其中 277 条已超出新三年窗口；另 8 条仍在时间窗口内，但未进入本轮分类结果，具体原因尚未逐篇确认。移出不等于撤稿；旧记录保留在 Git 历史中。
- arXiv 中 1,978 条记录与会议标题重叠，对应 1,977 个不同规范化标题；arXiv 内部另有 8 条规范化标题重复。标题重叠不构成录用证明，两层源数据独立保留。

仍在窗口内、但本轮未纳入的旧 arXiv ID：

| ID | 上次收录的标题 |
| --- | --- |
| 2603.07775 | Residual Control for Fast Recovery from Dynamics Shifts |
| 2510.20483 | Dual Control Reference Generation for Optimal Pick-and-Place Execution under Payload Uncertainty |
| 2505.03761 | Soft yet Effective Robots via Holistic Co-Design |
| 2606.05663 | Preserving Full 6-DOF Actuation Under Abrupt Total Rotor Failures: Passive Fault-Tolerant Flight Control Using a Biaxial-Tilt Hexacopter |
| 2606.17317 | Transformer-Based Warm-Starting for Feasible and Optimal Terminal Approach to Tumbling Objects with Space Manipulators |
| 2601.21976 | Macro-Scale Electrostatic Origami Motor |
| 2609.04381 | Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models |
| 2609.02319 | From Multi-Fisheye Sensing to Panoramic Perception: A Parallax-Aware Onboard Platform for Ultra-Low-Altitude UAVs |

## 验证与发布边界

使用现有同步脚本完成两层抓取，再统一重建 README、网页数据与分类目录。不调整分类阈值、不降低新鲜度门禁、不修改工作流、不下载论文 PDF。

更新前 36 项测试中有 2 项因旧快照已超过八天而失败；真实抓取新快照后重新运行全部审计，不以仅修改日期来消除失败。

本轮验收包括：目录数据审计、分类注释一致性、生成文件一致性、本地链接检查、36 项单元测试及 Git 空白检查。索引规则测试不能替代逐篇语义审查；本轮也没有浏览器视觉验收。

更新提交到现有 PR #1 所在分支。PR 更新不等于 main 合并或公开网站部署；两者应另以 GitHub 合并与部署回执确认。
