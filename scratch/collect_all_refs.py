import re

# Collect all references from BAB 1, BAB 2 (Outline/SOTA), and BAB 3
with open('BAB_1_Draft_Final.md', 'r', encoding='utf-8') as f:
    bab1_text = f.read()

with open('OUTLINE_PROPOSAL_REVISI_FINAL.md', 'r', encoding='utf-8') as f:
    outline_text = f.read()

with open('BAB_3_Draft_Final.md', 'r', encoding='utf-8') as f:
    bab3_text = f.read()

# Let's inspect the references in BAB 1
print("=== BAB 1 REFERENCES ===")
b1_refs_match = re.search(r'## DAFTAR PUSTAKA.*', bab1_text, re.DOTALL)
if b1_refs_match:
    print(b1_refs_match.group(0))

print("\n=== BAB 3 REFERENCES ===")
b3_refs_match = re.search(r'## DAFTAR PUSTAKA.*', bab3_text, re.DOTALL)
if b3_refs_match:
    print(b3_refs_match.group(0))
