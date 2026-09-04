# -*- coding: utf-8 -*-
"""证据包生成器（recheck-pipeline-v2 第 1+2 级合并实现）.

第 1 级 triage：噪声词库 v2 自动杀、已收录自动标、状态词守卫；
第 2 级 evidence pack：按句子切片聚合原文片段，主代理读包直判。

用法:
    python build_evidence_pack.py <paper_id> [<paper_id> ...]
输出:
    marker提取/audits/recheck-2026-09-02/batch1_work/<pid>_pack.md
"""
import io
import os
import re
import sys

BASE = r"D:\OneDrive\Desktop\组\marker提取"
WORK = os.path.join(BASE, "audits", "recheck-2026-09-02", "batch1_work")

NOISE = {
    # 队列/数据库
    "ASSESS", "BKBC", "KPMP", "GRCm38", "NCBI", "HPA", "HLCA",
    # 疾病缩写
    "AKI", "CKD", "ESKD", "IPF", "COPD", "MERS",
    # 组蛋白修饰
    "H3K27AC", "H3K4ME1", "H3K27ME3",
    # 细胞/组织名
    "AT2", "AT1", "NP1", "NP2", "NP3", "H10", "H12", "SMG", "NAF", "ASM", "TAL", "DRG",
    # 方法/工具
    "MERFISH", "GSEA", "ISH", "MAST", "MACS", "FACS", "IMS", "SHAP", "MBCO", "VDJ",
    "PLMM", "EMT", "LTSR", "CUT", "RUN", "MCC",
    # 试剂/货号/克隆号
    "S34857", "SK3", "HIB19", "RPA-T4", "M0293L",
    # 代谢物
    "G6P", "BPG",
    # 断行/截断
    "BRO1", "NKX2",
    # 流式描述
    "CD68HI", "CD4HI", "CD8LO", "CD45RA",
    # 非基因通名
    "ECM",
}

STAT_WORDS = {"cycling", "mature", "immature", "proliferating", "activated",
              "memory", "naive", "signalling", "signaling", "resident"}

MARKER_WORDS = re.compile(
    r"marker|marked by|canonical|signature|defined by|characteriz|specifically", re.I)
# 双栏拼接特征：基因命中点附近出现统计/方法词
ARTIFACT_WORDS = re.compile(
    r"MCC|Matthews|correlation coefficient|n = \d|P ?[<=]|t-test|regression|Benjamini", re.I)


def parse_candidates(text):
    """candidates.md -> {gate: [cand_dict,...]}"""
    sections, gate, cand = {}, None, None
    for line in text.split("\n"):
        m = re.match(r"^## (\S+)\s*$", line)
        if m:
            gate = m.group(1)
            sections.setdefault(gate, [])
            cand = None
            continue
        m = re.match(r"^### 候选(\d+)", line)
        if m and gate:
            cand = {"_no": int(m.group(1))}
            sections[gate].append(cand)
            continue
        if cand is not None and line.startswith("- "):
            body = line[2:]
            if ": " in body:
                k, v = body.split(": ", 1)
                cand[k] = v.strip()
    return sections


def parse_existing(text):
    rows = []
    for line in text.split("\n"):
        m = re.match(r"^## 行(\d+): (.*)$", line)
        if not m:
            continue
        d = {"_row": int(m.group(1))}
        for kv in m.group(2).split(" | "):
            if "=" in kv:
                k, v = kv.split("=", 1)
                d[k] = v
        rows.append(d)
    return rows


def load_review(pid):
    path = os.path.join(BASE, "review_md", pid + ".md")
    with io.open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def slice_around(line, positions, term, radius=260):
    """长行内按命中点切窗口，重叠区间合并。返回 [(start,text),...]"""
    spans = []
    for p in positions:
        s, e = max(0, p - radius), min(len(line), p + len(term) + radius)
        if spans and s <= spans[-1][1] + 60:
            spans[-1] = (spans[-1][0], e)
        else:
            spans.append((s, e))
    return [(s, line[s:e]) for s, e in spans]


def find_hits(lines, term, limit=12, prefer_marker=True):
    """返回 {line_idx: [(start, text), ...]}"""
    rx = re.compile(r"\b" + re.escape(term) + r"\b", re.I)
    raw = {}
    for i, l in enumerate(lines):
        for m in rx.finditer(l):
            raw.setdefault(i, []).append(m.start())
    if not raw:
        return {}
    if len(raw) > limit and prefer_marker:
        keep = [i for i in raw if MARKER_WORDS.search(lines[i])]
        rest = [i for i in raw if i not in keep]
        ordered = keep + sorted(rest)
        raw = {i: raw[i] for i in ordered[:limit]}
    else:
        raw = {i: raw[i] for i in sorted(raw)[:limit]}
    out = {}
    for i, ps in raw.items():
        out[i] = slice_around(lines[i], ps, term)
    return out


