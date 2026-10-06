import sys
import os
import shutil
import docx
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)

src_file = os.path.join(parent_dir, "temp_work_proposal.docx")
doc = docx.Document(src_file)

print(f"Loaded: {src_file}")
print(f"Paragraphs: {len(doc.paragraphs)}, Tables: {len(doc.tables)}")

def format_narrative(p):
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Inches(0.4)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    for r in p.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)

def format_caption(p):
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Inches(0)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(4)
    for r in p.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.bold = True

def format_table_note(p):
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Inches(0)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(6)
    for r in p.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.italic = True

# --- 1. Modify P[17] (Tujuan Penelitian) ---
p17 = doc.paragraphs[17]
p17.text = (
    "\tMengacu pada rumusan masalah yang telah ditetapkan, tujuan dari penelitian ini adalah untuk "
    "menerapkan dan mengevaluasi metode Explainable AI (XAI) berbasis Shapley Additive exPlanations (SHAP) "
    "pada algoritma klasifikasi CatBoost. Penelitian ini bertujuan membangun sebuah model penapisan risiko "
    "gangguan tidur yang teruji kinerjanya secara objektif melalui metrik evaluasi multi-kelas, serta mampu "
    "memberikan interpretasi yang transparan, logis, dan personal mengenai besaran kontribusi setiap variabel "
    "metrik gaya hidup digital sebagai faktor risiko utama."
)
format_narrative(p17)
print(f"[OK] P[17] Tujuan: {len(p17.text.split())} words")

# --- 2. Modify P[38] (Bab 2 P[81] - eliminate diagnosis) ---
p38 = doc.paragraphs[38]
p38.text = p38.text.replace(
    "otomatisasi diagnosis prediktif modern.",
    "otomatisasi penapisan risiko prediktif modern."
)
format_narrative(p38)
print(f"[OK] P[38] Bab 2: {len(p38.text.split())} words")

# --- 3. Modify P[67] (Bab 3 CRISP-DM encoding fix) ---
p67 = doc.paragraphs[67]
p67.text = (
    "Pendekatan penelitian yang digunakan dalam skripsi ini mengadopsi kerangka kerja standar industri CRISP-DM "
    "(Cross-Industry Standard Process for Data Mining). Kerangka kerja ini dipilih secara khusus karena menyediakan "
    "metodologi yang sangat sistematis, terstruktur, dan bersifat iteratif untuk memandu seluruh siklus pengembangan "
    "proyek penambangan data dan pembelajaran mesin. Standar CRISP-DM terdiri atas enam tahapan utama yang saling "
    "berkesinambungan, yaitu pemahaman kebutuhan masalah (business understanding), pemahaman data awal (data understanding), "
    "persiapan data (data preparation), pemodelan algoritma (modeling), evaluasi performa model (evaluation), serta "
    "penyebaran hasil temuan (deployment). Penerapan metodologi komprehensif ini menjamin setiap tahapan teknis "
    "terhubung secara konsisten dengan tujuan klinis, sehingga proses rekayasa fitur dan pelatihan model CatBoost dapat "
    "berjalan selaras dengan kebutuhan eksplanasi faktor risiko menggunakan metode XAI-SHAP (Martínez-Plumed et al., 2021; Schröer et al., 2021)."
)
format_narrative(p67)
print(f"[OK] P[67] Bab 3 CRISP-DM: {len(p67.text.split())} words")

# --- 4. Modify P[80] (Sub-bab 3.3.2 Sampel Penelitian) ---
p80 = doc.paragraphs[80]
p80.text = (
    "Sampel penelitian yang digunakan diambil melalui teknik purposive sampling dengan menetapkan kriteria kelengkapan "
    "atribut metrik gaya hidup digital dan rekaman fisiologis tidur secara terstruktur. Berdasarkan kriteria inklusi "
    "tersebut, sampel yang dianalisis berupa Sleep Health & Daily Performance Dataset karya Mohan Krishna Thalla (2026) "
    "dari repositori publik Kaggle dengan jumlah 100.000 rekaman dan 32 atribut fitur. Dataset ini merupakan data sekunder "
    "terbuka berbasis pemodelan sintetis terkalibrasi secara epidemiologis, sehingga bebas dari kewajiban izin etik medis "
    "langsung namun memiliki validitas statistik representatif. Struktur data mencakup 7 fitur kategorikal seperti profesi "
    "dan kondisi kesehatan mental, serta 24 fitur numerik seperti durasi layar gawai dan stres harian. Seluruh sampel "
    "memiliki variabel target dependen sleep_disorder_risk empat tingkatan risiko: Healthy, Mild, Moderate, dan Severe, "
    "yang sangat ideal untuk melatih model klasifikasi multi-kelas."
)
format_narrative(p80)
print(f"[OK] P[80] Sampel: {len(p80.text.split())} words")

