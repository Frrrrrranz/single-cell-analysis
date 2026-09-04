# DOI_10.1038_s41591-024-03215-z 复核判定报告

论文：A multi-modal single-cell and spatial expression map of metastatic breast cancer biopsies across clinicopathological features (Nature Medicine 2024, HTAN MBC 图谱)
原文：`D:\OneDrive\Desktop\组\marker提取\review_md\DOI_10.1038_s41591-024-03215-z.md`
复核日期：2026-09-02

**通用警示（影响本篇多处判定）**：本 PDF 的 review_md 为双栏排版逐行交错抽取，左右栏文字互相拼接。候选材料中的多条"证据句"是双栏伪影，必须按左右栏重组后才能判定。本报告所有"原句"凡标注（双栏重排）者均为按栏重组后的完整句，字词与原文一致。

## 摘要

| 动作 | 数量 | 明细 |
|---|---|---|
| 补录（新行） | 0 | 无（A 门 25 条候选全部不录；无满足双重门槛的漏提基因） |
| 升级（→ author_declared） | 8 | M01304 CD19、M01305 FCRL5、M01308 CD8A、M01309 EPCAM、M01311 CD163、M01313 CD14、M01316 NCAM1、M01317 CD4 |
| 恢复（exclusions 降级行） | 0 | B2 门 9 条全部维持排除 |
| 移除 | 2 | M01306（C 门重复+归属偏移）、M01314（D 门新发现的 CD163 重复行） |
| 维持（不升级） | 1 | M01307 FOXP3（注释用途成立但无 marker 措辞，维持 annotation_marker） |
| 归属修正 | 1 | M01306 FCRL5："B regulatory cells" → "B cells"（过度具体化，由 M01305 承载） |
| 维持不录 | 34 条候选 | A 门 25 条 + B2 门 9 条（其中 7 条与 A 门重审候选重叠，已统一判定不重复计数） |

判定要点：
1. **A 门核心句是双栏拼接伪影**：COL4A1/COL3A1/BGN/ACTA2/FN1/COL4A2/TAGLN/DCN/COL1A1/LUM 十个基因**不是**成纤维细胞注释 marker 面板，而是 Methods 中 "scRNA-seq-derived iNMF EMT program genes"（EMT 程序评分基因集），全部不录。
2. **Methods 基因面板设计句构成 author_declared**："Canonical cell-type-specific markers (for example, EPCAM for epithelial cells, ...)" + 面板"covering all major cell types" + MERFISH de novo "marker gene-based annotation" + Fig. 5b marker 分区，注释用途链完整，6 行升级；加上 FCRL5（"the typical B cell marker"）与 CD163（"a key macrophage marker"）共 8 行升级。
3. **旧"范围外"排除经重审全部维持排除**，但理由更新为双重门槛不满足（详见 A 门 19-25 与 B2 门）。

---

## A 门逐条判定

### A1-A6、A14-A17：十个胶原蛋白/基质基因（同一证据句，统一判定）

背景核实：候选证据句 "type label were investigated in detail using marker genes and assigned COL4A1, COL3A1, BGN, ..." 在原文中由左右两栏拼接而成。重组后：

- 左栏句（Methods, De novo cell type annotation）：**"Clearly distinct clusters that were annotated with the same cell type label were investigated in detail using marker genes and assigned more specific cell type labels. For a simplified annotation, all cells then received a second label based on their cell type label to be assigned to one of the four compartments: malignant, stromal, myeloid and lymphoid."** ——该句**不点名任何基因**。
- 右栏句（Methods, Scoring of expression programs in sc/snRNA-seq and spatial data）：**"Seurat was used to score the subcell-type marker genes17 as well as the hallmark gene sets in the Molecular Signatures Database (MSigDB)65,66, and SCANPY version 1.7.2 was used to score the scRNA-seq-derived iNMF EMT program genes (IGFBP7, SPARC, COL1A2, COL4A1, COL3A1, BGN, ACTA2, FN1, COL4A2, TAGLN, DCN, COL1A1, LUM, COL6A3, POSTN, AEBP1, COL6A2, VIM, TIMP1, TPM2, COL5A1, CALD1, COL6A1, A2M, SPARCL1, THY1, VCAN, CCN2, GNG11, PDGFRB, RGS5, ITGA1, MYL9, COL5A2, COL18A1, THBS2, IGHA1, CAVIN1, ELN, NID1, LHFPL6, APOE, IGLC3, HSPG2, CAV1, TCF4, NNMT, ASPN, FSTL1 and MGP), of which 20 genes are represented in MERFISH and ExSeq (TCF4, COL4A1, BGN, COL1A2, FN1, COL1A1, ACTA2, MYL9, HSPG2, TIMP1, VIM, THY1, APOE, COL3A1, DCN, LUM, TAGLN, TPM2, GNG11 and COL4A2) and three in CODEX (VIM, THY1 and COL4A2)."**（双栏重排）

