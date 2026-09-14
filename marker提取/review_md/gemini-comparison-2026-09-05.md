# Gemini 与正式 Marker 表核对

日期：2026-09-05

## 范围与结论

上传 JSON 只有 10.1038/s41586-020-2922-4 一篇，不是五篇合并结果。全文数据比对已完成；原图复查针对主要差异及疑点，不代表全部 112 条均已逐条批准。正式工作簿未修改。

| 截图顺序 | DOI | 我方正式记录行数 | Gemini 正式记录行数 |
|---|---|---:|---:|
| 1 | DOI_10.1038_s41586-020-2922-4 | 87 | 112 |
| 2 | DOI_10.1016_j.healun.2026.02.1666 | 3 | 未提供 |
| 3 | DOI_10.1016_j.jcf.2025.01.016 | 2 | 未提供 |
| 4 | DOI_10.1038_s44318-024-00328-6 | 34 | 未提供 |
| 5 | DOI_10.1101_2024.10.23.619925 | 55 | 未提供 |

## 第一篇机械比对口径

以细胞类型对照映射 + 原文基因符号（仅统一大小写）+ 物种 + 极性比较。描述性 subtype 暂按同一作者细胞群归并；保留每条原始记录供复查。未把宽泛细胞群拆成子群，未把 unknown 极性当作 positive，未自动修正 BPIFBP1。C20orf85 以 Gemini 的 gene_original 对齐，不视为新增 CFAP99。

- Gemini：112 行，112 个比较键；我方：87 行，87 个比较键。
- 相同细胞—基因—物种—极性：46 个。
- Gemini 单方：66 个；我方单方：41 个。单方不等于漏提或正确，应按下述证据复查。
- Gemini 58 个亚群中实际有正式记录的为 54 个，未覆盖：Cap-i2, Club, Mast Ba 2, Neu。另有 4 个组织区室标签。coverage_summary 声称全覆盖且缺失列表为空，与数据矛盾。

## 已确认的关键问题

| 对象 | 发现 | 原始证据与处理建议 |
|---|---|---|
| Gemini：AT2-s—NNMT | 配对错误 | Fig.1c 将 NNMT 列在 AT2 侧；Extended Data Fig.3i 将其列为 AT2 selective。不能按当前 AT2-s 配对入表。 |
| Gemini：ASM—DES | 所引图不支持 | Fig.1e 没有 DES 标签。该 source_context 不准确，需另找本文证据，否则不入表。 |
| Gemini：Club—CTSE | 可解决的未决项 | Extended Data Fig.5a 第一行清楚标为 CTSE，对应 cluster 1 Club；不是 GTSE1。 |
| Gemini：PGC | 特异性描述不准确且漏子群 | Fig.1c 位于通用 AT2 marker 区；Extended Data Fig.5a 的 14/15 均有信号，不能仅描述为 canonical AT2 特异。 |
| Gemini：AT2-s—SFTPC | 漏提；我方已有 | Fig.1d 明确标注 AT2-signalling 为 SFTPC+ WIF1−。 |
| Gemini：SFTPD | 两边均未收录该图中关系 | Fig.1c 通用 AT2 marker 包含 SFTPD。Gemini 所引 Fig.1c 的 source_context 却写 MUC1/SFTPA1；后两者在 Extended Data Fig.3i 有支持，应改定位。 |
| Gemini：MYRF、TBX5 | 用途需单独判断 | Extended Data Fig.5c/d 图注明确区分 AGER/COX4I2 marker 与 MYRF/TBX5 transcription factor。不能单凭选择性表达自动等同注释 marker。 |
| 我方：AlvF—SLC7A10（human） | 物种错误 | Extended Data Fig.4b 标为 Mouse AlvF，图中原始写法 Slc7a10；不能支持当前 human 记录。 |
| 我方：ASM/FibM—COX4I2 positive | 待澄清图文含义（本次更正） | Extended Data Fig.4f/g图注明确称COX4I2/ACTG2为fibromyocyte和airway smooth muscle markers，同时f展示ASPN+ COX4I2−的MyoF，h/j突出Peri阳性。此前直接判定两条阳性记录错误过强，应核查图文所指细胞范围后再裁决。 |
| 我方：Ser—BPIFBP1；Gemini：BPIFB1 | 原文内部拼写不一致 | Extended Data Fig.12g 图内为 BPIFB1，图注写 BPIFBP1，正文也为 BPIFB1。应保留图注原文并记录拼写修正依据，不能当两个独立基因。 |
| Gemini：PLVAP 仅候选 | 分类过窄 | 虽正文有功能讨论，Extended Data Fig.3j 明确将 PLVAP 放入 endothelial markers / Bro1/2 图；我方有宽泛 bronchial endothelial 记录，应结合图复核并补充定位。 |
| Gemini：页码字段 | 多处错位 | 本地 PDF 共37页。Extended Data Fig.3 位于17–18页，Fig.4 在19–20页，Fig.5 在21页，Fig.12 在31页；不是 JSON 中的9/10/11等页。不能把扩展图虚拟递增为印刷页627/628/629。 |

