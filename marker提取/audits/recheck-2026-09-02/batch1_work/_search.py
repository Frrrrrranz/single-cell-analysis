import sys, re

PATH = r'D:\OneDrive\Desktop\组\marker提取\review_md\DOI_10.1038_s41586-020-2922-4.md'
with open(PATH, encoding='utf-8') as f:
    TEXT = f.read()
LINES = TEXT.split('\n')

def search(pattern, ctx=3, flags=re.I):
    """Print line numbers and lines matching pattern with context, and a flattened window."""
    rx = re.compile(pattern, flags)
    hits = []
    for i, l in enumerate(LINES):
        if rx.search(l):
            hits.append(i)
    seen = set()
    for i in hits:
        lo, hi = max(0, i-ctx), min(len(LINES), i+ctx+1)
        key = (lo, hi)
        if key in seen:
            continue
        seen.add(key)
        print('=== lines %d-%d ===' % (lo, hi-1))
        for j in range(lo, hi):
            print('%5d| %s' % (j, LINES[j]))
        print()

if __name__ == '__main__':
    pattern = sys.argv[1]
    ctx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    search(pattern, ctx)