即：候选基因全部属于 **iNMF EMT 程序基因列表**，用途是用 AddModuleScore/score_genes 计算 EMT 程序得分（进而定义 EMT-high/EMT-low/EMT-patched 空间表型），不是任何细胞类型（包括成纤维细胞）的注释 marker，原文无任何 marker 措辞指向这些基因。按边界规则（基因集程序评分，同类于 GSEA hallmark 不收录）。

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | COL3A1 | 不录 | — | — | — | — | Methods, Scoring of expression programs | 见上文右栏句（双栏重排） | 双栏拼接伪影；属 iNMF EMT 程序基因，用于程序评分，非注释 marker（无 marker 措辞+无注释用途） |
| 2 | ACTA2 | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 3 | FN1 | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 4 | TAGLN | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 5 | DCN | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 6 | COL1A1 | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 14 | COL4A1 | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 15 | BGN | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 16 | COL4A2 | 不录 | — | — | — | — | 同上 | 同上 | 同上 |
| 17 | LUM | 不录 | — | — | — | — | 同上 | 同上 | 同上 |

### A7-A12、A18：噪声 token

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 7 | EMT | 不录-噪声token | — | — | — | — | Results, EMT 表型分析；Methods 面板设计 | "Although cells from samples with low and high EMT scores showed little variation of EMT scores across space, intermediate scoring samples showed patches of high-scoring cells (Fig. 5e, segmented MERFISH data)..."；面板设计分类 "Hallmarks of cancer: evasion of apoptosis, for example, BCL2; EMT, for example, VIM; immune evasion, for example, CD274; senescence, for example, TP53; proliferation, for example, MKI67" | EMT 是上皮-间充质转化程序名（hallmark 分类名），非基因符号 |
| 8 | MERFISH | 不录-噪声token | — | — | — | — | Fig. 5b 图注 | "b, Dot plot depicting the scaled expression (by gene, across clusters) and fraction of expressing cells of macrophage marker and function genes as well as marker genes for other cell types and differentially expressed genes between clusters as in a for cell-segmented MERFISH data." | 实验方法名，非基因 |
| 9 | GSEA | 不录-噪声token | — | — | — | — | Results | "clustering malignant profiles by mean gene set enrichment analysis (GSEA) hallmark signature scores in malignant cells yielded clear grouping in snRNA-seq..." | 分析方法名，非基因 |
| 10 | CD68Hi | 不录-噪声token | — | — | — | — | Results, 巨噬细胞引言段 | "For example, although CD68+ leukocyte density alone was not found to be a prognostic biomarker in primary treatment-naive BC, a CD68Hi, CD4Hi, CD8Lo immunophenotype was associated with reduced overall survival and recurrence-free survival50" | 流式/免疫表型描述符（Hi/Lo 后缀），非基因符号；且为既往研究引述 |
| 11 | CD4Hi | 不录-噪声token | — | — | — | — | 同上 | 同上 | 同上 |
| 12 | CD8Lo | 不录-噪声token | — | — | — | — | 同上 | 同上 | 同上 |
| 18 | M0293L | 不录-噪声token（试剂货号） | — | — | — | — | Methods, ExSeq/CODEX 试剂步骤 | "Subsequent exonuclease treatment was performed by resuspension of the bead pellet in 200 μl of Exonuclease I reaction mixture (1× ExoI buffer with 10 U μl−1 Exonuclease I (NEB, M0293L)) and incubated at 37 °C for 50 min, followed by one wash..." | NEB Exonuclease I 货号，试剂而非基因 |

