import fitz

doc = fitz.open('k3027_panduan-skripsi.pdf')
print("Total pages:", len(doc))

# Search for proposal structure or bab
for i, page in enumerate(doc):
    text = page.get_text()
    t_low = text.lower()
    if "sistematika" in t_low or "proposal" in t_low or "bab ii" in t_low:
        lines = [line.strip() for line in text.split('\n') if any(k in line.lower() for k in ['proposal', 'sistematika', 'bab i', 'bab ii', 'bab iii', 'tinjauan pustaka', 'landasan teori'])]
        if lines:
            print(f"--- Page {i+1} ---")
            for l in lines[:8]:
                print(" ", l)
