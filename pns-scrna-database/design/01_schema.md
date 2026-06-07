# 01 · 数据库 Schema 终稿（外周神经 scRNA 数据库）

> 本文件是整个资产包的地基。所有下游文件（提取规则 04、卡片模板 06、入库脚本 07 等）**必须**与本文件字段定义、枚举取值、命名规范严格一致。
> 形态：5 张关联 CSV 表 + 1 个 SQLite 主库（`db/database.sqlite`），CSV 为唯一可手改真源，SQLite 由脚本从 CSV 重建。
> 去重核心：以 `dataset_id`（GSE 号优先）为唯一键；同一数据集被多篇文章使用时，只在 `datasets.paper_ids` 追加，**不**重复提取细胞/处理信息。
>
> 全库通用约定（先读这一段，再看各表）：
> - **编码**：所有 CSV 一律 `UTF-8`（无 BOM），`\n` 换行，逗号分隔，字段值含逗号/换行/引号时用双引号包裹并按 RFC4180 转义（`"` → `""`）。
> - **缺失值**：一律填字符串 `NA`（大写），严禁留空、严禁填 `null`/`None`/`-`/`未知`，严禁臆造。
> - **布尔值**：只允许 `true` / `false`（全小写字符串）。未知 → `NA`，不要写 `false` 冒充未知。
> - **多值字段**：同一单元格内多值用英文分号 `;` 分隔，分号两侧不留空格（`GSE111;GSE222`）。单值时就写单值，不要尾随分号。
> - **provenance（溯源）**：必填，写清证据出处，格式见文末「§字段填写规范 · provenance」。
> - **ID 大小写**：内部主键（paper_id/ct_id/proc_id）固定零填充宽度；外部登记号（GSE/DOI/PMID）保持官方原始大小写。

---

## 表关系总览（文字版关系图）

```
                       ┌──────────────────────────┐
                       │          papers          │  文章登记表（1 行 = 1 篇文章）
                       │  PK: paper_id (P0001)    │
                       └──────────────────────────┘
                         ▲   │ dataset_ids (多值;)  │
            paper_ids    │   ▼ 多对多               │ paper_id (FK)
           (多值;)        │                          │
                       ┌──────────────────────────┐ │
                       │         datasets         │ │  数据集去重主表（1 行 = 1 个数据集）
                       │  PK: dataset_id (GSE…)   │ │
                       └──────────────────────────┘ │
                         │ 1                         │
              dataset_id │   ┌───────────────────────┘
                (FK)     │   │ dataset_id (FK)
                         ▼ N ▼ N
        ┌────────────────────┐   ┌────────────────────────┐
        │     cell_types     │   │       processing       │
        │  PK: ct_id (C00001)│   │  PK: proc_id (X00001)  │
        │  FK: dataset_id    │   │  FK: dataset_id        │
        └────────────────────┘   │  FK: paper_id          │
                                  └────────────────────────┘
```

关系说明（基数）：
- `papers` ↔ `datasets`：**多对多**。一篇文章可产出/使用多个数据集；一个数据集可被多篇文章使用。双向冗余记录：`papers.dataset_ids` 与 `datasets.paper_ids` 互为镜像（入库脚本负责校验两侧一致）。
- `datasets` → `cell_types`：**一对多**。一个数据集有多条细胞类型记录。`cell_types.dataset_id` 外键指向 `datasets.dataset_id`。
- `datasets` → `cell_subtypes`：**一对多**。细胞（亚）群详表（1 行 = 一个亚群，如施万细胞的 SC-Keloid/SC-Prolif…）。`cell_subtypes.dataset_id` 外键指向 `datasets.dataset_id`；`parent_cell_type` 软关联 `cell_types.cell_type` 大类。比 `cell_types.subtype` 记录更细（含条件特异/功能签名/分化谱系）。无亚群细分的数据集可没有任何 cell_subtypes 行。
- `datasets` → `processing`：**一对多**。一个数据集可有多条处理记录（通常 1 条；若同一数据集被不同文章各自再分析，可多条，用 `paper_id` 区分）。`processing.dataset_id` 外键指向 `datasets.dataset_id`，`processing.paper_id` 外键指向 `papers.paper_id`。
- `cell_types`、`processing` **不直接关联 papers**（除 processing 的 paper_id）。文章溯源统一经由 `datasets.paper_ids` 解析，避免重复维护。

> 为什么 `papers↔datasets` 用「双向多值列」而不用独立连接表：运行期由 DeepSeek 抽取、人工 QQ 裁决，保持表结构心智简单优先；多对多一致性由入库脚本（07）在重建 SQLite 时强制校验。若后期规模变大，可在 SQLite 内派生一张 `paper_dataset_link` 视图/表，但 CSV 真源仍是双向多值列。

---

## 表 A · papers（文章登记表）

