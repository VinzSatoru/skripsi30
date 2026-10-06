import json
import re

with open("scratch/all_pdf_full_dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total PDFs: {len(data)}")

for i, d in enumerate(data, 1):
    fname = d["filename"]
    doi = d["doi"]
    sample = d["text_sample"]
    lines = [l.strip() for l in sample.split("\n") if l.strip()]
    
    # Try to extract title, author, year
    first_few = " // ".join(lines[:6])
    print(f"\n[{i:2d}] File: {fname}")
    print(f"     DOI: {doi if doi else 'NO DOI FOUND'}")
    print(f"     Header: {first_few[:200]}")
