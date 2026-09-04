# Batch 1 复核子任务通用规范（recheck-2026-09-02）

## 背景
本项目的 markers 总表（our_markers.xlsx）收录文献中作者实际用于细胞群注释的 Marker。此前试点（PMID_35115729）交叉核对发现四类系统性问题：漏提、evidence_type 错判、语义重复、归属错误。现在对全部论文做完整复核，机械扫描产出的候选需要人工（你）逐条回原文核对后判定。

## Marker 收录双重门槛（缺一不可）
1. **Marker 身份成立**：作者明确将该基因作为某细胞群的 Marker 呈现或说明（如 "markers of X"、"X cells marked by G"、"canonical marker"、"we prepended a representative marker gene"），而不是仅称为 DEG、top DEG、功能基因、通路基因、受体、配体、药物靶点。
2. **注释用途成立**：该 Marker 实际参与该细胞群的识别、命名或归类，而不是注释完成后仅用于验证、证明、描述或功能展示。

边界规则：
- 作者用于注释的 marker 图/表/列表 → 整体收录（panel 中所有基因，不得因"看起来像功能基因"而剔除）
- 方法说依据 marker 注释 + 对应 marker 图表 → 关联证据成立，收录
- 仅 "enriched in / specifically expressed / elevated levels" 等富集措辞且无 marker 措辞 → 不满足身份门槛，不收录
- 注释后才用于验证/展示的 marker → 不收录
- 完整 DEG 表 / 基因集富集（GSEA hallmark）→ 不收录
- "progenitor markers"、"injury markers"、"gluconeogenesis markers"（代谢物）、"viability marker"（试剂）等非细胞群识别用途 → 逐条判定，通常不收录
- 图注中的 "marker genes of X" dot plot → 满足双重门槛（图用于注释），收录

## 各门判定规则

### Gate A 漏提候选
对每条候选：读原文完整上下文（用 review_md 文件 grep 关键词），判断双重门槛。
- 判定"补录"：给出 cell_type（作者原文标签）、gene_symbol（保留原文大小写）、species、evidence_type（author_declared / annotation_marker / figure_labeled）、source_locator（最小证据单元）、完整原句。
- 判定"不录"：给原因分类（噪声 token / 非 marker 措辞 / 无注释用途 / 试剂或方法学 marker / 代谢物等）。
- 噪声类型识别：MERFISH/GSEA/ISH/MAST/MCC/DRG(组织名)/AKI/CKD/COPD/IPF(疾病缩写)/CUT&RUN/H3K27ac(组蛋白修饰)/SMG/AT2(细胞名)/NP1-NP3(细胞名)/H10-H12(细胞名)/克隆号(SK3/HIB19/RPA-T4)/货号(S34857)/数据库(GRCm38/NCBI/KPMP/HPA/HLCA)/方法(MACS/FACS/IMS)等——这些不是基因，直接判定"不录-噪声token"。
- 拼写修正：如 "BPIFBP1" 实际是 "BPIFA1/BPIFB1" 需查原文；"Bro1" 可能是断行噪声；"NKX2" 是 "NKX2-1" 被截断；"PRP1" 在人 DRG 文献中应为 "PRPH"（peripherin）或原文如此——以原文实际拼写为准，不得静默修正。
- "此前已排除"的候选是重审：需要重新判断旧排除理由是否仍然成立（项目范围已从 PNS 扩大到全部细胞类型，旧的范围性排除理由已失效，只要满足双重门槛就应改判 include）。

### Gate B 证据类型候选（升级 author_declared）
对每条：读原文核实 source_context 中的 marker 措辞是否确实存在且指向该基因+该细胞。
- 判定"升级"：确认作者明确以 marker 措辞呈现（如 "fibroblast marker Pdgfra"），给出完整原句（从 review_md 中摘取）。
- 判定"维持"：context 中 marker 措辞与该基因无关（如句中 markers 指别的基因）、或该行 cell_type 与句子语境不符（如句子讲 monocytes 但行挂在别的细胞上→实为归属错误，需标注"归属错误"而非简单升级）。
- 注意：B 门候选中若发现 cell_type 归属与原句不符，单独标注为"归属修正"。

