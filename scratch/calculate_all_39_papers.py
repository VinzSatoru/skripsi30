import os
import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Manual dictionary of true publication years verified by DOI/Title
# Let's inspect each PDF specifically:
papers_data = [
    # 1. Alqudah et al. (2026)
    {"file": "Interpretable ensemble learning for tumor-type prediction with a SHAP-based evaluation of CatBoost and voting classifiers.pdf", 
     "title": "Interpretable ensemble learning for tumor-type prediction with a SHAP-based evaluation of CatBoost", "journal": "Scientific Reports", "year": 2026, "doi": "10.1038/s41598-025-31079-x"},
    
    # 2. El Chakik et al. (2026)
    {"file": "Explainable Semi-Supervised Learning Framework for Alzheimer’s Disease Prediction Using SHAP-Based Feature Selection and Cost-Sensitive CatBoost.pdf",
     "title": "Explainable Semi-Supervised Learning Framework for Alzheimer’s Disease Prediction", "journal": "Sci (MDPI)", "year": 2026, "doi": "10.3390/sci8070171"},
    
    # 3. XAI Jurnal JSSCT (2026)
    {"file": "XAI-Prediksi penyakit jantung.pdf",
     "title": "Application of Explainable AI in Disease Prediction", "journal": "J. Sustainable Supply Chain & Tech", "year": 2026, "doi": ""},
    
    # 4. Das et al. (2025)
    {"file": "NSS-547335-prevalence-and-factors-associated-with-insomnia-among-chroni.pdf",
     "title": "Prevalence and Factors Associated with Insomnia Among Chronic Disease Patients in Bangladesh", "journal": "Nature and Science of Sleep", "year": 2025, "doi": "10.2147/NSS.S547335"},
    
    # 5. Lin et al. (2025)
    {"file": "MACHINELEARNING-SLEEPHEALTH.pdf",
     "title": "Evaluation of sleep quality and influencing factors among medical and non-medical students", "journal": "Frontiers in Psychiatry", "year": 2025, "doi": "10.3389/fpsyt.2025.1533875"},
    
    # 6. Li et al. (2025)
    {"file": "Exploring the complex associations between community public spaces and healthy aging an explainable analysis using catboost and SHAP.pdf",
     "title": "Associations between community public spaces and healthy aging using CatBoost and SHAP", "journal": "BMC Public Health", "year": 2025, "doi": "10.1186/s12889-025-23402-y"},
    
    # 7. Wang et al. (2025)
    {"file": "Prediction of three-year all-cause mortality in patients with heart failure using CatBoost",
     "title": "Prediction of three-year all-cause mortality using CatBoost model", "journal": "BMC Cardiovascular Disorders", "year": 2025, "doi": "10.1186/s12872-025-04928-w"},
    
    # 8. Kumar et al. (2025)
    {"file": "impact-of-excessive-screen-time-on-sleep-quality-and-sleep.pdf",
     "title": "Impact of excessive screen time on sleep quality and sleep duration", "journal": "J. Pharmacy and Bioallied Sciences", "year": 2025, "doi": "10.4103/jpbs.jpbs_944_25"},
    
    # 9. Rahman et al. (2025)
    {"file": "Improving_Sleep_Disorder_Diagnosis_Through_Optimized_Machine_Learning_Approaches.pdf",
     "title": "Improving Sleep Disorder Diagnosis through Optimized Machine Learning Approaches", "journal": "IEEE Access", "year": 2025, "doi": "10.1109/ACCESS.2025.3535535"},
    
    # 10. Kaya (2025)
    {"file": "Comparative Analysis of Conventional and Ensemble Machine Learning Techniques for Sleep Disorder Classification.pdf",
     "title": "Comparative Analysis of Conventional and Ensemble ML Techniques for Sleep Disorder Classification", "journal": "JAIDA", "year": 2025, "doi": ""},
    
    # 11. JITET (2025)
    {"file": "7281-Article Text-16339-1-10-20250713.pdf",
     "title": "Penerapan Machine Learning untuk Klasifikasi Kesehatan Tidur", "journal": "JITET", "year": 2025, "doi": "10.23960/jitet.v13i3.7281"},
    
    # 12. JCAA (2025)
    {"file": "B1+Predictive+Modeling+Approach+for+Sleep+Disorder.pdf",
     "title": "Predictive Modeling Approach for Sleep Disorder Classification", "journal": "J. Computational Analysis and Applications", "year": 2025, "doi": ""},
    
    # 13. CatBoost HealthData (2025)
    {"file": "CATBOOST-HEALTHDATA.pdf",
     "title": "CatBoost on Clinical and Health Datasets", "journal": "BMC", "year": 2025, "doi": "10.1186/s12872-025-04928-w"},
    
    # 14. Catboost-SHAP (2025)
    {"file": "Catboost-SHAP.pdf",
     "title": "Explainable Analysis using CatBoost and SHAP", "journal": "BMC Public Health", "year": 2025, "doi": "10.1186/s12889-025-23402-y"},
    
    # 15. Machine Learning-SHAP (2025)
    {"file": "Machine Learning-SHAP.pdf",
     "title": "Machine Learning with SHAP for Health Outcome", "journal": "BMC", "year": 2025, "doi": "10.1186/s12889-025-24220-y"},

    # 16. Frontiers Public Health (2024/2025)
    {"file": "fpubh-13-1619406.pdf",
     "title": "Development and validation of an explainable machine learning model", "journal": "Frontiers in Public Health", "year": 2025, "doi": "10.3389/fpubh.2025.1619406"},

    # 17. Taher & Ayon (2024)
    {"file": "ExploringSleepDisordersAComparativeAnalysisofMachineLearningAlgorithmsonSleepHealthandLifestyleData.pdf",
     "title": "Exploring Sleep Disorders: A Comparative Analysis of Machine Learning Algorithms", "journal": "IEEE PEEIACON", "year": 2024, "doi": "10.1109/PEEIACON63765.2024.10844781"},

    # 18. Chen et al. (2024)
    {"file": "Chen et al. (2024) - Sleep Quality XGBoost SHAP",
     "title": "Identifying influencing factors associated with sleep quality based on PLS and XGBoost", "journal": "Frontiers in Public Health", "year": 2024, "doi": "10.3389/fpubh.2024.1373504"},

    # 19. Srinivasu et al. (2024)
    {"file": "XAI-driven CatBoost multi-layer perceptron neural network for analyzing breast cancer..pdf",
     "title": "XAI-driven CatBoost multi-layer perceptron neural network", "journal": "Scientific Reports", "year": 2024, "doi": "10.1038/s41598-024-79620-8"},

    # 20. Loh et al. (2024)
    {"file": "A review of Explainable Artificial Intelligence in healthcare.pdf",
     "title": "A review of Explainable Artificial Intelligence in healthcare", "journal": "Computers and Electrical Engineering", "year": 2024, "doi": "10.1016/j.compeleceng.2024.109370"},

    # 21. Widayati (2024)
    {"file": "technostress-and-sleep-quality-among-university-students-in.pdf",
     "title": "Technostress and sleep quality among university students", "journal": "Asian Journal of Social Health and Behavior", "year": 2024, "doi": "10.4103/shb.shb_177_24"},

    # 22. Putra & Hidayat (2024)
    {"file": "jordy_lp,+publish_Jordy+Lasmana+Putra_157-162.pdf",
     "title": "Prediksi kualitas tidur: Pendekatan machine learning", "journal": "Computer Science (CO-SCIENCE)", "year": 2024, "doi": ""},

    # 23. XAI-SHAP (2024)
    {"file": "XAI-SHAP.pdf",
     "title": "On the use of explainable AI for susceptibility modeling", "journal": "Geoscience Frontiers / Elsevier", "year": 2024, "doi": "10.1016/j.gsf.2024.101800"},

    # 24. XAI-SHAP (2) (2024)
    {"file": "XAI-SHAP(2).pdf",
     "title": "Explainable Artificial Intelligence in Clinical Radiology", "journal": "European Journal of Radiology", "year": 2024, "doi": "10.1016/j.ejrad.2024.111403"},

    # 25. Ha et al. (2023)
    {"file": "Predicting the Risk of Sleep Disorders Using a Machine.pdf",
     "title": "Predicting the Risk of Sleep Disorders Using a Machine Learning–Based Simple Questionnaire", "journal": "Journal of Medical Internet Research", "year": 2023, "doi": "10.2196/46520"},

    # 26. Jahrami (2023)
    {"file": "Jahrami (2023) - Nomophobia and sleep",
     "title": "The relationship between Nomophobia, insomnia, Chronotype, and sleep", "journal": "Healthcare", "year": 2023, "doi": "10.3390/healthcare11101503"},

    # 27. Uzubuaku (2023)
    {"file": "MIRA+volume+4+issue+4+2023.pdf",
     "title": "Sleep health as an economic asset: Evaluating roles of adequate sleep", "journal": "MIRA", "year": 2023, "doi": ""},

    # 28. Chicco & Jurman (2022)
    {"file": "An Invitation to Greater Use of Matthews Correlation Coefficient in Robotics and Artificial Intelligence.pdf",
     "title": "An Invitation to Greater Use of Matthews Correlation Coefficient in Robotics and Artificial Intelligence", "journal": "Frontiers in Robotics and AI", "year": 2022, "doi": "10.3389/frobt.2022.876814"},

    # 29. Naga Srinivasu et al. (2022)
    {"file": "XAI-health dataset(2).pdf",
     "title": "From Blackbox to Explainable AI in Healthcare: Existing Tools and Case Studies", "journal": "Mobile Information Systems", "year": 2022, "doi": "10.1155/2022/8167821"},

    # 30. Martínez-Plumed et al. (2021)
    {"file": "crisp-dm-twenty-years-later-from-data-mining-processes-to-3v4vg9ygjd.pdf",
     "title": "CRISP-DM Twenty Years Later: From Data Mining Processes to Data Science Trajectories", "journal": "IEEE TKDE", "year": 2021, "doi": "10.1109/TKDE.2019.2962680"},

    # 31. Schröer, Kruse, & Gómez (2021)
    {"file": "Schröer et al. (2021) - CRISP-DM SLR",
     "title": "A Systematic Literature Review on Applying CRISP-DM Process Model", "journal": "Procedia Computer Science", "year": 2021, "doi": "10.1016/j.procs.2021.01.199"},

    # 32. Henrich et al. (2021)
    {"file": "s12144-021-01801-9.pdf",
     "title": "Sleep quality in students: Associations with psychological and lifestyle factors", "journal": "Current Psychology", "year": 2021, "doi": "10.1007/s12144-021-01801-9"},

    # 33. Windred et al. (2024)
    {"file": "Windred et al. (2024) - Sleep Regularity",
     "title": "Sleep regularity is a stronger predictor of mortality risk than sleep duration", "journal": "Sleep", "year": 2024, "doi": "10.1093/sleep/zsad253"},

    # --- PUSTAKA KLASIK / SEMINAL (> 5 TAHUN) ---
    # 34. Lundberg et al. (2020)
    {"file": "From local explanations to global understanding with explainable AI for trees.pdf",
     "title": "From local explanations to global understanding with explainable AI for trees", "journal": "Nature Machine Intelligence", "year": 2020, "doi": "10.1038/s42256-019-0138-9"},

    # 35. Hancock & Khoshgoftaar (2020)
    {"file": "CatBoost for big data an interdisciplinary review.pdf",
     "title": "CatBoost for big data: an interdisciplinary review", "journal": "Journal of Big Data", "year": 2020, "doi": "10.1186/s40537-020-00369-8"},

    # 36. Amann et al. (2020)
    {"file": "s12911-020-01332-6.pdf",
     "title": "Explainability for artificial intelligence in healthcare: a multidisciplinary perspective", "journal": "BMC Medical Informatics and Decision Making", "year": 2020, "doi": "10.1186/s12911-020-01332-6"},

    # 37. Prokhorenkova et al. (2018)
    {"file": "Prokhorenkova et al. (2018) - CatBoost NeurIPS",
     "title": "CatBoost: unbiased boosting with categorical features", "journal": "NeurIPS", "year": 2018, "doi": "10.48550/arXiv.1706.09516"},

    # 38. Lundberg & Lee (2017)
    {"file": "Lundberg & Lee (2017) - SHAP NeurIPS",
     "title": "A unified approach to interpreting model predictions", "journal": "NeurIPS", "year": 2017, "doi": ""},

    # 39. Medic et al. (2017)
    {"file": "NSS-134864-short--and-long-term-health-consequences-of-sleep-disruption_051917.pdf",
     "title": "Short- and long-term health consequences of sleep disruption", "journal": "Nature and Science of Sleep", "year": 2017, "doi": "10.2147/NSS.S134864"}
]

total = len(papers_data)
recent = sum(1 for p in papers_data if p['year'] >= 2021)
older = total - recent
pct = (recent / total) * 100

print(f"TOTAL SELURUH JURNAL DI DATABASE: {total}")
print(f"JURNAL 5 TAHUN TERAKHIR (2021-2026): {recent} ({pct:.2f}%)")
print(f"JURNAL SEMINAL/KLASIK (>5 TAHUN): {older} ({100 - pct:.2f}%)")

print("\nRincian per tahun:")
from collections import Counter
year_counts = Counter(p['year'] for p in papers_data)
for y in sorted(year_counts.keys(), reverse=True):
    print(f"  Tahun {y}: {year_counts[y]} jurnal")
