import re

with open('BAB_2_Draft_Final.md', 'r', encoding='utf-8') as f:
    text = f.read()

pronouns = ['saya', 'kami', 'aku', 'kita', 'penulis']
found_pronouns = {}
for p in pronouns:
    matches = re.findall(rf'\b{p}\b', text, re.IGNORECASE)
    if matches:
        found_pronouns[p] = len(matches)

hyperbolic_words = [
    'luar biasa', 'menakjubkan', 'revolusioner', 'canggih', 'sempurna', 
    'tanpa cela', 'hebat', 'dijamin', 'mustahil', 'fantastis', 'bombastis', 
    'amat sangat', 'satu-satunya', 'game changer', 'game-changer', 'terhebat',
    'sangat mudah', 'sangat cepat', 'tebakan mesin', 'alat bernama', 'kehebatan'
]
found_hyperboles = {}
for hw in hyperbolic_words:
    matches = re.finditer(rf'\b{hw}\b', text, re.IGNORECASE)
    for m in matches:
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        snippet = text[start:end].replace('\n', ' ')
        found_hyperboles.setdefault(hw, []).append(snippet)

print("=== AUDIT BAB 2 TONE & VOCABULARY ===")
print("Found Pronouns:", found_pronouns)
print("Found Hyperbolic/Promotional Phrases Count:", len(found_hyperboles))
for hw, snippets in found_hyperboles.items():
    print(f"\nWord: '{hw}' ({len(snippets)} times):")
    for s in snippets:
        print(f"  Snippet: ...{s}...")
