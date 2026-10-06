import os
import fitz
import re
import json

pdf_files = []
for root, dirs, files in os.walk("jurnal"):
    for f in files:
        if f.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(root, f))

print(f"Total PDFs found in workspace: {len(pdf_files)}")

pdf_records = []
for p in sorted(pdf_files):
    fname = os.path.basename(p)
    doc = fitz.open(p)
    num_pages = len(doc)
    text_p0 = doc[0].get_text()
    text_p1 = doc[1].get_text() if num_pages > 1 else ""
    full_first_text = text_p0 + "\n" + text_p1
    
    # Extract DOI
    dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', full_first_text)
    # Clean trailing punctuation from DOI
    clean_dois = [re.sub(r'[\s.,;)]+$', '', d) for d in dois]
    doi = clean_dois[0] if clean_dois else ""
    
    # Extract header / first lines for title and authors
    lines = [line.strip() for line in text_p0.split('\n') if line.strip()]
    header_sample = " // ".join(lines[:8])
    
    pdf_records.append({
        "path": p.replace("\\", "/"),
        "filename": fname,
        "pages": num_pages,
        "doi": doi,
        "header_sample": header_sample[:250]
    })

print(f"\nExtracted {len(pdf_records)} records.")
import json

with open("scratch/local_pdf_metadata.json", "w", encoding="utf-8") as f:
    json.dump(pdf_records, f, indent=2, ensure_ascii=False)

for idx, r in enumerate(pdf_records, 1):
    safe_head = r['header_sample'].encode('ascii', 'replace').decode('ascii')
    doi_str = f"https://doi.org/{r['doi']}" if r['doi'] else "NONE DETECTED"
    print(f"[{idx:2d}] {r['filename'][:40]:40s} | DOI: {doi_str:35s}")