### A13：AGR2

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 13 | AGR2 | 不录 | — | — | — | — | Results, EMT 表型（Fig. 5f 段） | "EMT-patched and EMT-high phenotypes were each characterized by distinct cell cycle genes (EMT-patched: CCND1, RB1 and NF1; EMT-high: CDC20); EMT-low samples were further characterized by AGR2, a potential biomarker of poor prognosis53,54."（双栏重排） | AGR2 被称为"预后 biomarker"而非细胞群 marker；句中用途是对 EMT 空间表型的差异表达特征描述（注释完成后），无注释用途 |

### A19-A25："此前已排除（范围外）"重审候选（旧范围性排除理由已失效，按双重门槛重判）

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 19 | HIF1A | 不录（维持排除，理由更新） | — | — | — | — | Results, Fig. 5a/ED Fig. 9c,d 段 | "Across all methods, there were two major clusters of highly correlated method-specific clusters: a CD163+ cluster with high expression of macrophage markers as well as HIF1A and APOE/APOC1 and a CD163− cluster associated with lower macrophage marker expression and expression of MKI67 (Extended Data Fig. 9c,d)."（双栏重排）；Discussion 段："Across methods, we identified two macrophage states characterized by CD163/CD68/APOE/HIF1A and MKI67, respectively."（双栏重排） | 双门槛均不成立：①无 marker 措辞——原文明确把 HIF1A 与 "macrophage markers" 区分并列（"macrophage markers **as well as** HIF1A and APOE/APOC1"），"characterized by" 非措辞；②巨噬细胞簇/状态以 CD163+/CD163− 命名（CD163 已收录），HIF1A 仅为状态描述特征 |
| 20 | APOE | 不录（维持排除，理由更新） | — | — | — | — | 同上 + "Previous studies of primary BC described APOE-expressing macrophages as lipid-associated macrophages (LAMs), comprising up to 30–40% of all myeloid cells17. In our MERFISH data, the fraction of APOE-expressing macrophages varied from 24% to 85% of all macrophages (mean, 48%)." | ①LAM 身份归于既往研究（ref 17）而非本文作者 marker 声明；本文仅以 "APOE-expressing macrophages" 做亚群定量，未创建 APOE+ 注释标签；②APOE 在面板中唯一出现是 EMT 程序基因列表成员（见 A1-A17）；③与 "macrophage markers" 并列区分。双门槛均不成立 |
| 21 | KRT8 | 不录（维持排除，理由更新） | — | — | — | — | Results, Fig. 2g 段 | "Inter-patient variability in established epithelial BC marker genes (EPCAM, KRT8, KRT18, KRT19 and TRPS1) was minimally impacted by receptor status but notably by profiling method (Fig. 2g)."；Fig. 2g 图注："Dot plots depicting the expression level (mean expression) and frequency (fraction of expressing cells) of malignant marker genes as well as disease-relevant BC biomarkers across malignant cells, grouped by =profiling method and receptor status." | **只满足门槛一**：marker 身份成立（"established epithelial BC marker genes"），但注释用途不成立——Fig. 2g 是注释完成后跨方法/受体状态的变异性比较（方法学评估），未参与 MBC 识别/命名（恶性鉴定走 inferCNV + SingleR + ED Fig. 3 top-5 markers）。另见 KRT8/KRT18 在 Fig. 6e 语境为 "luminal epithelial genes"（差异表达描述） |
| 22 | KRT18 | 不录（维持排除，理由更新） | — | — | — | — | 同上 | 同上 | 同上 |
| 23 | KRT19 | 不录（维持排除，理由更新） | — | — | — | — | 同上 | 同上 | 同上 |
| 24 | APOC1 | 不录（维持排除，理由更新） | — | — | — | — | Results, Fig. 5a/ED Fig. 9c,d 段 | 同 #19 第一句 | 同 #19：与 "macrophage markers" 并列区分，无 marker 措辞，无注释用途 |
| 25 | MKI67 | 不录（维持排除，理由更新） | — | — | — | — | 同 #19 + Methods 面板设计分类 | "Hallmarks of cancer: evasion of apoptosis, for example, BCL2; EMT, for example, VIM; immune evasion, for example, CD274; senescence, for example, TP53; proliferation, for example, MKI67, etc."；"...a CD163− cluster associated with lower macrophage marker expression and expression of MKI67 (Extended Data Fig. 9c,d)" | ①面板设计中 MKI67 被列为**增殖 hallmark** 例基因而非 cell-type marker；②CD163− 簇命名依据是 CD163（阴性），MKI67 是该簇的伴随表达特征；无 marker 措辞、无注释用途 |

