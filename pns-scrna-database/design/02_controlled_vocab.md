# 02 · 外周神经系统(PNS)单细胞数据库 — 受控词表(Controlled Vocabulary)

> 用途：本表是 DeepSeek V4 在「信息提取」阶段统一用词的唯一权威参考。提取细胞类型、组织部位、平台、分析工具时，**必须把原文表述映射到本表的「标准名」**，再写入数据库字段。
>
> 强制规则(与 04/06 文件一致)：
> 1. **marker 命名**：人类 = 全大写(`SOX10`)；小鼠/大鼠 = 首字母大写其余小写(`Sox10`)。提取时按论文物种自动转换大小写。
> 2. **多值字段**：用分号 `;` 分隔(中间无空格或单空格均可，入库脚本会归一化)。
> 3. **缺失值**：一律填 `NA`，**严禁臆造**。原文没写就是 `NA`。
> 4. **未在本表内**的术语：保留原文写法并在该字段后追加 `(uncontrolled)` 标记，交主人抽查时人工补录词表，**不要强行套最近的标准名**。
> 5. **大类(category)字段**取值固定为下表第 1 部分的大类英文枚举值。

---

## 第 1 部分 · 外周神经细胞类型本体(Cell Type Ontology)

字段说明：
- **标准名(standard_name)**：写入 `cell_types.cell_type` 的取值。
- **同义词/缩写(synonyms)**：原文出现这些写法时映射到标准名。
- **is_pns_cell**：`yes` = 外周细胞;`context` = 需结合组织判断(如运动神经元/巨噬细胞);`no` = 通常为中枢/无关(列出用于反向排除)。
- **关键 marker**：示例按「人类大写 | 鼠首字母大写」给出,提取时按论文物种取一种大小写。

### 1.1 大类枚举(category 字段取值)

| category 枚举值 | 中文 | 说明 |
|---|---|---|
| `sensory_neuron` | 感觉神经元 | DRG/TG/nodose 等感觉节内神经元 |
| `autonomic_neuron` | 自主神经元 | 交感/副交感节后神经元 |
| `enteric_neuron` | 肠神经元 | ENS 肌间丛/黏膜下丛神经元 |
| `schwann_glia` | 施万细胞 | 髓鞘型/Remak/修复型 |
| `satellite_glia` | 卫星胶质 | 神经节内 SGC |
| `enteric_glia` | 肠胶质 | ENS 胶质 |
| `microenvironment` | 微环境/基质免疫血管 | 成纤维/巨噬免疫/内皮/周细胞等 |
| `pan_neuron` | 泛神经元(未细分) | 仅标注"neuron"未细分亚群时 |

---

### 1.2 感觉神经元(sensory_neuron) — 含亚群细分

