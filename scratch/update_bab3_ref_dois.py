import re

with open('BAB_3_Draft_Final.md', 'r', encoding='utf-8') as f:
    text = f.read()

new_ref = """## DAFTAR PUSTAKA BAB III

Chicco, D., & Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary/multiclass assessment. *BioData Mining*, 13(1), 6. https://doi.org/10.1186/s13040-020-00224-4

Chicco, D., & Jurman, G. (2022). An invitation to greater use of Matthews correlation coefficient in robotics and artificial intelligence. *Frontiers in Robotics and AI*, 9, 876814. https://doi.org/10.3389/frobt.2022.876814

El Chakik, A., Nakhal, B., & Nassreddine, G. (2026). Explainable semi-supervised learning framework for Alzheimer’s disease prediction using SHAP-based feature selection and cost-sensitive CatBoost. *Sci*, 8(3), 171. https://doi.org/10.3390/sci8070171

Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study. *Journal of Medical Internet Research*, 25, e46520. https://doi.org/10.2196/46520

Lundberg, S. M., Erion, G. G., Chen, H., DeGrave, A. J., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S. I. (2020). From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence*, 2(1), 56–67. https://doi.org/10.1038/s42256-019-0138-9

Martínez-Plumed, F., Contreras-Ochando, L., Ferri, C., Hernández-Orallo, J., Kull, M., Lachiche, N., Ramírez-Quintana, M. J., & Flach, P. A. (2021). CRISP-DM twenty years later: From data mining processes to data science trajectories. *IEEE Transactions on Knowledge and Data Engineering*, 33(8), 3048–3061. https://doi.org/10.1109/TKDE.2019.2962680

Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. *Advances in Neural Information Processing Systems (NeurIPS)*, 31, 6638–6648. https://doi.org/10.48550/arXiv.1706.09516

Taher, A., & Ayon, W. I. Z. (2024). Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data. *2024 IEEE PEEIACON*, 1–6. https://doi.org/10.1109/PEEIACON63765.2024.10844781
"""

# Replace the DAFTAR PUSTAKA section
pattern = r'## DAFTAR PUSTAKA BAB III.*'
text_updated = re.sub(pattern, new_ref.strip(), text, flags=re.DOTALL)

with open('BAB_3_Draft_Final.md', 'w', encoding='utf-8') as f:
    f.write(text_updated.strip() + '\n')

print("[OK] Updated DAFTAR PUSTAKA BAB III in BAB_3_Draft_Final.md")
