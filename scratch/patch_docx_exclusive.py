with open('scratch/generate_bab3_docx.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re

new_refs_block = """    # Daftar Pustaka Bab 3 (Jurnal Eksklusif Metodologi)
    add_heading_2("DAFTAR PUSTAKA BAB III")
    refs_bab3 = [
        "Chicco, D., & Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. BMC Genomics, 21, 6. https://doi.org/10.1186/s12864-019-6413-7",
        "Chicco, D., & Jurman, G. (2022). An invitation to greater use of Matthews correlation coefficient in robotics and artificial intelligence. Frontiers in Robotics and AI, 9, 876814. https://doi.org/10.3389/frobt.2022.876814",
        "El Chakik, A., Nakhal, B., & Nassreddine, G. (2026). Explainable semi-supervised learning framework for Alzheimer’s disease prediction using SHAP-based feature selection and cost-sensitive CatBoost. Sci, 8(3), 171. https://doi.org/10.3390/sci8070171",
        "Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585(7825), 357–362. https://doi.org/10.1038/s41586-020-2649-2",
        "Martínez-Plumed, F., Contreras-Ochando, L., Ferri, C., Hernández-Orallo, J., Kull, M., Lachiche, N., Ramírez-Quintana, M. J., & Flach, P. A. (2021). CRISP-DM twenty years later: From data mining processes to data science trajectories. IEEE Transactions on Knowledge and Data Engineering, 33(8), 3048–3061. https://doi.org/10.1109/TKDE.2019.2962680",
        "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html",
        "Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. Procedia Computer Science, 181, 526–534. https://doi.org/10.1016/j.procs.2021.01.199"
    ]"""

pattern = r'    # Daftar Pustaka Bab 3.*?refs_bab3 = \[.*?\]'
code_updated = re.sub(pattern, new_refs_block, code, flags=re.DOTALL)

with open('scratch/generate_bab3_docx.py', 'w', encoding='utf-8') as f:
    f.write(code_updated)

print("[OK] Updated generate_bab3_docx.py")