> 感觉神经元亚群命名以 Usoskin/Zeisel/Sharma/Tavares-Ferreira 等 DRG 图谱共识为准。提取时优先取论文自报亚群名,再映射到下表标准名。

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Peptidergic nociceptor | PEP; peptidergic; CGRP+ nociceptor; PEP1/PEP2 | yes | CALCA(CGRP);TAC1;TRPV1;SCN10A;NTRK1 \| Calca;Tac1;Trpv1;Scn10a;Ntrk1 |
| Non-peptidergic nociceptor | NP; non-peptidergic; NP1/NP2/NP3; IB4+ | yes | P2RX3;MRGPRD;GFRA2;LPAR3 \| P2rx3;Mrgprd;Gfra2;Lpar3 |
| Pruriceptor (itch neuron) | NP3; itch; pruritogen-sensing | yes | MRGPRA3;IL31RA;SST;NPPB;HTR1F \| Mrgpra3;Il31ra;Sst;Nppb;Htr1f |
| C-LTMR | C-low-threshold mechanoreceptor; tyrosine hydroxylase LTMR; TH+ C-fiber | yes | TH;FAM19A4;SLC17A8(VGLUT3);ZNF521 \| Th;Fam19a4;Slc17a8;Zfp521 |
| Aβ/Aδ LTMR | LTMR; low-threshold mechanoreceptor; Aβ-LTMR; Aδ-LTMR; RA/SA-LTMR | yes | NEFH;NTRK2;NTRK3;CALB1;SLC17A7 \| Nefh;Ntrk2;Ntrk3;Calb1;Slc17a7 |
| Proprioceptor | proprioceptive neuron; PV+ neuron; muscle spindle afferent | yes | PVALB;RUNX3;NTRK3;ETV1;WHRN \| Pvalb;Runx3;Ntrk3;Etv1;Whrn |
| Cold thermoreceptor | cold-sensing neuron; TRPM8+ | yes | TRPM8;FOXP2 \| Trpm8;Foxp2 |
| C-fiber unmyelinated nociceptor (generic) | C-nociceptor; unmyelinated nociceptor (未细分肽能/非肽能时用) | yes | SCN10A;SCN11A;TRPA1 \| Scn10a;Scn11a;Trpa1 |
| Nodose/vagal sensory neuron | jugular-nodose neuron; vagal afferent; visceral sensory | yes | PHOX2B;P2RX2;PIEZO2;TRPV1;CALCA \| Phox2b;P2rx2;Piezo2;Trpv1;Calca |
| Visceral/silent nociceptor | mechanically-insensitive afferent; silent nociceptor | yes | TRPV1;TAC1;SST;CHRNA3 \| Trpv1;Tac1;Sst;Chrna3 |
| Olfactory sensory neuron | OSN; olfactory receptor neuron; ORN | context | OMP;GNAL;CNGA2;ANO2 \| Omp;Gnal;Cnga2;Ano2 |

> **context 说明（发现#3）**：嗅感觉神经元(OSN)是明确的感觉神经元，但嗅觉系统在 PNS/CNS 归属上学界有争议（轴突直投嗅球/中枢）。标 `context` = 提取时 `is_pns_cell` 填 `NA` 交人工裁决，不默认 true。

> 注：DRG 感觉神经元**泛 marker**(判断"是否神经元"用)：`RBFOX3(NeuN);TUBB3;SNAP25;UCHL1(PGP9.5);ISL1;PRPH;SLC17A6` \| `Rbfox3;Tubb3;Snap25;Uchl1;Isl1;Prph;Slc17a6`。

---

### 1.3 自主神经元(autonomic_neuron)

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Sympathetic postganglionic neuron | sympathetic neuron; noradrenergic neuron; SCG neuron | yes | TH;DBH;CHGA;NPY;PHOX2B;PRPH;SLC18A2 \| Th;Dbh;Chga;Npy;Phox2b;Prph;Slc18a2 |
| Parasympathetic postganglionic neuron | parasympathetic neuron; cholinergic autonomic neuron | yes | CHAT;SLC18A3;PHOX2B;RET;NOS1 \| Chat;Slc18a3;Phox2b;Ret;Nos1 |
| Sympathetic cholinergic neuron | sudomotor neuron; cholinergic sympathetic | yes | CHAT;TH(low);VIP \| Chat;Th;Vip |
| Chromaffin cell | adrenal chromaffin; SIF cell (small intensely fluorescent) | context | TH;DBH;PNMT;CHGA;CHGB \| Th;Dbh;Pnmt;Chga;Chgb |

> **Chromaffin cell 标 context（发现#7）**：嗜铬细胞为神经嵴源、与交感神经元同源，但**功能上是内分泌细胞**（分泌肾上腺素），是否算"外周神经细胞"有争议。提取时 `is_pns_cell` 填 `NA` 交人工裁决，不默认 true。

---

