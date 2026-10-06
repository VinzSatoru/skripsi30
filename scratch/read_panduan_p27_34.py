import fitz

doc = fitz.open('k3027_panduan-skripsi.pdf')
for p in [27, 33, 34, 42]:
    print(f"=== PAGE {p} ===")
    print(doc[p-1].get_text())
