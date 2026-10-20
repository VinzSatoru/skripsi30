import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls
from latex2mathml.converter import convert as latex2mathml_convert
from lxml import etree
import os, sys, json, shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Paths
OUT_DIR = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\02_Draft_Per_Bab\Bab_2"
TARGET_DOCX = os.path.join(OUT_DIR, "BAB 2.docx")
ROOT_COPY = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\BAB 2.docx"
MASTER_DIR = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\01_Naskah_Proposal_Master"
PROPOSAL_BAB2_COPY = os.path.join(MASTER_DIR, "BAB 2.docx")
IMAGE_PATH = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\scratch\extracted_images\Gambar_2_1_Kerangka_Berpikir.png"
SOTA_JSON = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\scratch\sota_table_data.json"
XSLT_PATH = r"C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL"

xslt_tree = etree.parse(XSLT_PATH)
transform_omml = etree.XSLT(xslt_tree)

def latex_to_omml(latex_code):
    """Converts LaTeX string to native Word OMML XML string."""
    mathml = latex2mathml_convert(latex_code)
    tree = etree.fromstring(mathml)
    omml = transform_omml(tree)
    omml_str = etree.tostring(omml, encoding='unicode')
    return omml_str

doc = docx.Document()

# ---------------------------------------------------------------------------
# Page Setup: Standard Academic Thesis (Left 4cm, Top 3cm, Right 3cm, Bottom 3cm)
# Total text width = 21.0 - 4.0 - 3.0 = 14.0 cm = 5.51 inches
# ---------------------------------------------------------------------------
section = doc.sections[0]
section.page_width = Cm(21.0)
section.page_height = Cm(29.7)
section.left_margin = Cm(4.0)
section.right_margin = Cm(3.0)
section.top_margin = Cm(3.0)
section.bottom_margin = Cm(3.0)

# Set base Normal style
normal_style = doc.styles['Normal']
normal_style.font.name = 'Times New Roman'
normal_style.font.size = Pt(12)
normal_style.font.color.rgb = RGBColor(0, 0, 0)
normal_style.paragraph_format.line_spacing = 1.5
normal_style.paragraph_format.space_after = Pt(6)

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------
def remove_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'none')
        tblBorders.append(border)
    tblPr.append(tblBorders)

def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_p(doc, text, bold_prefix="", indent=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(space_after)
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.5)
    else:
        p.paragraph_format.first_line_indent = Inches(0.0)
        
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(12)
        r_b.font.bold = True
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p

