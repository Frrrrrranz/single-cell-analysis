import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"d:\OneDrive\Desktop\组\papers\FRONT-CELL-NEUROSCI.15.624826.2021\FRONT-CELL-NEUROSCI.15.624826.2021.full.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    
    # 查找像 "FIGURE 1 |" 或 "FIGURE 1  |" 这样格式的图注开头
    matches = re.findall(r'(FIGURE\s+\d+\s*\|)', text, re.IGNORECASE)
    if matches:
        print(f"--- Page {page_num + 1} contains captions: {matches} ---")
        # 打印那一段的开头
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if any(m in line.upper() for m in ["FIGURE 1 |", "FIGURE 2 |", "FIGURE 3 |", "FIGURE 4 |", "FIGURE 5 |", "FIGURE 6 |", "FIGURE 7 |", "FIGURE 8 |", "FIGURE 9 |", "FIGURE 10 |", "FIGURE 11 |"]):
                print(f"Match on page {page_num + 1}:")
                # 打印当前行及后面5行
                for j in range(max(0, i), min(len(lines), i + 6)):
                    print(f"  {lines[j].strip()}")
