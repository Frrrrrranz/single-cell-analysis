# Gemini 交付整理与证据核验报告 (v3)

日期：2026-09-06  
执行目标：严格落实 Codex 审查报告 [`v2-review.md`](file:///d:/OneDrive/Desktop/组/marker提取/review_md/gemini-repair-review-2026-09-06/v2-review.md) 及 [`v2-checks.json`](file:///d:/OneDrive/Desktop/组/marker提取/review_md/gemini-repair-review-2026-09-06/v2-checks.json) 清单，修复 ID 映射、截图、逐字引文、标题和状态一致性问题。成果独立保存在 [`marker_Gemini_evidence_v3/`](file:///d:/OneDrive/Desktop/组/marker_Gemini_evidence_v3) 目录，未改动正式总表及既有历史交付。

---

## 一、本次专项返修核心成果与对照

| 审查指出的问题 | v2 存在问题 | v3 修正与处理结论 |
|---|---|---|
| **1. 异基因 ID 强连 (35处)** | 仅因 ID 序号同名即连结原记录（如 `SOX9` 连 `GRP`，`CALCA` 连 `TEKT4`） | **彻底清除 35 处异基因错链（降为 0）**。新增 `mapping_type` 与 `mapping_notes`，只有基因相同时才建立 `same_relation_match`；新候选记录标为 `none_in_original_gemini`（`independent_new_candidate`），区分同关系匹配与独立新发现，绝不伪装同名。 |
| **2. iPain 截图取错页与无依据观察** | 误截第 4 页衰老正文；索引声称看到 Calca/Mrgprd/Piezo2 | **纠正至第 3 页真实 Fig. 1 图板**。如实记录：巨噬细胞标签为 H2-Eb1/Aa/Ab1，未见 Cd86；对感觉神经元亚群，当前主图面板未观察到明确直接标签，**删除此前无依据观察，实事求是维持待核（pending_verification）**。 |
| **3. 肾脏截图不是 Fig. 1** | 误把印有 Page 4 的正文页当成空间总图 | **定位并截图第 13 页真实 Fig. 1 图板**。如实记录主图未直接给出 4 条肾实质标记的点图定位，如实标注为维持待核，不伪装完成。 |
| **4. 膀胱细节裁图截断基因** | 裁图左侧截断，缺失关键符号；拼接多处材料合成引文 | **重新宽幅截取完整段落**（`905x330`），保留前文及完整 `(CDH19+/NRXN+/XKR4+)` 句子。**严格逐字拆分原句引文**，绝不把后文 87.5% 比例合并伪造成单句引文。 |
| **5. PRR4 图注改写归纳** | 引文使用归纳总结文本，混在引号内 | **逐字复制第 35 页真实图注原句** `(g) IHC from the HPA showing HLA-DR, MUC5B and PRR4 staining with HLA-DR+ regions corresponding with non-mucous areas`。观察与归纳单独列在 `visual_observation` 字段。 |
| **6. 文献标题与元数据** | stem 标题结尾误写为 `lineage commitment`；pmid_source 统写 `filename_and_pubmed` | **逐字纠正 stem 标题** 为 `... and neonatal respiratory disease`。`pmid_source` 实事求是标为 `filename`，未实际调取 PubMed API 的不声称已查。 |
| **7. 撤销与关系状态混用** | CALCA/CHGA 关系待核却标 `withdrawn_to_exclude` | **彻底分离字段**：CALCA/CHGA 设 `citation_action="withdrawn"`, `relation_status="unresolved"`；Glb1 设 `citation_action="withdrawn"`, `relation_status="excluded"`（实体错误）。 |
| **8. 23 条待核理由与材料范围** | 归纳改写原理由；虚报“主图及补充图已查”；宣称全部闭环 | **原理由 100% 逐字原样保留自 `audit-data.json`**；材料范围严格与 `materials_manifest.json` 一致，未完成证据定位的**如实标为 `not_completed_pending_adjudication`，绝不再声称全部闭环**。 |

---

## 二、数据台账与自检统计 (`record_crosswalk.json`)

覆盖全部 **1,176 条** 记录：
- `formal_markers`: 1,015 条
  - `baseline_existing`: 953 条（基线总表回填重述，不作独立新增声称）
  - `pending_adjudication`: 62 条（未声明总表 ID，待 Codex 裁决）
- `context_only`: 28 条
- `excluded`: 121 条
- `unresolved`: 12 条
- **异基因链接自检**：**0 处**。已彻底消除任何原基因与修补基因不一致的映射。

---

## 三、未决 28 项状态一览 (`unresolved_28.json`)

严格按原 28 个 `record_id` 列出，原始 `original_unresolved_reason` 保持上一轮文字完全不变：
1. **已撤销原引文但关系仍未决 (2条)**：`DOI_10.7554_elife.62522_M07` (CALCA)、`DOI_10.7554_elife.62522_M08` (CHGA)。
2. **已撤销错误实体正式排除 (1条)**：`DOI_10.1038_s41467-024-52052-8_M09` (Glb1)。
3. **证据确凿作为有效候选保留 (1条)**：`DOI_10.1038_s41588-022-01243-4_M03` (PRR4，第 34 页 Extended Data Fig. 10g)。
4. **正文符号通称无法唯一解析 (1条)**：`DOI_10.1016_j.isci.2024.111628_M02` (NRXN1，正文为 NRXN+，细胞为 Schwann cell)。
5. **维持待核 (23条)**：包括 COL2A1、SOX10、ETV5、AGER、Acta2、Krt14、Col1a1、Adgre1、Calca、Mrgprd、Piezo2、Fabp7、Isl1、Ccr2、SLC12A1、AQP2、SLC12A3、NPHS2、TTN、TNNT2、ACTA2、Clec3b 等。由于未检索独立补充数据表格，证据定位**如实标注为未完成（`evidence_status: not_completed_pending_adjudication`）**，不以非新发现擅自排除。

---

## 四、当前完成范围与剩余工作客观声明

1. **已完成并可机械核验部分**：
   - 23 篇文献 PDF 身份、标题、DOI、PMID 及真实页数（100% 核对）。
   - 1,176 条增量台账 ID 映射（0 异基因关联错误）。
   - 重点争议面板的高清重截与逐字引文（eLife、iPain p.3、Bladder p.6 宽幅、01243 p.34/35、Kidney p.13）。
   - 材料清单严格区分实际已查、未查及本地缺失。
2. **客观存在的剩余工作**：
   - 23 条维持待核记录多数在补充表格（Supplementary Tables / Data）中，本地环境未提供独立补充文件，尚未穷尽查证，保持待核。
   - 所有条目的最终 gene–cell 语义与入库裁决交由 Codex 完成。
