import os
import docx

def inspect(filename):
    print("="*50)
    print("INSPECTING:", filename)
    try:
        doc = docx.Document(filename)
        text_snippets = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        print(f"Total non-empty paragraphs: {len(text_snippets)}")
        for s in text_snippets[:10]:
            print("  -", s[:100])
        # Check if Bab 2 or Bab II exists in text
        full_text = " ".join(text_snippets)
        for term in ["BAB I", "BAB II", "BAB III", "BAB 1", "BAB 2", "BAB 3", "TINJAUAN PUSTAKA", "LANDASAN TEORI"]:
            if term.lower() in full_text.lower():
                print(f"  --> FOUND TERM: {term}")
    except Exception as e:
        print("  Error:", e)

for f in ["231110003599_SORAYA AZIZAH DHARMAWAN_MA.docx", "BAB 1_1438.docx", "OUTLINE.docx", "OUTLINE_PROPOSAL_1438.docx"]:
    inspect(f)
