"""生成修正版离线汇总页 marker_summary_audited.html。

数据来自 40 个终审 audit JSON；自包含单文件（内嵌 JSON + 原生 JS 筛选），
不覆盖原始 marker_summary.html。
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

from marker_schema import EVIDENCE_RANK

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
LOGGER = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_AUDIT_DIR = SCRIPT_DIR / "markers_audited"
DEFAULT_OUTPUT = SCRIPT_DIR / "marker_summary_audited.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Marker 全量终审汇总（40 篇 · full audit 2026-08-30）</title>
<style>
:root {
  --bg: #f5f7fa; --card: #ffffff; --ink: #2c3440; --muted: #6b7686;
  --line: #e3e8ef; --accent: #4a7ab5; --accent-soft: #eaf1f8;
  --ok: #3d8f6e; --warn: #b3813a; --bad: #b0563f;
  --chip: #f0f3f7; --chip-active: #4a7ab5;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink);
  font: 14px/1.6 "Segoe UI", "Microsoft YaHei", system-ui, sans-serif; }
.wrap { max-width: 1240px; margin: 0 auto; padding: 28px 20px 60px; }
h1 { font-size: 22px; margin: 0 0 4px; }
.sub { color: var(--muted); font-size: 13px; margin-bottom: 22px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-bottom: 14px; }
.stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; }
.stat .num { font-size: 26px; font-weight: 600; color: var(--accent); }
.stat .label { font-size: 12px; color: var(--muted); margin-top: 2px; }
.panel { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px 20px; margin-top: 16px; }
.panel h2 { font-size: 16px; margin: 0 0 10px; }
.bar-row { display: flex; align-items: center; gap: 10px; margin: 6px 0; font-size: 13px; }
.bar-label { width: 220px; color: var(--muted); text-align: right; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.bar { height: 12px; border-radius: 6px; background: linear-gradient(90deg, #7ba3cc, var(--accent)); min-width: 2px; }
.bar-val { color: var(--muted); font-size: 12px; }
#dist-bars { max-height: 430px; overflow: auto; }
.filters { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 12px; }
select, input { background: var(--chip); border: 1px solid var(--line); border-radius: 8px;
  padding: 6px 10px; color: var(--ink); font-size: 13px; }
input { min-width: 220px; }
table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
th { position: sticky; top: 0; background: var(--card); text-align: left; padding: 8px 10px;
  border-bottom: 2px solid var(--line); color: var(--muted); font-weight: 600; white-space: nowrap; }
td { padding: 7px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
tr:hover td { background: var(--accent-soft); }
.tag { display: inline-block; border-radius: 999px; padding: 1px 9px; font-size: 11px; white-space: nowrap; }
.tag.include { background: #e4f1eb; color: var(--ok); }
.tag.context_only { background: #f4eedd; color: var(--warn); }
.tag.exclude { background: #f3e6e1; color: var(--bad); }
.tag.unresolved { background: #eceded; color: #61666d; }
.mono { font-family: Consolas, "Courier New", monospace; }
.ctx { max-width: 460px; color: var(--muted); font-size: 12px; }
.count { color: var(--muted); font-size: 12px; margin: 4px 0 10px; }
.tabs { display: flex; gap: 8px; margin-bottom: 12px; }
.tab { border: 1px solid var(--line); background: var(--chip); border-radius: 8px;
  padding: 5px 14px; cursor: pointer; font-size: 13px; color: var(--ink); }
.tab.active { background: var(--chip-active); color: #fff; border-color: var(--chip-active); }
.note { color: var(--muted); font-size: 12px; margin-top: 14px; }
.papers { max-height: 560px; overflow: auto; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Marker 全量终审汇总</h1>
  <div class="sub">40 篇论文 · full audit 2026-08-30 · 数据来自 markers_audited/ 终审 JSON · 不覆盖原始 marker_summary.html</div>
  <div id="stats" class="grid"></div>

  <div class="panel">
    <h2>文章状态</h2>
    <div id="status-bars"></div>
  </div>
  <div class="panel">
    <h2>正式 Marker 分布（include）</h2>
    <div id="dist-bars"></div>
  </div>

  <div class="panel">
    <h2>逐篇结果</h2>
    <div class="papers"><table id="papers-table"></table></div>
  </div>

  <div class="panel">
    <h2>Marker 明细</h2>
    <div class="tabs" id="decision-tabs"></div>
    <div class="filters">
      <select id="f-species"><option value="">全部物种</option></select>
      <select id="f-evidence"><option value="">全部证据</option></select>
      <select id="f-paper"><option value="">全部论文</option></select>
      <input id="f-search" placeholder="搜索基因 / 细胞类型 / 基因符号…">
    </div>
    <div class="count" id="row-count"></div>
    <div class="papers"><table id="markers-table"></table></div>
    <div class="note">unresolved/exclude/context_only 视图含被排除与无法回溯的候选，均不进入修正版正式总表。</div>
  </div>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const ALL_DECISIONS = ['include', 'context_only', 'exclude', 'unresolved'];
let activeDecision = 'include';

function el(tag, cls, text) {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function fmt(n) { return n.toLocaleString('zh-CN'); }

(function renderStats() {
  const stats = DATA.stats;
  const items = [
    ['审核论文', stats.papers],
    ['正式 Marker', stats.include],
    ['涉及论文', stats.papers_with_include],
    ['corrected', stats.status.corrected],
    ['pass', stats.status.pass],
    ['no_formal_target_marker', stats.status.no_formal_target_marker],
    ['unresolved 文章', stats.status.unresolved],
    ['排除候选', stats.excluded_records],
  ];
  const root = document.getElementById('stats');
  items.forEach(([label, value]) => {
    const card = el('div', 'stat');
    card.append(el('div', 'num', fmt(value)), el('div', 'label', label));
    root.append(card);
  });
})();

function renderBars(containerId, rows, total) {
  const root = document.getElementById(containerId);
  root.innerHTML = '';
  const maxVal = Math.max(...rows.map(r => r[1]), 1);
  rows.forEach(([label, value]) => {
    const row = el('div', 'bar-row');
    const bar = el('div', 'bar');
    bar.style.width = Math.max((value / maxVal) * 640, 2) + 'px';
    row.append(el('div', 'bar-label', label + '（' + value + '）'), bar, el('div', 'bar-val', (total ? (value / total * 100).toFixed(1) + '%' : '')));
    root.append(row);
  });
}

renderBars('status-bars', Object.entries(DATA.stats.status));
renderBars('dist-bars', [
  ...Object.entries(DATA.stats.by_cell_type).sort((a, b) => b[1] - a[1]).map(([k, v]) => ['细胞: ' + k, v]),
  ...Object.entries(DATA.stats.by_species).map(([k, v]) => ['物种: ' + k, v]),
  ...Object.entries(DATA.stats.by_evidence).map(([k, v]) => ['证据: ' + k, v]),
], DATA.stats.include);

(function renderPapers() {
  const table = document.getElementById('papers-table');
  table.innerHTML = '';
  const head = el('tr');
  ['task', 'paper_id', '目标范围', '物种', '状态', 'include', 'context', 'exclude', 'unresolved'].forEach(h => head.append(el('th', null, h)));
  const thead = el('thead'); thead.append(head); table.append(thead);
  const tbody = el('tbody');
  DATA.papers.forEach(p => {
    const row = el('tr');
    [p.task_no, p.paper_id, p.scope, p.species, p.status, p.include, p.context_only, p.exclude, p.unresolved]
      .forEach(v => row.append(el('td', 'mono', v)));
    tbody.append(row);
  });
  table.append(tbody);
})();

(function renderTabs() {
  const root = document.getElementById('decision-tabs');
  ALL_DECISIONS.forEach(decision => {
    const count = DATA.markers.filter(m => m.decision === decision).length;
    const tab = el('div', 'tab' + (decision === activeDecision ? ' active' : ''), decision + '（' + count + '）');
    tab.onclick = () => {
      activeDecision = decision;
      root.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderMarkers();
    };
    root.append(tab);
  });
})();

(function fillFilters() {
  const unique = (values) => [...new Set(values.filter(Boolean))].sort();
  [['f-species', unique(DATA.markers.map(m => m.species))],
   ['f-evidence', unique(DATA.markers.map(m => m.evidence_type))],
   ['f-paper', unique(DATA.markers.map(m => m.paper_id))]].forEach(([id, values]) => {
    const select = document.getElementById(id);
    values.forEach(v => {
      const option = el('option', null, v);
      option.value = v;
      select.append(option);
    });
    select.onchange = renderMarkers;
  });
  document.getElementById('f-search').oninput = renderMarkers;
})();

function renderMarkers() {
  const species = document.getElementById('f-species').value;
  const evidence = document.getElementById('f-evidence').value;
  const paper = document.getElementById('f-paper').value;
  const query = document.getElementById('f-search').value.trim().toLowerCase();
  const rows = DATA.markers.filter(m => {
    if (m.decision !== activeDecision) return false;
    if (species && m.species !== species) return false;
    if (evidence && m.evidence_type !== evidence) return false;
    if (paper && m.paper_id !== paper) return false;
    if (query && !(`${m.symbol} ${m.cell_type} ${m.paper_id}`.toLowerCase().includes(query))) return false;
    return true;
  });
  document.getElementById('row-count').textContent = '共 ' + rows.length + ' 条';
  const table = document.getElementById('markers-table');
  table.innerHTML = '';
  const head = el('tr');
  ['paper_id', '细胞类型', '亚型', '物种', '基因', '证据类型', '极性', 'decision', 'citation', '定位', '原文证据'].forEach(h => head.append(el('th', null, h)));
  const thead = el('thead'); thead.append(head); table.append(thead);
  const tbody = el('tbody');
  rows.forEach(m => {
    const row = el('tr');
    row.append(el('td', 'mono', m.paper_id));
    row.append(el('td', null, m.cell_type));
    row.append(el('td', null, m.subtype || '—'));
    row.append(el('td', null, m.species));
    row.append(el('td', 'mono', m.symbol));
    row.append(el('td', null, m.evidence_type));
    row.append(el('td', null, m.polarity));
    const decision = el('td');
    decision.append(el('span', 'tag ' + m.decision, m.decision));
    row.append(decision);
    row.append(el('td', null, m.citation === true ? '✓ ' + m.score : '✗ ' + m.score));
    row.append(el('td', 'mono', m.locator || ''));
    row.append(el('td', 'ctx', m.context || ''));
    tbody.append(row);
  });
  table.append(tbody);
}
renderMarkers();
</script>
</body>
</html>
"""


