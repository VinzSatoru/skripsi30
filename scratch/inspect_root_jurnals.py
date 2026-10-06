import fitz
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

jurnal_dir = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\jurnal'
for fname in os.listdir(jurnal_dir):
    if fname.endswith('.pdf'):
        fpath = os.path.join(jurnal_dir, fname)
        doc = fitz.open(fpath)
        text = ""
        for i in range(min(2, len(doc))):
            text += doc[i].get_text() + "\n"
        dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
        print("="*50)
        print("FILE:", fname)
        print("DOIs:", list(set(dois))[:2])
