import sys
import os
import shutil
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')

outline_path = "OUTLINE_PROPOSAL_REVISI_FINAL.docx"
doc = docx.Document(outline_path)

# 1. Update Title in Table 0
new_title = "Penerapan Algoritma CatBoost dan SHAP untuk Klasifikasi Risiko Gangguan Tidur Berbasis Gaya Hidup"
t0 = doc.tables[0]
for r in t0.rows:
    if "JUDUL PENELITIAN" in r.cells[0].text:
        r.cells[1].text = new_title
        print(f"[OK] Table 0 Title updated: {new_title} ({len(new_title.split())} kata)")

# Also update in P[1] or text if present
for p in doc.paragraphs:
    if "Judul" in p.text:
        p.text = f"Judul Usulan Skripsi : {new_title}"

# 2. Rebuild Table 1 (Literature Review / Research Gap Table)
# The advisor requested:
# - Jelaskan temuan gap atau kekurangan dari sumber jurnalnya
# - Apa sih yang penelitian ini perbaiki dari gap tersebut
# - Penelitian ini lebih baik dari jurnal ini karena...
# - Dibuat dalam bentuk tabel dan mudah dibaca

t1 = doc.tables[1]

# Clear existing rows in t1 except header
# Let's inspect current rows count
print(f"Current Table 1 rows: {len(t1.rows)}, cols: {len(t1.columns)}")

# We will define 6 columns:
headers = [
    "No",
    "Peneliti, Tahun & Reputasi Jurnal",
    "Metode & Hasil Utama",
    "Temuan Gap / Kekurangan Jurnal",
    "Apa yang Diperbaiki Penelitian Ini",
    "Penelitian Ini Lebih Baik Karena..."
]

# Set header texts
for c_idx, h_text in enumerate(headers):
    t1.rows[0].cells[c_idx].text = h_text

# Define the 6 elite SOTA rows answering the advisor's questions directly:
sota_data = [
    (
        "1",
        "Taher & Ayon (2024)\n[IEEE PEEIACON]",
        "Gradient Boosting, Random Forest, AdaBoost pada data gaya hidup tidur.\n\nHasil: Gradient Boosting meraih akurasi tertinggi 93,80%.",
        "Model beroperasi murni sebagai kotak hitam (black-box) tanpa penjelasan (XAI); hanya mengeluarkan skor risiko tanpa mampu menjelaskan faktor pemicu spesifik pasien (lack of actionable insight).",
        "Mengintegrasikan metode Explainable AI (Tree-SHAP) untuk membuka kotak hitam model dan menghitung nilai kontribusi marginal setiap fitur gaya hidup secara transparan.",
        "Penelitian ini lebih baik karena tidak hanya menebak tingkat risiko secara akurat, melainkan menyajikan penjelasan transparan 'mengapa' risiko tersebut muncul dan kebiasaan spesifik apa yang memicunya."
    ),
    (
        "2",
        "Lin et al. (2025)\n[Frontiers in Psychiatry, Q1]",
        "ANN, Decision Tree, Naive Bayes pada 20.645 data survei mahasiswa.\n\nHasil: Berhasil memetakan korelasi durasi layar, kopi, dan begadang terhadap kualitas tidur.",
        "Analisis model hanya berlaku pada tataran agregat populasi umum (rata-rata kelompok); tidak mampu memberikan penjelasan risiko secara personal untuk masing-masing individu pasien.",
        "Menerapkan analisis SHAP lokal (waterfall plot) yang membedah profil risiko unik tiap individu secara interaktif per sesi pemeriksaan.",
        "Penelitian ini lebih baik karena mendukung kedokteran personal (personalized healthcare); dua pasien dengan tingkat risiko sama dapat diketahui akar penyebab kebiasaan yang berbeda secara spesifik."
    ),
    (
        "3",
        "Ha et al. (2023)\n[Journal of Medical Internet Research, Q1]",
        "XGBoost + SHAP pada 4.622 kuesioner medis klinis rumah sakit.\n\nHasil: Mencapai AUROC >0,897 untuk klasifikasi OSA dan insomnia.",
        "Fitur berbasis kuesioner medis statis di rumah sakit; metode SHAP hanya difungsikan sebatas seleksi fitur di awal, bukan untuk eksplanasi interaktif per pasien saat prediksi dijalankan.",
        "Memanfaatkan 32 metrik gaya hidup digital harian yang bersifat modifiable (dapat diubah perilakunya), serta mengintegrasikan Tree-SHAP secara real-time saat inferensi.",
        "Penelitian ini lebih baik karena eksplanasi XAI dihasilkan seketika saat pasien mengisi data, dan berfokus pada kebiasaan yang dapat langsung diubah pasien tanpa perlu uji lab klinis yang mahal."
    ),
    (
        "4",
        "Xie et al. (2026)\n[Frontiers in Psychology, Q1]",
        "PLS + XGBoost + One-Hot Encoding + SHAP pada survei tidur mahasiswa.\n\nHasil: Mengidentifikasi durasi tidur, stres, dan gawai sebagai prediktor utama.",
        "XGBoost mewajibkan One-Hot Encoding pada data kategori sehingga fitur terpecah menjadi variabel biner semu; atribusi SHAP terfragmentasi dan arti semantik aslinya menjadi hilang/membingungkan dokter.",
        "Mengadopsi algoritma CatBoost dengan fitur bawaan Ordered Target Statistics (native categorical handling) tanpa melalui prosedur One-Hot Encoding.",
        "Penelitian ini lebih baik karena nilai kontribusi SHAP tetap utuh pada nama variabel aslinya (misal: profesi, kronotipe), menjaga integritas semantik klinis tanpa ledakan dimensi fitur artifisial."
    ),
    (
        "5",
        "Das et al. (2025)\n[Nature and Science of Sleep, Q1]",
        "CatBoost, XGBoost, Random Forest, SVM pada 1.222 pasien insomnia komorbid.\n\nHasil: CatBoost terbukti terbaik (akurasi 71,67%, AUC 77,27%).",
        "Klasifikasi terbatas pada target biner (2 kelas), populasi sempit pasien penyakit kronis di rumah sakit, eksplanasi SHAP hanya di tingkat global populasi, dan tanpa sistem aplikasi terapan.",
        "Membangun klasifikasi multi-kelas 4 tingkatan risiko (Healthy, Mild, Moderate, Severe) dengan cost-sensitive learning pada 100.000 data populasi umum, dan membangun prototipe Web CDSS.",
        "Penelitian ini lebih baik karena mampu mendeteksi gradasi keparahan klinis secara halus, menangani class imbalance ekstrem (Severe 4,07%), dan menyediakan prototipe web interaktif siap pakai."
    ),
    (
        "6",
        "Srinivasu et al. (2024)\n[Scientific Reports, Nature Portfolio, Q1]",
        "CatBoost + Tree-SHAP pada data tabular klinis kanker payudara.\n\nHasil: Meraih akurasi 99,3% dengan visualisasi atribusi fitur yang sangat jelas.",
        "Divalidasi hanya pada data laboratorium sel kanker yang bersifat statis, belum pernah diuji pada variabel perilaku gaya hidup manusia (modifiable lifestyle) untuk kasus gangguan tidur.",
        "Mengadaptasi keunggulan komputasi CatBoost + Tree-SHAP ke domain kesehatan tidur era digital dan mentranslasikan nilai eksplanasi matematis menjadi modul rekomendasi Sleep Hygiene.",
        "Penelitian ini lebih baik karena tidak berhenti pada pembuktian grafik teoretis, melainkan menjembatani nilai XAI menjadi modul rencana aksi perilaku kebersihan tidur yang aplikatif bagi masyarakat."
    )
]

