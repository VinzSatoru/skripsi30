import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('temp_work_proposal.docx')
for i in range(62, 138):
    p = doc.paragraphs[i]
    txt = p.text.strip()
    if txt.startswith('Gambar ') or txt.startswith('Tabel ') or txt.startswith('Table '):
        print(f"P[{i:3d}]: {txt}")
