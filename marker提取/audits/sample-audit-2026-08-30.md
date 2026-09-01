# Marker 五篇抽查审计（2026-08-30）

## 审计方法

- 由独立子 Agent 只读完成，不修改 Excel、JSON、CSV 或 Markdown。
- 只使用现有 `review_md` Markdown、schema v2 raw JSON/review CSV 和 Marker 总表，不重新转换或提取论文。
- 采用可复现的覆盖优先分层抽样：强制覆盖两个别名 pending 所在论文，并覆盖 annotation marker、figure-labeled marker、无正式 PNS marker 阴性样本及正式 PNS marker 较多的压力样本。

## 结果

通过率：**1/5**。不满足批量清理 `pending` 的前提。

| 文章 | 结论 | 主要发现 |
|---|---|---|
| `DOI_10.1038_s41467-024-52052-8` | 通过 | NeuN 和 p21 的原文 marker 证据成立；`NeuN -> RBFOX3`、`p21 -> CDKN1A` 的基因级规范化合理，原始文本应保留。 |
| `DOI_10.1016_j.isci.2024.111628` | 不通过 | CDH19、XKR4 正确；`NRXN` 只是 neurexin 家族式写法，不能直接作为唯一标准基因符号。 |
| `DOI_10.1038_s41588-025-02158-6` | 不通过 | 已收入正式 marker 多数有证据，但 `ISL1-high`、`PPP2R2C-high`、低/负 PHOX2B 等作者亚群注释被错误降为 context-only。 |
| `DOI_10.1038_s41586-024-07069-w` | 不通过 | `Myelinating Schwann cells (Tgfb2+)` 是作者节点注释，Tgfb2 被错误降为 context-only，造成正式候选漏提。 |
| `PMID_35115729` | 不通过 | 多处明确的 `marked by`、`marks`、`Markers highlighting` 语句被 guardrail 误杀，且 B2m 等 marker 漏提。 |

## 系统性问题

1. 非唯一基因家族名可能进入 `gene_symbol`；
2. 明确的 `GENE+` / `GENE-high` 亚群注释可能被错误降级；
3. 明确的 `marked by` / `marks` / marker list 可能被 guardrail 误判为 context-only。

## 决策

- 不批量清理任何 Marker `pending`；
- 不将当前结果标记为“无需复核”；
- 按用户后续补充，本轮不修改现有表或 JSON，也不重新提取；仅保留审计结论并整理文件。