---

## B 门逐条判定

核心句（Methods, Gene panel design for MERFISH and ExSeq；双栏重排，逐条引用）：
**"The prior knowledge-driven gene selection (1) started by identifying categories of genes known to be important in MBC and in cancer in general and reviewing available literature to select representative genes of each category: • Canonical cell-type-specific markers (for example, EPCAM for epithelial cells, CD19 for B cells, CD4 for T helper cells, CD8 for cytotoxic T lymphocytes, CD56 for NK cells and CD14 for macrophages) • Clinical breast cancer biomarkers (for example, ESR1, PGR and ERBB2) ..."**

注释用途链（ Methods）：①"The total number of genes assessed was, thus, 297, representing all nine categories and 82 of the 83 original gene types (Supplementary Table 3). This high retention rate of represented gene types confirmed that we were still covering all major cell types, subtypes and programs of interest with the reduced gene set..."；②"we performed manual cluster-wise and marker gene-based annotation as is frequently done in scRNA-seq data"（MERFISH de novo 注释）；③Fig. 5b 以 "Macrophage marker genes / Macrophage function genes / Other cell type markers / Differentially expressed genes" 分区展示该面板基因。→ 满足"方法说依据 marker 注释 + 对应 marker 图表"的收录规则，且措辞为作者明确的 "Canonical cell-type-specific markers"，够 author_declared。

