import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('scratch/temp_read.docx')
for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if 'tabel' in txt.lower() and len(txt) < 100:
        print(f"P[{i:3d}]: {txt}")
