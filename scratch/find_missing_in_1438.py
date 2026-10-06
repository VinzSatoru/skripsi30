import sys
import docx

sys.path.append(".")
from inventory_all_37_jurnals import ALL_36_JURNALS

doc = docx.Document("BAB 1_1438.docx")
current_text = " ".join([p.text for p in doc.paragraphs[138:]])

print("=== CHECKING ALL 36 JURNALS AGAINST BAB 1_1438.docx DAFTAR PUSTAKA ===")
found = 0
missing = []
for j in ALL_36_JURNALS:
    first_author = j["author"].split(",")[0].strip()
    if first_author in current_text:
        found += 1
    else:
        missing.append(j)
        print(f"MISSING: {j['author']} ({j['year']}) - {j['title'][:60]}... [Bab {j['bab']}]")

print(f"\nFound: {found} / {len(ALL_36_JURNALS)}")
print(f"Missing: {len(missing)}")
