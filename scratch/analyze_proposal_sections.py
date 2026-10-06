import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
dump_file = os.path.join(base_dir, "dump_proposal_text.txt")

with open(dump_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Let's inspect Bab 1
b1_lines = []
b2_lines = []
b3_lines = []
dp_lines = []
current_sec = "PRE"

for line in lines:
    if "BAB I" in line:
        current_sec = "BAB1"
    elif "BAB II" in line:
        current_sec = "BAB2"
    elif "BAB III" in line:
        current_sec = "BAB3"
    elif "DAFTAR PUSTAKA" in line:
        current_sec = "DP"
    
    if current_sec == "BAB1":
        b1_lines.append(line)
    elif current_sec == "BAB2":
        b2_lines.append(line)
    elif current_sec == "BAB3":
        b3_lines.append(line)
    elif current_sec == "DP":
        dp_lines.append(line)

print(f"Bab 1 lines: {len(b1_lines)}")
print(f"Bab 2 lines: {len(b2_lines)}")
print(f"Bab 3 lines: {len(b3_lines)}")
print(f"DP lines: {len(dp_lines)}")
