import urllib.request
import json

dois_to_check = [
    ("Martínez-Plumed et al. (2021) - CRISP-DM", "10.1109/TKDE.2019.2962680"),
    ("El Chakik et al. (2026) - Cost-Sensitive CatBoost", "10.3390/sci8070171"),
    ("Chicco & Jurman (2020) - Confusion Matrix & Metrics", "10.1186/s13040-020-00224-4"),
    ("Chicco & Jurman (2022) - Multi-class AI Evaluation", "10.3389/frobt.2022.876814"),
    ("Schröer et al. (2021) - CRISP-DM SLR", "10.1016/j.procs.2021.01.199"),
    ("Ling & Sheng (2008) - Cost-Sensitive Theory", "10.1007/978-0-387-30164-8_185"),
    ("Harris et al. (2020) - NumPy Nature", "10.1038/s41586-020-2649-2")
]

print("Checking DOIs...")
for label, doi in dois_to_check:
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.citationstyles.csl+json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title', 'N/A')
            container = data.get('container-title', 'N/A')
            print(f"[VALID] {label}\n  -> DOI: https://doi.org/{doi}\n  -> Title: {title}\n  -> Journal: {container}\n")
    except Exception as e:
        print(f"[ERROR] {label} ({doi}): {e}")
