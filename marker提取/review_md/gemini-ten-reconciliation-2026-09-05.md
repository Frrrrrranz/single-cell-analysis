# Gemini 十篇 marker 差异裁决

日期：2026-09-05。未重新提取，仅比较 marker_Gemini 十篇现有 JSON 与总表，并针对差异查看已有正文、图与图注。

总表 1874 → 2416 条；新增 577 条，移出/合并 35 条。十篇以外基因级记录保持不变。按细胞查看表从当前总表同步生成。

## 口径

比较键为论文、作者细胞标签/真实亚型、物种、基因和极性。同义标签仅在有明确对应时归并；宽泛群与子群不自动合并。low 与 negative 分开，unknown 不强行转 positive。

正文或图注明确呈现为 marker 且有可读 gene–cell 关系的记录保留，即使 Gemini 写 differential_expression。仅列 top DEG 的 Fig.1F/4E 不因表达最高自动纳入。图中 TF activity 不当作 RNA marker；poly(A) isoform 的 P1/P2 富集不折叠为通用基因 marker。

## 逐篇统计

| 论文 | 原总表 | Gemini候选 | 一致/已覆盖 | 新增 | 上下文 | 排除 | 未决 | 更新后 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 10.1016/j.cell.2017.09.004 | 2 | 8 | 2 | 5 | 0 | 0 | 1 | 7 |
| 10.1016/j.healun.2026.02.1666 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 3 |
| 10.1016/j.jcf.2025.01.016 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 10.1038/s41586-020-2922-4 | 87 | 95 | 53 | 34 | 0 | 8 | 0 | 118 |
| 10.1038/s44318-024-00328-6 | 34 | 34 | 22 | 11 | 1 | 0 | 0 | 35 |
| 10.1101/2024.10.23.619925 | 55 | 134 | 38 | 11 | 85 | 0 | 0 | 62 |
| 10.1101/2025.01.17.633590 | 25 | 273 | 18 | 238 | 0 | 0 | 17 | 258 |
| 10.1101/2025.09.26.678707 | 48 | 185 | 38 | 130 | 9 | 2 | 6 | 178 |
| 10.1126/sciimmunol.adf9988 | 70 | 117 | 49 | 53 | 9 | 1 | 5 | 122 |
| 10.64898/2025.12.18.695268 | 53 | 132 | 25 | 95 | 6 | 1 | 5 | 136 |

## 关键裁决与限制

- 肺图谱：Slc7a10、Eln 改回小鼠；BPIFBP1 改为 BPIFB1，保留原文拼写依据。排除所引图中不存在的 KRT14、TP63、TUBB1、CCDC78、CA4、MARCO、GNLY、TPSAB1 配对。COX4I2 与 ASM/FibM 存在图注和图示冲突，未决归档。
- 胎肺免疫：large pre-B 的 BEST3 改为阳性；远端 tip SOX2 阴性被否决，保留原表共表达阳性记录。CD45RA/RO 统一至 PTPRC，同时原始抗体异构体信息留在裁决 JSON。
- 胰岛：IL4 误读改为 IL4I1。β cluster 3/5 和 δ cluster 5/6 的17条映射未获可靠一致支持，未决保留，不凭基因块顺序指定亚群。
- 膀胱：NGFR 应对应 xFB-7，而非 Schwann。xFB-0/xFB-5 的 HHIP 正负有正文/图注冲突，共同保留为未决；不强行反转其中一方。
- 总表原有、Gemini 缺席的项目按现有来源分别判断；明确分选、染色、命名证据保留。抗体面板的 unknown 保留原有粒度，未虚构阳性。
- 仅对当前候选集作裁决；没有补抓缺失的 Supplementary Tables，也没有宣称完成十篇所有可能 marker 的穷尽提取。Gemini 的抽象未决项（未给具体基因）不转成正式记录。
- 历史 audit_summary 为旧批次结果，本次不覆写。当前数以 markers、import_log 本轮记录和本报告为准。

## Gemini 全部候选裁决

