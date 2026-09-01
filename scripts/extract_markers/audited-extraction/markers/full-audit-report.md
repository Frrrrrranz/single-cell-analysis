# 40 篇 Marker 全量审核汇总报告（2026-08-30）

审核模型与规则：audit_markers_v1 提示词 + run_full_audit.py 自动降级规则（citation 词元覆盖率阈值 0.72）。

## 文章状态统计

- 审核论文数：40
- pass: 0
- corrected: 27
- no_formal_target_marker: 8
- unresolved: 5
- 修正版正式 Marker（include，已去重）：87
- 旧总表移除记录（40 篇范围内未获终审 include）：78
- 旧总表保留历史行（不在 40 篇审计范围）：10

## 逐篇结果

| task | paper_id | 目标范围 | 状态 | include | context | exclude | unresolved |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOI_10.1038_s41586-021-03710-0 | — | no_formal_target_marker | 0 | 0 | 16 | 0 |
| 4 | DOI_10.1038_s41586-020-2922-4 | L4:Pulmonary neuroendocrine cell | corrected | 2 | 0 | 113 | 0 |
| 5 | DOI_10.1038_s41588-022-01243-4 | L2:Myelinating Schwann cell/Non-myelinating Schwann cell / L4:Neuroendocrine cell | corrected | 13 | 0 | 80 | 1 |
| 6 | DOI_10.1164_rccm.202207-1384oc | L2:Schwann cell / L4:Pulmonary neuroendocrine cell | corrected | 3 | 0 | 45 | 0 |
| 7 | DOI_10.1038_s41586-021-04345-x | L4:Neuroendocrine cell | corrected | 2 | 0 | 82 | 0 |
| 8 | DOI_10.1016_j.jcf.2025.01.016 | L4:Pulmonary neuroendocrine cell | corrected | 0 | 0 | 4 | 0 |
| 9 | DOI_10.1016_j.cell.2022.11.005 | L2:Schwann cell/Schwann cell precursor/Immature Schwann cell / L4:Pulmonary neuroendocrine cell | corrected | 20 | 0 | 207 | 0 |
| 10 | DOI_10.1016_j.healun.2026.02.1666 | L4:Neuroendocrine cell | corrected | 0 | 0 | 5 | 0 |
| 11 | DOI_10.7554_elife.62522 | L4:Pulmonary neuroendocrine cell | corrected | 1 | 0 | 1 | 0 |
| 12 | DOI_10.1038_s44318-024-00328-6 | L4:Pulmonary neuroendocrine cell | corrected | 3 | 0 | 33 | 0 |
| 13 | DOI_10.1126_sciimmunol.adf9988 | L4:Pulmonary neuroendocrine cell | no_formal_target_marker | 0 | 0 | 94 | 0 |
| 14 | DOI_10.1038_s41591-023-02327-2 | L4:Pulmonary neuroendocrine cell | corrected | 1 | 0 | 45 | 0 |
| 15 | DOI_10.1038_s41467-023-40173-5 | L4:Pulmonary neuroendocrine cell | corrected | 0 | 0 | 41 | 0 |
| 16 | DOI_10.1038_s41588-024-01702-0 | L4:Pulmonary neuroendocrine cell | no_formal_target_marker | 0 | 0 | 19 | 0 |
| 17 | DOI_10.1038_s41586-021-03569-1 | — | unresolved | 0 | 0 | 28 | 0 |
| 18 | DOI_10.1016_j.stem.2022.11.013 | L4:Pulmonary neuroendocrine cell | unresolved | 0 | 0 | 80 | 0 |
| 20 | DOI_10.1016_j.cell.2021.07.023 | L4:Enteroendocrine cell | corrected | 2 | 0 | 150 | 0 |
| 21 | DOI_10.64898_2025.12.18.695268 | L2:Schwann cell | corrected | 3 | 1 | 61 | 0 |
| 22 | DOI_10.1126_science.aat5031 | — | no_formal_target_marker | 0 | 0 | 16 | 0 |
| 23 | DOI_10.1016_j.isci.2024.111628 | L2:Schwann cell | corrected | 2 | 0 | 0 | 1 |
| 24 | DOI_10.1002_pros.24020 | L4:Neuroendocrine cell | corrected | 1 | 0 | 2 | 1 |
| 25 | DOI_10.1016_j.celrep.2018.11.086 | L4:Neuroendocrine cell | corrected | 2 | 1 | 43 | 0 |
| 26 | DOI_10.1101_2024.10.23.619925 | L2:Myelinating Schwann cell | corrected | 2 | 0 | 63 | 0 |
| 27 | DOI_10.1101_2025.01.17.633590 | L2:Schwann cell | corrected | 1 | 0 | 25 | 0 |
| 28 | DOI_10.1016_j.cell.2017.09.004 | L4:Type D enteroendocrine cell | corrected | 0 | 0 | 2 | 0 |
| 29 | DOI_10.1038_s41591-024-03215-z | — | unresolved | 0 | 0 | 45 | 0 |
| 30 | DOI_10.1038_s42003-021-02562-8 | — | no_formal_target_marker | 0 | 0 | 27 | 0 |
| 31 | DOI_10.1038_s41588-025-02158-6 | L2:Schwann cell | unresolved | 0 | 0 | 52 | 2 |
| 32 | DOI_10.1038_s41586-021-03929-x | L2:Schwann cell | corrected | 0 | 0 | 37 | 0 |
| 33 | DOI_10.1038_s41588-025-02182-6 | L2:Schwann cell / L4:Enteroendocrine cell/Neuroendocrine cell | corrected | 3 | 0 | 17 | 0 |
| 34 | DOI_10.1126_science.abl4290 | L2:Schwann cell / L4:Neuroendocrine cell | corrected | 0 | 0 | 15 | 0 |
| 35 | DOI_10.1126_science.abo0510 | L4:Enteroendocrine cell | no_formal_target_marker | 0 | 0 | 58 | 0 |
| 36 | DOI_10.1038_s41467-024-52052-8 | L1:Sensory neuron (DRG) | corrected | 5 | 1 | 0 | 0 |
| 38 | PMID_35115729 | NaN | corrected | 18 | 0 | 0 | 0 |
| 39 | DOI_10.1101_2025.09.26.678707 | L2:Schwann cell | unresolved | 0 | 0 | 63 | 0 |
| 40 | DOI_10.1038_s41467-021-21783-3 | L2:Schwann cell | no_formal_target_marker | 0 | 0 | 15 | 0 |
| 41 | DOI_10.1038_s42255-023-00876-x | L2:Schwann cell | corrected | 3 | 0 | 64 | 0 |
| 42 | DOI_10.1038_s41586-024-07069-w | L1:Efferent neuron/Enteric neuron/Parasympathetic neuron/Peripheral nervous system neuron/Sensory neuron (DRG)/Sympathetic neuron / L2:Schwann cell precursor/Myelinating Schwann cell/Satellite glial cell / L4:Intestinal enteroendocrine cell | corrected | 1 | 0 | 0 | 0 |
| 43 | DOI_10.1038_s41586-020-2496-1 | L1:Cardiac neuron / L2:Schwann cell / L4:Neuroendocrine cell/Pulmonary neuroendocrine cell | corrected | 0 | 0 | 24 | 0 |
| 44 | DOI_10.1038_s42003-024-07315-x | L2:Schwann cell | no_formal_target_marker | 0 | 0 | 80 | 0 |

