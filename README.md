# PNS scRNA-seq Marker 提取

本项目整理 CellxGene 候选论文中的外周神经系统相关 Marker，并保留逐篇证据、文章元数据和离线汇总页面。

## 当前目录

```text
.
├── scripts/                          # 全部脚本与自动化测试（含 tests/）
├── marker提取/
│   ├── pdf/                          # 73 篇论文 PDF
│   ├── 表单/                         # 三个工作簿：总表、任务清单、文章元数据
│   ├── reference/                    # 导师参考工作簿
│   ├── audited-extraction/           # 40 篇终审 JSON、review CSV 和恢复轮产物
│   ├── review_md/                    # 论文 Markdown
│   ├── prompts/                      # 提取与终审提示词
│   ├── audits/                       # 审计与任务范围记录
│   └── article_metadata/             # 文章元数据提取产物
├── .agents/
└── papers_report/
```

Marker 流程说明见 [`marker提取/README.md`](marker提取/README.md)，当前唯一有效的纳入规则见 [`marker提取/MARKER_POLICY.md`](marker提取/MARKER_POLICY.md)。

## 当前状态

- 40 篇终审完成；2026-09-01 恢复轮按全量口径追加 1786 条，总表现为 1883 行；
- 当前总表统一存放在 `marker提取/表单/our_markers.xlsx`；
- 终审 JSON、逐篇 review CSV 与恢复轮产物集中在 `marker提取/audited-extraction/`；
- 旧版提取产物已从 Git 提交 `85b4727` 恢复到本地 `.archive/marker-extraction-85b4727/`，只供检阅，不作为当前输入；
- 正式 Marker 必须能回溯至作者明确的 marker、细胞注释、图表或补充材料证据。

*最后更新：2026-09-01*