1 行 = 1 篇文章。检索阶段由 Hermes 写入（status=pending），裁决/提取阶段更新。

| 字段名 | 类型 | 必填? | 主键/外键 | 枚举取值 | 说明 |
|---|---|:---:|---|---|---|
| paper_id | TEXT | 是 | **PK** | — | 内部主键。格式 `P` + 4 位零填充序号，如 `P0001`。全库唯一、单调递增、永不复用。 |
| title | TEXT | 是 | — | — | 文章标题，原文照抄（保留大小写）。含逗号需双引号包裹。 |
| first_author | TEXT | 是 | — | — | 第一作者姓氏 + 名首字母，如 `Avraham O`。多名并列第一作者取第一位即可。未知填 `NA`。 |
| corresponding | TEXT | 否 | — | — | 通讯作者，同 first_author 格式；多通讯用 `;`。抓不到填 `NA`。 |
| year | INTEGER | 是 | — | 1990–2030 | 发表年（4 位）。预印本用上线年。未知填 `NA`。 |
| journal | TEXT | 是 | — | — | 期刊名（可用 NLM 缩写，如 `Nat Commun`）。预印本写 `bioRxiv`/`medRxiv`。 |
| doi | TEXT | 否 | — | — | DOI，**小写**，仅留裸号不带 URL 前缀（`10.1038/s41467-020-xxxxx`）。无则 `NA`。 |
| pmid | TEXT | 否 | — | — | PubMed ID，纯数字字符串。预印本/无 PMID 填 `NA`。 |
| url | TEXT | 否 | — | — | 原文稳定链接（优先 DOI 解析地址 `https://doi.org/<doi>`）。无则 `NA`。 |
| species | TEXT | 是 | — | `human` / `mouse` / `rat`（多值;） | 文章涉及的目标物种（仅限三者）。多物种用 `;`，如 `human;mouse`。 |
| has_scrna | BOOLEAN | 是 | — | `true` / `false` | 是否含 scRNA/snRNA 数据。`false` 的文章一般会 reject，但仍可登记留痕。 |
| dataset_ids | TEXT | 否 | **FK → datasets.dataset_id**（多值;） | — | 关联数据集，如 `GSE147101;GSE201234`。检索阶段可能未知，填 `NA`；提取后补全。须与 `datasets.paper_ids` 镜像一致。 |
| status | TEXT | 是 | — | `pending` / `qualified` / `rejected` / `extracted` | 流转状态：pending 待裁决 → qualified 主人裁决合格 → extracted 已结构化提取入库；rejected 淘汰（理由写 notes）。 |
| source | TEXT | 是 | — | `PubMed` / `GEO` / `OpenAlex` / `SemanticScholar` / `EuropePMC` / `bioRxiv` / `other` | 该文章的首次发现渠道。GEO 逆向检索命中填 `GEO`。 |
| suppl_path | TEXT | 否 | — | — | 本地原始资料相对路径（相对项目根），固定 `raw/<paper_id>/`，如 `raw/P0001/`。未下载填 `NA`。 |
| notes | TEXT | 否 | — | — | 备注/淘汰原因/边界判定说明（如 `仅取DRG部分，脊髓不入库`）。无则 `NA`。 |

CSV 表头行（第 1 行，逐字照抄）：
```
paper_id,title,first_author,corresponding,year,journal,doi,pmid,url,species,has_scrna,dataset_ids,status,source,suppl_path,notes
```

---

## 表 B · datasets（数据集表 · 去重主表）

1 行 = 1 个数据集。**全库去重核心**。先查 `dataset_id` 是否已存在，存在则只在 `paper_ids` 追加，不新增行、不重复提取下游。