### Gate B2 补充候选
- B②身份恢复（exclusions 降级行）：判定满足双重门槛则"恢复"（给 cell_type、gene、evidence_type、locator、完整原句），否则"维持排除"。
- B①supplementary_marker 升级：作者 marker 措辞明确（如 "non-myelinating Schwann cell markers (CADM, GRIK2, ...)" 图注）则"升级 author_declared"，否则维持。
- 恢复行的新 cell_type 以原句为准；若基因是家族名（如 CADM 泛指），标注"基因名不可解析"维持排除。

### Gate C 语义重复候选
每组判定保留哪一行、移除哪一行：
- 若两行确属同一细胞同一证据（如同一个 dot plot 面板、同一原句），保留证据级更高（author_declared > annotation_marker > figure_labeled > supplementary_marker）或 cell_type 更具体的行，另一行移除。
- 若两行实际不同（不同面板、不同生物学背景、状态词不同如 AT2 vs AT2-s 是不同细胞亚群），判定"不合并"并说明理由。
- 状态词守卫：cycling/mature/immature/proliferating/activated/memory/naive/signalling 等状态词不同 = 不同细胞。
- 特别注意：若重复原因是把同一基因面板拆挂到两个 cell_type（如 CD19/NCAM1/CD4 同时挂在 monocytes 和 T cells 上），其中一个是归属错误——标注"归属修正"：错误行移入 exclusions，若该基因确实属于正确细胞则补录。

### Gate D 人工清单（5 项）
1. 聚类对账：正文/图注报告的 cluster 数和注释标签数 vs 总表 cell_type 去重数。明显少于应有数量（整簇漏提）则列出缺失的细胞类型及其 marker 证据。
2. marker 归属核对：同基因多细胞归属是否与原文语境一致（Ngfr 型错误）。
3. 物种一致性：行的 species 与论文物种（人/鼠/大鼠）是否一致。
4. 基因写法核对：保留原文大小写（人全大写、鼠首字母大写），不得转大写。
5. 跨篇一致性：细胞命名与四层分类（four_layer_category）口径。

## 输出格式
对每篇论文输出一份 markdown 报告，包含：
```
# <paper_id> 复核判定报告
## 摘要
（本篇判定统计：补录 X、升级 Y、恢复 Z、移除 W、归属修正 V、维持不录 N）
## A 门逐条判定
| # | 候选基因 | 判定 | cell_type | gene_symbol | species | evidence_type | source_locator | 原句（完整） | 理由 |
## B 门逐条判定
| marker_id | gene | cell_type | 判定 | 完整原句 | 理由 |
## B2 逐条判定
| 来源 | gene | cell_type | 判定 | 完整原句 | 理由 |
## C 门逐条判定
| 组 | 行1 | 行2 | 判定 | 保留 | 移除 | 理由 |
## D 门检查结论
（5 项逐项结论，发现的问题详列）
## 归属修正明细
（如发现：marker_id | 错误归属 | 正确归属 | 证据）
## 整簇漏提明细
（D 门对账发现整簇缺失时列出：cell_type | markers | 证据 locator + 原句）
```

要求：
- 每条判定的原句必须从 review_md 原文实际摘取（grep 验证），不得凭记忆或候选材料中的截断句直接引用；候选材料中的句子可能被截断（以...结尾），必须回原文找完整句。
- evidence_type 层级：author_declared（作者文字明确 marker 措辞）> annotation_marker（方法/注释流程引用的 marker）> figure_labeled（仅图中标注）> supplementary_marker（补充材料）。
- 物种判定：人基因全大写（如 MUC5B），小鼠基因首字母大写（如 Mrgpra3），保留原文拼写。
- 不确定时判定"存疑"并说明缺什么证据，不强行下结论。
