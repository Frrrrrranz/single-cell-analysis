# PNS scRNA-seq Marker 提取

本项目整理 CellxGene 候选论文中的外周神经系统相关 Marker，并保留逐篇证据、文章元数据和离线汇总页面。

## 当前目录

```text
.
├── db/
│   ├── cellxgene/
│   │   ├── our_markers.xlsx          # 旧严格筛选版总表（87 条，待全量补充）
│   │   ├── our_marker_papers.xlsx    # 44 条任务主清单
│   │   ├── our_paper_metadata.xlsx   # 文章支持性元数据
│   │   └── README.md
│   └── reference/                    # 当前参考工作簿
├── scripts/
│   ├── extract_markers/
│   │   ├── audited-extraction/       # 40 篇终审 JSON、review CSV 和 HTML
│   │   ├── review_md/                # 40 篇论文 Markdown
│   │   ├── prompts/                  # 提取与终审提示词
│   │   ├── tests/                    # 自动化测试
│   │   └── audits/                   # 审计与任务范围记录
│   └── extract_article_metadata/
├── .agents/
└── papers_report/
```

Marker 流程说明见 [`scripts/extract_markers/README.md`](scripts/extract_markers/README.md)，当前唯一有效的纳入规则见 [`scripts/extract_markers/MARKER_POLICY.md`](scripts/extract_markers/MARKER_POLICY.md)。

## 当前状态

- 旧严格筛选版已完成 40 篇终审并保留 87 条 Marker；该数字不是“全部保留”口径下的最终结果；
- 当前总表统一存放在 `db/cellxgene/our_markers.xlsx`；
- 终审 JSON、逐篇 review CSV 与离线 HTML 集中在 `scripts/extract_markers/audited-extraction/`；
- 旧版提取产物已从 Git 提交 `85b4727` 恢复到本地 `.archive/marker-extraction-85b4727/`，只供检阅，不作为当前输入；
- 正式 Marker 必须能回溯至作者明确的 marker、细胞注释、图表或补充材料证据。

*最后更新：2026-09-01*