### 1.4 肠神经元(enteric_neuron)

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Enteric neuron (generic) | ENS neuron; myenteric/submucosal neuron; ENC | yes | PHOX2B;RET;ELAVL4(HuD);TUBB3;UCHL1;SNAP25 \| Phox2b;Ret;Elavl4;Tubb3;Uchl1;Snap25 |
| Excitatory motor neuron (ENS) | cholinergic enteric motor neuron; ChAT+ ENS | yes | CHAT;TAC1;SLC18A3 \| Chat;Tac1;Slc18a3 |
| Inhibitory motor neuron (ENS) | nitrergic neuron; NOS+ ENS neuron | yes | NOS1;VIP;GAL \| Nos1;Vip;Gal |
| Intrinsic primary afferent neuron (IPAN) | sensory enteric neuron; AH neuron | yes | CALB1;NMU;NEFM \| Calb1;Nmu;Nefm |
| Interneuron (ENS) | enteric interneuron; serotonergic/descending interneuron | yes | SLC17A6;NOS1;SST;5HT(TPH2) \| Slc17a6;Nos1;Sst;Tph2 |

> 肠神经元提取时若论文只给 ENC1–ENC12 等编号亚群,在 `cell_type` 写论文编号 + `(uncontrolled)`,并在 `notes` 记原始 marker。

---

### 1.5 施万细胞(schwann_glia)

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Myelinating Schwann cell | mSC; myelinating SC; mySC | yes | MPZ;MBP;PMP22;PRX;MAG;EGR2(KROX20) \| Mpz;Mbp;Pmp22;Prx;Mag;Egr2 |
| Non-myelinating Schwann cell (Remak) | Remak cell; nmSC; non-myelinating SC | yes | NCAM1;L1CAM;SCN7A;GFRA3 \| Ncam1;L1cam;Scn7a;Gfra3 |
| Repair Schwann cell | Büngner cell; repair SC; dedifferentiated SC; reactive SC | yes | NGFR(p75);GAP43;SHH;OLIG1;BDNF;ATF3 \| Ngfr;Gap43;Shh;Olig1;Bdnf;Atf3 |
| Schwann cell precursor | SCP; immature Schwann cell | yes | SOX10;FOXD3;CDH19;PLP1;DHH \| Sox10;Foxd3;Cdh19;Plp1;Dhh |
| Perisynaptic/terminal Schwann cell | teloglia; terminal SC; PSC (NMJ) | yes | S100B;SOX10;GFAP;CDH19 \| S100b;Sox10;Gfap;Cdh19 |
| Schwann cell (generic/unspecified) | SC; Schwann cell | yes | SOX10;S100B;PLP1;MPZ \| Sox10;S100b;Plp1;Mpz |

> 施万细胞**泛 marker**(分型不明时):`SOX10;S100B;PLP1` \| `Sox10;S100b;Plp1`。

---

### 1.6 卫星胶质细胞(satellite_glia, SGC)

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Satellite glial cell | SGC; satellite glia; perineuronal glia | yes | FABP7(BLBP);KCNJ10(Kir4.1);GLUL(GS);CDH19;APOE;GJA1(Cx43) \| Fabp7;Kcnj10;Glul;Cdh19;Apoe;Gja1 |

> SGC 与施万细胞共享 `SOX10;S100B`,区分关键看 `FABP7/KCNJ10/GLUL`(SGC 高)且**位于神经节内环绕神经元胞体**。

---

### 1.7 肠胶质细胞(enteric_glia)

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Enteric glial cell | EGC; enteric glia; ENS glia | yes | SOX10;S100B;GFAP;PLP1;FABP7;ERBB3 \| Sox10;S100b;Gfap;Plp1;Fabp7;Erbb3 |

> EGC 与中枢星形胶质区别：EGC 为 `SOX10+`(神经嵴源)，星形胶质 `SOX10−/AQP4+`。

---

### 1.8 微环境/基质·免疫·血管(microenvironment)

