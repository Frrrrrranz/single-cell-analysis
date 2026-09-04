# DOI_10.1038_s41588-022-01243-4（人肺空间图谱 / GAIN）复核判定报告

> 判定方式：recheck-pipeline-v2（证据包 + 主代理直判 + 定向 grep 重组双栏拼接句；PDF 原文核对 CADM 拼写）
> 判定日期：2026-09-03

## 摘要

补录 5（A 门 1 + D 门整簇 4）；升级 28（B 门 1 + B2 门 2 + C 门合并升级 1 + D 门顺带 24）；移除 4（C 门 LPO 重复 1 + IR-fibro 命名重复 2 + CD4 T cell 语义重复 1）；标签修正 7；locator 更新 4；**is_pns_cell 系统性修正 72 行**（全表 85 行误设 true → 仅 Schwann 13 行 true）；维持不录 A 门 24 条（含自动噪声 10）+ B2 维持排除 4 条。
总表行数：85 → 86。

## A 门逐条判定（26 条）

| # | 候选基因 | 判定 | 理由与原句（重组后） |
|---|---|---|---|
| 1 | CD31 | 不录 | Fig.4g 图注：multiplex IHC 面板结构定位染色 "Hoechst for nuclei, EpCAM for epithelium, Phalloidin for actin, CD31 for vessels"——组织结构取向染色，无 marker 措辞、无聚类注释用途 |
| 2 | CD45RA | 不录 | EDF10i 图注（重组）："IHC staining of CD4, CD45RO (memory marker), CD45RA (naive marker), IgA2 and EpCAM in the SMG. Blue arrows indicate CD4+CD45RA+ cells."——有 "(naive marker)" 措辞但 CD45RA 为 PTPRC 剪接异构体蛋白（无对应基因符号可录）；用于 IHC 区分 T 细胞 naive/memory 状态而非聚类注释 |
| 3 | EpCAM | 不录 | 同 #1："EpCAM for epithelium" 泛上皮结构取向染色；L1546 "IHC staining of HLA-DR, EpCAM, CD3, CD31 and CD4" 亦为面板背景染色 |
| 4 | SMG | 不录-噪声 | 细胞类型缩写 |
| 5 | IgA2 | **不新增行；升级现有 M00284（IGHA2）** | IgA2 蛋白对应基因 IGHA2；Fig.4g 图注 "B lineage markers (IgD, IgA2 and IgG)" 明确 marker 措辞，用于 "confirm the presence of IgA2 but the absence of IgG cells in the SMG"（识别用途）→ M00284 plasma cells (IgA)/IGHA2 升级 author_declared，locator 补 Fig. 4g legend |
| 6 | HLCA | 不录-噪声 | 数据集名 |
| 7 | HPA | 不录-噪声 | 数据库名 |
| 8 | NAF | 不录-噪声 | 细胞类型缩写 |
| 9 | LTSR | 不录-噪声 | 统计量 |
| 10 | AT2 | 不录-噪声 | 细胞类型缩写 |
| 11 | VDJ | 不录-噪声 | 测序方法 |
| 12 | COL15A | 不录（同义重复） | EDF4a 图注 "staining of PB-Fibro markers (COL15A and ENTPD1)"——COL15A 为 COL15A1 之论文截断写法；现有 M00275 (PB-fibro/COL15A1/author_declared) locator 已含 EDF 4a,b，已覆盖 |
| 13 | IPF | 不录-噪声 | 疾病缩写 |
| 14 | LMCD1 | 不录 | EDF4c 图注（重组）："Selected upregulated genes associated with COPD or emphysema by GWAS (RGCC, DGKH, NTM, SULF1, NPC2, RPL5, LMCD1, MRTFA, DENND5A, KLF4) or in other studies (NFATC2, MT2A and SIK2)"——疾病相关上调基因，非 marker |
| 15 | MRTFA | 不录 | 同 #14 |
| 16 | DENND5A | 不录 | 同 #14 |
| 17 | KLF4 | 不录 | 同 #14 |
| 18 | NFATC2 | 不录 | 同 #14（"in other studies" 上调基因） |
| 19 | MT2A | 不录 | 同 #14 |
| 20 | EVX1 | 不录 | Results 神经节（重组）："…with EVX1, a key gene in spinal cord development, identified as a potential regulator of mSchwann cells in the airways."——作者称 transcription factor / key gene / potential regulator，非 marker |
| 21 | NPR2 | 不录 | EDF6d 图注（重组）："NPR2 staining in oesophagus and bronchus from the HPA. Black arrows indicate the airway and oesophagus surrounding non-vascular smooth muscle."——HPA 蛋白染色用于指示组织区域，无 marker 措辞、无聚类注释用途 |
| 22 | ASM | 不录-噪声 | 细胞类型缩写（airway smooth muscle） |
| 23 | PLMM | 不录-噪声 | 统计方法 |
| 24 | VCAN | 不录（归入 B2 门处置） | Methods 假时间根判定句："root was identified as the cell with the highest combined expression of canonical progenitor markers (VCAN for chondrocytes; TGM2, HMCN2 and SULF1 for smooth muscle)"——marker 措辞指向祖细胞身份，非成熟聚类注释（详见 B2 门） |
| 25 | PTPRC | 不录 | EDF3a 图注（重组）："smFISH staining in human bronchi tissue for IR-Fibro markers (CCL21, CCL19) showing independent localisation from immune cells (PTPRC) and smooth muscle cells (ACTA2) marked by arrows."——泛白细胞 smFISH 标识（定位/排除用途），非特定细胞群 marker |
| 26 | CADM | **补录（存疑标注）** | EDF5g 图注（PDF 原文核对，论文即写作 CADM）："HPA antibody staining of (g) non-myelinating Schwann cell markers (CADM, GRIK2, NCAM1, ITGB4 and L1CAM)"——明确 marker 措辞；新行：nonmyelinating Schwann cells (nmSchwann)/CADM/author_declared/EDF 5g legend；CADM 非标准 HGNC 符号（疑为 CADM1 之论文写法），notes 标注"原文即写作 CADM，待图版核对" |

