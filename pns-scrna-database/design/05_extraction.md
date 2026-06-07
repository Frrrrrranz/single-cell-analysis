# 05 · 信息提取 SOP + DeepSeek 提取 Prompt + Few-shot（外周神经 scRNA 数据库）

> 本文件是「运行期 DeepSeek V4 把一篇合格文章变成结构化 JSON」的决定性操作手册。
> 读者 = Hermes（调度）+ DeepSeek V4（执行 LLM 任务）。照搬即可，运行期不再依赖 Claude。
>
> **绝对底线（先记住这 6 条）**
> 1. **字段名以 `01_schema.md` 为唯一真源**。本文件 JSON 的每个 key 必须和 schema 的 CSV 列名**逐字一致**（大小写、下划线都一致）。
> 2. **词表取值以 `02_controlled_vocab.md` 为唯一真源**。组织/平台/细胞类型/工具一律先映射成「标准名」再写入。
> 3. **缺失填 `NA`（大写两字母），严禁臆造**。原文没写就是 `NA`。
> 4. **每条 cell_types / processing 记录必须有 `provenance`**（可追回原文证据：Fig.2B / Table S3 / Methods/段名 / GEO:GSE号）。
> 5. **marker 大小写按物种**：human 全大写 `SOX10`；mouse/rat 首字母大写其余小写 `Sox10`。
> 6. **内部 ID（paper_id/ct_id/proc_id）不由 DeepSeek 生成**，一律写占位 `__AUTO__`，由入库脚本（07）赋号。dataset_id 用**真实**登记号（GSE 优先），绝不自造。
>
> ⚠️ 关于 02 词表里的 `assay` / `category` / `analysis_tools` 三个名字：**它们不是 schema 字段**，只是词表的内部分类概念。落到 JSON 时必须按下表「02 概念 → 01 字段」对照转换，**不要**在 JSON 里凭空造出 `assay`/`category`/`analysis_tools` 这些 key。

---

## §0 「02 词表概念」→「01 schema 字段」对照表（强制先看，避免造错字段）

| 02 词表里的概念 | 02 的叫法 | 实际写入 01 的哪个字段 | 转换规则 |
|---|---|---|---|
| 单核 vs 单细胞 | `assay`（snRNA-seq / scRNA-seq） | **并入 `datasets.platform`** | 单核数据：在 platform 标准名后用 `;` 追加 `snRNA-seq`，如 `10x Chromium 3' v3;snRNA-seq`。单细胞：不加后缀。无平台信息仅知单核 → `platform = snRNA-seq`。 |
| 细胞大类枚举 | `category`（sensory_neuron 等 8 类） | **不单独入库**（无此字段） | 仅用于 DeepSeek 内部判断 `is_pns_cell`；最终 JSON 不输出 category。 |
| 分析工具合集 | `analysis_tools`（分号串） | **拆进 `processing` 的各专用列** | 按工具功能分配：QC 类→`qc`；标准化→`normalization`；批次→`batch_correction`；聚类→`clustering`；轨迹→`trajectory`；通讯→`cell_comm`；DE→`diff_expr`；框架+版本→`software`；降维→`dim_reduction`；富集/通路(GO/KEGG/GSEA/Metascape 等)→`enrichment`。 |

> 记牢：JSON 的合法 key 只能来自 §3 给出的三块骨架。任何 schema 没有的 key 都是错误，入库脚本会拒收。

---

## §1 提取 SOP（标准作业流程）

### 1.1 触发条件
仅对 `papers.status = qualified`（主人已 QQ 裁决合格）的文章执行提取。pending/rejected 不提取。

### 1.2 输入材料（位于 `raw/<paper_id>/`）
按优先级使用，**所有可得材料都要读**，不要只看摘要：
1. **正文全文**（OA：Europe PMC / PMC 的 XML 或 HTML；或下载的 PDF 转出的文本）—— 主要看 Methods、Results。
2. **补充材料**（supplementary PDF / Excel / Word）—— 细胞数、亚群 marker 表、QC 参数常在此。
3. **GEO 元数据**（`raw/<paper_id>/geo_<GSE>.txt`，由检索脚本 efetch db=gds 抓取）—— platform、n_samples、物种、data type 的权威来源。
4. 文章图注（figure legends）—— 亚群命名、marker、UMAP 分群常在图注。

### 1.3 提取单位 = dataset_id（一篇可能含多个数据集，必须拆分）
- 一篇文章若产出/使用**多个 GSE**（例如一个 GSE 是 DRG、另一个是坐骨神经），**每个 dataset_id 各跑一次提取、各出一份 JSON**。
- 判断「几个数据集」：以 GEO 登记的 SuperSeries/SubSeries、或文章明确区分的不同组织/不同物种批次为界。拿不准时**按 GEO 实际登记的独立 GSE 号**拆。
- **跨物种**：同一 GSE 内含 human+mouse，`datasets.species = human;mouse`；但 `cell_types.species` 是**单值**，同类细胞在两物种各测到 → 拆成两行（见 §3.2）。

