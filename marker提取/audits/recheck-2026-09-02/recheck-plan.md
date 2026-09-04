# Marker 总表完整复核方法论与执行手册（recheck-2026-09-02）

> 配套计划：`/.agents/plan/marker-recheck-and-newpapers-2026-09-02.md`
> 工作台：`audits/recheck-2026-09-02/recheck_plan.xlsx`
> 生成脚本：`scripts/build_recheck_plan.py`（重跑：`python scripts/build_recheck_plan.py`）
> 补充扫描脚本：`scripts/scan_b2_supplement.py`（步骤 0.5，只增补 B2 sheet，不覆盖其他 sheet）

## 1. 背景

豆包教学范例交叉核对 PMID_35115729 发现四类系统性问题：

1. **漏提**（Slit2：比较段落中作者并列举出的 "SC subpopulation marker genes" 全链路漏提）；
2. **evidence_type 错判**（Itgb4/Slc2a1：原文 "expression of markers" 却记为 annotation_marker）；
3. **语义重复**（M01532-34：cell_type 写法不同绕过 `paper_id+cell_type+subtype+gene_symbol` 唯一键）；
4. **归属/图注挖掘不足**（Ngfr 归属、Extended Data 图注漏挖——豆包对照发现）。

据此对全部 40 篇已提取论文 + 3 篇新论文做一轮完整复核。

## 2. 核心原则

- **双重门槛**（Marker 身份 + 注释用途）缺一不可；仅 enriched/DEG/高表达措辞不收录；
- **机械扫描只产候选**，所有落表改动必须回原文核对；
- **全程留痕**：移除行入 `audit_exclusions`（带 superseded_marker_id），每批改动记 `import_log`。

## 3. 五道检查门

### Gate A 漏提候选（314 条）

扫描 review_md 全文，凡句中含 marker 措辞（markers / marked by / marks / characterized by / defined by / specified by / signature）且出现类基因 token、而该篇总表未收录者列入候选。

置信分档：
- **词表命中**（跨篇基因词表）：41 条左右，高置信，优先人工核对；
- **模式命中**（全大写/带数字的强 token）：其余，需人工判别。

噪声修正（2026-09-02 定稿）：
| 噪声 | 处理 |
|---|---|
| 引文上标粘连（Cd45^28→"Cd4528"） | 尾部 1-4 位数字逐档剥离，词干命中该篇基因→跳过；命中跨篇词表→以词干为候选名 |
| 蛋白别名（CD45/Glut1） | 10 项常用别名映射（cd45→ptprc、glut1→slc2a1 等），别名命中已收录→跳过 |
| 构建体名（Mpz-Sun1/ActB-Cre/ChAT-Cre-tdT） | 构建体模式整段剔除后再提 token |
| 统计工具句（Seurat/harmony/doublet） | 跳过 |

**校准验证**：试点论文 PMID_35115729 修正后 Gate A 候选清零（Slit2 已补录、已收录基因零误报、六类噪声全部消除）。

### Gate B 证据类型候选（256 条）

- **升级候选**：evidence_type ∈ {annotation_marker, figure_labeled} 但 source_context 已含明确 marker 措辞且 locator 非"图注编号开头"→ 升级 author_declared；
- **恢复候选**：原设计为"context_only 行含 marker 措辞 → 身份恢复"，但总表 candidate_class 已全部为 formal_candidate，正式版扫描中该方向产出 0 条，实际降级池在 audit_exclusions——由下方 Gate B2 补充承接。

**已确认执行方式**：升级时 source_context 同步替换为完整原句，原值并入 audit_notes。

### Gate B2 补充候选（143 条，步骤 0.5，2026-09-02 晚）

数据核对发现两处口径缺口后的机械补扫（`scripts/scan_b2_supplement.py`）：

