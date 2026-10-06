import docx

doc = docx.Document("BAB 1_1438.docx")

print("=== VERIFYING BAB 1_1438.docx ===")
print("Total Paragraphs:", len(doc.paragraphs))
print("Total Tables:", len(doc.tables))

print("\n--- 1. PARAGRAPH 52 (BAB 2 SOTA NARRATIVE) ---")
p52 = doc.paragraphs[52]
print(p52.text)
words52 = len(p52.text.split())
print(f"Word count: {words52} words (Target: 120-130)")
assert "Xie et al. (2026)" in p52.text
assert "Chen et al." not in p52.text

print("\n--- 2. TABLE 0 ROW 4 (TABEL 2.1 SOTA MATRIX) ---")
t0 = doc.tables[0]
r4 = [c.text.strip().replace("\n", " ") for c in t0.rows[4].cells]
print(" | ".join(r4))
assert "Xie et al. (2026)" in r4[1]

print("\n--- 3. PARAGRAPH 11 (BAB 1 LATAR BELAKANG) ---")
p11 = doc.paragraphs[11]
print(p11.text[:120] + "...")
assert "Xie et al. (2026)" in p11.text or "Xie et al., 2026" in p11.text
assert "Chen et al." not in p11.text

print("\n--- 4. DAFTAR PUSTAKA ---")
start_dp = -1
for i, p in enumerate(doc.paragraphs):
    if "DAFTAR PUSTAKA" in p.text.upper():
        start_dp = i
        break

dp_entries = [p.text.strip() for p in doc.paragraphs[start_dp + 1:] if p.text.strip()]
print(f"Total DAFTAR PUSTAKA entries: {len(dp_entries)}")
assert len(dp_entries) >= 30, "Must be >= 30 references!"

# Check Xie entry
xie_entry = [e for e in dp_entries if e.startswith("Xie, Y.")]
print("Xie entry found:", xie_entry)
assert len(xie_entry) == 1
assert "fpsyg.2025.1732946" in xie_entry[0]
assert "Frontiers in Psychology" in xie_entry[0]

# Check 5 years percentage
recent = sum(1 for e in dp_entries if any(y in e for y in ["(2021)", "(2022)", "(2023)", "(2024)", "(2025)", "(2026)"]))
pct = (recent / len(dp_entries)) * 100
print(f"Journals from 2021-2026: {recent} / {len(dp_entries)} ({pct:.2f}%)")
assert pct >= 80.0, "Must be >= 80%!"

print("\n[ALL CHECKS PASSED PERFECTLY!]")