### 1.4 去重（DeepSeek 负责标注，入库脚本负责强制）
- DeepSeek 在每份 JSON 顶部 `dataset.dataset_id` 写明真实登记号。
- **是否已存在由脚本判断**，DeepSeek 不查库。但若文章明确写「我们复用了 GSExxxxx（他人数据）」，DeepSeek 照常提取该 dataset 的 cell_types/processing，并在 `processing.provenance` 注明再分析出处；入库脚本会据 dataset_id 去重，仅追加 paper_ids、仅新增 processing 行。

### 1.5 三表各自要填什么（papers 表预筛已建，提取阶段只补 `dataset_ids`，不在此 JSON 内）
- **datasets**：1 个 dataset_id 一行（本 JSON 的 `dataset` 块）。
- **cell_types**：该数据集里识别出的每一种（亚）细胞类型一行（本 JSON 的 `cell_types` 数组，每元素一行）。
- **processing**：该数据集在本文中的一套下游流程一行（本 JSON 的 `processing` 块）。

> **paper_id 从哪来（运行期入库契约 · 与 07 脚本对齐）**：提取是针对 `raw/<paper_id>/` 做的，paper_id 已知，**不写进 JSON**。Hermes 入库时通过命令行传入：
> ```
> python validate.py <本次提取JSON>                 # 先校验
> python ingest.py --db D:/database/db --json <本次提取JSON> --paper-id <paper_id>   # 校验通过再入库
> ```
> ingest.py 据此回填 `processing.paper_id`、`datasets.paper_ids`、`papers.dataset_ids` 镜像，并把该 paper 的 status 由 `qualified` 推进到 `extracted`。
> 若该 paper 尚未在 papers.csv（如黄金标准首测），加 `--paper-meta <题录JSON>` 一并新建。

### 1.6 合格性自检（提取完成前 DeepSeek 必须自查，不达标在 JSON 里报警）
一个数据集要算合格，必须同时满足：
- `datasets.species ∈ {human, mouse, rat}`；
- 关联文章 `has_scrna = true`（预筛已定）；
- `cell_types` 中**至少 1 条 `is_pns_cell = true`**。
- 若自查发现 0 条 `is_pns_cell=true`，**不要**强行把微环境细胞改成 true。在 JSON 末尾 `_self_check` 里写 `"qualified": false` 并说明原因，交人工复核。

---

## §2 给 DeepSeek 的提取 Prompt（逐字可照搬，作为 system+user 拼接）

> Hermes 调用 DeepSeek 时，把下面 ```PROMPT``` 块整体作为 system 提示；把「材料」用 `===== 材料开始 =====` / `===== 材料结束 =====` 包裹后作为 user 内容追加。词表（02）三张关键表（细胞类型、组织、平台、工具）作为附录拼进 system，确保 DeepSeek 手边有标准名。

