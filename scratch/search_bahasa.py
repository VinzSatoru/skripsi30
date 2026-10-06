import fitz

doc = fitz.open('k3027_panduan-skripsi.pdf')
for i, page in enumerate(doc):
    t = page.get_text()
    if "penggunaan bahasa" in t.lower() or "kaidah bahasa" in t.lower() or "kata ganti" in t.lower() or "b. bahasa" in t.lower() or "b. tata tulis" in t.lower():
        print(f"=== Page {i+1} ===")
        lines = [l.strip() for l in t.split('\n') if l.strip()]
        for l in lines[:15]:
            print(" ", l)
