import os
import fitz
import re
import json

pdf_files = []
for root, dirs, files in os.walk("jurnal"):
    for f in files:
        if f.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(root, f))

results = []
for p in sorted(pdf_files):
    fname = os.path.basename(p)
    doc = fitz.open(p)
    num_pages = len(doc)
    text_p0 = doc[0].get_text()
    text_p1 = doc[1].get_text() if num_pages > 1 else ""
    full_text = text_p0 + "\n" + text_p1
    
    # DOI search
    dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', full_text)
    clean_dois = [re.sub(r'[\s.,;)]+$', '', d) for d in dois]
    doi = clean_dois[0] if clean_dois else ""
    
    # First 1500 chars clean
    clean_p0 = text_p0[:1500].encode('ascii', 'replace').decode('ascii')
    
    results.append({
        "path": p.replace("\\", "/"),
        "filename": fname,
        "doi": doi,
        "text_sample": clean_p0
    })

with open("scratch/all_pdf_full_dump.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Dumped {len(results)} PDFs to scratch/all_pdf_full_dump.json")
