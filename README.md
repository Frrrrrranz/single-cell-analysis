# PNS scRNA-seq Marker 提取

本项目从 CellxGene 候选论文中提取和整理外周神经系统相关细胞 Marker，并保留论文原文证据、文章元数据和离线汇总页面。

## 当前目录

```text
.
├── scripts/
│   ├── extract_markers/          # 本轮 Marker 主目录
│   │   ├── our_markers.xlsx      # Marker 提取总表
│   │   ├── marker_summary.html   # 离线总结页面
│   │   ├── markers_output_v2/    # 40 篇 raw JSON + 来源证据 CSV
│   │   ├── review_md/            # 40 篇已有论文 Markdown
│   │   ├── prompts/              # 当前 v4 提示词
│   │   ├── tests/                # 自动测试
│   │   └── audits/               # 任务快照与抽查审核记录
│   └── extract_article_metadata/ # 组织、神经细胞和方法的支持性整理
├── db/
│   ├── cellxgene/                # 任务主表、PDF、论文映射与支持性元数据
│   └── reference/                # 原始参考表
├── .agents/                      # 计划与进度记录
└── papers_report/                # 此前独立汇报项目，本轮忽略且未改动
```

Marker 目录的文件说明和运行命令见 [`scripts/extract_markers/README.md`](scripts/extract_markers/README.md)。

## 当前状态

- 44 条任务中有 40 篇可处理文章；40 篇均已有 Marker raw JSON 和对应来源证据 CSV。
- Marker 总表、汇总 HTML、提取脚本、逐篇结果和审计记录已经集中到 `scripts/extract_markers/`。
- `db/cellxgene/our_marker_papers.xlsx` 保留为 44 条任务主清单；PDF 与论文身份映射继续保留在 `db/cellxgene/`，避免复制大型来源文件。
- 2026-08-30 由独立子 Agent 抽查 5 篇，结果仅 1/5 通过，因此未清理任何 `pending`，也未修改任何 Excel、JSON 或 CSV 内容。

## 证据原则

正式 Marker 必须能回溯到作者明确的 marker、细胞注释、图表或补充材料证据，普通 DEG 或表达信号不能直接视为正式 Marker。当前抽查发现 guardrail 仍可能漏掉明确的 `GENE+`、`GENE-high`、`marked by` 和 marker list 证据，详见：

- `scripts/extract_markers/audits/sample-audit-2026-08-30.md`

`papers_report/` 与 `.workflow/` 属于此前汇报工作，不纳入本轮 Marker 整理。

*最后更新：2026-08-30*
