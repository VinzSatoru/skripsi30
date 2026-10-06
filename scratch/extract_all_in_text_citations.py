import docx
import re
import shutil

shutil.copy2("PROPOSAL BAB 1-3.docx", "temp_inspect_proposal.docx")
with open("temp_inspect_proposal.docx", "rb") as f:
    doc = docx.Document(f)

# Collect paragraphs for Bab 1, 2, 3
b1_pars = []
b2_pars = []
b3_pars = []
dp_pars = []

current_bab = 0
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    if t.startswith("BAB I"):
        current_bab = 1
    elif t.startswith("BAB II"):
        current_bab = 2
    elif t.startswith("BAB III"):
        current_bab = 3
    elif "DAFTAR PUSTAKA" in t.upper():
        current_bab = 4
    
    if current_bab == 1:
        b1_pars.append((i, t))
    elif current_bab == 2:
        b2_pars.append((i, t))
    elif current_bab == 3:
        b3_pars.append((i, t))
    elif current_bab == 4:
        dp_pars.append((i, t))

def extract_citations(par_list):
    cits = []
    for idx, text in par_list:
        # Pattern 1: (Author, Year) or (Author & Author, Year) or (Author et al., Year)
        p1 = re.findall(r'\(([A-Z][a-zA-Z\s&.,\-]+?,\s*\d{4}[a-z]?)\)', text)
        for c in p1:
            cits.append((idx, c))
        # Pattern 2: Author et al. (Year) or Author (Year)
        p2 = re.findall(r'([A-Z][a-zA-Z\s&]+?(?:et al\.)?)\s*\((20\d\d[a-z]?|19\d\d[a-z]?)\)', text)
        for a, y in p2:
            a_clean = a.strip()
            # filter out non-author words
            if not any(w in a_clean for w in ["Gambar", "Tabel", "Persamaan", "Rumus", "Metode", "Bulan", "No", "Tahun"]):
                cits.append((idx, f"{a_clean} ({y})"))
    return cits

print("=== CITATIONS IN BAB 1 ===")
c1 = extract_citations(b1_pars)
for idx, c in c1:
    print(f"  P[{idx}]: {c}")

print("\n=== CITATIONS IN BAB 2 ===")
c2 = extract_citations(b2_pars)
for idx, c in c2:
    print(f"  P[{idx}]: {c}")

print("\n=== CITATIONS IN BAB 3 ===")
c3 = extract_citations(b3_pars)
for idx, c in c3:
    print(f"  P[{idx}]: {c}")

# Also check tables
print("\n=== CITATIONS IN TABLES ===")
for t_idx, table in enumerate(doc.tables):
    for r_idx, row in enumerate(table.rows):
        for c_idx, cell in enumerate(row.cells):
            t = cell.text.strip()
            m = re.findall(r'([A-Z][a-zA-Z\s&]+?et al\.\s*\(\d{4}\)|[A-Z][a-zA-Z\s&]+?\s*\(\d{4}\))', t)
            if m:
                print(f"  Table {t_idx} [{r_idx},{c_idx}]: {m}")
