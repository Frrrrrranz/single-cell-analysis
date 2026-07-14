import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"d:\OneDrive\Desktop\组\papers\FRONT-CELL-NEUROSCI.15.624826.2021\FRONT-CELL-NEUROSCI.15.624826.2021.full.pdf"
doc = fitz.open(pdf_path)

print("--- PAGE 1 ---")
print(doc[0].get_text()[:3000])

print("--- PAGE 2 ---")
print(doc[1].get_text()[:2000])