# --- 5. Modify P[90] (Sub-bab 3.5 Teknik Pengumpulan Data) ---
p90 = doc.paragraphs[90]
p90.text = (
    "Teknik pengumpulan data dalam penelitian ini dilakukan melalui dua metode utama, yaitu studi dokumentasi dataset "
    "sekunder dan studi kepustakaan ilmiah. Pengumpulan data sekunder dilakukan dengan mengunduh Sleep Health & Daily "
    "Performance Dataset karya Mohan Krishna Thalla (2026) secara resmi dari platform repositori data terbuka Kaggle "
    "dalam format berkas comma-separated values (.csv). Setelah berkas diunduh, dilakukan pemeriksaan integritas data "
    "digital guna memastikan tidak ada kerusakan data dan memastikan kelengkapan nilai tanpa data hilang pada 100.000 "
    "rekaman. Sementara itu, studi kepustakaan dilakukan dengan menelaah buku panduan skripsi, artikel jurnal internasional "
    "bereputasi, serta dokumentasi teknis pustaka algoritma. Telaah literatur ini bertujuan memperoleh landasan teoretis "
    "yang kuat terkait formulasi matematis CatBoost, prinsip keadilan nilai Shapley dalam metode XAI-SHAP, serta relevansi "
    "klinis dari parameter gaya hidup digital terhadap gangguan tidur."
)
format_narrative(p90)
print(f"[OK] P[90] Pengumpulan Data: {len(p90.text.split())} words")

# --- 6. Modify P[114] (Sub-bab 3.6.5 Toy Example: Metrik Evaluasi) ---
p114 = doc.paragraphs[114]
p114.text = (
    "Simulasi perhitungan manual ketiga mencakup validasi formula metrik evaluasi klasifikasi dari matriks kebingungan "
    "empat kali empat hasil pengujian awal serta pembuktian sifat aditivitas lokal metode XAI-SHAP. Berdasarkan rekapitulasi "
    "simulasi data uji sebanyak dua puluh ribu rekaman, perhitungan manual membuktikan bahwa formula Recall kelas Severe "
    "sebesar 89,05% dan Macro-averaged F1-Score sebesar 89,25% selaras sempurna dengan luaran pustaka Scikit-Learn. "
    "Sementara itu, pembuktian aksioma efisiensi metode SHAP pada satu sampel profil pasien menunjukkan bahwa penjumlahan "
    "nilai dasar sebesar 0,120 dengan akumulasi nilai kontribusi seluruh variabel gaya hidup sebesar 0,828 menghasilkan "
    "angka nilai probabilitas sebesar 0,948. Nilai tersebut terbukti sama persis dengan probabilitas akhir klasifikasi "
    "yang diprediksi oleh CatBoost, sehingga membuktikan secara nyata bahwa seluruh kontribusi marginal SHAP bersifat "
    "aditif, adil, konsisten, dan dapat dipertanggungjawabkan keabsahan matematisnya dalam ranah kesehatan."
)
format_narrative(p114)
print(f"[OK] P[114] Simulasi Evaluasi: {len(p114.text.split())} words")

# --- 7. Modify P[134] (Sub-bab 3.6.7 Deployment - eliminate diagnostik) ---
p134 = doc.paragraphs[134]
p134.text = p134.text.replace(
    "Informasi diagnostik yang transparan ini",
    "Informasi stratifikasi risiko yang transparan ini"
)
format_narrative(p134)
print(f"[OK] P[134] Deployment: {len(p134.text.split())} words")

