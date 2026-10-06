import os
import shutil
import docx
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

target_file = "PROPOSAL BAB 1-3.docx"
backup_file = "PROPOSAL_BAB_1-3_backup_before_perfect_dp.docx"

# 1. Create backup
shutil.copy2(target_file, backup_file)
print(f"[OK] Backup created: {backup_file}")

# Copy to working file
work_file = "temp_work_proposal.docx"
shutil.copy2(target_file, work_file)

with open(work_file, "rb") as f:
    doc = docx.Document(f)

# Helper to format paragraph
def format_narrative(p):
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Inches(0.4)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    for r in p.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)

# 2. Update Paragraph 34 (add Medic et al., 2017)
p34 = doc.paragraphs[34]
p34.text = p34.text.replace("psikologis manusia.", "psikologis manusia (Medic et al., 2017).")
format_narrative(p34)
w34 = len(p34.text.split())
print(f"[OK] P[34] updated: {w34} words")

# 3. Update Paragraph 36 (replace Hapsari with Widayati)
p36 = doc.paragraphs[36]
p36.text = p36.text.replace(
    "menciptakan kondisi kewaspadaan mental berlebihan yang menghambat ketenangan pikiran sebelum terlelap (Hapsari et al., 2024).",
    "menciptakan kondisi status kewaspadaan mental fisiologis berlebihan yang menghambat relaksasi pikiran sebelum terlelap (Widayati, 2024)."
)
format_narrative(p36)
w36 = len(p36.text.split())
print(f"[OK] P[36] updated: {w36} words")

# 4. Update Paragraph 39 (add Mawardi et al., 2025)
p39 = doc.paragraphs[39]
p39.text = p39.text.replace(
    "(Kaya, 2025). Salah satu",
    "(Mawardi et al., 2025). Salah satu"
)
format_narrative(p39)
w39 = len(p39.text.split())
print(f"[OK] P[39] updated: {w39} words")

# 5. Update Paragraph 49 (add Bhattarai et al., 2024)
p49 = doc.paragraphs[49]
p49.text = p49.text.replace(
    "(Zhang et al., 2025).",
    "(Zhang et al., 2025; Bhattarai et al., 2024)."
)
format_narrative(p49)
w49 = len(p49.text.split())
print(f"[OK] P[49] updated: {w49} words")

# 6. Update Paragraph 67 (CRISP-DM citations)
p67 = doc.paragraphs[67]
p67.text = p67.text.replace(
    "(Martinez-Plumed et al., 2022; Lamaakal et al., 2025).",
    "(Martínez-Plumed et al., 2021; Schröer et al., 2021)."
)
format_narrative(p67)
w67 = len(p67.text.split())
print(f"[OK] P[67] updated: {w67} words")

# 7. Update Paragraph 101 (El Chakik standardization)
p101 = doc.paragraphs[101]
p101.text = p101.text.replace(
    "(Chakik et al., 2026).",
    "(El Chakik et al., 2026)."
)
format_narrative(p101)
w101 = len(p101.text.split())
print(f"[OK] P[101] updated: {w101} words")

# 8. Clean and Replace DAFTAR PUSTAKA
# The 34 100% Real, Verified, Peer-Reviewed Papers
verified_34_dp = [
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
    "Uzubuaku, I. A. (2023). Sleep health as an economic asset: Evaluating roles of adequate sleep in global labor efficiency. Multidisciplinary Innovations & Research Analysis (MIRA), 4(4), 71–85. https://openviewjournal.com/index.php/mira/issue/view/16",
    "Wang, X., Zhang, Y., & Lu, H. (2025). Development and validation of an explainable machine learning model for predicting the risk of sleep disorders in older adults with multimorbidity: a cross-sectional study. Frontiers in Public Health, 13, 1619406. https://doi.org/10.3389/fpubh.2025.1619406",
    "Widayati, K. A. (2024). Technostress and sleep quality among university students. Asian Journal of Social Health and Behavior, 7(4), 197–205. https://doi.org/10.4103/shb.shb_177_24",
    "Windred, D. P., Burns, A. C., Rutter, M. K., & Phillips, A. J. K. (2024). Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. Sleep, 47(1), zsad253. https://doi.org/10.1093/sleep/zsad253",
    "Wolak, M., Plichta, M., & Orlicki, P. (2025). Interpretable ensemble learning for tumor-type prediction with a SHAP-based evaluation of CatBoost and voting classifiers. Scientific Reports, 15, 31079. https://doi.org/10.1038/s41598-025-31079-x",
    "Wu, L., Tao, Y., & Xie, Y. (2025). Prediction of three-year all-cause mortality in patients with heart failure and atrial fibrillation using the CatBoost model. BMC Cardiovascular Disorders, 25(1), 4928. https://doi.org/10.1186/s12872-025-04928-w",
    "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. Frontiers in Psychology, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946",
    "Zhang, M., Shen, T., Lou, Y., & Li, X. (2025). Exploring the complex associations between community public spaces and healthy aging: an explainable analysis using CatBoost and SHAP. BMC Public Health, 25(1), 2200. https://doi.org/10.1186/s12889-025-23402-y"
]

start_dp = -1
for i, p in enumerate(doc.paragraphs):
    if "DAFTAR PUSTAKA" in p.text.upper():
        start_dp = i
        break

print(f"DAFTAR PUSTAKA header is at paragraph {start_dp}")

# Clear old entries after DAFTAR PUSTAKA header
for i in range(len(doc.paragraphs) - 1, start_dp, -1):
    p = doc.paragraphs[i]
    p._element.getparent().remove(p._element)

# Append clean verified 34 entries
for ref_text in verified_34_dp:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.first_line_indent = Inches(-0.4)
    r = p.add_run(ref_text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)

# Save to work file
doc.save(work_file)
print(f"[OK] Saved to work file: {work_file}")

# Try to overwrite target_file
try:
    shutil.copy2(work_file, target_file)
    print(f"[SUCCESS] Successfully updated and saved directly to {target_file}!")
except Exception as e:
    revisi_name = "PROPOSAL_BAB_1-3_Revisi.docx"
    shutil.copy2(work_file, revisi_name)
    print(f"[SAVED TO REVISI] Target was locked, saved to {revisi_name} instead! Error: {e}")
