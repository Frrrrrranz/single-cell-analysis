# DOI_10.1101_2025.09.26.678707 复核判定报告

论文：Cellular and Spatial Drivers of Unresolved Injury and Functional Decline in the Human Kidney（Human Kidney Atlas v2；snRNA/scRNA + Slide-seq2 + CosMx + 组织学/代谢组学）
原文：D:\OneDrive\Desktop\组\marker提取\review_md\DOI_10.1101_2025.09.26.678707.md
物种：人（患者队列；附小鼠 IRI 模型，仅图注出现小鼠符号 Pxdn/Sox4/Gdf15）

## 摘要

本篇判定统计：**补录 0、升级 12、恢复 0、移除 0、归属修正 0、维持不录 24（A门）+ 维持 annotation_marker 5（B门）**。

- A门 24 条：全部不录。其中噪声 token 17 条（H3K4me1/AKI/H3K27ac/CKD/H3K27me3/TAL/G6P/SHAP/ASSESS/CUT/RUN/ESKD/BKBC/KPMP/IMS/BPG/MBCO）；非噪声理由不录 7 条（CD4/CDKN1A/PXDN/REL/MID1/PCK1/GDF15，均为临床生物标志物、功能基因、转录因子活性、表观可视化目标或分割用抗体，双重门槛不满足）。
- B门 17 条：升级 author_declared 12 条（frPT/frTAL 6 条 + moMAC-HBEGF+ 6 条，Results 正文 "marked by" 措辞）；维持 annotation_marker 5 条（MD/PECs/resMAC-HLAIIhi 的 Methods 反卷积句，属方法/注释流程引用层级）；无归属错误。
- B2门 0 条；C门 0 条（本篇无候选）。
- D门：正文层面无整簇漏提（详见下）；物种、基因写法基本一致，1 处 αSMA→ACTA2 蛋白名转换备注；无归属错误。

---

## A 门逐条判定

| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CD4 | 不录 | — | — | — | — | Methods, CosMx（ED 图/方法段落） | After all imaging cycles were completed, additional visualization markers for morphology and cell segmentation were added including pan-cytokeratin, CD45, CD3, CD298/B2M, and DAPI. | **候选证据句转录有误**：原句为 "CD45, CD3, CD298/B2M, and DAPI"，无 CD4；全文 standalone CD4 出现 0 次（所有命中均为 CD45/CD44 子串）。且该句 marker 为成像后追加的**形态学/细胞分割可视化 marker**（IF 抗体），非细胞群注释 marker，双重门槛均不满足。existing.md 亦无 CD4 行，口径一致 |
| 2 | CDKN1A | 不录 | — | — | — | — | Results, 'Epithelial injury…SOX4'；ED Figure 11d | Consistently, there was an observed increase in the senescence / cell cycle arrest genes CDKN1A and KHDRBS1 and decrease in pro-reparatory GDF15 gene 77 after SOX4 perturbation (Figure 5f). / ED Figure 11d: Genomic region of CDKN1A visualized with Cut&Run tracks for histone marks (H3K27ac, H3K4me1, and H3K27me3) in healthy reference and AKI/CKD kidney tissue… | 非 marker 措辞（senescence/cell cycle arrest 功能基因分类）；Cut&Run 图注为表观基因组可视化目标基因，非注释 marker，无注释用途 |
| 3 | H3K4me1 | 不录-噪声token | — | — | — | — | 多处 | marks (H3K27ac, H3K4me1, and H3K27me3)… | 组蛋白修饰，非基因 |
| 4 | AKI | 不录-噪声token | — | — | — | — | 多处 | H3K4me1 histone marks in AKI and CKD diseased tissue. | 疾病缩写（acute kidney injury） |
| 5 | H3K27ac | 不录-噪声token | — | — | — | — | 多处 | active enhancer (H3K27ac/H3K4me1) histone marks through CUT&RUN analysis… | 组蛋白修饰，非基因 |
| 6 | CKD | 不录-噪声token | — | — | — | — | 多处 | …in AKI and CKD diseased tissue. | 疾病缩写（chronic kidney disease） |
| 7 | H3K27me3 | 不录-噪声token | — | — | — | — | 多处 | marks (H3K27ac, H3K4me1, and H3K27me3) in healthy reference and AKI/CKD kidney tissue | 组蛋白修饰，非基因 |
| 8 | TAL | 不录-噪声token | — | — | — | — | 多处 | characterized by increased expression of canonical healthy TAL genes (SLC12A1, WNK4, EGF, UMOD, and DEFB1) | TAL 是细胞名缩写（thick ascending limb），非基因。句中基因 SLC12A1/WNK4/EGF/UMOD/DEFB1 已收录于总表 healthy TAL 行（M01555-M01559，author_declared），无漏提 |
| 9 | PXDN | 不录 | — | — | — | — | Results, 'Biomarkers associated with chronic kidney disease progression' | Several genes associated with progressive decline in kidney function were identified as putative SOX4 targets, including MID1 and PXDN, the latter of which was identified as a secreted marker in both the TRIBE and BKBC cohorts (Figure 6b-c, h). | "secreted marker" 指**临床队列（TRIBE/BKBC）中与 AKI-to-CKD 进展相关的分泌型蛋白生物标志物**（预后 biomarker），非细胞群注释 marker；后续用途为 SOX4 调控机制分析（CUT&RUN）与 IHC 蛋白定位（PT/间质成纤维细胞），均非注释用途。双重门槛不满足 |
| 10 | G6P | 不录-噪声token | — | — | — | — | Figure 3f 图注 | Glucose, pyruvate, and lactate were used as indicators of glycolysis, while phosphoenolpyruvate (PEP), 1,3-bisphosphoglycerate (1,3-BPG), and glucose-6-phosphate (G6P) served as gluconeogenesis markers. | 代谢物（glucose-6-phosphate），非基因；"gluconeogenesis markers" 为代谢通路的代谢物指示，非细胞群识别用途（BRIEF 明确此类通常不收录） |
| 11 | SHAP | 不录-噪声token | — | — | — | — | ED Figure 10 图注 | The marker's size corresponds to the global SHAP importance score… | 机器学习方法（Shapley additive explanations），非基因 |
| 12 | REL | 不录 | — | — | — | — | Results, 'Resolved versus unresolved epithelial repair' | aPT2 expressed the injury markers CDH6, VCAM1 and HAVCR1 with REL (NF-kB) and KLF6 binding site activities (Figure 3b) 1,13,18,54,55. | REL 是转录因子（NF-kB 家族），句中为**结合位点活性分析对象**（"with REL (NF-kB) and KLF6 binding site activities"）；"injury markers" 措辞仅覆盖 CDH6/VCAM1/HAVCR1（均已收录，M01536-M01538），REL 非表达 marker 亦无注释用途 |
| 13 | ASSESS | 不录-噪声token | — | — | — | — | Results, 'Biomarkers of acute kidney injury' | …markers confirmed in two additional AKI cohorts (ASSESS and NAIKID, Supplemental Table 27). | 队列名（ASSESS-AKI study） |
| 14 | MID1 | 不录 | — | — | — | — | Results, 'Biomarkers associated with chronic kidney disease progression' | MID1 represents an E3 ubiquitin ligase upregulated in human DKD and murine fibrosis models 92 that may regulate STAT3 to modulate EMT and inflammation. Both MID1 and PXDN proteins were immunohistochemically confirmed to localize to PTs… | 无 marker 措辞（E3 泛素连接酶功能描述、putative SOX4 target）；IHC 定位为蛋白溯源确认，非细胞群注释用途 |
| 15 | CUT | 不录-噪声token | — | — | — | — | 多处 | …through CUT&RUN analysis in participants with AKI or CKD | CUT&RUN 方法名拆词（方法名） |
| 16 | RUN | 不录-噪声token | — | — | — | — | 多处 | …through CUT&RUN analysis in participants with AKI or CKD | CUT&RUN 方法名拆词（方法名） |
| 17 | PCK1 | 不录 | — | — | — | — | Results, 'Epithelial injury…GWAS'；ED Figure 7e/h 图注 | …identified a variant within a SOX9 (negative) and HNF4A (positive) regulatory site of the Phosphoenolpyruvate carboxykinase 1 (PCK1) gene (Figure 3e…). / e. Genomic region of PCK1 visualized with Cut&Run tracks for histone marks (H3K27ac, H3K4me1, and H3K27me3)… / h. 10X xenium data showing enrichment of PCK1 in PT compared to aPT and dPT in the same tubule | GWAS 调控位点基因/代谢功能基因/Cut&Run 可视化目标；Xenium 处为 "enrichment of PCK1 in PT" 富集展示措辞，无 marker 措辞、无注释用途 |
| 18 | ESKD | 不录-噪声token | — | — | — | — | Supplementary Table 28 标题 | Soluble protein markers significant in progression to ESKD in BKBC | 疾病缩写（end-stage kidney disease） |
| 19 | BKBC | 不录-噪声token | — | — | — | — | Results, 'Biomarkers associated with chronic kidney disease progression' | …plasma proteomics data from 418 participants in the BKBC cohort… | 队列名（Boston Kidney Biopsy Cohort） |
| 20 | KPMP | 不录-噪声token | — | — | — | — | Methods, 'Clustering single nucleus RNA data' | The sub-clusters are then annotated based on markers from KPMP version 1.0 and literature 10,11,106,108. | 数据库/联盟名（Kidney Precision Medicine Project）；句中 markers 指 KPMP 数据库提供的 marker，非 KPMP 本身为基因 |
| 21 | IMS | 不录-噪声token | — | — | — | — | Methods, 图像配准 | …affine transformation matrix that was created based on fiducial markers selected from the post-IMS AF and IMS modalities. | 成像方法（imaging mass spectrometry）；"fiducial markers" 为图像配准基准标记（方法学 marker），非基因非注释 marker |
| 22 | BPG | 不录-噪声token | — | — | — | — | Figure 3f 图注 | …phosphoenolpyruvate (PEP), 1,3-bisphosphoglycerate (1,3-BPG), and glucose-6-phosphate (G6P) served as gluconeogenesis markers. | 代谢物（1,3-bisphosphoglycerate），非基因 |
| 23 | MBCO | 不录-噪声token | — | — | — | — | Methods, 路径富集 | Condition- or subtype-selective marker genes were then submitted to pathway enrichment analysis using MBCO level-3 subcellular processes… | 本体（Molecular Biology of the Cell Ontology） |
| 24 | GDF15 | 不录 | — | — | — | — | Results, 'Therapeutic response monitoring'；ED Figure 11e | …GDF15, associated with AKI severity in both the TRIBE-AKI and NAIKID cohorts 53, showed expression in the TAL that was responsive to sodium-glucose cotransporter-2 inhibitor (SGLT2i) therapy… / Genomic region of GDF15 visualized with Cut&Run tracks for histone marks… | "pro-reparatory GDF15 gene" 为功能分类措辞；临床语境为 AKI 严重度生物标志物（TRIBE-AKI/NAIKID 队列）；在 TAL 的表达用于 SGLT2i 治疗响应监测；Cut&Run 为表观可视化目标。均非细胞群注释用途 |

