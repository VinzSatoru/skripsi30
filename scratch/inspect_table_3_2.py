import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('scratch/temp_verify_final.docx')
t2 = doc.tables[2] # Table 3.2 (Deskripsi Atribut)

print(f"Table 3.2 Rows: {len(t2.rows)}, Cols: {len(t2.columns)}")
for r_idx in range(min(5, len(t2.rows))):
    cells = [c.text.strip().replace('\n', ' ') for c in t2.rows[r_idx].cells]
    print(f"  Row {r_idx}: {cells}")

print("...")
for r_idx in range(max(0, len(t2.rows)-3), len(t2.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t2.rows[r_idx].cells]
    print(f"  Row {r_idx}: {cells}")