# Ensure table has enough rows
while len(t1.rows) < len(sota_data) + 1:
    t1.add_row()

# Populate rows
for r_idx, row_vals in enumerate(sota_data, 1):
    r = t1.rows[r_idx]
    for c_idx, val in enumerate(row_vals):
        r.cells[c_idx].text = val

# Format Table 1
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

for r_idx, r in enumerate(t1.rows):
    for c_idx, c in enumerate(r.cells):
        if r_idx == 0:
            set_cell_background(c, "1E293B") # dark slate header
        elif r_idx % 2 == 1:
            set_cell_background(c, "F8FAFC") # light zebra
        else:
            set_cell_background(c, "FFFFFF")
            
        for p in c.paragraphs:
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            for run in p.runs:
                run.font.name = "Times New Roman"
                if r_idx == 0:
                    run.font.size = Pt(9.5)
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    run.bold = True
                else:
                    run.font.size = Pt(9)
                    if c_idx == 0:
                        run.bold = True
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    elif c_idx == 1:
                        run.bold = True
                    elif c_idx == 5:
                        run.bold = True # Highlight "Penelitian ini lebih baik karena..."

print(f"[OK] Table 1 successfully rebuilt with 6 rows and explicit comparative columns!")

# Also update Table 0 "TINJAUAN PUSTAKA (STATE OF THE ART)" summary cell in row 3
for r in t0.rows:
    if "TINJAUAN PUSTAKA" in r.cells[0].text:
        r.cells[1].text = (
            "Penelitian ini berpijak pada 6 kajian internasional bereputasi: "
            "(1) Taher & Ayon (2024, IEEE) membuktikan keunggulan Gradient Boosting pada data tidur namun murni black-box; "
            "(2) Lin et al. (2025, Frontiers in Psychiatry Q1) menganalisis 20.645 mahasiswa namun hanya pada agregat populasi umum; "
            "(3) Ha et al. (2023, JMIR Q1) menerapkan XGBoost+SHAP namun kuesioner statis dan SHAP hanya untuk seleksi fitur awal; "
            "(4) Xie et al. (2026, Frontiers in Psychology Q1) meneliti tidur mahasiswa dengan XGBoost namun One-Hot Encoding memecah atribusi SHAP; "
            "(5) Das et al. (2025, Nature and Science of Sleep Q1) membuktikan CatBoost terbaik untuk insomnia (AUC 77,27%) namun terbatas biner komorbid; "
            "(6) Srinivasu et al. (2024, Scientific Reports Q1) memvalidasi CatBoost+SHAP (akurasi 99,3%) pada kanker statis. "
            "Celah riset ini dijembatani dengan menggabungkan CatBoost (native categorical) dan Tree-SHAP lokal/global pada 100.000 data gaya hidup digital multi-kelas 4 risiko, yang ditranslasikan menjadi Web CDSS interaktif berbasis Sleep Hygiene."
        )
        print("[OK] Table 0 Literature Review narrative updated!")

doc.save(outline_path)
print(f"[SUCCESS] Updated and saved {outline_path}!")
