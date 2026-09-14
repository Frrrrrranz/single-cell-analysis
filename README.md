# PNS scRNA-seq Marker 整理

本项目整理 CellxGene 候选论文中的细胞类型 Marker，并保留最终工作簿、原始论文与参考资料。

## 当前目录

```text
.
├── marker提取/
│   ├── pdf/          # 原始论文 PDF
│   ├── 表单/         # Marker 总表、按细胞汇总表、论文清单与元数据
│   ├── reference/    # 导师参考工作簿
│   ├── MARKER_POLICY.md
│   └── README.md
└── papers_report/    # 既有论文阅读与分析资料
```

## 当前工作方式

旧的自动提取、批量审计和恢复管线已经停用并从工作区移除。

后续统一采用：

1. 将论文 PDF、补充材料和提取要求发送给 Gemini；
2. Gemini 输出逐篇、结构化的 Marker 提取结果；
3. Codex 对照原始 PDF、表格和方法部分复查；
4. 仅将复查通过的记录写入 `marker提取/表单/our_markers.xlsx`；
5. 必要时同步更新 `our_markers_by_cell.xlsx`。

正式纳入规则以 `marker提取/MARKER_POLICY.md` 为准。