```PROMPT
你是外周神经系统(PNS)单细胞数据库的"信息提取器"。你的唯一任务：把给定的一篇已裁决合格文章的材料(正文+补充+GEO元数据)，针对【一个指定的 dataset_id】，抽取成严格 JSON。你不做判断合格与否(已合格)，只做忠实抽取。

【铁律】
1. 只输出 JSON，不输出任何解释、前言、Markdown 代码围栏、注释。JSON 必须能被 json.loads 直接解析。
2. 字段名严格等于下方"JSON 骨架"给出的 key，一个不多一个不少，大小写下划线完全一致。禁止新增 key(如 assay/category/analysis_tools 都不是合法 key)。
3. 缺失/未提及/不适用 → 填字符串 "NA"(大写)。严禁臆造、严禁猜测、严禁用 null/None/-/未知/空字符串。
4. 多值字段用英文分号 ";" 分隔，分号两侧不留空格(如 "MPZ;MBP")。单值不加尾随分号。**分号只作字段级分隔符，禁止嵌入括号内部**：括号内若需并列多个值，改用斜杠 "/"，例如写 "time_series(0d/1d/3d/7d)"、"doublet_removal(neurons=Rbfox3/glia=Mbp)"，绝不可写 "time_series(0d;1d;3d;7d)"(会被下游按 ; 拆碎成无效碎片)。
5. 布尔值只允许 "true"/"false"(小写字符串)。判不准的 is_pns_cell/has_scrna 才可填 "NA"。
6. 内部主键不要生成：dataset 块的 dataset_id 用真实登记号(GSE优先,保持官方大写)；其余内部 ID 不出现在 JSON(脚本赋号)。
7. provenance 必填且必须可定位：用 "Fig.2B" / "Fig.S4" / "Table 1" / "Table S3" / "Methods/<小标题>" / "Results/<要点>" / "GEO:<GSE号>" / "Supplementary Methods" 这类锚点。多来源用 ";" 串。严禁写 "paper"/"原文"/"见上"。
8. marker 大小写按该记录的 species：human→全大写(SOX10)；mouse/rat→首字母大写其余小写(Sox10)。跨物种同基因须按各自规范分行书写。
9. 一切组织/平台/细胞类型/分析工具，必须先映射到【附录词表】的"标准名"再写。原文同义词→标准名。词表里找不到的，保留原文并在该值后加 "(uncontrolled)"，不要强套最近的名。

【从哪里找(字段定位指南)】
- dataset.dataset_id / repository / accession_url：GEO 元数据页(geo_*.txt)、文章 Data availability 段。GSE→repository=GEO。
- dataset.platform：Methods 建库测序段 + GEO 的 platform(GPL)行。单核数据在标准名后加 ";snRNA-seq"。仅"10x Chromium"无版本→"10x Chromium 3' (version NA)"。
- dataset.vendor：由 platform 推 10x Genomics/BD/Parse/Illumina/BGI-MGI/Fluidigm/other。
- dataset.species：GEO organism 行 + 正文。只允许 human/mouse/rat，多物种 ";"。
- dataset.tissue：正文标题/Methods 取材段/图注。映射到组织词表标准名(DRG/Sciatic nerve/...)。DRG+脊髓同篇只取外周(DRG)，脊髓不写。
- dataset.condition：实验设计段。健康/损伤模型(SNI/SNL/CCI/axotomy)/炎症(CFA)/糖尿病/化疗等。归一为"大类(模型缩写)"。未提→NA。
- dataset.n_cells：QC 后通过的细胞/核总数(整数,无千分位逗号)。优先正文"after QC, X cells"；否则补充表。给区间取主报告整数。未提→NA。
- dataset.n_samples：样本/动物/供体数。Methods 或样本表。未提→NA。
- dataset.data_availability：能下原始 counts/fastq=raw；仅处理后矩阵=processed；两者=both；受控(EGA/dbGaP)=restricted。看 GEO supplementary 文件类型 + Data availability 段。
- cell_types[*].cell_type：图注/Results 分群命名/补充亚群表。映射细胞类型词表标准名。
- cell_types[*].is_pns_cell：见下"is_pns_cell 判定"。
- cell_types[*].subtype：更细亚群名(peptidergic nociceptor/myelinating 等)。**本库只重点填外周神经细胞(is_pns_cell=true)的亚群，非 PNS 细胞填 NA**；更细亚群用 cell_subtypes[]。无细分→NA。
- cell_types[*].markers：该群定义/富集 marker。图注、marker 热图、补充 marker 表。按物种大小写。
- cell_types[*].species：该行单一物种(human/mouse/rat)。
- cell_types[*].n_cells_or_pct：该群细胞数(整数)或占比(带%)。原文给什么记什么。未提→NA。
- cell_types[*].annotation_method：manual-marker/SingleR/CellTypist/Azimuth/scANVI/reference-mapping/other。Methods 注释段。未提→NA。
- cell_subtypes[*]（**可选**,仅当论文对某大类做了亚群 subclustering 时填,每亚群一元素）：parent_cell_type=亚群所属大类标准名(如 Schwann cell)；subtype=论文自报亚群名(如 SC-Keloid)；is_pns_cell 继承大类；species 单值；condition_specificity=条件特异(keloid-specific/shared/skin-specific 等)；markers=亚群定义基因(按物种大小写)；functional_signature=功能签名(de-differentiated/pro-fibrotic 等,括号内并列用 /)；n_cells_or_pct；lineage=分化谱系(括号内用 /)；provenance 必填(如 Fig.3A)。没有亚群细分→输出空数组 []。
- processing.qc：QC 阈值(min_genes/min_counts/mito%/双细胞工具)，Methods QC 段。多项 ";"。未提→NA。
- processing.normalization：LogNormalize/SCTransform/scran/TPM/other。未提→NA。
- processing.batch_correction：Harmony/scVI/Seurat-CCA/Seurat-RPCA/fastMNN/BBKNN。明确没做→none；没提→NA。
- processing.dim_reduction：按流程顺序 "PCA;UMAP" / "PCA;tSNE"。未提→NA。
- processing.clustering：Leiden/Louvain(带分辨率如 "Leiden(res=1.0)")。未提→NA。
- processing.annotation：整体策略 marker-based/reference-mapping/mixed。未提→NA。
- processing.diff_expr：Wilcoxon/MAST/pseudobulk-DESeq2/edgeR/t-test。没做→none；没提→NA。
- processing.trajectory：Monocle2/Monocle3/Slingshot/PAGA/scVelo。没做→none；没提→NA。
- processing.cell_comm：CellChat/CellPhoneDB/NicheNet/LIANA。没做→none；没提→NA。
- processing.enrichment：富集/通路分析，记「类型(工具)」如 "GO(Metascape)"/"GO/KEGG(clusterProfiler)"/"GSEA"。Methods 富集段/GO-KEGG 结果。括号内并列用 "/"。没做→none；没提→NA。
- processing.software：主框架+版本，如 "Seurat v5;Cell Ranger 7.0"。未提→NA。

【is_pns_cell 判定(本库重点,务必准确)】
- true(外周神经/胶质,神经嵴源)：sensory neuron 各亚群、sympathetic/parasympathetic neuron、enteric neuron、Schwann cell(髓鞘/Remak/repair/SCP/terminal)、satellite glia(SGC)、enteric glia。
- "NA"·边界(神经嵴源但非神经元/胶质,功能争议→交人工)：chromaffin cell(肾上腺髓质嗜铬细胞,神经嵴源、与交感神经元同源,但功能为内分泌)、olfactory sensory neuron(嗅感觉神经元,嗅觉系统 PNS/CNS 归属学界有争议)——这两类填 is_pns_cell="NA" 并在 _self_check.notes 说明,交人工裁决,不要默认 true。
- false(微环境,非神经嵴主体)：fibroblast、macrophage/免疫(T/B/NK/DC/mast/中性粒)、endothelial、pericyte/SMC、erythrocyte、adipocyte、skeletal muscle 等——即使采自外周神经组织，这些本身仍记 false。
- "NA"：证据不足、命名含糊(如只写 "glia" 无 marker 无法区分施万/卫星/中枢)→ 填 NA 触发人工复核,不要默认 false。
- 中枢污染细胞(astrocyte/oligodendrocyte/OPC/microglia/ependymal/CNS neuron)：按边界规则【不写入 cell_types】(只取外周部分)。若不得不记录其存在,is_pns_cell=false 且在 provenance 注明,但优先剔除。
- 关键区分：SGC vs Schwann 都 SOX10+/S100B+，靠 FABP7;KCNJ10;GLUL(SGC高)且位于神经节内环绕胞体。EGC(SOX10+) vs 中枢星形胶质(SOX10−/AQP4+)。

【输出 JSON 骨架(只填这些 key)】
{
  "dataset_id": "<本次提取的 dataset_id,回显>",
  "dataset": {
    "dataset_id": "", "repository": "", "accession_url": "",
    "platform": "", "vendor": "", "species": "", "tissue": "",
    "condition": "", "n_cells": "", "n_samples": "", "data_availability": ""
  },
  "cell_types": [
    {
      "cell_type": "", "is_pns_cell": "", "subtype": "", "markers": "",
      "species": "", "n_cells_or_pct": "", "annotation_method": "", "provenance": ""
    }
  ],
  "cell_subtypes": [
    {
      "parent_cell_type": "", "subtype": "", "is_pns_cell": "", "species": "",
      "condition_specificity": "", "markers": "", "functional_signature": "",
      "n_cells_or_pct": "", "lineage": "", "provenance": ""
    }
  ],
  "processing": {
    "qc": "", "normalization": "", "batch_correction": "", "dim_reduction": "",
    "clustering": "", "annotation": "", "diff_expr": "", "trajectory": "",
    "cell_comm": "", "enrichment": "", "software": "", "provenance": ""
  },
  "_self_check": {
    "qualified": "true/false", "n_pns_cell_types": <整数>,
    "uncontrolled_terms": ["<词表外术语,无则空数组>"],
    "notes": "<拿不准/需人工复核处,无则 NA>"
  }
}

注意：dataset.paper_ids 与各表内部 ID 不在此 JSON 内(由脚本据 paper_id 上下文补)。cell_types/cell_subtypes/processing 的 dataset_id、processing 的 paper_id、cell_subtypes 的 subtype_id 也由脚本回填,你不写。cell_subtypes 为可选：仅当论文对某细胞大类做了亚群 subclustering 才填(每亚群一元素)，否则输出空数组 []。
现在只针对指定的 dataset_id 抽取,只输出 JSON。
```

