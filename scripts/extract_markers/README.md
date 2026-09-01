# Marker 提取与终审

> 2026-09-01 起，唯一有效口径见 `MARKER_POLICY.md`：论文中所有细胞类型的正式 Marker 全部保留；L1-L4、物种和组织仅用于分类。下述 87 条是旧严格筛选版基线，不是全量口径的最终数目。

当前结果按职责分开存放：

- 总表：`db/cellxgene/our_markers.xlsx`；
- 终审 JSON、逐篇 CSV、报告和 HTML：`audited-extraction/`；
- 论文 Markdown：`review_md/`；
- 共享脚本、提示词、测试和审计记录：本目录对应子目录。

## 当前结果

- 审核论文：40 篇；
- 旧严格筛选版 Marker：87 条（按审计键去重，待全量补充）；
- 总表、逐篇审计 JSON 和 HTML 已重新生成并通过验证；
- 旧版总表、旧逐篇提取产物和旧介绍 HTML 已从工作树删除。

旧版可从 Git 提交 `85b4727` 恢复。删除前确认原始总表 SHA256 为
`1c096dedc4191277f89e6131aeb772a919c346d9246390aa75d11f2e343fe71d`，且完整对账验证通过。

## 验证

```powershell
python -m unittest discover -s scripts/extract_markers/tests -p "test_*.py"
python scripts/extract_markers/validate_full_audit.py
```

重建 HTML：

```powershell
python scripts/extract_markers/build_audited_dashboard.py
```

如需重新执行依赖旧 raw JSON 或旧总表的流程，应先从 `85b4727` 将所需输入恢复到临时目录，再通过 `--raw-dir` 或 `--source-xlsx` 显式传入。