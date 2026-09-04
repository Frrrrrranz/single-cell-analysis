import sys, re

PATH = r'D:\OneDrive\Desktop\组\marker提取\review_md\DOI_10.1038_s41588-022-01243-4.md'
with open(PATH, encoding='utf-8') as f:
    TEXT = f.read()
LINES = TEXT.split('\n')

def search(pattern, ctx=3, flags=re.I):
    rx = re.compile(pattern, flags)
    hits = []
    for i, l in enumerate(LINES):
        if rx.search(l):
            hits.append(i)
    seen = set()
    out = []
    for i in hits:
        lo, hi = max(0, i-ctx), min(len(LINES), i+ctx+1)
        key = (lo, hi)
        if key in seen:
            continue
        seen.add(key)
        out.append('=== lines %d-%d ===' % (lo, hi-1))
        for j in range(lo, hi):
            out.append('%5d| %s' % (j, LINES[j]))
        out.append('')
    return '\n'.join(out)

if __name__ == '__main__':
    ctx = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 3
    pats = sys.argv[1:-1] if sys.argv[-1].isdigit() else sys.argv[1:]
    for p in pats:
        print('######## PATTERN: %s (ctx=%d) ########' % (p, ctx))
        print(search(p, ctx))
