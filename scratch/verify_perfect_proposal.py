import docx
import re
import os

target = "PROPOSAL_BAB_1-3_Revisi.docx"
print(f"=== FULL AUDIT OF {target} ===")

doc = docx.Document(target)
print("Total Paragraphs:", len(doc.paragraphs))
print("Total Tables:", len(doc.tables))

# 1. Check Alqudah, Loh, Hapsari, Li in entire document
print("\n--- 1. AUDIT UNVERIFIED / DUPLICATE NAMES ---")
bad_names = ["Alqudah", "Loh et al.", "Hapsari et al."]
for name in bad_names:
    found = [i for i, p in enumerate(doc.paragraphs) if name.lower() in p.text.lower()]
    print(f"Occurrences of '{name}': {len(found)}")
    assert len(found) == 0, f"Found '{name}' in document!"

# 2. Check P[34], P[36], P[39], P[49], P[67], P[101]
print("\n--- 2. PARAGRAPH WORD COUNTS CHECK ---")
check_indices = [7, 8, 9, 10, 11, 12, 34, 35, 36, 38, 39, 41, 42, 43, 45, 46, 48, 49, 51, 52, 53, 58, 60, 65, 67, 101, 125, 130]
all_pass = True
for idx in check_indices:
    p = doc.paragraphs[idx]
    w = len(p.text.split())
    status = "PASS" if 120 <= w <= 130 else f"FAIL ({w})"
    if status != "PASS":
        all_pass = False
    print(f"  P[{idx:3d}]: {w:3d} words [{status}] | {p.text[:55]}...")

assert all_pass, "Some narrative paragraphs are out of 120-130 range!"
print("All checked narrative paragraphs are strictly in 120-130 range!")

# 3. Check DAFTAR PUSTAKA
print("\n--- 3. DAFTAR PUSTAKA AUDIT ---")
start_dp = -1
for i, p in enumerate(doc.paragraphs):
    if "DAFTAR PUSTAKA" in p.text.upper():
        start_dp = i
        break

dp_entries = [p.text.strip() for p in doc.paragraphs[start_dp + 1:] if p.text.strip()]
print(f"Total DAFTAR PUSTAKA entries: {len(dp_entries)}")
assert len(dp_entries) >= 30, f"Must be >= 30 entries, got {len(dp_entries)}"

# Check DOIs and URLs
no_doi = [e for e in dp_entries if "http" not in e and "doi.org" not in e]
print(f"Entries without DOI/URL: {len(no_doi)}")
assert len(no_doi) == 0, f"Entries missing DOI: {no_doi}"

# Check recent percentage
recent = sum(1 for e in dp_entries if any(y in e for y in ["(2021)", "(2022)", "(2023)", "(2024)", "(2025)", "(2026)"]))
pct = (recent / len(dp_entries)) * 100
print(f"Recent journals (2021-2026): {recent} / {len(dp_entries)} ({pct:.2f}%)")
assert pct >= 80.0, f"Must be >= 80%, got {pct:.2f}%"

# 4. Check 1-to-1 in-text citation match
print("\n--- 4. 1-TO-1 BIJECTION VERIFICATION ---")
# Collect all body text before DP
body_text = " ".join([doc.paragraphs[i].text for i in range(start_dp)])
for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            body_text += " " + cell.text

orphans = []
for idx, entry in enumerate(dp_entries, 1):
    author = entry.split("(")[0].split(",")[0].strip()
    year = entry.split("(")[1].split(")")[0].strip() if "(" in entry else ""
    if author.lower() not in body_text.lower():
        orphans.append((idx, author, year, entry))
        print(f"  ORPHAN ENTRY in DP: #{idx} {author} ({year})")

print(f"Total orphan entries in DP: {len(orphans)}")
assert len(orphans) == 0, f"Found orphan entries in DP: {orphans}"

print("\n[ALL AUDIT CHECKS PASSED WITH 100% PERFECTION!]")
