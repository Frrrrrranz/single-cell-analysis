# Marker 提取旧产物归档（2026-08-13）

本目录保存本轮审计中从活动 marker 流程移出的旧产物。文件可用于追溯历史，但**不得直接重新导入数据库或作为可靠 marker 结果使用**。

## 目录说明

- `batches/`：基于旧 `paper_map.json` 生成的批次文件。旧映射存在论文 ID 冲突，因此仅供追溯。
- `derived/`：受错误论文映射和未完成人工复核影响的合并表、清洗报告、Excel 及网页报告。
- `invalid-paper-map/`：8 组确认错挂论文 ID 的 raw JSON / review CSV，以及产生冲突的旧 `paper_map.json`。
- `stale-review-csv/`：11 个只有表头、且早于对应 raw JSON 的复核表，不能代表已完成复核。
- `failed-extraction/`：抽取结果为 0 的 raw JSON，需要在映射和抽取流程修复后重跑。

## 使用限制

1. 不要从本目录向未来新建的 marker 主表执行导入。
2. 需要历史对照时，可读取 raw JSON 和报告，但必须以论文 PDF、正确 DOI 和新映射重新核验。
3. 新的 `paper_map.json` 应由 PDF 指纹、标题、DOI/PMID 校验后重新生成，不应复制本目录中的旧文件。