| 字段名 | 类型 | 必填? | 主键/外键 | 枚举取值 | 说明 |
|---|---|:---:|---|---|---|
| dataset_id | TEXT | 是 | **PK** | — | 去重主键。**GEO GSE 号优先**（`GSE147101`，大写无空格）。无 GSE 时退而用：SRA(`SRPxxxxxx`/`PRJNAxxxxxx`)、ArrayExpress(`E-MTAB-xxxx`)、Zenodo(`zenodo.<id>`)、其他仓库官方号。保持官方原始大小写。 |
| repository | TEXT | 是 | — | `GEO` / `SRA` / `ArrayExpress` / `Zenodo` / `EGA` / `other` | `dataset_id` 所属仓库。与 dataset_id 前缀对应。 |
| accession_url | TEXT | 是 | — | — | 数据集页面稳定链接（如 `https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147101`）。抓不到填 `NA`。 |
| platform | TEXT | 是 | — | 见文末「§平台词表」 | 测序/建库平台标准名，如 `10x Chromium 3' v3`。多平台用 `;`。未知填 `NA`。 |
| vendor | TEXT | 否 | — | `10x Genomics` / `BD` / `Parse Biosciences` / `Illumina` / `BGI-MGI` / `Fluidigm` / `other` | 平台/仪器厂商。多值用 `;`。未知填 `NA`。 |
| species | TEXT | 是 | — | `human` / `mouse` / `rat`（多值;） | 数据集物种（仅限三者）。混合物种数据集用 `;`。 |
| tissue | TEXT | 是 | — | 见文末「§组织词表」 | 组织/解剖部位标准名，如 `DRG`、`sciatic nerve`、`ENS-myenteric`。多组织用 `;`。 |
| condition | TEXT | 否 | — | 见文末「§condition 约定」 | 实验条件，如 `healthy`、`nerve injury(SNI)`、`diabetic`。多条件用 `;`。未知填 `NA`。 |
| n_cells | INTEGER | 否 | — | ≥0 | 通过 QC 的细胞/核总数（整数，不带千分位逗号）。仅有近似值时取报告值并在 notes 不记此处。未知填 `NA`。 |
| n_samples | INTEGER | 否 | — | ≥0 | 样本/动物/供体数。未知填 `NA`。 |
| data_availability | TEXT | 是 | — | `raw` / `processed` / `both` / `restricted` | raw=可下原始 counts/fastq；processed=仅处理后矩阵；both=两者皆有；restricted=受控访问（如 EGA/dbGaP）。 |
| paper_ids | TEXT | 是 | **FK → papers.paper_id**（多值;） | — | 使用本数据集的所有文章，如 `P0001;P0007`。须与各 `papers.dataset_ids` 镜像一致。至少 1 个。 |

CSV 表头行：
```
dataset_id,repository,accession_url,platform,vendor,species,tissue,condition,n_cells,n_samples,data_availability,paper_ids
```

---

## 表 C · cell_types（细胞类型表 · 重点）

1 行 = 某数据集中的一种（亚）细胞类型。**`is_pns_cell` 是本库重点**：一个数据集若 0 条 `is_pns_cell=true`，则该数据集不算合格（见质检规则）。

| 字段名 | 类型 | 必填? | 主键/外键 | 枚举取值 | 说明 |
|---|---|:---:|---|---|---|
| ct_id | TEXT | 是 | **PK** | — | 内部主键。格式 `C` + 5 位零填充，如 `C00001`。全库唯一、永不复用。 |
| dataset_id | TEXT | 是 | **FK → datasets.dataset_id** | — | 所属数据集。必须已存在于 datasets 表。 |
| paper_id | TEXT | 是 | **FK → papers.paper_id** | — | 鉴定该细胞的文章。由 `ingest.py --paper-id` 回填，**不在提取 JSON 内**。 |
| cell_type | TEXT | 是 | — | 见文末「§细胞类型词表」 | 标准化细胞大类名，**首字母大写**，如 `Schwann cell`、`Fibroblast`、`Sensory neuron`。 |
| is_pns_cell | BOOLEAN | 是 | — | `true` / `false` | **是否外周神经系统细胞（神经元/胶质，重点标记）**。施万细胞/卫星胶质/肠胶质/感觉·自主神经元=true；成纤维/免疫/内皮/周细胞等微环境=false。判定不清填 `NA`（不要默认 false）。 |
| subtype | TEXT | 否 | — | — | 亚群名，如 `myelinating`、`peptidergic nociceptor`。**本库只重点填外周神经细胞(is_pns_cell=true)的亚群，非 PNS 细胞填 `NA`**；更细亚群另见表 E cell_subtypes。无细分填 `NA`。 |
| markers | TEXT | 否 | — | — | 该（亚）类的 marker 基因，**多值用 `;`**，遵守跨物种大小写规范（人全大写 `SOX10`；鼠/大鼠首字母大写 `Sox10`）。无则 `NA`。 |
| species | TEXT | 是 | — | `human` / `mouse` / `rat` | 该记录对应物种（**单值**；若同数据集多物种各测出同类细胞，拆成多行）。 |
| n_cells_or_pct | TEXT | 否 | — | — | 该类细胞数（整数，如 `1203`）或占比（带 `%`，如 `12.4%`）。二选一，原文给什么记什么。未知填 `NA`。 |
| annotation_method | TEXT | 否 | — | `manual-marker` / `SingleR` / `CellTypist` / `Azimuth` / `scANVI` / `reference-mapping` / `other` | 注释方式。多法并用取主用法或用 `;`。未知填 `NA`。 |
| provenance | TEXT | 是 | — | 见文末「§provenance」 | 证据来源，如 `Fig.2B`、`Table S3`、`Methods/Cell type annotation`。 |

CSV 表头行：
```
ct_id,dataset_id,paper_id,cell_type,is_pns_cell,subtype,markers,species,n_cells_or_pct,annotation_method,provenance
```

---

## 表 D · processing（下游处理表）