| marker_id | gene | cell_type | 判定 | 完整原句 | 理由 |
|---|---|---|---|---|---|
| M01304 | CD19 | B cells | **升级 author_declared** | "Canonical cell-type-specific markers (for example, EPCAM for epithelial cells, **CD19 for B cells**, CD4 for T helper cells, CD8 for cytotoxic T lymphocytes, CD56 for NK cells and CD14 for macrophages)"（Methods, Gene panel design；双栏重排） | 作者明确的 canonical marker 措辞点名 CD19→B cells；面板用于细胞类型识别（de novo marker-gene 注释 + Fig. 5b 'other cell type markers' 分区）。source_locator 建议改为 "Methods, Gene panel design for MERFISH and ExSeq, Canonical cell-type-specific markers; Fig. 5b" |
| M01305 | FCRL5 | B cells | **升级 author_declared** | "For consistency, we used a similar level of resolution for the annotated cell types as was used in the sc/snRNA-seq annotation and assigned new cell type labels only when clusters clearly displayed features that did not match to any previously annotated cell types, which was the case for a small population of potentially regulatory B cells expressing FOXP3 in addition to **the typical B cell marker FCRL5**."（Methods, De novo cell type annotation of the cell-segmented MERFISH data；双栏重排） | "the typical B cell marker FCRL5" 为作者明确 marker 措辞，且语境即 MERFISH de novo 注释流程本身（注释用途直接成立） |
| M01306 | FCRL5 | B regulatory cells | **不升级；移除（C 门重复+归属偏移）** | 同 M01305 句；另见 Results："Although most were in agreement, MERFISH-based assignments lacked some granularity (only one endothelial cell label, joint T/NK labels) but captured other distinctions missing in sc/snRNA-seq, including a small cluster of B regulatory cells jointly expressing FOXP3 and FCRL5 (Extended Data Fig. 8e)."（双栏重排） | 句中 marker 措辞（"typical B cell marker"）指向 **B cells 全体**而非 B regulatory cells 亚群；B regulatory cells 的定义性特征是 FOXP3（M01307 已承载）。与 M01305 同一证据句的语义重复 → 按 C 门判定移除（见 C 门） |
| M01307 | FOXP3 | B regulatory cells | **维持 annotation_marker** | 同 M01305 句 | FOXP3 无 marker 措辞（仅 "expressing FOXP3"）；注释用途成立（新标签 "B regulatory cells" 赋值依据），但不构成 author_declared。维持现状 |
| M01308 | CD8A | cytotoxic T lymphocytes | **升级 author_declared**（附写法注记） | "...CD4 for T helper cells, **CD8 for cytotoxic T lymphocytes**, CD56 for NK cells..."（Methods, Gene panel design；双栏重排） | 同 M01304。注记：原文写 "**CD8**"（未区分 CD8A/CD8B），行内 gene_symbol=CD8A 属蛋白/家族→基因映射，应在行内注明原文写法（见 D 门第 4 项） |
| M01309 | EPCAM | epithelial cells | **升级 author_declared** | "Canonical cell-type-specific markers (for example, **EPCAM for epithelial cells**, CD19 for B cells, ...)"（Methods, Gene panel design；双栏重排） | 同 M01304。EPCAM 的另一出处（Fig. 2g "established epithelial BC marker genes"）注释用途不成立，不据此另立 MBC 行（见 B2 门候选 1） |
| M01311 | CD163 | Macrophage | **升级 author_declared**（附重复行处理建议） | "Macrophage co-localization phenotypes (Fig. 4c,e) were neither specifically enriched nor depleted with expression of **CD163, a key macrophage marker**, with the three representative samples showing predominantly CD163+ macrophages (Fig. 4f)."（Results, Fig. 4 段） | "CD163, a key macrophage marker" 为作者明确 marker 措辞；Fig. 4f/5a 以 CD163 表达展示并命名 CD163+/CD163− 巨噬细胞簇，注释/命名用途成立。另：升级后与 M01314（macrophages/CD163/author_declared，同一句）构成重复，建议移除 M01314、保留本行（见 D 门） |
| M01313 | CD14 | macrophages | **升级 author_declared** | "...CD56 for NK cells and **CD14 for macrophages**)"（Methods, Gene panel design；双栏重排） | 同 M01304；Fig. 5b 巨噬细胞 marker 分区展示 |
| M01316 | NCAM1 | NK cells | **升级 author_declared**（附写法注记） | "...CD8 for cytotoxic T lymphocytes, **CD56 for NK cells** and CD14 for macrophages)"（Methods, Gene panel design；双栏重排） | 同 M01304。注记：原文写 "**CD56**"（蛋白名），NCAM1 未在原文文本出现；行内 gene_symbol=NCAM1 属蛋白→基因映射，应注明原文写法（见 D 门第 4 项） |
| M01317 | CD4 | T helper cells | **升级 author_declared** | "...CD19 for B cells, **CD4 for T helper cells**, CD8 for cytotoxic T lymphocytes..."（Methods, Gene panel design；双栏重排） | 同 M01304 |

---

## B2 逐条判定

| 来源 | gene | cell_type | 判定 | 完整原句 | 理由 |
|---|---|---|---|---|---|
| B②恢复 | EPCAM | MBC (malignant) | **维持排除** | "Inter-patient variability in established epithelial BC marker genes (EPCAM, KRT8, KRT18, KRT19 and TRPS1) was minimally impacted by receptor status but notably by profiling method (Fig. 2g)." | marker 身份成立，但 Fig. 2g 用途为注释完成后的方法学变异性比较，不满足注释用途门槛；EPCAM 已由 M01309（epithelial cells，Methods 面板句）合规收录，勿重复 |
| B②恢复 | KRT8 | MBC (malignant) | **维持排除** | 同上 | 同上：门槛二不成立（旧"PNS 范围外"理由失效，新理由为注释用途不成立） |
| B②恢复 | KRT18 | MBC (malignant) | **维持排除** | 同上 | 同上 |
| B②恢复 | KRT19 | MBC (malignant) | **维持排除** | 同上 | 同上 |
| B②恢复 | TRPS1 | MBC (malignant) | **维持排除** | 同上；另见 "On a technical level, profiling method contributed to observed expression variability, including in key genes such as ESR1 and TRPS1, a finding with implications for marker gene-based approaches." | 同上；TRPS1 另一处仅作为技术变异性的"key genes"举例，无注释用途 |
| B②恢复 | APOE | macrophages (CD163+/CD68+/APOE+/HIF1A+ state) | **维持排除** | "Across methods, we identified two macrophage states characterized by CD163/CD68/APOE/HIF1A and MKI67, respectively."（双栏重排）；"Previous studies of primary BC described APOE-expressing macrophages as lipid-associated macrophages (LAMs)..." | 见 A 门 #20：无 marker 措辞（与 "macrophage markers" 并列区分；LAM 归于 ref 17），状态以 CD163+/CD163− 命名，APOE 用于描述与定量。双门槛均不成立 |
| B②恢复 | HIF1A | macrophages (同上 state) | **维持排除** | 同上 | 见 A 门 #19。双门槛均不成立 |
| B②恢复 | APOC1 | macrophages (同上 state) | **维持排除** | "a CD163+ cluster with high expression of macrophage markers as well as HIF1A and APOE/APOC1 and a CD163− cluster associated with lower macrophage marker expression and expression of MKI67 (Extended Data Fig. 9c,d)"（双栏重排） | 见 A 门 #24。双门槛均不成立 |
| B②恢复 | MKI67 | macrophages (CD163−/MKI67+ state) | **维持排除** | 同上 + "proliferation, for example, MKI67"（Methods 面板设计 hallmark 分类） | 见 A 门 #25。双门槛均不成立（面板中列为增殖 hallmark，非 cell-type marker） |

