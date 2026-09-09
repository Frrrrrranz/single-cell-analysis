from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


RUN_DIR = Path(__file__).resolve().parent
REVIEWS_PATH = RUN_DIR.parent / "execution" / "luna-existing-marker-correctness" / "review-records.json"
SOURCE_DIR = RUN_DIR.parents[1]
EXPECTED_IDS = {
    "M00101", "M00598", "M00711", "M00720", "M00734", "M00737", "M01059", "M01117",
    "M01240", "M01249", "M01256", "M01257", "M01263", "M01264", "M01267", "M01293",
    "M01578", "M01968", "M01973", "M01977", "M02299", "M02306", "M02474", "M02487",
    "M02533", "M02564", "M02570", "M02571", "M00001", "M00002",
}
DEFER_REASONS = {
    "M02299": "现有文本未包含 Figure 2h 的目标 marker 图，仅有二次摘要“C3 marker”；按缺图规则转待议。",
    "M02306": "现有文本未包含 Figure 2h 的目标 marker 图，仅有二次摘要“CD123 marker for pDCs”；按缺图规则转待议。",
    "M02487": "正文只确认 xFB-8 为 peri-arterial fibroblast，并把 DCN 描述为 generic fibroblast marker；缺少 DCN 与 xFB-8 的目标级直接绑定，转待议。",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def current_values(record: dict[str, Any]) -> dict[str, Any]:
    return dict(record.get("after_values") or record["original_values"])


review_doc = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))
rows = [record for record in review_doc["records"] if record["marker_id"] in EXPECTED_IDS]
if {record["marker_id"] for record in rows} != EXPECTED_IDS:
    raise RuntimeError("Final batch ID mismatch")

source_hashes: dict[str, tuple[Path, str]] = {}
decisions = []
for record in sorted(rows, key=lambda item: (item["paper_id"], item["marker_id"])):
    marker_id = record["marker_id"]
    paper_id = record["paper_id"]
    values = current_values(record)
    if paper_id not in source_hashes:
        source_path = SOURCE_DIR / f"{paper_id}.md"
        source_hashes[paper_id] = (source_path, sha256(source_path))
    source_path, source_hash = source_hashes[paper_id]

    if marker_id in DEFER_REASONS:
        decision = "defer_unresolved"
        eligible = False
        after_values = None
        reason = DEFER_REASONS[marker_id]
    elif marker_id == "M02474":
        values["source_locator"] = "Results, spatial fibroblast organization; Fig. 5F; Fig. S5A-B"
        values["source_context"] = "PDGFRA was broadly enriched across lamina propria fibroblast subsets; xFB-1 is the upper/inner lamina propria subset."
        values["notes"] = "Astra 复核补强：PDGFRA 是 lamina propria fibroblast 的广泛 marker，xFB-1 属于该层；不是 xFB-1 特异 marker。"
        values["audit_status"] = "astra_corrected_include"
        values["review_method"] = "astra_source_review_2026-09-09"
        decision = "correct_and_accept"
        eligible = True
        after_values = values
        reason = "正文直接说明 PDGFRA 广泛富集于 lamina propria subsets；补足非特异性限定后可支持 xFB-1 阳性关系。"
    else:
        decision = "accept_current_after_values"
        eligible = True
        after_values = values
        reason = "Astra 对照正文、图注或明确细胞/亚群命名复核，当前目标细胞—marker—极性关系成立。"

    decisions.append(
        {
            "decision_id": f"ASTRA-221-B028-{marker_id}",
            "marker_id": marker_id,
            "paper_id": paper_id,
            "decision": decision,
            "publication_eligible": eligible,
            "after_values": after_values,
            "source_file": str(source_path),
            "source_sha256": source_hash,
            "source_locator": values.get("source_locator"),
            "source_excerpt": values.get("source_context"),
            "astra_reason": reason,
            "reviewed_by": "GPT-6 Astra",
            "reviewed_at": "2026-09-09",
        }
    )

counts = Counter(item["decision"] for item in decisions)
result = {
    "run_id": "20260909-astra-remaining-221",
    "batch_id": "ASTRA-221-B028",
    "paper_id": "mixed-final-remainder",
    "record_count": len(decisions),
    "result_counts": dict(counts),
    "remaining_after_batch": 0,
    "decisions": decisions,
}
(RUN_DIR / "decisions-review-batch-028.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(json.dumps({"record_count": len(decisions), "counts": dict(counts), "remaining": 0}, ensure_ascii=False))