---

## B 门逐条判定

判定依据原句（均已从 review_md 原文 grep 核实，跨行断行已按原文拼接）：

**句1（Results, 'Resolved versus unresolved epithelial repair'）**：
"Failed repair (fr) states were further marked by the expression of PROM1 (frPT and frTAL), ROBO2 and MEG3 (frPT), or ITGB8 and TMPRSS4 (frTAL) 1,56,57."

**句2（Results, 'Clinicopathologically-linked immune subtypes'）**：
"We also found another inflammatory population marked by expression of growth factors HBEGF and AREG, as well as proinflammatory genes PLAUR, IL1B, OSM and CXCL8, and that is consistent with a subtype found in rheumatoid arthritis 40 (Figure 2g-h, ED Figure 6f). This subtype (moMAC-HBEGF+) expressed genes that have been shown to promote parenchymal cell proliferation or regeneration (AREG, IL1B and OSM), which chronic exposure would impair (IL1B), supporting its role in an early transitory state (ED Figure 6f) 17."

**句3（Methods, 'Slide-seq2 Spatial Transcriptomics – Cell type deconvolutions'）**：
"Subclasses were assessed for marker gene expression and spatial localization and those showing less accurate predictions were subset based on non-zero expression of distinguishing marker genes (PECs – CFH; MD – BBOX1; resMAC-HLAIIhi – CD163, STAB1, C1QA)."

