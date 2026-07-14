"""
gen_review_sheet.py — 生成人工复核用 CSV

功能：
1. 读取 LLM 提取的 JSON 文件（{paper_id}_raw.json）
2. 按人工核对的阅读顺序生成 CSV
3. 每行一个 marker，包含复核所需全部字段

用法：
    python gen_review_sheet.py [--input-dir markers_output] [--output-dir markers_output]
                               [--paper-id PID] [--all]

输出：
    markers_output/{paper_id}_review.csv

列顺序（按阅读顺序）：
    cell_type | gene_symbol | evidence_level | source_section | source_context
    | review_status | notes
"""
import argparse
import csv
import json
import logging
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_DIR = Path(__file__).parent / "markers_output"

REVIEW_HEADERS = [
    "cell_type",
    "subtype",
    "gene_symbol",
    "evidence_level",
    "source_section",
    "source_context",
    "review_status",
    "notes",
]

EVIDENCE_ORDER = {"explicit": 1, "implied": 2, "inferred": 3, "imported": 4}


def find_json_files(input_dir: Path, paper_id: Optional[str] = None) -> list[Path]:
    """查找 *_raw.json 文件"""
    pattern = f"{paper_id}_raw.json" if paper_id else "*_raw.json"
    files = sorted(input_dir.glob(pattern))
    return files


def generate_review_sheet(json_path: Path, output_dir: Path) -> Optional[Path]:
    """从 JSON 生成复核 CSV，返回输出文件路径"""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    paper_id = data.get("paper_id", json_path.stem.replace("_raw", ""))
    output_path = output_dir / f"{paper_id}_review.csv"

    rows: list[dict] = []
    for ct in data.get("cell_types", []):
        cell_type = ct.get("cell_type", "unknown")
        subtype = ct.get("subtype") or ""
        for m in ct.get("markers", []):
            rows.append({
                "cell_type": cell_type,
                "subtype": subtype,
                "gene_symbol": m.get("gene", ""),
                "evidence_level": m.get("evidence_level", "inferred"),
                "source_section": m.get("source_section", ""),
                "source_context": m.get("source_context", ""),
                "review_status": "pending",
                "notes": "",
            })

    # 按证据等级排序（explicit 在前），同一等级内按 cell_type 排序
    rows.sort(key=lambda r: (
        EVIDENCE_ORDER.get(r["evidence_level"], 99),
        r["cell_type"],
        r["gene_symbol"],
    ))

    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=REVIEW_HEADERS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    logger.info(f"  生成复核表: {output_path} ({len(rows)} 行)")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="生成人工复核 CSV")
    parser.add_argument("--input-dir", default=str(DEFAULT_DIR),
                        help="JSON 输入目录")
    parser.add_argument("--output-dir", default=str(DEFAULT_DIR),
                        help="CSV 输出目录")
    parser.add_argument("--paper-id", help="指定论文 ID")
    parser.add_argument("--all", action="store_true",
                        help="处理所有 JSON 文件")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    json_files = find_json_files(input_dir, paper_id=args.paper_id)
    if not json_files:
        logger.error(f"未找到 JSON 文件 in {input_dir}")
        if args.paper_id:
            logger.error(f"  匹配 pattern: {args.paper_id}_raw.json")
        return

    if not args.all and not args.paper_id:
        logger.info(f"找到 {len(json_files)} 个 JSON 文件。使用 --all 处理全部，或 --paper-id 指定一个。")
        for f in json_files:
            logger.info(f"  {f.name}")
        return

    for json_path in json_files:
        out = generate_review_sheet(json_path, output_dir)
        if out:
            logger.info(f"✅ {out.name}")

    logger.info("\n复核表生成完成。请用 Excel/WPS 打开 CSV 进行复核。")


if __name__ == "__main__":
    main()
