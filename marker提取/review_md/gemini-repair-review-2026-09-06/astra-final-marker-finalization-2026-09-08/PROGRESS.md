# Astra 最终 Marker 总表收口

开始日期：2026-09-08

## 目标

在不修改正式工作簿的前提下，完成 Luna 现有 marker 正确性轮的证据返修、未决记录隔离、主表一致性检查和按细胞汇总重建，最终形成可发布的 marker 总表。

## 当前阶段

- [x] Astra 独立抽查与阻断项确认
- [x] 识别 204 条机械 `source_context` 通过记录
- [x] 识别 445 条历史 quick-consistency 继承记录
- [x] 识别 34 条 evidence binding 空白记录
- [x] 定位两篇高风险预印本的正式页面与补充材料入口
- [x] 将两篇高复杂度预印本的 353 条记录隔离为 deferred unresolved
- [ ] 下载并校验原始 PDF、补图和补充表（暂缓，不阻塞其余收口）
- [ ] 逐证据组重新裁决 204 条机械通过记录
- [ ] 逐来源核验 445 条历史继承记录
- [x] 闭环 34 条 evidence binding 空白记录
- [ ] 生成 unresolved 清单与最终 change-set
- [ ] 重建主表及按细胞汇总
- [ ] Astra 最终发布验收

## 约束

- 正式 `our_markers.xlsx` 与 `our_markers_by_cell.xlsx` 在最终验收前保持不动。
- 关键词命中、旧 `source_context` 或抗体 panel 列表不能单独生成 biological pass。
- 无法取得决定性正文、图或表的关系进入 unresolved，不写入最终发布主表。