| 标准名 | 同义词/缩写 | is_pns_cell | 关键 marker(人类 \| 鼠) |
|---|---|---|---|
| Fibroblast | endoneurial/perineurial/epineurial fibroblast; stromal cell | yes(context) | PDGFRA;COL1A1;COL3A1;DCN;LUM \| Pdgfra;Col1a1;Col3a1;Dcn;Lum |
| Perineurial cell | perineurial fibroblast | yes | SLC2A1(GLUT1);CLDN1;ITGB4 \| Slc2a1;Cldn1;Itgb4 |
| Endoneurial fibroblast | endoneurial cell | yes | PDGFRA;SOX9;OSR2 \| Pdgfra;Sox9;Osr2 |
| Endothelial cell | EC; vascular endothelium | yes(context) | PECAM1(CD31);CDH5(VE-cad);CLDN5;FLT1 \| Pecam1;Cdh5;Cldn5;Flt1 |
| Pericyte | mural cell; perivascular | yes(context) | PDGFRB;RGS5;KCNJ8;ACTA2(low);NOTCH3 \| Pdgfrb;Rgs5;Kcnj8;Acta2;Notch3 |
| Vascular smooth muscle cell | vSMC; mural | yes(context) | ACTA2;MYH11;TAGLN;CNN1 \| Acta2;Myh11;Tagln;Cnn1 |
| Macrophage | endoneurial macrophage; resident Mφ; nerve-associated macrophage | yes(context) | PTPRC(CD45);AIF1(IBA1);CD68;LYZ;CX3CR1;MRC1(CD206);P2RY12 \| Ptprc;Aif1;Cd68;Lyz2;Cx3cr1;Mrc1;P2ry12 |
| Monocyte | classical/non-classical monocyte | context | LYZ;CD14;FCGR3A;CCR2 \| Lyz2;Cd14;Fcgr3;Ccr2 |
| Dendritic cell | DC; cDC; pDC | context | ITGAX(CD11c);FLT3;CLEC9A;IRF8 \| Itgax;Flt3;Clec9a;Irf8 |
| T cell | T lymphocyte; CD4/CD8 T | context | CD3D;CD3E;CD8A;CD4;IL7R \| Cd3d;Cd3e;Cd8a;Cd4;Il7r |
| B cell | B lymphocyte | context | CD79A;MS4A1(CD20);CD19 \| Cd79a;Ms4a1;Cd19 |
| NK cell | natural killer | context | NCAM1;NKG7;KLRD1;GNLY \| Ncam1;Nkg7;Klrd1 |
| Mast cell | mastocyte | context | CMA1;TPSAB1;KIT;CPA3 \| Cma1;Tpsab1;Kit;Cpa3 |
| Neutrophil | granulocyte; PMN | context | S100A8;S100A9;FCGR3B;CSF3R \| S100a8;S100a9;Csf3r;Ly6g |
| Lymphatic endothelial cell | LEC | context | PROX1;LYVE1;PDPN;FLT4 \| Prox1;Lyve1;Pdpn;Flt4 |
| Melanocyte | pigment cell (神经嵴源,可见于皮肤神经/节) | context | MLANA;PMEL;DCT;TYR;MITF \| Mlana;Pmel;Dct;Tyr;Mitf |
| Adipocyte | fat cell (epineurial/nerve-associated) | context | ADIPOQ;LEP;FABP4;PLIN1 \| Adipoq;Lep;Fabp4;Plin1 |
| Skeletal muscle cell | myocyte; myofiber (NMJ 周边污染) | context | ACTN2;MYH1;TNNT3;DES \| Actn2;Myh1;Tnnt3;Des |
| Erythrocyte | RBC; red blood cell (污染常见) | no | HBA1;HBB;ALAS2 \| Hba-a1;Hbb-bs;Alas2 |

> `context` 行：这些细胞本身非神经嵴/非外周特异，是否纳入取决于其**采样自外周神经/神经节组织**。提取时照实记录其在外周样本中的存在,不要因"非神经"而丢弃。

---

### 1.9 反向排除参考(is_pns_cell = no,出现即提示可能含中枢成分)

