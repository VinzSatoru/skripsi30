import docx
import re
import shutil

shutil.copy2("PROPOSAL BAB 1-3.docx", "temp_inspect_proposal.docx")
with open("temp_inspect_proposal.docx", "rb") as f:
    doc = docx.Document(f)

# The 34 clean authors
clean_authors = [
    "Amann", "Bhattarai", "Chicco", "Das", "Deivendran",
    "El Chakik", "Ha", "Hancock", "Henrich", "Hulsen",
    "Jahrami", "Kaya", "Lin", "Lundberg", "Martínez-Plumed",
    "Mawardi", "Medic", "Prokhorenkova", "Putra", "Rahman",
    "Sadeghi", "Schröer", "Srinivasu", "Taher", "Uzubuaku",
    "Wang", "Widayati", "Windred", "Wolak", "Wu", "Xie", "Zhang"
]

print(f"Total author keys: {len(clean_authors)}")

# Check every paragraph for citations
citations_found = []
for i in range(len(doc.paragraphs)):
    if "DAFTAR PUSTAKA" in doc.paragraphs[i].text.upper():
        break
    t = doc.paragraphs[i].text
    # find parenthetical (Author, Year)
    pats = re.findall(r'\(([A-Z][a-zA-Z\s&.,\-]+?,\s*\d{4}[a-z]?)\)', t)
    for c in pats:
        citations_found.append((i, c))
    # narrative Author et al. (Year)
    pats2 = re.findall(r'([A-Z][a-zA-Z\s&]+?(?:et al\.)?)\s*\((20\d\d[a-z]?|19\d\d[a-z]?)\)', t)
    for a, y in pats2:
        if not any(w in a for w in ["Gambar", "Tabel", "Persamaan", "Rumus", "Metode", "Bulan", "No", "Tahun"]):
            citations_found.append((i, f"{a.strip()} ({y})"))

print(f"Total citations found in body: {len(citations_found)}")
unrecognized = []
for idx, c in citations_found:
    matched = any(auth.lower() in c.lower() for auth in clean_authors)
    if not matched:
        unrecognized.append((idx, c))

print(f"Unrecognized citations: {len(unrecognized)}")
for idx, c in unrecognized:
    print(f"  P[{idx}]: {c}")