def extract_ngrams(sentence, n=5, max_out=2):
    """从证据句提取长 n-gram 用于精确定位（跨行断词可能失败，仅作补充）。"""
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-']*", sentence)
    grams = []
    for size in (7, 6, 5, 4):
        for i in range(len(words) - size + 1):
            g = words[i:i + size]
            if any(len(w) <= 2 for w in g):
                continue
            grams.append(g)
        if grams:
            break
    return [" ".join(g[:n]) for g in grams[:max_out]]


class Pack:
    def __init__(self, pid):
        self.pid = pid
        self.lines = load_review(pid)
        self.frag_id = 0
        self.frags = []          # list of (line_idx, text, terms)

    def add(self, line_idx, text, terms):
        for k, (i, t, _) in enumerate(self.frags):
            if i == line_idx and text[:80] in t:
                return k + 1
        self.frags.append((line_idx, text, terms))
        return len(self.frags)

    def collect(self, terms, limit=5, max_frags=3):
        """对一组搜索词收集片段，返回片段号列表。"""
        ids = []
        for term in terms:
            if not term or len(term) < 3:
                continue
            hits = find_hits(self.lines, term, limit=limit)
            for i, slices in hits.items():
                for _, text in slices:
                    fid = self.add(i, text, term)
                    ids.append(fid)
            if len(set(ids)) >= max_frags:
                break
        return sorted(set(ids))[:max_frags]

    def render(self):
        out = []
        order = sorted(range(len(self.frags)), key=lambda k: (self.frags[k][0], k))
        for k in order:
            i, text, terms = self.frags[k]
            flag = ""
            if ARTIFACT_WORDS.search(text):
                flag = " **[疑似双栏拼接:句内混入统计方法词，重组核实后再判]**"
            text = text.replace("|", "\\|")
            out.append("### 片段%d [L%d · %s]%s\n```\n%s\n```" % (
                k + 1, i + 1, terms, flag, text))
        return "\n\n".join(out)

    def map_id(self, ids):
        return sorted(set(ids))


def existing_index(existing_rows):
    """(cell_type_lower±subtype, gene_lower) -> count; 另建 gene -> set(cell_type)"""
    idx = {}
    gene_map = {}
    for r in existing_rows:
        ct = (r.get("cell_type", "") + " " + r.get("subtype", "")).strip().lower()
        g = r.get("gene_symbol", "").lower()
        idx[(ct, g)] = idx.get((ct, g), 0) + 1
        gene_map.setdefault(g, set()).add(r.get("cell_type", "?"))
    return idx, gene_map


