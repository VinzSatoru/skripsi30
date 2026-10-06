import os
import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

jurnal_root = 'jurnal'
pdf_list = []

for root, dirs, files in os.walk(jurnal_root):
    for f in files:
        if f.lower().endswith('.pdf'):
            full_path = os.path.join(root, f)
            pdf_list.append((full_path, f, root))

print(f"Total PDF files found: {len(pdf_list)}")

results = []
for full_path, fname, folder in pdf_list:
    doc = fitz.open(full_path)
    text = ""
    for i in range(min(2, len(doc))):
        text += doc[i].get_text() + "\n"
    
    # Extract DOIs
    dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
    doi = dois[0] if dois else ""
    
    # Extract Year: search for 201x or 202x
    # Prioritize years mentioned in header/copyright
    year_candidates = re.findall(r'\b(201\d|202\d)\b', text[:2000])
    # Filter reasonable years
    year = ""
    for y in ['2026', '2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017']:
        if y in year_candidates:
            year = y
            break
    if not year and year_candidates:
        year = year_candidates[0]

    # First clean text lines for title / author
    lines = [l.strip() for l in doc[0].get_text().split('\n') if len(l.strip()) > 5]
    header_snippet = " // ".join(lines[:4])

    results.append({
        "file": fname,
        "folder": os.path.relpath(folder, '.'),
        "year": int(year) if year.isdigit() else 2020,
        "year_str": year,
        "doi": doi,
        "snippet": header_snippet
    })

# Print detailed summary
print("\n" + "="*80)
print(f"INVENTARIS LENGKAP {len(results)} ARTIKEL JURNAL DI REPOSITORI 'jurnal/'")
print("="*80)

results_sorted = sorted(results, key=lambda x: (x['year'], x['file']), reverse=True)
count_recent = 0
for idx, r in enumerate(results_sorted):
    is_recent = r['year'] >= 2021
    if is_recent:
        count_recent += 1
    tag = "[5 TAHUN TERAKHIR]" if is_recent else "[KLASIK/SEMINAL]"
    print(f"{idx+1:02d}. ({r['year']}) {tag} {r['file']}")
    print(f"    Folder: {r['folder']}")
    if r['doi']:
        print(f"    DOI: https://doi.org/{r['doi']}")
    print(f"    Info: {r['snippet'][:110]}...")

pct = (count_recent / len(results)) * 100
print("\n" + "="*80)
print(f"TOTAL SELURUH KOLEKSI PDF JURNAL: {len(results)} JURNAL")
print(f"JURNAL 5 TAHUN TERAKHIR (2021-2026): {count_recent} DARI {len(results)} ({pct:.2f}%)")
print(f"JURNAL SEBELUM 2021 (>5 TAHUN): {len(results) - count_recent} DARI {len(results)} ({100 - pct:.2f}%)")
print("="*80)