| 术语 | 提示 | 关键 marker(人类 \| 鼠) |
|---|---|---|
| Astrocyte | 中枢星形胶质,非外周 | GFAP;AQP4;SLC1A3;ALDH1L1(SOX10−) \| Gfap;Aqp4;Slc1a3;Aldh1l1 |
| Oligodendrocyte | 中枢髓鞘,非外周 | MOG;MOBP;OLIG2;PLP1(+CNS context) \| Mog;Mobp;Olig2 |
| OPC | 中枢少突前体 | PDGFRA;CSPG4;OLIG1 \| Pdgfra;Cspg4;Olig1 |
| Microglia | 中枢固有免疫 | P2RY12;TMEM119;CX3CR1;SALL1 \| P2ry12;Tmem119;Cx3cr1;Sall1 |
| Ependymal cell | 脑室管膜 | FOXJ1;PIFO;CCDC153 \| Foxj1;Pifo;Ccdc153 |
| CNS excitatory/inhibitory neuron | 脑/脊髓神经元 | SLC17A7;GAD1;GAD2;RBFOX3(+CNS region) \| Slc17a7;Gad1;Gad2 |

> 判定：若样本核心是 DRG/TG/外周神经而**附带少量上述中枢细胞**(如 DRG 与脊髓同篇),按边界规则**只取外周部分**,中枢细胞类型不入 cell_types,在 papers.notes 记"含脊髓中枢成分,已剔除"。

---

## 第 2 部分 · 组织/解剖部位词表(Anatomy / Tissue)

写入 `datasets.tissue`。`is_pns` 用于纳入判断。

| 标准名 | 同义词/缩写 | is_pns | 类别 |
|---|---|---|---|
| Dorsal root ganglion | DRG; spinal ganglion; dorsal root ganglia | yes | 感觉神经节 |
| Trigeminal ganglion | TG; Gasserian ganglion; semilunar ganglion | yes | 感觉神经节(头面) |
| Nodose ganglion | nodose; inferior vagal ganglion | yes | 内脏感觉节 |
| Jugular ganglion | superior vagal ganglion | yes | 内脏感觉节 |
| Nodose-jugular complex | vagal sensory ganglion; jugular-nodose | yes | 内脏感觉节 |
| Geniculate ganglion | facial sensory ganglion | yes | 感觉神经节(味觉) |
| Vestibular/spiral ganglion | cochlear ganglion; spiral ganglion neuron (SGN) | yes | 特殊感觉节(听觉/前庭) |
| Petrosal ganglion | glossopharyngeal sensory ganglion | yes | 内脏感觉节 |
| Superior cervical ganglion | SCG | yes | 交感神经节 |
| Stellate ganglion | cervicothoracic ganglion | yes | 交感神经节 |
| Sympathetic ganglion (generic) | paravertebral/prevertebral ganglion; sympathetic chain | yes | 交感神经节 |
| Celiac/mesenteric ganglion | prevertebral ganglion | yes | 交感神经节 |
| Dorsal root ganglion + sciatic | DRG and nerve | yes | 复合(分别提取) |
| Sciatic nerve | nervus ischiadicus | yes | 外周神经干 |
| Peripheral nerve trunk | peripheral nerve; nerve; tibial/sural/vagus nerve trunk | yes | 外周神经干 |
| Vagus nerve | vagal nerve (trunk) | yes | 外周神经干(自主) |
| Optic nerve | — | no(CNS tract) | 排除(中枢) |
| Enteric nervous system | ENS; gut neurons | yes | 肠神经 |
| Myenteric plexus | Auerbach plexus; myenteric | yes | 肠神经(肌间丛) |
| Submucosal plexus | Meissner plexus; submucosal | yes | 肠神经(黏膜下丛) |
| Gut muscularis (with ENS) | intestinal muscularis externa | yes | 肠神经载体组织 |
| Skin (with innervation) | cutaneous innervation; skin nerve; hairy/glabrous skin | yes(context) | 皮肤神经支配 |
| Cornea (innervation) | corneal nerve | yes(context) | 角膜神经支配 |
| Tooth pulp | dental pulp innervation | yes(context) | 牙髓神经支配 |
| Visceral nerve / organ innervation | cardiac/bladder/pancreatic/airway innervation | yes(context) | 内脏神经 |
| Neuromuscular junction | NMJ; motor endplate | yes(context) | 外周突触(施万终末) |
| Adrenal medulla | suprarenal medulla | yes | 嗜铬/SIF(神经嵴源) |
| Carotid body | glomus | yes(context) | 外周化学感受器 |
| Spinal cord | spinal | no | 排除(中枢) |
| Brain / brainstem / cortex | — | no | 排除(中枢) |
| Retina | — | no | 排除(中枢) |

