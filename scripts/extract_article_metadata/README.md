# 文章元数据整理管线

本目录承接 `.agents/plan/article-metadata-extraction-2026-08-21.md`，只处理 `review_md/` 中已有的论文 Markdown。

## 当前边界

- 任务范围来自 `db/cellxgene/our_marker_papers.xlsx` 的 `我方Marker文章` sheet。
- 没有对应 Markdown 的任务写入范围映射并跳过，不伪造空结果。
- Marker 不重新提取，只从现有 schema v2 结果和总表关联状态。
- 论文原文值、标准化值、来源定位和证据片段同时保留。

## 用法

```powershell
python scripts/extract_article_metadata/run_metadata_extraction.py --pilot
python scripts/extract_article_metadata/run_metadata_extraction.py --all --skip-existing
```

中间结果保存到 `output/`；最终工作簿由后续汇总步骤生成到 `db/cellxgene/our_paper_metadata.xlsx`。