def add_h1(doc, text1, text2):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(18)
    
    r1 = p.add_run(text1 + "\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(14)
    r1.font.bold = True
    
    r2 = p.add_run(text2)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(14)
    r2.font.bold = True

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True

def add_native_equation_block(doc, latex_code, eq_num, param_list=None):
    """
    Creates a publication-grade native Microsoft Word equation block:
    - 2-column borderless table
    - Col 0: Centered native OMML equation (width = 4.4 inches)
    - Col 1: Right-aligned (Persamaan 2.X) (width = 1.1 inches)
    - Followed by a perfectly aligned 3-column table for parameter descriptions
    """
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    remove_table_borders(tbl)
    
    tbl.columns[0].width = Inches(4.4)
    tbl.columns[1].width = Inches(1.1)
    
    # Cell 0: Native OMML equation
    c0 = tbl.cell(0, 0)
    c0.width = Inches(4.4)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.paragraph_format.space_before = Pt(6)
    p0.paragraph_format.space_after = Pt(6)
    
    omml_xml = latex_to_omml(latex_code)
    omml_el = parse_xml(omml_xml)
    p0._p.append(omml_el)
    
    # Cell 1: Equation number
    c1 = tbl.cell(0, 1)
    c1.width = Inches(1.1)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p1.paragraph_format.space_before = Pt(6)
    p1.paragraph_format.space_after = Pt(6)
    r1 = p1.add_run(f"({eq_num})")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(11)
    r1.font.bold = True
    
    # Parameters section with aligned '='
    if param_list:
        p_intro = doc.add_paragraph()
        p_intro.paragraph_format.left_indent = Inches(0.25)
        p_intro.paragraph_format.first_line_indent = Inches(0.0)
        p_intro.paragraph_format.space_before = Pt(2)
        p_intro.paragraph_format.space_after = Pt(2)
        r_lead = p_intro.add_run("Keterangan:")
        r_lead.font.name = 'Times New Roman'
        r_lead.font.size = Pt(11)
        r_lead.font.italic = True
        
        # 3-column table: Symbol (1.2 in), '=' (0.25 in), Description (4.05 in)
        param_tbl = doc.add_table(rows=len(param_list), cols=3)
        param_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        param_tbl.autofit = False
        remove_table_borders(param_tbl)
        
        param_tbl.columns[0].width = Inches(1.2)
        param_tbl.columns[1].width = Inches(0.25)
        param_tbl.columns[2].width = Inches(4.05)
        
        for r_idx, item in enumerate(param_list):
            row = param_tbl.rows[r_idx]
            sym_latex, desc = item
            
            # Symbol cell: rendered via inline OMML math
            c_s = row.cells[0]
            c_s.width = Inches(1.2)
            p_s = c_s.paragraphs[0]
            p_s.paragraph_format.left_indent = Inches(0.25)
            p_s.paragraph_format.space_before = Pt(1)
            p_s.paragraph_format.space_after = Pt(1)
            p_s.paragraph_format.line_spacing = 1.15
            p_s.alignment = WD_ALIGN_PARAGRAPH.LEFT
            
            sym_omml = latex_to_omml(sym_latex)
            sym_el = parse_xml(sym_omml)
            p_s._p.append(sym_el)
            
            # Equal sign cell
            c_e = row.cells[1]
            c_e.width = Inches(0.25)
            p_e = c_e.paragraphs[0]
            p_e.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_e.paragraph_format.space_before = Pt(1)
            p_e.paragraph_format.space_after = Pt(1)
            p_e.paragraph_format.line_spacing = 1.15
            r_e = p_e.add_run("=")
            r_e.font.name = 'Times New Roman'
            r_e.font.size = Pt(11)
            
            # Description cell
            c_d = row.cells[2]
            c_d.width = Inches(4.05)
            p_d = c_d.paragraphs[0]
            p_d.paragraph_format.space_before = Pt(1)
            p_d.paragraph_format.space_after = Pt(1)
            p_d.paragraph_format.line_spacing = 1.15
            p_d.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r_d = p_d.add_run(desc)
            r_d.font.name = 'Times New Roman'
            r_d.font.size = Pt(10.5)

print("Building BAB 2.docx with native OMML equations...")

# ---------------------------------------------------------------------------
# DOCUMENT TITLE
# ---------------------------------------------------------------------------
add_h1(doc, "BAB II", "LANDASAN TEORI")

# ---------------------------------------------------------------------------
# 2.1 KAJIAN TEORI
# ---------------------------------------------------------------------------
add_h2(doc, "2.1 Kajian Teori")

# ---------------------------------------------------------------------------
# 2.1.1 Gangguan Tidur dan Metrik Gaya Hidup Digital
# ---------------------------------------------------------------------------
add_h3(doc, "2.1.1 Gangguan Tidur dan Metrik Gaya Hidup Digital")

add_p(doc, 
    "Kualitas tidur yang memadai merupakan salah satu pilar biologis yang sangat fundamental dalam menjaga stabilitas sistem fisiologis dan psikologis manusia (Medic et al., 2017). "
    "Secara fisiologis, siklus tidur manusia tersusun atas arsitektur kompleks yang terbagi ke dalam fase tidur non-Rapid Eye Movement (NREM) dan Rapid Eye Movement (REM). "
    "Fase NREM stadium 3, yang secara klinis dikenal sebagai tidur gelombang lambat (Slow-Wave Deep Sleep), memegang peranan krusial dalam pemulihan seluler, perbaikan jaringan somatik, pelepasan hormon pertumbuhan, serta konsolidasi memori imunologis. "
    "Berbagai studi epidemiologis skala luas membuktikan bahwa durasi tidur yang tidak mencukupi serta pola istirahat yang terdistorsi secara berkepanjangan berkorelasi langsung dengan lonjakan morbiditas penyakit kardiovaskular, sindrom metabolik, resistensi insulin, hingga risiko mortalitas dini (Windred et al., 2024). "
    "Dampak penurunan mutu istirahat ini terasa semakin destruktif apabila menimpa individu dengan riwayat komorbiditas kronis, di mana episode insomnia dan fragmentasi tidur malam secara klinis mempercepat perburukan prognosis medis pasien (Das et al., 2025). "
    "Mengingat prosedur evaluasi laboratoris standar emas seperti polisomnografi (PSG) memerlukan biaya tinggi, fasilitas rawat inap khusus, dan antrean waktu tunggu yang panjang, maka penapisan risiko preventif berbasis analisis multivariat gaya hidup kini diposisikan sebagai intervensi paling strategis dalam manajemen kesehatan masyarakat modern (Wang et al., 2025)."
)

add_p(doc,
    "Transformasi digital dan penetrasi perangkat cerdas (smartphones) dalam satu dekade terakhir telah merevolusi pola perilaku harian masyarakat secara menyeluruh. "
    "Tingginya intensitas penggunaan gawai elektronik menjelang waktu istirahat malam teridentifikasi sebagai determinan perilaku eksternal paling dominan yang merusak keteraturan sirkadian tubuh (Deivendran et al., 2025). "
    "Secara biokimiawi, emisi radiasi spektrum cahaya biru (blue light) dengan panjang gelombang 450–480 nm yang dipancarkan oleh layar LED menstimulasi sel ganglion retina fotosensitif intrinsik (ipRGCs). "
    "Sinyal saraf optik tersebut diteruskan secara langsung ke nukleus suprakiasmatik (SCN) pada hipotalamus, yang kemudian menekan biosintesis dan sekresi hormon melatonin oleh kelenjar pineal (Jahrami, 2023). "
    "Supresi melatonin ini menunda fase inisiasi rasa kantuk biologis (sleep onset latency), memperpendek durasi tidur gelombang lambat, serta memicu desinkronisasi jam sirkadian endogen. "
    "Akibatnya, pencatatan metrik durasi paparan layar gawai (screen time) merupakan variabel prediktor primer yang sangat esensial dalam stratifikasi risiko gangguan tidur era modern."
)

add_p(doc,
    "Di samping disrupsi fotobiologis akibat pancaran sinar layar gawai, interaksi digital yang konstan juga melahirkan beban tekanan psikologis baru yang didefinisikan sebagai technostress. "
    "Tuntutan untuk selalu responsif terhadap pesan kerja, arus informasi tanpa henti melalui media sosial, serta sindrom kecemasan tertinggal informasi (Fear of Missing Out / FOMO) menginduksi status hiperarousal mental fisiologis (Widayati, 2024). "
    "Kondisi ini menstimulasi aktivitas aksis hipotalamus-hipofisis-adrenal (HPA axis) dan sistem saraf simpatis secara berlebihan, sehingga melepaskan hormon kortisol yang menghambat relaksasi mental sebelum terlelap. "
    "Tekanan psikososial tersebut kemudian bersinergi secara destruktif dengan kebiasaan gaya hidup yang buruk, seperti konsumsi kafein berlebih, kebiasaan begadang, serta kurangnya aktivitas fisik teratur (Henrich et al., 2021). "
    "Untuk memutus lingkaran patologis tersebut, pedoman kebersihan tidur (Sleep Hygiene) diterapkan sebagai standar intervensi perilaku klinis lini pertama guna merestrukturisasi pola hidup individu (Irish et al., 2015). "
    "Standar parameter klinis Sleep Hygiene menetapkan ambang batas operasional bahwa interaksi dengan layar gawai wajib dihentikan minimal 30 hingga 60 menit sebelum waktu tidur guna memulihkan sekresi melatonin alami (Chang et al., 2015). "
    "Selain itu, asupan zat psikoaktif kafein wajib dibatasi setidaknya 6 jam sebelum tidur (misalnya maksimal pukul 14.00 WIB untuk jadwal tidur pukul 22.00 WIB) karena waktu paruh metabolisme eliminasi kafein dalam plasma darah manusia berkisar antara 3 hingga 7 jam (Drake et al., 2013). "
    "Penyelarasan parameter gaya hidup digital terhadap ambang batas klinis Sleep Hygiene inilah yang menjadi basis perancangan modul intervensi rekomendasi personal dalam penelitian ini."
)

# ---------------------------------------------------------------------------
# 2.1.2 Pembelajaran Mesin dan Klasifikasi Terawasi
# ---------------------------------------------------------------------------
add_h3(doc, "2.1.2 Pembelajaran Mesin dan Klasifikasi Terawasi")

add_p(doc,
    "Pembelajaran mesin (machine learning) merupakan cabang keilmuan kecerdasan buatan yang berfokus pada pengembangan algoritma komputasional yang mampu mempelajari pola tersembunyi secara langsung dari data historis tanpa diprogram secara kaku (rule-based). "
    "Dalam paradigma klasifikasi terawasi (supervised learning), model diinstruksikan untuk memetakan fungsi aproksimasi matematis f: X → Y yang menghubungkan matriks fitur prediktor independen X dengan vektor label target diskrit Y (Rahman et al., 2025). "
    "Pada penelitian ini, ruang target didefinisikan ke dalam empat tingkatan stratifikasi risiko klinis (K = 4), yaitu Healthy (c = 1), Mild (c = 2), Moderate (c = 3), dan Severe (c = 4). "
    "Keunggulan pendekatan machine learning terletak pada kapabilitasnya dalam menangkap interaksi multivariat non-linier antara metrik fisiologis dan pola perilaku digital yang terlampau rumit jika dianalisis melalui uji statistik univariat tradisional (Kaya, 2025)."
)

add_p(doc,
    "Dalam proses optimasi matematis klasifikasi multi-kelas, model memperbarui parameter bobot internalnya dengan meminimalkan fungsi kerugian Multi-Class Cross-Entropy Loss yang didefinisikan secara formal pada Persamaan (2.1):"
)

add_native_equation_block(
    doc,
    latex_code=r"\mathcal{L}_{\text{Multi-CE}} = - \frac{1}{N} \sum_{i=1}^N \sum_{k=1}^K y_{i,k} \ln(\hat{p}_{i,k})",
    eq_num="Persamaan 2.1",
    param_list=[
        (r"\mathcal{L}_{\text{Multi-CE}}", "nilai fungsi kerugian multi-class cross-entropy;"),
        (r"N", "total jumlah seluruh sampel observasi data (N = 80.000 pada data latih);"),
        (r"K", "jumlah kategori tingkatan kelas risiko target (K = 4: Healthy, Mild, Moderate, Severe);"),
        (r"y_{i,k}", "variabel indikator biner bernilai 1 jika sampel ke-i termasuk ke dalam kelas k, dan 0 jika sebaliknya;"),
        (r"\hat{p}_{i,k}", "estimasi probabilitas prediksi model bahwa sampel observasi ke-i tergolong pada kelas k.")
    ]
)

add_p(doc,
    "Pada domain medis, performa model klasifikasi tidak dapat hanya dinilai berdasarkan metrik akurasi semata, mengingat metrik akurasi sangat rentan memunculkan ilusi performa semu (accuracy paradox) pada populasi data yang mengalami ketimpangan sebaran kelas (class imbalance). "
    "Oleh karena itu, evaluasi diagnostik multi-kelas wajib diuraikan menggunakan metrik evaluasi Recall (sensitivitas deteksi) dan Precision (tingkat keyakinan positif) untuk masing-masing kelas target k, sebagaimana dirumuskan pada Persamaan (2.2) dan Persamaan (2.3):"
)

add_native_equation_block(
    doc,
    latex_code=r"\text{Recall}_k = \frac{\text{TP}_k}{\text{TP}_k + \text{FN}_k}",
    eq_num="Persamaan 2.2",
    param_list=[
        (r"\text{Recall}_k", "sensitivitas model dalam menjaring seluruh kasus aktual pada kelas k (True Positive Rate);"),
        (r"\text{TP}_k", "jumlah sampel kelas k yang diprediksi secara tepat oleh model (True Positive);"),
        (r"\text{FN}_k", "jumlah sampel kelas k yang terlewat dan diprediksi keliru sebagai kelas lain (False Negative).")
    ]
)

add_native_equation_block(
    doc,
    latex_code=r"\text{Precision}_k = \frac{\text{TP}_k}{\text{TP}_k + \text{FP}_k}",
    eq_num="Persamaan 2.3",
    param_list=[
        (r"\text{Precision}_k", "tingkat ketepatan prediksi positif model saat melabeli suatu sampel sebagai kelas k;"),
        (r"\text{TP}_k", "jumlah sampel kelas k yang diprediksi secara tepat (True Positive);"),
        (r"\text{FP}_k", "jumlah sampel dari kelas lain yang secara keliru diprediksi masuk ke dalam kelas k (False Positive).")
    ]
)

add_p(doc,
    "Guna menyatukan trade-off antara presisi dan sensitivitas ke dalam satu nilai kuantitatif agregat yang adil bagi seluruh tingkatan risiko, metrik Macro-averaged F1-Score dihitung dengan merata-ratakan nilai F1-Score harmonik dari setiap kelas tanpa dipengaruhi oleh dominasi kelas mayoritas, sebagaimana dirumuskan pada Persamaan (2.4) (Chicco & Jurman, 2022):"
)

add_native_equation_block(
    doc,
    latex_code=r"\text{Macro-F1} = \frac{1}{K} \sum_{k=1}^K \frac{2 \cdot \text{Precision}_k \cdot \text{Recall}_k}{\text{Precision}_k + \text{Recall}_k}",
    eq_num="Persamaan 2.4",
    param_list=[
        (r"\text{Macro-F1}", "rata-rata harmonik performa klasifikasi di seluruh tingkatan risiko tanpa pembobotan frekuensi;"),
        (r"K", "jumlah total kelas risiko target (K = 4);"),
        (r"\text{Precision}_k", "nilai presisi pada kelas risiko ke-k sesuai Persamaan (2.3);"),
        (r"\text{Recall}_k", "nilai sensitivitas (recall) pada kelas risiko ke-k sesuai Persamaan (2.2).")
    ]
)

# ---------------------------------------------------------------------------
# 2.1.3 Algoritma CatBoost (Categorical Boosting)
# ---------------------------------------------------------------------------
add_h3(doc, "2.1.3 Algoritma CatBoost (Categorical Boosting)")

add_p(doc,
    "CatBoost, singkatan dari Categorical Boosting, merupakan algoritma pembelajaran mesin mutakhir dalam rumpun Gradient Boosted Decision Trees (GBDT) yang dikembangkan oleh Prokhorenkova et al. (2018). "
    "Algoritma ini dirancang secara khusus untuk mengatasi dua kelemahan fundamental yang sering membatasi kinerja pustaka boosting konvensional (seperti XGBoost dan LightGBM), yaitu kerentanan terhadap kebocoran target (target leakage) saat memproses variabel kategorikal dan terjadinya pergeseran distribusi estimasi (prediction shift). "
    "Struktur dasar model pembelajar CatBoost dibangun menggunakan pohon keputusan simetris yang dikenal luas sebagai oblivious trees (Hancock & Khoshgoftaar, 2020). "
    "Pada oblivious trees, predikat aturan pemisahan fitur (feature split) pada setiap tingkat kedalaman pohon diterapkan secara seragam dan identik pada seluruh simpul di tingkat kedalaman yang sama. "
    "Struktur simetris ini bertindak sebagai mekanisme regularisasi struktural alami yang secara efektif membatasi variansi model, mencegah fenomena overfitting pada data pelatihan, serta memungkinkan eksekusi inferensi komputasi berkecepatan tinggi melalui operasi biner bitwise."
)

add_p(doc,
    "Dalam menghadapi tantangan ketimpangan kelas (class imbalance) di mana kelas klinis berisiko tinggi (Severe) hanya mencakup 4,066% dari total populasi, CatBoost menyediakan mekanisme pembelajaran peka biaya (Cost-Sensitive Learning). "
    "Mekanisme ini bekerja dengan mengonfigurasi parameter auto_class_weights='Balanced', yang secara otomatis menghitung faktor pembobotan penalti w_c untuk setiap kelas c berdasarkan rasio terbalik dari frekuensi kemunculannya, sebagaimana dirumuskan pada Persamaan (2.5):"
)

add_native_equation_block(
    doc,
    latex_code=r"w_c = \frac{N}{K \cdot N_c}",
    eq_num="Persamaan 2.5",
    param_list=[
        (r"w_c", "bobot penalti kesalahan klasifikasi untuk kelas target risiko c;"),
        (r"N", "total jumlah seluruh sampel data pelatihan (N = 80.000);"),
        (r"K", "jumlah kategori kelas target (K = 4);"),
        (r"N_c", "frekuensi jumlah sampel observasi yang termasuk ke dalam kelas target c.")
    ]
)

add_p(doc,
    "Melalui formulasi Persamaan (2.5), sampel yang berasal dari kelas minoritas Severe (N_Severe = 3.253 pada data latih) secara otomatis memperoleh bobot penalti w_Severe = 6,1485, sedangkan kelas mayoritas Healthy (N_Healthy = 43.325) memperoleh bobot penalti w_Healthy = 0,4616. "
    "Rasio penalti ini memberikan beban hukuman kerugian 13,32 kali lipat lebih berat terhadap kegagalan mendeteksi pasien berisiko Severe, sehingga mendorong model memprioritaskan sensitivitas klinis tanpa memerlukan manipulasi data sintetis seperti SMOTE yang berisiko merusak manifold distribusi alami data (Wolak et al., 2025)."
)

add_p(doc,
    "Keunggulan paling revolusioner dari CatBoost terletak pada kemampuannya mengolah variabel kategorikal heterogen secara alami (native) tanpa memerlukan prosedur One-Hot Encoding manual. "
    "Pada algoritma konvensional, One-Hot Encoding memecah satu variabel teks menjadi puluhan kolom biner tiruan yang memicu lonjakan dimensi data (curse of dimensionality), meningkatkan beban memori kerja secara drastis, serta memecah pemahaman semantik variabel asli. "
    "Sebaliknya, CatBoost menerapkan teknik transformasi statistik target terurut yang disebut Ordered Target Statistics (OTS). "
    "Pada teknik ini, dataset diacak secara acak melalui fungsi permutasi acak σ = (σ_1, ..., σ_n). "
    "Transformasi nilai kategori x_{σ_p, k} pada baris urutan ke-p menjadi representasi angka kontinu x̂_{σ_p, k} dihitung secara eksklusif hanya berdasarkan akumulasi nilai target dari sampel-sampel yang berada pada urutan sebelumnya (j < p), sebagaimana diformulasikan secara matematis pada Persamaan (2.6) (Prokhorenkova et al., 2018):"
)

add_native_equation_block(
    doc,
    latex_code=r"\hat{x}_{\sigma_p, k} = \frac{\sum_{j=1}^{p-1} \mathbb{I}(x_{\sigma_j, k} = x_{\sigma_p, k}) \cdot y_{\sigma_j} + a \cdot P}{\sum_{j=1}^{p-1} \mathbb{I}(x_{\sigma_j, k} = x_{\sigma_p, k}) + a}",
    eq_num="Persamaan 2.6",
    param_list=[
        (r"\hat{x}_{\sigma_p, k}", "nilai transformasi numerik kontinu dari variabel kategori pada observasi urutan ke-p;"),
        (r"\sigma", "vektor permutasi acak dari indeks observasi dataset pelatihan;"),
        (r"\mathbb{I}(\cdot)", "fungsi indikator bernilai 1 jika kategori sampel historis sama dengan sampel saat ini, dan 0 jika berbeda;"),
        (r"y_{\sigma_j}", "nilai target dari observasi terdahulu pada urutan permutasi (j < p);"),
        (r"P", "nilai prior acuan global, yakni rata-rata nilai target di seluruh dataset pelatihan;"),
        (r"a", "parameter bobot penghalusan prior (smoothing weight, bernilai konstan a = 1).")
    ]
)

add_p(doc,
    "Dalam implementasi praktis perhitungan manual (sebagaimana disimulasikan pada Bab III), formulasi operasional Persamaan (2.6) dapat dinyatakan secara ringkas sebagai rasio antara total target historis ditambah pembobotan prior terhadap frekuensi kemunculan historis:"
)

add_native_equation_block(
    doc,
    latex_code=r"\hat{x}_k = \frac{\sum y_{\text{historis}} + a \cdot P}{\text{Count}_{\text{historis}} + a}",
    eq_num="Persamaan 2.6b",
    param_list=[
        (r"\hat{x}_k", "nilai numerik terproses dari fitur kategori;"),
        (r"\sum y_{\text{historis}}", "akumulasi nilai target pada kemunculan kategori yang sama pada data terdahulu;"),
        (r"\text{Count}_{\text{historis}}", "frekuensi kemunculan kategori serupa terdahulu dalam permutasi data;"),
        (r"P", "prior global rata-rata nilai target;"),
        (r"a", "bobot prioritas penghalusan (a = 1).")
    ]
)

add_p(doc,
    "Pada klasifikasi multi-kelas empat tingkatan risiko (Healthy, Mild, Moderate, Severe), CatBoost menerapkan mekanisme OTS secara paralel dengan skema biner One-vs-All untuk masing-masing kelas target. "
    "Karena kalkulasi statistik pada sampel ke-p sama sekali tidak melibatkan label target dari sampel ke-p itu sendiri maupun sampel sesudahnya, prinsip Ordered Target Statistics sepenuhnya mengeliminasi fenomena kebocoran target (target leakage) dan menghasilkan estimasi fitur kategori yang unbiased (Wu et al., 2025)."
)

add_p(doc,
    "Dalam proses pelatihan berulang (boosting iterations), fungsi kerugian multi-class cross-entropy berbobot penalti kelas diminimalkan melalui pendekatan optimasi gradien. "
    "Fungsi objektif kerugian CatBoost yang dioptimalkan dirumuskan pada Persamaan (2.7):"
)

add_native_equation_block(
    doc,
    latex_code=r"\mathcal{L}_{\text{CatBoost}} = - \frac{1}{N} \sum_{i=1}^N \sum_{c=1}^K w_c \cdot y_{i,c} \cdot \ln \left[ \frac{\exp(F_c(x_i))}{\sum_{j=1}^K \exp(F_j(x_i))} \right]",
    eq_num="Persamaan 2.7",
    param_list=[
        (r"\mathcal{L}_{\text{CatBoost}}", "fungsi kerugian cross-entropy terbobot yang diminimalkan oleh algoritma;"),
        (r"w_c", "bobot penalti kelas cost-sensitive untuk kelas c sesuai Persamaan (2.5);"),
        (r"F_c(x_i)", "skor margin luaran mentah (raw logit margin) model ansambel untuk kelas c pada observasi x_i;"),
        (r"K", "jumlah total tingkatan kelas risiko (K = 4).")
    ]
)

add_p(doc,
    "Pada setiap tahapan boosting ke-t, pohon keputusan baru dilatih untuk memprediksi nilai gradien residual negatif g_{i,c}^t dari fungsi kerugian terhadap skor margin prediksi saat ini, sebagaimana dirumuskan pada Persamaan (2.8):"
)

add_native_equation_block(
    doc,
    latex_code=r"g_{i,c}^t = - \left[ \frac{\partial \mathcal{L}(y_i, F^{t-1}(x_i))}{\partial F_c(x_i)} \right] = w_c \cdot y_{i,c} - \hat{p}_{i,c}^{t-1} \sum_{j=1}^K w_j y_{i,j}",
    eq_num="Persamaan 2.8",
    param_list=[
        (r"g_{i,c}^t", "nilai gradien negatif residual untuk observasi i pada kelas c di iterasi ke-t;"),
        (r"F^{t-1}(x_i)", "skor akumulasi ansambel pohon keputusan hingga iterasi ke-(t-1);"),
        (r"\hat{p}_{i,c}^{t-1}", "estimasi probabilitas softmax kelas c pada iterasi ke-(t-1).")
    ]
)

add_p(doc,
    "Untuk mengatasi pergeseran distribusi prediksi (prediction shift) yang sering dialami oleh algoritma boosting standar, CatBoost menerapkan Ordered Boosting. "
    "Pada mekanisme ini, gradien residual g_{i,c}^t untuk sampel observasi ke-i dihitung menggunakan model bayangan pendukung M_{i-1} yang dilatih secara eksklusif hanya pada subset data sebelum indeks ke-i dalam urutan permutasi. "
    "Setelah struktur cabang pohon oblivious terbentuk, nilai keluaran daun (leaf value) γ_{J, c}^t untuk setiap wilayah simpul daun J dihitung dengan menyertakan parameter regularisasi L2 (l2_leaf_reg = 3) guna mencegah lonjakan bobot ekstrem, sebagaimana dirumuskan pada Persamaan (2.9):"
)

add_native_equation_block(
    doc,
    latex_code=r"\gamma_{J, c}^t = \frac{\sum_{i \in R_J} g_{i,c}^t}{\sum_{i \in R_J} h_{i,c}^t + \lambda}",
    eq_num="Persamaan 2.9",
    param_list=[
        (r"\gamma_{J, c}^t", "nilai penyesuaian bobot prediksi optimal pada daun simetris J untuk kelas c;"),
        (r"R_J", "himpunan sampel observasi data latih yang terpartisi masuk ke dalam daun simetris J;"),
        (r"g_{i,c}^t", "nilai gradien residual orde pertama sesuai Persamaan (2.8);"),
        (r"h_{i,c}^t", "nilai turunan kedua (Hessian matrix) dari fungsi kerugian;"),
        (r"\lambda", "koefisien regularisasi L2 daun (l2_leaf_reg, dikonfigurasi sebesar 3.0).")
    ]
)

add_p(doc,
    "Selanjutnya, skor margin prediksi akhir model ansambel untuk setiap kelas risiko c diakumulasikan secara bertahap dari iterasi t = 1 hingga iterasi maksimum T = 1.000 dengan dikalikan laju pembelajaran (learning rate η = 0,05), sebagaimana dinyatakan pada Persamaan (2.10):"
)

add_native_equation_block(
    doc,
    latex_code=r"F_c^T(x) = F_c^0(x) + \sum_{t=1}^T \eta \cdot h_t(x; \Theta_{t,c})",
    eq_num="Persamaan 2.10",
    param_list=[
        (r"F_c^T(x)", "total skor margin prediksi mentah model ansambel untuk kelas c pada input x;"),
        (r"F_c^0(x)", "skor inisialisasi awal model (bias dasar);"),
        (r"T", "jumlah total iterasi pohon keputusan (iterations = 1.000);"),
        (r"\eta", "laju pembelajaran (learning rate = 0,05);"),
        (r"h_t(x; \Theta_{t,c})", "fungsi prediksi pohon simetris oblivious ke-t dengan parameter struktur Θ_{t,c}.")
    ]
)

# ---------------------------------------------------------------------------
# 2.1.4 Explainable Artificial Intelligence (XAI)
# ---------------------------------------------------------------------------
add_h3(doc, "2.1.4 Explainable Artificial Intelligence (XAI)")

add_p(doc,
    "Meskipun model pembelajaran mesin modern seperti CatBoost mampu mencapai akurasi klasifikasi yang sangat impresif, arsitektur ansambel pohon bertingkat pada hakikatnya beroperasi sebagai kotak hitam (black box) yang sepenuhnya tidak transparan. "
    "Kompleksitas matematis yang melibatkan agregasi seribu pohon keputusan simetris yang berinteraksi secara multivariat menyebabkan tenaga medis tidak dapat menelusuri bagaimana atau mengapa sebuah keputusan klasifikasi dapat terbentuk bagi seorang pasien (Amann et al., 2020). "
    "Dalam praktik pelayanan klinis, ketidaktahuan atas logika inferensi algoritma ini menjadi penghalang terbesar dalam adopsi teknologi kecerdasan buatan, karena dokter secara hukum, etika, dan profesi wajib mempertanggungjawabkan setiap keputusan diagnostik kepada pasien (Sadeghi et al., 2024). "
    "Seorang klinisi tidak dapat merekomendasikan terapi farmakologis atau intervensi perilaku hanya berdasarkan keluaran label kategori risiko tanpa memahami kebiasaan mana yang menjadi pemicu utamanya. "
    "Oleh karena itu, paradigma Explainable Artificial Intelligence (XAI) menjadi kebutuhan mutlak guna membuka tabir kotak hitam komputasi menjadi penjelasan yang rasional, objektif, dan dapat diverifikasi (Hulsen, 2023)."
)

add_p(doc,
    "Dalam taksonomi keilmuan XAI, metode penjelasan model pembelajaran mesin secara umum diklasifikasikan ke dalam dua dimensi interpretasi utama: interpretabilitas global dan interpretabilitas lokal (Srinivasu et al., 2022). "
    "Interpretabilitas global bertujuan untuk memaparkan perilaku model secara agregat pada tingkat populasi data, yakni dengan mengidentifikasi variabel gaya hidup mana saja yang memiliki pengaruh paling dominan terhadap keputusan sistem secara menyeluruh. "
    "Sebaliknya, interpretabilitas lokal berfokus pada penguraian keputusan prediksi untuk satu kasus individu pasien tertentu, dengan merinci kontribusi positif (faktor pemicu risiko) dan kontribusi negatif (faktor pelindung) dari setiap parameter perilaku (Sadeghi et al., 2024). "
    "Di ranah kesehatan personal, penjelasan lokal menjadi komponen yang paling bernilai karena profil kebiasaan digital setiap pasien selalu unik, sehingga perancangan rekomendasi intervensi kebersihan tidur (Sleep Hygiene) dapat ditargetkan tepat sasaran pada variabel yang paling menyimpang."
)

# ---------------------------------------------------------------------------
# 2.1.5 Shapley Additive exPlanations (SHAP) dan Tree-SHAP
# ---------------------------------------------------------------------------
add_h3(doc, "2.1.5 Shapley Additive exPlanations (SHAP) dan Tree-SHAP")

add_p(doc,
    "Metode Shapley Additive exPlanations (SHAP) merupakan pendekatan penjelasan model terpadu yang dirumuskan oleh Lundberg & Lee (2017) berlandaskan teori permainan koalisi (cooperative game theory) karya pemenang Nobel Lloyd Shapley (1953). "
    "Dalam analogi pembelajaran mesin, setiap variabel prediktor input diposisikan layaknya pemain dalam sebuah tim, sedangkan luaran prediksi model diposisikan sebagai hasil kemenangan bersama (payout) yang harus didistribusikan secara adil di antara seluruh pemain. "
    "Nilai Shapley (φ_i) mengukur kontribusi marginal dari suatu variabel ke-i dengan cara menghitung rata-rata tertimbang dari selisih keluaran model ketika variabel tersebut disertakan dan dikeluarkan dari seluruh kemungkinan kombinasi himpunan bagian fitur lainnya. "
    "Formulasi matematis klasik dari nilai Shapley didefinisikan pada Persamaan (2.11):"
)

add_native_equation_block(
    doc,
    latex_code=r"\phi_i(f, x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} [f_x(S \cup \{i\}) - f_x(S)]",
    eq_num="Persamaan 2.11",
    param_list=[
        (r"\phi_i(f, x)", "nilai atribusi kontribusi marginal fitur prediktor ke-i terhadap keputusan model pada instans x;"),
        (r"F", "himpunan seluruh variabel fitur input yang digunakan model (|F| = M = 28 fitur);"),
        (r"S", "himpunan bagian (koalisi) fitur yang tidak memuat fitur ke-i (S ⊆ F \\ {i});"),
        (r"|S|", "kardinalitas atau jumlah anggota fitur dalam koalisi subset S;"),
        (r"|F|!", "total permutasi urutan kemungkinan masuknya seluruh fitur ke dalam koalisi;"),
        (r"f_x(S)", "nilai ekspektasi luaran model saat dievaluasi hanya menggunakan subset fitur S;"),
        (r"[f_x(S \cup \{i\}) - f_x(S)]", "kontribusi marginal penambahan fitur ke-i ke dalam koalisi S.")
    ]
)

add_p(doc,
    "Pendekatan berbasis nilai Shapley memiliki superioritas mutlak dibanding metode eksplanasi lainnya (seperti Feature Importance konvensional atau Permutation Importance) karena nilai Shapley terbukti secara matematis merupakan satu-satunya metode atribusi yang memenuhi empat aksioma fundamental teori permainan koalisi secara simultan (Lundberg & Lee, 2017):"
)

add_p(doc,
    "Jumlah total nilai atribusi kontribusi dari seluruh variabel input beserta nilai dasar ekspektasi global model sama persis dengan nilai luaran prediksi aktual model f(x), sebagaimana dirumuskan pada Persamaan (2.12):",
    bold_prefix="1. Aksioma Efisiensi (Efficiency): "
)

add_native_equation_block(
    doc,
    latex_code=r"\sum_{i=1}^M \phi_i(f, x) = f(x) - \mathbb{E}[f(X)]",
    eq_num="Persamaan 2.12",
    param_list=[
        (r"\sum_{i=1}^M \phi_i", "akumulasi nilai kontribusi marginal seluruh M variabel fitur prediktor (M = 28);"),
        (r"f(x)", "nilai prediksi akhir model untuk observasi x (pada ruang margin logit atau probabilitas);"),
        (r"\mathbb{E}[f(X)]", "nilai dasar acuan ekspektasi global model (base value φ_0) pada populasi data latih.")
    ]
)

add_p(doc,
    "Apabila dua fitur i dan j memberikan kontribusi marginal yang identik pada seluruh kemungkinan koalisi subset fitur S (yakni f_x(S ∪ {i}) = f_x(S ∪ {j}) untuk seluruh S ⊆ F \\ {i, j}), maka nilai atribusi kedua fitur tersebut dipastikan sama besar: φ_i = φ_j.",
    bold_prefix="2. Aksioma Simetri (Symmetry): "
)

add_p(doc,
    "Apabila keberadaan suatu fitur i sama sekali tidak mengubah nilai prediksi model pada koalisi manapun (yakni f_x(S ∪ {i}) = f_x(S) untuk seluruh S ⊆ F \\ {i}), maka nilai atribusi fitur tersebut dijamin bernilai tepat nol: φ_i = 0.",
    bold_prefix="3. Aksioma Dummy / Null Player: "
)

add_p(doc,
    "Apabila suatu model prediksi f terbentuk dari kombinasi linier dua model dasar f = f_1 + f_2, maka nilai kontribusi setiap fitur pada model gabungan adalah penjumlahan nilai kontribusi dari masing-masing model: φ_i(f_1 + f_2) = φ_i(f_1) + φ_i(f_2).",
    bold_prefix="4. Aksioma Aditivitas (Additivity): "
)

add_p(doc,
    "Berdasarkan pemenuhan keempat aksioma tersebut, Lundberg & Lee (2017) merumuskan kerangka kerja model atribusi aditif lokal (Additive Feature Attribution Method) yang menjamin representasi linear yang intuitif bagi pengguna, sebagaimana dinyatakan pada Persamaan (2.13):"
)

add_native_equation_block(
    doc,
    latex_code=r"g(z') = \phi_0 + \sum_{i=1}^M \phi_i \cdot z'_i \quad \Longrightarrow \quad f(x) = \phi_0 + \sum_{i=1}^M \phi_i(x)",
    eq_num="Persamaan 2.13",
    param_list=[
        (r"g(z')", "model penjelasan lokal linear yang mengaproksimasi perilaku model di sekitar instans x;"),
        (r"z' \in \{0, 1\}^M", "vektor biner koalisi fitur (z'_i = 1 jika fitur diobservasi, dan 0 jika tidak ada);"),
        (r"\phi_0", "nilai dasar acuan ekspektasi model saat tidak ada fitur yang diketahui (φ_0 = f_x(∅) = E[f(x)]);"),
        (r"\phi_i(x)", "nilai atribusi kontribusi lokal dari variabel ke-i pada instans pasien x.")
    ]
)

add_p(doc,
    "Kendati nilai Shapley memiliki landasan teoretis yang sangat kokoh, kalkulasi eksak menggunakan formulasi Persamaan (2.11) memiliki kompleksitas waktu eksponensial O(M · 2^M) karena mewajibkan evaluasi seluruh 2^M kemungkinan kombinasi koalisi subset fitur. "
    "Untuk memecahkan hambatan komputasi tersebut, Lundberg et al. (2020) merancang algoritma Tree-SHAP, sebuah algoritma komputasi eksak berkecepatan tinggi yang dioptimalkan secara khusus untuk model berbasis pohon keputusan seperti CatBoost. "
    "Algoritma Tree-SHAP mengeksploitasi struktur topologi pohon secara rekursif dengan merambati jalur keputusan dari simpul akar hingga ke simpul daun dalam waktu polinomial O(T · L · D^2), di mana T adalah jumlah pohon (T = 1.000), L adalah jumlah daun maksimum per pohon, dan D adalah kedalaman pohon (depth D = 6). "
    "Nilai Tree-SHAP untuk setiap pohon ke-t dihitung dengan menjumlahkan kontribusi terbobot dari seluruh simpul daun, sebagaimana dirumuskan pada Persamaan (2.14):"
)

add_native_equation_block(
    doc,
    latex_code=r"\phi_i(f_t, x) = \sum_{j \in \text{Daun}(f_t)} W(j, i, x) \cdot v_j",
    eq_num="Persamaan 2.14",
    param_list=[
        (r"\phi_i(f_t, x)", "atribusi kontribusi fitur ke-i pada pohon keputusan tunggal ke-t;"),
        (r"\text{Daun}(f_t)", "himpunan seluruh simpul daun pada pohon keputusan ke-t;"),
        (r"v_j", "nilai bobot prediksi numerik yang tersimpan pada simpul daun j;"),
        (r"W(j, i, x)", "fungsi bobot proporsional fraksi jalur keputusan yang bergantung pada fitur i sesuai topologi pohon.")
    ]
)

add_p(doc,
    "Pada model klasifikasi multi-kelas CatBoost dengan empat tingkatan risiko target, modul TreeExplainer menghitung nilai atribusi fitur pada ruang margin logit mentah F_c(x). "
    "Guna keperluan interpretasi klinis yang intuitif bagi dokter pada antarmuka sistem pendukung keputusan klinis (CDSS), margin logit terdekomposisi tersebut ditranslasikan ke dalam ruang probabilitas terkalibrasi melalui fungsi Softmax, sebagaimana dirumuskan pada Persamaan (2.15):"
)

add_native_equation_block(
    doc,
    latex_code=r"P(\text{Risiko} = c \mid x) = \frac{\exp\left(\phi_0^{(c)} + \sum_{i=1}^M \phi_i^{(c)}(x)\right)}{\sum_{k=1}^K \exp\left(\phi_0^{(k)} + \sum_{i=1}^M \phi_i^{(k)}(x)\right)}",
    eq_num="Persamaan 2.15",
    param_list=[
        (r"P(\text{Risiko} = c \mid x)", "probabilitas terkalibrasi bahwa pasien x berada pada tingkatan risiko c (0% hingga 100%);"),
        (r"\phi_0^{(c)}", "nilai dasar margin logit ekspektasi untuk kelas c;"),
        (r"\phi_i^{(c)}(x)", "nilai atribusi Tree-SHAP dari fitur prediktor ke-i terhadap kelas risiko c;"),
        (r"K", "jumlah total tingkatan kelas risiko target (K = 4: Healthy, Mild, Moderate, Severe).")
    ]
)

add_p(doc,
    "Untuk melengkapi analisis penjelasan lokal per pasien, kapabilitas interpretabilitas global diekstraksi dengan menghitung nilai kepentingan fitur global (Global Feature Importance). "
    "Nilai kepentingan global I_i dihitung dengan merata-ratakan magnitudo nilai absolut SHAP dari fitur ke-i di seluruh N_test sampel data uji, sebagaimana dirumuskan pada Persamaan (2.16):"
)

add_native_equation_block(
    doc,
    latex_code=r"I_i = \frac{1}{N_{\text{test}}} \sum_{k=1}^{N_{\text{test}}} |\phi_i(x_k)|",
    eq_num="Persamaan 2.16",
    param_list=[
        (r"I_i", "skor kepentingan global variabel ke-i pada populasi data uji;"),
        (r"N_{\text{test}}", "jumlah total sampel data uji yang dievaluasi (N_test = 20.000 sampel);"),
        (r"|\phi_i(x_k)|", "magnitudo nilai kontribusi absolut fitur ke-i pada sampel pasien ke-k.")
    ]
)

add_p(doc,
    "Visualisasi nilai kepentingan global ini disajikan melalui grafik ringkasan lebah (SHAP summary beeswarm plot) yang memetakan sebaran nilai atribusi fitur beserta arah pengaruhnya terhadap risiko klinis pasien (Zhang et al., 2025; Bhattarai et al., 2024)."
)

# ---------------------------------------------------------------------------
# 2.2 HASIL PENELITIAN YANG RELEVAN
# ---------------------------------------------------------------------------
add_h2(doc, "2.2 Hasil Penelitian yang Relevan")

add_p(doc,
    "Kajian mengenai pemanfaatan algoritma pembelajaran mesin untuk klasifikasi gangguan tidur telah berkembang secara signifikan dalam beberapa tahun terakhir. "
    "Taher & Ayon (2024) melakukan evaluasi komparatif terhadap empat algoritma machine learning pada dataset gaya hidup kesehatan tidur, di mana model Gradient Boosting berhasil membukukan nilai akurasi tertinggi mencapai 93,80%. "
    "Penelitian tersebut membuktikan bahwa algoritma berbasis pohon sangat efektif dalam memetakan korelasi antara parameter tidur dengan karakteristik fisik individu. "
    "Kendati demikian, studi tersebut masih memosisikan model sebagai kotak hitam yang tidak mampu menyajikan eksplanasi mengenai faktor risiko dominan yang dialami oleh masing-masing pasien secara spesifik. "
    "Di sisi lain, Lin et al. (2025) mengevaluasi pola tidur pada populasi mahasiswa berskala besar, namun sintesis temuannya masih terbatas pada tataran analisis statistik kelompok dan belum menyentuh personalisasi inferensi klinis."
)

add_p(doc,
    "Upaya menghadirkan transparansi pada model prediksi risiko tidur mulai dieksplorasi oleh sejumlah peneliti melalui integrasi metode Explainable AI. "
    "Ha et al. (2023) menerapkan algoritma XGBoost yang dikombinasikan dengan metode SHAP untuk memprediksi risiko gangguan tidur obstruktif berdasarkan data kuesioner medis, dengan hasil kurva AUROC melampaui angka 0,89. "
    "Meskipun sukses membuktikan kegunaan penjelasan model, metode SHAP pada studi tersebut hanya difungsikan sebatas instrumen penyaring fitur di awal, bukan sebagai media interpretasi interaktif per pasien. "
    "Celah metodologis lain tampak pada studi Xie et al. (2025) yang menerapkan One-Hot Encoding pada XGBoost, di mana prosedur pemecahan kolom kategori terbukti memecah nilai atribusi SHAP ke dalam sub-fitur biner terpisah. "
    "Fragmentasi nilai ini mengaburkan arti semantik variabel asli serta menyulitkan dokter dalam memahami profil risiko pasien."
)

add_p(doc,
    "Untuk menjembatani kesenjangan antara kebutuhan data kategorikal yang utuh dan transparansi inferensi klinis, kombinasi algoritma CatBoost dan SHAP mulai dieksplorasi dalam penelitian medis. "
    "Das et al. (2025) membuktikan keunggulan CatBoost dalam memprediksi insomnia, namun kajian tersebut masih terbatas pada klasifikasi biner pasien komorbid rumah sakit dengan visualisasi SHAP global. "
    "Di ranah onkologi, Srinivasu et al. (2024) mengintegrasikan CatBoost dan SHAP hingga meraih akurasi 99,3% dengan eksplanasi fitur yang jelas. "
    "Validasi keunggulan CatBoost atas data tabular medis juga diperkuat oleh Wolak et al. (2025). "
    "Meskipun demikian, penerapan sinergi CatBoost dan Tree-SHAP belum pernah dieksplorasi secara terpadu pada metrik gaya hidup digital untuk klasifikasi risiko multi-kelas. "
    "Mengisi celah riset inilah yang menjadi posisi kebaruan (novelty) utama penelitian ini, yakni menghadirkan sistem deteksi risiko yang akurat, transparan, dan dapat ditindaklanjuti secara nyata melalui rekomendasi Sleep Hygiene."
)

# Table 2.1 State of the Art
p_tbl_cap = doc.add_paragraph()
p_tbl_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_tbl_cap.paragraph_format.space_before = Pt(12)
p_tbl_cap.paragraph_format.space_after = Pt(6)
r_cap = p_tbl_cap.add_run("Tabel 2.1 Ringkasan Penelitian Terdahulu (State of the Art)")
r_cap.font.name = 'Times New Roman'
r_cap.font.size = Pt(11)
r_cap.font.bold = True

if os.path.exists(SOTA_JSON):
    with open(SOTA_JSON, 'r', encoding='utf-8') as f_sota:
        sota_data = json.load(f_sota)
        
    sota_tbl = doc.add_table(rows=len(sota_data), cols=9)
    sota_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    sota_tbl.autofit = False
    set_table_borders(sota_tbl, color="B0C4DE", sz="4", val="single")
    
    col_w_list = [Inches(0.3), Inches(0.85), Inches(0.95), Inches(0.85), Inches(0.8), Inches(0.65), Inches(0.75), Inches(0.85), Inches(0.9)]
    
    for r_idx, row_vals in enumerate(sota_data):
        row_obj = sota_tbl.rows[r_idx]
        is_hdr = (r_idx == 0)
        
        for c_idx, val in enumerate(row_vals):
            c_obj = row_obj.cells[c_idx]
            if c_idx < len(col_w_list):
                c_obj.width = col_w_list[c_idx]
            c_p = c_obj.paragraphs[0]
            c_p.paragraph_format.line_spacing = 1.05
            c_p.paragraph_format.space_before = Pt(2)
            c_p.paragraph_format.space_after = Pt(2)
            c_p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_hdr or c_idx == 0) else WD_ALIGN_PARAGRAPH.LEFT
            
            display_val = val.replace("Xie et al. (2026)", "Xie et al. (2025)")
            
            r_run = c_p.add_run(display_val)
            r_run.font.name = 'Times New Roman'
            r_run.font.size = Pt(8.5) if is_hdr else Pt(8.0)
            if is_hdr:
                r_run.font.bold = True
                shd = parse_xml(r'<w:shd {} w:fill="F1F5F9"/>'.format(nsdecls('w')))
                c_obj._tc.get_or_add_tcPr().append(shd)