> `context` 组织(皮肤/角膜/内脏/NMJ)：仅当论文**明确分析了其中的神经/胶质细胞**时纳入;若只测上皮/实质细胞则按排除标准剔除,在卡片 notes 注明。

---

## 第 3 部分 · 测序/建库平台词表(Sequencing / Library Platform)

写入 `processing.platform`。`vendor` 列供卡片展示。**snRNA 还需在 `processing.assay` 记 `snRNA-seq` vs `scRNA-seq`**。

| 标准名 | 同义词/缩写 | vendor | 类型 |
|---|---|---|---|
| 10x Chromium 3' v2 | 10X 3' v2; Chromium GEM v2 | 10x Genomics | 液滴 droplet |
| 10x Chromium 3' v3 | 10X 3' v3; Chromium GEM v3/v3.1 | 10x Genomics | 液滴 droplet |
| 10x Chromium 3' (version NA) | 10X 3'; Chromium 3' (未标版本) | 10x Genomics | 液滴 droplet |
| 10x Chromium 5' | 10X 5'; VDJ 5' | 10x Genomics | 液滴 droplet |
| 10x Multiome (RNA+ATAC) | 10X Multiome; ATAC+GEX | 10x Genomics | 液滴(多组学) |
| 10x Flex (Fixed RNA) | Fixed RNA Profiling; FRP | 10x Genomics | 探针固定 |
| Smart-seq2 | SS2 | (学术协议;板式) | 全长 plate full-length |
| Smart-seq3 | SS3 | (学术协议) | 全长 plate full-length |
| Drop-seq | dropseq | (学术协议;Macosko) | 液滴 droplet |
| inDrop | indrops; 1CellBio | 1CellBio/学术 | 液滴 droplet |
| BD Rhapsody | Rhapsody; BD WTA | BD Biosciences | 微孔 microwell |
| Parse Biosciences (split-seq) | SPLiT-seq; Parse WT; Evercode | Parse Biosciences | 组合标签 combinatorial |
| sci-RNA-seq / sci-RNA-seq3 | sci-RNA; combinatorial indexing | (学术;Shendure) | 组合标签 combinatorial |
| Microwell-seq | — | (学术;HCL/Guo lab) | 微孔 microwell |
| Seq-Well | Seq-Well S^3 | (学术;Shalek) | 微孔 microwell |
| Fluidigm C1 | C1 | Fluidigm/Standard BioTools | 微流控 IFC |
| MGI/BGI DNBelab C4 | DNBelab C4; C4 | MGI/BGI | 液滴 droplet |
| MGI DNBelab C-TaiM | C-TaiM 4 | MGI/BGI | 高通量液滴 |
| Singleron GEXSCOPE | Singleron; sCelLiVE | Singleron | 微孔/液滴 |
| HIVE scRNA-seq | Honeycomb HIVE | Honeycomb Bio | 微孔捕获 |
| CEL-seq / CEL-seq2 | celseq2 | (学术;MARS-seq 同族) | 板式 3' |
| MARS-seq | MARS-seq2 | (学术;Amit) | 板式 3' |
| snRNA-seq (generic) | single-nucleus RNA-seq; snRNAseq; sNuc-seq; DroNc-seq | (方法,非厂商;常配 10x) | 单核 |
| DroNc-seq | — | (学术;snRNA 液滴) | 单核 droplet |

