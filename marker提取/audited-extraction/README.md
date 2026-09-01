# 当前 Marker 终审产物

> 本目录现有结果是旧严格筛选版历史基线。2026-09-01 起，四层/物种/组织只作分类，不能据此排除正式 Marker；新口径见 `../MARKER_POLICY.md`。

本目录保存当前 40 篇论文的终审过程产物：

- `marker-summary.html`：由当前终审 JSON 重建的离线汇总页；
- `markers/`：40 篇终审 JSON、逐篇 review CSV、`audit_summary.csv` 和 `full-audit-report.md`。

当前 Marker 总表位于 `db/cellxgene/our_markers.xlsx`，含 `markers`、`audit_exclusions`、`audit_summary` 等工作表。

2026-08-31 清理前后均完成验证：

1. 原始总表哈希与审核前基准一致；
2. 新版保留范围外历史记录，以审计结果替换范围内旧记录，并把移除项目写入排除审计表；
3. 旧严格筛选版人工复核内容重建后共有 87 条 Marker；
4. 50 项单元测试和 `validate_full_audit.py` 全部通过；
5. 旧版可从 Git 提交 `19d4ca5`、`8893242` 和 `85b4727` 恢复。