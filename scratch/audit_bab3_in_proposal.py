import docx

doc = docx.Document("temp_inspect_proposal.docx")

print("=== BAB 3 DETAILED AUDIT IN PROPOSAL BAB 1-3.docx ===")

# Locate Bab 3
b3_start = -1
dp_start = -1
for i, p in enumerate(doc.paragraphs):
    if p.text.strip().startswith("BAB III"):
        b3_start = i
    if "DAFTAR PUSTAKA" in p.text.upper():
        dp_start = i

print(f"Bab 3 starts at P[{b3_start}], Daftar Pustaka starts at P[{dp_start}]")

# Check narrative paragraphs in Bab 3 (paragraphs with > 50 words)
b3_narrative = []
for i in range(b3_start, dp_start):
    p = doc.paragraphs[i]
    words = len(p.text.split())
    if words >= 40:
        b3_narrative.append((i, words, p.text.strip()[:60]))

print(f"\nTotal narrative paragraphs found in Bab 3: {len(b3_narrative)}")
all_b3_in_range = True
for idx, (p_num, w_cnt, snippet) in enumerate(b3_narrative, 1):
    status = "OK" if 120 <= w_cnt <= 130 else f"OUT OF RANGE ({w_cnt})"
    if status != "OK":
        all_b3_in_range = False
    print(f"  {idx:2d}. P[{p_num:3d}]: {w_cnt:3d} words [{status}] | {snippet}...")

print(f"\nAll Bab 3 narrative paragraphs in 120-130 range: {all_b3_in_range}")

# Check for manual calculation 3.6.5
found_manual_calc = False
for i in range(b3_start, dp_start):
    p = doc.paragraphs[i]
    if "3.6.5" in p.text or "Perhitungan Manual" in p.text or "Toy Example" in p.text or "Ordered Target Statistics" in p.text and "w_c" in p.text:
        found_manual_calc = True
        print(f"Manual calc heading/mention found at P[{i}]: {p.text.strip()[:80]}")

print("Manual calculation section present:", found_manual_calc)

# Check Tables in Bab 3 (Tables 1 to 11)
print("\n--- TABLES IN PROPOSAL BAB 1-3.docx ---")
for t_idx, t in enumerate(doc.tables):
    rows = len(t.rows)
    cols = len(t.columns)
    header = " | ".join(c.text.strip().replace("\n", " ") for c in t.rows[0].cells[:4])
    print(f"Table {t_idx:2d}: {rows:2d}x{cols:2d} | {header[:75]}...")
