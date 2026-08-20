"""
run_extraction.py — PDF → LLM → JSON 提取管线

功能：
1. 遍历 papers/ 目录下的所有 .full.pdf 文件（传统模式）
2. 或从扁平 PDF 目录读取文件（--flat-pdf-dir + --paper-map 模式）
3. 直接读取已经转换好的 Markdown（--markdown 模式）
4. 用 markitdown 将 PDF 转为 Markdown 文本
5. (可选) 按章节分块，防止超过 LLM 上下文窗口
6. 使用 LLM API 提取细胞类型和 marker 基因
7. 保存结构化 JSON 到 markers_output/ 目录

用法：
    python run_extraction.py [--paper-dir DIR] [--output-dir DIR] [--paper-id PID]
                              [--skip-existing] [--dry-run] [--max-chars 80000]
    python run_extraction.py --pdf PATH [--paper-id PID] ...
    python run_extraction.py --markdown PATH --paper-id PID [--document-id DID] ...
    python run_extraction.py --flat-pdf-dir DIR --paper-map MAP.json [--paper-id PID] ...

依赖：
    pip install markitdown openai python-dotenv
"""
import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from collections import Counter
from typing import Optional

from dotenv import load_dotenv

from marker_schema import EVIDENCE_RANK, MarkerSchemaError, SCHEMA_VERSION, apply_evidence_guardrail, validate_payload

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# 加载 .env 文件（优先项目根目录）
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)
    logger.info(f"已加载 .env: {dotenv_path}")

PROJECT_ROOT = Path(r"D:\OneDrive\Desktop\组")
PAPERS_DIR = PROJECT_ROOT / "papers"
OUTPUT_DIR = Path(__file__).parent / "markers_output_v2"
PROMPT_FILE = Path(__file__).parent / "prompts" / "extract_markers_v4.md"

# 用于分块的最大字符数（~80k chars ≈ 20k tokens 的中英文混合文本）
DEFAULT_MAX_CHARS = 80_000


def read_prompt(prompt_path: Optional[Path] = None) -> str:
    """读取提示词模板"""
    path = prompt_path or PROMPT_FILE
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def find_pdf_files(papers_dir: Path, paper_id: Optional[str] = None) -> list[tuple[str, str, str, Path]]:
    """遍历 papers/ 目录，找到所有 .full.pdf 文件

    返回: [(paper_id, pdf_path), ...]
    """
    pdfs: list[tuple[str, str, str, Path]] = []
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
            pdfs.append((subdir.name, subdir.name, "primary", pdf_file))
            logger.info(f"  发现: {subdir.name}")

    if paper_id and not pdfs:
        # 也直接在 papers/ 下搜索
        for subdir in sorted(papers_dir.iterdir()):
            if paper_id in subdir.name:
                pdf_file = subdir / f"{subdir.name}.full.pdf"
                if pdf_file.exists():
                    pdfs.append((subdir.name, subdir.name, "primary", pdf_file))
                    break

    return pdfs


def find_pdf_files_flat(pdf_dir: Path, paper_map: dict[str, dict[str, str]],
                        paper_id: Optional[str] = None) -> list[tuple[str, str, str, Path]]:
    """遍历扁平 PDF 目录，用映射表匹配 paper_id

    paper_map: {pdf_filename: {paper_id, document_id, document_role, sha256}}
    """
    pdfs: list[tuple[str, str, str, Path]] = []
    if not pdf_dir.exists():
        logger.error(f"PDF 目录不存在: {pdf_dir}")
        return pdfs

    for pdf_file in sorted(pdf_dir.iterdir()):
        if pdf_file.suffix.lower() != '.pdf':
            continue
        entry = paper_map.get(pdf_file.name)
        if entry is None:
            continue
        pid = entry["paper_id"]
        document_id = entry["document_id"]
        document_role = entry["document_role"]
        if paper_id and paper_id not in {pid, document_id}:
            continue
        expected_sha256 = entry.get("sha256", "")
        if expected_sha256:
            digest = hashlib.sha256()
            with pdf_file.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            actual_sha256 = digest.hexdigest()
            if actual_sha256 != expected_sha256:
                raise ValueError(
                    f"PDF 哈希与审计映射不一致: {pdf_file.name} "
                    f"(expected={expected_sha256}, actual={actual_sha256})"
                )
        pdfs.append((pid, document_id, document_role, pdf_file))
        logger.info("  发现: %s [%s] -> %s", document_id, document_role, pdf_file.name)

    if not pdfs:
        logger.warning(f"  未找到匹配的 PDF（共 {len(list(pdf_dir.glob('*.pdf')))} 个 PDF 文件）")
    return pdfs