## B 门逐条判定（4 条）

| marker_id | gene | cell_type | 判定 | 完整原句（重组后） | 理由 |
|---|---|---|---|---|---|
| M00250 | ABCC9 | IR-Ven-Peri | 维持 figure_labeled | "The IR-Ven-Peri expressed ABCC9 and ICAM1 but not CSPG4, similar to postcapillary venous perivascular cells important for immune cell homing to peripheral lymph nodes (Fig. 3d,e)."（Results §Vascular cell types） | 表达陈述句无 marker 措辞；Fig.3d marker gene dot plot 支撑 figure_labeled 定级恰当 |
| M00254 | CSPG4 | IR-Ven-Peri | 维持 figure_labeled（负极性） | 同上句 "but not CSPG4" | 现有行 polarity=negative 正确记录非表达特征（区分 IR-Ven-Peri 与 pericyte）；负极性行合法，无 marker 措辞不升级 |
| M00256 | ICAM1 | IR-Ven-Peri | 维持 figure_labeled | 同 M00250 句 | 同 M00250 |
| M00264 | CD14 | macro-intermediate | **升级 author_declared** | "We identified a previously undefined cluster expressing monocyte (CD14) and macrophage markers, termed macro-intermediate (Extended Data Fig. 8b)." | "monocyte (CD14) and macrophage markers" 明确 marker 措辞 + termed 命名用途；locator 补 Results 句 |

## B2 门逐条判定（7 条）

