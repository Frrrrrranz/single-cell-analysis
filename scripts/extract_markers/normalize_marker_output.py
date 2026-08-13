"""对既有 schema v2 marker JSON 应用确定性证据护栏。"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

from marker_schema import apply_payload_guardrails, validate_payload

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def normalize_file(input_path: Path, output_path: Path) -> dict[str, int]:
    with input_path.open("r", encoding="utf-8") as stream:
        payload = json.load(stream)
    validate_payload(payload)
    counts = apply_payload_guardrails(payload)
    validate_payload(payload)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="规范化既有 marker 提取 JSON")
    parser.add_argument("input", type=Path, help="输入的 *_raw.json")
    parser.add_argument("--output", type=Path, help="输出路径；默认原地更新")
    args = parser.parse_args()

    output_path = args.output or args.input
    counts = normalize_file(args.input, output_path)
    logger.info(
        "规范化完成: %s（证据降级 %d，极性降级 %d）",
        output_path,
        counts["evidence_downgraded"],
        counts["polarity_downgraded"],
    )


if __name__ == "__main__":
    main()
