# 35条待复核 marker 抽查审核记录

审核日期：2026-08-21  
审核方式：按论文分层、按同一 source_context/figure evidence 分组抽查；结合 `review.csv`、review Markdown、原文 PDF 正文、图注和 marker dotplot 核对。35条记录全部覆盖，但同一证据段中的重复 marker 按证据组一次核验，避免把同一句话重复计算为多个独立证据。

## 结果汇总

| 论文 | 待复核条数 | 结果 | 核验重点 |
|---|---:|---|---|
| DOI 10.1016/j.isci.2024.111628 | 3 | 3条通过 | 原文 Results/Classification of stromal cells、Fig. 1E：Schwann cluster 为 CDH19+/NRXN+/XKR4+ |
| DOI 10.1038/s41467-024-52052-8 | 2 | 证据通过，名称待规范化 | Fig. 3i/Results 明确称 NeuN 为 neuronal nuclei marker、p21 为 senescence marker；但二者是蛋白/通用命名，不是标准基因符号 |
| DOI 10.1038/s41588-022-01243-4 | 4 | 4条通过 | Results“Four distinct cell types in airway peripheral nerves”：mSchwann 为 NFASC、NCMAP、MBP、PRX |
| DOI 10.1038/s41588-025-02158-6 | 6 | 6条通过 | VIM 在正文中用于 mesenchymal neuroblastic population；ISL1/PHOX2B 出现在 human Fig. 1d marker dotplot；Hand2/Isl1/Phox2b 出现在 mouse Fig. 5c marker dotplot |
| DOI 10.1164/rccm.202207-1384oc | 3 | 3条通过 | Results“Cellular Diversity along the Proximal–Distal Airway Axis”：Gli 为 CDH19、MPZ、NRXN1 |
| DOI 10.64898/2025.12.18.695268 | 1 | 1条通过 | Fig. S3E 关联文字：nerve bundle 中 Schwann cells 为 NRXN1+ |
| PMID 35115729 | 16 | 16条通过 | 正文及 Fig. 1/2/4/Abstract：nmSC 和 cluster 3 mSC 的 marker 证据均可回溯；重复的 cluster 3/Abstract 记录属于不同层级/来源上下文，不是抽取错误 |

总计：33条可批准，2条保留 pending 以完成命名规范化；未发现正文、图注或图中 marker 归属明显错误。

## 需处理的两条记录

- `M00057 NeuN`：原文证据成立，但 NeuN 是抗体/蛋白标记名称。建议确认项目是否将其映射为 `RBFOX3`；在确认前不进入标准基因级总表。
- `M00058 p21`：原文证据成立，但 p21 是通用蛋白名称。建议确认项目是否将其映射为 `CDKN1A`；在确认前不进入标准基因级总表。

这两条不是“原文没有marker”，而是“marker证据正确、字段命名尚未达到基因符号规范”。

## 论文与来源文件

- 原文 PDF：`db/cellxgene/cellxgene_filtered/downloads/`
- review Markdown：`scripts/extract_markers/review_md/`
- 机器提取审核 CSV：`scripts/extract_markers/markers_output_v2/`
- 本次更新总表：`scripts/extract_markers/our_markers.xlsx`

总表中本次35条记录的 `review_method` 已更新为 `spot_check_original_pdf_review_md`；33条状态改为 `approved`，2条保持 `pending` 并写入规范化说明。
