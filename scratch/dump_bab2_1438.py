import docx

doc = docx.Document("BAB 1_1438.docx")
print("=== CURRENT BAB 2 IN BAB 1_1438.docx ===")
for i in range(31, 62):
    p = doc.paragraphs[i]
    print(f"--- P[{i}] ({p.style.name}) ---")
    print(p.text)
