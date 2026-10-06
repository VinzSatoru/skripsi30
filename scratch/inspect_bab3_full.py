import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/dump_proposal_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

paragraphs = text.split("\n\n")

print("\n" + "="*50)
print("=== BAB III INSPECTION ===")
print("="*50)
for p in paragraphs:
    if any(f"P[{i}]:" in p for i in range(105, 182)):
        print(p + "\n")
