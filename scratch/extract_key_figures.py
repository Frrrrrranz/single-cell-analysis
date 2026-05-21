import re
from pathlib import Path
import fitz

ROOT = Path(r"d:/OneDrive/Desktop/组")
TASKS = [
    {
        "pdf": ROOT / "陈1.pdf",
        "out_dir": ROOT / "COMMUN-BIOL.5.1105.2022.full" / "paper_figures",
    },
    {
        "pdf": ROOT / "陈2.pdf",
        "out_dir": ROOT / "PNAS.117.9466.2020.full" / "paper_figures",
    },
]

FIG_PAT = re.compile(r"\b(Figure|Fig\.)\s*([0-9]+[A-Za-z]?)", re.IGNORECASE)

for task in TASKS:
    pdf_path = task["pdf"]
    out_dir = task["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)

    # Clear previous extracted files in this folder only
    for p in out_dir.glob("page_*.png"):
        p.unlink()
    idx_file = out_dir / "figure_index.txt"
    if idx_file.exists():
        idx_file.unlink()

    doc = fitz.open(pdf_path)

    selected = []
    for i in range(len(doc)):
        text = doc.load_page(i).get_text("text")
        if FIG_PAT.search(text):
            selected.append(i)

    # Fallback: if no text hit (scanned PDF), sample likely figure-heavy pages excluding references tail
    if not selected:
        upper = max(1, len(doc) - 2)
        selected = list(range(0, min(upper, 12)))

    # De-duplicate while keeping order
    seen = set()
    pages = []
    for p in selected:
        if p not in seen:
            seen.add(p)
            pages.append(p)

    lines = [f"PDF: {pdf_path.name}", f"Total pages: {len(doc)}", ""]

    for n, page_idx in enumerate(pages, start=1):
        page = doc.load_page(page_idx)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), alpha=False)
        out_name = f"page_{n:02d}.png"
        out_path = out_dir / out_name
        pix.save(out_path)

        text = page.get_text("text")
        figs = FIG_PAT.findall(text)
        fig_label = ", ".join(sorted({f"{m[0]} {m[1]}" for m in figs})) if figs else "(no explicit figure label found)"
        lines.append(f"{out_name} <- PDF page {page_idx+1} | labels: {fig_label}")

    idx_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"{pdf_path.name}: extracted {len(pages)} pages -> {out_dir}")

