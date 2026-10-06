import fitz

doc = fitz.open('k3027_panduan-skripsi.pdf')
print("=== PAGE 19 ===")
print(doc[18].get_text())