| 基因 | cell_type | 判定 | 完整原句（重组后） | 理由 |
|---|---|---|---|---|
| VCAN | chondrocytes | **维持排除** | "root was identified as the cell with the highest combined expression of canonical progenitor markers (VCAN for chondrocytes; …)"（Methods，验证外部数据集假时间根） | "canonical progenitor markers" 指向祖细胞身份（progenitor state）；该句为 Methods 轨迹根判定而非聚类注释，恢复入 chondrocytes 会造成祖/成熟细胞错误归属 |
| TGM2 | smooth muscle | **维持排除** | 同上句 "TGM2, HMCN2 and SULF1 for smooth muscle" | 同上 |
| HMCN2 | smooth muscle | **维持排除** | 同上 | 同上 |
| SULF1 | smooth muscle | **维持排除** | 同上（另 L1441 SULF1 出现于 COPD GWAS 上调基因列表，亦非 marker 语境） | 同上 |
| CADM | nmSchwann | **恢复补录（author_declared）** | EDF5g："HPA antibody staining of (g) non-myelinating Schwann cell markers (CADM, GRIK2, NCAM1, ITGB4 and L1CAM)" | 与 NCAM1/ITGB4/L1CAM（均已在表）并列的明确 marker 措辞；原排除理由（unresolved）现已解决 |
| GRIK2 | nmSchwann | **升级 author_declared**（B①补充） | 同上句 | 同句 marker 措辞；M00024 supplementary_marker → author_declared，locator 补 EDF 5g legend |
| ITGB4 | nmSchwann | **升级 author_declared**（B①补充） | 同上句 | 同上；M00025 |

## C 门逐条判定（1 组）

| 组 | 行1 | 行2 | 判定 | 保留 | 移除 | 理由 |
|---|---|---|---|---|---|---|
| LPO | M00294 SMG serous cell/LPO/annotation_marker | M00297 SMG-serous/LPO/figure_labeled | **合并（保留 M00294 并升级）** | M00294 | M00297 | 同一细胞群（serous）同一基因；M00294 升级 author_declared，locator 合并为 "Results (Fig. 5g; Extended Data Fig. 10d,e); Fig. 4b legend; Extended Data Fig. 7d legend" |

## D 门检查结论

### D1 聚类对账

论文聚类全集 vs existing 覆盖：神经节四新簇（mSchwann/nmSchwann/endoneurial NAF/perineurial NAF）✓、成纤维系列（IR-fibro/PB-fibro/PC-fibro）✓、血管系列（IR-Ven-Peri/venous endothelia）✓、SMG 系列（duct/serous/mucous/myoepithelial）✓、髓系新亚群（macro-intermediate/Macro-CCL/Macro-alv-MT/CHIT1+/intravascular）✓、软骨细胞 ✓、浆细胞/IgA plasma ✓。

本轮 D 门补录整簇缺口（气道上皮参考类型，此前整簇漏提）：
- **smooth muscle cells | ACTA2**（EDF6f "venous endothelia (ACKR1) and smooth muscle (ACTA2) markers"）
- **secretory goblet/club cells | SCGB1A1**（EDF7e）
- **ciliated cells | FOXJ1**（EDF7e）
- **basal cells | KRT14**（EDF7i "basal epithelia (KRT14)"）

整簇漏提留档（marker 基因名仅存在于图版/补充表，review_md 不可恢复，不强行补录）：T/NK 亚群（CD4-naive/CM、CD4-EM/Effector、Treg、CD4-TRM、γδT、CD8-EM/EMRA、CD8-TRM/EM、MAIT、NK、NKT、ILC）、B 系亚群（naive B、memory B）、血管亚型（E-Art-syst/pulm、E-Ven-syst、SM-pulm、SM-syst、SM-Art-syst、Peri-pulm、Peri-syst、ASM）、megakaryocytes、mast cells、SMG-basal、dividing basal、deuterosomal、ionocyte、suprabasal。EDF8/EDF9 marker dot plot 图注存在但未点名基因（"Marker gene expression dot plot for B-lineage cells" 等）。

