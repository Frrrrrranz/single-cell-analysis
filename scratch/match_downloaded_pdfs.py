# -*- coding: utf-8 -*-
"""Match downloaded PDFs to literature table - using os.listdir to handle Chinese path"""
import os, sys, openpyxl

# Find the literature table file by listing directory
db_dir = r"D:\OneDrive\Desktop\组\db"
files = os.listdir(db_dir)
lit_file = None
for f in files:
    if "文献" in f or "一览表" in f:
        lit_file = os.path.join(db_dir, f)
        break

if not lit_file:
    print("ERROR: literature table not found!")
    sys.exit(1)

print(f"Using file: {lit_file}")

wb = openpyxl.load_workbook(lit_file, data_only=True)
ws = wb.active

# Check fills separately
wb_fill = openpyxl.load_workbook(lit_file, data_only=False)
ws_fill = wb_fill.active

downloaded_pdfs = [
    "s42003-024-07315-x.pdf",
    "s42255-023-00876-x.pdf",
    "s41467-021-21783-3.pdf",
    "2025.09.26.678707v2.full.pdf",
    "s41467-024-52052-8.pdf",
    "s41591-024-03215-z.pdf",
    "2025.01.17.633590.full.pdf",
    "s41467-025-60371-7.pdf",
    "mmc9.pdf",
    "s41586-021-03569-1.pdf",
    "s41588-024-01702-0.pdf",
    "s41467-023-40173-5.pdf",
    "s41591-023-02327-2.pdf",
    "s44318-024-00328-6.pdf",
    "elife-62522-v2.pdf",
    "PIIS0092867422014155.pdf",
    "PIIS1569199325000499.pdf",
    "LAM.pdf",
]

def extract_doi_key(doi_text):
    t = doi_text.strip()
    for prefix in ["DOI:", "PMID:"]:
        t = t.replace(prefix, "")
    for prefix in ["10.1038/", "10.1016/", "10.1126/", "10.7554/", "10.1002/",
                    "10.1158/", "10.1084/", "10.1101/", "10.3389/", "10.64898/",
                    "10.1161/", "10.1164/"]:
        t = t.replace(prefix, "")
    return t.strip().lower()

print("\n=== Matching downloaded PDFs to unhighlighted (B类) papers ===\n")

matched_pdfs = {}
for row_idx in range(2, ws.max_row + 1):
    fill = ws_fill.cell(row=row_idx, column=1).fill
    fg = fill.fgColor
    color = fg.rgb if fg else "00000000"
    highlighted = color not in (None, "00000000", "0", "FFFFFF", "ffffffff")
    if highlighted:
        continue
    
    doi = str(ws.cell(row=row_idx, column=6).value or "")
    title = str(ws.cell(row=row_idx, column=3).value or "")
    doi_key = extract_doi_key(doi)
    
    for pdf in downloaded_pdfs:
        pdf_key = pdf.lower().replace(".full.pdf", "").replace("v2", "").replace("v3", "").replace("-v", "").replace(".pdf", "")
        if doi_key and (doi_key in pdf_key or pdf_key in doi_key):
            matched_pdfs[pdf] = {
                "row": row_idx,
                "title": title[:60],
                "doi": doi[:50],
            }
            break

print(f"Matched: {len(matched_pdfs)} / {len(downloaded_pdfs)} downloaded PDFs\n")
for pdf, info in sorted(matched_pdfs.items()):
    print(f"  [MATCH] {pdf}")
    print(f"           Row {info['row']}: {info['title']}")
    print(f"           DOI: {info['doi']}")

unmatched_pdfs = [p for p in downloaded_pdfs if p not in matched_pdfs]
if unmatched_pdfs:
    print(f"\nUnmatched PDFs ({len(unmatched_pdfs)}):")
    for p in unmatched_pdfs:
        print(f"  {p}")

wb.close()
wb_fill.close()
