"""
run_extraction.py — PDF → LLM → JSON 提取管线

功能：
1. 遍历 papers/ 目录下的所有 .full.pdf 文件（传统模式）
2. 或从扁平 PDF 目录读取文件（--flat-pdf-dir + --paper-map 模式）
3. 用 markitdown 将 PDF 转为 Markdown 文本
4. (可选) 按章节分块，防止超过 LLM 上下文窗口
5. 使用 LLM API 提取细胞类型和 marker 基因
6. 保存结构化 JSON 到 markers_output/ 目录

用法：
    python run_extraction.py [--paper-dir DIR] [--output-dir DIR] [--paper-id PID]
                              [--skip-existing] [--dry-run] [--max-chars 80000]
    python run_extraction.py --pdf PATH [--paper-id PID] ...
    python run_extraction.py --flat-pdf-dir DIR --paper-map MAP.json [--paper-id PID] ...

依赖：
    pip install markitdown openai python-dotenv
"""
import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# 加载 .env 文件（优先项目根目录）
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)
    logger.info(f"已加载 .env: {dotenv_path}")

PROJECT_ROOT = Path(r"D:\OneDrive\Desktop\组")
PAPERS_DIR = PROJECT_ROOT / "papers"
OUTPUT_DIR = Path(__file__).parent / "markers_output"
PROMPT_FILE = Path(__file__).parent / "prompts" / "extract_markers.txt"

# 用于分块的最大字符数（~80k chars ≈ 20k tokens 的中英文混合文本）
DEFAULT_MAX_CHARS = 80_000


def read_prompt() -> str:
    """读取提示词模板"""
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()


def find_pdf_files(papers_dir: Path, paper_id: Optional[str] = None) -> list[tuple[str, Path]]:
    """遍历 papers/ 目录，找到所有 .full.pdf 文件

    返回: [(paper_id, pdf_path), ...]
    """
    pdfs: list[tuple[str, Path]] = []
    if not papers_dir.exists():
        logger.error(f"论文目录不存在: {papers_dir}")
        return pdfs

    for subdir in sorted(papers_dir.iterdir()):
        if not subdir.is_dir():
            continue
        if paper_id and paper_id not in subdir.name:
            continue
        pdf_file = subdir / f"{subdir.name}.full.pdf"
        if pdf_file.exists():
            pdfs.append((subdir.name, pdf_file))
            logger.info(f"  发现: {subdir.name}")

    if paper_id and not pdfs:
        # 也直接在 papers/ 下搜索
        for subdir in sorted(papers_dir.iterdir()):
            if paper_id in subdir.name:
                pdf_file = subdir / f"{subdir.name}.full.pdf"
                if pdf_file.exists():
                    pdfs.append((subdir.name, pdf_file))
                    break

    return pdfs


def find_pdf_files_flat(pdf_dir: Path, paper_map: dict[str, str],
                        paper_id: Optional[str] = None) -> list[tuple[str, Path]]:
    """遍历扁平 PDF 目录，用映射表匹配 paper_id

    paper_map: {pdf_filename: paper_id}
    """
    pdfs: list[tuple[str, Path]] = []
    if not pdf_dir.exists():
        logger.error(f"PDF 目录不存在: {pdf_dir}")
        return pdfs

    for pdf_file in sorted(pdf_dir.iterdir()):
        if pdf_file.suffix.lower() != '.pdf':
            continue
        pid = paper_map.get(pdf_file.name)
        if pid is None:
            continue
        if paper_id and pid != paper_id:
            continue
        pdfs.append((pid, pdf_file))
        logger.info(f"  发现: {pid} -> {pdf_file.name}")

    if not pdfs:
        logger.warning(f"  未找到匹配的 PDF（共 {len(list(pdf_dir.glob('*.pdf')))} 个 PDF 文件）")
    return pdfs


def load_paper_map(map_path: Path) -> dict[str, str]:
    """加载 paper_id 映射 JSON"""
    if not map_path.exists():
        logger.error(f"映射表不存在: {map_path}")
        return {}
    with open(map_path, "r", encoding="utf-8") as f:
        return json.load(f)