print("Added Table 2.1 State of the Art.")

# ---------------------------------------------------------------------------
# 2.3 KERANGKA BERPIKIR
# ---------------------------------------------------------------------------
add_h2(doc, "2.3 Kerangka Berpikir")

add_p(doc,
    "Kerangka berpikir dalam penelitian ini dibangun secara komprehensif dan runtut guna memecahkan tantangan trade-off klasik antara tuntutan akurasi model komputasi yang tinggi dengan kebutuhan interpretabilitas klinis yang transparan dalam penapisan risiko gangguan tidur. "
    "Titik tolak masalah berakar dari meluasnya fenomena disrupsi tidur di era modern akibat kebiasaan digital yang tidak sehat (seperti tingginya durasi screen time sebelum tidur dan technostress), yang terekam dalam dataset tabular heterogen serta mengalami ketimpangan distribusi kelas yang berat. "
    "Permasalahan ini diselesaikan melalui implementasi algoritma pembelajaran mesin mutakhir CatBoost Classifier yang mengolah fitur kategorikal tanpa One-Hot Encoding via Ordered Target Statistics, serta menerapkan pembobotan biaya kelas (Cost-Sensitive Learning) untuk melindungi kelas minoritas berisiko tinggi (Severe)."
)

add_p(doc,
    "Guna menghilangkan sifat kotak hitam (black box) dari model ansambel CatBoost, lapisan interpretabilitas Explainable AI berbasis algoritma Tree-SHAP diintegrasikan secara terpadu. "
    "Modul Tree-SHAP mengekstraksi nilai kontribusi marginal fitur secara aditif pada tingkat global (summary plot) dan tingkat lokal per pasien (waterfall plot) tanpa mengalami distorsi fragmentasi nilai kategori. "
    "Pada tahap akhir, atribusi fitur personal tersebut ditranslasikan menjadi rekomendasi perilaku klinis berbasis standar kebersihan tidur (Sleep Hygiene), sehingga menghasilkan sebuah purwarupa sistem pendukung keputusan klinis (Clinical Decision Support System / CDSS) berbasis web yang akurat, terpercaya, dan mudah ditindaklanjuti secara nyata oleh tenaga kesehatan maupun masyarakat luas."
)

