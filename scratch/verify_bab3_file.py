with open('BAB_3_Draft_Final.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
current_para = []
narratives = []
in_fence = False

for line in lines:
    l = line.strip()
    if l.startswith('```'):
        in_fence = not in_fence
        if current_para:
            p_text = " ".join(current_para).strip()
            if len(p_text.split()) > 50:
                narratives.append(p_text)
            current_para = []
        continue
    if in_fence:
        continue
    if not l:
        if current_para:
            p_text = " ".join(current_para).strip()
            if len(p_text.split()) > 50:
                narratives.append(p_text)
            current_para = []
        continue
    if l.startswith('#') or l.startswith('|') or l.startswith('**Gambar') or l.startswith('**Tabel') or l.startswith('+--') or l.startswith('$$\\text') or l.startswith('*Catatan') or l.startswith('*di mana') or l.startswith('---'):
        if current_para:
            p_text = " ".join(current_para).strip()
            if len(p_text.split()) > 50:
                narratives.append(p_text)
            current_para = []
        continue
    current_para.append(l)

if current_para:
    p_text = " ".join(current_para).strip()
    if len(p_text.split()) > 50:
        narratives.append(p_text)

print(f'Total paragraf narasi terdeteksi: {len(narratives)}')
all_pass = True
for idx, p in enumerate(narratives):
    cnt = len(p.split())
    status = 'LOLOS (120-130)' if 120 <= cnt <= 130 else f'TIDAK LOLOS ({cnt})'
    if not (120 <= cnt <= 130):
        all_pass = False
    print(f'Paragraf {idx+1:02d}: {cnt} kata [{status}] -> {" ".join(p.split()[:6])}...')

print(f'\nSTATUS KELULUSAN SEMUA PARAGRAF: {all_pass}')