def build(pid):
    cand_path = os.path.join(WORK, pid + "_candidates.md")
    exist_path = os.path.join(WORK, pid + "_existing.md")
    with io.open(cand_path, encoding="utf-8") as f:
        cands = parse_candidates(f.read())
    with io.open(exist_path, encoding="utf-8") as f:
        existing = parse_existing(f.read())

    pack = Pack(pid)
    idx, gene_map = existing_index(existing)

    out = ["# %s 证据包（recheck-pipeline-v2 自动生成）\n" % pid]

    # ---- 0. 总表防重复摘要 ----
    out.append("## 0. 总表现有行（防重复补录；格式 cell_type|gene|evidence_type|locator）\n")
    seen = set()
    for r in existing:
        key = (r.get("cell_type"), r.get("gene_symbol"), r.get("evidence_type"))
        if key in seen:
            continue
        seen.add(key)
        out.append("- %s | %s | %s | %s" % (r.get("cell_type"), r.get("gene_symbol"),
                                            r.get("evidence_type"), r.get("source_locator", "")))
    out.append("")

    # ---- A 门 ----
    a_rows = []
    for c in cands.get("A_漏提候选", []):
        gene = c.get("候选基因", "")
        vocab = c.get("跨篇词表命中", "否") == "是"
        ev = c.get("证据句（原文，[章节]前缀）", "")
        auto = ""
        if gene.upper() in NOISE and not vocab:
            auto = "自动判:不录-噪声token(%s)" % gene.upper()
        else:
            ct_hit = gene_map.get(gene.lower())
            if ct_hit:
                auto = "自动标:总表已有该基因(%s)，核对是否同细胞重复" % ";".join(sorted(ct_hit)[:3])
        terms = [gene] + extract_ngrams(ev)
        fids = [] if auto.startswith("自动判") else pack.collect(terms)
        a_rows.append((c["_no"], gene, vocab, auto, ev, fids))
    out.append("## A 门候选 %d 条\n" % len(a_rows))
    out.append("| # | 基因 | 词表 | 自动分流 | 片段 | 证据句提示（截断，完整见片段） |")
    out.append("|---|---|---|---|---|---|")
    frag_lines = []
    for no, gene, vocab, auto, ev, fids in a_rows:
        fragref = ",".join("F%d" % x for x in pack.map_id(fids)) if fids else "-"
        hint = ev[:110].replace("|", "\\|")
        out.append("| %d | %s | %s | %s | %s | %s |" % (no, gene, "是" if vocab else "-",
                                                        auto or "人工判", fragref, hint))
        if fids:
            frag_lines.append((no, pack.map_id(fids)))
    out.append("")

    # ---- B 门 ----
    b_rows = []
    for c in cands.get("B_证据类型候选", []):
        gene = c.get("gene", "")
        ctx = c.get("source_context", "")
        terms = [gene] + extract_ngrams(ctx)
        fids = pack.collect(terms)
        b_rows.append((c, fids))
    out.append("## B 门候选 %d 条（升级 author_declared 审查）\n" % len(b_rows))
    out.append("| mid | gene | cell_type | 片段 | 当前context |")
    out.append("|---|---|---|---|---|")
    for c, fids in b_rows:
        fragref = ",".join("F%d" % x for x in pack.map_id(fids)) if fids else "未定位"
        ctx = c.get("source_context", "")[:90].replace("|", "\\|")
        out.append("| %s | %s | %s | %s | %s |" % (c.get("marker_id"), c.get("gene"),
                                                   c.get("cell_type"), fragref, ctx))
    out.append("")

    # ---- B2 门 ----
    b2_rows = []
    for c in cands.get("B2_补充候选", []):
        gene = c.get("gene", "")
        ctx = c.get("source_context", "")
        terms = [gene] + extract_ngrams(ctx)
        fids = pack.collect(terms)
        b2_rows.append((c, fids))
    out.append("## B2 门候选 %d 条\n" % len(b2_rows))
    for c, fids in b2_rows:
        fragref = ",".join("F%d" % x for x in pack.map_id(fids)) if fids else "未定位"
        out.append("- [%s] %s | %s | %s | recovery=%s | 片段=%s\n  context: %s" % (
            c.get("来源", "?"), c.get("gene"), c.get("cell_type"),
            c.get("evidence_type"), c.get("recovery_outcome", "-"), fragref,
            c.get("source_context", "")))
    out.append("")

    # ---- C 门 ----
    out.append("## C 门候选 %d 条（含两行现值）\n" % len(cands.get("C_语义重复候选", [])))
    for c in cands.get("C_语义重复候选", []):
        gene = c.get("gene", "")
        auto = ""
        r1, r2 = c.get("行1", ""), c.get("行2", "")
        ct1, ct2 = r1.split("/")[0], r2.split("/")[0]
        w1 = set(ct1.lower().replace("(", " ").replace(")", " ").split())
        w2 = set(ct2.lower().replace("(", " ").replace(")", " ").split())
        diff = (w1 - w2) | (w2 - w1)
        if diff & STAT_WORDS:
            auto = "自动判:不合并（状态词差异 %s）" % sorted(diff & STAT_WORDS)
        out.append("- gene=%s | 行1=%s | 行2=%s | %s" % (
            gene, r1, r2, auto or "人工判"))
    out.append("")

    # ---- D 门材料 ----
    out.append("## D 门材料\n### D1 聚类对账：existing cell_type 去重清单（cell_type | 行数 | genes 前12个）\n")
    by_ct = {}
    for r in existing:
        by_ct.setdefault(r.get("cell_type", "?"), []).append(r.get("gene_symbol", "?"))
    for ct in sorted(by_ct):
        gs = by_ct[ct]
        uniq = sorted({g for g in gs}, key=str.lower)
        out.append("- %s | %d | %s" % (ct, len(gs), ", ".join(uniq[:12])))
    out.append("\n### D2 图注/结果节的 marker 句（自动 grep，供整簇漏提对账）\n")
    shown = 0
    for i, l in enumerate(pack.lines):
        low = l.lower()
        if "marker" in low and shown < 60 and (
                "dot plot" in low or "scatter" in low or "umap" in low or
                re.search(r"\b(a|b|c|d|e|f|g|h|i|j), ", l[:6]) or "expression of" in low):
            text = l.replace("|", "\\|")
            if len(text) > 500:
                p = low.index("marker")
                s, e = max(0, p - 250), min(len(text), p + 250)
                text = "…" + text[s:e] + "…"
            out.append("- L%d: %s" % (i + 1, text))
            shown += 1
    out.append("")

    # ---- 片段库 ----
    frag_text = pack.render()
    out.append("## 片段库（review_md 原文切片）\n")
    out.append(frag_text)

    pack_path = os.path.join(WORK, pid + "_pack.md")
    with io.open(pack_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    size = os.path.getsize(pack_path)
    print("%s -> %s (%.1f KB, fragments=%d)" % (pid, os.path.basename(pack_path),
                                                size / 1024.0, len(pack.frags)))


if __name__ == "__main__":
    for pid in sys.argv[1:]:
        build(pid)
