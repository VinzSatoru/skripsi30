import docx
import shutil

shutil.copy2("BAB 1_1438.docx", "BAB_1_1438_temp.docx")
doc = docx.Document("BAB_1_1438_temp.docx")

print("Total paragraphs:", len(doc.paragraphs))
print("Total tables:", len(doc.tables))

# Print all paragraphs between P[28] and P[70]
print("\n--- AROUND BAB II BOUNDARY ---")
for i in range(28, 68):
    if i < len(doc.paragraphs):
        p = doc.paragraphs[i]
        print(f"[{i:3d}] ({p.style.name:15s}): {p.text[:90]}")

# Check where tables are placed
# In python-docx, doc.tables is a list of tables. Let's see which table belongs to Bab 2.
print("\n--- TABLES SUMMARY ---")
for i, t in enumerate(doc.tables):
    rows = len(t.rows)
    cols = len(t.columns)
    header = " | ".join(c.text.strip().replace("\n", " ") for c in t.rows[0].cells[:4])
    print(f"Table {i}: {rows}x{cols} | {header[:80]}")