## 有原图支持的补充例子

下列例子在我方相同配对中未匹配，并在 Extended Data Fig.5a（PDF第21页）可读：ASM—KCNA5；Art—DKK2；Vein—CPE；Meso—KRT19；Ser—PRR4；Ion—ASCL3；Plasma—MZB1；MP—LPL；pDC—SCT；mDC2—CD1E。VSM 原文为 C2orf40，Peri 原文为 FAM105A；别名 ECRG4/OTULINL 本次未独立查证，保留原文。

## Gemini 全部正式记录对照

“已匹配”只表示表间一致，不代表两边结论已被独立验证为正确。

| 序号 | 细胞 | 原文基因 | Gemini 标准化基因 | 极性 | 对照 | Gemini 定位 |
|---:|---|---|---|---|---|---|
| 1 | Epithelial | EPCAM | EPCAM | positive | 已匹配 | Main Text, Results; Extended Data Fig. 1b |
| 2 | Endothelial | CLDN5 | CLDN5 | positive | 已匹配 | Methods; Extended Data Fig. 1b |
| 3 | Stromal | COL1A2 | COL1A2 | positive | 已匹配 | Methods; Extended Data Fig. 1b |
| 4 | Immune | PTPRC | PTPRC | positive | 已匹配 | Methods; Extended Data Fig. 1b |
| 5 | AT2 | SFTPC | SFTPC | positive | 已匹配 | Fig. 1c, d |
| 6 | AT2 | SFTPB | SFTPB | positive | Gemini 单方，待复核 | Fig. 1c |
| 7 | AT2 | SFTPA1 | SFTPA1 | positive | 已匹配 | Fig. 1c |
| 8 | AT2 | MUC1 | MUC1 | positive | 已匹配 | Fig. 1c |
| 9 | AT2 | WIF1 | WIF1 | positive | 已匹配 | Fig. 1c, d |
| 10 | AT2 | HHIP | HHIP | positive | 已匹配 | Fig. 1c; Extended Data Fig. 3i |
| 11 | AT2 | CA2 | CA2 | positive | 已匹配 | Fig. 1c; Extended Data Fig. 3i |
| 12 | AT2 | ETV5 | ETV5 | positive | 已匹配 | Fig. 1c; Extended Data Fig. 3i |
| 13 | AT2 | PGC | PGC | positive | Gemini 单方，待复核 | Fig. 1c; Extended Data Fig. 5a |
| 14 | AT2-s | WIF1 | WIF1 | negative | 已匹配 | Fig. 1d |
| 15 | AT2-s | WNT5A | WNT5A | positive | 已匹配 | Fig. 1c; Extended Data Fig. 3i |
| 16 | AT2-s | LRP5 | LRP5 | positive | 已匹配 | Fig. 1c; Extended Data Fig. 3i |
| 17 | AT2-s | CP | CP | positive | Gemini 单方，待复核 | Fig. 1c; Extended Data Fig. 3i |
| 18 | AT2-s | NNMT | NNMT | positive | Gemini 单方，待复核 | Fig. 1c |
| 19 | AT2-s | TCF7L2 | TCF7L2 | positive | 已匹配 | Fig. 1c; Extended Data Fig. 3i |
| 20 | AT1 | AGER | AGER | positive | 已匹配 | Extended Data Fig. 5a, c |
| 21 | AT1 | MYRF | MYRF | positive | Gemini 单方，待复核 | Main Text, Results; Extended Data Fig. 5c |
| 22 | AlvF | GPC3 | GPC3 | positive | 已匹配 | Fig. 1e, f; Extended Data Fig. 4a |
| 23 | AlvF | FGFR4 | FGFR4 | positive | 已匹配 | Fig. 1e; Extended Data Fig. 5a |
| 24 | AlvF | SPINT2 | SPINT2 | positive | 已匹配 | Fig. 1e |
| 25 | AdvF | SERPINF1 | SERPINF1 | positive | 已匹配 | Fig. 1e, f; Extended Data Fig. 4c |
| 26 | AdvF | PI16 | PI16 | positive | 已匹配 | Fig. 1e; Extended Data Fig. 5a |
| 27 | AdvF | SFRP2 | SFRP2 | positive | 已匹配 | Fig. 1e; Extended Data Fig. 4e |
| 28 | LipF | APOE | APOE | positive | 已匹配 | Extended Data Fig. 4i; Fig. 1e |
| 29 | LipF | PLIN2 | PLIN2 | positive | Gemini 单方，待复核 | Fig. 1e; Extended Data Fig. 12g |
| 30 | LipF | PI15 | PI15 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 31 | MyoF | ACTA2 | ACTA2 | positive | 已匹配 | Main Text, Results; Fig. 1e |
| 32 | MyoF | ASPN | ASPN | positive | 已匹配 | Extended Data Fig. 4f; Fig. 1e |
| 33 | MyoF | FGF18 | FGF18 | positive | 已匹配 | Main Text, Results; Extended Data Fig. 5a |
| 34 | FibM | MYH11 | MYH11 | positive | Gemini 单方，待复核 | Main Text, Results; Fig. 1e |
| 35 | FibM | CNN1 | CNN1 | positive | Gemini 单方，待复核 | Main Text, Results; Fig. 1e |
| 36 | FibM | TAGLN | TAGLN | positive | Gemini 单方，待复核 | Main Text, Results; Fig. 1e |
| 37 | FibM | SCX | SCX | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 38 | ASM | KCNA5 | KCNA5 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 39 | ASM | DES | DES | positive | Gemini 单方，待复核 | Fig. 1e |
| 40 | VSM | C2orf40 | ECRG4 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 41 | Peri | COX4I2 | COX4I2 | positive | 已匹配 | Extended Data Fig. 4h; Extended Data Fig. 5d |
| 42 | Peri | TBX5 | TBX5 | positive | Gemini 单方，待复核 | Extended Data Fig. 5d; Main Text p. 622 |
| 43 | Peri | FAM105A | OTULINL | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 44 | Meso | KRT19 | KRT19 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 45 | Art | GJA5 | GJA5 | positive | 已匹配 | Extended Data Fig. 3j, m |
| 46 | Art | DKK2 | DKK2 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3j |
| 47 | Vein | ACKR1 | ACKR1 | positive | 已匹配 | Extended Data Fig. 3j, l |
| 48 | Vein | CPE | CPE | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3j |
| 49 | Cap-a | S100A3 | S100A3 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3j |
| 50 | Cap-a | EDNRB | EDNRB | positive | Gemini 单方，待复核 | Extended Data Fig. 3j |
| 51 | Cap | IL7R | IL7R | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3j |
| 52 | Cap-i1 | SPRY1 | SPRY1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 53 | Bro1 | HBEGF | HBEGF | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 54 | Bro1 | ACKR1 | ACKR1 | positive | 已匹配 | Extended Data Fig. 3k |
| 55 | Bro1 | MYC | MYC | positive | Gemini 单方，待复核 | Extended Data Fig. 3k |
| 56 | Bro2 | MYC | MYC | positive | Gemini 单方，待复核 | Extended Data Fig. 3k |
| 57 | Bro2 | ACKR1 | ACKR1 | negative | Gemini 单方，待复核 | Extended Data Fig. 3k |
| 58 | Lym | CCL21 | CCL21 | positive | 已匹配 | Extended Data Fig. 3j, n; Extended Data Fig. 5a |
| 59 | Bas | KRT5 | KRT5 | positive | 已匹配 | Extended Data Fig. 3c, f |
| 60 | Bas | DLK2 | DLK2 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3b |
| 61 | Bas-px | SERPINB3 | SERPINB3 | positive | 已匹配 | Extended Data Fig. 3f |
| 62 | Bas-d | HES1 | HES1 | positive | Gemini 单方，待复核 | Main Text p. 621; Extended Data Fig. 3c |
| 63 | Bas-d | SCGB3A2 | SCGB3A2 | positive | Gemini 单方，待复核 | Main Text p. 621; Extended Data Fig. 3b |
| 64 | Bas-d | KRT7 | KRT7 | positive | Gemini 单方，待复核 | Main Text p. 621; Extended Data Fig. 3b |
| 65 | Bas-d | DAPL1 | DAPL1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 66 | Bas-p | MKI67 | MKI67 | positive | Gemini 单方，待复核 | Extended Data Fig. 3a, d |
| 67 | Bas-p | TOP2A | TOP2A | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3a |
| 68 | Cil | C20orf85 | CFAP99 | positive | 已匹配 | Extended Data Fig. 3g, h; Extended Data Fig. 5a |
| 69 | Cil | FOXJ1 | FOXJ1 | positive | Gemini 单方，待复核 | Extended Data Fig. 3g |
| 70 | Cil-px | DHRS9 | DHRS9 | positive | 已匹配 | Extended Data Fig. 3h |
| 71 | Cil-px | EPPIN | EPPIN | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3g |
| 72 | Gob | MUC5AC | MUC5AC | positive | 已匹配 | Extended Data Fig. 5a; Extended Data Fig. 11c |
| 73 | Gob | MUC5B | MUC5B | positive | 已匹配 | Extended Data Fig. 11c |
| 74 | Gob | SPDEF | SPDEF | positive | Gemini 单方，待复核 | Main Text p. 623; Extended Data Fig. 11c |
| 75 | Muc | SLC5A5 | SLC5A5 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 76 | Ser | PRR4 | PRR4 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 77 | Ser | LTF | LTF | positive | 已匹配 | Main Text p. 623; Extended Data Fig. 12g |
| 78 | Ser | LYZ | LYZ | positive | 已匹配 | Main Text p. 623; Extended Data Fig. 12g |
| 79 | Ser | BPIFB1 | BPIFB1 | positive | Gemini 单方，待复核 | Main Text p. 623; Extended Data Fig. 12g |
| 80 | Ion | ASCL3 | ASCL3 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 81 | NE | CHGA | CHGA | positive | 已匹配 | Extended Data Fig. 5a |
| 82 | NE | ASCL1 | ASCL1 | positive | 已匹配 | Fig. 4e |
| 83 | B | MS4A1 | MS4A1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 84 | Plasma | MZB1 | MZB1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 85 | CD8 M/E | GZMK | GZMK | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 86 | CD8 Na | CD8A | CD8A | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 87 | CD4 M/E | CD40LG | CD40LG | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 88 | CD4 Na | LEF1 | LEF1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 89 | NKT | KRT81 | KRT81 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 90 | NK | CHST2 | CHST2 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 91 | NK/T-p | MKI67 | MKI67 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3a |
| 92 | Mast Ba 1 | CPA3 | CPA3 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 93 | Mega | GP9 | GP9 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 94 | MP | LPL | LPL | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 95 | MP-p | MKI67 | MKI67 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a; Extended Data Fig. 3a |
| 96 | pDC | SCT | SCT | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 97 | mDC1 | LAMP3 | LAMP3 | positive | Gemini 单方，待复核 | Fig. 2b; Extended Data Fig. 5a; Extended Data Fig. 4k |
| 98 | mDC1 | CLEC9A | CLEC9A | positive | Gemini 单方，待复核 | Fig. 2b; Extended Data Fig. 4k |
| 99 | mDC2 | CD1C | CD1C | positive | Gemini 单方，待复核 | Fig. 2b; Extended Data Fig. 4k |
| 100 | mDC2 | PLD4 | PLD4 | positive | Gemini 单方，待复核 | Fig. 2b; Extended Data Fig. 4k |
| 101 | mDC2 | CD1E | CD1E | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 102 | DC IGSF21 | IGSF21 | IGSF21 | positive | 已匹配 | Fig. 2b; Extended Data Fig. 4l; Main Text p. 622 |
| 103 | DC IGSF21 | GPR34 | GPR34 | positive | 已匹配 | Fig. 2b; Extended Data Fig. 4l |
| 104 | DC EREG | EREG | EREG | positive | 已匹配 | Fig. 2b; Extended Data Fig. 4m; Main Text p. 622 |
| 105 | DC EREG | CLEC5A | CLEC5A | positive | Gemini 单方，待复核 | Fig. 2b |
| 106 | DC TREM2 | TREM2 | TREM2 | positive | 已匹配 | Fig. 2b; Extended Data Fig. 4n; Main Text p. 622 |
| 107 | DC TREM2 | CHI3L1 | CHI3L1 | positive | 已匹配 | Fig. 2b; Extended Data Fig. 4n |
| 108 | DC TREM2 | CHIT1 | CHIT1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 109 | Mono Cl. | S100A12 | S100A12 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 110 | Mono OLR1 | SLAMF1 | SLAMF1 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 111 | Mono NC | LYPD2 | LYPD2 | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |
| 112 | Mono Int. | CLEC10A | CLEC10A | positive | Gemini 单方，待复核 | Extended Data Fig. 5a |