# --- 8. Renumber Figures & Tables Captions ---
# P[116]: Gambar 3.5 -> Gambar 3.2
p116 = doc.paragraphs[116]
p116.text = "Gambar 3.2 Diagram Alir Simulasi Perhitungan Matematis Manual (Toy Example Workflow) pada Algoritma CatBoost dan XAI-SHAP"
format_caption(p116)
print(f"[OK] P[116] Figure caption updated to Gambar 3.2")

# P[118]: Gambar 3.6 -> Gambar 3.3
p118 = doc.paragraphs[118]
p118.text = "Gambar 3.3 Visualisasi Bobot Penalti Kelas dan Simulasi Matriks Kebingungan (Confusion Matrix) 4x4"
format_caption(p118)
print(f"[OK] P[118] Figure caption updated to Gambar 3.3")

# P[119]: Tabel 3.9 title update
p119 = doc.paragraphs[119]
p119.text = "Tabel 3.9 Simulasi Matriks Kebingungan 4x4 (Data Uji Awal) dan Pembuktian Manual Formula Metrik Evaluasi"
format_caption(p119)
print(f"[OK] P[119] Table caption updated to Tabel 3.9")

# P[132]: Gambar 3.2 -> Gambar 3.4
p132 = doc.paragraphs[132]
p132.text = "Gambar 3.4 Alur Komputasi dan Interpretasi XAI Tree-SHAP"
format_caption(p132)
print(f"[OK] P[132] Figure caption updated to Gambar 3.4")

# P[136]: Gambar 3.3 -> Gambar 3.5
p136 = doc.paragraphs[136]
p136.text = "Gambar 3.5 Mockup Antarmuka Prototipe Web CDSS Analisis Gangguan Tidur Berbasis CatBoost-SHAP"
format_caption(p136)
print(f"[OK] P[136] Figure caption updated to Gambar 3.5")

# --- 9. Remove duplicate table caption P[127] ---
p127 = doc.paragraphs[127]
if "Tabel 3.7" in p127.text and "Struktur Matriks Kebingungan" in p127.text:
    p127._element.getparent().remove(p127._element)
    print(f"[OK] Removed duplicate table title at P[127]")

# --- 10. Re-build DAFTAR PUSTAKA with Thalla (2026) added ---
# Find DAFTAR PUSTAKA header
dp_header = -1
for i, p in enumerate(doc.paragraphs):
    if "DAFTAR PUSTAKA" in p.text.upper():
        dp_header = i
        break

print(f"DAFTAR PUSTAKA header at index: {dp_header}")