| 论文 | JSON序号 | 细胞 | 亚型 | 基因 | 物种 | 极性 | 处理 | marker_id | 依据 |
|---|---:|---|---|---|---|---|---|---|---|
| 10.1016/j.cell.2017.09.004 | 1 | b-cells |  | INS | human | positive | matched | M01302 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 2 | a-cells |  | GCG | human | positive | matched | M01301 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 3 | δ-cells |  | SST | human | positive | add | M01918 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 4 | PP-cells |  | PPY | human | positive | add | M01919 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 5 | acinar |  | PRSS1 | human | positive | add | M01920 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 6 | ductal |  | PROM1 | human | positive | add | M01921 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 7 | ductal |  | EPCAM | human | positive | unresolved |  | STAR Methods 只列出 EpCAM 抗体，未建立 ductal 专属门控关系；Fig.1A ductal 对应 PROM1。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.cell.2017.09.004 | 8 | mesenchymal |  | THY1 | human | positive | add | M01922 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1A, PDF p.3 / printed p.322 |
| 10.1016/j.healun.2026.02.1666 | 1 | Myofibroblast |  | ACTA2 | human | positive | matched | M00599 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 1153; Figure 3A |
| 10.1016/j.healun.2026.02.1666 | 2 | Myofibroblast |  | TAGLN | human | positive | matched | M00600 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 1153, 1154; Figure 3A; Supplemental Figure 5A |
| 10.1016/j.healun.2026.02.1666 | 3 | endothelial cell |  | CDH5 | human | positive | matched | M00598 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 1155 |
| 10.1016/j.jcf.2025.01.016 | 1 | Neutrophil-like cells |  | FCGR3B | human | positive | matched | M00410 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 851, Results; Fig. S1F-G |
| 10.1016/j.jcf.2025.01.016 | 2 | Neutrophil-like cells |  | CSF3R | human | positive | matched | M00409 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 851, Results; Fig. S1F-G |
| 10.1038/s41586-020-2922-4 | 1 | Epithelial |  | EPCAM | human | positive | matched | M00178 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 619; Extended Data Fig. 1b |
| 10.1038/s41586-020-2922-4 | 2 | Endothelial |  | CLDN5 | human | positive | matched | M00175 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 619; Extended Data Fig. 1b |
| 10.1038/s41586-020-2922-4 | 3 | Stromal |  | COL1A2 | human | positive | matched | M00215 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 619; Extended Data Fig. 1b |
| 10.1038/s41586-020-2922-4 | 4 | Immune |  | PTPRC | human | positive | matched | M00187 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 619; Extended Data Fig. 1b |
| 10.1038/s41586-020-2922-4 | 5 | Alveolar type 2 (AT2) |  | SFTPC | human | positive | matched | M00137 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1c, d |
| 10.1038/s41586-020-2922-4 | 6 | Alveolar type 2 (AT2) |  | SFTPB | human | positive | add | M01923 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1c |
| 10.1038/s41586-020-2922-4 | 7 | Alveolar type 2 (AT2) |  | SFTPA1 | human | positive | matched | M00136 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig.3i, PDF p.17 |
| 10.1038/s41586-020-2922-4 | 8 | Alveolar type 2 (AT2) |  | SFTPD | human | positive | add | M01924 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1c |
| 10.1038/s41586-020-2922-4 | 9 | Alveolar type 2 (AT2) |  | MUC1 | human | positive | matched | M00140 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig.3i, PDF p.17 |
| 10.1038/s41586-020-2922-4 | 10 | Alveolar type 2 (AT2) |  | WIF1 | human | positive | matched | M00138 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1c, d; Extended Data Fig. 3i |
| 10.1038/s41586-020-2922-4 | 11 | Alveolar type 2 (AT2) |  | HHIP | human | positive | matched | M00135 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 12 | Alveolar type 2 (AT2) |  | CA2 | human | positive | matched | M00133 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 13 | Alveolar type 2 (AT2) |  | ETV5 | human | positive | matched | M00134 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 14 | Alveolar type 2 (AT2) |  | NNMT | human | positive | add | M01925 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 15 | Alveolar type 2 (AT2) |  | PGC | human | positive | add | M01926 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1c; Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 16 | AT2-signalling cell (AT2-s) |  | SFTPC | human | positive | matched | M00142 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1d |
| 10.1038/s41586-020-2922-4 | 17 | AT2-signalling cell (AT2-s) |  | WIF1 | human | negative | matched | M00143 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1d |
| 10.1038/s41586-020-2922-4 | 18 | AT2-signalling cell (AT2-s) |  | WNT5A | human | positive | matched | M00146 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 19 | AT2-signalling cell (AT2-s) |  | LRP5 | human | positive | matched | M00144 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 20 | AT2-signalling cell (AT2-s) |  | TCF7L2 | human | positive | matched | M00145 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 21 | AT2-signalling cell (AT2-s) |  | CP | human | positive | add | M01927 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3i; Fig. 1c |
| 10.1038/s41586-020-2922-4 | 22 | Alveolar type 1 (AT1) |  | AGER | human | positive | matched | M00132 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a, c |
| 10.1038/s41586-020-2922-4 | 23 | Basal cell |  | KRT5 | human | positive | matched | M00153 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3b, c, f |
| 10.1038/s41586-020-2922-4 | 24 | Basal cell |  | KRT14 | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 3b |
| 10.1038/s41586-020-2922-4 | 25 | Basal cell |  | TP63 | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 3b |
| 10.1038/s41586-020-2922-4 | 26 | Differentiating basal |  | DAPL1 | human | positive | add | M01928 | DAPL1 对应 Bas-d，修正 Gemini 的泛 basal 配对。 定位：Extended Data Fig.5a, PDF p.21 |
| 10.1038/s41586-020-2922-4 | 27 | Proximal basal cell |  | SERPINB3 | human | positive | matched | M00213 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3f |
| 10.1038/s41586-020-2922-4 | 28 | Differentiating basal |  | HES1 | human | positive | add | M01929 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3c |
| 10.1038/s41586-020-2922-4 | 29 | Proliferating basal |  | MKI67 | human | positive | add | M01930 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3d |
| 10.1038/s41586-020-2922-4 | 30 | Ciliated cell |  | C20orf85 | human | positive | matched | M00163 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3h |
| 10.1038/s41586-020-2922-4 | 31 | Ciliated cell |  | FOXJ1 | human | positive | add | M01931 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3g |
| 10.1038/s41586-020-2922-4 | 32 | Ciliated cell |  | TUBB1 | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 3g |
| 10.1038/s41586-020-2922-4 | 33 | Ciliated cell |  | CCDC78 | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 3g |
| 10.1038/s41586-020-2922-4 | 34 | Proximal ciliated cell |  | DHRS9 | human | positive | matched | M00214 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3g, h |
| 10.1038/s41586-020-2922-4 | 35 | Club |  | CTSE | human | positive | add | M01932 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 36 | Goblet cells |  | MUC5B | human | positive | matched | M01886 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig.11c |
| 10.1038/s41586-020-2922-4 | 37 | Serous cells |  | PRR4 | human | positive | add | M01933 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 38 | Serous cells |  | LTF | human | positive | matched | M01888 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 12g |
| 10.1038/s41586-020-2922-4 | 39 | Serous cells |  | LYZ | human | positive | matched | M01889 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 12g |
| 10.1038/s41586-020-2922-4 | 40 | Serous cells |  | BPIFB1 | human | positive | matched | M01890 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 12g |
| 10.1038/s41586-020-2922-4 | 41 | Serous cells |  | HP | human | positive | matched | M01891 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 12g |
| 10.1038/s41586-020-2922-4 | 42 | Ionocyte |  | ASCL3 | human | positive | add | M01934 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 43 | Pulmonary neuroendocrine cell (NE) |  | CHGA | human | positive | matched | M00012 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Supplementary Table 1; Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 44 | Pulmonary neuroendocrine cell (NE) |  | ASCL1 | human | positive | matched | M00011 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig.4e |
| 10.1038/s41586-020-2922-4 | 45 | Alveolar fibroblast |  | GPC3 | human | positive | matched | M00128 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1e, f; Extended Data Fig. 4a |
| 10.1038/s41586-020-2922-4 | 46 | Alveolar fibroblast |  | FGFR4 | human | positive | matched | M00127 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e; Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 47 | Alveolar fibroblast |  | SPINT2 | human | positive | matched | M00129 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 48 | Adventitial fibroblast |  | SERPINF1 | human | positive | matched | M00119 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1e, f; Extended Data Fig. 4c |
| 10.1038/s41586-020-2922-4 | 49 | Adventitial fibroblast |  | PI16 | human | positive | matched | M00118 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e; Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 50 | Adventitial fibroblast |  | SFRP2 | human | positive | matched | M00120 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e; Extended Data Fig. 4e |
| 10.1038/s41586-020-2922-4 | 51 | Lipofibroblast |  | APOE | human | positive | matched | M00190 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4i; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 52 | Lipofibroblast |  | PLIN2 | human | positive | add | M01935 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 12g; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 53 | Lipofibroblast |  | PI15 | human | positive | add | M01936 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 54 | Myofibroblast |  | ACTA2 | human | positive | matched | M00193 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 55 | Myofibroblast |  | ASPN | human | positive | matched | M00194 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4f; Main Text p. 621 |
| 10.1038/s41586-020-2922-4 | 56 | Myofibroblast |  | FGF18 | human | positive | matched | M00195 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 57 | Fibromyocyte |  | MYH11 | human | positive | add | M01937 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 58 | Fibromyocyte |  | CNN1 | human | positive | add | M01938 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 59 | Fibromyocyte |  | TAGLN | human | positive | add | M01939 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 621; Fig. 1e |
| 10.1038/s41586-020-2922-4 | 60 | Fibromyocyte |  | SCX | human | positive | add | M01940 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 61 | Airway smooth muscle cell |  | KCNA5 | human | positive | add | M01941 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 62 | Airway smooth muscle cell |  | ACTG2 | human | positive | matched | M00123 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4g |
| 10.1038/s41586-020-2922-4 | 63 | Vascular smooth muscle cell |  | C2orf40 | human | positive | add | M01942 | 原图为 C2orf40；保留原文符号，不自动应用未查证别名 ECRG4。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 64 | Pericyte |  | COX4I2 | human | positive | matched | M00212 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4h; Extended Data Fig. 5d |
| 10.1038/s41586-020-2922-4 | 65 | Pericyte |  | FAM105A | human | positive | add | M01943 | 原图为 FAM105A；保留原文符号，不自动应用未查证别名 OTULINL。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 66 | Mesothelial |  | KRT19 | human | positive | add | M01944 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 67 | Artery endothelial cell |  | GJA5 | human | positive | matched | M00139 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3m |
| 10.1038/s41586-020-2922-4 | 68 | Artery endothelial cell |  | DKK2 | human | positive | add | M01945 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a; Extended Data Fig. 3j |
| 10.1038/s41586-020-2922-4 | 69 | Vein endothelial cell |  | ACKR1 | human | positive | matched | M00226 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3l |
| 10.1038/s41586-020-2922-4 | 70 | Vein endothelial cell |  | CPE | human | positive | add | M01946 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a; Extended Data Fig. 3j |
| 10.1038/s41586-020-2922-4 | 71 | General capillary cell |  | CA4 | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 5a; Extended Data Fig. 3j |
| 10.1038/s41586-020-2922-4 | 72 | Capillary aerocyte |  | EDNRB | human | positive | add | M01947 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a; Extended Data Fig. 3j |
| 10.1038/s41586-020-2922-4 | 73 | Bronchial vessel 1 cell (Bro1) |  | ACKR1 | human | positive | matched | M00161 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3k |
| 10.1038/s41586-020-2922-4 | 74 | Bronchial vessel 1 cell (Bro1) |  | MYC | human | positive | add | M01948 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3k |
| 10.1038/s41586-020-2922-4 | 75 | Bronchial vessel 2 cell |  | MYC | human | positive | add | M01949 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3k |
| 10.1038/s41586-020-2922-4 | 76 | Bronchial vessel 2 cell |  | PLVAP | human | positive | add | M01950 | 图3j将 PLVAP 列为 Bro1/2 marker；Bro2 有图示表达，不能描述为 Bro2 特异。 定位：Extended Data Fig. 3j |
| 10.1038/s41586-020-2922-4 | 77 | Lymphatic endothelial cell |  | CCL21 | human | positive | matched | M00191 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 3n |
| 10.1038/s41586-020-2922-4 | 78 | IGSF21+ dendritic cell |  | IGSF21 | human | positive | matched | M00184 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4l; Fig. 2b |
| 10.1038/s41586-020-2922-4 | 79 | IGSF21+ dendritic cell |  | GPR34 | human | positive | matched | M00185 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4l |
| 10.1038/s41586-020-2922-4 | 80 | EREG+ dendritic |  | EREG | human | positive | matched | M00180 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4m; Fig. 2b |
| 10.1038/s41586-020-2922-4 | 81 | TREM2+ dendritic cell |  | TREM2 | human | positive | matched | M00224 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4n; Fig. 2b |
| 10.1038/s41586-020-2922-4 | 82 | TREM2+ dendritic cell |  | CHI3L1 | human | positive | matched | M00225 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4n |
| 10.1038/s41586-020-2922-4 | 83 | pDC |  | SCT | human | positive | add | M01951 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 84 | mDC2 |  | CD1E | human | positive | add | M01952 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 85 | classical monocytes |  | CD14 | human | positive | matched | M00168 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods: Flow cytometry and cell sorting |
| 10.1038/s41586-020-2922-4 | 86 | Alveolar macrophage |  | MARCO | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 87 | Macrophage (MP) |  | LPL | human | positive | add | M01953 | LPL 对应 MP；图5a不能把该群再限定为 interstitial。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 88 | Plasma cell |  | MZB1 | human | positive | add | M01954 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 89 | B cells |  | MS4A1 | human | positive | matched | M00151 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 90 | CD4+ T cells |  | CD4 | human | positive | matched | M00162 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods: Flow cytometry and cell sorting |
| 10.1038/s41586-020-2922-4 | 91 | CD8 naive T cells |  | CD8A | human | positive | add | M01955 | 图5a CD8A 对应 CD8 Na 亚群，保留其粒度。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 92 | natural killer cells |  | GNLY | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 93 | Basophil/Mast cell 1 |  | TPSAB1 | human | positive | exclude |  | 所引 Extended Data Fig.3/5 中不存在该标注关系，不能以经典 marker 常识补入。 定位：Extended Data Fig. 5a |
| 10.1038/s41586-020-2922-4 | 94 | Alveolar fibroblast |  | Slc7a10 | mouse | positive | matched | M00131 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4b |
| 10.1038/s41586-020-2922-4 | 95 | Adventitial fibroblast |  | Serpinf1 | mouse | positive | add | M01956 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Extended Data Fig. 4d |
| 10.1038/s44318-024-00328-6 | 1 | AT2-like (fdAT2 organoid cells) |  | NKX2-1 | human | positive | matched | M00620 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2B; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 2 | AT2-like (fdAT2 organoid cells) |  | SFTPC | human | positive | matched | M00610 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G, 1I, 1J; Fig. 2C; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 3 | AT2-like (fdAT2 organoid cells) |  | SFTPB | human | positive | matched | M00609 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G, 1I, 1J; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 4 | AT2-like (fdAT2 organoid cells) |  | SFTPA1 | human | positive | matched | M00621 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I, 1J; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 5 | AT2-like (fdAT2 organoid cells) |  | SFTPA2 | human | positive | add | M01957 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. 1M; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 6 | AT2-like (fdAT2 organoid cells) |  | SFTPD | human | positive | add | M01958 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. 1M; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 7 | AT2-like (fdAT2 organoid cells) |  | SLC34A2 | human | positive | matched | M00624 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2B; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 8 | AT2-like (fdAT2 organoid cells) |  | LPCAT1 | human | positive | matched | M00618 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2B |
| 10.1038/s44318-024-00328-6 | 9 | AT2-like (fdAT2 organoid cells) |  | HOPX | human | positive | matched | M00606 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G, 1I; Fig. EV2B; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 10 | AT2-like (fdAT2 organoid cells) |  | NAPSA | human | positive | matched | M00608 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G, 1I, 1J; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 11 | AT2-like (fdAT2 organoid cells) |  | LAMP3 | human | positive | matched | M00607 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G, 1I, 1M; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 12 | AT2-like (fdAT2 organoid cells) |  | CEACAM6 | human | positive | matched | M00614 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2B |
| 10.1038/s44318-024-00328-6 | 13 | AT2-like (fdAT2 organoid cells) |  | ABCA3 | human | positive | matched | M00604 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G; Fig. 1M; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 14 | AT2-like (fdAT2 organoid cells) |  | SFTA3 | human | positive | context_only |  | SFTA3 仅来自 Fig.1M 的 AT2 fate DEG 热图；不在 Fig.1I 注释 marker 面板。 定位：Fig. 1M |
| 10.1038/s44318-024-00328-6 | 15 | CXCL+ AT2-like cells |  | CXCL1 | human | positive | matched | M00615 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I, 1K; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 16 | CXCL+ AT2-like cells |  | CXCL2 | human | positive | matched | M00625 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2D |
| 10.1038/s44318-024-00328-6 | 17 | CXCL+ AT2-like cells |  | CXCL3 | human | positive | matched | M00626 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2D |
| 10.1038/s44318-024-00328-6 | 18 | CXCL+ AT2-like cells |  | CXCL8 | human | positive | add | M01959 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I |
| 10.1038/s44318-024-00328-6 | 19 | Cycling AT2-like |  | MKI67 | human | positive | add | M01960 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1G, 1I; Fig. EV2C; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 20 | Cycling AT2-like |  | PCNA | human | positive | add | M01961 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I |
| 10.1038/s44318-024-00328-6 | 21 | Intermediate |  | SOX2 | human | positive | add | M01962 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2G |
| 10.1038/s44318-024-00328-6 | 22 | Differentiating basal-like |  | TP63 | human | positive | add | M01963 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2K; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 23 | NE prog |  | ASCL1 | human | positive | matched | M00052 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2H; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 24 | Differentiating pulmonary NE |  | GRP | human | positive | matched | M00054 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2I |
| 10.1038/s44318-024-00328-6 | 25 | Differentiating pulmonary NE |  | PROX1 | human | positive | add | M01964 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I |
| 10.1038/s44318-024-00328-6 | 26 | Differentiating pulmonary NE |  | CHGA | human | positive | add | M01965 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I |
| 10.1038/s44318-024-00328-6 | 27 | Differentiating pulmonary NE |  | NEUROD1 | human | positive | matched | M00053 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2I |
| 10.1038/s44318-024-00328-6 | 28 | Ciliated-like |  | FOXJ1 | human | positive | add | M01966 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2J |
| 10.1038/s44318-024-00328-6 | 29 | Fetal tip progenitor |  | SOX9 | human | positive | matched | M00629 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1I; Fig. EV2E; Main Text p. 641 |
| 10.1038/s44318-024-00328-6 | 30 | AT2-like (fdAT2 organoid cells) |  | SOX9 | human | negative | add | M01967 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 641, Results; Fig. 1G; Appendix Fig. S1 |
| 10.1038/s44318-024-00328-6 | 31 | Alveolar type 1 cell (AT1) |  | AQP5 | human | positive | matched | M00602 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2C, 2F |
| 10.1038/s44318-024-00328-6 | 32 | Alveolar type 1 cell (AT1) |  | CAV1 | human | positive | matched | M00603 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2C, 2D, 2F, 2G, 2I-K; Fig. EV2F |
| 10.1038/s44318-024-00328-6 | 33 | Alveolar type 1 cell (AT1) |  | AGER | human | positive | matched | M00601 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2C, 2F, 2G, 2I-K; Fig. EV2F |
| 10.1038/s44318-024-00328-6 | 34 | proximal airway cells |  | SCGB3A2 | human | positive | matched | M00630 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. EV1A; Main Text Results p. 641 |
| 10.1101/2024.10.23.619925 | 1 | Epithelial |  | KRT19 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 2 | Epithelial |  | KLK3 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 3 | Epithelial |  | MSMB | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 4 | Epithelial |  | SCGB3A1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 5 | Epithelial |  | LTF | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 6 | T-cells |  | CD69 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 7 | T-cells |  | CXCR4 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 8 | T-cells |  | CCL4 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 9 | T-cells |  | IL7R | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 10 | T-cells |  | CCL5 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 11 | Endothelial |  | SPRY1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 12 | Endothelial |  | VWF | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 13 | Endothelial |  | SELE | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 14 | Endothelial |  | ACKR1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 15 | Endothelial |  | IFI27 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 16 | SMCs |  | ACTA2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 17 | SMCs |  | TAGLN | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 18 | SMCs |  | TPM2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 19 | SMCs |  | RGS5 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 20 | SMCs |  | C11orf96 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 21 | Myeloid |  | S100A9 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 22 | Myeloid |  | CXCL8 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 23 | Myeloid |  | IL1B | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 24 | Myeloid |  | LYZ | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 25 | Myeloid |  | HLA-DRA | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 26 | Myeloid |  | AIF1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 27 | CAFs |  | PTGDS | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 28 | CAFs |  | CFD | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 29 | CAFs |  | DCN | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 30 | CAFs |  | APOD | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 31 | CAFs |  | LUM | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 32 | PNS glial cells |  | CRYAB | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F; Fig. 5E |
| 10.1101/2024.10.23.619925 | 33 | PNS glial cells |  | PLP1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F; Fig. 5E |
| 10.1101/2024.10.23.619925 | 34 | PNS glial cells |  | S100B | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F; Fig. 5E |
| 10.1101/2024.10.23.619925 | 35 | PNS glial cells |  | GPM6B | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F; Fig. 5E |
| 10.1101/2024.10.23.619925 | 36 | PNS glial cells |  | SCN7A | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F; Fig. 5E |
| 10.1101/2024.10.23.619925 | 37 | B-cells |  | CD83 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 38 | B-cells |  | BANK1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 39 | B-cells |  | MS4A1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 40 | B-cells |  | CD37 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 41 | Cycling |  | TOP2A | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 42 | Cycling |  | PCLAF | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 43 | Cycling |  | HMGB2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 44 | Cycling |  | STMN1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 45 | Plasma cells |  | IGHM | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 46 | Plasma cells |  | JCHAIN | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 47 | Plasma cells |  | IGHA1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 48 | Plasma cells |  | IGHG1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 49 | Plasma cells |  | IGKC | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 50 | Plasma cells |  | IGLC2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 51 | Unassigned |  | DKK3 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 52 | Unassigned |  | CRYM | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 53 | Unassigned |  | RGS13 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 54 | Unassigned |  | ANXA4 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 55 | Unassigned |  | ANXA1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 1F |
| 10.1101/2024.10.23.619925 | 56 | CAFs |  | DCN | human | positive | matched | M01234 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 23; Fig. 4D |
| 10.1101/2024.10.23.619925 | 57 | CAFs |  | PDGFRA | human | positive | matched | M01235 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 23; Fig. 4D |
| 10.1101/2024.10.23.619925 | 58 | uniCAFs |  | DPT | human | positive | matched | M01272 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 24; Fig. 4D |
| 10.1101/2024.10.23.619925 | 59 | uniCAFs |  | PI16 | human | positive | matched | M01273 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 24; Fig. 4D |
| 10.1101/2024.10.23.619925 | 60 | uniCAFs |  | MGP | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 24 |
| 10.1101/2024.10.23.619925 | 61 | uniCAFs |  | CCDC80 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 24 |
| 10.1101/2024.10.23.619925 | 62 | uniCAFs |  | GAS1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 24 |
| 10.1101/2024.10.23.619925 | 63 | uniCAFs |  | PCOLCE2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 24 |
| 10.1101/2024.10.23.619925 | 64 | uniCAFs |  | PLA2G2A | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 24 |
| 10.1101/2024.10.23.619925 | 65 | NPF-like |  | IGFBP2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25-26 |
| 10.1101/2024.10.23.619925 | 66 | NPF-like |  | PTN | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25-26 |
| 10.1101/2024.10.23.619925 | 67 | NPF-like |  | APCDD1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25-26 |
| 10.1101/2024.10.23.619925 | 68 | NPF-like |  | PTGDS | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25-26 |
| 10.1101/2024.10.23.619925 | 69 | NPF-like |  | A2M | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25-26 |
| 10.1101/2024.10.23.619925 | 70 | pnCAFs |  | DPT | human | low | matched | M01263 | 作者 DPTlow 是低表达，不等于阴性。 定位：Main Text p. 26; Fig. 4D |
| 10.1101/2024.10.23.619925 | 71 | pnCAFs |  | PI16 | human | positive | matched | M01264 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 26; Fig. 4D |
| 10.1101/2024.10.23.619925 | 72 | pnCAFs |  | CDH19 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 26 |
| 10.1101/2024.10.23.619925 | 73 | pnCAFs |  | APOD | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 26 |
| 10.1101/2024.10.23.619925 | 74 | pnCAFs |  | DDIT4 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 26 |
| 10.1101/2024.10.23.619925 | 75 | pnCAFs |  | ANGPTL7 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 26 |
| 10.1101/2024.10.23.619925 | 76 | pnCAFs |  | SLC2A1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 26 |
| 10.1101/2024.10.23.619925 | 77 | whCAFs |  | FAP | human | positive | add | M01968 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 25; Fig. 4D |
| 10.1101/2024.10.23.619925 | 78 | whCAFs |  | COL3A1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25 |
| 10.1101/2024.10.23.619925 | 79 | whCAFs |  | COL1A1 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25 |
| 10.1101/2024.10.23.619925 | 80 | whCAFs |  | VCAN | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25 |
| 10.1101/2024.10.23.619925 | 81 | whCAFs |  | POSTN | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25 |
| 10.1101/2024.10.23.619925 | 82 | whCAFs |  | CXCL2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E; Main Text p. 25 |
| 10.1101/2024.10.23.619925 | 83 | SMC-like CAFs |  | ACTA2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 84 | SMC-like CAFs |  | MYH11 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 85 | SMC-like CAFs |  | ADAMTS4 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 86 | SMC-like CAFs |  | MT1A | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 87 | SMC-like CAFs |  | CCL2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 88 | CAFs_IFN |  | IFI6 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 89 | CAFs_IFN |  | ISG15 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 90 | CAFs_IFN |  | IFI44L | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 91 | CAFs_IFN |  | IFIT2 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 92 | CAFs_IFN |  | IFI27 | human | positive | context_only |  | Fig.1F/4E 明确展示 top DEG；未提供此 gene–cell 对用于定义/注释的独立证据。 定位：Fig. 4E |
| 10.1101/2024.10.23.619925 | 93 | pSMCs |  | ACTG2 | human | positive | matched | M01265 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 94 | pSMCs |  | CNN1 | human | positive | matched | M01266 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 95 | vSMCs |  | RERGL | human | positive | matched | M01276 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22-23; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 96 | vSMCs |  | BCAM | human | positive | matched | M01274 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 97 | vSMCs |  | PLN | human | positive | matched | M01275 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 98 | Pericytes |  | THY1 | human | positive | matched | M01262 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 99 | Pericytes |  | COL6A3 | human | positive | matched | M01260 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 100 | Pericytes |  | GGT5 | human | positive | matched | M01261 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 22; Supp. Fig. S13C-D |
| 10.1101/2024.10.23.619925 | 101 | Basal |  | KRT5 | human | positive | matched | M01227 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11; Supp. Fig. S7C |
| 10.1101/2024.10.23.619925 | 102 | Basal |  | TP63 | human | positive | matched | M01228 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11; Supp. Fig. S7C |
| 10.1101/2024.10.23.619925 | 103 | Luminal |  | KLK3 | human | positive | matched | M01247 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 10-11; Supp. Fig. S7C |
| 10.1101/2024.10.23.619925 | 104 | Luminal |  | NKX3-1 | human | positive | matched | M01249 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11; Supp. Fig. S7C |
| 10.1101/2024.10.23.619925 | 105 | Luminal |  | MSMB | human | positive | matched | M01248 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11-12; Fig. 2E |
| 10.1101/2024.10.23.619925 | 106 | Club |  | SCGB3A1 | human | positive | matched | M01239 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11-12; Fig. 2E |
| 10.1101/2024.10.23.619925 | 107 | Club |  | PIGR | human | positive | matched | M01238 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 10-11; Supp. Fig. S7C |
| 10.1101/2024.10.23.619925 | 108 | Club |  | LCN2 | human | positive | matched | M01237 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11; Supp. Fig. S7C |
| 10.1101/2024.10.23.619925 | 109 | NE |  | CHGA | human | positive | matched | M01259 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 10; Fig. 2E |
| 10.1101/2024.10.23.619925 | 110 | NE |  | CALCA | human | positive | matched | M01258 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 10; Fig. 2E |
| 10.1101/2024.10.23.619925 | 111 | Ciliated |  | CAPS | human | positive | matched | M01236 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text p. 11; Fig. 2E |
| 10.1101/2024.10.23.619925 | 112 | Luminal-like | c0 | MGP | human | positive | add | M01969 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 113 | Basal | c1 | KRT15 | human | positive | add | M01970 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 114 | Basal | c2 | S100A2 | human | positive | matched | M01233 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 115 | Basal | c3 | PLCG2 | human | positive | matched | M01232 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 116 | Club | c4 | MMP7 | human | positive | add | M01971 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 117 | Basal | c6 | DST | human | positive | add | M01972 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 118 | Luminal | c8 | SPON2 | human | positive | add | M01973 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 119 | Luminal | c8 | ERG | human | positive | add | M01974 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 120 | Club | c9 | OLFM4 | human | positive | matched | M01241 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 121 | Luminal-like | c10 | PLA2G2A | human | positive | matched | M01256 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 122 | Luminal | c11 | NCAPD3 | human | positive | matched | M01251 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 123 | Luminal | c12 | ERG | human | positive | add | M01975 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 124 | Luminal | c13 | ETV4 | human | positive | add | M01976 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 125 | Luminal | c14 | FABP5 | human | positive | add | M01977 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 126 | Club | c15 | SAA1 | human | positive | matched | M01246 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 127 | Club | c16 | CCL20 | human | positive | matched | M01245 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 128 | Basal | c17 | RARRES2 | human | positive | matched | M01231 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 129 | Basal | c17 | FOXI1 | human | positive | matched | M01230 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 130 | Luminal | c18 | NPY | human | positive | matched | M01252 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 131 | Luminal | c19 | TFF3 | human | positive | matched | M01253 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 132 | Club | c20 | IFI6 | human | positive | matched | M01240 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 133 | Luminal | c21 | ETV1 | human | positive | add | M01978 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2024.10.23.619925 | 134 | Luminal | c22 | KLK12 | human | positive | matched | M01250 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 2A, 2D, 2E; Main Text p. 11-12 |
| 10.1101/2025.01.17.633590 | 1 | beta |  | INS | human | positive | matched | M01280 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 4 line 95; Page 26 line 795 |
| 10.1101/2025.01.17.633590 | 2 | alpha |  | GCG | human | positive | matched | M01279 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 4 line 95; Page 26 line 795 |
| 10.1101/2025.01.17.633590 | 3 | delta |  | SST | human | positive | matched | M01281 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 4 line 95; Page 26 line 795 |
| 10.1101/2025.01.17.633590 | 4 | gamma |  | PPY | human | positive | matched | M01285 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 4 line 95; Page 26 line 796 |
| 10.1101/2025.01.17.633590 | 5 | epsilon |  | GHRL | human | positive | matched | M01284 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 4 line 95; Page 26 line 796 |
| 10.1101/2025.01.17.633590 | 6 | Ductal |  | KRT19 | human | positive | matched | M01282 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 796 |
| 10.1101/2025.01.17.633590 | 7 | Acinar |  | REG1B | human | positive | matched | M01277 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 796 |
| 10.1101/2025.01.17.633590 | 8 | Stellate |  | COL1A1 | human | positive | matched | M01289 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 796 |
| 10.1101/2025.01.17.633590 | 9 | activated stellate |  | FABP4 | human | positive | matched | M01278 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 797 |
| 10.1101/2025.01.17.633590 | 10 | Endothelial |  | PLVAP | human | positive | matched | M01283 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 797 |
| 10.1101/2025.01.17.633590 | 11 | Schwann |  | NGFR | human | positive | matched | M00067 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 797 |
| 10.1101/2025.01.17.633590 | 12 | Immune |  | C1QC | human | positive | matched | M01286 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 797 |
| 10.1101/2025.01.17.633590 | 13 | Mast |  | TPSB2 | human | positive | matched | M01287 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 26 line 797 |
| 10.1101/2025.01.17.633590 | 14 | proliferating cells |  | TOP2A | human | positive | matched | M01288 | 所引方法 TOP2A 仅定义 proliferating cells，不直接指定 proliferating alpha。 定位：Methods Page 26 line 798 |
| 10.1101/2025.01.17.633590 | 15 | alpha |  | DPP4 | human | positive | add | M01979 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 16 | alpha |  | ADAMTS18 | human | positive | add | M01980 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 17 | alpha |  | F2 | human | positive | add | M01981 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 18 | alpha |  | ADCY7 | human | positive | add | M01982 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 19 | alpha |  | APOH | human | positive | add | M01983 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 20 | alpha |  | GPER1 | human | positive | add | M01984 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 21 | alpha |  | GRIN3A | human | positive | add | M01985 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 22 | alpha |  | ADORA2A | human | positive | add | M01986 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 23 | alpha |  | FAP | human | positive | add | M01987 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 24 | alpha |  | EPHA4 | human | positive | add | M01988 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 25 | alpha |  | CD109 | human | positive | add | M01989 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 26 | alpha |  | CCK | human | positive | add | M01990 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 27 | alpha |  | MMP26 | human | positive | add | M01991 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 28 | alpha |  | DRD1 | human | positive | add | M01992 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 29 | alpha |  | NLRP3 | human | positive | add | M01993 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 30 | alpha |  | FGB | human | positive | add | M01994 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 31 | alpha |  | IL4I1 | human | positive | add | M01995 | Supplementary Fig.2 最后一行是 IL4I1，Gemini 误读为 IL4。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 32 | P.Alpha |  | PRC1 | human | positive | add | M01996 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 33 | P.Alpha |  | MND1 | human | positive | add | M01997 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 34 | P.Alpha |  | MKI67 | human | positive | add | M01998 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 35 | P.Alpha |  | BRCA2 | human | positive | add | M01999 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 36 | P.Alpha |  | KIFC1 | human | positive | add | M02000 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 37 | P.Alpha |  | SGO1 | human | positive | add | M02001 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 38 | P.Alpha |  | CDCA5 | human | positive | add | M02002 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 39 | P.Alpha |  | NCAPG | human | positive | add | M02003 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 40 | P.Alpha |  | NCAPH | human | positive | add | M02004 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 41 | P.Alpha |  | CHEK1 | human | positive | add | M02005 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 42 | beta |  | ADCYAP1 | human | positive | add | M02006 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 43 | beta |  | NKX6-1 | human | positive | add | M02007 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 44 | beta |  | HADH | human | positive | add | M02008 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 45 | beta |  | SLC2A2 | human | positive | add | M02009 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 46 | beta |  | PDX1 | human | positive | add | M02010 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 47 | beta |  | MAFA | human | positive | add | M02011 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 48 | beta |  | GLP1R | human | positive | add | M02012 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 49 | beta |  | CASR | human | positive | add | M02013 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 50 | beta |  | CPLX3 | human | positive | add | M02014 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 51 | delta |  | GABRA1 | human | positive | add | M02015 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 52 | delta |  | DRD2 | human | positive | add | M02016 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 53 | delta |  | GABRG2 | human | positive | add | M02017 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 54 | delta |  | HAP1 | human | positive | add | M02018 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 55 | delta |  | GABRA5 | human | positive | add | M02019 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 56 | delta |  | GABRA3 | human | positive | add | M02020 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 57 | delta |  | GABRB2 | human | positive | add | M02021 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 58 | epsilon |  | HRH2 | human | positive | add | M02022 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 59 | epsilon |  | NPY1R | human | positive | add | M02023 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 60 | epsilon |  | ADGRD1 | human | positive | add | M02024 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 61 | epsilon |  | FFAR3 | human | positive | add | M02025 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 62 | epsilon |  | CALCR | human | positive | add | M02026 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 63 | epsilon |  | OPRK1 | human | positive | add | M02027 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 64 | epsilon |  | GPR12 | human | positive | add | M02028 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 65 | epsilon |  | PTGFR | human | positive | add | M02029 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 66 | epsilon |  | GRM8 | human | positive | add | M02030 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 67 | gamma |  | ETV1 | human | positive | add | M02031 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 68 | gamma |  | MEIS2 | human | positive | add | M02032 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 69 | gamma |  | FOXP2 | human | positive | add | M02033 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 70 | gamma |  | SLITRK6 | human | positive | add | M02034 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 71 | gamma |  | SLC8A1 | human | positive | add | M02035 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 72 | gamma |  | ITGA2 | human | positive | add | M02036 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 73 | gamma |  | DMD | human | positive | add | M02037 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 74 | gamma |  | USP53 | human | positive | add | M02038 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 75 | Acinar |  | PRSS2 | human | positive | add | M02039 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 76 | Acinar |  | CTRB2 | human | positive | add | M02040 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 77 | Acinar |  | SGK1 | human | positive | add | M02041 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 78 | Acinar |  | CTRB1 | human | positive | add | M02042 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 79 | Acinar |  | PRSS1 | human | positive | add | M02043 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 80 | Acinar |  | AKR1C2 | human | positive | add | M02044 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 81 | Acinar |  | SERPINA3 | human | positive | add | M02045 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 82 | Acinar |  | AKR1C1 | human | positive | add | M02046 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 83 | Acinar |  | PNLIP | human | positive | add | M02047 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 84 | Acinar |  | CLPSL2 | human | positive | add | M02048 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 85 | Ductal |  | KRT8 | human | positive | add | M02049 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 86 | Ductal |  | FGFR2 | human | positive | add | M02050 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 87 | Ductal |  | KRT18 | human | positive | add | M02051 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 88 | Ductal |  | EVPL | human | positive | add | M02052 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 89 | Ductal |  | KRT80 | human | positive | add | M02053 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 90 | Ductal |  | SLC44A4 | human | positive | add | M02054 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 91 | Ductal |  | KRT23 | human | positive | add | M02055 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 92 | Ductal |  | KRT15 | human | positive | add | M02056 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 93 | Ductal |  | LAMB3 | human | positive | add | M02057 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 94 | Endothelial |  | NOTCH4 | human | positive | add | M02058 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 95 | Endothelial |  | ENG | human | positive | add | M02059 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 96 | Endothelial |  | DLL4 | human | positive | add | M02060 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 97 | Endothelial |  | SOX17 | human | positive | add | M02061 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 98 | Endothelial |  | CLIC4 | human | positive | add | M02062 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 99 | Endothelial |  | RAPGEF3 | human | positive | add | M02063 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 100 | Endothelial |  | ACVRL1 | human | positive | add | M02064 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 101 | Endothelial |  | ICAM1 | human | positive | add | M02065 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 102 | Endothelial |  | PDE2A | human | positive | add | M02066 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 103 | Endothelial |  | PECAM1 | human | positive | add | M02067 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 104 | Immune |  | LILRB4 | human | positive | add | M02068 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 105 | Immune |  | CD300A | human | positive | add | M02069 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 106 | Immune |  | DOCK2 | human | positive | add | M02070 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 107 | Immune |  | HAVCR2 | human | positive | add | M02071 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 108 | Immune |  | WAS | human | positive | add | M02072 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 109 | Immune |  | NCKAP1L | human | positive | add | M02073 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 110 | Immune |  | CLEC7A | human | positive | add | M02074 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 111 | Immune |  | AIF1 | human | positive | add | M02075 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 112 | Immune |  | TNFAIP8L2 | human | positive | add | M02076 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 113 | Immune |  | CD4 | human | positive | add | M02077 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 114 | Schwann |  | DAG1 | human | positive | add | M02078 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 115 | Schwann |  | LPAR1 | human | positive | add | M02079 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 116 | Schwann |  | GPC1 | human | positive | add | M02080 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 117 | Schwann |  | LGI4 | human | positive | add | M02081 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 118 | Schwann |  | PLP1 | human | positive | add | M02082 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 119 | Schwann |  | SOX10 | human | positive | add | M02083 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 120 | Schwann |  | PMP22 | human | positive | add | M02084 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 121 | Schwann |  | S100B | human | positive | add | M02085 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 122 | Schwann |  | NTRK3 | human | positive | add | M02086 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 123 | Schwann |  | PTPRZ1 | human | positive | add | M02087 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 124 | Stellate |  | DDR2 | human | positive | add | M02088 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 125 | activated stellate |  | DDR2 | human | positive | add | M02089 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 126 | Stellate |  | COL5A1 | human | positive | add | M02090 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 127 | activated stellate |  | COL5A1 | human | positive | add | M02091 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 128 | Stellate |  | COL6A3 | human | positive | add | M02092 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 129 | activated stellate |  | COL6A3 | human | positive | add | M02093 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 130 | Stellate |  | COL6A1 | human | positive | add | M02094 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 131 | activated stellate |  | COL6A1 | human | positive | add | M02095 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 132 | Stellate |  | VCAN | human | positive | add | M02096 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 133 | activated stellate |  | VCAN | human | positive | add | M02097 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 134 | Stellate |  | ADAM19 | human | positive | add | M02098 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 135 | activated stellate |  | ADAM19 | human | positive | add | M02099 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 136 | Stellate |  | POSTN | human | positive | add | M02100 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 137 | activated stellate |  | POSTN | human | positive | add | M02101 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 138 | Stellate |  | SFRP2 | human | positive | add | M02102 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 139 | activated stellate |  | SFRP2 | human | positive | add | M02103 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 140 | Stellate |  | TGFB1 | human | positive | add | M02104 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 141 | activated stellate |  | TGFB1 | human | positive | add | M02105 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 2 |
| 10.1101/2025.01.17.633590 | 142 | beta | cluster 1 | RBP4 | human | positive | add | M02106 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 143 | beta | cluster 1 | MAFA | human | positive | add | M02107 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 144 | beta | cluster 1 | HADH | human | positive | add | M02108 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 145 | beta | cluster 1 | TTR | human | positive | add | M02109 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 146 | beta | cluster 1 | ABCC8 | human | positive | add | M02110 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 147 | beta | cluster 1 | PDX1 | human | positive | add | M02111 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 148 | beta | cluster 1 | SLC30A8 | human | positive | add | M02112 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 149 | beta | cluster 1 | G6PC2 | human | positive | add | M02113 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 150 | beta | cluster 1 | FFAR4 | human | positive | add | M02114 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 392 |
| 10.1101/2025.01.17.633590 | 151 | beta | cluster 2 | HILPDA | human | positive | add | M02115 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 152 | beta | cluster 2 | CITED2 | human | positive | add | M02116 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 153 | beta | cluster 2 | NDRG1 | human | positive | add | M02117 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 154 | beta | cluster 2 | PLOD2 | human | positive | add | M02118 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 155 | beta | cluster 2 | CD24 | human | positive | add | M02119 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 156 | beta | cluster 2 | NOL3 | human | positive | add | M02120 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 157 | beta | cluster 2 | ADM | human | positive | add | M02121 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 158 | beta | cluster 2 | PGK1 | human | positive | add | M02122 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 159 | beta | cluster 2 | ERO1A | human | positive | add | M02123 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 160 | beta | cluster 2 | EPAS1 | human | positive | add | M02124 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 161 | beta | cluster 2 | BNIP3 | human | positive | add | M02125 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 162 | beta | cluster 2 | HMOX1 | human | positive | add | M02126 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 163 | beta | cluster 2 | ATP1B1 | human | positive | add | M02127 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 164 | beta | cluster 3 | SIX3 | human | positive | unresolved |  | Fig.4c 与正文 cluster 3/5 的功能描述对应不一致；不能仅靠连续基因块顺序确定 SIX3/TFF3 亚群归属。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 165 | beta | cluster 3 | SIX3-AS1 | human | positive | unresolved |  | Fig.4c 与正文 cluster 3/5 的功能描述对应不一致；不能仅靠连续基因块顺序确定 SIX3/TFF3 亚群归属。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 166 | beta | cluster 3 | TFF3 | human | positive | unresolved |  | Fig.4c 与正文 cluster 3/5 的功能描述对应不一致；不能仅靠连续基因块顺序确定 SIX3/TFF3 亚群归属。 定位：Figure 4c |
| 10.1101/2025.01.17.633590 | 167 | beta | cluster 4 | HSPA1A | human | positive | add | M02128 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 168 | beta | cluster 4 | HSPA6 | human | positive | add | M02129 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 169 | beta | cluster 4 | HSPA1B | human | positive | add | M02130 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 170 | beta | cluster 4 | DNAJB1 | human | positive | add | M02131 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 171 | beta | cluster 4 | HSPB1 | human | positive | add | M02132 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 172 | beta | cluster 4 | HSPH1 | human | positive | add | M02133 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 173 | beta | cluster 4 | HSP90AA1 | human | positive | add | M02134 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 174 | beta | cluster 4 | PPP1R15A | human | positive | add | M02135 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 175 | beta | cluster 4 | BAG3 | human | positive | add | M02136 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 176 | beta | cluster 4 | HSPD1 | human | positive | add | M02137 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 177 | beta | cluster 4 | SERPINH1 | human | positive | add | M02138 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 178 | beta | cluster 4 | DNAJB4 | human | positive | add | M02139 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 179 | beta | cluster 4 | ATF3 | human | positive | add | M02140 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 180 | beta | cluster 4 | HSP90AB1 | human | positive | add | M02141 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 181 | beta | cluster 4 | DNAJA1 | human | positive | add | M02142 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 395 |
| 10.1101/2025.01.17.633590 | 182 | beta | cluster 5 | RPL4 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 183 | beta | cluster 5 | PABPC1 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 184 | beta | cluster 5 | RPL23A | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 185 | beta | cluster 5 | RPS3 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 186 | beta | cluster 5 | EIF3E | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 187 | beta | cluster 5 | RPL6 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 188 | beta | cluster 5 | RPL13 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 189 | beta | cluster 5 | RPS14 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 190 | beta | cluster 5 | RPL12 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 191 | beta | cluster 5 | RPS8 | human | positive | unresolved |  | Fig.4c translation initiation 基因块的 cluster 3/5 对应与正文不一致，保留未决而不直接沿用 Gemini cluster 5。 定位：Figure 4c; Main Text Page 13 line 393 |
| 10.1101/2025.01.17.633590 | 192 | beta | cluster 6 | DDIT3 | human | positive | add | M02143 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 193 | beta | cluster 6 | HSPA5 | human | positive | add | M02144 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 194 | beta | cluster 6 | HERPUD1 | human | positive | add | M02145 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 195 | beta | cluster 6 | TRIB3 | human | positive | add | M02146 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 196 | beta | cluster 6 | HSP90B1 | human | positive | add | M02147 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 197 | beta | cluster 6 | PDIA4 | human | positive | add | M02148 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 198 | beta | cluster 6 | MANF | human | positive | add | M02149 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 199 | beta | cluster 6 | CEBPB | human | positive | add | M02150 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 200 | beta | cluster 6 | SDF2L1 | human | positive | add | M02151 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 201 | beta | cluster 6 | ATF4 | human | positive | add | M02152 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 202 | beta | cluster 6 | DNAJB9 | human | positive | add | M02153 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 203 | beta | cluster 6 | SELENOK | human | positive | add | M02154 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 204 | beta | cluster 6 | DNAJB11 | human | positive | add | M02155 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 205 | beta | cluster 6 | SERP1 | human | positive | add | M02156 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 206 | beta | cluster 6 | CALR | human | positive | add | M02157 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 207 | beta | cluster 6 | SELENOS | human | positive | add | M02158 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 208 | beta | cluster 6 | SEL1L | human | positive | add | M02159 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 388 |
| 10.1101/2025.01.17.633590 | 209 | beta | cluster 7 | ID3 | human | positive | add | M02160 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 210 | beta | cluster 7 | PLK2 | human | positive | matched | M01297 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 211 | beta | cluster 7 | LSAMP | human | positive | add | M02161 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 212 | beta | cluster 7 | RGS16 | human | positive | add | M02162 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 213 | beta | cluster 7 | BTG3 | human | positive | add | M02163 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 214 | beta | cluster 7 | SYNE2 | human | positive | add | M02164 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 215 | beta | cluster 7 | CDKN2B | human | positive | matched | M01296 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 216 | beta | cluster 7 | CDKN2A | human | positive | matched | M01295 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 217 | beta | cluster 7 | TP53BP1 | human | positive | add | M02165 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 218 | beta | cluster 7 | B2M | human | positive | matched | M01294 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 397 |
| 10.1101/2025.01.17.633590 | 219 | beta | cluster 8 | ID2 | human | positive | add | M02166 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 220 | beta | cluster 8 | STX1A | human | positive | add | M02167 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 221 | beta | cluster 8 | ITGB1 | human | positive | add | M02168 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 222 | beta | cluster 8 | RAB3B | human | positive | add | M02169 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 223 | beta | cluster 8 | ANXA2 | human | positive | add | M02170 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 224 | beta | cluster 8 | AQP3 | human | positive | add | M02171 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 225 | beta | cluster 8 | ADGRG1 | human | positive | add | M02172 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Figure 4c; Main Text Page 13 line 398 |
| 10.1101/2025.01.17.633590 | 226 | alpha | cluster 1 | ARRDC4 | human | positive | add | M02173 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 227 | alpha | cluster 1 | SPC25 | human | positive | add | M02174 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 228 | alpha | cluster 1 | PLK2 | human | positive | add | M02175 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 229 | alpha | cluster 1 | KIF12 | human | positive | add | M02176 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 230 | alpha | cluster 2 | FXYD5 | human | positive | add | M02177 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 231 | alpha | cluster 2 | NDRG1 | human | positive | add | M02178 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 232 | alpha | cluster 2 | CITED2 | human | positive | add | M02179 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 233 | alpha | cluster 2 | SOCS1 | human | positive | add | M02180 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 234 | alpha | cluster 2 | CEBPD | human | positive | add | M02181 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 235 | alpha | cluster 2 | LDHA | human | positive | add | M02182 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 236 | alpha | cluster 2 | TNFRSF12A | human | positive | add | M02183 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 237 | alpha | cluster 3 | RSAD2 | human | positive | add | M02184 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 238 | alpha | cluster 3 | TPM4 | human | positive | add | M02185 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 239 | alpha | cluster 3 | CD68 | human | positive | add | M02186 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 240 | alpha | cluster 3 | TUBB3 | human | positive | add | M02187 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 241 | alpha | cluster 4 | PLCE1 | human | positive | add | M02188 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 242 | alpha | cluster 4 | G6PC2 | human | positive | add | M02189 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 243 | alpha | cluster 4 | CRH | human | positive | add | M02190 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 244 | alpha | cluster 4 | TMEM236 | human | positive | add | M02191 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 245 | alpha | cluster 5 | PFN2 | human | positive | add | M02192 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 246 | alpha | cluster 5 | MT-ND6 | human | positive | add | M02193 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 247 | alpha | cluster 5 | MT-CO3 | human | positive | add | M02194 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 248 | alpha | cluster 5 | MT-ATP6 | human | positive | add | M02195 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 249 | alpha | cluster 5 | MT-CYB | human | positive | add | M02196 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 250 | alpha | cluster 6 | PART1 | human | positive | add | M02197 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 251 | alpha | cluster 6 | SMOC1 | human | positive | add | M02198 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 252 | alpha | cluster 6 | MUC13 | human | positive | add | M02199 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 253 | alpha | cluster 6 | IGFBP2 | human | positive | add | M02200 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 254 | alpha | cluster 6 | PDK4 | human | positive | add | M02201 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 255 | alpha | cluster 7 | HSPA1A | human | positive | add | M02202 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 256 | alpha | cluster 7 | HSPA6 | human | positive | add | M02203 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 257 | alpha | cluster 7 | HSPA1B | human | positive | add | M02204 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 258 | alpha | cluster 7 | DNAJB1 | human | positive | add | M02205 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 259 | alpha | cluster 7 | HSPH1 | human | positive | add | M02206 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 8e |
| 10.1101/2025.01.17.633590 | 260 | delta | cluster 1 | ANK1 | human | positive | add | M02207 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 261 | delta | cluster 2 | SERPINA1 | human | positive | add | M02208 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 262 | delta | cluster 2 | CD68 | human | positive | add | M02209 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 263 | delta | cluster 2 | ANXA2 | human | positive | add | M02210 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 264 | delta | cluster 3 | BCHE | human | positive | add | M02211 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 265 | delta | cluster 3 | TTR | human | positive | add | M02212 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 266 | delta | cluster 4 | HAP1 | human | positive | add | M02213 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 267 | delta | cluster 4 | NPY | human | positive | add | M02214 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 268 | delta | cluster 5 | FRZB | human | positive | unresolved |  | Supplementary Fig.9e 该区域 cluster 5/6 配对需更清晰源表确认，当前 Gemini 连续行分组不能作为唯一依据。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 269 | delta | cluster 5 | PHGR1 | human | positive | unresolved |  | Supplementary Fig.9e 该区域 cluster 5/6 配对需更清晰源表确认，当前 Gemini 连续行分组不能作为唯一依据。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 270 | delta | cluster 6 | SYT1 | human | positive | unresolved |  | Supplementary Fig.9e 该区域 cluster 5/6 配对需更清晰源表确认，当前 Gemini 连续行分组不能作为唯一依据。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 271 | delta | cluster 6 | CPB1 | human | positive | unresolved |  | Supplementary Fig.9e 该区域 cluster 5/6 配对需更清晰源表确认，当前 Gemini 连续行分组不能作为唯一依据。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 272 | delta | cluster 7 | GRP | human | positive | add | M02215 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.01.17.633590 | 273 | delta | cluster 7 | RGS2 | human | positive | add | M02216 | 所引图注明确为 marker gene expression，按图中对应细胞/cluster核对；不是仅因 differential_expression 字段即拒绝。 定位：Supplementary Figure 9e |
| 10.1101/2025.09.26.678707 | 1 | C-FIB |  | C7 | human | positive | add | M02217 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 2 | C-FIB |  | MEG3 | human | positive | add | M02218 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 3 | C-FIB |  | SELENOP | human | positive | add | M02219 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 4 | C-FIB |  | CXCL12 | human | positive | add | M02220 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 5 | C-FIB-PATH |  | CCN1 | human | positive | add | M02221 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 6 | C-FIB-PATH |  | CXCL12 | human | positive | add | M02222 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 7 | C-FIB-OSMRlo |  | CCN1 | human | positive | add | M02223 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 8 | C-FIB-OSMRlo |  | CXCL12 | human | positive | add | M02224 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 9 | C-FIB-OSMRhi |  | OSMR | human | positive | matched | M01543 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 6 |
| 10.1101/2025.09.26.678707 | 10 | C-FIB-OSMRhi |  | IL1R1 | human | positive | matched | M01542 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 6, 14 |
| 10.1101/2025.09.26.678707 | 11 | C-FIB-OSMRhi |  | CCL2 | human | positive | matched | M01540 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 6, 14 |
| 10.1101/2025.09.26.678707 | 12 | C-FIB-OSMRhi |  | CXCL10 | human | positive | matched | M01541 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 6 |
| 10.1101/2025.09.26.678707 | 13 | C-FIB-OSMRhi |  | CCL19 | human | positive | matched | M01539 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 6 |
| 10.1101/2025.09.26.678707 | 14 | C-FIB-OSMRhi |  | IL1B | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Main text Page 14 |
| 10.1101/2025.09.26.678707 | 15 | C-MYOF |  | SULF1 | human | positive | add | M02225 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 16 | C-MYOF |  | FAP | human | positive | matched | M01545 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 17 | C-MYOF |  | POSTN | human | positive | matched | M01547 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 18 | C-MYOF |  | SPARC | human | positive | matched | M01548 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 6 |
| 10.1101/2025.09.26.678707 | 19 | C-MYOF |  | COL3A1 | human | positive | matched | M01544 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 6 |
| 10.1101/2025.09.26.678707 | 20 | pvFIB-RSPO3+ |  | RSPO3 | human | positive | matched | M01577 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 7 |
| 10.1101/2025.09.26.678707 | 21 | pvFIB-RSPO3+ |  | FLRT2 | human | positive | add | M02226 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 22 | pvFIB-RSPO3+ |  | IGF1 | human | positive | add | M02227 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 7 |
| 10.1101/2025.09.26.678707 | 23 | pvFIB-RSPO3+ |  | C3 | human | positive | add | M02228 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 24 | pvFIB-RSPO3+ |  | WNT5B | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Main text Page 7 |
| 10.1101/2025.09.26.678707 | 25 | pvFIB-PI16+ |  | PI16 | human | positive | matched | M01576 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 7 |
| 10.1101/2025.09.26.678707 | 26 | pvFIB-PI16+ |  | CD34 | human | positive | matched | M01574 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 7 |
| 10.1101/2025.09.26.678707 | 27 | pvFIB-PI16+ |  | MFAP5 | human | positive | matched | M01575 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 7 |
| 10.1101/2025.09.26.678707 | 28 | pvFIB-PI16+ |  | FLRT2 | human | positive | add | M02229 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 29 | pvFIB-PI16+ |  | EPHA3 | human | positive | add | M02230 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 30 | pvFIB |  | CD34 | human | positive | add | M02231 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 31 | pvFIB |  | PI16 | human | positive | add | M02232 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 32 | pvFIB |  | EPHA3 | human | positive | add | M02233 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 33 | pvMYOF |  | MYH11 | human | positive | add | M02234 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b |
| 10.1101/2025.09.26.678707 | 34 | pvMYOF |  | ACTA2 | human | positive | matched | M01578 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2b, Main text Page 7 |
| 10.1101/2025.09.26.678707 | 35 | B |  | BANK1 | human | positive | add | M02235 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 36 | PL |  | XBP1 | human | positive | add | M02236 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 37 | Naïve Th |  | CD3D | human | positive | add | M02237 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 38 | Naïve Th |  | IL7R | human | positive | add | M02238 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 39 | MAIT |  | CD3D | human | positive | add | M02239 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 40 | MAIT |  | SLC4A10 | human | positive | add | M02240 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 41 | ILC3 |  | IL7R | human | positive | add | M02241 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 42 | ILC3 |  | KIT | human | positive | add | M02242 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 43 | T-REG |  | CD3D | human | positive | add | M02243 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 44 | T-REG |  | IKZF2 | human | positive | add | M02244 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 45 | CD8+ TEM/TRM |  | CD3D | human | positive | add | M02245 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 46 | CD8+ TEM/TRM |  | CD8A | human | positive | add | M02246 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 47 | CD8+ TEM/TRM |  | GZMK | human | positive | add | M02247 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 48 | CD8+ TEM/TEMRA |  | CD3D | human | positive | add | M02248 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 49 | CD8+ TEM/TEMRA |  | CD8A | human | positive | add | M02249 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 50 | CD8+ TEM/TEMRA |  | CCL5 | human | positive | add | M02250 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 51 | CD8+ TEM/TEMRA |  | NKG7 | human | positive | add | M02251 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 52 | NK |  | CCL5 | human | positive | add | M02252 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 53 | NK |  | NKG7 | human | positive | add | M02253 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 54 | NK |  | KLRF1 | human | positive | add | M02254 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 55 | MAST |  | KIT | human | positive | add | M02255 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 56 | MAST |  | CPA3 | human | positive | add | M02256 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 57 | resMAC-LYVE1+ |  | LYVE1 | human | positive | matched | M01583 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, Main text Page 8 |
| 10.1101/2025.09.26.678707 | 58 | resMAC-LYVE1+ |  | MRC1 | human | positive | add | M02257 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 59 | resMAC-LYVE1+ |  | C1QA | human | positive | add | M02258 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 60 | resMAC-LYVE1+ |  | MERTK | human | positive | add | M02259 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 8, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 61 | resMAC-LYVE1+ |  | IGF1 | human | positive | add | M02260 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 8, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 62 | resMAC-LYVE1+ |  | PDGFB | human | positive | add | M02261 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 8, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 63 | resMAC-LYVE1+ |  | PDGFC | human | positive | add | M02262 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 8, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 64 | resMAC-HLAIIhi |  | MRC1 | human | positive | add | M02263 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 65 | resMAC-HLAIIhi |  | C1QA | human | positive | matched | M01580 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, ED Figure 6f, Methods Page 41 |
| 10.1101/2025.09.26.678707 | 66 | resMAC-HLAIIhi |  | C1QB | human | positive | add | M02264 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 67 | resMAC-HLAIIhi |  | TGFB1 | human | positive | add | M02265 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 68 | resMAC-HLAIIhi |  | HLA-DRA | human | positive | add | M02266 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 8, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 69 | resMAC-HLAIIhi |  | HLA-DQA1 | human | positive | add | M02267 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 8, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 70 | resMAC-HLAIIhi |  | CD81 | human | positive | add | M02268 | Fig.ED6f 基因是 CD81，已对照标签。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 71 | resMAC-HLAIIhi |  | TMEM176A | human | positive | add | M02269 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 72 | resMAC-HLAIIhi |  | TMEM176B | human | positive | add | M02270 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 73 | resMAC-HLAIIhi |  | CD163 | human | positive | matched | M01581 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 41 |
| 10.1101/2025.09.26.678707 | 74 | resMAC-HLAIIhi |  | STAB1 | human | positive | matched | M01582 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 41 |
| 10.1101/2025.09.26.678707 | 75 | MON |  | FCN1 | human | positive | matched | M01572 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 76 | MON |  | CD300E | human | positive | add | M02271 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 77 | MON |  | CFP | human | positive | add | M02272 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 78 | moMAC-HBEGF+ |  | HBEGF | human | positive | matched | M01568 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, Main text Page 9 |
| 10.1101/2025.09.26.678707 | 79 | moMAC-HBEGF+ |  | AREG | human | positive | matched | M01566 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 80 | moMAC-HBEGF+ |  | PLAUR | human | positive | matched | M01571 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 81 | moMAC-HBEGF+ |  | IL1B | human | positive | matched | M01569 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, 14, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 82 | moMAC-HBEGF+ |  | OSM | human | positive | matched | M01570 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 83 | moMAC-HBEGF+ |  | CXCL8 | human | positive | matched | M01567 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 84 | moMAC-CXCL10+ |  | CXCL10 | human | positive | matched | M01564 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 85 | moMAC-CXCL10+ |  | CXCL9 | human | positive | matched | M01565 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 86 | moMAC-CXCL10+ |  | CCL2 | human | positive | matched | M01563 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 87 | moMAC-CXCL10+ |  | STAT1 | human | positive | add | M02273 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 88 | moMAC-CXCL10+ |  | GBP1 | human | positive | add | M02274 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 89 | moMAC-CXCL10+ |  | GBP5 | human | positive | add | M02275 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 90 | moMAC-CXCL10+ |  | NFKBIA | human | positive | add | M02276 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 91 | moMAC-CXCL10+ |  | IRF1 | human | positive | add | M02277 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 92 | moMAC-CXCL10+ |  | FCGR1A | human | positive | add | M02278 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 93 | moMAC-CXCL10+ |  | CXCL11 | human | positive | add | M02279 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 94 | moMAC-CXCL10+ |  | TNF | human | positive | add | M02280 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 95 | moFAM |  | GPNMB | human | positive | matched | M01561 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 96 | moFAM |  | SPP1 | human | positive | matched | M01562 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h, Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 97 | moFAM |  | TREM2 | human | positive | add | M02281 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main text Page 9, ED Figure 6f |
| 10.1101/2025.09.26.678707 | 98 | moFAM |  | APOE | human | positive | add | M02282 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 99 | moFAM |  | PPARG | human | positive | add | M02283 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 100 | moFAM |  | LIPA | human | positive | add | M02284 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 101 | moFAM |  | CD63 | human | positive | add | M02285 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 102 | moFAM |  | PLA2G7 | human | positive | add | M02286 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 103 | moFAM |  | LGALS3 | human | positive | add | M02287 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 104 | moFAM |  | CD9 | human | positive | add | M02288 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 105 | moFAM |  | CAPG | human | positive | add | M02289 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 106 | moFAM |  | NR1H3 | human | positive | add | M02290 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 107 | moFAM |  | CD68 | human | positive | add | M02291 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 108 | moFAM |  | FABP5 | human | positive | add | M02292 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 109 | moFAM |  | CHIT1 | human | positive | add | M02293 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 110 | moFAM |  | CHI3L1 | human | positive | add | M02294 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 111 | moFAM |  | MMP2 | human | positive | add | M02295 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 112 | moFAM |  | MMP14 | human | positive | add | M02296 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 113 | moFAM |  | MMP9 | human | positive | add | M02297 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 114 | moFAM |  | AXL | human | positive | add | M02298 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：ED Figure 6f |
| 10.1101/2025.09.26.678707 | 115 | moMAC-C3+ |  | C3 | human | positive | add | M02299 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 116 | moMAC-C3+ |  | C1QA | human | positive | add | M02300 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 117 | ncMON |  | TCF7L2 | human | positive | add | M02301 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 118 | ncMON |  | FCGR3A | human | positive | add | M02302 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 119 | cDC2 |  | CLEC10A | human | positive | add | M02303 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 120 | cDC1 |  | WDFY4 | human | positive | add | M02304 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 121 | mDC |  | CCR7 | human | positive | add | M02305 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 122 | pDC |  | IL3RA | human | positive | add | M02306 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 123 | N |  | FCGR3B | human | positive | add | M02307 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 2h |
| 10.1101/2025.09.26.678707 | 124 | PT-S1/S2 |  | HNF4A | human | positive | context_only |  | Fig.3b HNF4A 位于右侧 TF activity 栏，不能当作中间 RNA marker。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 125 | PT-S1/S2 |  | GDA | human | positive | add | M02308 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 126 | PT-S1/S2 |  | PCK1 | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Figure 3e, Main text Page 11, ED Figure 7h-i |
| 10.1101/2025.09.26.678707 | 127 | PT-S3 |  | SLC7A13 | human | positive | add | M02309 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 128 | PT-S3 |  | HNF4A | human | positive | context_only |  | Fig.3b HNF4A 位于右侧 TF activity 栏，不能当作中间 RNA marker。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 129 | PT-S3 |  | PCK1 | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Figure 3e, Main text Page 11, ED Figure 7h-i |
| 10.1101/2025.09.26.678707 | 130 | aPT1 |  | CDH6 | human | positive | add | M02310 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 131 | aPT1 |  | HAVCR1 | human | positive | add | M02311 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 132 | aPT1 |  | SOX4 | human | positive | add | M02312 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 133 | aPT1 |  | PROM1 | human | positive | add | M02313 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 134 | aPT1 |  | GDA | human | positive | add | M02314 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 135 | aPT2 |  | CDH6 | human | positive | matched | M01536 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 136 | aPT2 |  | HAVCR1 | human | positive | matched | M01537 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 137 | aPT2 |  | VCAM1 | human | positive | matched | M01538 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 138 | aPT2 |  | SOX4 | human | positive | add | M02315 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 139 | aPT2 |  | IL32 | human | positive | add | M02316 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 140 | aPT2 |  | ITGB8 | human | positive | add | M02317 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 141 | aPT2 |  | ITGB3 | human | positive | add | M02318 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 142 | aPT2 |  | CCL2 | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Main text Page 14 |
| 10.1101/2025.09.26.678707 | 143 | aPT-S1/S2 |  | CDH6 | human | positive | add | M02319 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 144 | aPT-S1/S2 |  | HAVCR1 | human | positive | add | M02320 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 145 | aPT-S1/S2 |  | SOX4 | human | positive | add | M02321 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 146 | frPT-S1/S2 |  | ITGB8 | human | positive | add | M02322 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 147 | frPT-S1/S2 |  | CDH6 | human | positive | add | M02323 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 148 | frPT-S1/S2 |  | HAVCR1 | human | positive | add | M02324 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 149 | frPT-S1/S2 |  | SOX4 | human | positive | add | M02325 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 150 | frPT-S1/S2 |  | PROM1 | human | positive | add | M02326 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 151 | frPT-S1/S2 |  | ROBO2 | human | positive | add | M02327 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 152 | frPT-S1/S2 |  | MEG3 | human | positive | add | M02328 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 153 | frPT-S1/S2 |  | SPON1 | human | positive | add | M02329 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 154 | frPT-S3 |  | ITGB8 | human | positive | add | M02330 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 155 | frPT-S3 |  | SOX4 | human | positive | add | M02331 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 156 | frPT-S3 |  | PROM1 | human | positive | add | M02332 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 157 | frPT-S3 |  | ROBO2 | human | positive | add | M02333 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 158 | frPT-S3 |  | MEG3 | human | positive | add | M02334 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 159 | frPT-S3 |  | KITLG | human | positive | add | M02335 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 160 | C/M-TAL-A |  | SLC12A1 | human | positive | unresolved |  | Fig.3b 将 C-TAL 与 C/M-TAL 分行，Gemini 合并 C/M 标签后无法唯一确认本配对；保留待源表核定。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 161 | C/M-TAL-A |  | EGF | human | positive | exclude |  | Fig.3b 所示为 EGFR，Gemini 读为 EGF；且不能把 pooled C/M 标签替代图中不同 cortical/medullary 行。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 162 | C/M-TAL-A |  | PHACTR1 | human | positive | unresolved |  | Fig.3b 将 C-TAL 与 C/M-TAL 分行，Gemini 合并 C/M 标签后无法唯一确认本配对；保留待源表核定。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 163 | C/M-TAL-B |  | SLC12A1 | human | positive | unresolved |  | Fig.3b 将 C-TAL 与 C/M-TAL 分行，Gemini 合并 C/M 标签后无法唯一确认本配对；保留待源表核定。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 164 | C/M-TAL-B |  | EGF | human | positive | exclude |  | Fig.3b 所示为 EGFR，Gemini 读为 EGF；且不能把 pooled C/M 标签替代图中不同 cortical/medullary 行。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 165 | C/M-TAL-B |  | CALCR | human | positive | unresolved |  | Fig.3b 将 C-TAL 与 C/M-TAL 分行，Gemini 合并 C/M 标签后无法唯一确认本配对；保留待源表核定。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 166 | C/M-TAL-B |  | LRMDA | human | positive | unresolved |  | Fig.3b 将 C-TAL 与 C/M-TAL 分行，Gemini 合并 C/M 标签后无法唯一确认本配对；保留待源表核定。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 167 | C/M-TAL-B |  | SCN7A | human | positive | unresolved |  | Fig.3b 将 C-TAL 与 C/M-TAL 分行，Gemini 合并 C/M 标签后无法唯一确认本配对；保留待源表核定。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 168 | aTAL1 |  | SLC12A1 | human | positive | add | M02336 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 169 | aTAL1 |  | CREB5 | human | positive | add | M02337 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 170 | aTAL1 |  | ITGA3 | human | positive | add | M02338 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 171 | aTAL1 |  | ITGB6 | human | positive | add | M02339 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 172 | aTAL1 |  | NRP1 | human | positive | add | M02340 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 173 | aTAL1 |  | IL11 | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Main text Page 12 |
| 10.1101/2025.09.26.678707 | 174 | aTAL1 |  | LIF | human | positive | context_only |  | 所引正文为信号配体/代谢/炎症功能讨论，未将该配对列作细胞注释 marker。 定位：Main text Page 12 |
| 10.1101/2025.09.26.678707 | 175 | aTAL2 |  | SLC12A1 | human | positive | add | M02341 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 176 | aTAL2 |  | ITGA3 | human | positive | add | M02342 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 177 | aTAL2 |  | ITGB6 | human | positive | add | M02343 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 178 | aTAL2 |  | NRP1 | human | positive | add | M02344 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 179 | frTAL |  | SLC12A1 | human | positive | add | M02345 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 180 | frTAL |  | ITGB8 | human | positive | matched | M01552 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 181 | frTAL |  | PROM1 | human | positive | matched | M01553 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 182 | frTAL |  | TMPRSS4 | human | positive | matched | M01554 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b, Main text Page 11 |
| 10.1101/2025.09.26.678707 | 183 | frTAL |  | RHEX | human | positive | add | M02346 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Figure 3b |
| 10.1101/2025.09.26.678707 | 184 | PECs |  | CFH | human | positive | matched | M01573 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 41 |
| 10.1101/2025.09.26.678707 | 185 | MD |  | BBOX1 | human | positive | matched | M01560 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Methods Page 41 |
| 10.1126/sciimmunol.adf9988 | 1 | HSCs |  | CD34 | human | positive | add | M02347 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 2 | HSCs |  | SPINK2 | human | positive | matched | M00672 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 5G, Main Text P9 |
| 10.1126/sciimmunol.adf9988 | 3 | HSCs |  | SMIM24 | human | positive | matched | M00671 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5G, Main Text P9 |
| 10.1126/sciimmunol.adf9988 | 4 | LMPP/ELP |  | CD34 | human | positive | matched | M00679 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 5 | LMPP/ELP |  | EBF1 | human | negative | matched | M00680 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 6 | LMPP/ELP |  | SPINK2 | human | positive | add | M02348 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C |
| 10.1126/sciimmunol.adf9988 | 7 | Pre-pro-B |  | EBF1 | human | positive | matched | M00639 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 8 | Pre-pro-B |  | SPINK2 | human | positive | matched | M00641 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 9 | Pre-pro-B |  | VPREB1 | human | positive | matched | M00642 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 10 | Pre-pro-B |  | IL7R | human | positive | matched | M00640 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 11 | Pro-B |  | DNTT | human | positive | matched | M00643 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 3E, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 12 | Pro-B |  | VPREB1 | human | positive | add | M02349 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 3E, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 13 | Pro-B |  | EBF1 | human | positive | add | M02350 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C |
| 10.1126/sciimmunol.adf9988 | 14 | Pro-B |  | RAG1 | human | positive | add | M02351 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 15 | Late pro-B |  | NEIL1 | human | positive | matched | M00638 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 16 | Late pro-B |  | MKI67 | human | negative | matched | M00637 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 17 | Pro-B/Pre-B transition |  | RAG1 | human | positive | matched | M00645 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 18 | Pro-B/Pre-B transition |  | MS4A1 | human | positive | matched | M00644 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 19 | Pro-B/Pre-B transition |  | IGLL1 | human | positive | add | M02352 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C |
| 10.1126/sciimmunol.adf9988 | 20 | Large pre-B |  | IL7R | human | positive | add | M02353 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 21 | Large pre-B |  | MS4A1 | human | positive | add | M02354 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 22 | Large pre-B |  | MKI67 | human | positive | add | M02355 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 23 | Large pre-B |  | BEST3 | human | positive | add | M02356 | Fig.3E 图注明确 large pre-B 为 BEST3+RAG1−，更正 Gemini BEST3−。 定位：Fig 3E, Legend P31 |
| 10.1126/sciimmunol.adf9988 | 24 | κ small pre-B |  | IL7R | human | positive | add | M02357 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 25 | κ small pre-B |  | SPIB | human | positive | add | M02358 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 26 | κ small pre-B |  | MKI67 | human | negative | add | M02359 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 27 | κ small pre-B |  | BEST3 | human | positive | add | M02360 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 3E, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 28 | κ small pre-B |  | RAG1 | human | positive | add | M02361 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 3E, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 29 | κ small pre-B |  | IGKC | human | positive | matched | M00648 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 30 | λ small pre-B |  | IL7R | human | positive | add | M02362 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 31 | λ small pre-B |  | SPIB | human | positive | add | M02363 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 32 | λ small pre-B |  | MKI67 | human | negative | add | M02364 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 33 | λ small pre-B |  | BEST3 | human | positive | add | M02365 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 3E, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 34 | λ small pre-B |  | RAG1 | human | positive | add | M02366 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Fig 3E, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 35 | λ small pre-B |  | IGLC2 | human | positive | matched | M00649 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 36 | λ small pre-B |  | IGLC3 | human | positive | matched | M00650 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 37 | Late pre-B |  | MS4A1 | human | positive | add | M02367 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 38 | Late pre-B |  | IGLL1 | human | positive | matched | M00636 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 39 | Immature B |  | MS4A1 | human | positive | add | M02368 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 40 | Immature B |  | IGHD | human | low | add | M02369 | 保留作者 lo 低表达极性，不转写为 negative。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 41 | Immature B |  | IGHM | human | positive | matched | M00635 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 42 | Immature B |  | VPREB3 | human | positive | add | M02370 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 43 | CD5- Mature B |  | MS4A1 | human | positive | add | M02371 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 44 | CD5- Mature B |  | IGHD | human | positive | add | M02372 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 45 | CD5- Mature B |  | IGHM | human | positive | add | M02373 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 46 | CD5- Mature B |  | VPREB3 | human | low | add | M02374 | 保留作者 lo 低表达极性，不转写为 negative。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 47 | CD5- Mature B |  | CD5 | human | negative | add | M02375 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 48 | CD5+ Mature B |  | CD5 | human | positive | matched | M00634 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 49 | CD5+ Mature B |  | CD27 | human | positive | matched | M00653 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 50 | CD5+ Mature B |  | SPN | human | positive | matched | M00655 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 51 | CD5+ Mature B |  | CCR10 | human | positive | matched | M00652 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 52 | CD5+ Mature B |  | CCL22 | human | positive | matched | M00651 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 53 | CD5+ Mature B |  | PRDM1 | human | negative | add | M02376 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 3C, Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 54 | T progenitors |  | PTCRA | human | positive | matched | M00698 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P7, Fig S6D |
| 10.1126/sciimmunol.adf9988 | 55 | T progenitors |  | RAG1 | human | positive | matched | M00699 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P7, Fig S6D |
| 10.1126/sciimmunol.adf9988 | 56 | T progenitors |  | RAG2 | human | positive | matched | M00700 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P7, Fig S6D |
| 10.1126/sciimmunol.adf9988 | 57 | CD4 T |  | SELL | human | positive | add | M02377 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 58 | CD4 T |  | CD27 | human | positive | add | M02378 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 59 | CD4 T |  | LEF1 | human | positive | add | M02379 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 60 | CD4 T |  | CCR7 | human | positive | add | M02380 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 61 | CD4 T |  | PTPRC | human | positive | add | M02381 | CD45RA/RO 为 PTPRC 蛋白异构体；保留 original_symbol，gene_symbol 统一 PTPRC；不以两者为两个基因。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 62 | CD4 T |  | PTPRC | human | positive | matched | M02381 | CD45RA/RO 为 PTPRC 蛋白异构体；保留 original_symbol，gene_symbol 统一 PTPRC；不以两者为两个基因。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 63 | CD4 T |  | GZMA | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 64 | CD4 T |  | NKG7 | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 65 | CD8 T |  | SELL | human | positive | add | M02382 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 66 | CD8 T |  | CD27 | human | positive | add | M02383 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 67 | CD8 T |  | LEF1 | human | positive | add | M02384 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 68 | CD8 T |  | CCR7 | human | positive | add | M02385 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 69 | CD8 T |  | GZMA | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 70 | CD8 T |  | NKG7 | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Main Text P7 |
| 10.1126/sciimmunol.adf9988 | 71 | CD8 T |  | GZMB | human | positive | unresolved |  | Fig.4B 的 GZMB/PRF1 为低信号，无法批准为 CD8 T 阳性注释 marker。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 72 | CD8 T |  | PRF1 | human | positive | unresolved |  | Fig.4B 的 GZMB/PRF1 为低信号，无法批准为 CD8 T 阳性注释 marker。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 73 | CD8 T |  | PTPRC | human | positive | add | M02386 | CD45RA/RO 为 PTPRC 蛋白异构体；保留 original_symbol，gene_symbol 统一 PTPRC；不以两者为两个基因。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 74 | Treg |  | CCR4 | human | positive | add | M02387 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 75 | Treg |  | PTPRC | human | positive | add | M02388 | CD45RA/RO 为 PTPRC 蛋白异构体；保留 original_symbol，gene_symbol 统一 PTPRC；不以两者为两个基因。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 76 | Treg |  | SELL | human | positive | add | M02389 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 77 | Treg |  | CD27 | human | positive | add | M02390 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 4B |
| 10.1126/sciimmunol.adf9988 | 78 | ILCPs |  | HPN | human | positive | matched | M00673 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P8, Fig S6E |
| 10.1126/sciimmunol.adf9988 | 79 | ILCPs |  | SCN1B | human | positive | matched | M00674 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P8, Fig S6E |
| 10.1126/sciimmunol.adf9988 | 80 | CMPs |  | MPO | human | positive | matched | M00662 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Main Text P9 |
| 10.1126/sciimmunol.adf9988 | 81 | GMPs |  | ELANE | human | positive | matched | M00670 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Main Text P9 |
| 10.1126/sciimmunol.adf9988 | 82 | GMPs |  | MPO | human | positive | add | M02391 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Main Text P9 |
| 10.1126/sciimmunol.adf9988 | 83 | promyelocytes |  | AZU1 | human | positive | matched | M00692 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Legend P35 |
| 10.1126/sciimmunol.adf9988 | 84 | promyelocytes |  | MPO | human | positive | add | M02392 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Legend P35 |
| 10.1126/sciimmunol.adf9988 | 85 | promonocytes |  | S100A8 | human | positive | matched | M00691 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Legend P35 |
| 10.1126/sciimmunol.adf9988 | 86 | promonocytes |  | MPO | human | positive | add | M02393 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 5H, Legend P35 |
| 10.1126/sciimmunol.adf9988 | 87 | monocytes | S100A12hi CD14+ | CD14 | human | positive | matched | M00686 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P8-9, Fig 5F |
| 10.1126/sciimmunol.adf9988 | 88 | monocytes | S100A12hi CD14+ | S100A12 | human | positive | matched | M00687 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P8-9, Fig 5F, Fig 7F |
| 10.1126/sciimmunol.adf9988 | 89 | monocytes | S100A12hi CD14+ | CCR2 | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Fig 5F |
| 10.1126/sciimmunol.adf9988 | 90 | monocytes | S100A12hi CD14+ | IL6 | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Fig 5F |
| 10.1126/sciimmunol.adf9988 | 91 | S100A12-lo CD14+ mono |  | CD14 | human | positive | add | M02394 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 2A, Main Text P8 |
| 10.1126/sciimmunol.adf9988 | 92 | CD16+ mono |  | FCGR3A | human | positive | add | M02395 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 2A, Main Text P8 |
| 10.1126/sciimmunol.adf9988 | 93 | neutrophils/monocytes |  | S100A9 | human | positive | matched | M00690 | Fig.7F 为 neutrophils/monocytes 联合标记，不强行限定 neutrophil。 定位：Fig 7F, Main Text P11 |
| 10.1126/sciimmunol.adf9988 | 94 | neutrophils/monocytes |  | S100A12 | human | positive | add | M02396 | Fig.7F 为 neutrophils/monocytes 联合标记，不强行限定 neutrophil。 定位：Fig 7F, Main Text P11 |
| 10.1126/sciimmunol.adf9988 | 95 | Neutrophil |  | IL1B | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Fig 7B, Fig 7C, Fig 7F |
| 10.1126/sciimmunol.adf9988 | 96 | DC2 cells |  | CD1C | human | positive | matched | M00665 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P11, Fig 7D |
| 10.1126/sciimmunol.adf9988 | 97 | DC2 cells |  | IL1B | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Main Text P11, Fig 7B-C |
| 10.1126/sciimmunol.adf9988 | 98 | macrophages |  | CD68 | human | positive | add | M02397 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P9, Fig 5I |
| 10.1126/sciimmunol.adf9988 | 99 | macrophages |  | MRC1 | human | positive | matched | M00682 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P9, P11, Fig 7E |
| 10.1126/sciimmunol.adf9988 | 100 | interstitial macrophages |  | CD14 | human | positive | matched | M00676 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P9, Fig S8C |
| 10.1126/sciimmunol.adf9988 | 101 | interstitial macrophages |  | CD36 | human | positive | matched | M00677 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P9, Fig S8C |
| 10.1126/sciimmunol.adf9988 | 102 | macrophages |  | IL10 | human | positive | context_only |  | 此项仅用于细胞毒性/细胞因子/分化功能表达讨论，所引位置未建立该细胞身份 marker 关系。 定位：Main Text P9, Fig 5F |
| 10.1126/sciimmunol.adf9988 | 103 | macrophages | APOE+ | APOE | human | positive | matched | M00684 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 2A, Main Text P9 |
| 10.1126/sciimmunol.adf9988 | 104 | macrophages | CXCL9+ | CXCL9 | human | positive | unresolved |  | 正文 CXCL2+ 与图中 CXCL9+ 巨噬群标签不一致，暂不据 Gemini 另立新配对。 定位：Fig 2A, Fig 5C |
| 10.1126/sciimmunol.adf9988 | 105 | distal epithelial tip progenitors |  | SOX9 | human | positive | matched | M00667 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P9, P10, Fig 6A, 7D-E |
| 10.1126/sciimmunol.adf9988 | 106 | epithelial cells |  | SOX2 | human | negative | exclude |  | 正文明确 pseudoglandular distal tip 共表达 SOX2 与 SOX9，SOX2 阴性配对错误。 定位：Main Text P10, Fig 7G |
| 10.1126/sciimmunol.adf9988 | 107 | epithelial cells |  | EPCAM | human | positive | unresolved |  | 所引 EpCAM 为泛上皮染色，未证明应收窄为 distal tip 亚群；保留现有泛上皮记录。 定位：Fig 7A, Main Text P6 |
| 10.1126/sciimmunol.adf9988 | 108 | basal cells |  | SOX2 | human | positive | add | M02398 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10-11, Fig 7G |
| 10.1126/sciimmunol.adf9988 | 109 | basal cells |  | TP63 | human | positive | matched | M00657 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10-11, Fig 6H-I, 7G |
| 10.1126/sciimmunol.adf9988 | 110 | basal cells |  | KRT5 | human | positive | matched | M00656 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10-11, Fig 6J-K, 7G |
| 10.1126/sciimmunol.adf9988 | 111 | ciliated cells |  | FOXJ1 | human | positive | matched | M00661 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10 |
| 10.1126/sciimmunol.adf9988 | 112 | secretory cells |  | SCGB3A1 | human | positive | matched | M00694 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10 |
| 10.1126/sciimmunol.adf9988 | 113 | secretory cells |  | SCGB3A2 | human | positive | matched | M00695 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10 |
| 10.1126/sciimmunol.adf9988 | 114 | secretory cells |  | MUC5AC | human | positive | matched | M00693 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10 |
| 10.1126/sciimmunol.adf9988 | 115 | secretory cells |  | MUC5B | human | positive | add | M02399 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text P10 |
| 10.1126/sciimmunol.adf9988 | 116 | CD31+ vasculature |  | PECAM1 | human | positive | matched | M00658 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig 1C, Fig 3E, Fig 5I, Main Text P5 |
| 10.1126/sciimmunol.adf9988 | 117 | TNC+ fibro |  | TNC | human | positive | unresolved |  | 所引 Fig.2A/正文尚未核实 TNC+ fibro 定义，不能只按标签猜配基因。 定位：Fig 2A |
| 10.64898/2025.12.18.695268 | 1 | basal urothelial cells |  | KRT5 | human | positive | add | M02400 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 1-2; Fig. S1A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 2 | basal urothelial cells |  | KRT13 | human | positive | matched | M01080 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 1-2; Fig. 1D; Fig. S1A |
| 10.64898/2025.12.18.695268 | 3 | basal urothelial cells |  | ADAMTS9 | human | positive | matched | M01079 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 1-2; Fig. S1A |
| 10.64898/2025.12.18.695268 | 4 | basal urothelial cells |  | DST | human | positive | context_only |  | 原文讨论具体 poly(A) isoform（P1/P2）使用或富集，不能丢失异构体层级后当作通用 gene marker。 定位：Main Text Page 5 lines 7-12; Fig. 4A-D |
| 10.64898/2025.12.18.695268 | 5 | basal urothelial cells |  | MCCC2 | human | positive | context_only |  | 原文讨论具体 poly(A) isoform（P1/P2）使用或富集，不能丢失异构体层级后当作通用 gene marker。 定位：Main Text Page 5 lines 13-16; Fig. 4C-D |
| 10.64898/2025.12.18.695268 | 6 | Intermediate |  | KRT13 | human | positive | add | M02401 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 2; Fig. 1D; Fig. S1A |
| 10.64898/2025.12.18.695268 | 7 | Intermediate |  | ABCC3 | human | positive | matched | M01081 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 2; Fig. S1A |
| 10.64898/2025.12.18.695268 | 8 | Intermediate |  | UPK1A | human | positive | add | M02402 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 9 | Intermediate |  | KRT19 | human | positive | add | M02403 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S1A |
| 10.64898/2025.12.18.695268 | 10 | umbrella cells |  | UPK1A | human | positive | matched | M01083 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 1-2; Fig. 1D; Fig. S1A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 11 | umbrella cells |  | UPK3A | human | positive | matched | M01076 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 1-2; Fig. 1D; Fig. S1A; Fig. S5A |
| 10.64898/2025.12.18.695268 | 12 | urothelial cells |  | SHH | human | positive | add | M02404 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 13 | urothelial cells |  | KRT7 | human | positive | add | M02405 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 14 | urothelial cells |  | KRT13 | human | positive | add | M02406 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 15 | urothelial cells |  | UPK1A | human | positive | add | M02407 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 16 | urothelial cells |  | UPK1B | human | positive | add | M02408 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 17 | urothelial cells |  | UPK3A | human | positive | matched | M01078 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 18 | urothelial cells |  | UPK3B | human | positive | add | M02409 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D dotplot |
| 10.64898/2025.12.18.695268 | 19 | FB1 |  | PDGFRA | human | positive | add | M02410 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 20 | FB1 |  | C7 | human | positive | add | M02411 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 21 | FB2 |  | PDGFRA | human | positive | add | M02412 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 22 | FB2 |  | C7 | human | positive | add | M02413 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 23 | FB3 |  | PDGFRA | human | positive | add | M02414 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 24 | FB3 |  | C7 | human | positive | add | M02415 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 25 | FB3 |  | PTCH1 | human | positive | add | M02416 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 26 | FB4 |  | PDGFRA | human | positive | add | M02417 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 27 | FB4 |  | C7 | human | positive | add | M02418 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 28 | FB4 |  | PTCH1 | human | positive | add | M02419 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 29 | FB4 |  | LAMC3 | human | positive | add | M02420 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 30 | FB4 |  | HHIP | human | positive | add | M02421 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 31 | FB4 |  | RBFOX1 | human | positive | add | M02422 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 32 | FB5 |  | PDGFRA | human | positive | add | M02423 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 33 | FB5 |  | C7 | human | positive | add | M02424 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 34 | FB5 |  | CXCL14 | human | positive | add | M02425 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 35 | FB6 |  | PDGFRA | human | positive | add | M02426 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 36 | FB6 |  | C7 | human | positive | add | M02427 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 37 | FB6 |  | NGFR | human | positive | add | M02428 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 38 | smooth muscle cells |  | ACTA2 | human | positive | matched | M01068 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 6; Fig. S1B; Fig. 6C |
| 10.64898/2025.12.18.695268 | 39 | smooth muscle cells |  | MYLK | human | positive | matched | M01069 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 6; Fig. 1D |
| 10.64898/2025.12.18.695268 | 40 | smooth muscle cells |  | MYH11 | human | positive | add | M02429 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 41 | vascular smooth muscle cells |  | RGS5 | human | positive | matched | M01070 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 6; Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 42 | vascular smooth muscle cells |  | MYLK | human | positive | add | M02430 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 43 | vascular smooth muscle cells |  | PDGFRB | human | positive | add | M02431 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 44 | vascular smooth muscle cells |  | CSPG4 | human | positive | add | M02432 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 45 | vascular smooth muscle cells |  | MYH11 | human | positive | add | M02433 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 46 | pericytes |  | CSPG4 | human | positive | matched | M01065 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 6; Fig. 1D |
| 10.64898/2025.12.18.695268 | 47 | pericytes |  | RGS5 | human | positive | add | M02434 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 48 | pericytes |  | MYLK | human | positive | add | M02435 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 49 | pericytes |  | PDGFRB | human | positive | add | M02436 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 50 | pericytes |  | MYH11 | human | positive | add | M02437 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 51 | arterial endothelial cells |  | GJA5 | human | positive | matched | M01041 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 7; Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 52 | arterial endothelial cells |  | PECAM1 | human | positive | matched | M01042 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S3C |
| 10.64898/2025.12.18.695268 | 53 | arterial endothelial cells |  | VWF | human | positive | add | M02438 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 54 | arterial endothelial cells |  | CXCL12 | human | positive | context_only |  | 原文讨论具体 poly(A) isoform（P1/P2）使用或富集，不能丢失异构体层级后当作通用 gene marker。 定位：Main Text Page 5 lines 17-21; Fig. 4E-G |
| 10.64898/2025.12.18.695268 | 55 | venous endothelial cells |  | FLT1 | human | positive | matched | M01048 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 7; Fig. 1D; Fig. S3D |
| 10.64898/2025.12.18.695268 | 56 | venous endothelial cells |  | PECAM1 | human | positive | matched | M01086 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S3C |
| 10.64898/2025.12.18.695268 | 57 | venous endothelial cells |  | VWF | human | positive | add | M02439 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 58 | lymphatic endothelial cells |  | MMRN1 | human | positive | matched | M01046 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 7-8; Fig. 1D |
| 10.64898/2025.12.18.695268 | 59 | lymphatic endothelial cells |  | TFF3 | human | positive | matched | M01047 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 7-8; Fig. 1D |
| 10.64898/2025.12.18.695268 | 60 | lymphatic endothelial cells |  | LYVE1 | human | positive | add | M02440 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S1B; Fig. S3C |
| 10.64898/2025.12.18.695268 | 61 | lymphatic endothelial cells |  | PECAM1 | human | positive | add | M02441 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S3C |
| 10.64898/2025.12.18.695268 | 62 | Schwann cells |  | NRXN1 | human | positive | matched | M00058 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 8; Fig. 1D; Fig. S3C; Fig. S3E |
| 10.64898/2025.12.18.695268 | 63 | Schwann cells |  | XKR4 | human | positive | matched | M00059 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 line 8; Fig. 1D; Fig. S1B |
| 10.64898/2025.12.18.695268 | 64 | Schwann cells |  | NGFR | human | positive | exclude |  | Fig.S3E 图注明确 NGFR 为 xFB-7 marker，神经束中 Schwann 标记是 NRXN1；Gemini 配错细胞。 定位：Fig. S3E |
| 10.64898/2025.12.18.695268 | 65 | adipocytes |  | FABP3 | human | positive | matched | M01040 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 8-9; Fig. 1D |
| 10.64898/2025.12.18.695268 | 66 | adipocytes |  | ADIPOQ | human | positive | matched | M01039 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 3 lines 8-9; Fig. 1D |
| 10.64898/2025.12.18.695268 | 67 | adipocytes |  | FABP4 | human | positive | add | M02442 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S1B |
| 10.64898/2025.12.18.695268 | 68 | macrophages |  | C1QA | human | positive | add | M02443 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1C |
| 10.64898/2025.12.18.695268 | 69 | macrophages |  | C1QB | human | positive | add | M02444 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 70 | macrophages |  | C1QC | human | positive | add | M02445 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 71 | macrophages |  | PTPRC | human | positive | add | M02446 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 72 | DC |  | CIITA | human | positive | add | M02447 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1C |
| 10.64898/2025.12.18.695268 | 73 | DC |  | C1QA | human | positive | add | M02448 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 74 | DC |  | C1QB | human | positive | add | M02449 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 75 | DC |  | C1QC | human | positive | add | M02450 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 76 | DC |  | PTPRC | human | positive | add | M02451 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 77 | Monocyte |  | S100A8 | human | positive | add | M02452 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 78 | Monocyte |  | S100A9 | human | positive | add | M02453 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 79 | Monocyte |  | C1QA | human | positive | add | M02454 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 80 | Monocyte |  | C1QB | human | positive | add | M02455 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 81 | Monocyte |  | C1QC | human | positive | add | M02456 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 82 | Monocyte |  | PTPRC | human | positive | add | M02457 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 83 | Plasma_B |  | JCHAIN | human | positive | add | M02458 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S3C |
| 10.64898/2025.12.18.695268 | 84 | Plasma_B |  | FCRL1 | human | positive | add | M02459 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 85 | Plasma_B |  | PTPRC | human | positive | add | M02460 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 86 | T cells |  | CD247 | human | positive | add | M02461 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 87 | T cells |  | IL7R | human | positive | add | M02462 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1C |
| 10.64898/2025.12.18.695268 | 88 | T cells |  | CD8A | human | positive | add | M02463 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S1C |
| 10.64898/2025.12.18.695268 | 89 | T cells |  | PTPRC | human | positive | add | M02464 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 90 | NK cells |  | CD247 | human | positive | add | M02465 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 91 | NK cells |  | IL7R | human | positive | add | M02466 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1C |
| 10.64898/2025.12.18.695268 | 92 | NK cells |  | KLRD1 | human | positive | add | M02467 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S1C |
| 10.64898/2025.12.18.695268 | 93 | NK cells |  | PTPRC | human | positive | add | M02468 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 94 | Mast cells |  | KIT | human | positive | add | M02469 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D; Fig. S1C |
| 10.64898/2025.12.18.695268 | 95 | Mast cells |  | TPSAB1 | human | positive | add | M02470 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 1D |
| 10.64898/2025.12.18.695268 | 96 | Mast cells |  | PTPRC | human | positive | add | M02471 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 97 | xFB-0 |  | HHIP | human | positive | unresolved |  | 正文 xFB-0 HHIP+/xFB-5 HHIP− 与 Fig.3C 图注 xFB-5(HHIP)冲突；保留原始证据，暂不批准极性。 定位：Main Text Page 6 lines 33-36; Fig. 5F; Fig. 6B |
| 10.64898/2025.12.18.695268 | 98 | xFB-0 |  | PDGFRA | human | positive | add | M02472 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5F; Fig. S3C |
| 10.64898/2025.12.18.695268 | 99 | xFB-0 |  | DCN | human | positive | add | M02473 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 100 | xFB-1 |  | PDGFRA | human | positive | add | M02474 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 5 lines 36-37; Fig. 5F; Fig. S3C |
| 10.64898/2025.12.18.695268 | 101 | xFB-1 |  | DCN | human | positive | add | M02475 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 102 | xFB-2 |  | NQO1 | human | positive | context_only |  | 原文讨论具体 poly(A) isoform（P1/P2）使用或富集，不能丢失异构体层级后当作通用 gene marker。 定位：Main Text Page 6 lines 16-17; Fig. S5C |
| 10.64898/2025.12.18.695268 | 103 | xFB-2 |  | PDGFRA | human | positive | add | M02476 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5F; Fig. S3C |
| 10.64898/2025.12.18.695268 | 104 | xFB-2 |  | DCN | human | positive | add | M02477 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 105 | xFB-3 |  | CXCL12 | human | positive | context_only |  | 原文讨论具体 poly(A) isoform（P1/P2）使用或富集，不能丢失异构体层级后当作通用 gene marker。 定位：Main Text Page 6 lines 13-16; Fig. 5F; Fig. S5B |
| 10.64898/2025.12.18.695268 | 106 | xFB-3 |  | PDGFRA | human | positive | add | M02478 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5F; Fig. S3C |
| 10.64898/2025.12.18.695268 | 107 | xFB-3 |  | DCN | human | positive | add | M02479 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 108 | xFB-4 |  | COL4A4 | human | positive | unresolved |  | 所引图未显示该 xFB 亚群的独立 gene–cell 对，不能从空间位置/亚群功能推断。 定位：Fig. S5A |
| 10.64898/2025.12.18.695268 | 109 | xFB-4 |  | PCOLCE2 | human | positive | unresolved |  | 所引图未显示该 xFB 亚群的独立 gene–cell 对，不能从空间位置/亚群功能推断。 定位：Fig. S5A |
| 10.64898/2025.12.18.695268 | 110 | xFB-4 |  | PDGFRA | human | positive | add | M02480 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5F; Fig. S3C |
| 10.64898/2025.12.18.695268 | 111 | xFB-4 |  | DCN | human | positive | add | M02481 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 112 | xFB-5 |  | HHIP | human | positive | unresolved |  | 正文 xFB-0 HHIP+/xFB-5 HHIP− 与 Fig.3C 图注 xFB-5(HHIP)冲突；保留原始证据，暂不批准极性。 定位：Main Text Page 6 lines 11-16; Fig. 5F; Fig. 6B |
| 10.64898/2025.12.18.695268 | 113 | xFB-5 |  | CXCL12 | human | positive | context_only |  | 原文讨论具体 poly(A) isoform（P1/P2）使用或富集，不能丢失异构体层级后当作通用 gene marker。 定位：Main Text Page 6 lines 13-16; Fig. 5F; Fig. S5B |
| 10.64898/2025.12.18.695268 | 114 | xFB-5 |  | PDGFRA | human | positive | add | M02482 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5F; Fig. S3C |
| 10.64898/2025.12.18.695268 | 115 | xFB-5 |  | DCN | human | positive | add | M02483 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 116 | xFB-6 |  | ACTA2 | human | positive | unresolved |  | 所引图未显示该 xFB 亚群的独立 gene–cell 对，不能从空间位置/亚群功能推断。 定位：Main Text Page 6 lines 37-38; Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 117 | xFB-6 |  | MYH11 | human | positive | add | M02484 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 118 | xFB-6 |  | DCN | human | positive | add | M02485 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 6C; Fig. S3C |
| 10.64898/2025.12.18.695268 | 119 | xFB-7 |  | DCN | human | positive | matched | M01055 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 6 lines 39-40; Fig. S3C; Fig. S3E |
| 10.64898/2025.12.18.695268 | 120 | xFB-7 |  | PDGFRA | human | positive | add | M02486 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 121 | xFB-8 |  | DCN | human | positive | add | M02487 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 6 lines 38-39; Fig. 6A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 122 | xFB-8 |  | PDGFRA | human | positive | add | M02488 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 123 | xFB-9 |  | CXCL14 | human | positive | matched | M01058 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Main Text Page 6 lines 38-39; Fig. S3D |
| 10.64898/2025.12.18.695268 | 124 | xFB-9 |  | DCN | human | positive | add | M02489 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C; Fig. S3D |
| 10.64898/2025.12.18.695268 | 125 | xFB-9 |  | PDGFRA | human | positive | add | M02490 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 126 | Capillary |  | PECAM1 | human | positive | add | M02491 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 127 | Uro_MKI67 |  | MKI67 | human | positive | matched | M01082 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 128 | Uro_MKI67 |  | UPK1A | human | positive | add | M02492 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 129 | MP_MS4A7 |  | MS4A7 | human | positive | matched | M01061 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 130 | MP_MS4A7 |  | PTPRC | human | positive | add | M02493 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |
| 10.64898/2025.12.18.695268 | 131 | MP_LYVE1 |  | LYVE1 | human | positive | matched | M01060 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. 5A; Fig. S3C |
| 10.64898/2025.12.18.695268 | 132 | MP_LYVE1 |  | PTPRC | human | positive | add | M02494 | 对照现有正文及所引图/图注，确认作者 marker 与细胞关系。 定位：Fig. S3C |

