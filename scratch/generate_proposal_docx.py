import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_proposal_docx():
    doc = docx.Document()

    # Set Margins (2.54 cm / 1 inch)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Style Helpers
    def set_font(run, name='Times New Roman', size=11, bold=False, italic=False, color=RGBColor(0,0,0)):
        run.font.name = name
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color

    def set_cell_shading(cell, color_hex):
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
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
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:left w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    # 1. HEADER
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_inst.add_run("OUTLINE PROPOSAL SKRIPSI\n")
    set_font(r1, size=13, bold=True)
    r2 = p_inst.add_run("PROGRAM STUDI TEKNIK INFORMATIKA - FAKULTAS SAINS DAN TEKNOLOGI\nUNIVERSITAS ISLAM NAHDLATUL ULAMA (UNISNU) JEPARA\n")
    set_font(r2, size=11, bold=True)

    # Identitas
    p_id = doc.add_paragraph()
    set_font(p_id.add_run("Nama Mahasiswa : "), bold=True)
    set_font(p_id.add_run("Ahmad Novian Dzulfanni\n"))
    set_font(p_id.add_run("NIM            : "), bold=True)
    set_font(p_id.add_run("231240001438\n"))
    set_font(p_id.add_run("Program Studi  : "), bold=True)
    set_font(p_id.add_run("S1 Teknik Informatika\n"))
    set_font(p_id.add_run("Bidang Minat   : "), bold=True)
    set_font(p_id.add_run("Sains Data, Pembelajaran Mesin (Machine Learning), dan Explainable AI (XAI)\n"))
    p_id.paragraph_format.space_after = Pt(12)

    # 2. TABEL OUTLINE UTAMA (FORMULIR RESMI UNISNU)
    p_tbl_title = doc.add_paragraph()
    set_font(p_tbl_title.add_run("TABEL OUTLINE FORMULIR PROPOSAL SKRIPSI"), size=11, bold=True)
    
    table_outline = doc.add_table(rows=5, cols=2)
    table_outline.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_outline)
    table_outline.columns[0].width = Inches(2.2)
    table_outline.columns[1].width = Inches(4.3)

    rows_data = [
        ("JUDUL PENELITIAN", 
         "Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Klasifikasi Faktor Risiko Gangguan Tidur Berbasis Metrik Gaya Hidup Digital"),
        
        ("RUMUSAN MASALAH", 
         "Bagaimana penerapan Shapley Additive exPlanations (SHAP) sebagai metode Explainable AI (XAI) pada algoritma CatBoost dapat menghasilkan model klasifikasi risiko gangguan tidur yang akurat dan transparan, sekaligus mampu mengidentifikasi faktor-faktor gaya hidup digital yang paling berpengaruh secara personal dan mudah dipahami?"),
        
        ("LATAR BELAKANG", [
            ("Paragraf 1: Urgensi Masalah Gangguan Tidur & Metrik Gaya Hidup Digital (121 kata)",
             "Gangguan tidur saat ini telah berkembang menjadi masalah kesehatan masyarakat yang serius di era modern. Kondisi ini tidak hanya menurunkan kebugaran tubuh sehari-hari, tetapi juga berhubungan erat dengan peningkatan risiko berbagai penyakit kronis seperti gangguan kardiovaskular, diabetes, hingga depresi. Pada era serba digital, sebagian besar pemicu gangguan tidur berkaitan langsung dengan pola kebiasaan harian yang dapat diukur secara kuantitatif. Faktor-faktor tersebut meliputi durasi paparan layar gawai sebelum tidur, beban kerja, konsumsi kafein, hingga minimnya aktivitas fisik harian. Studi Lin et al. (2025) terhadap 20.645 responden membuktikan bahwa kebiasaan gaya hidup digital merupakan prediktor nyata yang dapat dipetakan secara akurat menggunakan machine learning. Temuan tersebut membuka peluang besar untuk mengembangkan sistem deteksi dini risiko gangguan tidur yang bersifat proaktif berbasis data perilaku."),
            
            ("Paragraf 2: Karakteristik Data Gaya Hidup & Keunggulan CatBoost (121 kata)",
             "Membangun sistem deteksi dini tersebut memerlukan algoritma pembelajaran mesin yang berakurasi tinggi sekaligus mampu mengolah data gaya hidup heterogen. Data gaya hidup memadukan variabel numerik seperti durasi tidur dan detak jantung dengan variabel kategorikal seperti jenis pekerjaan dan tingkat stres. Banyak algoritma konvensional seperti Random Forest atau XGBoost mengalami kendala saat memproses data kategorikal, karena membutuhkan proses encoding manual yang rentan memicu bias serta ledakan dimensi data. Algoritma CatBoost dirancang khusus untuk mengatasi masalah ini melalui mekanisme ordered target statistics yang memproses fitur kategorikal secara langsung tanpa encoding manual. Keunggulan gradient boosting terbukti pada studi Taher & Ayon (2024) yang meraih akurasi 93,80% pada klasifikasi gangguan tidur. Oleh karena itu, CatBoost sangat tepat digunakan karena selaras dengan karakteristik data gaya hidup."),
            
            ("Paragraf 3: Tantangan Black-Box & Urgensi Explainable AI (123 kata)",
             "Kendati memiliki akurasi yang tinggi, algoritma berbasis ensemble seperti CatBoost memiliki kelemahan utama karena beroperasi sebagai model kotak hitam atau black-box. Keputusan prediksi dihasilkan dari ratusan pohon keputusan paralel yang rumit, sehingga pengguna tidak dapat memahami alasan di balik penetapan tingkat risiko seseorang secara logis. Dalam dunia medis, ketidakmampuan model menjelaskan proses keputusannya menjadi hambatan besar bagi adopsi teknologi kecerdasan buatan klinis. Dokter maupun pasien membutuhkan landasan rasional yang transparan dan dapat dipertanggungjawabkan sebelum mengambil keputusan medis atau intervensi perilaku harian. Penelitian Ha et al. (2023) menunjukkan bahwa metode Explainable AI mampu meningkatkan keterbukaan prediksi gangguan tidur, meskipun penerapannya masih terbatas pada penyaringan kuesioner awal. Oleh sebab itu, integrasi Explainable AI menjadi kebutuhan mutlak agar model klasifikasi tidak hanya akurat, tetapi juga transparan."),
            
            ("Paragraf 4: Metode SHAP untuk Penjelasan Adil & Konsisten (123 kata)",
             "Di antara berbagai pendekatan Explainable AI modern, metode Shapley Additive exPlanations atau SHAP dipandang paling unggul karena memiliki landasan teori permainan kooperatif yang kokoh. Berdasarkan prinsip matematis fundamental yang dirumuskan oleh Lundberg & Lee (2017), metode SHAP mampu menjamin perhitungan kontribusi setiap variabel input secara adil, konsisten, dan aditif. Keunggulan utama metode SHAP adalah kemampuannya menyajikan penjelasan pada tingkat populasi global sekaligus tingkat individu lokal secara mendalam. Efektivitas SHAP dalam menganalisis faktor penentu kualitas tidur juga telah berhasil dibuktikan secara konkret oleh Xie et al. (2026). Melalui analisis SHAP, tenaga medis maupun pasien dapat mengetahui secara pasti variabel gaya hidup mana yang paling mendorong timbulnya risiko gangguan tidur pada setiap individu, seperti tingginya tingkat stres kerja atau durasi paparan layar gawai yang berlebih."),
            
            ("Paragraf 5: Identifikasi Riset Terdahulu & 5 Celah Riset / GAP (126 kata)",
             "Meskipun berbagai penelitian terdahulu menunjukkan hasil positif, terdapat lima celah riset utama yang belum terselesaikan secara simultan. Taher & Ayon (2024) menghasilkan model berakurasi tinggi namun tanpa transparansi faktor risiko individual. Lin et al. (2025) hanya menganalisis faktor tidur pada tingkat populasi umum tanpa personalisasi per individu. Ha et al. (2023) menerapkan metode SHAP sebatas untuk seleksi fitur kuesioner statis menggunakan algoritma XGBoost. Xie et al. (2026) menggunakan teknik one-hot encoding yang memecah fitur kategorikal sehingga penjelasan SHAP terfragmentasi dan membingungkan secara klinis. Terakhir, Das et al. (2025) berhasil membuktikan keunggulan CatBoost-SHAP pada insomnia namun terbatas pada klasifikasi biner pasien kronis tanpa visualisasi lokal per individu. Belum ada penelitian yang menggabungkan keunggulan CatBoost dan SHAP untuk klasifikasi multi-kelas risiko gangguan tidur berbasis gaya hidup secara personal."),
            
            ("Paragraf 6: Solusi Usulan, CatBoost-SHAP & Prototipe Web CDSS (123 kata)",
             "Berdasarkan kelima celah riset tersebut, penelitian ini mengusulkan penerapan metode Explainable AI berbasis SHAP pada algoritma CatBoost untuk klasifikasi risiko gangguan tidur berbasis metrik gaya hidup digital. Algoritma CatBoost dipilih karena memiliki keunggulan dalam mengolah data kategorikal tanpa merusak struktur data aslinya, sehingga nilai kontribusi SHAP tetap utuh dan bermakna secara klinis. Pendekatan ini diharapkan mampu mengenali pola risiko tidur secara akurat sekaligus memetakan faktor pemicu dominan pada setiap individu secara tepat. Selain itu, model yang dikembangkan akan diintegrasikan secara langsung ke dalam purwarupa sistem pendukung keputusan klinis berbasis web yang interaktif. Sistem ini dirancang agar mudah digunakan oleh masyarakat umum untuk mengenali kebiasaan buruknya, sekaligus membantu tenaga medis dalam merancang rekomendasi perubahan gaya hidup yang terarah, efektif, dan berbasis bukti ilmiah terpercaya.")
        ]),
        
        ("TINJAUAN PUSTAKA (STATE OF THE ART)", [
            ("1. Xie et al. (2026)",
             "Meneliti faktor kualitas tidur mahasiswa menggunakan PLS dan XGBoost dengan SHAP. Menemukan durasi tidur, stres, dan layar gawai sebagai faktor dominan.\nCelah Riset (Gap): Penggunaan one-hot encoding memecah fitur nominal ke dalam variabel biner tiruan sehingga penjelasan SHAP terfragmentasi dan sulit dipahami secara klinis."),
            
            ("2. Ha et al. (2023)",
             "Memprediksi risiko OSA, insomnia, dan COMISA menggunakan XGBoost dan SHAP dari 4.622 pasien rumah sakit (AUROC >0,897).\nCelah Riset (Gap): Fitur berbasis kuesioner medis statis, memerlukan encoding manual, dan SHAP hanya digunakan untuk seleksi fitur awal, bukan untuk penjelasan individual real-time."),
            
            ("3. Lin et al. (2025)",
             "Menganalisis faktor kualitas tidur pada 20.645 mahasiswa menggunakan ANN, Decision Tree, dan Naive Bayes.\nCelah Riset (Gap): Model bersifat black-box dan analisis hanya berlaku pada tingkat populasi umum secara agregat tanpa penjelasan personal per individu."),
            
            ("4. Das et al. (2025)",
             "Menganalisis faktor risiko insomnia pada 1.222 pasien penyakit kronis di Nature and Science of Sleep menggunakan 6 algoritma ML. CatBoost terbukti terbaik (akurasi 71,67%, AUC 77,27%) dengan eksplanasi SHAP.\nCelah Riset (Gap): Pemodelan klasifikasi terbatas pada target biner pasien komorbid rumah sakit, visualisasi SHAP hanya agregat global populasi tanpa visualisasi lokal per individu, dan tanpa sistem web CDSS terapan."),
            
            ("5. Taher & Ayon (2024)",
             "Menguji klasifikasi gangguan tidur dengan Gradient Boosting (akurasi 93,80%), Random Forest, dan AdaBoost.\nCelah Riset (Gap): Model beroperasi murni sebagai black-box tanpa XAI, hanya mendeteksi tingkat risiko tanpa menjelaskan faktor penyebab spesifik yang dapat ditindaklanjuti.")
        ]),
        
        ("REFERENSI / DAFTAR PUSTAKA", [
            "1. Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. Frontiers in Psychology, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946",
            "2. Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A. A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025). Prevalence and Factors Associated with Insomnia Among Chronic Disease Patients in Bangladesh: A Machine Learning Study. Nature and Science of Sleep, 17, 2541–2567. https://doi.org/10.2147/NSS.S547335",
            "3. Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the Risk of Sleep Disorders Using a Machine Learning–Based Simple Questionnaire: Development and Validation Study. Journal of Medical Internet Research, 25, e46520. https://doi.org/10.2196/46520",
            "4. Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L. (2025). Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. Frontiers in Psychiatry, 16, 1533875. https://doi.org/10.3389/fpsyt.2025.1533875",
            "5. Lundberg, S. M., & Lee, S. I. (2017). A Unified Approach to Interpreting Model Predictions. Advances in Neural Information Processing Systems (NeurIPS), 30.",
            "6. Taher, A., & Ayon, W. I. Z. (2024). Exploring Sleep Disorders: A Comparative Analysis of Machine Learning Algorithms on Sleep Health and Lifestyle Data. 2024 IEEE PEEIACON, 1–6. https://doi.org/10.1109/PEEIACON63629.2024.10800593"
        ])
    ]

    for idx, (label, content) in enumerate(rows_data):
        row = table_outline.rows[idx]
        set_cell_margins(row.cells[0])
        set_cell_margins(row.cells[1])
        set_cell_shading(row.cells[0], "F2F2F2")

        # Label cell
        p_lbl = row.cells[0].paragraphs[0]
        set_font(p_lbl.add_run(label), bold=True, size=10)

        # Content cell
        p_cnt = row.cells[1].paragraphs[0]
        if isinstance(content, str):
            set_font(p_cnt.add_run(content), size=10)
        elif isinstance(content, list):
            if isinstance(content[0], tuple): # Subsections
                for s_idx, (stitle, stext) in enumerate(content):
                    if s_idx > 0:
                        p_cnt = row.cells[1].add_paragraph()
                    set_font(p_cnt.add_run(stitle + "\n"), bold=True, size=10)
                    set_font(p_cnt.add_run(stext), size=10)
                    p_cnt.paragraph_format.space_after = Pt(6)
            else: # Plain list of references
                for r_idx, ref in enumerate(content):
                    if r_idx > 0:
                        p_cnt = row.cells[1].add_paragraph()
                    set_font(p_cnt.add_run(ref), size=9.5)
                    p_cnt.paragraph_format.space_after = Pt(4)

    # 3. TABEL RESEARCH GAP PENELITIAN
    doc.add_page_break()
    p_gap_title = doc.add_paragraph()
    set_font(p_gap_title.add_run("TABEL RESEARCH GAP PENELITIAN TERDAHULU"), size=12, bold=True)
    p_gap_desc = doc.add_paragraph()
    set_font(p_gap_desc.add_run("Tabel ini memetakan secara komprehensif keterbatasan penelitian terdahulu dan solusi yang diajukan oleh penelitian ini (Ahmad, 2026):"), size=10, italic=True)

    gap_table = doc.add_table(rows=6, cols=6)
    gap_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(gap_table)

    headers = [
        "No", 
        "Peneliti & Tahun", 
        "Metode / Algoritma", 
        "Hasil Utama", 
        "Celah Riset (Research Gap)", 
        "Solusi Penelitian Ini (Ahmad, 2026)"
    ]
    
    col_widths = [Inches(0.4), Inches(1.1), Inches(1.1), Inches(1.2), Inches(1.5), Inches(1.5)]

    # Set Header
    for c_idx, h_text in enumerate(headers):
        cell = gap_table.rows[0].cells[c_idx]
        set_cell_margins(cell, 140, 140, 120, 120)
        set_cell_shading(cell, "1F4E79") # Deep Blue
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h_text)
        set_font(run, size=9.5, bold=True, color=RGBColor(255,255,255))

    gap_data = [
        ("1",
         "Taher & Ayon\n(2024)",
         "Gradient Boosting, Random Forest, AdaBoost pada dataset gaya hidup",
         "Gradient Boosting mencapai akurasi tertinggi 93,80% dalam mendeteksi risiko gangguan tidur.",
         "Model bekerja sebagai black-box murni tanpa XAI; hanya mendeteksi tingkat risiko global tanpa mampu menjelaskan faktor penyebab spesifik per individu (lack of actionable insight).",
         "Menerapkan metode XAI-SHAP untuk membuka kotak hitam model dan menjelaskan kontribusi faktor gaya hidup secara personal bagi setiap individu."),
        
        ("2",
         "Lin et al.\n(2025)",
         "ANN, Decision Tree, Naive Bayes pada 20.645 data survei mahasiswa",
         "Menemukan korelasi signifikan antara durasi layar, kopi, begadang, dan kualitas tidur.",
         "Analisis hanya pada tingkat populasi umum secara agregat; tidak mampu memberikan penjelasan risiko secara personal untuk masing-masing individu.",
         "Mengimplementasikan analisis SHAP lokal (waterfall plot) yang membedah profil risiko unik per individu secara interaktif."),
        
        ("3",
         "Ha et al.\n(2023)",
         "XGBoost + SHAP pada 4.622 kuesioner medis klinis rumah sakit",
         "Model mencapai AUROC >0,897 untuk klasifikasi OSA, COMISA, dan insomnia.",
         "Menggunakan XGBoost yang butuh encoding manual, data kuesioner statis, dan SHAP hanya digunakan untuk seleksi fitur awal bukan penjelasan individual real-time.",
         "Menggunakan CatBoost yang memproses data kategorikal secara native, memanfaatkan data gaya hidup fleksibel (modifiable), dan menerapkan SHAP untuk interpretasi real-time."),
        
        ("4",
         "Chen et al.\n(2024)",
         "PLS + XGBoost + SHAP pada survei gaya hidup mahasiswa",
         "Mengidentifikasi durasi tidur, tingkat stres, dan ponsel sebagai prediktor utama.",
         "XGBoost mewajibkan one-hot encoding sehingga fitur terpecah menjadi variabel tiruan biner; visualisasi SHAP menjadi terfragmentasi dan sulit dipahami secara klinis.",
         "Mengadopsi CatBoost (ordered target statistics) tanpa one-hot encoding, menjaga keutuhan fitur sehingga hasil penjelasan SHAP tetap kohesif dan intuitif."),
        
        ("5",
         "Das et al.\n(2025)",
         "CatBoost, XGBoost, RF, SVM, GBM, KNN + SHAP (Nature & Science of Sleep)",
         "CatBoost meraih akurasi tertinggi 71,67% dan AUC 77,27% dalam memprediksi insomnia klinis.",
         "Klasifikasi hanya biner (2 kelas), populasi terbatas pasien penyakit kronis di RS, eksplanasi SHAP hanya di tingkat global populasi, dan tanpa sistem web CDSS terapan.",
         "Membangun klasifikasi multi-kelas 4 level risiko (Healthy s/d Severe) pada 100.000 data gaya hidup digital, XAI-SHAP lokal waterfall per pasien secara real-time, dan Prototipe Web CDSS interaktif.")
    ]

    for r_idx, r_data in enumerate(gap_data, start=1):
        row = gap_table.rows[r_idx]
        bg_color = "F9FBFD" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            set_cell_margins(cell, 100, 100, 120, 120)
            set_cell_shading(cell, bg_color)
            p = cell.paragraphs[0]
            if c_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_font(p.add_run(val), size=9, bold=True)
            elif c_idx == 1:
                set_font(p.add_run(val), size=9, bold=True)
            else:
                set_font(p.add_run(val), size=9)

    # 4. TABEL MATRIKS NOVELTY
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    p_mat_title = doc.add_paragraph()
    set_font(p_mat_title.add_run("TABEL MATRIKS PEMETAAN NOVELTY (ORISINALITAS RISET)"), size=12, bold=True)

    mat_table = doc.add_table(rows=9, cols=7)
    mat_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(mat_table)

    m_headers = [
        "Kriteria / Parameter",
        "Taher & Ayon (2024)",
        "Lin et al. (2025)",
        "Ha et al. (2023)",
        "Xie et al. (2026)",
        "Das et al. (2025)",
        "Penelitian Ini (Ahmad, 2026)"
    ]

    for c_idx, h in enumerate(m_headers):
        cell = mat_table.rows[0].cells[c_idx]
        set_cell_margins(cell, 120, 120, 100, 100)
        set_cell_shading(cell, "2B4C7E")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_font(run, size=8.5, bold=True, color=RGBColor(255,255,255))

    m_rows = [
        ("Domain Kasus: Gangguan Tidur", "Ya", "Ya", "Ya", "Ya", "Ya", "YA (100% Homogen)"),
        ("Algoritma Utama: CatBoost (Native)", "Tidak", "Tidak", "Tidak (XGBoost)", "Tidak (XGBoost)", "Ya", "YA"),
        ("Target: Multi-Kelas 4 Level Risiko", "Tidak (Biner)", "Tidak (Skor PSQI)", "Tidak (Biner)", "Tidak (Regresi)", "Tidak (Biner)", "YA (4 Tingkat)"),
        ("Skala Data: 100.000 Rekaman Data", "Tidak (374)", "Ya (20.645)", "Tidak (4.622)", "Tidak (Kuesioner)", "Tidak (1.222)", "YA (100.000 Data)"),
        ("Karakter Fitur: Gaya Hidup (Modifiable)", "Ya", "Ya", "Tidak (Klinis)", "Ya", "Tidak (Pasien Kronis)", "YA"),
        ("Metodologi XAI: Implementasi SHAP", "Tidak", "Tidak", "Ya (Seleksi Fitur)", "Ya (Terfragmentasi OHE)", "Ya (Summary Global)", "YA"),
        ("Penjelasan Lokal per Pasien (Waterfall)", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak (Hanya Global)", "YA (Real-Time)"),
        ("Prototipe Web Interaktif (CDSS)", "Tidak", "Tidak", "Ya (Web Statis)", "Tidak", "Tidak", "YA (INTERAKTIF)")
    ]

    for r_idx, r_vals in enumerate(m_rows, start=1):
        row = mat_table.rows[r_idx]
        bg_col = "F5F8FA" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_vals):
            cell = row.cells[c_idx]
            set_cell_margins(cell, 90, 90, 90, 90)
            set_cell_shading(cell, bg_col)
            p = cell.paragraphs[0]
            if c_idx == 0:
                set_font(p.add_run(val), size=8.5, bold=True)
            elif c_idx == 6:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_font(p.add_run(val), size=8.5, bold=True, color=RGBColor(0, 102, 204))
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_font(p.add_run(val), size=8.5)

    # Save
    out_path = "OUTLINE_PROPOSAL_REVISI_FINAL.docx"
    doc.save(out_path)
    print(f"File successfully created at {out_path}")

if __name__ == "__main__":
    create_proposal_docx()
