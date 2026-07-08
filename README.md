# PNS scRNA-seq 数据库

> 外周神经系统（PNS）单细胞 RNA 测序文献数据收集与结构化数据库

## 项目结构

```
.
├── db/                         # 数据库
│   ├── pns-scrna.xlsx          # 主数据库（5表：papers/datasets/cell_types/cell_subtypes/processing）
│   └── cellxgene/              # CellxGene 外周神经文献抓取模块
│       ├── cellxgene_all_details/    # API 原始元数据抓取与粗筛结果
│       └── cellxgene_filtered/       # 过滤后的候选文献集
│           ├── pns_papers_summary.xlsx  # 82个候选数据集状态汇总表
│           ├── manual_download_helper.html # 26篇待手动下载/损坏文献的可视化看板
│           └── downloads/            # 已下载归库且通过二次核对的规范 PDF 文献库
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
├── scripts/                    # 分析脚本
│   └── step1_scRNA.Rmd         # 单细胞分析 R 脚本
│
└── scratch/                    # 自动化抓取、剪切及纠错校验脚本库 [NEW]
    ├── download_batch.py       # 联动 OpenTabs 的 1-75 篇文献流式自动检索与触发下载脚本
    ├── organize_cellxgene_downloads.py # 关联 OpenTabs 下载记录对 PDF 剪切并重命名归库脚本
    └── verify_and_update.py    # 提取 PDF 内容二次核对、回写 Excel 并重构看板的终端大闭环脚本
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

## CellxGene 外周神经文献抓取模块说明

本模块基于 CellxGene API 全网抓取并粗筛出包含外周神经系统相关细胞（如 Schwann cell, sensory neuron 等）的单细胞数据集，建立起完整的自动化文献抓取与核对大闭环：

### 🛠️ 自动化大闭环机制
1. **自动下载流** (`download_batch.py`)：使用 `opentabs` 联动本地 Chrome 浏览器，对 1-75 篇候选文献进行学术检索与流式触发下载（内置 7s 加载 + 5s 冷却，防止被封 IP/触发人机验证），包含 sorry 验证码熔断拦截功能。
2. **剪切重命名归库** (`organize_cellxgene_downloads.py`)：通过分析 OpenTabs 下载任务日志，对下载完成 of PDF 进行物理级 Download ID 与 DOI 后缀绑定，移动并重命名为 `PMID_...pdf` 或 `DOI_...pdf` 存入 `downloads/`。
3. **二次内容校验与状态对齐** (`verify_and_update.py`)：基于 Excel 表格数据遍历 PDF，利用 PyMuPDF 提取内容，核对 PMID、DOI 及标题英文词重合度，将损坏（0字节）或错配的文章揪出，回填 Excel，并在 HTML 看板中实时隐藏已就位文献、高亮显示需干预卡片。

### 📊 阶段性战报 (2026-07-08)
* **总数据集行数**：82 个
* **已归库并成功校验**：**73 个** (完成率 **89%**)
* **当前遗留待干预**：**9 个** (主要由于无有效 DOI，或 Cell、Science 等顶级版权锁限制，记录在 HTML 面板中待手动补齐)

---

## 设计规范

数据库设计遵循 `pns-scrna-database/SKILL.md` 中的规范：
- 以 `dataset_id`（GSE 号）为去重主键
- 缺失值统一填 `NA`，布尔值为 `true`/`false`
- 多值字段用英文分号 `;` 分隔
- `provenance` 必填（可溯源到原文图表）

---

*最后更新：2026-07-08*
