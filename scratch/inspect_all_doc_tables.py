import sys
import docx

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('scratch/temp_read.docx')

print(f"Total tables: {len(doc.tables)}")
for i, t in enumerate(doc.tables):
    # Find which paragraph is right before this table
    # We can inspect the first cell or header
    first_cell = t.rows[0].cells[0].text.strip()
    headers = [c.text.strip().replace('\n', ' ') for c in t.rows[0].cells[:4]]
    print(f"Table index {i}: {len(t.rows)} rows x {len(t.columns)} cols | Headers: {headers}")
