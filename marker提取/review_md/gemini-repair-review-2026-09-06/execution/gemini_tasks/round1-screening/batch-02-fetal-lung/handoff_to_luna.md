# Batch 02 首筛交接说明 (Handoff to Luna)

## 一、批次概述与执行规范

- **批次标识**: `batch-02-fetal-lung`
- **执行模型**: Gemini 3.8 Flash (Thinking 档位: high)
- **执行依据**: `operations-manual.md` v1.2 及 `MARKER_POLICY.md` v1.2
- **审查范围**:
  1. `DOI_10.1016_j.stem.2022.11.013` (人胎儿肺泡类器官发育模型, 70 条 baseline markers)
  2. `DOI_10.1016_j.cell.2022.11.005` (人胎儿肺单细胞时空发育图谱, 207 条 baseline markers)
  - **总计首筛核查 baseline 记录**: **277 条**（无估算，100% 真实对账核实）

---

## 二、首筛判定与统计汇总

| 建议动作 (Action) | 记录数量 | 核心说明与依据 |
| :--- | :---: | :--- |
| **keep** | **187** | 经核对正文、主图及补充图表，标志物对应关系确凿，特异性与细胞标签完全合格 |
| **context_only** | **44** | 负标志物排他门控（如 SFTPC-、SOX9-、PLN-）、流式分选操作分区（CD44/CD36 门控）、全上皮/全内皮广谱背景标志（CDH1, PECAM1） |
| **merge_duplicate** | **33** | 单复数命名重复（如 club cell vs club cells, aerocyte vs aerocytes）、大小写重复（Myofibroblasts vs myofibroblasts）、同一基因在同章节多次重复提取 |
| **exclude** | **11** | 9 条解剖外来污染组织细胞（食管、心脏、滋养层、肝脏污染）+ 1 条实验归一化对照（EPCAM+ 磁珠分选）+ 1 条阴性排他门控误赋（SFTPC 赋给 AT1） |
| **update** | **2** | 类器官体外模型细胞类型规范化更新（LinPOS 类器官更新为 alveolar type 2 cell (organoid)） |
| **合计** | **277** | **100% 完成首筛核验，无未核对遗留项** |

---

## 三、重大问题与纠错判定要点

### 1. 【核心纠错核实】HOPX 在人类胎儿肺发育中为 AT2 标志物
- **涉及记录**: `M00839` (HOPX / AT2 cells)
- **判定与证据**: 正文 p. 8 与 Figure 3D 明确声明并证实，HOPX 在人类胎儿肺类器官分化中与 SFTPC、SLC34A2 协同上调，属于人胎儿期 AT2 谱系标志物。此前将 HOPX 误判为成熟小鼠 AT1 的常识性错误被本研究彻底修正，判定为 `keep`。

### 2. 【硬排除】外来解剖污染细胞（Contaminants）
- **涉及记录**: `M00432`, `M00433`, `M00451`, `M00452`, `M00468`, `M00469`, `M00479`, `M00480`, `M00481` (共 9 条)
- **判定与证据**: STAR Methods p. 27 明确记载：`APOA1+ APOA2+` (肝/卵黄囊), `ACTN2+ MYH6+` (心肌), `GSTA3+ PAGE4+` (胎盘滋养层), `SOX2+ TP63+ KRT5+ TRH+` (食管上皮) 均为胚胎取样过程中的非肺组织外来污染，作者在数据预处理阶段已作为污染簇剔除。原提取将外来污染细胞当作肺固有 marker，属于严重概念混淆，坚决予以 `exclude`。

### 3. 【负标志物与门控归入 context_only】
- **涉及记录**: 
  - `M00846~M00851`: 流式分选操作门控区（`CD44+CD36-` 与 `CD44-CD36-`），属于体外实验分选门控，非生理细胞类型；
  - `M00859, M00860, M00883, M00889, M00244~M00248, M00587, M00593`: 负标志物（如 GHRL 在经典 PNEC 为阴性、GRP 在 GHRL+ NE 为阴性、PLN 在 vSMC 为阴性、SOX9 在 stalk 为阴性等）；
- **判定规范**: 严格遵循 `MARKER_POLICY.md`，负向标志物不作为正向 formal marker，建议归入 `context_only`。
- 特殊排他：`M00856` (SFTPC 在 Fetal AT1 cells 标为 negative)，因 SFTPC 是经典 AT2 阳性 marker，作者图例注明 `SFTPC, green, AT2 cell marker`，原提取将其标给 AT1 属于严重倒错，判定为 `exclude`。

### 4. 【神经内分泌亚型粒度解析】
- **经典 PNEC**: ASCL1+, GRP+ (`M00034`, `M00035`)，正向特异性确凿；
- **GHRL+ NE**: NEUROD1+, GHRL+, TTR+, RFX6+ (`M00036~M00039`)，正向特异性确凿；
- **中间态祖细胞**: NEUROG3+ (`M00040`)，正向特异性确凿；
- **复数及亚型重复条目**: `M00041~M00043, M00047~M00050` 建议去重合并至主条目。

---

## 四、证据索引与原图清单

本批次建立 9 个高精度结构化证据块（`EVID_06` ~ `EVID_14`），并从论文 PDF 提取 8 张原版高分辨率图片存入 `evidence_images/` 目录：
1. `stem_2022_fig3_at2_hopx.png` (Figure 3: HOPX, SFTPC, SLC34A2 表达)
2. `stem_2022_figs1_tip_epithelium.png` (Figure S1: Tip 上皮 SOX9/SFTPC/CD36/PDPN 染色)
3. `stem_2022_figs5_myofibroblast_wnt2_at1.png` (Figure S5: NOTUM/ACTA2/PDGFRA 肌成纤维与 WNT2 成纤维及 AT1 SPOCK2)
4. `cell_2022_fig2_epithelial_subtypes.png` (Figure 2: 气道及 Tip 上皮亚群点图)
5. `cell_2022_fig4_mesenchymal_types.png` (Figure 4: 间充质亚型图谱点图与定位)
6. `cell_2022_fig7_neuroendocrine_subtypes.png` (Figure 7: 神经内分泌两亚群转录调控)
7. `cell_2022_figs7_endothelial_mesenchymal.png` (Figure S7: 内皮及平滑肌亚群点图)
8. `cell_2022_figs8_tf_ne_subtypes.png` (Figure S8: 神经内分泌亚型互斥转录因子)

---

## 五、对 Luna 的复核指引

1. **重点复核 HOPX (`M00839`)**: 确认在 `EVID_06` (Fig 3D) 和正文 p. 8 中 HOPX 作为人胎儿 AT2 标志物的合法性。
2. **复核污染细胞排除 (`M00432` 等 9 条)**: 确认 STAR Methods p. 27 排除解剖污染的硬边界。
3. **复核去重合并映射**: 检查 33 条 `merge_duplicate` 记录的 `merge_into_marker_id` 映射是否完全对应规范单数词主条目。