### D2 归属核对（Ngfr 型错误）

**未发现归属错误**。负极性行逐条核对均正确：
- M00254 CSPG4/IR-Ven-Peri（negative）✓——"expressed ABCC9 and ICAM1 but not CSPG4"
- M00295 SMG serous cell/RARRES1（negative）✓——"serous cells (LPO+RARRES1−APRILhigh)"（Fig. 5g; EDF 10d,e）；RARRES1 阳性行正确挂在 SMG duct cells（M00293，"duct (ALDH1A3/RARRES1)"，Fig. 4b; EDF 7e）
- M00267 DES/myoepithelial cells（negative）✓

（过程记录：复核中曾怀疑 CSPG4/RARRES1-serous 为归属错误，经 existing.md 极性字段核对证伪——两行本就是 negative 极性，记录正确。）

### D3 物种一致性

本篇 human，全部行 species=human ✓，无鼠式写法行。

### D4 跨篇一致性

IR-fibro、IR-Ven-Peri、NAF 系列、SMG 系列为本篇特有命名；与肺图谱（DOI_10.1038_s41586-020-2922-4，HLCA 体系）共享的参考类型（ciliated/basal/secretory 等）命名风格差异留批次层面统一处理。

### D5 基因写法核对

| 项 | 处置 | 依据 |
|---|---|---|
| CADM（EDF5g） | 按原文收录 CADM + notes 存疑标注 | PDF 原文（p.25）即写作 "CADM"；非标准 HGNC 符号（疑为 CADM1），待图版核对 |
| COL15A（EDF4a 论文写法） | 无动作 | 论文截断写法；表内正确用 COL15A1（M00275） |

### D6 标签统一

| marker_id | 现值 | 修正 | 依据 |
|---|---|---|---|
| M00240/M00241 | immune recruiting fibroblasts (IR-fibro) | cell_type → **IR-fibro** | 与 M00244-249 短名统一（6:2 多数）；重命名后与 M00244/M00245 同键 → 后者移除、locator 并入 |
| M00244/M00245 | IR-fibro/CCL19、CCL21（figure_labeled） | **移除（命名重复）** | 与 M00240/M00241（author_declared）重命名后同键；Fig. 2c legend 证据并入 M00240/M00241 |
| M00236/M00237 | endoneurial nerve-associated fibroblasts (NAF) | cell_type → **endoneurial NAF** | 与 M00235 短名统一；无键冲突（USP54 vs OSR2/SOX9） |
| M00294/M00295 | SMG serous cell | cell_type → **SMG serous cells** | 与 "SMG duct cells" 复数风格统一 |
| M00296 | SMG-mucous | cell_type → **SMG mucous cells** | 同上；论文正文用 "SMG mucous and serous cells"（L325） |
| M00227 | CD4 T cell/CD4（Fig. 6 schematic） | **移除（语义重复）** | Fig. 6 schematic 的 "CD4 T cells" 与 Fig. 4g/Results 的 "CD3+ CD4+ T helper cells" 为同一群（GAIN 内 CD4 T 细胞）；保留 M00228（正文+IHC 证据更强），locator 并入 Fig. 6 schematic |

### D7 D 门顺带升级（图注/正文明确 marker 措辞，证据句已重组核实）