# Insert Gambar 2.1
if os.path.exists(IMAGE_PATH):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(IMAGE_PATH, width=Inches(6.2))
    
    p_fig_cap = doc.add_paragraph()
    p_fig_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_fig_cap.paragraph_format.space_before = Pt(2)
    p_fig_cap.paragraph_format.space_after = Pt(12)
    r_fig = p_fig_cap.add_run("Gambar 2.1 Bagan Kerangka Berpikir Integrasi CatBoost dan Tree-SHAP untuk Deteksi Risiko Gangguan Tidur")
    r_fig.font.name = 'Times New Roman'
    r_fig.font.size = Pt(11)
    r_fig.font.bold = True
    print("Added Gambar 2.1.")

# ---------------------------------------------------------------------------
# 2.4 PERTANYAAN PENELITIAN
# ---------------------------------------------------------------------------
add_h2(doc, "2.4 Pertanyaan Penelitian")

add_p(doc,
    "Berdasarkan penegasan rumusan masalah dan seluruh kerangka teoretis yang telah diuraikan, maka pertanyaan penelitian operasional yang akan diuji dan dijawab melalui tahapan eksperimen ini dirumuskan secara berpasangan satu-lawan-satu sebagai berikut:\n"
    "1. Bagaimana tingkat kinerja, presisi, dan akurasi klasifikasi algoritma CatBoost dalam mengidentifikasi kategori risiko gangguan tidur pada dataset metrik gaya hidup digital yang mengalami ketidakseimbangan kelas (class imbalance)?\n"
    "2. Bagaimana kapabilitas metode Tree-SHAP dalam mengekstraksi serta menyajikan visualisasi atribusi kontribusi fitur gaya hidup secara utuh tanpa mengalami distorsi fragmentasi nilai kategori?\n"
    "3. Bagaimana rancangan integrasi penjelasan lokal Tree-SHAP dengan pedoman kebersihan tidur (Sleep Hygiene) sehingga mampu menghasilkan rekomendasi intervensi klinis personal yang mudah dipahami dan ditindaklanjuti secara nyata oleh tenaga medis maupun pasien?",
    indent=False
)