（B2 与 A 门重审候选 APOE/HIF1A/APOC1/MKI67/KRT8/KRT18/KRT19 为同一语境，判定统一，不重复计数。）

---

## C 门逐条判定

| 组 | 行1 | 行2 | 判定 | 保留 | 移除 | 理由 |
|---|---|---|---|---|---|---|
| fcrl5 | M01305：B cells / subtype=potentially regulatory B cells / annotation_marker | M01306：B regulatory cells / annotation_marker | **判定重复（同一基因、同一核心证据句、同一生物学事件）** | **M01305**（升级 author_declared） | **M01306** | 两行均出自 Methods de novo 注释同一句；M01305 的 subtype 字段（potentially regulatory B cells）与 M01306 的 cell_type（B regulatory cells）指向同一小群，规范化后互为包含 → 同一证据重复。保留依据：①升级后证据级更高（author_declared "the typical B cell marker FCRL5" > annotation_marker）；②归属准确——FCRL5 的 marker 声明指向 **B cells 全体**（"typical B cell marker"），把它挂到 B regulatory cells 属过度具体化（归属修正）；③B regulatory cells 簇的定义性 marker 是 FOXP3，已由 M01307 承载，移除 M01306 不丢失该簇证据。M01306 的补充出处（Results "jointly expressing FOXP3 and FCRL5"）为共表达描述而非 marker 声明，可并入 M01307 的 locator |

---

## D 门检查结论

### 1. 聚类对账
- 论文注释细胞类型数：**26**（Fig. 2e 图注："the 26 annotated cell types (e). n = 26 cell types"）。由 UMAP 图文（Fig. 2a 区域）重建 26 类：MBC、MBC_stem-like、MBC_neuronal、MBC_chondroid、Endothelial、Endothelial_sinusoidal、Endothelial_angiogenic、Endothelial_vascular、Fibroblast、Chondrocyte、Smooth muscle_vascular、Skeletal muscle、Stellate、Hepatocyte、Adipocyte、Neuron、Keratinocyte、Macrophage、Monocyte、Neutrophil、Erythrocyte、Mast、B_plasma、B、T、NK；另有 MERFISH de novo 新增标签 **B regulatory cells**（第 27 个标签）。
- 总表 15 行覆盖细胞类型（去重 9 个）：adipocytes、B cells、B regulatory cells、cytotoxic T lymphocytes、epithelial cells（方法句泛称，非论文簇标签）、hepatocytes、Macrophage/macrophages（同一类）、NK cells、T helper cells。
- **整簇漏提 21 个**（详见"整簇漏提明细"）。但需如实说明：这些簇的 marker 基因名在 review_md 文本中**不可恢复**——论文每类细胞的 top-5 marker 基因只在 ED Fig. 3a,b 小提琴图（图片内容，文本抽取不到基因名）与 Supplementary Table 3 / ref 17（subcell-type marker genes）中；正文文本可指名的唯一整簇 marker 面板是 MBC 的 "established epithelial BC marker genes"，但其用途判定不满足注释门槛（见 B2 门）。**结论：整簇漏提确认存在，但本次文本复核无可补录证据；如需填补须另行核对 ED Fig. 3a,b 图版与 Supplementary Table 3（超出 review_md 文本范围）。**
- 细胞类型只在 snRNA-seq 检出：adipocytes、neurons、部分 endothelial 亚群、stellate cells、smooth/skeletal muscle；只在 scRNA-seq 检出：neutrophils、mast cells、erythrocytes、keratinocytes（正文明确列出，可作对账旁证）。

