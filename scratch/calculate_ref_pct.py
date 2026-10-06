# Master list of all journals used across Bab 1, Bab 2, and Bab 3

references = [
    # BAB 1 & SOTA
    {"authors": "Chen et al.", "year": 2024, "chapter": "Bab 1, 2", "title": "Influencing factors associated with sleep quality in undergraduates", "journal": "Frontiers in Public Health"},
    {"authors": "Das et al.", "year": 2025, "chapter": "Bab 1, 2", "title": "Prevalence and factors associated with insomnia among chronic disease patients", "journal": "Nature and Science of Sleep"},
    {"authors": "Ha et al.", "year": 2023, "chapter": "Bab 1, 2, 3", "title": "Predicting the risk of sleep disorders using a machine learning-based simple questionnaire", "journal": "Journal of Medical Internet Research"},
    {"authors": "Lin et al.", "year": 2025, "chapter": "Bab 1, 2", "title": "Evaluation of sleep quality and influencing factors using machine learning", "journal": "Frontiers in Psychiatry"},
    {"authors": "Lundberg & Lee", "year": 2017, "chapter": "Bab 1, 2", "title": "A unified approach to interpreting model predictions", "journal": "NeurIPS (Seminal SHAP)"},
    {"authors": "Taher & Ayon", "year": 2024, "chapter": "Bab 1, 2, 3", "title": "Exploring sleep disorders: A comparative analysis of ML algorithms", "journal": "IEEE PEEIACON"},

    # BAB 2 Tambahan
    {"authors": "Loh et al.", "year": 2024, "chapter": "Bab 2", "title": "A review of Explainable Artificial Intelligence in healthcare", "journal": "Computers and Electrical Engineering"},
    {"authors": "Hancock & Khoshgoftaar", "year": 2020, "chapter": "Bab 2", "title": "CatBoost for big data: an interdisciplinary review", "journal": "Journal of Big Data"},
    {"authors": "Li et al.", "year": 2025, "chapter": "Bab 2", "title": "Associations between community public spaces and healthy aging using CatBoost and SHAP", "journal": "BMC Public Health"},
    {"authors": "Lundberg et al.", "year": 2020, "chapter": "Bab 2, 3", "title": "From local explanations to global understanding with explainable AI for trees", "journal": "Nature Machine Intelligence"},
    {"authors": "Kumar et al.", "year": 2025, "chapter": "Bab 2", "title": "Impact of excessive screen time on sleep quality and sleep duration", "journal": "Journal of Pharmacy and Bioallied Sciences"},
    {"authors": "Alqudah et al.", "year": 2026, "chapter": "Bab 2", "title": "Interpretable ensemble learning for tumor-type prediction with CatBoost", "journal": "Scientific Reports"},
    {"authors": "Wang et al.", "year": 2025, "chapter": "Bab 2", "title": "Prediction of all-cause mortality using the CatBoost model", "journal": "BMC Cardiovascular Disorders"},
    {"authors": "Widayati", "year": 2024, "chapter": "Bab 1, 2", "title": "Technostress and sleep quality among university students", "journal": "Asian Journal of Social Health and Behavior"},
    {"authors": "Srinivasu et al.", "year": 2024, "chapter": "Bab 1, 2", "title": "XAI-driven CatBoost multi-layer perceptron neural network", "journal": "Scientific Reports"},

    # BAB 3 Tambahan
    {"authors": "Martínez-Plumed et al.", "year": 2021, "chapter": "Bab 3", "title": "CRISP-DM Twenty Years Later", "journal": "IEEE TKDE"},
    {"authors": "Schröer, Kruse, & Gómez", "year": 2021, "chapter": "Bab 3", "title": "A systematic literature review on applying CRISP-DM process model", "journal": "Procedia Computer Science"},
    {"authors": "El Chakik, Nakhal, & Nassreddine", "year": 2026, "chapter": "Bab 3", "title": "Explainable Semi-Supervised Learning Framework Using Cost-Sensitive CatBoost", "journal": "Sci (MDPI)"},
    {"authors": "Chicco & Jurman", "year": 2020, "chapter": "Bab 3", "title": "The advantages of the Matthews correlation coefficient over F1 score and accuracy", "journal": "BMC Genomics"},
    {"authors": "Chicco & Jurman", "year": 2022, "chapter": "Bab 3", "title": "An Invitation to Greater Use of Matthews Correlation Coefficient", "journal": "Frontiers in Robotics and AI"},
    {"authors": "Pedregosa et al.", "year": 2011, "chapter": "Bab 3", "title": "Scikit-learn: Machine Learning in Python", "journal": "JMLR (Tool Reference)"},
    {"authors": "Harris et al.", "year": 2020, "chapter": "Bab 3", "title": "Array programming with NumPy", "journal": "Nature (Tool Reference)"}
]

total = len(references)
# Window 5 years from 2026: 2021-2026 (or 2022-2026)
count_2021_2026 = sum(1 for r in references if r['year'] >= 2021)
pct_2021_2026 = (count_2021_2026 / total) * 100

count_2022_2026 = sum(1 for r in references if r['year'] >= 2022)
pct_2022_2026 = (count_2022_2026 / total) * 100

print(f"Total Combined References: {total}")
print(f"References from 2021-2026: {count_2021_2026} ({pct_2021_2026:.2f}%)")
print(f"References from 2022-2026: {count_2022_2026} ({pct_2022_2026:.2f}%)")
print("\nPapers older than 2021:")
for r in references:
    if r['year'] < 2021:
        print(f"  - {r['authors']} ({r['year']}): {r['title']} [{r['chapter']}]")