## 我方单方记录

| 细胞 | 基因 | 物种 | 极性 | 我方定位 |
|---|---|---|---|---|
| Adventitial fibroblast | BSG | human | positive | Results §New lung cell types, p.621 |
| Adventitial fibroblast | COL1A2 | human | positive | Fig.1f legend |
| Airway smooth muscle cell | ACTG2 | human | positive | Extended Data Fig.4g legend |
| Airway smooth muscle cell | COX4I2 | human | positive | Extended Data Fig.4f legend |
| Alveolar fibroblast | BSG | human | positive | Results §New lung cell types, p.621 |
| Alveolar fibroblast | COL1A2 | human | positive | Fig.1f legend |
| Alveolar fibroblast | SLC7A10 | human | positive | Extended Data Fig.4b legend |
| AT2-signalling (AT2-s) | SFTPC | human | positive | Fig.1d legend |
| B cells | CD19 | human | positive | Methods: Flow cytometry and cell sorting; Materials and Methods, Antibodies |
| B cells | CD27 | human | unknown | Materials and Methods, Antibodies |
| B cells | MS4A1 | human | unknown | Materials and Methods, Antibodies |
| basophils, neutrophils and eosinophils | CCR3 | human | unknown | Materials and Methods, Antibodies |
| basophils, neutrophils and eosinophils | IL3RA | human | unknown | Materials and Methods, Antibodies |
| basophils, neutrophils and eosinophils | ITGB7 | human | unknown | Materials and Methods, Antibodies |
| CD4+ T cells | CD4 | human | positive | Methods: Flow cytometry and cell sorting |
| classical monocytes | CD14 | human | positive | Methods: Flow cytometry and cell sorting |
| Dendritic cell (general) | GPR183 | human | positive | Extended Data Fig.4m legend |
| endothelial or stromal | EPCAM | human | negative | Methods: Flow cytometry and cell sorting |
| endothelial or stromal | PTPRC | human | negative | Methods: Flow cytometry and cell sorting |
| epithelial | PTPRC | human | negative | Methods: Flow cytometry and cell sorting |
| Fibromyocyte | ACTG2 | human | positive | Extended Data Fig.4g legend |
| Fibromyocyte | ASPN | human | positive | Extended Data Fig.4f legend |
| Fibromyocyte | COX4I2 | human | positive | Extended Data Fig.4f legend |
| immune | EPCAM | human | negative | Methods: Flow cytometry and cell sorting |
| immune and endothelial enriched | PECAM1 | human | positive | Methods: Lung cell processing and staining |
| immune and endothelial enriched | PTPRC | human | positive | Methods: Lung cell processing and staining |
| Myofibroblast | ELN | human | positive | Fig. 4d legend |
| Myofibroblast | WIF1 | human | positive | Results §New lung cell types; Fig.1e legend |
| natural killer cells | NCAM1 | human | positive | Methods: Flow cytometry and cell sorting |
| NK cells | NCAM1 | human | unknown | Materials and Methods, Antibodies |
| pDCs, mDCs, CD16+ DCs | CD1C | human | unknown | Materials and Methods, Antibodies |
| pDCs, mDCs, CD16+ DCs | CD4 | human | unknown | Materials and Methods, Antibodies |
| pDCs, mDCs, CD16+ DCs | IL3RA | human | unknown | Materials and Methods, Antibodies |
| pDCs, mDCs, CD16+ DCs | ITGAX | human | unknown | Materials and Methods, Antibodies |
| T cells | CCR7 | human | unknown | Materials and Methods, Antibodies |
| T cells | PTPRC | human | unknown | Materials and Methods, Antibodies |
| T cells | SELL | human | unknown | Materials and Methods, Antibodies |
| Serous cells | BPIFBP1 | human | positive | Extended Data Fig. 12g legend |
| Serous cells | HP | human | positive | Extended Data Fig. 12g legend |
| Bronchial endothelial cell | PLVAP | human | positive | Results §Cell markers, regulators and interactions, p.621 |
| Bronchial vessel cells | MYC | human | positive | Extended Data Fig.3k legend |

