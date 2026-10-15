import docx
import re
import os
import sys

sys.path.insert(0, os.path.abspath("scratch"))
sys.path.insert(0, os.path.abspath("."))
import define_clean_papers as dcp

papers = list(dcp.clean_papers)

# Add 35th reference: Thalla (2026) Dataset
papers.append({
    "cite": "Thalla, 2026",
    "author": "Thalla, M. K.",
    "year": 2026,
    "title": "Sleep Health & Daily Performance Dataset (Version 1)",
    "journal": "Kaggle",
    "volume": "1",
    "issue": "",
    "pages": "",
    "doi": "https://www.kaggle.com/datasets/mohankrishnat/sleep-health-and-daily-performance-dataset",
    "is_dataset": True
})

print(f"Total entries: {len(papers)}")

def clean_authors(author_str):
    s = author_str.replace(" & ", ", ").replace("&", ",")
    tokens = [x.strip() for x in s.split(",") if x.strip()]
    authors = []
    i = 0
    while i < len(tokens):
        if i + 1 < len(tokens) and re.match(r'^[A-Z](\.|\s)*[A-Z]?(\.|\s)*[A-Z]?(\.|\s)*$', tokens[i+1]):
            authors.append(f"{tokens[i]}, {tokens[i+1]}")
            i += 2
        else:
            authors.append(tokens[i])
            i += 1
    return authors

def parse_journal_details(journal_str):
    jname = journal_str
    vol = ""
    issue = ""
    pages = ""
    
    match = re.match(r'^(.*?),\s*(\d+)(?:\((.*?)\))?,\s*(.*)$', journal_str)
    if match:
        jname = match.group(1).strip()
        vol = match.group(2).strip()
        issue = match.group(3).strip() if match.group(3) else ""
        pages = match.group(4).strip()
    else:
        match2 = re.match(r'^(.*?),\s*(\d+),\s*(.*)$', journal_str)
        if match2:
            jname = match2.group(1).strip()
            vol = match2.group(2).strip()
            pages = match2.group(3).strip()
    return jname, vol, issue, pages

# 1. RIS GENERATION
ris_lines = []
for p in papers:
    is_data = p.get("is_dataset", False)
    ris_lines.append("TY  - DATA" if is_data else "TY  - JOUR")
    
    author_list = clean_authors(p["author"])
    for a in author_list:
        ris_lines.append(f"AU  - {a}")
    
    ris_lines.append(f"TI  - {p['title']}")
    
    jname, vol, issue, pages = parse_journal_details(p.get("journal", ""))
    if jname:
        ris_lines.append(f"JO  - {jname}")
        ris_lines.append(f"T2  - {jname}")
    if p.get("year"):
        ris_lines.append(f"PY  - {p['year']}")
        ris_lines.append(f"Y1  - {p['year']}")
    if vol:
        ris_lines.append(f"VL  - {vol}")
    if issue:
        ris_lines.append(f"IS  - {issue}")
    if pages:
        page_match = re.match(r'^([A-Za-z0-9]+)[–\-]+([A-Za-z0-9]+)$', pages)
        if page_match:
            ris_lines.append(f"SP  - {page_match.group(1)}")
            ris_lines.append(f"EP  - {page_match.group(2)}")
        else:
            ris_lines.append(f"SP  - {pages}")
            
    doi = p.get("doi", "")
    if doi:
        clean_doi = doi.replace("https://doi.org/", "").strip()
        if "doi.org" not in clean_doi and not is_data:
            ris_lines.append(f"DO  - {clean_doi}")
        ris_lines.append(f"UR  - {doi}")
        
    ris_lines.append("ER  - ")
    ris_lines.append("")

ris_content = "\n".join(ris_lines)

# 2. BIBTEX GENERATION
bib_lines = []
for p in papers:
    first_author = p["cite"].split(",")[0].replace(" & ", "").replace(" et al.", "").strip()
    cite_key = re.sub(r'[^a-zA-Z0-9]', '', first_author) + str(p["year"])
    is_data = p.get("is_dataset", False)
    entry_type = "misc" if is_data else "article"
    
    bib_lines.append(f"@{entry_type}{{{cite_key},")
    author_list = clean_authors(p["author"])
    bib_authors = " and ".join(author_list)
    bib_lines.append(f"  author = {{{bib_authors}}},")
    bib_lines.append(f"  title = {{{{{p['title']}}}}},")
    
    jname, vol, issue, pages = parse_journal_details(p.get("journal", ""))
    if is_data:
        bib_lines.append(f"  howpublished = {{{jname}}},")
    else:
        if jname:
            bib_lines.append(f"  journal = {{{jname}}},")
    if p.get("year"):
        bib_lines.append(f"  year = {{{p['year']}}},")
    if vol:
        bib_lines.append(f"  volume = {{{vol}}},")
    if issue:
        bib_lines.append(f"  number = {{{issue}}},")
    if pages:
        bib_lines.append(f"  pages = {{{pages.replace('–', '--')}}},")
    
    doi = p.get("doi", "")
    if doi:
        clean_doi = doi.replace("https://doi.org/", "").strip()
        if not is_data:
            bib_lines.append(f"  doi = {{{clean_doi}}},")
        bib_lines.append(f"  url = {{{doi}}},")
    bib_lines.append("}\n")

bib_content = "\n".join(bib_lines)

ris_path = "01_Naskah_Proposal_Master/mendeley_references.ris"
bib_path = "01_Naskah_Proposal_Master/mendeley_references.bib"

with open(ris_path, "w", encoding="utf-8") as f:
    f.write(ris_content)

with open(bib_path, "w", encoding="utf-8") as f:
    f.write(bib_content)

print(f"Generated successfully:")
print(f"1. {ris_path} ({os.path.getsize(ris_path)} bytes)")
print(f"2. {bib_path} ({os.path.getsize(bib_path)} bytes)")
