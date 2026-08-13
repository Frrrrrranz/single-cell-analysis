# db/_archive 说明

该目录保存历史过程材料和可恢复的旧产物，不是当前 marker 提取的活动输入目录。

## 仍有价值的内容

- `cellxgene_all_details/`：早期 CellxGene API 原始响应、候选集和汇总，可用于追溯候选论文来源。
- `filtered_datasets.csv`、`excluded_datasets.csv`、`dedup_log.csv`、`filter_report.md`：可用于复现早期筛选和去重决策。
- `download_papers.log`、`manual_download_helper.html`：可用于排查早期下载失败和人工下载过程。

这些文件不应被 marker 提取代码直接读取；当前论文清单以 `db/cellxgene/pns_papers_summary.xlsx` 及经 PDF 正文核验后的新映射为准。

## 保留策略

- 原始抓取和筛选日志至少保留到 marker 数据库重建并验收完成。
- `marker-extraction/` 下的旧结果用于问题追溯，确认新结果无误后可整体删除。
- 新活动文件不得写入 `_archive`。