### 2. marker 归属核对
- **M01306（FCRL5→B regulatory cells）**：过度具体化——marker 声明指向 B cells 全体；已按 C 门移除（归属修正，由 M01305 承载 B cells 归属）。
- **M01311 与 M01314（CD163，"Macrophage" vs "macrophages"）**：新发现的语义重复对（机械扫描未标记）。两行同基因、同细胞类型（仅大小写/单复数差异）、证据重叠（同出 "CD163, a key macrophage marker" 句，Fig. 4f）。建议：保留 M01311（升级 author_declared，locator 含 Fig. 4f; Fig. 5a,b; Methods，覆盖最全，cell_type "Macrophage" 与论文簇标签一致），**移除 M01314**。
- **M01315（CD68→macrophages，subtype="CD163+/CD68+/APOE+/HIF1A+ state"）**：subtype 字段把 APOE/HIF1A 嵌入状态名，但二者并非作者声明的 marker（见 A/B2 门判定），建议将该行 subtype 简化为 "CD163+ state"（或留空）；另该行 evidence_type=annotation_marker 的文本依据实际是 "characterized by" 句 + Fig. 5b 面板分区展示，若严格按层级更接近 figure_labeled——建议复核时一并修正（非本次 B 门对象，仅记录建议）。
- M01309（EPCAM→epithelial cells）与 Methods 原句归属一致，无问题。

### 3. 物种一致性
论文为人转移性乳腺癌活检（HTAPP 队列，人源）。总表 15 行 species=human，全部一致。✓（升级的 8 行亦为人源，基因符号全大写与原文一致。）

### 4. 基因写法核对
- 人源全大写规范整体一致。✓
- **两处蛋白/家族名→基因符号映射偏离原文拼写**（应在行内注记原文写法，避免"静默修正"）：①M01308 gene_symbol=CD8A，原文写 "**CD8**"（未区分 CD8A/CD8B，存在歧义，建议注明）；②M01316 gene_symbol=NCAM1，原文写 "**CD56**"（蛋白名；NCAM1 在原文文本中未出现）。
- CD68Hi/CD4Hi/CD8Lo 等 Hi/Lo 流式描述符未入表（正确）。M0293L 为试剂货号（正确排除）。

### 5. 跨篇一致性（four_layer_category）
总表 15 行均为 four_layer_category=outside、is_pns_cell=false，与论文（乳腺癌、非 PNS）一致。本次升级的 8 行与保留行均维持 outside；无跨篇命名冲突（CD19/CD4/CD8A/CD14/NCAM1/EPCAM/CD163/FCRL5 与其他收录篇目的同名 marker 用法一致）。✓

---

## 归属修正明细

| marker_id | 错误归属 | 正确归属 | 证据 |
|---|---|---|---|
| M01306 | FCRL5 → B regulatory cells（过度具体化） | FCRL5 → B cells（由 M01305 承载） | "a small population of potentially regulatory B cells expressing FOXP3 in addition to **the typical B cell marker FCRL5**"（Methods, De novo cell type annotation）——marker 声明针对 B cells 全体；B regulatory cells 的定义特征是 FOXP3（M01307） |
| （建议）M01314 | CD163 → macrophages（与 M01311 重复，非归属错误） | 并入 M01311（Macrophage） | 同一句 "CD163, a key macrophage marker"（Results, Fig. 4f 段）；M01311 locator 更全 |

## 整簇漏提明细