# ---------------------------------------------------------------------------
# Save Document
# ---------------------------------------------------------------------------
os.makedirs(OUT_DIR, exist_ok=True)
ALT_TARGET = os.path.join(OUT_DIR, "BAB_2_REVISI_RUMUS_RAPI.docx")
ALT_ROOT = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\BAB_2_REVISI_RUMUS_RAPI.docx"

# Always save to the non-locked new version first
doc.save(ALT_TARGET)
print(f"[SUCCESS] Saved formatted file to: {ALT_TARGET}")

try:
    shutil.copy2(ALT_TARGET, ALT_ROOT)
    print(f"[SUCCESS] Copied to workspace root: {ALT_ROOT}")
except Exception as e:
    print(f"[WARN] Root copy warning: {e}")

# Try overwriting the original BAB 2.docx if user closed it
try:
    doc.save(TARGET_DOCX)
    print(f"[SUCCESS] Saved standalone file to: {TARGET_DOCX}")
except PermissionError:
    print(f"[NOTICE] {TARGET_DOCX} is currently OPEN in Microsoft Word. Saved as {ALT_TARGET} instead.")

try:
    shutil.copy2(ALT_TARGET, ROOT_COPY)
    print(f"[SUCCESS] Copied to workspace root: {ROOT_COPY}")
except PermissionError:
    print(f"[NOTICE] {ROOT_COPY} is currently OPEN in Microsoft Word. Accessible via {ALT_ROOT}.")
except Exception as e:
    print(f"[WARN] Root copy warning: {e}")

try:
    shutil.copy2(ALT_TARGET, PROPOSAL_BAB2_COPY)
    print(f"[SUCCESS] Copied to proposal master folder: {PROPOSAL_BAB2_COPY}")
except PermissionError:
    print(f"[NOTICE] {PROPOSAL_BAB2_COPY} is currently OPEN in Microsoft Word.")
except Exception as e:
    print(f"[WARN] Master folder copy warning: {e}")

