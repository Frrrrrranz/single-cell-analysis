# Marker 提取与终审

> 2026-09-01 起，唯一有效口径见 `MARKER_POLICY.md`：论文中所有细胞类型的正式 Marker 全部保留；L1-L4、物种和组织仅用于分类。下述 87 条是旧严格筛选版基线，不是全量口径的最终数目。

当前结果按职责分开存放：

- 总表：`表单/our_markers.xlsx`；
- 终审 JSON、逐篇 CSV、报告和 HTML：`audited-extraction/`；
- 论文 Markdown：`review_md/`；
- 脚本与测试集中在 `scripts/`；提示词与审计记录在本目录对应子目录。

## 当前结果

- 审核论文：40 篇；
- 恢复轮（2026-09-01）追加 1786 条，总表 `表单/our_markers.xlsx` 共 1883 行（97 冻结 + 1786 恢复追加）；
- 逐篇审计 JSON 与恢复轮产物在本目录 `audited-extraction/`；
- 旧版总表与旧逐篇提取产物已从工作树删除。

旧版可从 Git 提交 `85b4727` 恢复。删除前确认原始总表 SHA256 为
`1c096dedc4191277f89e6131aeb772a919c346d9246390aa75d11f2e343fe71d`，且完整对账验证通过。

## 验证

```powershell
python -m unittest discover -s scripts/tests -p "test_*.py"
python scripts/validate_full_audit.py
```

重建 HTML：

```powershell
python scripts/build_audited_dashboard.py
```

如需重新执行依赖旧 raw JSON 或旧总表的流程，应先从 `85b4727` 将所需输入恢复到临时目录，再通过 `--raw-dir` 或 `--source-xlsx` 显式传入。