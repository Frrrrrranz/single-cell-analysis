# Luna 第二轮独立复筛进度

## 当前基线

- 当前正式总表 `our_markers.xlsx` SHA-256：`8abdddb800dce6e84ca711d9cb5905cc114390e77adc499f8ef5471f09021373`；2499 条数据行，2499 个唯一 marker_id。
- 当前正式按细胞表 SHA-256：`9b166cd7aef77d39c8019dcc163a6e2aa8dd0ab74927dbe0195060390062c3e2`。
- Gemini Batch-02 使用的声明哈希与当前正式表不一致；277 个稳定 ID 均仍存在，已按当前正式表复核，没有恢复旧文件。

## 已完成

- 读取并核验 Marker policy、operations manual、项目适用 AGENTS 规则、两批 Gemini manifest/coverage/screening/evidence/handoff/PROGRESS。
- 实际查看 Batch-01 关键证据图/图注 EVID01–EVID05，以及 Batch-02 EVID06–EVID14 的图像或文本证据范围。
- 对首轮全部 490 个单元完成独立复筛记录，逐条保留稳定 ID、来源、基线值、证据定位、分歧与停止条件。
- Round2 统计：executed=490，evidence_supported=479，relationship_unresolved=11，blocked=0。
- Luna建议变更 20 项；首轮提案被拒绝或维持 no_change 的记录 91 项；所有 change 均明确交由 Astra 最终裁决。

## 全局覆盖边界

- 首轮只覆盖当前正式表 2499 条中的 473 个基线 ID，以及 17 个候选单元；本轮不宣称全量总表复筛完成。
- 原 62 候选、28 状态接续、28 context_only、121 excluded、953 baseline backfill 的实际对账及未覆盖范围见 `acceptance.json`。
- 这些集合有交叉，不相加作为独立总数。

## 未完成与补件需求

- unresolved/hold：REV_ELIFE_02_CALCA, REV_ELIFE_03_CHGA, REV_IPAIN_03_Calca, REV_IPAIN_04_Mrgprd, REV_IPAIN_05_Piezo2, REV_IPAIN_06_Fabp7, REV_BLADDER_01_NRXN1, REV_KIDNEY_01_SLC12A1, REV_KIDNEY_02_AQP2, REV_KIDNEY_03_SLC12A3, REV_KIDNEY_04_NPHS2。
- 若 Astra 要求补核，需限定到具体 paper、PDF/Markdown、页码/图号和 stable_id；当前没有无边界全文搜索或重跑提取计划。
- 未生成暂存工作簿，正式表和 Gemini 交付均未修改。

## 接续位置

- Astra 应先读取 `handoff_to_astra.md`，再用 `proposed_change_set.json` 的 expected_baseline_sha256 校验基线，最后按优先顺序抽查证据和批准动作。
