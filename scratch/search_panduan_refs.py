import fitz

doc = fitz.open('k3027_panduan-skripsi.pdf')

keywords = ['daftar pustaka', 'pustaka', 'referensi', 'jurnal', 'minimal', 'jumlah', 'tahun terakhir']

print("Searching panduan for reference rules...")
for page_num in range(len(doc)):
    page_text = doc[page_num].get_text()
    for line in page_text.split('\n'):
        line_clean = line.strip()
        if any(kw in line_clean.lower() for kw in ['daftar pustaka', 'referensi', 'jurnal', 'minimal', 'sumber pustaka', 'sumber rujukan']):
            print(f"Page {page_num+1}: {line_clean}")