def build_payload(audit_dir: Path) -> dict[str, Any]:
    audits: dict[str, dict[str, Any]] = {}
    for path in sorted(audit_dir.glob("*_audit.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        audits[data["paper_id"]] = data

    markers: list[dict[str, Any]] = []
    status_counts: dict[str, int] = {"pass": 0, "corrected": 0, "no_formal_target_marker": 0, "unresolved": 0}
    papers: list[dict[str, Any]] = []
    papers_with_include: set[str] = set()
    by_species: dict[str, int] = {}
    by_evidence: dict[str, int] = {}
    by_cell_type: dict[str, int] = {}

    def marker_row(paper_id: str, marker: dict[str, Any]) -> dict[str, Any]:
        return {
            "paper_id": paper_id,
            "cell_type": marker.get("cell_type"),
            "subtype": marker.get("subtype"),
            "species": marker.get("species"),
            "symbol": marker.get("normalized_symbol") or marker.get("original_symbol"),
            "original_symbol": marker.get("original_symbol"),
            "evidence_type": marker.get("evidence_type"),
            "polarity": marker.get("marker_polarity"),
            "decision": marker.get("decision"),
            "citation": marker.get("citation_verified"),
            "score": marker.get("citation_match_score"),
            "locator": marker.get("source_locator"),
            "context": marker.get("source_context"),
        }

    for paper_id, data in sorted(audits.items(), key=lambda kv: (kv[1].get("task", {}).get("task_no", 0), kv[0])):
        task = data.get("task", {})
        status_counts[data["paper_status"]] = status_counts.get(data["paper_status"], 0) + 1
        decisions = [marker.get("decision") for marker in data.get("markers", [])]
        papers.append(
            {
                "task_no": task.get("task_no"),
                "paper_id": paper_id,
                "scope": task.get("target_cell_scope", "—"),
                "species": task.get("task_species"),
                "status": data["paper_status"],
                "include": decisions.count("include"),
                "context_only": decisions.count("context_only"),
                "exclude": decisions.count("exclude"),
                "unresolved": decisions.count("unresolved"),
            }
        )

        # include 行按计划 5.7 去重键合并：保留证据等级最高的一条，附加 locator 并入主行，
        # 使 HTML 的 include 计数与 our_markers_audited.xlsx 完全一致。
        include_groups: dict[tuple, list[dict[str, Any]]] = {}
        for marker in data.get("markers", []):
            row = marker_row(paper_id, marker)
            if marker.get("decision") != "include":
                markers.append(row)
                continue
            key = (
                paper_id,
                str(marker.get("cell_type") or "").strip().lower(),
                str(marker.get("subtype") or "").strip().lower(),
                marker.get("species"),
                str(marker.get("normalized_symbol") or "").strip(),
                marker.get("marker_polarity"),
            )
            include_groups.setdefault(key, []).append(row)

        for rows in include_groups.values():
            rows.sort(key=lambda r: -EVIDENCE_RANK.get(r["evidence_type"] or "", 0))
            primary = rows[0]
            for extra in rows[1:]:
                primary["locator"] = f"{primary['locator']}；同键附加证据: {extra['locator']}"
            markers.append(primary)
            papers_with_include.add(paper_id)
            by_species[primary["species"] or "unknown"] = by_species.get(primary["species"] or "unknown", 0) + 1
            by_evidence[primary["evidence_type"] or "unknown"] = by_evidence.get(primary["evidence_type"] or "unknown", 0) + 1
            by_cell_type[primary["cell_type"] or "未知"] = by_cell_type.get(primary["cell_type"] or "未知", 0) + 1

    return {
        "stats": {
            "papers": len(audits),
            "include": sum(1 for marker in markers if marker["decision"] == "include"),
            "papers_with_include": len(papers_with_include),
            "excluded_records": sum(1 for marker in markers if marker["decision"] != "include"),
            "status": status_counts,
            "by_species": by_species,
            "by_evidence": by_evidence,
            "by_cell_type": by_cell_type,
        },
        "papers": papers,
        "markers": markers,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="生成修正版 HTML 汇总页")
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    payload = build_payload(args.audit_dir)
    if payload["stats"]["papers"] != 40:
        raise SystemExit(f"audit JSON 数量不是 40: {payload['stats']['papers']}")
    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(payload, ensure_ascii=False))
    args.output.write_text(html, encoding="utf-8")
    LOGGER.info(
        "生成 %s（include=%d，论文=%d）",
        args.output,
        payload["stats"]["include"],
        payload["stats"]["papers"],
    )


if __name__ == "__main__":
    main()
