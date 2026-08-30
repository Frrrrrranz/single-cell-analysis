# Marker 提取目录

本目录集中保存本轮 PNS 单细胞 Marker 提取的可复现脚本、逐篇结果、总表、汇总页面、论文 Markdown 和审计记录。`papers_report/` 是此前独立汇报项目，不属于本目录，也未参与本轮整理。

## 目录结构

```text
extract_markers/
├── our_markers.xlsx              # 原始总表（永久保留，未修改；SHA256 基准见 validate_full_audit.py）
├── our_markers_audited.xlsx      # 40 篇全量终审后的修正版总表
├── marker_summary.html           # 原始离线汇总页面（保留）
├── marker_summary_audited.html   # 修正版离线汇总页面
├── build_dashboard.mjs           # 重新生成原始汇总页面
├── build_audited_dashboard.py    # 重新生成修正版汇总页面
├── run_extraction.py             # Markdown/PDF → schema v2 JSON 主提取脚本
├── run_full_audit.py             # 40 篇全量终审脚本（LLM 审核 + 自动降级规则）
├── recheck_citations.py          # 粘连 PDF 文本 citation 复核（确定性，无 LLM）
├── build_audited_outputs.py      # 从终审 JSON 生成修正版总表/review CSV/汇总报告
├── validate_full_audit.py        # 程序化质量检查（退出 0 = 全部通过）
├── marker_schema.py              # schema、证据等级和确定性护栏
├── normalize_marker_output.py    # 已有 schema v2 JSON 规范化
├── audit_paper_map.py            # 论文/PDF 身份与哈希审计
├── quarantine_pdf_issues.py      # 无效 PDF/重复副本隔离工具
├── gen_review_sheet.py           # 从 raw JSON 重建证据 CSV
├── import_markers.py             # 将已确认记录导入总表
├── convert_gene_symbols.py       # 可选基因符号标准化
├── prompts/
│   ├── extract_markers_v4.md     # 提取提示词
│   └── audit_markers_v1.md       # 终审提示词
├── review_md/                    # 40 篇已经转换好的论文 Markdown
├── markers_output_v2/            # 40 篇原始 raw JSON + review CSV（不覆盖）
├── markers_audited/              # 40 篇终审 JSON + review CSV + audit_summary.csv + full-audit-report.md
├── tests/                        # schema、审核规则和论文映射测试
└── audits/                       # 历史审核、任务快照和五篇抽查报告
```

## 当前结果

### 2026-08-30 全量终审（已完成）

40/40 篇全部审核（模型 deepseek-v4-flash + audit_markers_v1 提示词 + run_full_audit.py 自动门槛），详见 `.agents/progress/marker-full-audit-2026-08-30.md`：

- 文章状态：corrected 23、no_formal_target_marker 17；
- 修正版正式 Marker（include，按 5.7 去重键去重）：78 条，覆盖 16 篇论文；
- 78 条中 56 条沿自原表（其中 33 条修正了物种/极性/证据/细胞类型）、22 条为新增；原表 40 篇范围内另有 22 条未获终审 include 被移除；
- 原表 88 行（86 approved + 2 pending）全部保留原样；范围外 10 行历史行在修正版中标记 `not_in_40_article_audit`；
- unresolved 7 条（含 CDH19：原文 0 次出现）；排除候选（exclude/context_only/unresolved）1749+3+7 条记录于 `audit_exclusions` sheet。

### 早期提取轮次

- 可处理论文：40 篇；每篇均有一个 `*_raw.json`。
- 40 份 `*_review.csv` 继续保留，因为 `our_markers.xlsx` 的 `source_file` 字段引用这些文件。
- 2026-08-30 独立子 Agent 五篇抽查仅 1/5 通过，触发本轮全量终审。详见 `audits/sample-audit-2026-08-30.md`。

## 运行方式

优先直接使用已存在的 Markdown，不重复转换 PDF：

```powershell
python run_extraction.py `
  --markdown review_md/DOI_10.1038_s41588-022-01243-4.md `
  --paper-id DOI_10.1038_s41588-022-01243-4 `
  --skip-existing
```

默认输出目录为 `markers_output_v2/`，默认提示词为 `prompts/extract_markers_v4.md`。

全量终审与产物重建（按顺序）：

```powershell
python run_full_audit.py --workers 3 --overwrite   # 断点续跑去掉 --overwrite
python recheck_citations.py                        # 粘连文本 citation 复核
python build_audited_outputs.py                    # 修正版总表 + review CSV + 报告
python build_audited_dashboard.py                  # 修正版 HTML
python validate_full_audit.py                      # 程序化质量检查
```

运行测试（本环境无 pytest，用 unittest 等价运行）：

```powershell
python -m unittest discover -s tests -p "test_*.py"
```

重新生成原始汇总页面：

```powershell
node build_dashboard.mjs
```

Dashboard 还会读取以下支持文件：

- `db/cellxgene/our_marker_papers.xlsx`：44 条任务主清单；
- `db/cellxgene/our_paper_metadata.xlsx`：组织、神经细胞和统计方法汇总。

PDF、论文身份映射及完整登记仍保留在 `db/cellxgene/`，避免复制大型来源文件。

## 证据边界

正式 Marker 必须能回溯至作者明确的 marker/注释/图表证据。五篇抽查曾发现（现已由全量终审规则修复并有回归测试覆盖）：

1. 把家族式名称写入唯一 `gene_symbol` → 终审以 `normalization_status=ambiguous/non_gene_entity` 阻断入表；
2. 把明确的 `GENE+` / `GENE-high` 注释降为 context-only → guardrail 已扩展亚群语法识别；
3. 漏掉 `marked by` / `marks` / marker list 中的正式候选 → 终审要求主动扫描全文目标层级；
4. 无任务 scope（`PNS层级=—`）论文误纳普通细胞 Marker → 终审要求主动扫描 PNS/神经内分泌细胞，无则记 `no_formal_target_marker`。

修正版数据的可信度依赖：`validate_full_audit.py` 退出 0 + 50 个单元测试通过 + 原表 SHA256 基准未变。