def convert_pdf_to_text(pdf_path: Path) -> Optional[str]:
    """将 PDF 转换为纯文本

    优先使用 markitdown，回退到 PyPDF2 → pdfminer
    """
    text = None

    # 尝试 markitdown
    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(str(pdf_path))
        text_content = result.text_content
        if text_content and len(text_content) > 100:
            logger.info("  使用 markitdown 转换成功")
            return text_content
    except ImportError:
        logger.info("  markitdown 未安装，尝试回退方案")
    except Exception as e:
        logger.warning(f"  markitdown 转换失败: {e}")

    # 回退 PyPDF2
    try:
        import PyPDF2
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            parts = []
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    parts.append(f"--- Page {page_num + 1} ---\n{page_text}")
            text = "\n\n".join(parts)
            if text and len(text) > 100:
                logger.info("  使用 PyPDF2 转换成功")
                return text
    except ImportError:
        logger.info("  PyPDF2 未安装")
    except Exception as e:
        logger.warning(f"  PyPDF2 转换失败: {e}")

    # 回退 pdfminer
    try:
        from pdfminer.high_level import extract_text
        text = extract_text(str(pdf_path))
        if text and len(text) > 100:
            logger.info("  使用 pdfminer 转换成功")
            return text
    except ImportError:
        logger.info("  pdfminer 未安装")
    except Exception as e:
        logger.warning(f"  pdfminer 转换失败: {e}")

    return text


def split_into_chunks(text: str, max_chars: int = DEFAULT_MAX_CHARS) -> list[tuple[str, str]]:
    """按章节将文本分块

    返回: [(section_name, section_content), ...]
    """
    # 尝试识别常见章节标题
    section_patterns = [
        r"(?i)^#{1,3}\s*(Abstract|Introduction|Results|Discussion|Methods"
        r"|Materials and Methods|Experimental Procedures|Figure Legends?"
        r"|Supplementary|References|Acknowledgments)\b",
        r"(?i)^(Abstract|Introduction|Results|Discussion|Methods"
        r"|Materials and Methods|Figure Legends?|Supplementary)\s*\n",
    ]

    chunks: list[tuple[str, str]] = []
    current_section = "preamble"
    current_lines: list[str] = []

    for line in text.split("\n"):
        is_section_header = False
        for pattern in section_patterns:
            m = re.match(pattern, line.strip())
            if m:
                if current_lines:
                    content = "\n".join(current_lines).strip()
                    if content:
                        chunks.append((current_section, content))
                current_section = m.group(1) if m.lastindex else m.group(0).strip()
                current_lines = []
                is_section_header = True
                break
        if not is_section_header:
            current_lines.append(line)

    if current_lines:
        content = "\n".join(current_lines).strip()
        if content:
            chunks.append((current_section, content))

    # 过滤无用章节
    skip_sections = {"References", "Acknowledgments", "Author contributions",
                     "Conflict of interest", "Data availability"}
    filtered = [(name, content) for name, content in chunks
                if name.lower() not in {s.lower() for s in skip_sections}]

    # 如果按章节分块后还有大块超过 max_chars，则按字符数硬切
    result: list[tuple[str, str]] = []
    for name, content in filtered:
        if len(content) <= max_chars:
            result.append((name, content))
        else:
            # 按段落切
            paragraphs = content.split("\n\n")
            sub_parts: list[str] = []
            sub_size = 0
            part_idx = 0
            for para in paragraphs:
                if sub_size + len(para) > max_chars and sub_parts:
                    result.append((f"{name}_part{part_idx}", "\n\n".join(sub_parts)))
                    part_idx += 1
                    sub_parts = []
                    sub_size = 0
                sub_parts.append(para)
                sub_size += len(para)
            if sub_parts:
                result.append((f"{name}_part{part_idx}", "\n\n".join(sub_parts)))

    return result


