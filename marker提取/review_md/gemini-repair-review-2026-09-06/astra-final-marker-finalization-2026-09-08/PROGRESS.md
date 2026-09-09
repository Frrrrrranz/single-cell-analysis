# Astra 最终 Marker 总表收口

开始日期：2026-09-08

## 目标

在不修改正式工作簿的前提下，完成 Luna 现有 marker 正确性轮的证据返修、未决记录隔离、主表一致性检查和按细胞汇总重建，最终形成可发布的 marker 总表。

## 当前阶段

- [x] 当前进度已提交并推送至 `feat/0909`（checkpoint：`2e87110`）
- [x] Astra 独立抽查与阻断项确认
- [x] 识别 204 条机械 `source_context` 通过记录
- [x] 识别 445 条历史 quick-consistency 继承记录
- [x] 识别 34 条 evidence binding 空白记录
- [x] 定位两篇高风险预印本的正式页面与补充材料入口
- [x] 将两篇高复杂度预印本的 353 条记录隔离为 deferred unresolved
- [x] 将 DOI 10.64898/2025.12.18.695268 的 41 条图/表缺失记录隔离为 deferred unresolved
- [x] 确认 5 条不合格 marker，并从工作版主表剔除：M00157、M00188、M00209、M00210、M00223
- [x] 生成 2485 条的复核工作版 `staged/our_markers_reviewing.xlsx`；正式表未覆盖
- [x] 清理 `.temp`、inspect dump 和旧预览图等明确可再生缓存
- [ ] 下载并校验原始 PDF、补图和补充表（暂缓，不阻塞其余收口）
- [ ] 完成剩余 221 条复核（已完成 26，剩余 195）
- [x] 闭环 34 条 evidence binding 空白记录
- [x] 394 条 unresolved 已形成独立清单，待 221 条完成后再复核
- [ ] 汇总 221 条裁决并生成最终 change-set
- [ ] 重建主表及按细胞汇总
- [ ] Astra 最终发布验收

## 当前计数（2026-09-09）

- 1819 条 evidence-bound：按用户决定暂沿用。
- 已独立接受：63 条（34 + 27 + 2）。
- 已确认剔除：5 条。
- 221 条复核：已完成 26 条，剩余 195 条。
- 暂缓待议：394 条。
- 当前工作版 active marker：2485 条（2490 - 5）。

## 221 条复核批次

- Batch 001：DOI 10.1126/sciimmunol.adf9988，共 26 条；25 条原值接受，M02348 从 `LMPP/ELP–SPINK2` 纠正为正文支持的 `pre-pro-B–SPINK2` 后接受。

## 约束

- 正式 `our_markers.xlsx` 与 `our_markers_by_cell.xlsx` 在最终验收前保持不动。
- 关键词命中、旧 `source_context` 或抗体 panel 列表不能单独生成 biological pass。
- 无法取得决定性正文、图或表的关系进入 unresolved，不写入最终发布主表。
