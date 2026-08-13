# PNS scRNA-seq Marker 提取

> 从 CellxGene 候选论文及论文 PDF 中提取、复核和整理外周神经系统（PNS）细胞 marker。

## 项目结构

```
.
├── db/
│   ├── cellxgene/              # Marker 项目的论文登记与 PDF 语料
│   │   ├── pns_papers_summary.xlsx   # 候选论文/数据集登记表
│   │   └── cellxgene_filtered/
│   │       └── downloads/             # 当前论文 PDF 库
│   ├── pns-scrna.xlsx          # 历史累计工作簿；映射修复前不作为可靠 marker 主表
│   └── _archive/               # 历史抓取材料及可恢复旧产物，不是活动输入
│
├── scripts/
│   └── extract_markers/        # Marker 抽取、复核表生成和导入程序
│
├── .agents/
│   ├── plan/                   # 当前实施计划
│   └── progress/               # 按日期汇总的进度
│
└── papers_report/              # 旧文献汇报项目，与 marker 提取无关
```

## 当前任务边界

- 项目文献范围与 PDF 输入以 `db/cellxgene/` 为准。
- Marker 活动代码和逐篇结果位于 `scripts/extract_markers/`。
- `db/pns-scrna.xlsx` 含历史累计结果，但当前存在论文映射和复核完整性问题；修复前不能视为最终 marker 数据库。
- `papers_report/` 属于独立的旧文献汇报工作，不纳入本项目。

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

## Marker 证据原则

正式 marker 应能定位到论文正文、图表或补充材料，并区分作者明确声明/用于细胞注释的 marker 与普通差异表达基因。详细实施方案见 `.agents/plan/marker-extraction-plan.md`。

---

*最后更新：2026-08-13*