1 行 = 某数据集（在某文章中）的一套下游分析流程。通常每数据集 1 行；同一数据集被多文章各自再分析时可多行，用 `paper_id` 区分。

| 字段名 | 类型 | 必填? | 主键/外键 | 枚举取值 | 说明 |
|---|---|:---:|---|---|---|
| proc_id | TEXT | 是 | **PK** | — | 内部主键。格式 `X` + 5 位零填充，如 `X00001`。全库唯一、永不复用。 |
| dataset_id | TEXT | 是 | **FK → datasets.dataset_id** | — | 所属数据集。必须已存在。 |
| paper_id | TEXT | 是 | **FK → papers.paper_id** | — | 本流程出自哪篇文章（区分同数据集的不同再分析）。必须已存在。 |
| qc | TEXT | 否 | — | — | QC 标准，如 `min_genes=200;mito%<20;Scrublet`。多项用 `;`。未知填 `NA`。 |
| normalization | TEXT | 否 | — | `LogNormalize` / `SCTransform` / `scran` / `TPM` / `other` | 标准化方法。未知填 `NA`。 |
| batch_correction | TEXT | 否 | — | `Harmony` / `scVI` / `Seurat-CCA` / `Seurat-RPCA` / `fastMNN` / `BBKNN` / `none` | 批次校正。明确未做填 `none`；没提及填 `NA`。多法用 `;`。 |
| dim_reduction | TEXT | 否 | — | 如 `PCA;UMAP` / `PCA;tSNE` | 降维。多步用 `;` 按流程顺序。未知填 `NA`。 |
| clustering | TEXT | 否 | — | 如 `Leiden(res=1.0)` / `Louvain` | 聚类算法（带分辨率参数若有）。未知填 `NA`。 |
| annotation | TEXT | 否 | — | `marker-based` / `reference-mapping` / `mixed` | 注释策略（与 cell_types.annotation_method 呼应，此处记整体策略）。未知填 `NA`。 |
| diff_expr | TEXT | 否 | — | `Wilcoxon` / `MAST` / `pseudobulk-DESeq2` / `edgeR` / `t-test` / `none` / `other` | 差异表达方法。未做填 `none`；没提及填 `NA`。多法用 `;`。 |
| trajectory | TEXT | 否 | — | `Monocle2` / `Monocle3` / `Slingshot` / `PAGA` / `scVelo` / `none` | 轨迹/拟时。未做填 `none`；没提及填 `NA`。多法用 `;`。 |
| cell_comm | TEXT | 否 | — | `CellChat` / `CellPhoneDB` / `NicheNet` / `LIANA` / `none` | 细胞通讯。未做填 `none`；没提及填 `NA`。多法用 `;`。 |
| enrichment | TEXT | 否 | — | 富集分析「类型(工具)」如 `GO(Metascape)` / `GO/KEGG(clusterProfiler)` / `GSEA` / `none` | 富集/通路分析。未做填 `none`；没提及填 `NA`。多值用 `;`；**括号内并列用 `/`（禁嵌分号）**。工具标准名见 02 第 4 部分。 |
| software | TEXT | 否 | — | 如 `Seurat v5`；`Scanpy 1.9` | 主分析框架 + 版本，多个用 `;`。未知填 `NA`。 |
| provenance | TEXT | 是 | — | 见文末「§provenance」 | 证据来源，通常 `Methods/...` 或 `Supplementary Methods`。 |

CSV 表头行：
```
proc_id,dataset_id,paper_id,qc,normalization,batch_correction,dim_reduction,clustering,annotation,diff_expr,trajectory,cell_comm,enrichment,software,provenance
```

---

## 表 E · cell_subtypes（细胞亚群详表）

1 行 = 某数据集中某细胞大类的一个细分亚群（如施万细胞的 SC-Keloid / SC-Prolif / SC-EC…）。比 `cell_types.subtype` 记录更细，承载条件特异性、功能签名、分化谱系等亚群专属维度。无亚群细分的数据集可没有任何行。

