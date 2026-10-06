import sys
import os
import fitz
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\jurnal\Jurnal tambahan BAB 3'
for fname in os.listdir(pdf_dir):
    if fname.endswith('.pdf'):
        fpath = os.path.join(pdf_dir, fname)
        doc = fitz.open(fpath)
        print("="*60)
        print("FILE:", fname)
        print(f"Total pages: {len(doc)}")
        text = ""
        for i in range(min(2, len(doc))):
            text += doc[i].get_text() + "\n"
        
        dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
        print("DOIs found on p1-2:", list(set(dois)))
        
        lines = [l.strip() for l in doc[0].get_text().split('\n') if l.strip()]
        print("Header lines:")
        for l in lines[:10]:
            print("  ", l)
