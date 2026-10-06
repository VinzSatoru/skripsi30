import docx
import re

doc = docx.Document("BAB 1_1438.docx")

# Separate into Bab 1, Bab 2, Bab 3, and Daftar Pustaka
b1_text = ""
b2_text = ""
b3_text = ""
dp_text = ""

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
        b1_text += t + "\n"
    elif current_bab == 2:
        b2_text += t + "\n"
    elif current_bab == 3:
        b3_text += t + "\n"
    elif current_bab == 4:
        dp_text += t + "\n"

# Also check tables
for t_idx, table in enumerate(doc.tables):
    for row in table.rows:
        for cell in row.cells:
            # We know Table 0 is in Bab 2, Tables 1-11 are in Bab 3
            if t_idx == 0:
                b2_text += cell.text + "\n"
            else:
                b3_text += cell.text + "\n"

print("=== CITATIONS FOUND IN BAB 1 ===")
c1 = set(re.findall(r'\(([A-Z][a-zA-Z\s&]+(?:et al\.)?,\s*\d{4})\)', b1_text))
for c in sorted(c1):
    print(" ", c)

print("\n=== CITATIONS FOUND IN BAB 2 ===")
c2 = set(re.findall(r'\(([A-Z][a-zA-Z\s&]+(?:et al\.)?,\s*\d{4})\)', b2_text))
# Also direct citations like Taher & Ayon (2024)
c2_direct = set(re.findall(r'([A-Z][a-zA-Z\s&]+(?:et al\.)?)\s*\((20\d\d)\)', b2_text))
for a, y in sorted(c2_direct):
    print(f"  {a} ({y})")

print("\n=== CITATIONS FOUND IN BAB 3 ===")
c3_direct = set(re.findall(r'([A-Z][a-zA-Z\s&]+(?:et al\.)?)\s*\((20\d\d)\)', b3_text))
for a, y in sorted(c3_direct):
    print(f"  {a} ({y})")