> 提取规则：
> - 平台与"单核 vs 单细胞"**分两个字段**。例:`platform = 10x Chromium 3' v3`,`assay = snRNA-seq`。
> - 若仅写"10x Chromium"未标版本/端别 → `10x Chromium 3' (version NA)`。
> - 若仅写"single-cell RNA-seq"无任何平台信息 → `platform = NA`,`assay = scRNA-seq`。

---

## 第 4 部分 · 下游分析工具词表(Analysis Tools,按功能分类)

写入 `processing.analysis_tools`(多值分号分隔)。`category` 列写入 `processing` 备注或用于卡片分组。**只记论文实际用到的工具**,缺失填 `NA`。

| category 分类 | 标准名 | 同义词/缩写 |
|---|---|---|
| framework 框架 | Seurat | Seurat v3/v4/v5 |
| framework 框架 | Scanpy | scanpy; AnnData pipeline |
| framework 框架 | Monocle | Monocle(作框架时) |
| framework 框架 | Bioconductor/SingleCellExperiment | SCE; scater; scran(框架) |
| framework 框架 | Cell Ranger | CellRanger; 10x pipeline |
| framework 框架 | STARsolo | STAR solo |
| framework 框架 | salmon alevin / alevin-fry | alevin; alevin-fry |
| framework 框架 | kallisto\|bustools | kb-python; kallisto bustools |
| QC/doublet 质控去双细胞 | EmptyDrops | emptyDrops (DropletUtils) |
| QC/doublet 质控去双细胞 | Scrublet | scrublet |
| QC/doublet 质控去双细胞 | DoubletFinder | doubletfinder |
| QC/doublet 质控去双细胞 | scDblFinder | scdblfinder |
| QC/doublet 质控去双细胞 | DoubletDetection | doubletdetection |
| QC/doublet 质控去双细胞 | SoupX | soupx (ambient RNA) |
| QC/doublet 质控去双细胞 | CellBender | cellbender (remove-background) |
| QC/doublet 质控去双细胞 | DecontX | decontX (celda) |
| normalization 标准化 | LogNormalize | log-normalization; NormalizeData |
| normalization 标准化 | SCTransform | SCT; sctransform |
| normalization 标准化 | scran | scran normalization; deconvolution |
| normalization 标准化 | TPM/CPM | CPM; counts per million |
| batch 批次整合 | Harmony | harmony |
| batch 批次整合 | scVI | scvi-tools; scVI |
| batch 批次整合 | scANVI | scanvi |
| batch 批次整合 | Seurat CCA | CCA; anchors; IntegrateData |
| batch 批次整合 | Seurat RPCA | rpca |
| batch 批次整合 | fastMNN | mnnCorrect; batchelor |
| batch 批次整合 | BBKNN | bbknn |
| batch 批次整合 | Scanorama | scanorama |
| batch 批次整合 | LIGER | rliger; iNMF |
| clustering 聚类 | Louvain | louvain |
| clustering 聚类 | Leiden | leiden |
| clustering 聚类 | k-means/hierarchical | kmeans; hclust |
| annotation 注释 | manual marker-based | manual annotation; marker-based; canonical markers |
| annotation 注释 | SingleR | singler |
| annotation 注释 | CellTypist | celltypist |
| annotation 注释 | Azimuth | azimuth (reference mapping) |
| annotation 注释 | scmap | scmap-cell/cluster |
| annotation 注释 | scPred | scpred |
| annotation 注释 | Garnett | garnett |
| trajectory 轨迹/拟时 | Monocle2 | monocle 2 |
| trajectory 轨迹/拟时 | Monocle3 | monocle 3 |
| trajectory 轨迹/拟时 | Slingshot | slingshot |
| trajectory 轨迹/拟时 | PAGA | paga (partition graph abstraction) |
| trajectory 轨迹/拟时 | scVelo | scvelo; RNA velocity |
| trajectory 轨迹/拟时 | velocyto | velocyto.py/R |
| trajectory 轨迹/拟时 | CellRank | cellrank |
| trajectory 轨迹/拟时 | Palantir | palantir |
| trajectory 轨迹/拟时 | Wishbone/DPT | dpt; diffusion pseudotime |
| communication 细胞通讯 | CellChat | cellchat |
| communication 细胞通讯 | CellPhoneDB | cellphonedb |
| communication 细胞通讯 | NicheNet | nichenet; nichenetr |
| communication 细胞通讯 | LIANA | liana (consensus) |
| communication 细胞通讯 | iTALK/Connectome | italk; connectome |
| communication 细胞通讯 | Squidpy (ligrec) | squidpy |
| enrichment 富集/通路 | clusterProfiler (GO) | GO enrichment; enrichGO |
| enrichment 富集/通路 | clusterProfiler (KEGG) | KEGG; enrichKEGG |
| enrichment 富集/通路 | GSEA | gsea; fgsea; GSEAPreranked |
| enrichment 富集/通路 | AUCell | aucell (gene-set activity) |
| enrichment 富集/通路 | Metascape | metascape |
| enrichment 富集/通路 | gProfiler | g:Profiler; gprofiler2 |
| enrichment 富集/通路 | Enrichr | enrichr |
| DE 差异表达 | Wilcoxon (FindMarkers) | wilcoxon rank-sum; FindAllMarkers |
| DE 差异表达 | MAST | mast |
| DE 差异表达 | DESeq2/edgeR (pseudobulk) | pseudobulk DE |
| regulon 调控网络 | SCENIC/pySCENIC | scenic; regulon; GRNBoost2 |
| copy number 拷贝数 | inferCNV | infercnv |
| copy number 拷贝数 | CopyKAT | copykat |

