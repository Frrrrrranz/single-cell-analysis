"""
PDF Figure 页面提取脚本
功能：识别含有 Figure 的页面，渲染为高分辨率 PNG 并保存
策略：通过文本检测 "Fig." / "Figure" 关键词 + 页面图像面积占比，筛选含 Figure 的页面
"""

import sys
import os
import re
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

try:
    import fitz  # PyMuPDF
except ImportError:
    logger.error("请先安装 PyMuPDF: pip install PyMuPDF")
    sys.exit(1)


def hasImageContent(page: fitz.Page, minImageAreaRatio: float = 0.05) -> bool:
    """判断页面是否包含足够大的图片内容"""
    pageArea = page.rect.width * page.rect.height
    if pageArea == 0:
        return False

    images = page.get_images(full=True)
    if not images:
        return False

    totalImageArea = 0
    for img in images:
        xref = img[0]
        try:
            imgRects = page.get_image_rects(xref)
            for rect in imgRects:
                totalImageArea += rect.width * rect.height
        except Exception:
            # NOTE: 某些图片可能无法获取矩形信息，跳过
            continue

    return (totalImageArea / pageArea) > minImageAreaRatio


def hasFigureText(page: fitz.Page) -> bool:
    """判断页面文本中是否包含 Figure 相关关键词"""
    text = page.get_text()
    # 匹配 "Fig. 1" / "Figure 1" / "Fig 1" / "FIGURE 1" 等模式
    figurePattern = re.compile(
        r'\b(?:Fig(?:ure)?\.?\s*\d+|FIGURE\s*\d+)',
        re.IGNORECASE
    )
    return bool(figurePattern.search(text))


def isReferencePage(page: fitz.Page) -> bool:
    """判断是否为纯参考文献页（排除含 Figure 的参考文献页）"""
    text = page.get_text()
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return False

    # 检查是否以 "References" 开头且没有 Figure
    refPattern = re.compile(r'^(References|REFERENCES|Bibliography)', re.IGNORECASE)
    hasRefHeader = any(refPattern.match(line) for line in lines[:5])

    # 检测引用编号密度（如 [1], [2] 或 1. Author, Year 格式）
    citationPattern = re.compile(r'^\[?\d+\]?\s*[A-Z]')
    citationCount = sum(1 for line in lines if citationPattern.match(line))
    citationRatio = citationCount / len(lines) if lines else 0

    # 如果有大量引用格式行且没有 Figure 文本，判定为参考文献页
    if (hasRefHeader or citationRatio > 0.3) and not hasFigureText(page):
        return True
    return False


def extractFigurePages(pdfPath: str, outputDir: str, dpi: int = 300) -> list:
    """
    从 PDF 中提取含有 Figure 的页面

    Args:
        pdfPath: PDF 文件路径
        outputDir: 输出目录
        dpi: 渲染分辨率，默认 300 DPI

    Returns:
        提取的页面信息列表
    """
    pdfPath = Path(pdfPath)
    outputDir = Path(outputDir)
    outputDir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdfPath)
    totalPages = len(doc)
    logger.info(f"📄 PDF: {pdfPath.name} ({totalPages} 页)")

    extractedPages = []
    skippedPages = []

    # NOTE: 缩放因子 = DPI / 72（PyMuPDF 默认 72 DPI）
    zoomFactor = dpi / 72
    matrix = fitz.Matrix(zoomFactor, zoomFactor)

    for pageNum in range(totalPages):
        page = doc[pageNum]
        pdfPageNum = pageNum + 1  # 人类可读的 1-indexed 页码

        hasFig = hasFigureText(page)
        hasImg = hasImageContent(page)
        isRef = isReferencePage(page)

        # 筛选逻辑：页面含有 Figure 文本 且 包含图片内容，且不是纯参考文献页
        if hasFig and hasImg and not isRef:
            # 渲染页面为 PNG
            pixmap = page.get_pixmap(matrix=matrix)
            filename = f"page_{pdfPageNum:02d}.png"
            filepath = outputDir / filename
            pixmap.save(str(filepath))

            extractedPages.append({
                "filename": filename,
                "pdfPage": pdfPageNum,
                "hasFigureText": hasFig,
                "hasImage": hasImg
            })
            logger.info(f"  ✅ 第{pdfPageNum}页 → {filename}")
        else:
            reason = []
            if not hasFig:
                reason.append("无Fig文本")
            if not hasImg:
                reason.append("无图片")
            if isRef:
                reason.append("参考文献页")
            skippedPages.append((pdfPageNum, ", ".join(reason)))
            logger.info(f"  ⏭️  第{pdfPageNum}页 跳过（{', '.join(reason)}）")

    doc.close()

    logger.info(f"\n✅ 完成！共提取 {len(extractedPages)} 页，跳过 {len(skippedPages)} 页")
    return extractedPages


def createFigureIndex(extractedPages: list, outputDir: str, pdfName: str) -> None:
    """创建 figure_index_clean.txt 索引文件"""
    outputDir = Path(outputDir)
    indexPath = outputDir / "figure_index_clean.txt"

    with open(indexPath, "w", encoding="utf-8") as f:
        f.write(f"Paper: {pdfName}\n")
        f.write(f"Exported figure pages: {len(extractedPages)}\n\n")
        f.write("Notes:\n")
        f.write("- 请对照 PDF 原文和 Gemini 标注信息，确认每张图片对应的 Figure 编号\n")
        f.write("- \"caption\" 表示该页面包含 Figure 图注\n")
        f.write("- \"content\" 表示该页面主要展示 Figure 面板\n\n")

        for page in extractedPages:
            f.write(
                f"{page['filename']} <- PDF page {page['pdfPage']} "
                f"| caption: ? | content: ?\n"
            )

    logger.info(f"📄 图序索引已创建：{indexPath}")
    logger.info("⚠️  请对照原文和 Gemini 标注，手动更新 Figure 编号")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法：python extract_figure_pages.py <PDF路径> <输出目录> [DPI]")
        print("示例：python extract_figure_pages.py paper.pdf paper_figures 300")
        sys.exit(1)

    pdfPath = sys.argv[1]
    outputDir = sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300

    if not os.path.exists(pdfPath):
        print(f"❌ PDF 文件不存在：{pdfPath}")
        sys.exit(1)

    pages = extractFigurePages(pdfPath, outputDir, dpi)
    if pages:
        createFigureIndex(pages, outputDir, Path(pdfPath).stem)