| cell_type | markers | 证据 locator + 原句 |
|---|---|---|
| MBC（含 MBC_stem-like、MBC_neuronal、MBC_chondroid，4 簇） | 文本可指名：EPCAM、KRT8、KRT18、KRT19、TRPS1（"established epithelial BC marker genes"）——但判定注释用途不成立，**不补录**；每簇 top-5 marker 在 ED Fig. 3a,b（图片，文本不可恢复） | Results, Fig. 2g 段："Inter-patient variability in established epithelial BC marker genes (EPCAM, KRT8, KRT18, KRT19 and TRPS1) was minimally impacted by receptor status but notably by profiling method (Fig. 2g)."；ED Fig. 3a,b 图注："Stacked violin plots depicting the expression of the top 5 cell type marker genes for each of the indicated cell types, detected by 1 vs. all differential expression analysis..." |
| Endothelial、Endothelial_sinusoidal、Endothelial_angiogenic、Endothelial_vascular（4 簇） | 文本无名（ED Fig. 3a,b / Supplementary Table 3） | 同上 ED Fig. 3a,b 图注 |
| Fibroblast | 文本无名 | 同上；注意：Methods 的胶原基因列表是 EMT 程序基因而非 fibroblast marker（见 A 门 A1-A17），不得误补 |
| Chondrocyte、Smooth muscle_vascular、Skeletal muscle、Stellate、Neuron、Keratinocyte | 文本无名 | 同上 |
| Monocyte、Neutrophil、Erythrocyte、Mast、B_plasma | 文本无名 | 同上 |

（处理建议：以上 21 簇确属整簇漏提，但 marker 基因名需查论文 ED Fig. 3a,b 图版与 Supplementary Table 3 才能补录，超出本次 review_md 文本复核能力；建议在总表以"漏提-待图版核对"记录或维持现状并注明原因。）

---

## 附：本次复核验证过的全部关键原句（供追溯）

1. Methods, Scoring of expression programs（EMT 程序基因 52 个 + MERFISH/ExSeq 20 个子集 + CODEX 3 个）——A1-A17 判定依据。
2. Methods, De novo cell type annotation of the cell-segmented MERFISH data："we performed manual cluster-wise and marker gene-based annotation as is frequently done in scRNA-seq data... assigned new cell type labels only when clusters clearly displayed features that did not match to any previously annotated cell types, which was the case for a small population of potentially regulatory B cells expressing FOXP3 in addition to the typical B cell marker FCRL5."——M01305/M01306/M01307 判定依据。
3. Methods, Gene panel design（九类基因选择，Canonical cell-type-specific markers / Clinical BC biomarkers / BC intrinsic subtypes / Hallmarks of cancer (含 MKI67 为 proliferation 例) / Epithelial hierarchy / ER signaling / Genomic landscape；297 基因覆盖 all major cell types；ALB/LIPE "for ready identification of... hepatocytes... adipocytes"）——B 门升级与 A19-A25 判定依据。
4. Results, Fig. 4f 段："CD163, a key macrophage marker"——M01311 升级依据。
5. Results, Fig. 5a 段（双栏重排）："Across all methods, there were two major clusters of highly correlated method-specific clusters: a CD163+ cluster with high expression of macrophage markers as well as HIF1A and APOE/APOC1 and a CD163− cluster associated with lower macrophage marker expression and expression of MKI67 (Extended Data Fig. 9c,d)."——APOE/HIF1A/APOC1/MKI67 判定依据。
6. Discussion 前 Results 段（双栏重排）："Across methods, we identified two macrophage states characterized by CD163/CD68/APOE/HIF1A and MKI67, respectively."——同上。
7. Results, Fig. 2g 段（双栏重排）："Inter-patient variability in established epithelial BC marker genes (EPCAM, KRT8, KRT18, KRT19 and TRPS1) was minimally impacted by receptor status but notably by profiling method (Fig. 2g)."——KRT8/18/19/TRPS1/EPCAM→MBC 判定依据。
8. Results, EMT 表型段（双栏重排）："EMT-patched and EMT-high phenotypes were each characterized by distinct cell cycle genes (EMT-patched: CCND1, RB1 and NF1; EMT-high: CDC20); EMT-low samples were further characterized by AGR2, a potential biomarker of poor prognosis53,54."——AGR2 判定依据。
