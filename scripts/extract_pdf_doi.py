"""提取 PDF 中的 DOI 信息"""
import re
import os

def extract_doi_from_pdf(filepath):
    """从 PDF 中提取 DOI"""
    try:
        import PyPDF2
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            # 检查 metadata
            meta = reader.metadata
            if meta:
                for key in meta:
                    print(f"  Meta {key}: {meta[key]}")
            
            # 搜索前 5 页的文本
            for page_num in range(min(5, len(reader.pages))):
                page = reader.pages[page_num]
                text = page.extract_text()
                # DOI pattern
                doi_match = re.search(r'10\.\d{4,}/[^\s]+', text)
                if doi_match:
                    doi = doi_match.group().rstrip('.')
                    print(f"  Found DOI (page {page_num+1}): {doi}")
                    return doi
    except ImportError:
        pass
    
    try:
        import pdfminer
    except ImportError:
        pass
    
    # Try with pdfminer.six
    try:
        from pdfminer.high_level import extract_text
        text = extract_text(filepath, page_numbers=[0,1,2,3,4])
        doi_match = re.search(r'10\.\d{4,}/[^\s]+', text)
        if doi_match:
            doi = doi_match.group().rstrip('.')
            print(f"  Found DOI (pdfminer): {doi}")
            return doi
    except Exception as e:
        print(f"  pdfminer failed: {e}")
    
    return None

def extract_text_simple(filepath):
    """简单的文本提取"""
    try:
        import PyPDF2
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text_parts = []
            for page_num in range(min(3, len(reader.pages))):
                text_parts.append(reader.pages[page_num].extract_text())
            return '\n'.join(text_parts)
    except ImportError:
        return "PyPDF2 not installed"

# File 1
file1 = 'C:/Users/35221/Downloads/1346.pdf'
print(f"=== {file1} ===")
print(f"Size: {os.path.getsize(file1)} bytes")
doi1 = extract_doi_from_pdf(file1)
if not doi1:
    print("  No DOI found, extracting text preview...")
    text = extract_text_simple(file1)
    print(f"  Text preview (first 1000 chars):\n{text[:1000]}")

print()

# File 2
file2 = 'C:/Users/35221/Downloads/PIIS0092867419307329.pdf'
print(f"=== {file2} ===")
print(f"Size: {os.path.getsize(file2)} bytes")
doi2 = extract_doi_from_pdf(file2)
if not doi2:
    print("  No DOI found, extracting text preview...")
    text = extract_text_simple(file2)
    print(f"  Text preview (first 1000 chars):\n{text[:1000]}")