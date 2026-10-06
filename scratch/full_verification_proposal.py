import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('PROPOSAL BAB 1-3.docx')

print(f"=== FULL VERIFICATION OF PROPOSAL BAB 1-3.docx ===")
print(f"Total Paragraphs: {len(doc.paragraphs)}")
print(f"Total Tables: {len(doc.tables)}")

# 1. Check Tables
print("\n--- TABLES AUDIT ---")
for i, t in enumerate(doc.tables):
    h = [c.text.strip().replace('\n', ' ') for c in t.rows[0].cells[:3]]
    print(f"Table {i:2d}: {len(t.rows):2d}x{len(t.columns):2d} | {h}")

# 2. Check Figures & Table Titles in Bab 3
print("\n--- BAB 3 CAPTIONS AUDIT ---")
for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if txt.startswith("Gambar ") or txt.startswith("Tabel "):
        print(f"P[{i:3d}]: {txt}")

# 3. Check Narrative Paragraphs Word Counts
print("\n--- NARRATIVE PARAGRAPHS AUDIT (Word Counts) ---")
b1_narratives = []
b2_narratives = []
b3_narratives = []

curr_bab = ""
for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if "BAB I" in txt:
        curr_bab = "BAB 1"
    elif "BAB II" in txt:
        curr_bab = "BAB 2"
    elif "BAB III" in txt:
        curr_bab = "BAB 3"
    elif "DAFTAR PUSTAKA" in txt:
        curr_bab = "DP"
    
    words = len(txt.split())
    if words >= 100 and not txt.startswith("Tabel") and not txt.startswith("Gambar") and curr_bab != "DP":
        if curr_bab == "BAB 1":
            b1_narratives.append((i, words, txt[:50]))
        elif curr_bab == "BAB 2":
            b2_narratives.append((i, words, txt[:50]))
        elif curr_bab == "BAB 3":
            b3_narratives.append((i, words, txt[:50]))

print(f"Bab 1 Latar Belakang Paragraphs ({len(b1_narratives)}):")
for p_num, w_cnt, snip in b1_narratives:
    status = "OK" if 120 <= w_cnt <= 130 else f"OUT OF RANGE ({w_cnt})"
    print(f"  P[{p_num:3d}]: {w_cnt:3d} words [{status}] | {snip}...")

print(f"\nBab 2 Narrative Paragraphs ({len(b2_narratives)}):")
for p_num, w_cnt, snip in b2_narratives:
    status = "OK" if 120 <= w_cnt <= 130 else f"OUT OF RANGE ({w_cnt})"
    print(f"  P[{p_num:3d}]: {w_cnt:3d} words [{status}] | {snip}...")

print(f"\nBab 3 Narrative Paragraphs ({len(b3_narratives)}):")
for p_num, w_cnt, snip in b3_narratives:
    status = "OK" if 120 <= w_cnt <= 130 else f"OUT OF RANGE ({w_cnt})"
    print(f"  P[{p_num:3d}]: {w_cnt:3d} words [{status}] | {snip}...")

# 4. Check DP
dp_idx = -1
for i, p in enumerate(doc.paragraphs):
    if "DAFTAR PUSTAKA" in p.text.upper():
        dp_idx = i
        break

dp_entries = [doc.paragraphs[j].text.strip() for j in range(dp_idx + 1, len(doc.paragraphs))]
print(f"\n--- DAFTAR PUSTAKA AUDIT ---")
print(f"Total DP Entries: {len(dp_entries)}")
for idx, e in enumerate(dp_entries, 1):
    author = e.split("(")[0].strip()
    year = e.split("(")[1].split(")")[0].strip() if "(" in e else ""
    print(f"  {idx:2d}. {author} ({year})")
