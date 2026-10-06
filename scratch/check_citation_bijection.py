import sys
import re
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('scratch/temp_verify_final.docx')

# 1. Extract DP authors and years
dp_idx = -1
for i, p in enumerate(doc.paragraphs):
    if "DAFTAR PUSTAKA" in p.text.upper():
        dp_idx = i
        break

dp_entries = [p.text.strip() for p in doc.paragraphs[dp_idx+1:] if p.text.strip()]
print(f"Total DP Entries: {len(dp_entries)}")

dp_dict = {}
for e in dp_entries:
    # Match: Author, A. B. (Year)
    m = re.match(r'^([^(]+)\s*\((\d{4}[a-z]?)\)', e)
    if m:
        first_author = m.group(1).split(",")[0].strip()
        year = m.group(2)
        dp_dict[(first_author.lower(), year)] = e[:60]
    else:
        print(f"Failed to parse DP entry: {e[:60]}")

print(f"Parsed {len(dp_dict)} DP keys.")

# 2. Extract in-text citations from Bab 1, 2, 3
in_text_citations = []
for i in range(dp_idx):
    p = doc.paragraphs[i]
    txt = p.text
    # find patterns like (Author, Year) or Author et al. (Year) or (Author et al., Year)
    # Regex for citations
    matches = re.findall(r'([A-Z][a-zA-Z\u00C0-\u017F\-\']+)(?:\s+et\s+al\.|\s+&\s+[A-Z][a-zA-Z\u00C0-\u017F\-\']+)?\s*[\(,]\s*(\d{4}[a-z]?)', txt)
    for auth, yr in matches:
        in_text_citations.append((auth.lower(), yr, i, txt[:40]))

# Also check tables
for t_idx, t in enumerate(doc.tables):
    for r in t.rows:
        for c in r.cells:
            txt = c.text
            matches = re.findall(r'([A-Z][a-zA-Z\u00C0-\u017F\-\']+)(?:\s+et\s+al\.|\s+&\s+[A-Z][a-zA-Z\u00C0-\u017F\-\']+)?\s*[\(,]\s*(\d{4}[a-z]?)', txt)
            for auth, yr in matches:
                in_text_citations.append((auth.lower(), yr, f"Table {t_idx}", txt[:40]))

print(f"Total in-text citation instances found: {len(in_text_citations)}")
unique_in_text = sorted(list(set((a, y) for a, y, _, _ in in_text_citations)))
print(f"Unique in-text (Author, Year) pairs: {len(unique_in_text)}")

# Check for orphan in-text citations (not in DP)
print("\n--- CHECKING IN-TEXT CITATIONS AGAINST DP ---")
orphan_in_text = []
for a, y in unique_in_text:
    found = False
    for (dp_a, dp_y) in dp_dict.keys():
        if (a in dp_a or dp_a in a) and y == dp_y:
            found = True
            break
    if not found:
        # Check if it's a known non-citation like (CRISP-DM, 2021) or something
        orphan_in_text.append((a, y))

if orphan_in_text:
    print(f"[WARNING] Orphan in-text citations found ({len(orphan_in_text)}):")
    for a, y in orphan_in_text:
        print(f"  - {a} ({y})")
else:
    print("[PERFECT] All in-text citations exist in DAFTAR PUSTAKA!")

# Check for orphan DP entries (not cited in text)
print("\n--- CHECKING DP ENTRIES AGAINST IN-TEXT CITATIONS ---")
orphan_dp = []
for (dp_a, dp_y), desc in dp_dict.items():
    found = False
    for a, y in unique_in_text:
        if (a in dp_a or dp_a in a) and y == dp_y:
            found = True
            break
    if not found:
        orphan_dp.append((dp_a, dp_y, desc))

if orphan_dp:
    print(f"[WARNING] Orphan DP entries found ({len(orphan_dp)}):")
    for dp_a, dp_y, desc in orphan_dp:
        print(f"  - {dp_a} ({dp_y}): {desc}...")
else:
    print("[PERFECT] All DAFTAR PUSTAKA entries are actively cited in the proposal!")