def load_paper_map(map_path: Path) -> dict[str, dict[str, str]]:
    """加载结构化文档映射；兼容旧的字符串 paper_id 值。"""
    if not map_path.exists():
        logger.error(f"映射表不存在: {map_path}")
        return {}
    with open(map_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("paper_map 必须是 {pdf_filename: paper_id} 对象")
    mapping: dict[str, dict[str, str]] = {}
    valid_roles = {"primary", "supplement", "extended_data", "correction"}
    for filename, value in data.items():
        if not isinstance(filename, str) or not filename.lower().endswith(".pdf"):
            raise ValueError(f"无效 PDF 文件名: {filename!r}")
        if isinstance(value, str):
            paper_id = value.strip()
            entry = {"paper_id": paper_id, "document_id": paper_id, "document_role": "primary", "sha256": ""}
        elif isinstance(value, dict):
            entry = {
                "paper_id": str(value.get("paper_id") or "").strip(),
                "document_id": str(value.get("document_id") or "").strip(),
                "document_role": str(value.get("document_role") or "").strip(),
                "sha256": str(value.get("sha256") or "").strip(),
            }
        else:
            raise ValueError(f"无效映射值: {filename} -> {value!r}")
        if not entry["paper_id"] or not entry["document_id"]:
            raise ValueError(f"映射缺少 paper_id/document_id: {filename}")
        if entry["document_role"] not in valid_roles:
            raise ValueError(f"无效 document_role: {filename} -> {entry['document_role']!r}")
        mapping[filename] = entry
    document_id_counts = Counter(entry["document_id"] for entry in mapping.values())
    duplicate_ids = sorted(document_id for document_id, count in document_id_counts.items() if count > 1)
    if duplicate_ids:
        raise ValueError(f"paper_map 中存在重复 document_id: {duplicate_ids}")
    return mapping


def convert_pdf_to_text(pdf_path: Path) -> Optional[str]:
    """将 PDF 转换为纯文本

    无论文件大小均优先使用 MarkItDown，失败后回退到 PyPDF2 → pdfminer。
    """
    text = None
    file_size_mb = pdf_path.stat().st_size / 1024 / 1024

    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(str(pdf_path))
        text_content = result.text_content
        if text_content and len(text_content) > 100:
            logger.info(f"  使用 MarkItDown 转换成功 ({file_size_mb:.1f} MB)")
            return text_content
    except ImportError:
        logger.info("  MarkItDown 未安装，尝试回退方案")
    except Exception as e:
        logger.warning(f"  MarkItDown 转换失败: {e}")

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


def read_markdown_text(markdown_path: Path) -> Optional[str]:
    """读取已经完成转换的 Markdown，避免重复处理 PDF。"""
    try:
        text = markdown_path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.error("读取 Markdown 失败: %s (%s)", markdown_path, exc)
        return None
    return text if len(text.strip()) > 100 else None


# 章节标题关键词（小写匹配）
_SECTION_KEYWORDS = [
    "abstract", "introduction", "results", "discussion", "methods",
    "materials and methods", "materials & methods", "experimental procedures",
    "figure legends", "figure legends", "supplementary", "references",
    "acknowledgments", "acknowledgements", "author contributions",
    "conflict of interest", "competing interests", "data availability",
    "online content", "ethics statement", "consent", "funding",
    "supplementary information", "additional information",
    "star methods", "key resources table", "resource availability",
    "methodology", "materials", "experimental design",
]

# 应过滤掉的章节（不含 marker 信息）
_SKIP_SECTIONS = {
    "references", "acknowledgments", "acknowledgements", "author contributions",
    "conflict of interest", "competing interests", "data availability",
    "funding", "consent", "ethics statement", "resource availability",
    "additional information", "supplementary information",
}


def _is_section_header(line: str) -> Optional[str]:
    """判断一行是否是章节标题，返回归一化后的章节名或 None

    匹配策略（按优先级）：
    1. markdown 标题: # / ## / ### 开头
    2. 独立行且仅由章节关键词构成（允许尾部冒号/数字/点号）
    3. 全大写的短行（≤6 词）且匹配关键词
    """
    stripped = line.strip()
    if not stripped or len(stripped) > 80:
        return None

    lower = stripped.lower().rstrip(":.").strip()

    # 策略 1: markdown 标题
    md_match = re.match(r"^#{1,4}\s+(.+)", stripped)
    if md_match:
        header_text = md_match.group(1).strip().lower().rstrip(":.").strip()
        for kw in _SECTION_KEYWORDS:
            if header_text == kw or header_text.startswith(kw):
                return kw

    # 策略 2: 独立行精确匹配关键词（允许 "Methods 2" 等尾部编号）
    for kw in _SECTION_KEYWORDS:
        if lower == kw or re.match(rf"^{re.escape(kw)}\s*[\d.]*(\s|$)", lower):
            return kw

    # 策略 3: 全大写短行匹配（Nature/Cell 风格：RESULTS / METHODS）
    if stripped.isupper() and len(stripped.split()) <= 6:
        for kw in _SECTION_KEYWORDS:
            if lower.startswith(kw):
                return kw

    return None


def split_into_chunks(text: str, max_chars: int = DEFAULT_MAX_CHARS) -> list[tuple[str, str]]:
    """按章节将文本分块

    返回: [(section_name, section_content), ...]

    改进点：
    - 支持 markdown 标题、独立行标题、全大写标题三种识别策略
    - 自动过滤 References / Acknowledgments / Data availability 等无用章节
    - 大块按段落二次切分，不超过 max_chars
    """
    chunks: list[tuple[str, str]] = []
    current_section = "preamble"
    current_lines: list[str] = []

    for line in text.split("\n"):
        section_name = _is_section_header(line)
        if section_name:
            # 保存当前块
            if current_lines:
                content = "\n".join(current_lines).strip()
                if content:
                    chunks.append((current_section, content))
            current_section = section_name
            current_lines = []
        else:
            current_lines.append(line)

    # 保存最后一块
    if current_lines:
        content = "\n".join(current_lines).strip()
        if content:
            chunks.append((current_section, content))

    # 过滤无用章节
    filtered = [(name, content) for name, content in chunks
                if name.lower() not in _SKIP_SECTIONS]

    # 大块按段落二次切分
    result: list[tuple[str, str]] = []
    for name, content in filtered:
        if len(content) <= max_chars:
            result.append((name, content))
        else:
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
    merged: dict = {"schema_version": SCHEMA_VERSION, "paper_id": "", "cell_types": []}

    cell_type_map: dict[str, dict] = {}
    for result_str in results:
        if not result_str:
            continue
        try:
            data = json.loads(result_str)
        except json.JSONDecodeError:
            logger.warning(f"  跳过无效 JSON: {result_str[:200]}")
            continue

        try:
            validate_payload(data)
        except MarkerSchemaError as exc:
            logger.warning("  跳过 schema 无效的提取块: %s", exc)
            continue

        if not merged["paper_id"] and data.get("paper_id"):
            merged["paper_id"] = data["paper_id"]

        for ct in data.get("cell_types", []):
            ct_key = (
                f"{ct.get('cell_type', '')}|{ct.get('subtype', '')}|"
                f"{ct.get('species', '')}"
            )
            if ct_key not in cell_type_map:
                cell_type_map[ct_key] = {
                    "cell_type": ct["cell_type"],
                    "subtype": ct.get("subtype"),
                    "species": ct.get("species"),
                    "is_pns_cell": ct.get("is_pns_cell"),
                    "markers": [],
                }
            else:
                # 补洞：若已有记录缺 species/is_pns_cell，用新值补上
                for k in ("species", "is_pns_cell"):
                    if not cell_type_map[ct_key].get(k) and ct.get(k):
                        cell_type_map[ct_key][k] = ct.get(k)

            # 去重 markers
            existing_genes: dict[str, int] = {}
            for m in cell_type_map[ct_key]["markers"]:
                marker_key = f"{m['gene']}|{m.get('marker_polarity', 'unknown')}"
                existing_genes[marker_key] = EVIDENCE_RANK.get(m["evidence_type"], 0)

            for m in ct.get("markers", []):
                m = apply_evidence_guardrail(m)
                gene = m["gene"]
                marker_key = f"{gene}|{m.get('marker_polarity', 'unknown')}"
                new_rank = EVIDENCE_RANK.get(m["evidence_type"], 0)
                if marker_key in existing_genes:
                    if new_rank > existing_genes[marker_key]:
                        # 替换为更高证据等级
                        cell_type_map[ct_key]["markers"] = [
                            x for x in cell_type_map[ct_key]["markers"]
                            if f"{x['gene']}|{x.get('marker_polarity', 'unknown')}" != marker_key
                        ]
                        cell_type_map[ct_key]["markers"].append(m)
                        existing_genes[marker_key] = new_rank
                else:
                    cell_type_map[ct_key]["markers"].append(m)
                    existing_genes[marker_key] = new_rank

    merged["cell_types"] = list(cell_type_map.values())
    return merged


def process_paper(
    paper_id: str,
    document_id: str,
    document_role: str,
    source_path: Path,
    args: argparse.Namespace,
    source_kind: str = "pdf",
) -> bool:
    """处理单篇论文，返回是否成功"""
    logger.info(f"\n{'='*60}")
    logger.info("处理文档: %s (%s, paper=%s)", document_id, document_role, paper_id)
    logger.info("  %s: %s", source_kind.upper(), source_path)

    output_file = Path(args.output_dir) / f"{document_id}_raw.json"
    if args.skip_existing and output_file.exists():
        logger.info(f"  跳过（已存在）: {output_file}")
        return True

    # 1. 读取 Markdown 或转换 PDF → 文本
    if source_kind == "markdown":
        logger.info("  [1/4] 读取已有 Markdown...")
        text = read_markdown_text(source_path)
    else:
        logger.info("  [1/4] 转换 PDF → 文本...")
        text = convert_pdf_to_text(source_path)
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
    prompt_path = Path(args.prompt_file) if args.prompt_file else None
    prompt = read_prompt(prompt_path)
    results: list[Optional[str]] = []

    for idx, (section_name, section_content) in enumerate(chunks):
        logger.info(f"  处理块 {idx+1}/{len(chunks)}: {section_name}")
        user_content = (
            f"以下文本来自论文 [{paper_id}] 的 [{document_role}] 文档，文档 ID 为 [{document_id}]，"
            f"当前为 {section_name} 章节。\n"
            f"请在输出顶层原样填写 paper_id、document_id 和 document_role。\n"
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

    if len(results) != len(chunks):
        logger.error(
            "  LLM 提取不完整：成功 %d/%d 块；为避免生成残缺论文结果，本次不保存",
            len(results),
            len(chunks),
        )
        return False

    # 4. 合并 & 保存
    logger.info("  [4/4] 合并并保存结果...")
    merged = merge_json_results(results)
    merged["paper_id"] = paper_id
    merged["document_id"] = document_id
    merged["document_role"] = document_role
    if source_kind == "markdown":
        merged["source_markdown"] = source_path.name
    else:
        merged["source_pdf"] = source_path.name

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    n_cell_types = len(merged.get("cell_types", []))
    n_markers = sum(len(ct.get("markers", [])) for ct in merged.get("cell_types", []))
    logger.info(f"  ✅ 完成: {n_cell_types} 个细胞类型, {n_markers} 个 marker")
    logger.info(f"  保存到: {output_file}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF/Markdown → LLM → JSON Marker 提取管线")
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
    parser.add_argument("--prompt-file", default=None,
                        help="提示词模板文件路径 (默认: prompts/extract_markers_v4.md)")
    parser.add_argument("--document-id", help="Markdown 输入时指定文档 ID；默认使用 paper_id")
    parser.add_argument("--document-role", default="primary",
                        choices=["primary", "supplement", "extended_data", "correction"],
                        help="文档角色（默认: primary）")
    # 单文件模式
    parser.add_argument("--pdf", help="直接指定单个 PDF 文件路径")
    parser.add_argument("--markdown", help="直接指定已经转换好的 Markdown 文件路径")
    # 扁平目录模式
    parser.add_argument("--flat-pdf-dir", help="扁平 PDF 目录（所有 PDF 在同一层）")
    parser.add_argument("--paper-map", help="paper_id 映射 JSON 文件路径")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 模式 1: 已有 Markdown 文件
    if args.markdown:
        markdown_path = Path(args.markdown)
        if not markdown_path.exists():
            logger.error(f"Markdown 文件不存在: {markdown_path}")
            sys.exit(1)
        paper_id = args.paper_id or markdown_path.stem
        document_id = args.document_id or paper_id
        logger.info("Markdown 模式: %s -> %s", paper_id, markdown_path)
        documents = [(paper_id, document_id, args.document_role, markdown_path, "markdown")]

    # 模式 2: 单 PDF 文件
    elif args.pdf:
        pdf_path = Path(args.pdf)
        if not pdf_path.exists():
            logger.error(f"PDF 文件不存在: {pdf_path}")
            sys.exit(1)
        paper_id = args.paper_id or pdf_path.stem
        logger.info(f"单文件模式: {paper_id} -> {pdf_path}")
        documents = [(paper_id, paper_id, "primary", pdf_path, "pdf")]

    # 模式 2: 扁平目录模式
    elif args.flat_pdf_dir:
        if not args.paper_map:
            logger.error("扁平目录模式需要 --paper-map 参数")
            sys.exit(1)
        try:
            paper_map = load_paper_map(Path(args.paper_map))
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            logger.error("映射表校验失败: %s", exc)
            sys.exit(1)
        if not paper_map:
            sys.exit(1)
        logger.info(f"扁平目录模式: {args.flat_pdf_dir} (映射表: {len(paper_map)} 项)")
        try:
            pdfs = find_pdf_files_flat(Path(args.flat_pdf_dir), paper_map,
                                       paper_id=args.paper_id)
        except (OSError, ValueError) as exc:
            logger.error("PDF 与映射校验失败: %s", exc)
            sys.exit(1)
        documents = [(*item, "pdf") for item in pdfs]

    # 模式 3: 传统 papers/ 目录模式
    else:
        papers_dir = Path(args.paper_dir)
        logger.info(f"扫描论文目录: {papers_dir}")
        pdfs = find_pdf_files(papers_dir, paper_id=args.paper_id)
        documents = [(*item, "pdf") for item in pdfs]

    if not documents:
        logger.error("未找到任何输入文档")
        sys.exit(1)
    logger.info(f"找到 {len(documents)} 篇论文")

    # 处理每篇论文
    success = 0
    for paper_id, document_id, document_role, source_path, source_kind in documents:
        if process_paper(
            paper_id,
            document_id,
            document_role,
            source_path,
            args,
            source_kind=source_kind,
        ):
            success += 1

    logger.info(f"\n{'='*60}")
    logger.info(f"完成: {success}/{len(documents)} 篇论文成功处理")
    if success != len(documents):
        sys.exit(1)


if __name__ == "__main__":
    main()