# Current 34 papers + Thalla 2026 = 35 verified entries
verified_35_dp = [
    "Amann, J., Blasimme, A., Vayena, E., Frey, D., & Madai, V. I. (2020). Explainability for artificial intelligence in healthcare: a multidisciplinary perspective. BMC Medical Informatics and Decision Making, 20(1), 310. https://doi.org/10.1186/s12911-020-01332-6",
    "Bhattarai, P., Thakuri, D. S., Nie, Y., & Chand, G. B. (2024). Explainable AI-based Deep-SHAP for mapping the multivariate relationships between regional neuroimaging biomarkers and cognition. European Journal of Radiology, 174, 111403. https://doi.org/10.1016/j.ejrad.2024.111403",
    "Chicco, D., & Jurman, G. (2022). An invitation to greater use of Matthews correlation coefficient in robotics and artificial intelligence. Frontiers in Robotics and AI, 9, 876814. https://doi.org/10.3389/frobt.2022.876814",
    "Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025). Prevalence and factors associated with insomnia among chronic disease patients in Bangladesh: A machine learning study. Nature and Science of Sleep, 17, 2725–2741. https://doi.org/10.2147/NSS.S547335",
    "Deivendran, S., Kanagaraj, K., & Leelabai, T. (2025). Impact of excessive screen time on sleep quality and sleep disturbances among young adults: A cross-sectional study. Journal of Pharmacy and Bioallied Sciences, 17(Suppl 1), S944–S947. https://doi.org/10.4103/jpbs.jpbs_944_25",
    "El Chakik, A., Nakhal, B., & Nassreddine, G. (2026). Explainable semi-supervised learning framework for Alzheimer’s disease prediction using SHAP-based feature selection and cost-sensitive CatBoost. Sci, 8(7), 171. https://doi.org/10.3390/sci8070171",
    "Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study. Journal of Medical Internet Research, 25, e46520. https://doi.org/10.2196/46520",
    "Hancock, J. T., & Khoshgoftaar, T. M. (2020). CatBoost for big data: an interdisciplinary review. Journal of Big Data, 7(1), 94. https://doi.org/10.1186/s40537-020-00369-8",
    "Henrich, L. C., Antypa, N., & Van den Berg, J. F. (2021). Sleep quality in students: Associations with psychological and lifestyle factors. Current Psychology, 41, 4221–4230. https://doi.org/10.1007/s12144-021-01801-9",
    "Hulsen, T. (2023). Explainable artificial intelligence (XAI): Concepts and challenges in healthcare. AI, 4(3), 652–666. https://doi.org/10.3390/ai4030034",
    "Jahrami, H. (2023). The relationship between Nomophobia, insomnia, Chronotype, phone in proximity, screen time, and sleep duration in adults: A mobile phone app-assisted cross-sectional study. Healthcare, 11(10), 1503. https://doi.org/10.3390/healthcare11101503",
    "Kaya, C. (2025). Comparative analysis of conventional and ensemble machine learning techniques for sleep disorder classification. Journal of Artificial Intelligence and Data Science (JAIDA), 5(2), 132–139. https://dergipark.org.tr/en/pub/jaida/issue/87774/1825274",
    "Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L. (2025). Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. Frontiers in Psychiatry, 16, 1533875. https://doi.org/10.3389/fpsyt.2025.1533875",
    "Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 4765–4774. https://doi.org/10.48550/arXiv.1705.07874",
    "Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S. I. (2020). From local explanations to global understanding with explainable AI for trees. Nature Machine Intelligence, 2(1), 56–67. https://doi.org/10.1038/s42256-019-0138-9",
    "Martínez-Plumed, F., Contreras-Ochando, L., Ferri, C., Hernandez-Orallo, J., Kull, M., Lachiche, N., & Flach, P. (2021). CRISP-DM twenty years later: From data mining processes to data science trajectories. IEEE Transactions on Knowledge and Data Engineering, 33(8), 3048–3061. https://doi.org/10.1109/TKDE.2019.2962680",
    "Mawardi, A. B., Pradini, R. S., & Haris, M. S. (2025). Komparasi algoritma boosting untuk prediksi gangguan tidur. JITET (Jurnal Informatika dan Teknik Elektro Terapan), 13(3), 1377–1385. https://doi.org/10.23960/jitet.v13i3.7281",
    "Medic, G., Wille, M., & Hemels, M. E. (2017). Short- and long-term health consequences of sleep disruption. Nature and Science of Sleep, 9, 151–161. https://doi.org/10.2147/NSS.S134864",
    "Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. Advances in Neural Information Processing Systems (NeurIPS 2018), 31, 6638–6648. https://doi.org/10.48550/arXiv.1706.09516",
    "Putra, J. L., & Hidayat, W. F. (2024). Prediksi kualitas tidur: Pendekatan machine learning yang mengintegrasikan faktor kesehatan dan lingkungan. Computer Science (CO-SCIENCE), 4(2), 157–162. https://doi.org/10.31294/coscience.v4i2.4737",
    "Rahman, M. A., Jahan, I., Islam, M., Jabid, T., Ali, M. S., Rashid, M. R. A., Islam, M. M., Ferdaus, M. H., Rasel, M. M. K., Jahan, M. R., Sharmin, S., Rimi, T. A., Talukder, A. S., Matin, M. M. H., & Ali, M. A. (2025). Improving sleep disorder diagnosis through optimized machine learning approaches. IEEE Access, 13, 22051–22070. https://doi.org/10.1109/ACCESS.2025.3535535",
    "Sadeghi, Z., Alizadehsani, R., & Cifci, M. A. (2024). A review of Explainable Artificial Intelligence in healthcare. Computers and Electrical Engineering, 118, 109370. https://doi.org/10.1016/j.compeleceng.2024.109370",
    "Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. Procedia Computer Science, 181, 526–534. https://doi.org/10.1016/j.procs.2021.01.199",
    "Srinivasu, P. N., Sandhya, N., Jhaveri, R. H., & Raut, R. (2022). From Blackbox to Explainable AI in Healthcare: Existing Tools and Case Studies. Mobile Information Systems, 2022, 8167821. https://doi.org/10.1155/2022/8167821",
    "Srinivasu, P. N., Shafi, J., Arif, M., Debtera, B., & Gudi, A. (2024). XAI-driven CatBoost multi-layer perceptron neural network for analyzing breast cancer. Scientific Reports, 14, 28674. https://doi.org/10.1038/s41598-024-79620-8",
    "Taher, A., & Ayon, W. I. Z. (2024). Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data. 2024 IEEE PEEIACON, 1–6. https://doi.org/10.1109/PEEIACON63629.2024.10800593",
    "Thalla, M. K. (2026). Sleep Health & Daily Performance Dataset (Version 1) [Data set]. Kaggle. https://www.kaggle.com/datasets/mohankrishnat/sleep-health-and-daily-performance-dataset",
    "Uzubuaku, I. A. (2023). Sleep health as an economic asset: Evaluating roles of adequate sleep in global labor efficiency. Multidisciplinary Innovations & Research Analysis (MIRA), 4(4), 71–85. https://openviewjournal.com/index.php/mira/issue/view/16",
    "Wang, X., Zhang, Y., & Lu, H. (2025). Development and validation of an explainable machine learning model for predicting the risk of sleep disorders in older adults with multimorbidity: a cross-sectional study. Frontiers in Public Health, 13, 1619406. https://doi.org/10.3389/fpubh.2025.1619406",
    "Widayati, K. A. (2024). Technostress and sleep quality among university students. Asian Journal of Social Health and Behavior, 7(4), 197–205. https://doi.org/10.4103/shb.shb_177_24",
    "Windred, D. P., Burns, A. C., Rutter, M. K., & Phillips, A. J. K. (2024). Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. Sleep, 47(1), zsad253. https://doi.org/10.1093/sleep/zsad253",
    "Wolak, M., Plichta, M., & Orlicki, P. (2025). Interpretable ensemble learning for tumor-type prediction with a SHAP-based evaluation of CatBoost and voting classifiers. Scientific Reports, 15, 31079. https://doi.org/10.1038/s41598-025-31079-x",
    "Wu, L., Tao, Y., & Xie, Y. (2025). Prediction of three-year all-cause mortality in patients with heart failure and atrial fibrillation using the CatBoost model. BMC Cardiovascular Disorders, 25(1), 4928. https://doi.org/10.1186/s12872-025-04928-w",
    "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. Frontiers in Psychology, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946",
    "Zhang, M., Shen, T., Lou, Y., & Li, X. (2025). Exploring the complex associations between community public spaces and healthy aging: an explainable analysis using CatBoost and SHAP. BMC Public Health, 25(1), 2200. https://doi.org/10.1186/s12889-025-23402-y"
]

# Remove old DP entries
for i in range(len(doc.paragraphs) - 1, dp_header, -1):
    p = doc.paragraphs[i]
    p._element.getparent().remove(p._element)

# Add verified 35 entries
for ref_text in verified_35_dp:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.first_line_indent = Inches(-0.4)
    r = p.add_run(ref_text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

print(f"[OK] DAFTAR PUSTAKA refreshed with {len(verified_35_dp)} entries (34 peer-reviewed journals + 1 official Kaggle dataset).")

# Save to temp_work_proposal.docx
doc.save(src_file)
print(f"[OK] Saved to: {src_file}")

# Sync to PROPOSAL BAB 1-3.docx and PROPOSAL_BAB_1-3_Revisi.docx
master_doc = os.path.join(parent_dir, "PROPOSAL BAB 1-3.docx")
revisi_doc = os.path.join(parent_dir, "PROPOSAL_BAB_1-3_Revisi.docx")

shutil.copy2(src_file, revisi_doc)
print(f"[SUCCESS] Copied to: {revisi_doc}")

try:
    shutil.copy2(src_file, master_doc)
    print(f"[SUCCESS] Copied to: {master_doc}")
except Exception as e:
    print(f"[WARNING] Could not overwrite {master_doc} directly: {e}")