| marker_id | gene | cell_type | 判定 | 完整原句 | 理由 |
|---|---|---|---|---|---|
| M01549 | MEG3 | frPT | **升级 author_declared** | 句1 | "states were further marked by the expression of …" 为 BRIEF author_declared 典型措辞（"X cells marked by G"）；frPT 失败修复状态的识别/呈现 marker，注释用途成立。与总表已有 aPT2（"injury markers"）、healthy TAL（"canonical … genes"）行的 author_declared 口径一致 |
| M01550 | PROM1 | frPT | **升级 author_declared** | 句1 | 同上；括注 "(frPT and frTAL)" 明确该基因同时为两状态 marker |
| M01551 | ROBO2 | frPT | **升级 author_declared** | 句1 | 同上；括注 "(frPT)" 归属正确 |
| M01552 | ITGB8 | frTAL | **升级 author_declared** | 句1 | 同上；括注 "(frTAL)" 归属正确 |
| M01553 | PROM1 | frTAL | **升级 author_declared** | 句1 | 同上；括注 "(frPT and frTAL)" 明确含 frTAL |
| M01554 | TMPRSS4 | frTAL | **升级 author_declared** | 句1 | 同上；括注 "(frTAL)" 归属正确 |
| M01560 | BBOX1 | MD | **维持 annotation_marker** | 句3 | BBOX1 确认在 distinguishing marker genes 列表（MD – BBOX1），gene-cell 映射无误、无归属错误；但该句为 Methods 中 Slide-seq2 反卷积流程的**程序性描述**，按 BRIEF 层级 "annotation_marker（方法/注释流程引用的 marker）" 正是此类，不满足 author_declared（Results 正文生物学声明）层级 |
| M01566 | AREG | moMAC-HBEGF+ | **升级 author_declared** | 句2 | "population marked by expression of …" 明确 marker 措辞，"growth factors" 为基因功能角色描述、不否定其作为该群识别 marker 的身份；该群以 HBEGF+ 命名（Figure 2g-h 呈现），注释用途成立 |
| M01567 | CXCL8 | moMAC-HBEGF+ | **升级 author_declared** | 句2 | "marked by expression of … proinflammatory genes PLAUR, IL1B, OSM and CXCL8" —— "marked by" 动词短语统辖全列表；按 BRIEF "作者用于注释的 marker 列表整体收录，不得因看起来像功能基因而剔除" |
| M01568 | HBEGF | moMAC-HBEGF+ | **升级 author_declared** | 句2 | 细胞群以 HBEGF+ 命名，"marked by expression of growth factors HBEGF and AREG" —— marker 身份与注释用途最强 |
| M01569 | IL1B | moMAC-HBEGF+ | **升级 author_declared** | 句2 | 同 M01567 |
| M01570 | OSM | moMAC-HBEGF+ | **升级 author_declared** | 句2 | 同 M01567 |
| M01571 | PLAUR | moMAC-HBEGF+ | **升级 author_declared** | 句2 | 同 M01567 |
| M01573 | CFH | PECs | **维持 annotation_marker** | 句3 | CFH 确认在列表（PECs – CFH），映射无误；同 M01560 理由（Methods 流程句 = annotation_marker 层级） |
| M01580 | C1QA | resMAC-HLAIIhi | **维持 annotation_marker** | 句3 | C1QA 确认在列表（resMAC-HLAIIhi – CD163, STAB1, C1QA），映射无误；同 M01560 理由 |
| M01581 | CD163 | resMAC-HLAIIhi | **维持 annotation_marker** | 句3 | CD163 确认在列表，映射无误；同 M01560 理由 |
| M01582 | STAB1 | resMAC-HLAIIhi | **维持 annotation_marker** | 句3 | STAB1 确认在列表，映射无误；同 M01560 理由 |

B门小结：升级 12、维持 5、归属修正 0。升级与维持的分界 = Results 正文 "marked by" 生物学声明（author_declared）vs Methods 反卷积流程引用（annotation_marker），与总表现有先例（REN 行 M01579 为 Methods 句且 annotation_marker）口径一致。

---

## B2 逐条判定

本篇无 B2 候选。

## C 门逐条判定

本篇无 C 候选。

---

## D 门检查结论

