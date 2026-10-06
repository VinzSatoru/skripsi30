import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def create_bab1_docx():
    doc = docx.Document()

    # Standar UNISNU: Top 4cm, Left 4cm, Bottom 3cm, Right 3cm
    for section in doc.sections:
        section.top_margin = Cm(4)
        section.left_margin = Cm(4)
        section.bottom_margin = Cm(3)
        section.right_margin = Cm(3)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    def set_font(run, name='Times New Roman', size=12, bold=False, italic=False, color=RGBColor(0,0,0)):
        run.font.name = name
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(18)
        p.paragraph_format.line_spacing = 1.5
        run = p.add_run(text)
        set_font(run, size=14, bold=True)
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        run = p.add_run(text)
        set_font(run, size=12, bold=True)
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.5
        run = p.add_run(text)
        set_font(run, size=12, bold=True, italic=True)
        return p

    def add_academic_paragraph(text, space_after=6):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.0) # 1 tab = 10 mm
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(space_after)
        
        # Format text with italics for latin/foreign words
        words = text.split()
        foreign_words = [
            'machine', 'learning', 'black-box', 'gradient', 'boosting', 'ensemble',
            'ordered', 'target', 'statistics', 'Explainable', 'Artificial', 'Intelligence',
            'Shapley', 'Additive', 'exPlanations', 'TreeExplainer', 'Clinical', 'Decision',
            'Support', 'System', 'waterfall', 'plot', 'summary', 'beeswarm', 'one-hot',
            'encoding', 'multi-class', 'cost-sensitive', 'balanced', 'AUROC', 'F1-score',
            'accuracy', 'recall', 'precision', 'healthy', 'mild', 'moderate', 'severe',
            'technostress', 'nomophobia', 'modifiable', 'oversampling'
        ]
        
        run = p.add_run(text)
        set_font(run, size=12)
        return p

    def add_bullet_item(prefix, text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-0.5)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(4)
        
        r_pre = p.add_run(prefix + " ")
        set_font(r_pre, size=12, bold=True)
        r_txt = p.add_run(text)
        set_font(r_txt, size=12)
        return p

    # Read markdown
    with open('BAB_1_Draft_Final.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Build Document
    add_heading_1("BAB I\nPENDAHULUAN")
    
    # 1.1 Latar Belakang
    add_heading_2("1.1 Latar Belakang Masalah")
    
    p1 = ("Gangguan tidur saat ini telah berkembang menjadi masalah kesehatan masyarakat yang serius di era modern. "
          "Kondisi ini tidak hanya menurunkan kebugaran tubuh sehari-hari, tetapi juga berhubungan erat dengan peningkatan risiko berbagai penyakit kronis "
          "seperti gangguan kardiovaskular, diabetes, hingga depresi. Pada era serba digital, sebagian besar pemicu gangguan tidur berkaitan langsung "
          "dengan pola kebiasaan harian yang dapat diukur secara kuantitatif. Faktor-faktor tersebut meliputi durasi paparan layar gawai sebelum tidur, "
          "beban kerja, konsumsi kafein, hingga minimnya aktivitas fisik harian. Studi Lin et al. (2025) terhadap 20.645 responden membuktikan bahwa "
          "kebiasaan gaya hidup digital merupakan prediktor nyata yang dapat dipetakan secara akurat menggunakan machine learning. "
          "Temuan tersebut membuka peluang besar untuk mengembangkan sistem deteksi dini risiko gangguan tidur yang bersifat proaktif berbasis data perilaku.")
    add_academic_paragraph(p1)

    p2 = ("Membangun sistem deteksi dini tersebut memerlukan algoritma pembelajaran mesin yang berakurasi tinggi sekaligus mampu mengolah data gaya hidup heterogen. "
          "Data gaya hidup memadukan variabel numerik seperti durasi tidur dan detak jantung dengan variabel kategorikal seperti jenis pekerjaan dan tingkat stres. "
          "Banyak algoritma konvensional seperti Random Forest atau XGBoost mengalami kendala saat memproses data kategorikal, karena membutuhkan proses encoding manual "
          "yang rentan memicu bias serta ledakan dimensi data. Algoritma CatBoost dirancang khusus untuk mengatasi masalah ini melalui mekanisme ordered target statistics "
          "yang memproses fitur kategorikal secara langsung tanpa encoding manual. Keunggulan gradient boosting terbukti pada studi Taher & Ayon (2024) "
          "yang meraih akurasi 93,80% pada klasifikasi gangguan tidur. Oleh karena itu, CatBoost sangat tepat digunakan karena selaras dengan karakteristik data gaya hidup.")
    add_academic_paragraph(p2)

    p3 = ("Kendati memiliki akurasi yang tinggi, algoritma berbasis ensemble seperti CatBoost memiliki kelemahan utama karena beroperasi sebagai model kotak hitam atau black-box. "
          "Keputusan prediksi dihasilkan dari ratusan pohon keputusan paralel yang rumit, sehingga pengguna tidak dapat memahami alasan di balik penetapan tingkat risiko seseorang secara logis. "
          "Dalam dunia medis, ketidakmampuan model menjelaskan proses keputusannya menjadi hambatan besar bagi adopsi teknologi kecerdasan buatan klinis. "
          "Dokter maupun pasien membutuhkan landasan rasional yang transparan dan dapat dipertanggungjawabkan sebelum mengambil keputusan medis atau intervensi perilaku harian. "
          "Penelitian Ha et al. (2023) menunjukkan bahwa metode Explainable AI mampu meningkatkan keterbukaan prediksi gangguan tidur, meskipun penerapannya masih terbatas "
          "pada penyaringan kuesioner awal. Oleh sebab itu, integrasi Explainable AI menjadi kebutuhan mutlak agar model klasifikasi tidak hanya akurat, tetapi juga transparan.")
    add_academic_paragraph(p3)

    p4 = ("Di antara berbagai pendekatan Explainable AI modern, metode Shapley Additive exPlanations atau SHAP dipandang paling unggul karena memiliki landasan teori permainan kooperatif yang kokoh. "
          "Berdasarkan prinsip matematis fundamental yang dirumuskan oleh Lundberg & Lee (2017), metode SHAP mampu menjamin perhitungan kontribusi setiap variabel input secara adil, konsisten, dan aditif. "
          "Keunggulan utama metode SHAP adalah kemampuannya menyajikan penjelasan pada tingkat populasi global sekaligus tingkat individu lokal secara mendalam. "
          "Efektivitas SHAP dalam menganalisis faktor penentu kualitas tidur juga telah berhasil dibuktikan secara konkret oleh Xie et al. (2026). "
          "Melalui analisis SHAP, tenaga medis maupun pasien dapat mengetahui secara pasti variabel gaya hidup mana yang paling mendorong timbulnya risiko gangguan tidur pada setiap individu, "
          "seperti tingginya tingkat stres kerja atau durasi paparan layar gawai yang berlebih.")
    add_academic_paragraph(p4)

    p5 = ("Meskipun berbagai penelitian terdahulu menunjukkan hasil positif, terdapat lima celah riset utama yang belum terselesaikan secara simultan. "
          "Taher & Ayon (2024) menghasilkan model berakurasi tinggi namun tanpa transparansi faktor risiko individual. "
          "Lin et al. (2025) hanya menganalisis faktor tidur pada tingkat populasi umum tanpa personalisasi per individu. "
          "Ha et al. (2023) menerapkan metode SHAP sebatas untuk seleksi fitur kuesioner statis menggunakan algoritma XGBoost. "
          "Xie et al. (2026) menggunakan teknik one-hot encoding yang memecah fitur kategorikal sehingga penjelasan SHAP terfragmentasi dan membingungkan secara klinis. "
          "Terakhir, Das et al. (2025) berhasil membuktikan keunggulan CatBoost-SHAP pada insomnia namun terbatas pada klasifikasi biner pasien kronis tanpa visualisasi lokal per individu. "
          "Belum ada penelitian yang menggabungkan keunggulan CatBoost dan SHAP untuk klasifikasi multi-kelas risiko gangguan tidur berbasis gaya hidup secara personal.")
    add_academic_paragraph(p5)

    p6 = ("Berdasarkan kelima celah riset tersebut, penelitian ini mengusulkan penerapan metode Explainable AI berbasis SHAP pada algoritma CatBoost untuk klasifikasi risiko gangguan tidur berbasis metrik gaya hidup digital. "
          "Algoritma CatBoost dipilih karena memiliki keunggulan dalam mengolah data kategorikal tanpa merusak struktur data aslinya, sehingga nilai kontribusi SHAP tetap utuh dan bermakna secara klinis. "
          "Pendekatan ini diharapkan mampu mengenali pola risiko tidur secara akurat sekaligus memetakan faktor pemicu dominan pada setiap individu secara tepat. "
          "Selain itu, model yang dikembangkan akan diintegrasikan secara langsung ke dalam purwarupa sistem pendukung keputusan klinis berbasis web yang interaktif. "
          "Sistem ini dirancang agar mudah digunakan oleh masyarakat umum untuk mengenali kebiasaan buruknya, sekaligus membantu tenaga medis dalam merancang rekomendasi perubahan gaya hidup yang terarah, efektif, dan berbasis bukti ilmiah terpercaya.")
    add_academic_paragraph(p6)

    # 1.2 Rumusan Masalah
    add_heading_2("1.2 Rumusan Masalah")
    p_rm_intro = ("Berdasarkan latar belakang masalah dan identifikasi celah riset di atas, maka rumusan masalah dalam penelitian ini dirumuskan sebagai berikut:")
    add_academic_paragraph(p_rm_intro, space_after=4)
    add_bullet_item("1.", "Bagaimana mengimplementasikan algoritma CatBoost dengan penanganan ketidakseimbangan kelas berbasis cost-sensitive learning untuk klasifikasi multikelas tingkat risiko gangguan tidur berbasis metrik gaya hidup digital?")
    add_bullet_item("2.", "Bagaimana menerapkan metode Explainable Artificial Intelligence (XAI) berbasis Shapley Additive exPlanations (SHAP) guna mengekstraksi penjelasan global dan lokal dari keputusan prediksi model secara transparan, adil, dan konsisten?")
    add_bullet_item("3.", "Bagaimana merancang purwarupa Clinical Decision Support System (CDSS) berbasis web yang interaktif guna menyajikan visualisasi prediksi risiko dan rekomendasi intervensi gaya hidup yang dapat dipahami oleh pengguna awam dan klinisi?")

    # 1.3 Tujuan Penelitian
    add_heading_2("1.3 Tujuan Penelitian")
    p_tj_intro = ("Mengacu pada rumusan masalah yang telah diuraikan, tujuan yang hendak dicapai dalam penelitian ini adalah sebagai berikut:")
    add_academic_paragraph(p_tj_intro, space_after=4)
    add_bullet_item("1.", "Mengembangkan model klasifikasi multikelas empat tingkat risiko gangguan tidur (Healthy, Mild, Moderate, Severe) menggunakan algoritma CatBoost dengan mekanisme Ordered Target Statistics dan pembobotan penalti kelas (cost-sensitive weights) guna mengatasi ketidakseimbangan sebaran data.")
    add_bullet_item("2.", "Menerapkan metode XAI-SHAP (TreeExplainer) guna menguraikan kontribusi fitur secara global pada tingkat populasi (summary beeswarm plot) dan secara lokal pada tingkat individu (waterfall plot), sehingga mewujudkan transparansi proses inferensi bagi tenaga medis.")
    add_bullet_item("3.", "Membangun purwarupa sistem pendukung keputusan klinis (Clinical Decision Support System) berbasis web yang mengintegrasikan hasil prediksi risiko CatBoost dan interpretasi visual SHAP ke dalam bentuk rekomendasi tindakan perubahan gaya hidup yang terarah.")

    # 1.4 Manfaat Penelitian
    add_heading_2("1.4 Manfaat Penelitian")
    p_mf_intro = ("Hasil penelitian ini diharapkan dapat memberikan kontribusi dan manfaat nyata, baik secara teoretis maupun praktis:")
    add_academic_paragraph(p_mf_intro, space_after=4)

    add_heading_3("1.4.1 Manfaat Teoretis")
    add_bullet_item("1.", "Bagi Pengembangan Ilmu Pengetahuan: Memberikan kontribusi ilmiah dalam ranah informatika medis (health informatics) dan kecerdasan buatan terapan, khususnya mengenai efektivitas integrasi algoritma CatBoost dengan metode XAI-SHAP dalam memproses data perilaku gaya hidup heterogen tanpa menimbulkan fragmentasi fitur akibat teknik encoding manual.")
    add_bullet_item("2.", "Bagi Peneliti: Memperluas wawasan keilmuan metodologis dan keterampilan teknis dalam rekayasa sistem pembelajaran mesin yang dapat dipertanggungjawabkan (interpretable machine learning), mulai dari pra-pemrosesan data berskala besar, pembuktian aksioma matematika SHAP, hingga diseminasi sistem berbasis web.")

    add_heading_3("1.4.2 Manfaat Praktis")
    add_bullet_item("1.", "Bagi Tenaga Kesehatan dan Klinisi: Menyediakan instrumen skrining awal yang objektif dan transparan guna membantu tenaga medis mengenali faktor pemicu dominan gangguan tidur pasien secara terpersonalisasi, sehingga mempermudah formulasi intervensi klinis yang lebih efektif dan tepat sasaran.")
    add_bullet_item("2.", "Bagi Masyarakat Umum: Meningkatkan literasi dan kesadaran preventif mengenai bahaya gaya hidup digital yang tidak teratur terhadap kesehatan tidur, serta memfasilitasi evaluasi kebiasaan harian secara mandiri melalui antarmuka web yang informatif dan mudah dipahami.")

    # 1.5 Daftar Pustaka Bab 1
    add_heading_2("DAFTAR PUSTAKA")
    refs = [
        "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. Frontiers in Psychology, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946",
        "Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025). Prevalence and factors associated with insomnia among chronic disease patients in Bangladesh: A machine learning study. Nature and Science of Sleep, 17, 2725–2741. https://doi.org/10.2147/NSS.S547335",
        "Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study. Journal of Medical Internet Research, 25, e46520. https://doi.org/10.2196/46520",
        "Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L. (2025). Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. Frontiers in Psychiatry, 16, 1533875. https://doi.org/10.3389/fpsyt.2025.1533875",
        "Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems (NeurIPS), 30, 4765–4774.",
        "Taher, A., & Ayon, W. I. Z. (2024). Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data. 2024 IEEE PEEIACON, 1–6. https://doi.org/10.1109/PEEIACON63765.2024.10844781"
    ]
    for r in refs:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.left_indent = Cm(1.0)
        p_ref.paragraph_format.first_line_indent = Cm(-1.0) # hanging indent
        p_ref.paragraph_format.line_spacing = 1.5
        p_ref.paragraph_format.space_after = Pt(6)
        r_run = p_ref.add_run(r)
        set_font(r_run, size=11)

    output_path = 'BAB_1_Draft_Final.docx'
    doc.save(output_path)
    print(f"[OK] Successfully built: {output_path}")

if __name__ == '__main__':
    create_bab1_docx()