## 主要问题（issue 汇总）

| issue_type | 数量 |
| --- | --- |
| missing_marker | 25 |
| evidence | 25 |
| scope | 24 |
| symbol | 22 |
| false_positive | 19 |
| other | 14 |
| species | 12 |
| polarity | 6 |
| resolved_marker | 5 |
| citation | 2 |
| duplicate | 1 |

## unresolved 条目及原因

- DOI_10.1002_pros.24020: CGRP (neuroendocrine epithelia) — CGRP 为肽段/蛋白名，可对应 CALCA 或 CALCB，论文未给出唯一基因符号，无法唯一解析，不能进入总表。
- DOI_10.1016_j.isci.2024.111628: NRXN (Schwann cells) — NRXN 是 neurexin 家族名，不是唯一基因符号（NRXN1/2/3），原文未提供具体基因，按规则不能 include，仅保留为 unresolved。
- DOI_10.1038_s41588-022-01243-4: CADM (nonmyelinating Schwann cells (nmSchwann)) — CADM is a gene family (CADM1-CADM4); the paper does not provide a unique gene symbol, so this marker cannot be resolved to a unique gene.
- DOI_10.1038_s41588-025-02158-6: PLP1 (Schwann cells) — figure_labeled 证据不足：唯一依据为 Fig. 1d 通用图注（Dotplot showing the mean expression of marker genes...）与基因轴 OCR（PLP1）/细胞轴 OCR（Schwann cells）同图共现；OCR 无法读出 PLP1 与 Schwann cells 的具体对应关系，不满足 figure_labeled 标准（计划 5.1）; Codex 抽查续检 2026-08-30
- DOI_10.1038_s41588-025-02158-6: CDH19 (Schwann cells) — Fig.1d dotplot 基因轴 OCR 以带空格形式（CD H19，原文 L112）出现，但行列对应关系在 OCR 中丢失，无法读出 CDH19 与 Schwann cells 的具体映射；不得用领域常识补证据，维持 unresolved 待查原图; Codex 抽查续检 2026-08-30

旧版总表与逐篇提取结果已提交至 Git；工作树仅保留当前终审结果和论文 Markdown。