| 字段名 | 类型 | 必填? | 主键/外键 | 枚举取值 | 说明 |
|---|---|:---:|---|---|---|
| subtype_id | TEXT | 是 | **PK** | — | 内部主键。格式 `S` + 5 位零填充，如 `S00001`。全库唯一、永不复用。 |
| dataset_id | TEXT | 是 | **FK → datasets.dataset_id** | — | 所属数据集。必须已存在。 |
| paper_id | TEXT | 是 | **FK → papers.paper_id** | — | 做该亚群 subclustering 的文章。由 `ingest.py --paper-id` 回填，**不在提取 JSON 内**。 |
| parent_cell_type | TEXT | 是 | — | 见「§细胞类型词表」 | 亚群所属细胞大类标准名（软关联 `cell_types.cell_type`），如 `Schwann cell`。 |
| subtype | TEXT | 是 | — | — | 亚群名（论文自报，如 `SC-Keloid`、`myelinating`）。 |
| is_pns_cell | BOOLEAN | 是 | — | `true` / `false` / `NA` | 是否外周神经系统细胞（继承大类判定）。 |
| species | TEXT | 是 | — | `human` / `mouse` / `rat` | 该记录物种（**单值**）。 |
| condition_specificity | TEXT | 否 | — | — | 亚群在哪些条件富集，如 `keloid-specific` / `shared(skin+keloid)` / `skin-specific`。无则 `NA`。 |
| markers | TEXT | 否 | — | — | 亚群定义 marker，**多值用 `;`**，遵跨物种大小写。无则 `NA`。 |
| functional_signature | TEXT | 否 | — | — | 功能/状态签名，如 `de-differentiated/pro-fibrotic`、`proliferating`、`Schwann-endothelial hybrid`。括号内并列用 `/`。无则 `NA`。 |
| n_cells_or_pct | TEXT | 否 | — | — | 亚群细胞数（整数）或占比（带 `%`）。未知填 `NA`。 |
| lineage | TEXT | 否 | — | — | 分化/谱系关系，如 `拟时起点(root)`、`SC-Skin->SC-Promyel->SC-Keloid 中间态`。括号内并列用 `/`。无则 `NA`。 |
| provenance | TEXT | 是 | — | 见文末「§provenance」 | 证据来源，如 `Fig.3A;Fig.3C`。 |

CSV 表头行：
```
subtype_id,dataset_id,paper_id,parent_cell_type,subtype,is_pns_cell,species,condition_specificity,markers,functional_signature,n_cells_or_pct,lineage,provenance
```

> 与 `cell_types` 关系：`cell_types` 记**大类**（含一个主 subtype），`cell_subtypes` 记**某大类的全部细分亚群**，靠 `parent_cell_type` 软关联（不强制 FK 到 ct_id，保持入库简单）。提取阶段亚群**可选**：论文做了亚群 subclustering 才填，否则该数据集无 cell_subtypes 行；亚群不参与合格性判定（仍看 cell_types 的 is_pns_cell）。

---

## SQLite CREATE TABLE DDL

> SQLite 由入库脚本（07）从 4 张 CSV 重建：每次 `DROP TABLE IF EXISTS` → `CREATE` → 批量 `INSERT`。
> 多值字段（dataset_ids/paper_ids/markers/species 等）在 SQLite 内仍以「分号分隔字符串」原样存储，不展开成连接表（保持与 CSV 真源 1:1）。
> SQLite 无原生 BOOLEAN，用 `TEXT` 存 `'true'`/`'false'`/`'NA'`，并加 `CHECK` 约束。所有缺失统一存字符串 `'NA'` 而非 SQL `NULL`，便于与 CSV 完全对齐。
> 开启外键：执行前先 `PRAGMA foreign_keys = ON;`。