## 原总表逐条处置

| marker_id | 论文 | 处理 | 理由 |
|---|---|---|---|
| M00131 | 10.1038/s41586-020-2922-4 | correct | 原图 Extended Data Fig.4b 明确 Mouse AlvF，更正物种与原文符号。 |
| M00192 | 10.1038/s41586-020-2922-4 | correct | Fig.4d 的 elastin 验证明确来自 mouse，更正物种；保留原文 elastin 蛋白标识。 |
| M01890 | 10.1038/s41586-020-2922-4 | correct | 正文和图12g图内为 BPIFB1；图注 BPIFBP1 为拼写不一致，原始写法保留。 |
| M00151 | 10.1038/s41586-020-2922-4 | correct | 图5a 明确 B–MS4A1 阳性，用图证补足原抗体表 unknown。 |
| M00052 | 10.1038/s44318-024-00328-6 | correct | Fig.EV2H 与 Fig.1I 将 ASCL1 对应 NE progenitor。 |
| M00053 | 10.1038/s44318-024-00328-6 | correct | Fig.EV2I 对应 differentiating pulmonary NE。 |
| M00054 | 10.1038/s44318-024-00328-6 | correct | Fig.EV2I 对应 differentiating pulmonary NE。 |
| M00615 | 10.1038/s44318-024-00328-6 | correct | Fig.1K 对应 CXCL+ AT2-like 子群。 |
| M01257 | 10.1101/2024.10.23.619925 | correct | 原文 low 为低表达，和 negative 不等价。 |
| M01263 | 10.1101/2024.10.23.619925 | correct | 原文 low 为低表达，和 negative 不等价。 |
| M01267 | 10.1101/2024.10.23.619925 | correct | 原文 low 为低表达，和 negative 不等价。 |
| M00065 | 10.1101/2024.10.23.619925 | context_only | 现有依据仅 Fig.1F top DEG；与新候选使用同一证据口径，不能凭高表达/历史批准当正式 marker。 |
| M00066 | 10.1101/2024.10.23.619925 | context_only | 现有依据仅 Fig.1F top DEG；与新候选使用同一证据口径，不能凭高表达/历史批准当正式 marker。 |
| M00124 | 10.1038/s41586-020-2922-4 | unresolved | Extended Data Fig.4f 图为 MyoF ASPN+/COX4I2−，但图注措辞将 COX4I2 连到 fibromyocyte/ASM；图文冲突，不批准当前 positive。 |
| M00183 | 10.1038/s41586-020-2922-4 | unresolved | Extended Data Fig.4f 图为 MyoF ASPN+/COX4I2−，但图注措辞将 COX4I2 连到 fibromyocyte/ASM；图文冲突，不批准当前 positive。 |
| M00203 | 10.1038/s41586-020-2922-4 | exclude | 与 natural killer cells–NCAM1 的已知阳性分选记录重复；原 unknown 抗体面板证据保存在本裁决档案。 |
| M00605 | 10.1038/s44318-024-00328-6 | context_only | CDH1 在本文为上皮极性/连接验证，不能据此作为 AT2 身份 marker；原始记录保留。 |
| M00611 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00610 |
| M00612 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00604 |
| M00613 | 10.1038/s44318-024-00328-6 | context_only | CDH1 在本文为上皮极性/连接验证，不能据此作为 AT2 身份 marker；原始记录保留。 |
| M00616 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00606 |
| M00617 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00607 |
| M00619 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00608 |
| M00622 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00609 |
| M00623 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00610 |
| M00628 | 10.1038/s44318-024-00328-6 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00610 |
| M00654 | 10.1126/sciimmunol.adf9988 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00634 |
| M01044 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01041 |
| M01045 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01042 |
| M01051 | 10.64898/2025.12.18.695268 | unresolved | xFB-0/xFB-5 的 HHIP 正负在正文与 Fig.3C 图注冲突；暂移出正式表并完整保留未决证据。 |
| M01053 | 10.64898/2025.12.18.695268 | unresolved | xFB-0/xFB-5 的 HHIP 正负在正文与 Fig.3C 图注冲突；暂移出正式表并完整保留未决证据。 |
| M01062 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01052 |
| M01063 | 10.64898/2025.12.18.695268 | unresolved | xFB-0/xFB-5 的 HHIP 正负在正文与 Fig.3C 图注冲突；暂移出正式表并完整保留未决证据。 |
| M01067 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M00058 |
| M01084 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01070 |
| M01085 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01048 |
| M01087 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01057 |
| M01088 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01056 |
| M01089 | 10.64898/2025.12.18.695268 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01058 |
| M01242 | 10.1101/2024.10.23.619925 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01237 |
| M01244 | 10.1101/2024.10.23.619925 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01238 |
| M01290 | 10.1101/2025.01.17.633590 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01279 |
| M01291 | 10.1101/2025.01.17.633590 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01280 |
| M01298 | 10.1101/2025.01.17.633590 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01285 |
| M01299 | 10.1101/2025.01.17.633590 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01281 |
| M01300 | 10.1101/2025.01.17.633590 | deduplicate | 同义标签同一 gene–cell–物种–极性，合并到 M01284 |
| M00011 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00012 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00058 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M00059 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M00067 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M00116 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00117 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00118 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00119 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00120 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00123 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00125 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00126 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00127 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00128 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00129 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00132 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00133 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00134 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00135 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00136 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00137 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00138 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00139 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00140 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00142 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00143 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00144 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00145 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00146 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00148 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00149 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00153 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00154 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00157 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00158 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00161 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00162 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00163 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00168 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00174 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00175 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00176 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00177 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00178 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00179 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00180 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00181 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00182 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00184 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00185 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00186 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00187 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00188 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00189 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00190 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00191 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00193 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00194 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00195 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00196 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00199 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00207 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00208 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00209 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00210 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00212 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00213 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00214 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00215 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00216 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00222 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00223 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00224 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00225 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00226 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M00409 | 10.1016/j.jcf.2025.01.016 | matched | 双表对应一致。 |
| M00410 | 10.1016/j.jcf.2025.01.016 | matched | 双表对应一致。 |
| M00598 | 10.1016/j.healun.2026.02.1666 | matched | 双表对应一致。 |
| M00599 | 10.1016/j.healun.2026.02.1666 | matched | 双表对应一致。 |
| M00600 | 10.1016/j.healun.2026.02.1666 | matched | 双表对应一致。 |
| M00601 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00602 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00603 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00604 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00606 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00607 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00608 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00609 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00610 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00614 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00618 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00620 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00621 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00624 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00625 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00626 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00627 | 10.1038/s44318-024-00328-6 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00629 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00630 | 10.1038/s44318-024-00328-6 | matched | 双表对应一致。 |
| M00631 | 10.1038/s44318-024-00328-6 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00632 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00633 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00634 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00635 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00636 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00637 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00638 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00639 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00640 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00641 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00642 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00643 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00644 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00645 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00646 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00647 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00648 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00649 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00650 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00651 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00652 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00653 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00655 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00656 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00657 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00658 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00659 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00660 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00661 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00662 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00663 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00664 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00665 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00666 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00667 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00668 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00669 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00670 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00671 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00672 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00673 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00674 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00675 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00676 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00677 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00678 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00679 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00680 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00681 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00682 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00683 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00684 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00685 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00686 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00687 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00688 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00689 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00690 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00691 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00692 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00693 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00694 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00695 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00696 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00697 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M00698 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00699 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00700 | 10.1126/sciimmunol.adf9988 | matched | 双表对应一致。 |
| M00701 | 10.1126/sciimmunol.adf9988 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01039 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01040 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01041 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01042 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01043 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01046 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01047 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01048 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01049 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01050 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01052 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01054 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01055 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01056 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01057 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01058 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01059 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01060 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01061 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01064 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01065 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01066 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01068 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01069 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01070 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01071 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01072 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01073 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01074 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01075 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01076 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01077 | 10.64898/2025.12.18.695268 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01078 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01079 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01080 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01081 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01082 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01083 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01086 | 10.64898/2025.12.18.695268 | matched | 双表对应一致。 |
| M01224 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01225 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01226 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01227 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01228 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01229 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01230 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01231 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01232 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01233 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01234 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01235 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01236 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01237 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01238 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01239 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01240 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01241 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01243 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01245 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01246 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01247 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01248 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01249 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01250 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01251 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01252 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01253 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01254 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01255 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01256 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01258 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01259 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01260 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01261 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01262 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01264 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01265 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01266 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01268 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01269 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01270 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01271 | 10.1101/2024.10.23.619925 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01272 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01273 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01274 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01275 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01276 | 10.1101/2024.10.23.619925 | matched | 双表对应一致。 |
| M01277 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01278 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01279 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01280 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01281 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01282 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01283 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01284 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01285 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01286 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01287 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01288 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01289 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01292 | 10.1101/2025.01.17.633590 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01293 | 10.1101/2025.01.17.633590 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01294 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01295 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01296 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01297 | 10.1101/2025.01.17.633590 | matched | 双表对应一致。 |
| M01301 | 10.1016/j.cell.2017.09.004 | matched | 双表对应一致。 |
| M01302 | 10.1016/j.cell.2017.09.004 | matched | 双表对应一致。 |
| M01536 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01537 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01538 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01539 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01540 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01541 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01542 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01543 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01544 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01545 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01546 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01547 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01548 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01549 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01550 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01551 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01552 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01553 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01554 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01555 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01556 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01557 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01558 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01559 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01560 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01561 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01562 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01563 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01564 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01565 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01566 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01567 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01568 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01569 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01570 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01571 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01572 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01573 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01574 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01575 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01576 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01577 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01578 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01579 | 10.1101/2025.09.26.678707 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01580 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01581 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01582 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01583 | 10.1101/2025.09.26.678707 | matched | 双表对应一致。 |
| M01886 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M01887 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01888 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M01889 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M01891 | 10.1038/s41586-020-2922-4 | matched | 双表对应一致。 |
| M01892 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
| M01893 | 10.1038/s41586-020-2922-4 | retain | Gemini 未覆盖此独立粒度/方法证据，保留现有记录与来源；未将缺席视为否决。 |
