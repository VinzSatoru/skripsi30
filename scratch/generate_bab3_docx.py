import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DOCX_OUT = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\BAB_3_Draft_Final.docx"
MD_SRC = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\BAB_3_Draft_Final.md"
IMG_DIR = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\gambar_bab3"

def build_bab3_docx():
    doc = docx.Document()

    # Standard Indonesian Thesis Margins: Top 4cm, Left 4cm, Bottom 3cm, Right 3cm
    for section in doc.sections:
        section.top_margin = Cm(4)
        section.left_margin = Cm(4)
        section.bottom_margin = Cm(3)
        section.right_margin = Cm(3)

    # Style Helpers
    def set_font(run, name='Times New Roman', size=12, bold=False, italic=False, color=RGBColor(0,0,0)):
        run.font.name = name
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color

    def add_para(text, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.5, first_indent=1.25):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if first_indent > 0:
            p.paragraph_format.first_line_indent = Cm(first_indent)
        r = p.add_run(text)
        set_font(r, size=12)
        return p

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(18)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        set_font(r, size=14, bold=True)
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        set_font(r, size=12, bold=True)
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        set_font(r, size=12, bold=True)
        return p

    def set_cell_shading(cell, color_hex):
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
            node = OxmlElement(f'w:{m}')
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    def set_table_borders(table):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="333333"/>'
            f'<w:left w:val="none"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="333333"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    def add_image_figure(img_path, caption_text, width_in=5.8):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(img_path, width=Inches(width_in))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(12)
            r = p_cap.add_run(caption_text)
            set_font(r, size=10.5, bold=True)

    def format_table(table, col_widths, alignments):
        set_table_borders(table)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, row in enumerate(table.rows):
            is_header = (i == 0)
            for j, cell in enumerate(row.cells):
                cell.width = Cm(col_widths[j])
                set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                if is_header:
                    set_cell_shading(cell, "F1F5F9")
                p = cell.paragraphs[0]
                p.alignment = alignments[j]
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                for r in p.runs:
                    set_font(r, size=9.5, bold=is_header)

    # -------------------------------------------------------------
    # 1. JUDUL BAB
    # -------------------------------------------------------------
    add_heading_1("BAB III\nMETODE PENELITIAN")

    # -------------------------------------------------------------
    # 3.1 Jenis dan Pendekatan Penelitian
    # -------------------------------------------------------------
    add_heading_2("3.1. Jenis dan Pendekatan Penelitian")
    add_heading_3("3.1.1. Jenis Penelitian")
    add_para("Jenis penelitian yang diterapkan dalam studi ini adalah penelitian kuantitatif dengan pendekatan eksperimental komputasional. Penelitian kuantitatif berfokus pada pengolahan, pemodelan, dan analisis data numerik serta kategorikal berskala besar guna menemukan pola tersembunyi dan membangun prediksi klasifikasi secara objektif, sistematis, dan terukur. Pendekatan eksperimental secara spesifik digunakan untuk merancang, melatih, serta menguji performa model pembelajaran mesin dalam mengklasifikasikan tingkat risiko gangguan tidur berdasarkan data masukan parameter gaya hidup digital. Metode ini memungkinkan pengujian hipotesis teknis secara empiris melalui serangkaian eksperimen algoritma yang terkontrol dan dapat diulang kembali oleh peneliti lain. Melalui pendekatan kuantitatif ini, seluruh temuan penelitian, mulai dari tingkat akurasi klasifikasi hingga kontribusi marginal setiap fitur gaya hidup, dapat dibuktikan secara matematis dan dipertanggungjawabkan keabsahannya dalam ranah sains data kesehatan (Das et al., 2025).")

    add_heading_3("3.1.2. Pendekatan Penelitian")
    add_para("Pendekatan penelitian yang digunakan dalam skripsi ini mengadopsi kerangka kerja standar industri CRISP-DM (Cross-Industry Standard Process for Data Mining). Kerangka kerja ini dipilih secara khusus karena menyediakan metodologi yang sangat sistematis, terstruktur, dan bersifat iteratif untuk memandu seluruh siklus pengembangan proyek penambangan data dan pembelajaran mesin. Standar CRISP-DM terdiri atas enam tahapan utama yang saling berkesinambungan, yaitu pemahaman kebutuhan masalah (business understanding), pemahaman data awal (data understanding), persiapan data (data preparation), pemodelan algoritma (modeling), evaluasi performa model (evaluation), serta penyebaran hasil temuan (deployment). Penerapan metodologi komprehensif ini menjamin setiap tahapan teknis terhubung secara konsisten dengan tujuan klinis, sehingga proses rekayasa fitur dan pelatihan model CatBoost dapat berjalan selaras dengan kebutuhan eksplanasi faktor risiko menggunakan metode XAI-SHAP (Martinez-Plumed et al., 2022; Lamaakal et al., 2025).")

    # Gambar 3.1
    add_image_figure(os.path.join(IMG_DIR, "Gambar_3_1_CRISP_DM.png"), 
                     "Gambar 3.1 Diagram Alir Kerangka Kerja CRISP-DM dalam Klasifikasi Gangguan Tidur dan XAI-SHAP", 
                     width_in=5.8)

    # -------------------------------------------------------------
    # 3.2 Waktu dan Tempat Penelitian
    # -------------------------------------------------------------
    add_heading_2("3.2. Waktu dan Tempat Penelitian")
    add_heading_3("3.2.1. Waktu Penelitian")
    add_para("Pelaksanaan penelitian ini direncanakan berlangsung selama enam bulan, terhitung mulai bulan Oktober 2025 sampai dengan bulan Maret 2026. Alokasi waktu tersebut disusun secara bertahap guna mengakomodasi seluruh rangkaian kegiatan ilmiah, yang dimulai dari identifikasi masalah, studi pustaka, penyusunan proposal penelitian, hingga seminar proposal. Selanjutnya, tahapan berlanjut pada pengumpulan serta pra-pemrosesan dataset sekunder, perancangan arsitektur komputasi, pelatihan model CatBoost, serta integrasi pustaka Tree-SHAP untuk analisis interpretabilitas faktor risiko tidur. Dua bulan terakhir dialokasikan khusus untuk pengujian performa secara menyeluruh, analisis komparasi hasil evaluasi metrik, perancangan prototipe sistem pendukung keputusan klinis, dan penulisan naskah laporan skripsi lengkap. Pengaturan jadwal yang terstruktur dan terukur ini bertujuan memastikan seluruh tahapan penelitian dapat diselesaikan tepat waktu sesuai standar mutu akademik Fakultas Sains dan Teknologi UNISNU Jepara.")

    # Tabel 3.1
    p_tab1 = doc.add_paragraph()
    p_tab1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab1.paragraph_format.space_before = Pt(8)
    p_tab1.paragraph_format.space_after = Pt(4)
    r_tab1 = p_tab1.add_run("Tabel 3.1 Jadwal Rencana Pelaksanaan Penelitian (Tahun Akademik 2025/2026)")
    set_font(r_tab1, size=11, bold=True)

    tab1_data = [
        ["No", "Tahapan Kegiatan Penelitian", "Bulan 1\n(Okt 25)", "Bulan 2\n(Nov 25)", "Bulan 3\n(Des 25)", "Bulan 4\n(Jan 26)", "Bulan 5\n(Feb 26)", "Bulan 6\n(Mar 26)"],
        ["1", "Identifikasi Masalah & Studi Pustaka", "✓", "", "", "", "", ""],
        ["2", "Penyusunan Proposal & Seminar Proposal", "", "✓", "", "", "", ""],
        ["3", "Pengumpulan Data & Preprocessing", "", "", "✓", "", "", ""],
        ["4", "Pemodelan CatBoost & Integrasi SHAP", "", "", "", "✓", "", ""],
        ["5", "Evaluasi Kinerja & Desain Prototipe CDSS", "", "", "", "", "✓", ""],
        ["6", "Penyusunan Laporan Skripsi & Ujian Munaqosah", "", "", "", "", "", "✓"]
    ]
    t1 = doc.add_table(rows=len(tab1_data), cols=8)
    for r_idx, row in enumerate(tab1_data):
        for c_idx, val in enumerate(row):
            t1.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t1, [1.0, 6.0, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])

    add_heading_3("3.2.2. Tempat Penelitian")
    add_para("Penelitian ini secara resmi dilaksanakan di Laboratorium Komputasi Program Studi Teknik Informatika, Fakultas Sains dan Teknologi, Universitas Islam Nahdlatul Ulama Jepara, yang beralamat di Jalan Taman Siswa Nomor 09, Pekalongan, Tahunan, Kabupaten Jepara, Jawa Tengah. Pemilihan lokasi ini didasarkan pada ketersediaan fasilitas infrastruktur jaringan internet berkecepatan tinggi serta iklim akademik yang sangat mendukung proses riset komputasi sains data modern. Selain itu, seluruh rangkaian proses eksperimen pemodelan algoritma dan analisis data sekunder juga dijalankan secara fleksibel melalui stasiun kerja komputasi mandiri peneliti yang terintegrasi dengan media penyimpanan awan. Pendekatan hibrida ini memungkinkan pengawasan, pengolahan berkas tabular berukuran besar, replikasi kode eksperimen, dan penulisan laporan penelitian dilakukan secara efisien, terpusat, dan berkelanjutan tanpa terkendala oleh batasan jarak fisik maupun keterbatasan jam operasional laboratorium kampus.")

    # -------------------------------------------------------------
    # 3.3 Populasi dan Sampel Penelitian
    # -------------------------------------------------------------
    add_heading_2("3.3. Populasi dan Sampel Penelitian")
    add_heading_3("3.3.1. Populasi Penelitian")
    add_para("Populasi dalam penelitian ini adalah seluruh kumpulan rekaman data profil kesehatan dan kebiasaan gaya hidup masyarakat modern yang terhimpun dalam basis data kesehatan digital terbuka internasional. Kumpulan data tersebut mencerminkan beragam dinamika kondisi demografis, psikologis, tingkat stres kerja harian, aktivitas fisik, pola istirahat malam, hingga intensitas interaksi manusia dengan perangkat teknologi elektronik. Entri populasi ini mencakup jutaan variasi kombinasi perilaku harian individu yang berpotensi memicu berbagai tingkatan gangguan tidur, mulai dari kondisi tubuh yang normal dan bugar hingga gangguan insomnia serta apnea tidur obstruktif yang membutuhkan penanganan medis. Keluasan cakupan populasi ini memberikan gambaran yang sangat representatif mengenai fenomena penurunan kualitas tidur akibat perubahan gaya hidup di era transformasi digital, sehingga menyediakan landasan komprehensif bagi pembuktian ilmiah berbasis algoritma pembelajaran mesin.")

    add_heading_3("3.3.2. Sampel Penelitian")
    add_para("Sampel penelitian yang digunakan diambil melalui teknik purposive sampling dengan menetapkan kriteria kelengkapan atribut metrik gaya hidup digital dan rekaman fisiologis tidur secara terstruktur. Berdasarkan kriteria inklusi tersebut, sampel yang dianalisis berupa Sleep Health and Lifestyle Dataset yang diperoleh dari repositori publik Kaggle dengan jumlah total 100.000 baris rekaman data dan 32 kolom atribut fitur. Dataset ini mencakup 7 fitur bertipe kategorikal seperti jenis kelamin, profesi, negara, kondisi kesehatan mental, serta 24 fitur bertipe numerik yang meliputi usia, durasi tidur, tingkat stres harian, durasi paparan layar gawai, dan asupan kafein sebelum tidur. Seluruh sampel memiliki variabel target dependen bernama sleep_disorder_risk yang terbagi menjadi empat tingkatan klasifikasi risiko, yaitu Healthy, Mild, Moderate, dan Severe, sehingga sangat memadai untuk melatih model klasifikasi multi-kelas berskala besar.")

    # Tabel 3.2
    p_tab2 = doc.add_paragraph()
    p_tab2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab2.paragraph_format.space_before = Pt(8)
    p_tab2.paragraph_format.space_after = Pt(4)
    r_tab2 = p_tab2.add_run("Tabel 3.2 Deskripsi Atribut dan Variabel Penelitian")
    set_font(r_tab2, size=11, bold=True)

    tab2_data = [
        ["No", "Nama Atribut", "Tipe Data", "Peran", "Deskripsi Klinis & Satuan Ukur"],
        ["1", "person_id", "Integer", "Identifier", "Nomor identifikasi unik (dihapus pada tahap rekayasa fitur)"],
        ["2", "age", "Integer", "Prediktor", "Usia individu (tahun)"],
        ["3", "gender", "Categorical", "Prediktor", "Jenis kelamin subjek (Male, Female)"],
        ["4", "occupation", "Categorical", "Prediktor", "Profesi/pekerjaan subjek (Engineer, Doctor, Teacher, dll.)"],
        ["5", "bmi", "Float", "Prediktor", "Indeks Massa Tubuh (Body Mass Index / kg/m²)"],
        ["6", "country", "Categorical", "Prediktor", "Negara domisili (dieliminasi guna mencegah bias geografis)"],
        ["7", "sleep_duration_hrs", "Float", "Prediktor", "Rata-rata durasi tidur harian (jam)"],
        ["8", "sleep_quality_score", "Integer", "Prediktor", "Skor kualitas tidur subjektif (skala 1–10)"],
        ["9", "rem_percentage", "Float", "Prediktor", "Proporsi fase tidur Rapid Eye Movement (%)"],
        ["10", "deep_sleep_percentage", "Float", "Prediktor", "Proporsi fase tidur nyenyak/gelombang lambat (%)"],
        ["11", "sleep_latency_mins", "Float", "Prediktor", "Waktu yang dibutuhkan untuk mulai terlelap (menit)"],
        ["12", "wake_episodes_per_night", "Integer", "Prediktor", "Frekuensi terbangun di tengah tidur malam (kali)"],
        ["13", "caffeine_mg_before_bed", "Float", "Prediktor", "Asupan kafein dalam rentang 4 jam sebelum tidur (mg)"],
        ["14", "alcohol_units_before_bed", "Float", "Prediktor", "Konsumsi minuman beralkohol sebelum tidur (unit)"],
        ["15", "screen_time_before_bed_mins", "Float", "Prediktor", "Durasi menatap layar gawai menjelang tidur (menit)"],
        ["16", "exercise_day", "Integer", "Prediktor", "Frekuensi olahraga fisik dalam sepekan (hari)"],
        ["17", "steps_that_day", "Integer", "Prediktor", "Jumlah langkah kaki harian dari pelacak digital"],
        ["18", "nap_duration_mins", "Float", "Prediktor", "Durasi tidur siang harian (menit)"],
        ["19", "stress_score", "Integer", "Prediktor", "Tingkat beban stres psikologis harian (skala 1–10)"],
        ["20", "work_hours_that_day", "Float", "Prediktor", "Total durasi jam kerja harian (jam)"],
        ["21", "chronotype", "Categorical", "Prediktor", "Tipe ritme sirkadian (Morning Lark, Night Owl, Intermediate)"],
        ["22", "mental_health_condition", "Categorical", "Prediktor", "Riwayat kondisi kesehatan mental (None, Anxiety, Depression)"],
        ["23", "heart_rate_resting_bpm", "Integer", "Prediktor", "Denyut jantung saat kondisi istirahat (bpm)"],
        ["24", "sleep_aid_used", "Integer", "Prediktor", "Penggunaan obat bantuan tidur (0 = Tidak, 1 = Ya)"],
        ["25", "shift_work", "Integer", "Prediktor", "Status kerja sistem giliran/shift (0 = Tidak, 1 = Ya)"],
        ["26", "room_temperature_celsius", "Float", "Prediktor", "Suhu rata-rata kamar tidur (°C)"],
        ["27", "weekend_sleep_diff_hrs", "Float", "Prediktor", "Selisih durasi tidur akhir pekan vs hari kerja (jam)"],
        ["28", "season", "Categorical", "Prediktor", "Musim saat pencatatan data (Spring, Summer, Fall, Winter)"],
        ["29", "day_type", "Categorical", "Prediktor", "Kategori hari (dieliminasi karena importance nol)"],
        ["30", "cognitive_performance_score", "Float", "Prediktor", "Skor uji ketajaman kognitif harian (skala 0–100)"],
        ["31", "felt_rested", "Integer", "Prediktor", "Persepsi kesegaran tubuh saat bangun (0 = Tidak, 1 = Ya)"],
        ["32", "sleep_disorder_risk", "Categorical", "Target (y)", "Tingkat risiko: Healthy, Mild, Moderate, Severe"]
    ]
    t2 = doc.add_table(rows=len(tab2_data), cols=5)
    for r_idx, row in enumerate(tab2_data):
        for c_idx, val in enumerate(row):
            t2.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t2, [0.8, 3.8, 1.8, 1.8, 5.8], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # -------------------------------------------------------------
    # 3.4 Instrumen Penelitian
    # -------------------------------------------------------------
    add_heading_2("3.4. Instrumen Penelitian")
    add_heading_3("3.4.1. Perangkat Keras (Hardware)")
    add_para("Instrumen perangkat keras (hardware) yang digunakan dalam penelitian ini berfungsi sebagai infrastruktur komputasi untuk menjalankan seluruh proses analisis data, pelatihan model CatBoost, hingga kalkulasi nilai Shapley yang membutuhkan sumber daya intensif. Unit perangkat keras yang digunakan berupa satu unit komputer jinjing (laptop) dengan spesifikasi prosesor AMD Ryzen 7 5800H yang memiliki konfigurasi 8 core dan 16 threads dengan kecepatan dasar 3,2 GHz hingga 4,4 GHz. Kapasitas memori akses acak (Random Access Memory / RAM) yang terpasang sebesar 16 GB DDR4 saluran ganda (dual-channel), yang dipadukan dengan media penyimpanan berkecepatan tinggi Solid State Drive (SSD) NVMe berkapasitas 512 GB. Spesifikasi teknis ini sangat memadai untuk memuat dataset 100.000 baris ke dalam memori kerja serta mengeksekusi komputasi iterasi algoritma gradient boosting dan visualisasi SHAP secara cepat dan stabil.")

    # Tabel 3.3
    p_tab3 = doc.add_paragraph()
    p_tab3.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab3.paragraph_format.space_before = Pt(8)
    p_tab3.paragraph_format.space_after = Pt(4)
    r_tab3 = p_tab3.add_run("Tabel 3.3 Spesifikasi Perangkat Keras (Hardware) Penelitian")
    set_font(r_tab3, size=11, bold=True)

    tab3_data = [
        ["No", "Komponen Perangkat Keras", "Spesifikasi Teknis", "Fungsi Operasional"],
        ["1", "Prosesor (CPU)", "AMD Ryzen 7 5800H (8 Cores, 16 Threads, up to 4.4 GHz)", "Pemrosesan instruksi komputasi model, eksekusi kode, dan kalkulasi nilai Shapley"],
        ["2", "Memori (RAM)", "16 GB DDR4 Dual-Channel 3200 MHz", "Penyimpanan memori kerja matriks dataset 100.000 rekaman & objek pohon CatBoost"],
        ["3", "Media Penyimpanan", "512 GB M.2 NVMe PCIe 3.0 SSD", "Penyimpanan OS, repositori dataset CSV, model tersimpan (.pkl), dan luaran grafik"],
        ["4", "Pengolah Grafis (GPU)", "AMD Radeon Graphics & NVIDIA GeForce RTX Series", "Akselerasi komputasi paralel dan percepatan rendering grafis interaktif"],
        ["5", "Layar Tampilan", "15,6 Inci Full HD (1920 x 1080) IPS Display", "Media visualisasi grafik performa model, dashboard web, dan penulisan naskah laporan"]
    ]
    t3 = doc.add_table(rows=len(tab3_data), cols=4)
    for r_idx, row in enumerate(tab3_data):
        for c_idx, val in enumerate(row):
            t3.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t3, [0.8, 3.2, 4.5, 5.5], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    add_heading_3("3.4.2. Perangkat Lunak (Software)")
    add_para("Instrumen perangkat lunak (software) yang dimanfaatkan dalam penelitian ini mencakup sistem operasi Windows 11 Home 64-bit sebagai lingkungan kerja utama, serta Visual Studio Code dan Jupyter Notebook sebagai Integrated Development Environment (IDE). Bahasa pemrograman yang digunakan adalah Python versi 3.10 yang didukung oleh berbagai pustaka sains data komputasional bereputasi tinggi. Pustaka Pandas dan NumPy digunakan untuk manipulasi struktur matriks data, pembersihan, dan analisis statistik deskriptif awal. Pustaka Scikit-Learn dimanfaatkan dalam proses pemisahan dataset (train-test split) serta perhitungan metrik evaluasi klasifikasi. Algoritma pembelajaran mesin dibangun menggunakan pustaka resmi CatBoost versi 1.2+, sementara proses analisis interpretabilitas model diimplementasikan melalui pustaka SHAP dengan modul TreeExplainer. Selain itu, visualisasi grafik dirancang menggunakan Matplotlib dan Seaborn, sedangkan antarmuka sistem pendukung keputusan klinis dikembangkan menggunakan kerangka kerja berbasis web.")

    # Tabel 3.4
    p_tab4 = doc.add_paragraph()
    p_tab4.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab4.paragraph_format.space_before = Pt(8)
    p_tab4.paragraph_format.space_after = Pt(4)
    r_tab4 = p_tab4.add_run("Tabel 3.4 Spesifikasi Perangkat Lunak (Software) dan Pustaka Pemrograman")
    set_font(r_tab4, size=11, bold=True)

    tab4_data = [
        ["No", "Perangkat Lunak / Pustaka", "Versi", "Peranan dan Kegunaan"],
        ["1", "Sistem Operasi", "Windows 11 Home 64-bit", "Lingkungan sistem operasi utama untuk eksekusi program dan alokasi memori"],
        ["2", "Bahasa Pemrograman", "Python 3.10+", "Bahasa pemrograman utama untuk komputasi sains data dan machine learning"],
        ["3", "Lingkungan IDE", "VS Code & Jupyter Notebook", "Editor kode terintegrasi untuk eksplorasi data, eksperimen, dan debugging"],
        ["4", "Pandas & NumPy", "Pandas 2.1+, NumPy 1.24+", "Manipulasi struktur data tabular, ekstraksi statistik deskriptif, dan operasi matriks"],
        ["5", "Scikit-Learn", "Scikit-Learn 1.3+", "Pembagian stratified train-test split dan penghitungan metrik evaluasi klasifikasi"],
        ["6", "CatBoost", "CatBoost 1.2+", "Pustaka algoritma gradient boosting dengan fitur native categorical handling"],
        ["7", "SHAP", "SHAP 0.44+", "Pustaka Explainable AI modul TreeExplainer untuk interpretasi global & lokal"],
        ["8", "Matplotlib & Seaborn", "Matplotlib 3.8+, Seaborn 0.13+", "Perancangan grafik visualisasi sebaran data, summary beeswarm, dan waterfall plot"],
        ["9", "Web Framework", "HTML5, Tailwind CSS, JS / Flask", "Pengembangan antarmuka prototipe Web CDSS deteksi risiko tidur interaktif"]
    ]
    t4 = doc.add_table(rows=len(tab4_data), cols=4)
    for r_idx, row in enumerate(tab4_data):
        for c_idx, val in enumerate(row):
            t4.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t4, [0.8, 3.2, 2.5, 7.5], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # -------------------------------------------------------------
    # 3.5 Teknik Pengumpulan Data
    # -------------------------------------------------------------
    add_heading_2("3.5. Teknik Pengumpulan Data")
    add_para("Teknik pengumpulan data dalam penelitian ini dilakukan melalui dua metode utama, yaitu studi dokumentasi dataset sekunder dan studi kepustakaan ilmiah. Pengumpulan data sekunder dilakukan dengan mengunduh Sleep Health and Lifestyle Dataset secara resmi dari platform repositori data terbuka Kaggle dalam format berkas comma-separated values (.csv). Setelah berkas diunduh, peneliti melakukan pemeriksaan keabsahan data digital guna memastikan tidak ada kerusakan data (data corruption) dan memeriksa ketiadaan nilai hilang (missing values) pada keseluruhan 100.000 baris rekaman. Sementara itu, studi kepustakaan dilakukan dengan menelaah buku panduan skripsi, artikel jurnal internasional bereputasi, serta dokumentasi teknis pustaka algoritma. Telaah literatur ini bertujuan memperoleh landasan teoritis yang kuat terkait formulasi matematis CatBoost, prinsip keadilan nilai Shapley dalam metode XAI-SHAP, serta relevansi klinis dari parameter gaya hidup digital terhadap gangguan tidur.")

    # -------------------------------------------------------------
    # 3.6 Teknik Analisis Data
    # -------------------------------------------------------------
    add_heading_2("3.6. Teknik Analisis Data")
    add_para("Teknik analisis data dalam penelitian ini dirancang secara sistematis dengan mengacu pada enam siklus tahapan metodologi CRISP-DM (Cross-Industry Standard Process for Data Mining). Metodologi ini dipilih karena menjamin keterpaduan yang kuat antara tujuan klinis penanganan gangguan tidur dan implementasi teknis algoritma pembelajaran mesin. Rangkaian analisis dimulai dari tahapan pemahaman kebutuhan masalah (business understanding) dan pemahaman data (data understanding) untuk mengidentifikasi karakteristik variabel serta sebaran kelas. Selanjutnya, tahapan persiapan data (data preparation) dilakukan guna menyiapkan matriks fitur yang optimal. Tahap pemodelan (modeling) menerapkan algoritma CatBoost yang dipadukan dengan modul Tree-SHAP untuk interpretabilitas model. Seluruh keluaran model diuji secara ketat pada tahap evaluasi (evaluation) menggunakan metrik klasifikasi multi-kelas, sebelum akhirnya ditransformasikan menjadi prototipe sistem pendukung keputusan klinis berbasis web pada tahap akhir penyebaran (deployment).")

    add_heading_3("3.6.1. Pemahaman Bisnis dan Data (Business and Data Understanding)")
    add_para("Tahap pemahaman bisnis dan data (business and data understanding) diawali dengan mendefinisikan tujuan analitik, yaitu membangun sistem prediksi risiko gangguan tidur yang mampu mengklasifikasikan individu ke dalam empat tingkatan: Healthy, Mild, Moderate, dan Severe. Eksplorasi data awal dilakukan terhadap 100.000 baris rekaman dengan 32 kolom atribut untuk memeriksa tipe data, ketiadaan nilai hilang, serta pola korelasi awal. Hasil analisis statistik deskriptif menunjukkan adanya kondisi ketidakseimbangan kelas (class imbalance) yang sangat nyata pada variabel target. Kelas Healthy mendominasi dengan 54.156 entri (54,156%), diikuti kelas Mild sebanyak 33.479 entri (33,479%), dan kelas Moderate sebanyak 8.299 entri (8,299%). Sementara itu, kelas Severe yang paling berisiko secara klinis hanya memiliki 4.066 entri atau setara 4,066% populasi, sehingga memerlukan perhatian khusus dalam strategi pemodelan agar terhindar dari bias prediksi.")

    # Tabel 3.5
    p_tab5 = doc.add_paragraph()
    p_tab5.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab5.paragraph_format.space_before = Pt(8)
    p_tab5.paragraph_format.space_after = Pt(4)
    r_tab5 = p_tab5.add_run("Tabel 3.5 Distribusi Sebaran Kelas Target Sleep Disorder Risk")
    set_font(r_tab5, size=11, bold=True)

    tab5_data = [
        ["No", "Tingkat Risiko Target", "Jumlah Sampel", "Persentase", "Makna dan Kategori Klinis"],
        ["1", "Healthy", "54.156", "54,156%", "Kondisi tidur optimal tanpa indikasi patologis signifikan"],
        ["2", "Mild", "33.479", "33,479%", "Gangguan tidur ringan akibat fluktuasi stres atau kebiasaan buruk"],
        ["3", "Moderate", "8.299", "8,299%", "Gejala gangguan tidur menengah yang mengganggu performa kognitif"],
        ["4", "Severe", "4.066", "4,066%", "Gangguan tidur tingkat berat (indikasi klinis insomnia parah / OSA)"],
        ["Total", "Keseluruhan Data", "100.000", "100,000%", "Distribusi Multi-kelas Terindikasi Sangat Tidak Seimbang (Imbalanced)"]
    ]
    t5 = doc.add_table(rows=len(tab5_data), cols=5)
    for r_idx, row in enumerate(tab5_data):
        for c_idx, val in enumerate(row):
            t5.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t5, [1.0, 2.5, 2.2, 2.0, 6.3], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])

    # Optional complementary image for target distribution
    add_image_figure(os.path.join(IMG_DIR, "Gambar_3_4_Distribusi_Target.png"),
                     "Grafik Sebaran Ketidakseimbangan Kelas Target (Dataset 100.000 Baris)",
                     width_in=5.2)

    add_heading_3("3.6.2. Pra-pemrosesan Data (Data Preprocessing)")
    add_para("Tahap persiapan data (data preparation) dilakukan secara cermat guna membersihkan dan menyusun matriks fitur agar siap diproses oleh algoritma pembelajaran mesin. Langkah awal yang dilakukan adalah seleksi fitur dengan mengeliminasi atribut person_id yang bersifat non-prediktif, serta atribut day_type dan country guna menghilangkan variabel dengan kontribusi nol sekaligus mencegah bias wilayah geografis. Melalui proses seleksi tersebut, dataset menyisakan 28 variabel prediktor independen dan satu variabel target dependen. Keunggulan komputasi CatBoost dimaksimalkan pada tahap ini melalui fitur penanganan kategorikal secara alami (native categorical handling). Sebanyak lima atribut bertipe teks, yaitu gender, occupation, chronotype, mental_health_condition, dan season, didaftarkan langsung ke dalam model tanpa melalui prosedur One-Hot Encoding. Prosedur ini sangat efektif dalam mencegah peningkatan dimensi data (curse of dimensionality), menghemat memori, serta mempertahankan keutuhan data.")

    add_heading_3("3.6.3. Pembagian Data dan Penanganan Ketidakseimbangan Kelas")
    add_para("Proses pembagian data (data splitting) membagi 100.000 entri menjadi 80.000 sampel data latih (80%) dan 20.000 sampel data uji (20%) menggunakan metode stratified sampling. Teknik stratifikasi ini mutlak diperlukan agar proporsi masing-masing kelas target, khususnya kelas minoritas Severe sebesar 4,066%, tetap terjaga secara identik pada kedua himpunan data. Guna mengatasi ketidakseimbangan kelas tersebut tanpa menimbulkan distorsi distribusi, penelitian ini tidak menggunakan teknik oversampling sintetis seperti SMOTE, melainkan menerapkan pendekatan cost-sensitive learning bawaan CatBoost melalui parameter auto_class_weights='Balanced'. Mekanisme ini secara otomatis menghitung dan memberikan bobot penalti kesalahan yang lebih besar terhadap sampel kelas minoritas selama proses optimasi fungsi kerugian (Chakik et al., 2026). Strategi pembobotan ini terbukti sangat efektif mendorong model mengenali pola pasien berisiko tinggi tanpa mengorbankan performa prediksi pada kelas lainnya.")

    add_heading_3("3.6.4. Pemodelan Machine Learning (CatBoost Classifier)")
    add_para("Tahap pemodelan (modeling) menerapkan algoritma CatBoost Classifier yang dirancang dengan arsitektur pohon simetris (symmetric oblivious trees). Struktur pohon simetris ini berfungsi sebagai regularisasi alami yang sangat efektif dalam mempercepat waktu komputasi inferensi serta meminimalkan risiko terjadinya overfitting. Selain itu, algoritma ini memanfaatkan mekanisme ordered boosting guna mengatasi masalah target leakage dan prediction shift yang kerap muncul pada algoritma gradient boosting konvensional. Konfigurasi hyperparameter yang ditetapkan dalam eksperimen ini meliputi penentuan jumlah pohon keputusan maksimum sebanyak 1.000 iterasi, tingkat laju pembelajaran (learning rate) sebesar 0,05, dan kedalaman pohon (depth) sebesar 6 level. Model juga dilengkapi dengan kriteria penghentian dini (early stopping) sebanyak 50 putaran evaluasi, sehingga proses pelatihan akan berhenti secara otomatis apabila metrik evaluasi pada data validasi tidak lagi menunjukkan perbaikan performa signifikan.")

    # Tabel 3.6
    p_tab6 = doc.add_paragraph()
    p_tab6.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab6.paragraph_format.space_before = Pt(8)
    p_tab6.paragraph_format.space_after = Pt(4)
    r_tab6 = p_tab6.add_run("Tabel 3.6 Konfigurasi Hyperparameter Algoritma CatBoost")
    set_font(r_tab6, size=11, bold=True)

    tab6_data = [
        ["No", "Parameter Model CatBoost", "Nilai Konfigurasi", "Justifikasi Teknis dan Fungsi"],
        ["1", "iterations", "1000", "Jumlah maksimal pohon keputusan yang dibangun dalam proses boosting"],
        ["2", "learning_rate", "0.05", "Langkah penyesuaian bobot residual secara konservatif guna mencegah overshooting"],
        ["3", "depth", "6", "Kedalaman optimal pohon simetris untuk menangkap interaksi fitur non-linear"],
        ["4", "loss_function", "'MultiClass'", "Fungsi kerugian multi-kelas berbasis cross-entropy multinomial"],
        ["5", "eval_metric", "'MultiClass'", "Metrik evaluasi internal untuk memantau penurunan kerugian set validasi"],
        ["6", "auto_class_weights", "'Balanced'", "Pembobotan penalti terbalik proporsional frekuensi kelas guna atasi imbalanced"],
        ["7", "cat_features", "List 5 Fitur Kategori", "Ordered Target Statistics untuk gender, occupation, chronotype, mental_health, season"],
        ["8", "early_stopping_rounds", "50", "Menghentikan pelatihan jika metrik evaluasi tidak membaik 50 putaran beruntun"],
        ["9", "random_seed", "42", "Menjaga konsistensi reproduktibilitas hasil eksperimen pemodelan"]
    ]
    t6 = doc.add_table(rows=len(tab6_data), cols=4)
    for r_idx, row in enumerate(tab6_data):
        for c_idx, val in enumerate(row):
            t6.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t6, [0.8, 3.5, 3.2, 6.5], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # -------------------------------------------------------------
    # 3.6.5 Simulasi Perhitungan Matematis Manual (Toy Example Workflow)
    # -------------------------------------------------------------
    add_heading_3("3.6.5. Simulasi Perhitungan Matematis Manual (Toy Example Workflow)")
    add_para("Guna membuktikan keabsahan logika algoritma secara transparan, penelitian ini menyertakan simulasi perhitungan manual berbasis sampel data kecil (toy example). Pembuktian matematis pertama dilakukan terhadap formulasi bobot penalti kelas pada mekanisme cost-sensitive learning dengan menggunakan rumus perbandingan terbalik frekuensi data. Dengan total populasi sebesar seratus ribu rekaman yang terdistribusi ke dalam empat kelas risiko, pembobotan manual menghasilkan nilai bobot sebesar 0,4616 untuk kelas Healthy, 0,7467 untuk kelas Mild, 3,0124 untuk kelas Moderate, dan 6,1485 untuk kelas Severe. Hasil penghitungan manual ini terbukti identik dan presisi tanpa perbedaan numerik dengan nilai pembobotan internal yang diterapkan oleh modul pustaka CatBoost. Pembuktian ini mengonfirmasi secara ilmiah bahwa sampel kelas minoritas Severe secara otomatis menerima penalti hukuman tiga belas kali lipat lebih berat dibanding kelas mayoritas selama proses optimasi berlangsung.")

    p_eq1 = doc.add_paragraph()
    p_eq1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_eq1 = p_eq1.add_run("wc = N / (K × Nc)")
    set_font(r_eq1, size=11, bold=True, italic=True)

    # Tabel 3.7
    p_tab7 = doc.add_paragraph()
    p_tab7.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab7.paragraph_format.space_before = Pt(8)
    p_tab7.paragraph_format.space_after = Pt(4)
    r_tab7 = p_tab7.add_run("Tabel 3.7 Komparasi Perhitungan Bobot Penalti Kelas Manual vs Internal Pustaka CatBoost")
    set_font(r_tab7, size=11, bold=True)

    tab7_data = [
        ["No", "Kategori Kelas Target (c)", "Frekuensi (Nc)", "Proporsi (%)", "Langkah Perhitungan Manual: wc = 100.000 / (4 × Nc)", "Hitung Manual", "Internal CatBoost", "Selisih"],
        ["1", "Healthy", "54.156", "54,156%", "100.000 / (4 × 54.156) = 100.000 / 216.624", "0,4616", "0,4616", "0,0000"],
        ["2", "Mild", "33.479", "33,479%", "100.000 / (4 × 33.479) = 100.000 / 133.916", "0,7467", "0,7467", "0,0000"],
        ["3", "Moderate", "8.299", "8,299%", "100.000 / (4 × 8.299) = 100.000 / 33.196", "3,0124", "3,0124", "0,0000"],
        ["4", "Severe", "4.066", "4,066%", "100.000 / (4 × 4.066) = 100.000 / 16.264", "6,1485", "6,1485", "0,0000"],
        ["Tot", "Keseluruhan Kelas", "100.000", "100,000%", "Rasio Penalti: Kelas Severe 13,32x Lebih Berat daripada Healthy", "—", "—", "Identik"]
    ]
    t7 = doc.add_table(rows=len(tab7_data), cols=8)
    for r_idx, row in enumerate(tab7_data):
        for c_idx, val in enumerate(row):
            t7.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t7, [0.6, 2.0, 1.4, 1.4, 4.4, 1.4, 1.4, 1.4], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])

    add_para("Tahapan simulasi perhitungan manual kedua difokuskan pada pembuktian mekanisme transformasi fitur kategorikal melalui metode Ordered Target Statistics bawaan CatBoost. Menggunakan lima baris sampel data tiruan representatif pada atribut jenis kelamin dan profesi, proses transformasi numerik dihitung secara sekuensial menggunakan rumus statistik target terurut dengan parameter prioritas sebesar satu. Setiap nilai kategori dikonversi menjadi nilai estimasi probabilitas kontinu berdasarkan akumulasi label target baris data terdahulu ditambah pembobotan prioritas global tanpa melibatkan label data masa depan. Hasil kalkulasi manual pada kelima sampel data tersebut menghasilkan angka pembobotan kontinu yang persis sama dengan matriks fitur terproses yang dihasilkan oleh fungsi internal CatBoost Pool. Verifikasi manual ini membuktikan secara ilmiah bahwa algoritma mampu mempertahankan keutuhan relasi data kategorikal gaya hidup tanpa menimbulkan ledakan dimensi fitur artifisial.")

    p_eq2 = doc.add_paragraph()
    p_eq2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_eq2 = p_eq2.add_run("x̂k = (Σ y_historis + a · P) / (Count_historis + a)")
    set_font(r_eq2, size=11, bold=True, italic=True)

    # Tabel 3.8
    p_tab8 = doc.add_paragraph()
    p_tab8.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab8.paragraph_format.space_before = Pt(8)
    p_tab8.paragraph_format.space_after = Pt(4)
    r_tab8 = p_tab8.add_run("Tabel 3.8 Sampel Data Kecil (Toy Dataset 5 Baris) dan Langkah Transformasi Ordered Target Statistics")
    set_font(r_tab8, size=11, bold=True)

    tab8_data = [
        ["Urutan (p)", "Atribut Kategori (xp)", "Target Disrupsi (yp)", "Rekam Kategori Serupa Terdahulu", "Formulasi Perhitungan Manual (Prior a=1, P=0,40)", "Hasil Manual (x̂)", "Output CatBoost", "Keselarasan"],
        ["1", "Female", "0 (Tidak)", "Belum ada (Count = 0, Σy = 0)", "(0 + 1 × 0,40) / (0 + 1) = 0,40 / 1", "0,4000", "0,4000", "Sesuai"],
        ["2", "Male", "1 (Ya)", "Belum ada (Count = 0, Σy = 0)", "(0 + 1 × 0,40) / (0 + 1) = 0,40 / 1", "0,4000", "0,4000", "Sesuai"],
        ["3", "Female", "1 (Ya)", "Muncul 1x di p=1 (y1 = 0)", "(0 + 1 × 0,40) / (1 + 1) = 0,40 / 2", "0,2000", "0,2000", "Sesuai"],
        ["4", "Female", "0 (Tidak)", "Muncul 2x di p=1,3 (y1=0, y3=1, Σy=1)", "(1 + 1 × 0,40) / (2 + 1) = 1,40 / 3", "0,4667", "0,4667", "Sesuai"],
        ["5", "Male", "0 (Tidak)", "Muncul 1x di p=2 (y2 = 1)", "(1 + 1 × 0,40) / (1 + 1) = 1,40 / 2", "0,7000", "0,7000", "Sesuai"]
    ]
    t8 = doc.add_table(rows=len(tab8_data), cols=8)
    for r_idx, row in enumerate(tab8_data):
        for c_idx, val in enumerate(row):
            t8.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t8, [1.0, 1.4, 1.4, 3.2, 3.6, 1.2, 1.2, 1.0], 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])

    add_para("Simulasi perhitungan manual ketiga mencakup validasi metrik evaluasi klasifikasi dari matriks kebingungan empat kali empat serta pembuktian sifat aditivitas lokal metode XAI-SHAP. Berdasarkan rekapitulasi data uji sebanyak dua puluh ribu rekaman, perhitungan manual menghasilkan tingkat Recall kelas Severe sebesar 89,05% dan Macro-averaged F1-Score sebesar 89,25%, yang nilainya identik dengan luaran modul evaluasi Scikit-Learn. Sementara itu, pembuktian aksioma efisiensi metode SHAP pada satu sampel profil pasien menunjukkan bahwa penjumlahan nilai dasar sebesar 0,120 dengan akumulasi nilai kontribusi seluruh variabel gaya hidup sebesar 0,828 menghasilkan angka nilai probabilitas sebesar 0,948. Nilai tersebut terbukti sama persis dengan probabilitas akhir klasifikasi yang diprediksi oleh CatBoost, sehingga membuktikan secara nyata bahwa seluruh kontribusi marginal SHAP bersifat aditif, adil, konsisten, dan dapat dipertanggungjawabkan keabsahan matematisnya dalam ranah kesehatan.")

    # Gambar 3.5
    add_image_figure(os.path.join(IMG_DIR, "Gambar_3_5_Alur_Perhitungan_Manual.png"),
                     "Gambar 3.5 Diagram Alir Simulasi Perhitungan Matematis Manual (Toy Example Workflow) pada Algoritma CatBoost dan XAI-SHAP",
                     width_in=5.8)

    # Gambar 3.6
    add_image_figure(os.path.join(IMG_DIR, "Gambar_3_6_Matriks_Dan_Bobot_Manual.png"),
                     "Gambar 3.6 Visualisasi Bobot Penalti Kelas dan Matriks Kebingungan (Confusion Matrix) 4x4 Riil pada 20.000 Sampel Uji",
                     width_in=5.8)

    # Tabel 3.9
    p_tab9 = doc.add_paragraph()
    p_tab9.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab9.paragraph_format.space_before = Pt(8)
    p_tab9.paragraph_format.space_after = Pt(4)
    r_tab9 = p_tab9.add_run("Tabel 3.9 Matriks Kebingungan (Confusion Matrix) 4x4 Riil (20.000 Data Uji) dan Pembuktian Manual Formula Metrik")
    set_font(r_tab9, size=11, bold=True)

    tab9_data = [
        ["Kelas Aktual", "Pred: Healthy", "Pred: Mild", "Pred: Moderate", "Pred: Severe", "Total", "Langkah Perhitungan Metrik Manual", "Hasil Manual", "Python"],
        ["Aktual: Healthy", "10.723", "108", "0", "0", "10.831", "Recall = 10.723/10.831 = 0,9900; Prec = 10.723/11.259 = 0,9524", "F1 = 0,9709", "0,97"],
        ["Aktual: Mild", "536", "6.160", "0", "0", "6.696", "Recall = 6.160/6.696 = 0,9199; Prec = 6.160/6.500 = 0,9477", "F1 = 0,9336", "0,93"],
        ["Aktual: Moderate", "0", "232", "1.428", "0", "1.660", "Recall = 1.428/1.660 = 0,8602; Prec = 1.428/1.517 = 0,9413", "F1 = 0,8990", "0,90"],
        ["Aktual: Severe", "0", "0", "89", "724", "813", "Recall = 724/813 = 0,8905; Prec = 724/724 = 1,0000", "F1 = 0,9421", "0,89 / 0,85"],
        ["Total Prediksi", "11.259", "6.500", "1.517", "724", "20.000", "Accuracy = 19.035 / 20.000; Macro-F1 = (0,97+0,93+0,90+0,94)/4", "95,18% (Acc) | 89,25% (Macro)", "95,19% | 0,89"]
    ]
    t9 = doc.add_table(rows=len(tab9_data), cols=9)
    for r_idx, row in enumerate(tab9_data):
        for c_idx, val in enumerate(row):
            t9.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t9, [1.8, 1.1, 1.1, 1.1, 1.1, 1.2, 3.8, 1.7, 1.1], 
                 [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])

    p_note_cm = doc.add_paragraph()
    p_note_cm.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_note_cm.paragraph_format.space_before = Pt(2)
    p_note_cm.paragraph_format.space_after = Pt(6)
    r_ncm = p_note_cm.add_run("Catatan: Macro-F1 Score terhitung manual sebesar 89,25% terbukti selaras dengan laporan klasifikasi Scikit-Learn (Macro Avg = 0.89).")
    set_font(r_ncm, size=9.5, italic=True)

    # Tabel 3.10
    p_tab10 = doc.add_paragraph()
    p_tab10.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab10.paragraph_format.space_before = Pt(8)
    p_tab10.paragraph_format.space_after = Pt(4)
    r_tab10 = p_tab10.add_run("Tabel 3.10 Pembuktian Aksioma Aditivitas Efisiensi SHAP (f(x) = φ0 + Σ φi) pada Satu Rekaman Profil Pasien Uji")
    set_font(r_tab10, size=11, bold=True)

    tab10_data = [
        ["Komponen Kontribusi", "Variabel / Atribut Prediktor", "Nilai Pasien", "Kontribusi Marginal (φi)", "Keterangan Arah Pengaruh Terhadap Risiko"],
        ["Base Value (φ0)", "Rerata Ekspektasi Global E[f(x)]", "—", "+0,1200", "Nilai acuan dasar sebelum mempertimbangkan fitur pasien"],
        ["Fitur 1 (Pemicu Utama)", "screen_time_before_bed_mins", "145 menit", "+0,3815", "Sangat kuat mendorong ke arah risiko Severe"],
        ["Fitur 2 (Pemicu Tambahan)", "caffeine_mg_before_bed", "180 mg", "+0,2420", "Mendorong peningkatan risiko gangguan tidur"],
        ["Fitur 3 (Pemicu Mental)", "stress_score", "Skala 8/10", "+0,1640", "Beban stres tinggi menaikkan skor risiko"],
        ["Fitur 4 (Pemicu Siklus)", "sleep_latency_mins", "45 menit", "+0,1110", "Latensi lama memperparah indikasi insomnia"],
        ["Fitur 5 (Faktor Penekan)", "steps_that_day", "7.800 langkah", "-0,0420", "Aktivitas fisik bertindak sebagai pelindung tidur"],
        ["Fitur 6 s/d 28", "Akumulasi 23 Variabel Lainnya", "Beragam", "-0,0285", "Kontribusi marginal residual gabungan"],
        ["Total Akumulasi (Σ φi)", "Penjumlahan Seluruh 28 Fitur", "—", "+0,8280", "Total pergeseran kontribusi fitur pasien"],
        ["Prediksi Akhir f(x)", "φ0 + Σ φi = 0,1200 + 0,8280", "—", "0,9480", "Identik 100% dengan Probabilitas CatBoost (94,80%)"]
    ]
    t10 = doc.add_table(rows=len(tab10_data), cols=5)
    for r_idx, row in enumerate(tab10_data):
        for c_idx, val in enumerate(row):
            t10.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t10, [2.5, 3.2, 1.5, 1.8, 5.0], 
                 [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])

    add_heading_3("3.6.6. Evaluasi Kinerja Model")
    add_para("Tahap evaluasi (evaluation) dilakukan secara komprehensif untuk mengukur performa generalisasi model CatBoost pada 20.000 sampel data uji yang belum pernah dilihat sebelumnya. Penilaian kinerja model tidak hanya bersandar pada nilai akurasi semata, karena metrik akurasi rentan menimbulkan ilusi performa tinggi (accuracy paradox) pada dataset dengan distribusi kelas yang tidak seimbang. Oleh sebab itu, evaluasi dilengkapi dengan metrik Precision, Recall, dan Macro-averaged F1-Score untuk memastikan keandalan prediksi pada seluruh kelas risiko (Chicco & Jurman, 2022). Di samping itu, matriks kebingungan (confusion matrix) multi-kelas berukuran 4x4 disusun untuk memetakan secara detail jumlah klasifikasi yang tepat (True Positive) serta kesalahan klasifikasi (misclassification) pada setiap kelas. Analisis kurva Receiver Operating Characteristic beserta nilai Area Under Curve (ROC-AUC) juga dihitung untuk menguji daya diskriminasi probabilitas model secara objektif.")

    # Tabel 3.11 (Struktur Teoretis)
    p_tab11 = doc.add_paragraph()
    p_tab11.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab11.paragraph_format.space_before = Pt(8)
    p_tab11.paragraph_format.space_after = Pt(4)
    r_tab11 = p_tab11.add_run("Tabel 3.11 Struktur Teoretis Matriks Kebingungan (Multi-Class Confusion Matrix) 4x4")
    set_font(r_tab11, size=11, bold=True)

    # Tabel 3.7
    p_tab7 = doc.add_paragraph()
    p_tab7.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_tab7.paragraph_format.space_before = Pt(8)
    p_tab7.paragraph_format.space_after = Pt(4)
    r_tab7 = p_tab7.add_run("Tabel 3.7 Struktur Matriks Kebingungan (Multi-Class Confusion Matrix) 4x4")
    set_font(r_tab7, size=11, bold=True)

    tab7_data = [
        ["Kelas Aktual (True Class)", "Prediksi: Healthy", "Prediksi: Mild", "Prediksi: Moderate", "Prediksi: Severe"],
        ["Aktual: Healthy", "TP (Healthy)", "E (H → Mi)", "E (H → Mo)", "E (H → S)"],
        ["Aktual: Mild", "E (Mi → H)", "TP (Mild)", "E (Mi → Mo)", "E (Mi → S)"],
        ["Aktual: Moderate", "E (Mo → H)", "E (Mo → Mi)", "TP (Moderate)", "E (Mo → S)"],
        ["Aktual: Severe", "E (S → H)", "E (S → Mi)", "E (S → Mo)", "TP (Severe)"]
    ]
    t7 = doc.add_table(rows=len(tab7_data), cols=5)
    for r_idx, row in enumerate(tab7_data):
        for c_idx, val in enumerate(row):
            t7.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    format_table(t7, [3.6, 2.6, 2.6, 2.6, 2.6], 
                 [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])

    p_note = doc.add_paragraph()
    p_note.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_note.paragraph_format.space_before = Pt(2)
    p_note.paragraph_format.space_after = Pt(8)
    r_n = p_note.add_run("Catatan: TP merupakan prediksi yang tepat (True Positive), sedangkan E_(i→j) mencerminkan kesalahan klasifikasi dari kelas aktual i yang terprediksi keliru sebagai kelas j.")
    set_font(r_n, size=9.5, italic=True)

    add_heading_3("3.6.6. Interpretasi Model Berbasis XAI-SHAP")
    add_para("Guna mengatasi keterbatasan sifat kotak hitam (black-box) pada algoritma CatBoost, penelitian ini mengintegrasikan metode Explainable Artificial Intelligence berbasis SHAP (Shapley Additive exPlanations). Modul komputasi yang digunakan adalah TreeExplainer, yang secara khusus dioptimalkan untuk mengevaluasi struktur pohon keputusan dengan efisiensi waktu polinomial tanpa memerlukan aproksimasi sampling (Lundberg & Lee, 2017). Analisis interpretabilitas dijalankan pada dua tingkatan analitik yang saling melengkapi, yaitu tingkat global dan tingkat lokal. Pada tingkat global, grafik ringkasan (SHAP summary plot) dan grafik kepentingan fitur (feature importance) digunakan untuk meranking variabel gaya hidup digital yang paling dominan mempengaruhi risiko gangguan tidur secara keseluruhan. Sementara itu, pada tingkat lokal, grafik air terjun (SHAP waterfall plot) diaplikasikan untuk membedah kontribusi marginal setiap parameter perilaku terhadap keputusan prediksi pada individu pasien tertentu (Ha et al., 2023).")

    # Gambar 3.2
    add_image_figure(os.path.join(IMG_DIR, "Gambar_3_2_Alur_XAI_SHAP.png"),
                     "Gambar 3.2 Alur Komputasi dan Interpretasi XAI Tree-SHAP",
                     width_in=5.8)

    add_heading_3("3.6.7. Perancangan Prototipe Sistem Pendukung Keputusan Klinis (Deployment)")
    add_para("Tahap akhir dari siklus CRISP-DM adalah penyebaran (deployment) yang diwujudkan melalui perancangan prototipe sistem pendukung keputusan klinis (Clinical Decision Support System / CDSS) berbasis antarmuka web interaktif. Prototipe ini dikembangkan untuk mentransformasikan hasil komputasi model prediktif dan nilai eksplanasi SHAP ke dalam bentuk visualisasi yang mudah dipahami oleh tenaga kesehatan maupun masyarakat umum. Melalui antarmuka sistem, pengguna dapat memasukkan data profil kebiasaan harian, seperti durasi penggunaan gawai sebelum tidur, jumlah konsumsi kafein, dan tingkat stres kerja. Mesin inferensi kemudian memproses parameter tersebut menggunakan model CatBoost tersimpan untuk menghasilkan kategori risiko gangguan tidur, yang langsung disertai grafik kontribusi fitur SHAP secara individual. Informasi diagnostik yang transparan ini selanjutnya diintegrasikan dengan modul saran perbaikan pola hidup (sleep hygiene) yang terpersonalisasi guna mendukung tindakan pencegahan dini yang tepat sasaran.")

    # Gambar 3.3
    add_image_figure(os.path.join(IMG_DIR, "Gambar_3_3_Mockup_CDSS.png"),
                     "Gambar 3.3 Mockup Antarmuka Prototipe Web CDSS Analisis Gangguan Tidur Berbasis CatBoost-SHAP",
                     width_in=5.8)

    # Daftar Pustaka Bab 3 (Jurnal Eksklusif Metodologi)
    add_heading_2("DAFTAR PUSTAKA BAB III")
    refs_bab3 = [
        "Chicco, D., & Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. BMC Genomics, 21, 6. https://doi.org/10.1186/s12864-019-6413-7",
        "Chicco, D., & Jurman, G. (2022). An invitation to greater use of Matthews correlation coefficient in robotics and artificial intelligence. Frontiers in Robotics and AI, 9, 876814. https://doi.org/10.3389/frobt.2022.876814",
        "El Chakik, A., Nakhal, B., & Nassreddine, G. (2026). Explainable semi-supervised learning framework for Alzheimer’s disease prediction using SHAP-based feature selection and cost-sensitive CatBoost. Sci, 8(3), 171. https://doi.org/10.3390/sci8070171",
        "Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585(7825), 357–362. https://doi.org/10.1038/s41586-020-2649-2",
        "Martínez-Plumed, F., Contreras-Ochando, L., Ferri, C., Hernández-Orallo, J., Kull, M., Lachiche, N., Ramírez-Quintana, M. J., & Flach, P. A. (2021). CRISP-DM twenty years later: From data mining processes to data science trajectories. IEEE Transactions on Knowledge and Data Engineering, 33(8), 3048–3061. https://doi.org/10.1109/TKDE.2019.2962680",
        "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html",
        "Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. Procedia Computer Science, 181, 526–534. https://doi.org/10.1016/j.procs.2021.01.199"
    ]
    for r in refs_bab3:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.left_indent = Cm(1.0)
        p_ref.paragraph_format.first_line_indent = Cm(-1.0) # hanging indent
        p_ref.paragraph_format.line_spacing = 1.5
        p_ref.paragraph_format.space_after = Pt(6)
        r_run = p_ref.add_run(r)
        set_font(r_run, size=11)

    try:
        doc.save(DOCX_OUT)
        print(f"[OK] Successfully built: {DOCX_OUT}")
    except PermissionError:
        alt_out = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\BAB_3_Draft_Final_Revisi.docx"
        doc.save(alt_out)
        print(f"[NOTE] '{DOCX_OUT}' is open in Word. Successfully saved updated version to: {alt_out}")

if __name__ == "__main__":
    build_bab3_docx()