```sql
PRAGMA foreign_keys = ON;

-- 表 A · papers --------------------------------------------------------------
DROP TABLE IF EXISTS papers;
CREATE TABLE papers (
    paper_id      TEXT PRIMARY KEY,                      -- P0001
    title         TEXT NOT NULL,
    first_author  TEXT NOT NULL,
    corresponding TEXT,
    year          TEXT,                                  -- 4位年或 'NA'
    journal       TEXT NOT NULL,
    doi           TEXT,
    pmid          TEXT,
    url           TEXT,
    species       TEXT NOT NULL,                         -- 'human' / 'mouse' / 'rat'，多值用 ';'
    has_scrna     TEXT NOT NULL CHECK (has_scrna IN ('true','false','NA')),
    dataset_ids   TEXT,                                  -- 'GSE...;GSE...' 或 'NA'
    status        TEXT NOT NULL CHECK (status IN ('pending','qualified','rejected','extracted')),
    source        TEXT NOT NULL CHECK (source IN ('PubMed','GEO','OpenAlex','SemanticScholar','EuropePMC','bioRxiv','other')),
    suppl_path    TEXT,
    notes         TEXT
);

-- 表 B · datasets ------------------------------------------------------------
DROP TABLE IF EXISTS datasets;
CREATE TABLE datasets (
    dataset_id        TEXT PRIMARY KEY,                  -- GSE 号优先
    repository        TEXT NOT NULL CHECK (repository IN ('GEO','SRA','ArrayExpress','Zenodo','EGA','other')),
    accession_url     TEXT,
    platform          TEXT NOT NULL,
    vendor            TEXT,
    species           TEXT NOT NULL,                     -- 多值用 ';'
    tissue            TEXT NOT NULL,                     -- 多值用 ';'
    condition         TEXT,
    n_cells           TEXT,                              -- 整数字符串或 'NA'
    n_samples         TEXT,                              -- 整数字符串或 'NA'
    data_availability TEXT NOT NULL CHECK (data_availability IN ('raw','processed','both','restricted')),
    paper_ids         TEXT NOT NULL                      -- 'P0001;P0007'
);

-- 表 C · cell_types ----------------------------------------------------------
DROP TABLE IF EXISTS cell_types;
CREATE TABLE cell_types (
    ct_id             TEXT PRIMARY KEY,                  -- C00001
    dataset_id        TEXT NOT NULL,
    paper_id          TEXT NOT NULL,
    cell_type         TEXT NOT NULL,
    is_pns_cell       TEXT NOT NULL CHECK (is_pns_cell IN ('true','false','NA')),
    subtype           TEXT,
    markers           TEXT,                              -- 'SOX10;MPZ' 或 'NA'
    species           TEXT NOT NULL CHECK (species IN ('human','mouse','rat')),
    n_cells_or_pct    TEXT,
    annotation_method TEXT,
    provenance        TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES datasets(dataset_id),
    FOREIGN KEY (paper_id)   REFERENCES papers(paper_id)
);

-- 表 E · cell_subtypes -------------------------------------------------------
DROP TABLE IF EXISTS cell_subtypes;
CREATE TABLE cell_subtypes (
    subtype_id            TEXT PRIMARY KEY,                 -- S00001
    dataset_id            TEXT NOT NULL,
    paper_id              TEXT NOT NULL,
    parent_cell_type      TEXT NOT NULL,
    subtype               TEXT NOT NULL,
    is_pns_cell           TEXT NOT NULL CHECK (is_pns_cell IN ('true','false','NA')),
    species               TEXT NOT NULL CHECK (species IN ('human','mouse','rat')),
    condition_specificity TEXT,
    markers               TEXT,
    functional_signature  TEXT,
    n_cells_or_pct        TEXT,
    lineage               TEXT,
    provenance            TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES datasets(dataset_id),
    FOREIGN KEY (paper_id)   REFERENCES papers(paper_id)
);

-- 表 D · processing ----------------------------------------------------------
DROP TABLE IF EXISTS processing;
CREATE TABLE processing (
    proc_id          TEXT PRIMARY KEY,                   -- X00001
    dataset_id       TEXT NOT NULL,
    paper_id         TEXT NOT NULL,
    qc               TEXT,
    normalization    TEXT,
    batch_correction TEXT,
    dim_reduction    TEXT,
    clustering       TEXT,
    annotation       TEXT,
    diff_expr        TEXT,
    trajectory       TEXT,
    cell_comm        TEXT,
    enrichment       TEXT,
    software         TEXT,
    provenance       TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES datasets(dataset_id),
    FOREIGN KEY (paper_id)   REFERENCES papers(paper_id)
);

-- 便于查询的索引（非强制，提速去重与连接） -----------------------------------
CREATE INDEX IF NOT EXISTS idx_ct_dataset   ON cell_types(dataset_id);
CREATE INDEX IF NOT EXISTS idx_cst_dataset  ON cell_subtypes(dataset_id);
CREATE INDEX IF NOT EXISTS idx_proc_dataset ON processing(dataset_id);
CREATE INDEX IF NOT EXISTS idx_proc_paper   ON processing(paper_id);
CREATE INDEX IF NOT EXISTS idx_ct_is_pns    ON cell_types(is_pns_cell);
```

> 建表顺序固定：`papers` → `datasets` → `cell_types` → `cell_subtypes` → `processing`（被引用表先建）。删除/重建时反序 DROP（processing → cell_subtypes → cell_types → datasets → papers）以满足外键。

---

## 5 张表 CSV 表头行（汇总，供脚本初始化空文件）

```
# db/papers.csv
paper_id,title,first_author,corresponding,year,journal,doi,pmid,url,species,has_scrna,dataset_ids,status,source,suppl_path,notes

# db/datasets.csv
dataset_id,repository,accession_url,platform,vendor,species,tissue,condition,n_cells,n_samples,data_availability,paper_ids

# db/cell_types.csv
ct_id,dataset_id,paper_id,cell_type,is_pns_cell,subtype,markers,species,n_cells_or_pct,annotation_method,provenance

# db/cell_subtypes.csv
subtype_id,dataset_id,paper_id,parent_cell_type,subtype,is_pns_cell,species,condition_specificity,markers,functional_signature,n_cells_or_pct,lineage,provenance

# db/processing.csv
proc_id,dataset_id,paper_id,qc,normalization,batch_correction,dim_reduction,clustering,annotation,diff_expr,trajectory,cell_comm,enrichment,software,provenance
```

---

## §字段填写规范（运行期 DeepSeek + 脚本必须照此执行）

