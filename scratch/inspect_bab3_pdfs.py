import fitz
import os
import re

pdf_dir = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\jurnal\Jurnal tambahan BAB 3'
for fname in os.listdir(pdf_dir):
    if fname.endswith('.pdf'):
        fpath = os.path.join(pdf_dir, fname)
        doc = fitz.open(fpath)
        print("="*60)
        print("FILE:", fname)
        print(f"Total pages: {len(doc)}")
        text = ""
        for i in range(min(3, len(doc))):
            text += doc[i].get_text() + "\n"
        
        dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
        print("Found DOIs:", list(set(dois)))
        
        # Look for Title and Journal info in first 10 lines
        lines = [l.strip() for l in doc[0].get_text().split('\n') if l.strip()]
        print("First 8 lines:")
        for l in lines[:8]:
            try:
                print("  ", l)
            except:
                print("  ", repr(l))
