from pathlib import Path

files = [
    (
        Path(r"d:/OneDrive/Desktop/组/COMMUN-BIOL.5.1105.2022.full/paper_figures/figure_index.txt"),
        "Paper: Single-cell transcriptional landscape of the rat sciatic nerve after chronic constriction injury (Communications Biology, 2022)",
    ),
    (
        Path(r"d:/OneDrive/Desktop/组/PNAS.117.9466.2020.full/paper_figures/figure_index.txt"),
        "Paper: Single-cell transcriptomics identifies peripheral nerve resident cell types and immune interactions (PNAS, 2020)",
    ),
]

for path, title in files:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        lines = [title]
    else:
        lines[0] = title
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"updated: {path}")
