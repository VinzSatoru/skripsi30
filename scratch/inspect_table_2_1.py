import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('scratch/temp_verify_final.docx')
t0 = doc.tables[0]

print(f"Table 2.1 Rows: {len(t0.rows)}, Cols: {len(t0.columns)}")
for r_idx, r in enumerate(t0.rows):
    cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
    print(f"\n--- ROW {r_idx} ---")
    for c_idx, cell in enumerate(cells):
        print(f"  Col {c_idx} [{t0.rows[0].cells[c_idx].text.strip()}]: {cell}")
