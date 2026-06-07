---
name: pns-scrna-database
description: 外周神经scRNA数据库的设计资产维护手册。当主人要查看、修改、扩展这个数据库的设计（schema、受控词表、检索式、预筛/提取prompt、QQ协议、Python脚本、runbook）时召唤。快速定位 design/ 下的资产、说明跨文件一致性铁律、以及改完怎么跑测试验证。Trigger：改数据库设计 / 改schema / 改提取prompt / 外周神经数据库设计 / PNS scRNA design。
---

# 外周神经 scRNA 数据库 · 设计维护手册（小玖用）

> 设计资产在本包 `design/` 子目录（作者本机原路径为 `D:/database/design/`，分享时已改为相对路径）。架构：小玖(Claude)只做设计，运行期小钰(Hermes)+DeepSeek V4 执行。
> 改设计前先读本手册，**避免破坏跨文件一致性**（这是最容易出 bug 的地方）。

## 资产地图（改哪个文件、会连带影响什么）
| 文件 | 内容 | 改它必须连带检查 |
|---|---|---|
| 01_schema.md | 5 表字段/枚举/SQLite DDL（**地基**）| 改字段 → 04/05/06/07 全部跟着改 |
| 02_controlled_vocab.md | 细胞/组织/平台/工具受控词表 | 改词表 → 05 提取判定、stats 统计 |
| 03_retrieval.md | PubMed/GEO 检索式 + 分层下载 | 相对独立 |
| 04_prescreen.md | 预筛 SOP + DeepSeek prompt | 卡片 10 字段要和 06 一致 |
| 05_extraction.md | 提取 SOP + prompt + few-shot | JSON 结构要和 07 脚本一致 |
| 06_qq_protocol.md | QQ 协议（卡片/解析/回写）| 卡片字段要和 04 一致 |
| 07_scripts/*.py | validate/dedupe/ingest/stats | 字段/枚举要和 01 schema 一致 |
| 08_runbook.md / README.md | 执行手册 / 导航 | 改流程或命令后同步 |

## 跨文件一致性铁律（最易踩坑，改前必查）
1. **提取 JSON = per-dataset 结构**：`{dataset_id, dataset{}, cell_types[], cell_subtypes[], processing{}, _self_check{}}`（cell_subtypes 可选，无亚群则 `[]`），**无 paper 对象**。05 的 few-shot、07 的 validate/ingest 必须三方逐字一致。
2. **字段名/枚举** 以 01_schema.md 为唯一真源；改枚举要同步 `validate.py` 的白名单常量（SPECIES/REPOSITORY/DATA_AVAIL/各 PROC_*/CST_* 等）。新表/新字段还要同步 `ingest.py` 的 HEADERS + DDL（建表顺序 papers→datasets→cell_types→cell_subtypes→processing）。
3. **预筛卡片 10 字段** 在 04 与 06 必须逐字一致。
4. **paper_id 由 `ingest.py --paper-id` 传入**，不在 JSON；内部 ID（ct_id/proc_id）脚本赋号（`__AUTO__`）。
5. **marker 大小写**：人全大写 / 鼠·大鼠首字母大写；`cell_types.species` 单值（混合物种拆行）。
6. **去重键 = dataset_id**（GSE 优先）；同数据集多文章只追加 paper_ids、不重复 cell_types。

## 改完必做：跑测试验证（verification-before-completion）
```bash
# 在本包根目录下执行
PYTHONIOENCODING=utf-8 python design/07_scripts/tests/test_scripts.py
```
预期 **11/11 全绿**：validate 合法通过 / 非法物种·provenance·未知字段·嵌套分号·enrichment 拦截、ingest 入库+幂等+外键+cell_subtypes+paper_id 回填、stats 生成。
改了 schema/脚本后这一步**不能跳**——之前 workflow 的验证 agent 翻过车，断链 bug 就是漏验证导致的。

## 关键设计决策（别轻易推翻）
- 结构化 5 表(CSV) + SQLite + Markdown 卡片；CSV 为真源，SQLite 由脚本重建
- **5 表** = papers / datasets / cell_types / cell_subtypes(细胞亚群详表,PK `S00001`,记 SC-Keloid 等亚群) / processing；processing 含 `enrichment`(富集分析,GO/KEGG/GSEA)字段。均经 TDD + 全 design 同步落地，旧数据填 NA 不回填
- per-dataset 提取（非 per-paper），应对多 GSE 文章
- 确定性活（去重/校验/入库/统计）用 Python 不用 LLM
- **运行期不调 Claude**（规避 2026-06-15 起 `-p` 按 API 计费 + 订阅套利政策风险）
- 检索不用谷歌（校园网环境），PubMed/GEO 为主；下载分层 OA→校园网
- DeepSeek 模型名 = `deepseek-v4-pro`（不带 `[1m]`），summarizer = `deepseek-v4-flash`
- Windows 跑脚本设 `PYTHONIOENCODING=utf-8`
- chromaffin cell / olfactory sensory neuron 标 `context`（is_pns_cell 填 NA 交人工）

## 审查历史
小钰(Hermes)做过一轮设计审查（本包 `design_review.md`，11 条）：已采纳 #3/#5/#7/#8/#10/#11；#1/#2 按 YAGNI 未做；#4/#6/#9 为误读。改设计时可参考。
