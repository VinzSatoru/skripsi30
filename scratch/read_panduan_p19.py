import fitz

doc = fitz.open('k3027_panduan-skripsi.pdf')
for p in [19, 20, 21, 22]:
    print(f"=== PAGE {p} ===")
    print(doc[p-1].get_text())