> Hermes 拼接示例（伪代码）：
> `system = PROMPT + "\n\n【附录词表】\n" + 细胞类型表 + 组织表 + 平台表 + 工具表`
> `user = "【本次 dataset_id】" + GSE号 + "\n===== 材料开始 =====\n" + 正文+补充+GEO + "\n===== 材料结束 ====="`

---

## §3 输出格式（严格 JSON · 与 schema 字段逐一对应）

### 3.1 顶层结构
```json
{
  "dataset_id": "GSE...",
  "dataset":    { /* 对应 datasets 表 11 列中由 LLM 提取的部分 */ },
  "cell_types": [ /* 数组,每元素 = cell_types 表一行 */ ],
  "cell_subtypes":[ /* 可选数组,每元素 = cell_subtypes 表一行(亚群);无则 [] */ ],
  "processing": { /* 对应 processing 表的方法列 */ },
  "_self_check":{ /* 非入库,供 Hermes 质检与人工复核路由 */ }
}
```

### 3.2 字段映射表（JSON key → schema CSV 列，含谁来填）

`dataset` 块 → `datasets` 表：

| JSON key | schema 列 | 谁填 | 备注 |
|---|---|---|---|
| dataset_id | dataset_id | DeepSeek | 真实 GSE，官方大写 |
| repository | repository | DeepSeek | GEO/SRA/ArrayExpress/Zenodo/EGA/other |
| accession_url | accession_url | DeepSeek | GEO acc 链接 |
| platform | platform | DeepSeek | 标准名；单核加 `;snRNA-seq` |
| vendor | vendor | DeepSeek | 由平台推 |
| species | species | DeepSeek | human/mouse/rat 多值`;` |
| tissue | tissue | DeepSeek | 组织标准名 |
| condition | condition | DeepSeek | 归一；未提 NA |
| n_cells | n_cells | DeepSeek | 整数无逗号 |
| n_samples | n_samples | DeepSeek | 整数 |
| data_availability | data_availability | DeepSeek | raw/processed/both/restricted |
| —（不在 JSON）| paper_ids | 脚本 | 据 paper_id 上下文回填，DeepSeek 不写 |

`cell_types[*]` → `cell_types` 表：