### 1. ID 生成规则
| 表 | 前缀 | 宽度 | 示例 | 生成方式 |
|---|---|---|---|---|
| papers.paper_id | `P` | 4 位零填充 | `P0001` | 取现有最大序号 +1；空表从 `P0001` 起。 |
| cell_types.ct_id | `C` | 5 位零填充 | `C00001` | 同上，全库单调递增。 |
| cell_subtypes.subtype_id | `S` | 5 位零填充 | `S00001` | 同上，全库单调递增。 |
| processing.proc_id | `X` | 5 位零填充 | `X00001` | 同上。 |
| datasets.dataset_id | — | — | `GSE147101` | **不自造**：用真实登记号（GSE 优先），保持官方大小写。 |

规则：内部 ID 一旦分配**永不复用、永不回收**；删除记录留空号即可。生成由 Python 脚本完成（确定性任务，不用 LLM），DeepSeek 提取时该列可留占位 `__AUTO__`，由入库脚本统一赋号。

### 2. 多值字段分隔
- 分隔符固定英文分号 `;`，**两侧不留空格**：`GSE111;GSE222`、`MPZ;MBP;PMP22`。
- **分号禁止嵌入括号内部**（仅作字段级分隔符）：括号内并列多值改用斜杠 `/`，如 `time_series(0d/1d/3d/7d)`、`doublet_removal(neurons=Rbfox3/glia=Mbp)`。写成 `time_series(0d;1d;3d;7d)` 会被 `stats.py` 按 `;` 拆碎成 `time_series(0d`、`7d)` 等无效碎片污染分面统计。`validate.py` 的 `check_no_nested_delimiter` 守卫此约定（拆分后括号不闭合即报错）。
- 适用列：`species`(papers/datasets)、`dataset_ids`、`paper_ids`、`markers`、以及 platform/vendor/condition/tissue/各 processing 方法列在确有多值时。
- 单值就写单值，**不**加尾随分号；空则填 `NA`（不是空字符串、不是 `;`）。
- 多值内部不去重由脚本兜底；顺序不敏感（除 dim_reduction 按流程顺序）。

### 3. NA 约定
- 任何抓不到/不适用的字段一律填字符串 `NA`（大写两字母）。
- 禁止：空单元格、`null`、`None`、`-`、`—`、`N/A`、`unknown`、`无`、`0`（除非真实数值为 0）。
- **必填字段不允许 NA** 的例外：`species`、`has_scrna`、`status`、`source`（papers）；`repository`、`platform`、`species`、`tissue`、`data_availability`、`paper_ids`（datasets）；`cell_type`、`is_pns_cell`、`species`、`provenance`（cell_types）；`dataset_id`、`paper_id`、`provenance`（processing）。这些拿不准时**不要入库**，回流人工。其中 `has_scrna`/`is_pns_cell` 实在判不准可填 `NA`（已在 CHECK 中允许），但应触发人工复核。

### 4. bool 取值约定
- 只允许 `true` / `false`（全小写）。
- 未知/判不准 → `NA`（仅 `has_scrna`、`is_pns_cell` 允许）。**不得**用 `false` 代替「未知」。
- 录入来源：DeepSeek 输出必须是这三个字面值之一，入库脚本校验，非法值拒收。

### 5. provenance 写法（溯源，必填）
目的：每条 cell_types / processing 记录都能被人追回原文证据。格式约定：
- 图：`Fig.<编号>`，如 `Fig.2B`、`Fig.S4`（补充图加 S）。
- 表：`Table <编号>`，如 `Table 1`、`Table S3`（补充表加 S）。
- 正文/方法：`<Section>/<小标题或要点>`，如 `Methods/Cell type annotation`、`Results/Schwann cell heterogeneity`、`Supplementary Methods`。
- 数据库元数据：`GEO:<GSE号>`，如 `GEO:GSE147101`（n_cells/platform 等来自 GEO 页面时）。
- 多来源用 `;` 串联：`Fig.2B;Table S3`。
- 严禁写 `paper`、`原文`、`见上` 这类无法定位的占位。

### 6. 命名与大小写规范（marker 与 ID）
- **marker 基因**：人类全大写（`SOX10`、`CALCA`）；小鼠/大鼠首字母大写其余小写（`Sox10`、`Calca`）。以 `cell_types.species` 决定大小写，跨物种同一基因须按各自规范分行书写。
- **dataset_id / GSE**：全大写无空格（`GSE147101`）。
- **doi**：全小写裸号（不带 `https://doi.org/`）。
- **pmid**：纯数字字符串。
- 物种枚举一律小写：`human` / `mouse` / `rat`（不写 `Human`/`Homo sapiens`/`mice`）。

### 7. 数值字段
- `year`：4 位整数（或 `NA`）。`n_cells`/`n_samples`：非负整数，**不带千分位逗号**（`12000` 不是 `12,000`），近似/区间值取主报告整数。
- CSV 中数值仍按文本写入，由 SQLite/脚本按需转换；含逗号的数字必须去逗号，避免破坏 CSV 分列。

