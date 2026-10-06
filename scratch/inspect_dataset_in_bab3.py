import sys
import os
import io
import docx

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(base_dir, "temp_read.docx")

with open(target_file, "rb") as f:
    doc = docx.Document(f)

for i in range(75, 112):
    p = doc.paragraphs[i]
    if len(p.text.strip()) > 0:
        print(f"P[{i}]: {p.text}\n")
