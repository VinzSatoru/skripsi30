import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/dump_proposal_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

paragraphs = text.split("\n\n")

print(f"Total parsed paragraphs: {len(paragraphs)}")

# Let's inspect Bab 1 (P[47] to P[73])
print("\n" + "="*50)
print("=== BAB I INSPECTION ===")
print("="*50)
for p in paragraphs:
    if any(f"P[{i}]:" in p for i in range(47, 74)):
        print(p + "\n")