| marker_id | gene | cell_type | 升级依据原句 | locator |
|---|---|---|---|---|
| M00013-M00016 | NFASC/NCMAP/MBP/PRX | mSchwann | Results（重组）："we identified the following four new clusters relating to airway peripheral nerves: myelinating Schwann cells (mSchwann) (NFASC, NCMAP, MBP and PRX), …"；"nmSchwann and mSchwann cell marker genes were enriched in cell adhesion and myelination gene sets" | Results §Four distinct cell types in airway peripheral nerves; Extended Data Fig. 5a,b |
| M00017-M00021 | NGFR/SCN7A/CHD2/L1CAM/NCAM1 | nmSchwann | 同上句 "nonmyelinating Schwann cells (nmSchwann) (NGFR, SCN7A, CHD2, L1CAM and NCAM1)"；L1CAM/NCAM1 另有 EDF5g "non-myelinating Schwann cell markers (… L1CAM)" | 同上; Extended Data Fig. 5g |
| M00023 | SOX10 | nmSchwann | Fig. 2i 图注（重组）："Nerve-associated cell type markers have distinct locations in the airway nerve bundles identified by smFISH staining"；EDF5j "non-myelinating (SCN7A, SOX10) Schwann cell … specific genes"；SOX10 为 Fig. 2i smFISH 通道 | Fig. 2i legend; Extended Data Fig. 5j |
| M00024/M00025 | GRIK2/ITGB4 | nmSchwann | EDF5g "non-myelinating Schwann cell markers (CADM, GRIK2, NCAM1, ITGB4 and L1CAM)"（B2 门处置） | Extended Data Fig. 5g legend |
| M00235 | USP54 | endoneurial NAF | EDF5h："endoneurial NAF marker (USP54)" | Extended Data Fig. 5h legend |
| M00279/M00281 | SLC22A3/SORBS1 | perineurial NAF | EDF5i："perineurial NAF markers (SLC22A3 and SORBS1)" | Extended Data Fig. 5i legend |
| M00246-M00249 | CXCL12/CXCL13/FDCSP/GREM1 | IR-fibro | Fig. 2c 图注（重组）："Dot plot of IR-fibro marker genes that overlap with Fibroblast reticular cell and fDC markers." | Fig. 2c legend |
| M00240/M00241 | CCL19/CCL21 | IR-fibro | 同上句 + EDF3a："smFISH staining in human bronchi tissue for IR-Fibro markers (CCL21, CCL19)"（locator 并入，类型不变） | preamble; Fig. 2c legend; Extended Data Fig. 3a legend |
| M00251/M00253 | CCL19/CCL21 | IR-Ven-Peri | Fig. 3g 图注（重组）："IR-Ven-Peri markers CCL21 and CCL19 localize adjacent to the venous vessel marker ACKR1"；EDF6f："smFISH staining for IR-Ven-peri (CCL21, CCL19), venous endothelia (ACKR1) and smooth muscle (ACTA2) markers" | Fig. 3g legend; Extended Data Fig. 6f legend |
| M00264 | CD14 | macro-intermediate | B 门（"monocyte (CD14) and macrophage markers, termed macro-intermediate"） | Results §Myeloid cells; Extended Data Fig. 8b |
| M00282 | MZB1 | plasma cells | locator 修正（原 EDF 9b 有误）：EDF9c 图注 "B plasma marker MZB1 in the bronchus (d) and nasopharyngeal glands (e)"；Results "Enrichment of plasma cells (MZB1+)" | Results; Extended Data Fig. 9c legend (panels d,e) |
| M00284/M00285 | IGHA2/IGHD | plasma cells (IgA/IgD) | Fig. 4g 图注 "B lineage markers (IgD, IgA2 and IgG)" + 正文 "We also detected IgD+ naive B cells and CD3+ CD4+ T helper cells in the human SMG (Fig. 4g)" | Methods, COVID-19 data analysis; Fig. 4g legend |
| M00292 | MIA | SMG duct cells | EDF7d 图注："smFISH staining for mucous (MUC5B), serous (LPO) and duct (MIA) cell markers in human bronchi sections" | Results §Identification of duct cells; Extended Data Fig. 7d legend |
| M00294 | LPO | SMG serous cells | 同上句 "serous (LPO) … cell markers"（C 门合并升级） | Results (Fig. 5g; EDF 10d,e); Fig. 4b legend; Extended Data Fig. 7d legend |
| M00296 | MUC5B | SMG mucous cells | 同上句 "mucous (MUC5B) … cell markers" | Fig. 4b legend; Extended Data Fig. 7d legend |
| M00298 | ACKR1 | venous endothelial cells | Fig. 3g "the venous vessel marker ACKR1" + EDF6f "venous endothelia (ACKR1) … markers" | Fig. 3g legend; Extended Data Fig. 6f legend |

