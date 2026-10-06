ref_bab3 = """

---

## DAFTAR PUSTAKA BAB III

Chakik, A., Dahbi, A., & Balouki, Y. (2024). Explainable semi-supervised learning framework for disease prediction using SHAP-based feature selection and cost-sensitive CatBoost. *Journal of Big Data*, 11(1), 1–24. https://doi.org/10.1186/s40537-024-00950-w

Chicco, D., & Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary/multiclass assessment. *BioData Mining*, 13(1), 1–13. https://doi.org/10.1186/s13040-020-00224-4

Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study. *Journal of Medical Internet Research*, 25, e46520. https://doi.org/10.2196/46520

Lundberg, S. M., Erion, G. G., Chen, H., DeGrave, A. J., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S. I. (2020). From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence*, 2(1), 56–67. https://doi.org/10.1038/s42256-019-0138-9

Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. *Advances in Neural Information Processing Systems (NeurIPS)*, 31, 6638–6648.

Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. *Procedia Computer Science*, 181, 526–534. https://doi.org/10.1016/j.procs.2021.01.199

Taher, A., & Ayon, W. I. Z. (2024). Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data. *2024 IEEE PEEIACON*, 1–6. https://doi.org/10.1109/PEEIACON63765.2024.10844781
"""

with open('BAB_3_Draft_Final.md', 'r', encoding='utf-8') as f:
    content = f.read()

if "## DAFTAR PUSTAKA BAB III" not in content:
    with open('BAB_3_Draft_Final.md', 'w', encoding='utf-8') as f:
        f.write(content.strip() + ref_bab3)
    print("[OK] Appended DAFTAR PUSTAKA to BAB_3_Draft_Final.md")
else:
    print("[NOTE] DAFTAR PUSTAKA already exists in BAB_3_Draft_Final.md")
