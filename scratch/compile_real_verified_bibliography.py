import json
import os
import fitz
import re

with open("scratch/local_pdf_metadata.json", "r", encoding="utf-8") as f:
    records = json.load(f)

print(f"Total local records: {len(records)}")

# Let's inspect each unique real paper
unique_papers = {}
for r in records:
    doi = r["doi"]
    fname = r["filename"]
    if doi and doi in unique_papers:
        continue
    unique_papers[fname] = r

print(f"Unique files: {len(unique_papers)}")
for fname, r in unique_papers.items():
    print(f"- {fname} | DOI: {r['doi']}")