| JSON key | schema 列 | 谁填 | 备注 |
|---|---|---|---|
| —（不在 JSON）| ct_id | 脚本 | `__AUTO__` 赋号 |
| —（不在 JSON）| dataset_id | 脚本 | 回填本数据集 |
| cell_type | cell_type | DeepSeek | 标准名 |
| is_pns_cell | is_pns_cell | DeepSeek | true/false/NA |
| subtype | subtype | DeepSeek | 无→NA |
| markers | markers | DeepSeek | 按物种大小写 |
| species | species | DeepSeek | 单值 |
| n_cells_or_pct | n_cells_or_pct | DeepSeek | 数或% |
| annotation_method | annotation_method | DeepSeek | 词表枚举 |
| provenance | provenance | DeepSeek | 必填锚点 |

`cell_subtypes[*]` → `cell_subtypes` 表（**可选**；论文做了亚群 subclustering 才填，每亚群一元素）：

| JSON key | schema 列 | 谁填 | 备注 |
|---|---|---|---|
| —（不在 JSON）| subtype_id | 脚本 | `__AUTO__` 赋号(S00001) |
| —（不在 JSON）| dataset_id | 脚本 | 回填本数据集 |
| parent_cell_type | parent_cell_type | DeepSeek | 亚群所属大类标准名(软关联 cell_types) |
| subtype | subtype | DeepSeek | 论文自报亚群名 |
| is_pns_cell | is_pns_cell | DeepSeek | 继承大类 true/false/NA |
| species | species | DeepSeek | 单值 |
| condition_specificity | condition_specificity | DeepSeek | 条件特异；无→NA |
| markers | markers | DeepSeek | 按物种大小写 |
| functional_signature | functional_signature | DeepSeek | 功能签名；括号内用 / |
| n_cells_or_pct | n_cells_or_pct | DeepSeek | 数或% |
| lineage | lineage | DeepSeek | 分化谱系；括号内用 / |
| provenance | provenance | DeepSeek | 必填锚点 |

`processing` 块 → `processing` 表：

| JSON key | schema 列 | 谁填 | 备注 |
|---|---|---|---|
| —（不在 JSON）| proc_id | 脚本 | `__AUTO__` |
| —（不在 JSON）| dataset_id | 脚本 | 回填 |
| —（不在 JSON）| paper_id | 脚本 | 回填本文 paper_id |
| qc | qc | DeepSeek | |
| normalization | normalization | DeepSeek | |
| batch_correction | batch_correction | DeepSeek | none/NA 区分 |
| dim_reduction | dim_reduction | DeepSeek | 按顺序 |
| clustering | clustering | DeepSeek | |
| annotation | annotation | DeepSeek | marker-based/reference-mapping/mixed |
| diff_expr | diff_expr | DeepSeek | none/NA 区分 |
| trajectory | trajectory | DeepSeek | none/NA 区分 |
| cell_comm | cell_comm | DeepSeek | none/NA 区分 |
| enrichment | enrichment | DeepSeek | 富集「类型(工具)」；括号内用 /；none/NA 区分 |
| software | software | DeepSeek | 框架+版本 |
| provenance | provenance | DeepSeek | 必填 |

`_self_check` 块 → **不入任何表**，仅供 Hermes 路由质检：
| key | 含义 |
|---|---|
| qualified | 本数据集是否过合格自检（≥1 条 is_pns_cell=true 且物种合法）|
| n_pns_cell_types | is_pns_cell=true 的记录数 |
| uncontrolled_terms | 用了 `(uncontrolled)` 标记的术语清单 |
| notes | 拿不准、需人工复核的说明 |

### 3.3 `none` vs `NA` 的硬区别（processing 高频错点）
- 论文**明说没做**某步（"no batch correction was performed"）→ 写 `none`。
- 论文**完全没提**该步 → 写 `NA`。
- 适用列：`batch_correction`、`diff_expr`、`trajectory`、`cell_comm`、`enrichment`。其余列没提即 `NA`（无 `none` 概念）。

---

## §4 分块策略（材料超出 DeepSeek 上下文时）

### 4.1 何时分块
单次输入（正文+补充+GEO）预估超过 DeepSeek 上下文安全线（建议留 ~30% 余量给输出）时分块。Hermes 用字符数粗估（如 > 80k 字符）即触发。

### 4.2 怎么分（按"证据所在"切，不要无脑等分）
按材料天然边界切片，每片单独喂给 DeepSeek，**每片都带同一套 PROMPT + 同一 dataset_id**：
- **片 A · 数据集元信息**：标题 + Abstract + Methods(取材/建库/测序/数据可得性) + GEO 元数据 → 主产出 `dataset` 块 + `processing` 块。
- **片 B · 细胞类型主体**：Results(分群/异质性) + 主图图注(UMAP/marker 热图) → 主产出 `cell_types` 数组。
- **片 C · 补充材料**：补充表(亚群 marker 表 / per-cluster 细胞数 / QC 参数表) → 补全/校正 `cell_types` 与 `processing`。
- 大补充 Excel：**按表（sheet/Table 编号）切**，一张大 marker 表一片。

每片在 prompt 末尾加一行指示，告诉 DeepSeek 本片**只可能**含哪些块，其余块该片输出空/占位：
- 片 A：`本片只产出 dataset 与 processing；cell_types 输出空数组 []。`
- 片 B/C：`本片只产出 cell_types；dataset 与 processing 输出空对象 {} 或沿用占位。`