def call_llm_api(system_prompt: str, user_content: str,
                 model: Optional[str] = None, api_key: Optional[str] = None,
                 api_base: Optional[str] = None) -> Optional[str]:
    """调用 LLM API 进行提取

    优先使用 OpenAI 兼容接口。可通过环境变量配置：
        MARKER_LLM_API_KEY
        MARKER_LLM_API_BASE
        MARKER_LLM_MODEL
    """
    api_key = api_key or os.environ.get("MARKER_LLM_API_KEY", "")
    api_base = api_base or os.environ.get("MARKER_LLM_API_BASE", "")
    model = model or os.environ.get("MARKER_LLM_MODEL", "deepseek-v4-flash")

    if not api_key:
        logger.error("未设置 LLM API Key。请设置 MARKER_LLM_API_KEY 环境变量")
        return None

    try:
        from openai import OpenAI
    except ImportError:
        logger.error("需要安装 openai 库: pip install openai")
        return None

    client_kwargs = {"api_key": api_key}
    if api_base:
        client_kwargs["base_url"] = api_base

    try:
        client = OpenAI(**client_kwargs)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"LLM API 调用失败: {e}")
        return None


def merge_json_results(results: list[Optional[str]]) -> dict:
    """合并多个分块的 JSON 结果

    处理去重：同一 cell_type + subtype + gene 组合只保留证据等级最高的
    """
    merged: dict = {"paper_id": "", "cell_types": []}

    cell_type_map: dict[str, dict] = {}
    evidence_rank = {"explicit": 4, "implied": 3, "inferred": 2, "imported": 1}

    for result_str in results:
        if not result_str:
            continue
        try:
            data = json.loads(result_str)
        except json.JSONDecodeError:
            logger.warning(f"  跳过无效 JSON: {result_str[:200]}")
            continue

        if not merged["paper_id"] and data.get("paper_id"):
            merged["paper_id"] = data["paper_id"]

        for ct in data.get("cell_types", []):
            ct_key = f"{ct.get('cell_type', '')}|{ct.get('subtype', '')}"
            if ct_key not in cell_type_map:
                cell_type_map[ct_key] = {
                    "cell_type": ct["cell_type"],
                    "subtype": ct.get("subtype"),
                    "markers": [],
                }

            # 去重 markers
            existing_genes: dict[str, int] = {}
            for m in cell_type_map[ct_key]["markers"]:
                existing_genes[m["gene"]] = evidence_rank.get(m["evidence_level"], 0)

            for m in ct.get("markers", []):
                gene = m["gene"]
                new_rank = evidence_rank.get(m["evidence_level"], 0)
                if gene in existing_genes:
                    if new_rank > existing_genes[gene]:
                        # 替换为更高证据等级
                        cell_type_map[ct_key]["markers"] = [
                            x for x in cell_type_map[ct_key]["markers"]
                            if x["gene"] != gene
                        ]
                        cell_type_map[ct_key]["markers"].append(m)
                        existing_genes[gene] = new_rank
                else:
                    cell_type_map[ct_key]["markers"].append(m)
                    existing_genes[gene] = new_rank

    merged["cell_types"] = list(cell_type_map.values())
    return merged


