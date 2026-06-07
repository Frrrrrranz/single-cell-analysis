# PNS scRNA-seq 数据库

> 外周神经系统（PNS）单细胞 RNA 测序文献数据收集与结构化数据库

## 项目结构

```
.
├── db/                         # 数据库
│   └── pns-scrna.xlsx          # 主数据库（5表：papers/datasets/cell_types/cell_subtypes/processing）
│
├── papers/                     # 文献资料
│   ├── ENEURO.0066-20.2020/    # Toma et al. 2020, eNeuro（坐骨神经Drop-seq）
│   ├── COMMUN-BIOL.5.1105.2022/ # 施万细胞相关文献（Commun Biol 2022）
│   └── PNAS.117.9466.2020/     # PNAS 2020 外周神经文献
│
├── pns-scrna-database/         # 数据库设计 Skill（Schema + 提取SOP + 脚本）
│   ├── SKILL.md
│   └── design/
│       ├── 01_schema.md        # 5表字段定义（唯一真源）
│       ├── 02_controlled_vocab.md  # 受控词表
│       ├── 05_extraction.md    # 提取 SOP + prompt + few-shot
│       └── 07_scripts/         # 校验/入库/统计 Python 脚本
│
├── reports/                    # 分析报告
│   └── GSE181316-assessment.md # GSE181316 表格评估报告
│
└── scripts/                    # 分析脚本
    └── step1_scRNA.Rmd         # 单细胞分析 R 脚本
```

## 数据库说明

`db/pns-scrna.xlsx` 为主数据库，采用 5 表结构：

| Sheet | 说明 | 当前条目 |
|-------|------|---------|
| papers | 文章登记表 | P0006（Direder 2022）、P0007（Toma 2020） |
| datasets | 数据集去重主表 | GSE181316、GSE147285 |
| cell_types | 细胞类型表 | 23 条（含 is_pns_cell 标注） |
| cell_subtypes | 细胞亚群详表 | 10 条（施万细胞亚型） |
| processing | 分析流程表 | 2 条 |

## 设计规范

数据库设计遵循 `pns-scrna-database/SKILL.md` 中的规范：
- 以 `dataset_id`（GSE 号）为去重主键
- 缺失值统一填 `NA`，布尔值为 `true`/`false`
- 多值字段用英文分号 `;` 分隔
- `provenance` 必填（可溯源到原文图表）

---

*最后更新：2026-06-07*
