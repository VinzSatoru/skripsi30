import fitz
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\jurnal\jurnal tambahan BAB2'
for fname in os.listdir(pdf_dir):
    if fname.endswith('.pdf'):
        fpath = os.path.join(pdf_dir, fname)
        doc = fitz.open(fpath)
        text = ""
        for i in range(min(2, len(doc))):
            text += doc[i].get_text() + "\n"
        
        # Find years like 201x, 202x
        years = re.findall(r'\b(201\d|202\d)\b', text)
        dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
        print("="*50)
        print("FILE:", fname)
        print("Years found:", list(set(years))[:5])
        print("DOIs found:", list(set(dois))[:2])