| 来源 | 扫描池 | 命中 | 候选方向 |
|---|---|---|---|
| B② 身份恢复 | audit_exclusions 中 recovery_outcome ∈ {recheck_context_only, recheck_unresolved, new_finding_recheck_unresolved, new_finding_recheck_context_only}（354 行，context 均非空） | 117 | 双重门槛满足则恢复入表（新发 marker_id，recovery_source=recovered_context_only_2026-09-02，原 exclusion 行 recovery_outcome 改写 recovered_2026-09-02） |
| B① 补充升级 | markers 表 evidence_type=supplementary_marker（43 行） | 26 | 作者措辞明确则升级 author_declared（不受定位符守卫） |

分布要点：143 条覆盖 28 篇；单篇最多 s41586-021-04345-x（24 条）；117 条恢复候选中 16 条该篇总表已有同基因（多为不同 cell_type 语境，人工判是否真重复）；s41586-020-2496-1 的 4 条并入 Batch 9 与旧 24 条重判同批处理。
处置规则与 B 门一致：命中行按 paper_id 并入 Batch 1-8 对应批次，只产候选不落表。

### Gate C 语义重复候选（68 组）

同篇同基因、cell_type 规范化（去括号/小写/去标点）后完全相同或 token 集互为包含 → 合并候选。
状态词守卫：cycling/mature/immature/proliferating/activated/memory/naive 等**状态词不同 = 不同细胞**，不报重复（B cells vs Cycling B cells 共享 MS4A1 属正常）；plasma 等分化阶段词不守卫（可能是误归属，交人工）。

处置：保留更具体/证据级更高的行，另一行移入 audit_exclusions（recovery_outcome=dedup_removed_2026-09-02）。

### Gate D 人工清单（每篇 5 项）

1. 聚类清单对账（正文/图注 cluster 数 vs 总表细胞类型数）；
2. marker 归属核对（同基因多细胞归属与原文语境一致性，Ngfr 型）；
3. 物种一致性（行内 species vs 任务表；鼠/大鼠基因写法）；
4. 基因写法核对（保留原文大小写，大鼠首字母大写）；
5. 跨篇一致性（细胞命名与四层分类口径）。

### 校准基准

PMID_35115729（修正后 42 行）作为参照样本，每批复核后抽查其不回退。

## 4. 优先级与批次

优先级 = A 词表命中 > 0 或 C 组 > 0 → 高；A 模式或 B > 0 → 中；否则低。
当前分布：**高 29 / 中 9 / 低 2**（共 40 篇）。

批次安排（每批 5 篇、批后汇报）见计划文件第 8 节；试点已完成，剩 Batch 1-8 复核 + Batch 9 新论文提取（3 篇）。

## 5. 落表规范

- 新增行：`review_method=recheck_2026-09-02`、`audit_status=recheck_include`、`recovery_source=recheck_2026-09-02`（新论文用 `new_extract_2026-09-02`）；
- 升级行：原 evidence_type 记入 audit_notes，source_context 换完整原句；
- 移除行：入 audit_exclusions，superseded_marker_id + recovery_outcome（dedup_removed / misattributed_removed_2026-09-02）；
- 归属修正：旧行移入 exclusions、新行补录；
- 每批一次 import_log（batch_id=B20260902-RECHECK-B<n>）。

## 6. 批次汇报模板

```
## Batch <n> 复核汇报（<5 篇 paper_id>）
- 补录：X 条（paper | cell_type | gene | evidence_type | 依据句摘录；重审改判单列）
- 升级：X 条（marker_id | gene | 旧→新 | 原句；B① supplementary 升级单列）
- 身份恢复：X 条（新 marker_id | gene | 原 recovery_outcome）
- 重审改判：X 条（原排除理由摘要 → 新结论）
- 重复移除：X 条（superseded_marker_id）
- 归属修正：X 条
- 维持不录：X 条（原因分类计数）
- 总表行数：A → B
- 问题模式（供后续批次参考）
```

## 7. 验收

1. A/B/C/D 四门 + B2 补充候选 + 试点遗留 2 条（M01516/M01517）每条候选均有处置结论（补录/升级/恢复/移除/维持 + 理由）；
2. 3 篇新论文完成 v4 提取导入、元数据补齐（3 篇均缺，2026-09-02 核对确认）；
3. 唯一键无冲突、citation_verified=true、`validate_full_audit.py` 通过；
4. dashboard 重建、README 统计更新。
