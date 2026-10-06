import os
import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

all_pdfs = []
for root, dirs, files in os.walk('jurnal'):
    for f in files:
        if f.endswith('.pdf'):
            all_pdfs.append(os.path.join(root, f))

print(f"Total PDFs found: {len(all_pdfs)}")
for p in all_pdfs:
    doc = fitz.open(p)
    text = ""
    for i in range(min(2, len(doc))):
        text += doc[i].get_text() + "\n"
    
    # Extract year: prioritize publication year patterns like 202x
    years = re.findall(r'\b(202[1-6])\b', text)
    title = [l.strip() for l in doc[0].get_text().split('\n') if len(l.strip()) > 15]
    t_str = title[0] if title else os.path.basename(p)
    print(f"[{years[0] if years else 'OLDER'}] {os.path.basename(p)[:40]} -> {t_str[:70]}")