## 细胞名称对照

| Gemini | 我方 |
|---|---|
| NE | Pulmonary neuroendocrine cell (NE) |
| AdvF | Adventitial fibroblast |
| ASM | Airway smooth muscle cell |
| AlvF | Alveolar fibroblast |
| AT1 | Alveolar type 1 (AT1) |
| AT2 | Alveolar type 2 (AT2) |
| Art | Artery endothelial cell |
| AT2-s | AT2-signalling (AT2-s)；AT2-signalling cell (AT2-s) |
| B | B cells |
| Bas | Basal cell |
| Bro1 | Bronchial vessel 1 cell (Bro1) |
| Cil | Ciliated cell |
| Mono Cl. | classical monocytes |
| Endothelial | endothelial |
| Epithelial | epithelial |
| DC EREG | EREG+ dendritic |
| FibM | Fibromyocyte |
| DC IGSF21 | IGSF21+ dendritic；IGSF21+ dendritic cell |
| Immune | immune |
| LipF | Lipofibroblast |
| Lym | Lymphatic endothelial cell |
| MyoF | Myofibroblast |
| NK | natural killer cells；NK cells |
| Peri | Pericyte |
| Bas-px | Proximal basal cell |
| Cil-px | Proximal ciliated cell |
| Stromal | stromal |
| DC TREM2 | TREM2+ dendritic；TREM2+ dendritic cell |
| Vein | Vein endothelial cell |
| Gob | Goblet cells |
| Ser | Serous cells |

## 输入与限制

- Gemini：gemini-code-1788582091593.json，schema_version=3，1篇，112条正式、4条候选、1条未决。
- 我方：表单/our_markers.xlsx 的 markers 工作表；未将历史 audit_exclusions 当作现行正式记录。
- 原文：pdf/A_molecular_cell_atlas_of_the_human_lung_from_single-cell_RNA_sequencing(科研通-ablesci.com).pdf。视觉复查PDF第2、3、17、19、21、31页，并参照已有全文Markdown。
- 不将 JSON 中 complete/high 等自报字段视为复核结论。未读取缺失的独立 Supplementary Tables 1–9 / Supplementary Figures 1–2，也未联网验证基因别名。
- 其余4篇需各自的Gemini输出后才能核对。此次仅交付比较报告，不自动合并或替换正式表。