### 4.3 怎么合并去重（脚本做，确定性，不用 LLM）
Hermes 调用合并脚本，规则：
1. **dataset 块**：以片 A 为准；其它片若也产出 dataset 字段，仅当片 A 为 `NA` 时用非 NA 值补洞，冲突时片 A 优先并记日志。
2. **processing 块**：以片 A 为主，片 C（补充 Methods）补 `NA` 洞。
3. **cell_types 合并去重键 = `(cell_type, subtype, species)` 三元组**：
   - 同键多片重复 → 合并为一条；`markers` 取并集（按 `;` 拆分去重再拼），`n_cells_or_pct` 取**有数值的非 NA**（补充表的精确值优先于正文约值），`provenance` 取并集（`;` 串），`is_pns_cell` 冲突时 true/false 不一致 → 置 `NA` 并写入 `_self_check.notes` 报警。
   - 不同键 → 各自保留为独立行。
4. `_self_check`：合并后由脚本重新统计 `n_pns_cell_types`、汇总各片 `uncontrolled_terms`、重算 `qualified`。
5. 合并产物再过一次入库脚本（07）的字段校验（枚举/bool/NA/marker 大小写）。

### 4.4 多 dataset 文章
先按 §1.3 拆 dataset_id，**每个 dataset_id 独立走 4.1–4.3 全流程**，互不混合。合并只在同一 dataset_id 的分片之间进行。

---

## §5 完整 Few-shot 范例（输入材料片段 → 完整 JSON 输出，可照搬）

> 下列范例的 marker、亚群命名均按 02 词表与领域共识构造，体现 provenance 与 NA 的正确用法。DeepSeek 应模仿其**结构与严谨度**，不是抄其内容。

### 范例 1 · 小鼠 DRG 10x 数据集（含 Schwann/SGC/感觉神经元亚群 + marker）

**输入材料片段（节选，模拟 raw/P0001/ 内容）：**

> *Title:* Single-cell transcriptomic atlas of the mouse dorsal root ganglion.
> *Methods — Tissue & library:* Lumbar (L4–L6) dorsal root ganglia were dissected from 8 adult C57BL/6 mice (4 male, 4 female). Single-cell suspensions were processed using the 10x Genomics Chromium Single Cell 3′ Reagent Kit v3. Libraries were sequenced on Illumina NovaSeq 6000.
> *Methods — Processing:* Reads were aligned with Cell Ranger 6.1. Low-quality cells (<500 genes or >10% mitochondrial reads) were removed; doublets were filtered with DoubletFinder. Data were normalized using SCTransform, integrated across animals with Harmony, reduced by PCA and UMAP, and clustered using the Leiden algorithm (resolution 1.2). Cell types were annotated manually with canonical markers. Differential expression used the Wilcoxon rank-sum test in Seurat v4.
> *Results:* After QC, 21,455 cells were retained. We resolved peptidergic nociceptors (Calca, Tac1, Trpv1), non-peptidergic nociceptors (Mrgprd, P2rx3), C-LTMRs (Th, Slc17a8), proprioceptors (Pvalb, Runx3), satellite glial cells (Fabp7, Kcnj10), and myelinating Schwann cells (Mpz, Mbp). Endothelial cells (Pecam1) and macrophages (Aif1) were also present.
> *Fig.1C:* UMAP with the above clusters. *Table S2:* per-cluster cell counts (peptidergic 4120; non-peptidergic 3890; C-LTMR 1560; proprioceptor 980; SGC 5230; myelinating SC 410; endothelial 2310; macrophage 2955).
> *Data availability:* Raw and processed data are available at GEO accession GSE190000.
> *GEO geo_GSE190000.txt:* Organism: Mus musculus; Platform: GPL24247 Illumina NovaSeq 6000 (Mus musculus); Series type: Expression profiling by high throughput sequencing.

