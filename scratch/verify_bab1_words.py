with open('BAB_1_Draft_Final.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract the 6 paragraphs under 1.1 Latar Belakang Masalah
import re
lb_match = re.search(r'## 1\.1 Latar Belakang Masalah\s*\n\n(.*?)\n\n## 1\.2 Rumusan Masalah', text, re.DOTALL)
if lb_match:
    paras = lb_match.group(1).strip().split('\n\n')
    print(f"Total paragraphs in 1.1: {len(paras)}")
    for i, p in enumerate(paras):
        wc = len(p.split())
        status = "PASSED (120-130)" if 120 <= wc <= 130 else f"FAILED: {wc}"
        print(f"Paragraf {i+1}: {wc} kata -> {status}")