def process_paper(paper_id: str, pdf_path: Path, args: argparse.Namespace) -> bool:
    """处理单篇论文，返回是否成功"""
    logger.info(f"\n{'='*60}")
    logger.info(f"处理论文: {paper_id}")
    logger.info(f"  PDF: {pdf_path}")

    output_file = OUTPUT_DIR / f"{paper_id}_raw.json"
    if args.skip_existing and output_file.exists():
        logger.info(f"  跳过（已存在）: {output_file}")
        return True

    # 1. 转换 PDF → 文本
    logger.info("  [1/4] 转换 PDF → 文本...")
    text = convert_pdf_to_text(pdf_path)
    if not text:
        logger.error(f"  无法提取文本: {paper_id}")
        return False

    text_len = len(text)
    logger.info(f"  文本长度: {text_len:,} 字符")

    # 2. 按章节分块
    logger.info("  [2/4] 按章节分块...")
    chunks = split_into_chunks(text, max_chars=args.max_chars)
    logger.info(f"  分块: {len(chunks)} 块")
    for name, content in chunks:
        logger.info(f"    - {name}: {len(content):,} chars")

    if args.dry_run:
        logger.info("  [DRY RUN] 跳过 LLM 调用")
        return True

    # 3. 对每块调用 LLM
    logger.info("  [3/4] 调用 LLM 提取...")
    prompt = read_prompt()
    results: list[Optional[str]] = []

    for idx, (section_name, section_content) in enumerate(chunks):
        logger.info(f"  处理块 {idx+1}/{len(chunks)}: {section_name}")
        user_content = (
            f"以下论文文本来自 [{paper_id}] 的 {section_name} 章节。\n"
            f"请从中提取所有细胞类型及其 marker 基因。\n\n"
            f"论文文本:\n{section_content}"
        )
        result = call_llm_api(prompt, user_content,
                              model=args.model, api_key=args.api_key)
        if result:
            results.append(result)
            logger.info(f"    块 {idx+1} 提取完成")
        else:
            logger.warning(f"    块 {idx+1} 提取失败")
        # 避免 API 限流
        if idx < len(chunks) - 1:
            time.sleep(1)

    if not results:
        logger.error("  LLM 提取全部失败")
        return False

    # 4. 合并 & 保存
    logger.info("  [4/4] 合并并保存结果...")
    merged = merge_json_results(results)
    merged["paper_id"] = paper_id

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    n_cell_types = len(merged.get("cell_types", []))
    n_markers = sum(len(ct.get("markers", [])) for ct in merged.get("cell_types", []))
    logger.info(f"  ✅ 完成: {n_cell_types} 个细胞类型, {n_markers} 个 marker")
    logger.info(f"  保存到: {output_file}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF → LLM → JSON Marker 提取管线")
    parser.add_argument("--paper-dir", default=str(PAPERS_DIR),
                        help=f"论文目录 (默认: {PAPERS_DIR})")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR),
                        help=f"输出目录 (默认: {OUTPUT_DIR})")
    parser.add_argument("--paper-id", help="指定处理某篇论文 (子目录名 或 映射表中的 ID)")
    parser.add_argument("--skip-existing", action="store_true",
                        help="跳过已有输出文件的论文")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅显示会处理哪些论文，不调用 LLM")
    parser.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS,
                        help=f"单块最大字符数 (默认: {DEFAULT_MAX_CHARS})")
    parser.add_argument("--model", default=None,
                        help="LLM 模型名 (默认: 读取 MARKER_LLM_MODEL 环境变量)")
    parser.add_argument("--api-key", help="LLM API Key (默认: MARKER_LLM_API_KEY 环境变量)")
    # 单文件模式
    parser.add_argument("--pdf", help="直接指定单个 PDF 文件路径")
    # 扁平目录模式
    parser.add_argument("--flat-pdf-dir", help="扁平 PDF 目录（所有 PDF 在同一层）")
    parser.add_argument("--paper-map", help="paper_id 映射 JSON 文件路径")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 模式 1: 单 PDF 文件
    if args.pdf:
        pdf_path = Path(args.pdf)
        if not pdf_path.exists():
            logger.error(f"PDF 文件不存在: {pdf_path}")
            sys.exit(1)
        paper_id = args.paper_id or pdf_path.stem
        logger.info(f"单文件模式: {paper_id} -> {pdf_path}")
        pdfs = [(paper_id, pdf_path)]

    # 模式 2: 扁平目录模式
    elif args.flat_pdf_dir:
        if not args.paper_map:
            logger.error("扁平目录模式需要 --paper-map 参数")
            sys.exit(1)
        paper_map = load_paper_map(Path(args.paper_map))
        if not paper_map:
            sys.exit(1)
        logger.info(f"扁平目录模式: {args.flat_pdf_dir} (映射表: {len(paper_map)} 项)")
        pdfs = find_pdf_files_flat(Path(args.flat_pdf_dir), paper_map,
                                   paper_id=args.paper_id)

    # 模式 3: 传统 papers/ 目录模式
    else:
        papers_dir = Path(args.paper_dir)
        logger.info(f"扫描论文目录: {papers_dir}")
        pdfs = find_pdf_files(papers_dir, paper_id=args.paper_id)

    if not pdfs:
        logger.error("未找到任何 PDF 文件")
        sys.exit(1)
    logger.info(f"找到 {len(pdfs)} 篇论文")

    # 处理每篇论文
    success = 0
    for paper_id, pdf_path in pdfs:
        if process_paper(paper_id, pdf_path, args):
            success += 1

    logger.info(f"\n{'='*60}")
    logger.info(f"完成: {success}/{len(pdfs)} 篇论文成功处理")


if __name__ == "__main__":
    main()