**输出 JSON：**
```json
{
  "dataset_id": "GSE190000",
  "dataset": {
    "dataset_id": "GSE190000",
    "repository": "GEO",
    "accession_url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE190000",
    "platform": "10x Chromium 3' v3",
    "vendor": "10x Genomics",
    "species": "mouse",
    "tissue": "DRG",
    "condition": "healthy",
    "n_cells": "21455",
    "n_samples": "8",
    "data_availability": "both"
  },
  "cell_types": [
    {
      "cell_type": "sensory neuron",
      "is_pns_cell": "true",
      "subtype": "peptidergic nociceptor",
      "markers": "Calca;Tac1;Trpv1",
      "species": "mouse",
      "n_cells_or_pct": "4120",
      "annotation_method": "manual-marker",
      "provenance": "Results/sensory neuron subtypes;Fig.1C;Table S2"
    },
    {
      "cell_type": "sensory neuron",
      "is_pns_cell": "true",
      "subtype": "non-peptidergic nociceptor",
      "markers": "Mrgprd;P2rx3",
      "species": "mouse",
      "n_cells_or_pct": "3890",
      "annotation_method": "manual-marker",
      "provenance": "Results/sensory neuron subtypes;Fig.1C;Table S2"
    },
    {
      "cell_type": "sensory neuron",
      "is_pns_cell": "true",
      "subtype": "C-LTMR",
      "markers": "Th;Slc17a8",
      "species": "mouse",
      "n_cells_or_pct": "1560",
      "annotation_method": "manual-marker",
      "provenance": "Results/sensory neuron subtypes;Fig.1C;Table S2"
    },
    {
      "cell_type": "sensory neuron",
      "is_pns_cell": "true",
      "subtype": "proprioceptor",
      "markers": "Pvalb;Runx3",
      "species": "mouse",
      "n_cells_or_pct": "980",
      "annotation_method": "manual-marker",
      "provenance": "Results/sensory neuron subtypes;Fig.1C;Table S2"
    },
    {
      "cell_type": "satellite glia",
      "is_pns_cell": "true",
      "subtype": "NA",
      "markers": "Fabp7;Kcnj10",
      "species": "mouse",
      "n_cells_or_pct": "5230",
      "annotation_method": "manual-marker",
      "provenance": "Results/glial populations;Fig.1C;Table S2"
    },
    {
      "cell_type": "Schwann cell",
      "is_pns_cell": "true",
      "subtype": "myelinating",
      "markers": "Mpz;Mbp",
      "species": "mouse",
      "n_cells_or_pct": "410",
      "annotation_method": "manual-marker",
      "provenance": "Results/glial populations;Fig.1C;Table S2"
    },
    {
      "cell_type": "endothelial",
      "is_pns_cell": "false",
      "subtype": "NA",
      "markers": "Pecam1",
      "species": "mouse",
      "n_cells_or_pct": "2310",
      "annotation_method": "manual-marker",
      "provenance": "Results/non-neuronal cells;Fig.1C;Table S2"
    },
    {
      "cell_type": "macrophage/immune",
      "is_pns_cell": "false",
      "subtype": "NA",
      "markers": "Aif1",
      "species": "mouse",
      "n_cells_or_pct": "2955",
      "annotation_method": "manual-marker",
      "provenance": "Results/non-neuronal cells;Fig.1C;Table S2"
    }
  ],
  "processing": {
    "qc": "min_genes=500;mito%<10;DoubletFinder",
    "normalization": "SCTransform",
    "batch_correction": "Harmony",
    "dim_reduction": "PCA;UMAP",
    "clustering": "Leiden(res=1.2)",
    "annotation": "marker-based",
    "diff_expr": "Wilcoxon",
    "trajectory": "NA",
    "cell_comm": "NA",
    "software": "Cell Ranger 6.1;Seurat v4",
    "provenance": "Methods/Processing"
  },
  "_self_check": {
    "qualified": "true",
    "n_pns_cell_types": 6,
    "uncontrolled_terms": [],
    "notes": "NA"
  }
}
```

> 范例 1 要点：①8 个分群各一行；②6 条神经/胶质 `is_pns_cell=true`，2 条微环境 `false`；③感觉神经元用大类 `sensory neuron` + `subtype` 区分亚群（不把亚群名塞进 cell_type）；④marker 全部小鼠首字母大写；⑤`trajectory`/`cell_comm` 论文没提 → `NA`（不是 none，因为没说"没做"，只是没提）；⑥`data_availability=both`（GEO 有 raw+processed）；⑦provenance 串联 Results+Fig+Table 三处。

---

### 范例 2 · 大鼠坐骨神经损伤数据集（含损伤条件 + 修复型 Schwann + snRNA）

**输入材料片段（节选，模拟 raw/P0002/ 内容）：**

> *Title:* Single-nucleus RNA-seq reveals Schwann cell reprogramming after rat sciatic nerve crush injury.
> *Methods:* Sciatic nerves from adult Sprague-Dawley rats were collected 7 days after crush injury (injury group, n=3) and from uninjured contralateral nerves (control, n=3). Nuclei were isolated and profiled by single-nucleus RNA sequencing on the 10x Genomics Chromium platform (3′ v3.1 chemistry). Sequencing on Illumina NovaSeq.
> *Methods — Analysis:* Cell Ranger 7.0 with intronic reads included. After removing nuclei with <300 genes or >5% mitochondrial content, 14,082 nuclei passed QC. Ambient RNA was corrected with SoupX. No batch correction was applied. Data were log-normalized, reduced by PCA and UMAP, and clustered with Louvain. Trajectory analysis of the Schwann cell lineage used Monocle3. Cell–cell communication was inferred with CellChat. Cell types annotated using SingleR with a peripheral nerve reference.
> *Results:* We identified myelinating Schwann cells (Mpz, Prx), non-myelinating (Remak) Schwann cells (Ncam1, Scn7a), and a prominent population of repair Schwann cells expressing Ngfr, Gap43, and Atf3 that expanded after injury. Endoneurial fibroblasts (Pdgfra, Col1a1) and macrophages (Cd68) were also captured. *Fig.3A* shows the Schwann cell trajectory; repair Schwann cells comprised 38.5% of all Schwann cells in the injury group.
> *Supplementary Table S4:* cluster markers and counts (myelinating SC 2110; Remak SC 1875; repair SC 3320; endoneurial fibroblast 4100; macrophage 2677).
> *Data availability:* Processed count matrices are deposited at GEO (GSE205500). Raw sequencing reads are under controlled access at EGA (EGAS00001000000).
> *GEO geo_GSE205500.txt:* Organism: Rattus norvegicus; Series type: Expression profiling by high throughput sequencing (single nucleus).

