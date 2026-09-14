# Luna 单模型收尾正式报告

## 发布结果

2026-09-06 已完成全量基线收尾并发布两份正式总表。

- 基线：2,499 条 marker、43 篇论文；基线 pending=0。
- 发布集合：2,488 条 active marker、43 篇论文。
- 两份正式表均已由暂存版替换；发布后的 SHA256 与暂存版逐文件一致。
- 机械验证：通过；无重复 ID、无缺失新增 ID、无归档 ID残留、无公式错误。

正式文件：

- `marker提取/表单/our_markers.xlsx`
- `marker提取/表单/our_markers_by_cell.xlsx`

## 本轮裁决计数

- 新增 3：RIMS2、PRR4、LAMC3—Pericytes。
- 修改 1：M00071 的 NeuN/RBFOX3 细胞上下文修正为 nociceptors/neurons，保留衰老实验上下文。
- 合并归档 13：完整重复关系移入 `audit_exclusions`，主表保留代表行。
- context_only 转存 1：M01510，移入审计记录，不进入正式 marker 集合。
- 候选排除归档 3：FCN1、Cd86、Glb1；这些是本轮候选，不是从基线正式表删除的记录。
- 候选未决隔离 11：保留在 registry/unresolved.json 与审计记录，不进入正式 marker 集合。

## 证据边界

既有 490 个单元有逐条旧 Luna 定位；其中 473 个为原基线记录，另有 2,026 个基线记录属于此前未覆盖范围。本次对全部 2,499 条建立 review_id 并完成裁决状态，但新增覆盖部分以本地 Markdown、原始 source_locator/source_context、历史交叉表和可回溯 registry 为主，不把缺少逐字命中的记录伪装成新逐图核验。LAMC3—Pericytes 已重新打开指定 Fig.1D 实图并登记纠错证据。

详细台账、变更集、证据和验证结果位于本目录的 `registry/`、`change_set.json`、`validation.json` 与 `release.json`。