> 提取规则：
> - 工具名按本表**标准名**写,版本号(如 Seurat v4)可保留在标准名内或 notes。
> - 一篇文章常跨多类工具,全部记入 `analysis_tools`,分号分隔。
> - 论文未交代分析流程 → `analysis_tools = NA`。
> - 未收录的新工具 → 原名 + `(uncontrolled)`,交主人抽查补录。
> - **落库映射**：各类工具按功能拆进 `processing` 专用列（见 05 §0）。其中**富集/通路类**(clusterProfiler/GSEA/Metascape/AUCell/gProfiler/Enrichr) → `processing.enrichment`，记「类型(工具)」如 `GO(Metascape)`，多值用 `;`、括号内并列用 `/`；没做 `none`、没提 `NA`。

---

## 附录 · DeepSeek 提取 mini few-shot(用法示例)

输入片段(人类 DRG):
> "We profiled human dorsal root ganglia using 10x Chromium 3' v3. Doublets were removed with Scrublet, batches integrated by Harmony, clusters identified by Leiden, and cell types annotated manually using canonical markers. We identified peptidergic nociceptors (CALCA+/TAC1+) and satellite glial cells (FABP7+)."

提取结果:
- `tissue = Dorsal root ganglion`
- `platform = 10x Chromium 3' v3`;`assay = scRNA-seq`
- `cell_types`: `Peptidergic nociceptor (markers: CALCA;TAC1)` | category `sensory_neuron`;`Satellite glial cell (markers: FABP7)` | category `satellite_glia`
- `analysis_tools = Scrublet;Harmony;Leiden;manual marker-based`
- marker 大小写:物种=Human → 全大写,已符合。

输入片段(小鼠坐骨神经损伤):
> "Mouse sciatic nerve was dissociated and processed by Drop-seq. We observed repair Schwann cells expressing Ngfr and Gap43."

提取结果:
- `tissue = Sciatic nerve`
- `platform = Drop-seq`;`assay = scRNA-seq`
- `cell_types`: `Repair Schwann cell (markers: Ngfr;Gap43)` | category `schwann_glia`(物种=Mouse → 首字母大写,已符合)
- 其余流程未提 → `analysis_tools = NA`