### 1. 聚类对账
- 正文报告的人 atlas 规模："This strategy enabled a high level of cell type resolution, identifying 128 distinct cell identities including 60 altered cell states (ED Figure 1) having distinct marker gene profiles (SD Figure 2, Supplementary Table 12)."；小鼠 atlas："Integrative analyses identified 111 annotated cell types and 44 altered cell states with distinct marker gene profiles (Supplementary Table 16, 17, SD Figure 5)."
- 总表 48 行覆盖 18 个去重 cell_type：aPT2、C-FIB-OSMRhi、C-MYOF、frPT、frTAL、healthy TAL、MD、moFAM、moMAC-CXCL10+、moMAC-HBEGF+、MON、PECs、pvFIB-PI16+、pvFIB-RSPO3+、pvMYOF、REN+ cells、resMAC-HLAIIhi、resMAC-LYVE1+。
- 逐一核对正文各 Results 章节（Interstitial fibroblasts / Perivascular fibroblasts / Clinicopathologically-linked immune subtypes / Resolved versus unresolved epithelial repair / 空间生态位 / 生物标志物翻译）：**凡正文给出基因级 marker 证据的细胞群均已在总表**。正文提及但无正文基因级 marker 证据的群（marker 清单只在补充材料/图中）：aPT1、aTAL1（仅 "EGF was downregulated…CREB5, ITGA3, ITGB6 were upregulated" 富集措辞）、aTAL2、healthy PT（PT-S1/S2/S3）、dPT、C-FIB-PATH、C-FIB-OSMRlo、pvFIB、EC-AEA/EC-DVR/EC-GC、淋巴系（CD8+ TEM/TEMRA/TRM、NK、PL、naïve T、ILC3、B）、pDC、cDC1、mDC、MAIT、ncMON、POD。各 dot plot 图注（"Middle, dotplot showing average expression values for selected marker genes" 等）不含基因名单。
- **结论：正文层面无整簇漏提可补录**（18 个有正文 marker 证据的群全部覆盖；其余 ~110 个身份的 marker 基因清单在 SD Figure 2/Supplementary Table 12 等补充材料中，review_md 不含，无法审计——属覆盖范围限制而非漏提）。基因级边缘项（resMAC-LYVE1+ 的 MERTK/IGF1/PDGFB/PDGFC、pvFIB-RSPO3+ 的 WNT5B/IGF1、moFAM 的 TREM2、aTAL1 的 IL11/LIF）均为 "expressed 功能基因" 措辞，无 marker 措辞，不满足身份门槛，不补录。

### 2. marker 归属核对
- PROM1 挂 frPT 与 frTAL 两行：原句括注 "(frPT and frTAL)"，归属正确。
- CCL2 挂 C-FIB-OSMRhi（M01540）与 moMAC-CXCL10+（M01563）：分别来自 "expressed genes…including IL1R1, CCL2, CXCL10, CCL19 and the Oncostatin-M receptor (OSMR)" 与 "M1-like pro-inflammatory CXCL10+ CXCL9+ CCL2+ state (moMAC-CXCL10+)" 两个不同句子，均正确。
- CXCL10 挂 C-FIB-OSMRhi 与 moMAC-CXCL10+：同上两处语境，均正确。
- CD34 挂 pvFIB-PI16+："CD34+/PI16+ adventitial fibroblasts" 与 "A second progenitor subtype (pvFIB-PI16+) expressed CD34, MFAP5 and PI16"，正确。
- 未发现 Ngfr 型归属错误；B 门 17 条均无归属不符。

### 3. 物种一致性
论文主体为人（患者队列/健康参考者），48 行 species 均 human，正确。小鼠基因符号（Pxdn、Sox4、Gdf15）仅出现于小鼠 IRI 图注，未被收录，无物种混淆。

### 4. 基因写法核对
48 行基因全大写（人源规范），与原文一致。1 处备注：M01578（pvMYOF, ACTA2）原句为 "αSMA+ myofibroblast (pvMYOF) states"——αSMA 为蛋白名，ACTA2 为其 HGNC 基因符号，属蛋白名→基因符号转换（可接受，建议行备注注明原文用 αSMA）。其余无写法偏差；CD298/B2M（Methods 面板句）未收录，无影响。

### 5. 跨篇一致性
48 行 four_layer_category 均 outside（肾脏，非 PNS），一致；cell_type 均采用作者原文标签（aPT2、frPT、frTAL、C-FIB-OSMRhi、moMAC-HBEGF+ 等），与原文命名一致。

---

## 归属修正明细

无。

## 整簇漏提明细

无（正文层面所有带基因级 marker 证据的细胞群均已收录；其余细胞身份的 marker 清单仅存在于补充材料，review_md 无法核实，不构成可补录项）。
