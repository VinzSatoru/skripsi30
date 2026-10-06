import sys
import os
import docx

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(base_dir, "temp_read.docx")

with open(target_file, "rb") as f:
    doc = docx.Document(f)

for i, t in enumerate(doc.tables):
    txt = t.rows[0].cells[0].text
    print(f"Table {i}: {len(t.rows)} rows x {len(t.columns)} cols | {txt}")
    if "Atribut" in t.rows[0].cells[1].text or i == 2:
        for r in t.rows[:5]:
            print([c.text.strip() for c in r.cells])