### 8. 去重与一致性（入库脚本强制，非 LLM）
- 主键唯一：四表各自 PK 不得重复。
- 外键存在性：cell_types/processing 的 dataset_id、processing 的 paper_id 必须在父表存在。
- 镜像一致：对每个 `dataset_id`，其 `paper_ids` 集合 == 所有在 `dataset_ids` 中含该 dataset 的 papers 的 paper_id 集合（双向校验，不一致即报错）。
- 数据集去重键 = `dataset_id`：新文章命中已存在数据集时，仅 `datasets.paper_ids` 追加 + 该 paper 的 `dataset_ids` 追加，**不**新增 datasets/cell_types/processing 行（除非确为对同一数据的独立再分析，此时仅 processing 可新增一行并标新 paper_id）。
- 合格性校验：一个数据集要进入合格库，须满足 `papers.has_scrna=true` 关联、`species ∈ {human,mouse,rat}`、且其 cell_types 中**至少 1 条 `is_pns_cell=true`**。否则标记待人工复核，不计入 index 统计。

---

## §受控词表（取值参考摘要，完整版见 02 受控词表文件）

> 以下为本 schema 字段的合法取值锚点；运行期遇到词表外取值，先归一到最接近的标准名，归一不了则记原文并在 notes 标注，交人工扩词表。

### §平台词表（datasets.platform）
`10x Chromium 3' v2` · `10x Chromium 3' v3` · `10x Chromium 5'` · `10x Multiome` · `Smart-seq2` · `Smart-seq3` · `Drop-seq` · `inDrop` · `BD Rhapsody` · `Parse split-seq` · `Microwell-seq` · `Fluidigm C1` · `BGI/MGI DNBelab C4` · `snRNA-seq`（单核，可与上叠加，如 `10x Chromium 3' v3;snRNA-seq`）

### §组织词表（datasets.tissue）
外周（合法）：`DRG` · `TG`（三叉神经节）· `nodose ganglion` · `vagal ganglion` · `sympathetic ganglion`（含 `SCG`）· `sciatic nerve` · `peripheral nerve trunk` · `ENS-myenteric`（肌间丛）· `ENS-submucosal`（黏膜下丛）· `skin innervation` · `visceral nerve`
中枢（排除，**不应入库**，仅供识别）：`spinal cord` · `brainstem` · `cortex` · `brain` · `retina`
混合篇规则：DRG 常与 spinal cord 同篇 → **只取 DRG**，spinal cord 部分不入库，并在 papers.notes 标注。

### §细胞类型词表（cell_types.cell_type）+ is_pns_cell 默认
| cell_type 标准名 | 默认 is_pns_cell | 典型 marker（人；鼠首字母大写） |
|---|:---:|---|
| sensory neuron | true | RBFOX3;ISL1;POU4F1 |
| sympathetic neuron | true | TH;DBH;CHGA |
| enteric neuron | true | PHOX2B;RET;ELAVL4 |
| Schwann cell | true | MPZ;MBP;PMP22;SOX10;PLP1 |
| satellite glia | true | FABP7;KCNJ10;GLUL |
| enteric glia | true | SOX10;S100B;GFAP |
| fibroblast | false | PDGFRA;COL1A1;DCN |
| macrophage/immune | false | PTPRC;CX3CR1;LYZ |
| endothelial | false | PECAM1;CLDN5 |
| pericyte/SMC | false | PDGFRB;RGS5;ACTA2 |

> subtype 示例（写入 subtype 列，不写入 cell_type）：`peptidergic nociceptor`(CALCA;TAC1;TRPV1) · `non-peptidergic`(P2RX3;MRGPRD;GFRA2) · `proprioceptor`(PVALB;RUNX3;NTRK3) · `C-LTMR`(TH) · `myelinating`/`non-myelinating/repair` Schwann。

### §condition 约定（datasets.condition）
自由文本但建议归一为 `<大类>(<模型缩写>)`：`healthy`/`naive` · `nerve injury(SNI)`/`(SNL)`/`(CCI)`/`(axotomy)` · `inflammation(CFA)` · `diabetic` · `chemotherapy(paclitaxel)` · `tumor` · `development(E14.5)` · `aging`。多条件 `;` 分隔。

---

## §运行期目录落位（与本 schema 配套）
```
D:/database/
├─ design/01_schema.md            ← 本文件（资产包，运行期只读参考）
├─ db/
│  ├─ papers.csv  datasets.csv  cell_types.csv  processing.csv   ← 唯一可手改真源
│  └─ database.sqlite             ← 由脚本从 4 张 CSV 重建
├─ cards/<dataset_id>.md          ← 每数据集一张可读卡片
├─ raw/<paper_id>/                ← 原始资料归档（对应 papers.suppl_path）
├─ logs/                          ← 过程日志
└─ index.md                       ← 总览统计
```