**输出 JSON：**
```json
{
  "dataset_id": "GSE205500",
  "dataset": {
    "dataset_id": "GSE205500",
    "repository": "GEO",
    "accession_url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205500",
    "platform": "10x Chromium 3' v3;snRNA-seq",
    "vendor": "10x Genomics",
    "species": "rat",
    "tissue": "sciatic nerve",
    "condition": "healthy;nerve injury(crush)",
    "n_cells": "14082",
    "n_samples": "6",
    "data_availability": "both"
  },
  "cell_types": [
    {
      "cell_type": "Schwann cell",
      "is_pns_cell": "true",
      "subtype": "myelinating",
      "markers": "Mpz;Prx",
      "species": "rat",
      "n_cells_or_pct": "2110",
      "annotation_method": "SingleR",
      "provenance": "Results/Schwann cell populations;Table S4"
    },
    {
      "cell_type": "Schwann cell",
      "is_pns_cell": "true",
      "subtype": "non-myelinating/Remak",
      "markers": "Ncam1;Scn7a",
      "species": "rat",
      "n_cells_or_pct": "1875",
      "annotation_method": "SingleR",
      "provenance": "Results/Schwann cell populations;Table S4"
    },
    {
      "cell_type": "Schwann cell",
      "is_pns_cell": "true",
      "subtype": "repair",
      "markers": "Ngfr;Gap43;Atf3",
      "species": "rat",
      "n_cells_or_pct": "38.5%",
      "annotation_method": "SingleR",
      "provenance": "Results/repair Schwann cells;Fig.3A;Table S4"
    },
    {
      "cell_type": "fibroblast",
      "is_pns_cell": "false",
      "subtype": "endoneurial fibroblast",
      "markers": "Pdgfra;Col1a1",
      "species": "rat",
      "n_cells_or_pct": "4100",
      "annotation_method": "SingleR",
      "provenance": "Results/non-Schwann cells;Table S4"
    },
    {
      "cell_type": "macrophage/immune",
      "is_pns_cell": "false",
      "subtype": "NA",
      "markers": "Cd68",
      "species": "rat",
      "n_cells_or_pct": "2677",
      "annotation_method": "SingleR",
      "provenance": "Results/non-Schwann cells;Table S4"
    }
  ],
  "processing": {
    "qc": "min_genes=300;mito%<5;SoupX",
    "normalization": "LogNormalize",
    "batch_correction": "none",
    "dim_reduction": "PCA;UMAP",
    "clustering": "Louvain",
    "annotation": "reference-mapping",
    "diff_expr": "NA",
    "trajectory": "Monocle3",
    "cell_comm": "CellChat",
    "software": "Cell Ranger 7.0",
    "provenance": "Methods/Analysis"
  },
  "_self_check": {
    "qualified": "true",
    "n_pns_cell_types": 3,
    "uncontrolled_terms": [],
    "notes": "snRNA-seq单核;repair SC占比为占Schwann总数38.5%(原文未给绝对数),记入n_cells_or_pct;raw读段在EGA受控,processed在GEO,故data_availability=both"
  }
}
```

> 范例 2 要点：①**snRNA-seq** → platform 标准名后加 `;snRNA-seq`；②损伤 vs 对照两条件 → `condition = healthy;nerve injury(crush)`（crush 不在 SNI/SNL/CCI 标准缩写内，照实记 crush，未加 uncontrolled 因 condition 是自由文本约定）；③三种 Schwann 用同一大类 `Schwann cell` + 不同 `subtype`，全部 `is_pns_cell=true`；④repair SC 只给占比 → `n_cells_or_pct=38.5%`；⑤`batch_correction=none`（原文明说"No batch correction was applied"，区别于"没提"的 NA）；⑥`diff_expr=NA`（确实没提 DE）；⑦marker 大鼠首字母大写；⑧data 分布在 GEO(processed)+EGA(raw 受控)，综合判 `both` 并在 notes 说明（若全部受控才填 restricted）；⑨annotation_method=SingleR，annotation 整体策略=reference-mapping，两者呼应。

---

## §6 DeepSeek 自检清单（输出 JSON 前最后过一遍）
- [ ] 只输出了 JSON，无任何多余文字/代码围栏？
- [ ] 所有 key 都在 §2 骨架内，没造出 assay/category/analysis_tools 等非法 key？
- [ ] dataset_id 是真实登记号、官方大写？没自造内部 ID？
- [ ] 每条 cell_types、processing 都有可定位的 provenance？
- [ ] marker 大小写与各行 species 匹配（human 全大写 / mouse·rat 首字母大写）？
- [ ] 缺失填 `NA`，没用空串/null/-/未知？多值用 `;` 无空格？bool 是 true/false/NA？
- [ ] batch_correction/diff_expr/trajectory/cell_comm 正确区分了 `none`（明说没做）与 `NA`（没提）？
- [ ] 组织/平台/细胞类型/工具都映射到了 02 标准名？词表外的加了 `(uncontrolled)`？
- [ ] 至少 1 条 is_pns_cell=true？否则 `_self_check.qualified=false` 并说明？
- [ ] 中枢污染细胞已剔除（未写入 cell_types），或必要时 false 并在 notes 说明？
