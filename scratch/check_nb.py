import json

with open("preprocessing_catboost.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb["cells"]):
    source = "".join(cell.get("source", []))
    if "person_id" in source or "country" in source or "day_type" in source:
        print(f"=== Cell {i} ({cell['cell_type']}) ===")
        print(source.strip())
        print()