维持不动（核过无升级依据）：M00022 MLIP（EDF5j "specific genes" 非 marker 措辞）、M00242/M00243 LYVE1/MAF（"expressing"）、M00258-M00260 MT 系列（"expressing metallothioneins, including"）、M00261-M00263 Macro-CCL（"expressing chemokines"）、M00238/M00239 CCR10/TNFRSF17（已 author_declared ✓）、M00250/M00254/M00256（B 门维持）、M00265-M00274 myoepithelial 系列（已 author_declared ✓）、M00291/M00293 ALDH1A3/RARRES1 duct 行（无点名 marker 措辞，维持 annotation_marker）。

### D8 is_pns_cell 系统性修正

本篇 85 行全部误设 is_pns_cell=true（提取期系统性错误；对照：肺图谱全 false 正确、乳腺癌全 false 正确）。按白名单规则（neurons、Schwann cells、satellite cells → true）：
- 保持 true：M00013-M00025（mSchwann/nmSchwann 共 13 行）
- 修正为 false：其余 72 行（含 NAF 系列成纤维细胞、SMG、免疫、血管、软骨等）

新补录 5 行按同规则赋值：CADM（nmSchwann）true；ACTA2/SCGB1A1/FOXJ1/KRT14 false。

## 试点遗留 B 候选处置（PMID_35115729，并入 Batch 1）

| marker_id | gene | cell_type | 判定 | 依据 | 理由 |
|---|---|---|---|---|---|
| M01516 | Pdgfra | endoneurial fibroblasts (EFs) | **升级 author_declared** | "EFs express the fibroblast marker Pdgfra as well as the stem cell markers Cd34 and nmSC marker Ngfr"（Results p.4）；"Endoneurial fibroblasts express Pdgfra as well as Cspg4 and Enpp2 (Figure 1e)" | "fibroblast marker Pdgfra" 明确 marker 措辞 + 直接归属 EFs |
| M01517 | Cd34 | endoneurial/epineurial fibroblasts | **维持 annotation_marker** | 同句 "stem cell markers Cd34"；"endoneurial/epineurial fibroblasts expressed Pdgfra and Cd34" | "stem cell markers" 措辞指向干性身份而非 fibroblast 群的识别/命名；对 fibroblast 行注释用途不成立，不升级 |

## 计数（供落表脚本与批次报告）

- 补录：5 条（CADM、ACTA2/smooth muscle cells、SCGB1A1/secretory goblet/club cells、FOXJ1/ciliated cells、KRT14/basal cells）
- 升级：28 条 = B 门 1（M00264）+ B2 门 2（M00024/M00025）+ C 门 1（M00294）+ D 门 24（M00013-21 九条、M00023、M00235、M00279、M00281、M00246-49 四条、M00251、M00253、M00284、M00285、M00292、M00296、M00298）
- 移除：4 条（M00297 LPO 重复、M00244/M00245 IR-fibro 命名重复、M00227 CD4 T cell 语义重复）
- 标签修正：7 条（M00240/M00241→IR-fibro、M00236/M00237→endoneurial NAF、M00294/M00295→SMG serous cells、M00296→SMG mucous cells）
- locator 更新：4 条（M00240/M00241、M00282、M00228）
- is_pns_cell 修正：72 条
- 维持不录：A 门 24（自动噪声 10 + 人工不录 14）；B2 门维持排除 4（VCAN/TGM2/HMCN2/SULF1）
- 总表行数：85 → 86
- 另：试点遗留 M01516 升级 author_declared（PMID_35115729）
