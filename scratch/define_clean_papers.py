# Script to build the clean, 100% verified, 1-to-1 matching bibliography

clean_papers = [
    # 1. Amann et al. (2020)
    {
        "cite": "Amann et al., 2020",
        "author": "Amann, J., Blasimme, A., Vayena, E., Frey, D., & Madai, V. I.",
        "year": 2020,
        "title": "Explainability for artificial intelligence in healthcare: a multidisciplinary perspective",
        "journal": "BMC Medical Informatics and Decision Making, 20(1), 310",
        "doi": "https://doi.org/10.1186/s12911-020-01332-6",
        "where": ["Bab 1", "Bab 2"]
    },
    # 2. Chicco & Jurman (2022)
    {
        "cite": "Chicco & Jurman, 2022",
        "author": "Chicco, D., & Jurman, G.",
        "year": 2022,
        "title": "An invitation to greater use of Matthews correlation coefficient in robotics and artificial intelligence",
        "journal": "Frontiers in Robotics and AI, 9, 876814",
        "doi": "https://doi.org/10.3389/frobt.2022.876814",
        "where": ["Bab 3"]
    },
    # 3. Das et al. (2025)
    {
        "cite": "Das et al., 2025",
        "author": "Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A., Al Mamun, F., Mamun, M. A., & Gozal, D.",
        "year": 2025,
        "title": "Prevalence and factors associated with insomnia among chronic disease patients in Bangladesh: A machine learning study",
        "journal": "Nature and Science of Sleep, 17, 2725–2741",
        "doi": "https://doi.org/10.2147/NSS.S547335",
        "where": ["Bab 1", "Bab 2", "Bab 3"]
    },
    # 4. Deivendran et al. (2025)
    {
        "cite": "Deivendran et al., 2025",
        "author": "Deivendran, S., Kanagaraj, K., & Leelabai, T.",
        "year": 2025,
        "title": "Impact of Excessive Screen Time on Sleep Quality and Sleep Disturbances Among Young Adults: A Cross-Sectional Study",
        "journal": "Journal of Pharmacy and Bioallied Sciences, 17(Suppl 1), S944–S947",
        "doi": "https://doi.org/10.4103/jpbs.jpbs_944_25",
        "where": ["Bab 2"]
    },
    # 5. El Chakik et al. (2026)
    {
        "cite": "El Chakik et al., 2026",
        "author": "El Chakik, A., Nakhal, B., & Nassreddine, G.",
        "year": 2026,
        "title": "Explainable semi-supervised learning framework for Alzheimer’s disease prediction using SHAP-based feature selection and cost-sensitive CatBoost",
        "journal": "Sci, 8(7), 171",
        "doi": "https://doi.org/10.3390/sci8070171",
        "where": ["Bab 3"]
    },
    # 6. Ha et al. (2023)
    {
        "cite": "Ha et al., 2023",
        "author": "Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K.",
        "year": 2023,
        "title": "Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study",
        "journal": "Journal of Medical Internet Research, 25, e46520",
        "doi": "https://doi.org/10.2196/46520",
        "where": ["Bab 1", "Bab 2", "Bab 3"]
    },
    # 7. Hancock & Khoshgoftaar (2020)
    {
        "cite": "Hancock & Khoshgoftaar, 2020",
        "author": "Hancock, J. T., & Khoshgoftaar, T. M.",
        "year": 2020,
        "title": "CatBoost for big data: an interdisciplinary review",
        "journal": "Journal of Big Data, 7(1), 94",
        "doi": "https://doi.org/10.1186/s40537-020-00369-8",
        "where": ["Bab 2"]
    },
    # 8. Henrich et al. (2021)
    {
        "cite": "Henrich et al., 2021",
        "author": "Henrich, L. C., Antypa, N., & Van den Berg, J. F.",
        "year": 2021,
        "title": "Sleep quality in students: Associations with psychological and lifestyle factors",
        "journal": "Current Psychology, 41, 4221–4230",
        "doi": "https://doi.org/10.1007/s12144-021-01801-9",
        "where": ["Bab 1", "Bab 2"]
    },
    # 9. Hulsen (2023)
    {
        "cite": "Hulsen, 2023",
        "author": "Hulsen, T.",
        "year": 2023,
        "title": "Explainable artificial intelligence (XAI): Concepts and challenges in healthcare",
        "journal": "AI, 4(3), 652–666",
        "doi": "https://doi.org/10.3390/ai4030034",
        "where": ["Bab 1"]
    },
    # 10. Jahrami (2023)
    {
        "cite": "Jahrami, 2023",
        "author": "Jahrami, H.",
        "year": 2023,
        "title": "The relationship between Nomophobia, insomnia, Chronotype, phone in proximity, screen time, and sleep duration in adults: A mobile phone app-assisted cross-sectional study",
        "journal": "Healthcare, 11(10), 1503",
        "doi": "https://doi.org/10.3390/healthcare11101503",
        "where": ["Bab 1", "Bab 2"]
    },
    # 11. Kaya (2025)
    {
        "cite": "Kaya, 2025",
        "author": "Kaya, C.",
        "year": 2025,
        "title": "Comparative analysis of conventional and ensemble machine learning techniques for sleep disorder classification",
        "journal": "Journal of Artificial Intelligence and Data Science (JAIDA), 5(2), 132–139",
        "doi": "https://dergipark.org.tr/en/pub/jaida/issue/87774/1825274",
        "where": ["Bab 1", "Bab 2"]
    },
    # 12. Lin et al. (2025)
    {
        "cite": "Lin et al., 2025",
        "author": "Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L.",
        "year": 2025,
        "title": "Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques",
        "journal": "Frontiers in Psychiatry, 16, 1533875",
        "doi": "https://doi.org/10.3389/fpsyt.2025.1533875",
        "where": ["Bab 1", "Bab 2"]
    },
    # 13. Lundberg & Lee (2017)
    {
        "cite": "Lundberg & Lee, 2017",
        "author": "Lundberg, S. M., & Lee, S. I.",
        "year": 2017,
        "title": "A unified approach to interpreting model predictions",
        "journal": "Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 4765–4774",
        "doi": "https://doi.org/10.48550/arXiv.1705.07874",
        "where": ["Bab 2", "Bab 3"]
    },
    # 14. Lundberg et al. (2020)
    {
        "cite": "Lundberg et al., 2020",
        "author": "Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S. I.",
        "year": 2020,
        "title": "From local explanations to global understanding with explainable AI for trees",
        "journal": "Nature Machine Intelligence, 2(1), 56–67",
        "doi": "https://doi.org/10.1038/s42256-019-0138-9",
        "where": ["Bab 2"]
    },
    # 15. Martínez-Plumed et al. (2021)
    {
        "cite": "Martínez-Plumed et al., 2021",
        "author": "Martínez-Plumed, F., Contreras-Ochando, L., Ferri, C., Hernandez-Orallo, J., Kull, M., Lachiche, N., & Flach, P.",
        "year": 2021,
        "title": "CRISP-DM twenty years later: From data mining processes to data science trajectories",
        "journal": "IEEE Transactions on Knowledge and Data Engineering, 33(8), 3048–3061",
        "doi": "https://doi.org/10.1109/TKDE.2019.2962680",
        "where": ["Bab 3"]
    },
    # 16. Mawardi et al. (2025)
    {
        "cite": "Mawardi et al., 2025",
        "author": "Mawardi, A. B., Pradini, R. S., & Haris, M. S.",
        "year": 2025,
        "title": "Komparasi Algoritma Boosting untuk Prediksi Gangguan Tidur",
        "journal": "JITET (Jurnal Informatika dan Teknik Elektro Terapan), 13(3), 1377–1385",
        "doi": "https://doi.org/10.23960/jitet.v13i3.7281",
        "where": ["Bab 1", "Bab 2"]
    },
    # 17. Medic et al. (2017)
    {
        "cite": "Medic et al., 2017",
        "author": "Medic, G., Wille, M., & Hemels, M. E.",
        "year": 2017,
        "title": "Short- and long-term health consequences of sleep disruption",
        "journal": "Nature and Science of Sleep, 9, 151–161",
        "doi": "https://doi.org/10.2147/NSS.S134864",
        "where": ["Bab 2"]
    },
    # 18. Prokhorenkova et al. (2018)
    {
        "cite": "Prokhorenkova et al., 2018",
        "author": "Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A.",
        "year": 2018,
        "title": "CatBoost: unbiased boosting with categorical features",
        "journal": "Advances in Neural Information Processing Systems (NeurIPS 2018), 31, 6638–6648",
        "doi": "https://doi.org/10.48550/arXiv.1706.09516",
        "where": ["Bab 2"]
    },
    # 19. Putra & Hidayat (2024)
    {
        "cite": "Putra & Hidayat, 2024",
        "author": "Putra, J. L., & Hidayat, W. F.",
        "year": 2024,
        "title": "Prediksi kualitas tidur: Pendekatan machine learning yang mengintegrasikan faktor kesehatan dan lingkungan",
        "journal": "Computer Science (CO-SCIENCE), 4(2), 157–162",
        "doi": "https://doi.org/10.31294/coscience.v4i2.4737",
        "where": ["Bab 1"]
    },
    # 20. Rahman et al. (2025)
    {
        "cite": "Rahman et al., 2025",
        "author": "Rahman, M. A., Jahan, I., Islam, M., Jabid, T., Ali, M. S., Rashid, M. R. A., Islam, M. M., Ferdaus, M. H., Rasel, M. M. K., Jahan, M. R., Sharmin, S., Rimi, T. A., Talukder, A. S., Matin, M. M. H., & Ali, M. A.",
        "year": 2025,
        "title": "Improving sleep disorder diagnosis through optimized machine learning approaches",
        "journal": "IEEE Access, 13, 22051–22070",
        "doi": "https://doi.org/10.1109/ACCESS.2025.3535535",
        "where": ["Bab 1", "Bab 2"]
    },
    # 21. Sadeghi et al. (2024)
    {
        "cite": "Sadeghi et al., 2024",
        "author": "Sadeghi, Z., Alizadehsani, R., & Cifci, M. A.",
        "year": 2024,
        "title": "A review of Explainable Artificial Intelligence in healthcare",
        "journal": "Computers and Electrical Engineering, 118, 109370",
        "doi": "https://doi.org/10.1016/j.compeleceng.2024.109370",
        "where": ["Bab 2"]
    },
    # 22. Schröer et al. (2021)
    {
        "cite": "Schröer et al., 2021",
        "author": "Schröer, C., Kruse, F., & Gómez, J. M.",
        "year": 2021,
        "title": "A systematic literature review on applying CRISP-DM process model",
        "journal": "Procedia Computer Science, 181, 526–534",
        "doi": "https://doi.org/10.1016/j.procs.2021.01.199",
        "where": ["Bab 3"]
    },
    # 23. Srinivasu et al. (2022)
    {
        "cite": "Srinivasu et al., 2022",
        "author": "Srinivasu, P. N., Sandhya, N., Jhaveri, R. H., & Raut, R.",
        "year": 2022,
        "title": "From Blackbox to Explainable AI in Healthcare: Existing Tools and Case Studies",
        "journal": "Mobile Information Systems, 2022, 8167821",
        "doi": "https://doi.org/10.1155/2022/8167821",
        "where": ["Bab 2"]
    },
    # 24. Srinivasu et al. (2024)
    {
        "cite": "Srinivasu et al., 2024",
        "author": "Srinivasu, P. N., Shafi, J., Arif, M., Debtera, B., & Gudi, A.",
        "year": 2024,
        "title": "XAI-driven CatBoost multi-layer perceptron neural network for analyzing breast cancer",
        "journal": "Scientific Reports, 14, 28674",
        "doi": "https://doi.org/10.1038/s41598-024-79620-8",
        "where": ["Bab 1", "Bab 2"]
    },
    # 25. Taher & Ayon (2024)
    {
        "cite": "Taher & Ayon, 2024",
        "author": "Taher, A., & Ayon, W. I. Z.",
        "year": 2024,
        "title": "Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data",
        "journal": "2024 IEEE PEEIACON, 1–6",
        "doi": "https://doi.org/10.1109/PEEIACON63629.2024.10800593",
        "where": ["Bab 1", "Bab 2"]
    },
    # 26. Uzubuaku (2023)
    {
        "cite": "Uzubuaku, 2023",
        "author": "Uzubuaku, I. A.",
        "year": 2023,
        "title": "Sleep health as an economic asset: Evaluating roles of adequate sleep in global labor efficiency",
        "journal": "Multidisciplinary Innovations & Research Analysis (MIRA), 4(4), 71–85",
        "doi": "https://openviewjournal.com/index.php/mira/issue/view/16",
        "where": ["Bab 1"]
    },
    # 27. Wang et al. (2025)
    {
        "cite": "Wang et al., 2025",
        "author": "Wang, X., Zhang, Y., & Lu, H.",
        "year": 2025,
        "title": "Development and validation of an explainable machine learning model for predicting the risk of sleep disorders in older adults with multimorbidity: a cross-sectional study",
        "journal": "Frontiers in Public Health, 13, 1619406",
        "doi": "https://doi.org/10.3389/fpubh.2025.1619406",
        "where": ["Bab 2"]
    },
    # 28. Widayati (2024)
    {
        "cite": "Widayati, 2024",
        "author": "Widayati, K. A.",
        "year": 2024,
        "title": "Technostress and sleep quality among university students",
        "journal": "Asian Journal of Social Health and Behavior, 7(4), 197–205",
        "doi": "https://doi.org/10.4103/shb.shb_177_24",
        "where": ["Bab 1", "Bab 2"]
    },
    # 29. Windred et al. (2024)
    {
        "cite": "Windred et al., 2024",
        "author": "Windred, D. P., Burns, A. C., Rutter, M. K., & Phillips, A. J. K.",
        "year": 2024,
        "title": "Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study",
        "journal": "Sleep, 47(1), zsad253",
        "doi": "https://doi.org/10.1093/sleep/zsad253",
        "where": ["Bab 1", "Bab 2"]
    },
    # 30. Wolak et al. (2025)
    {
        "cite": "Wolak et al., 2025",
        "author": "Wolak, M., Plichta, M., & Orlicki, P.",
        "year": 2025,
        "title": "Interpretable ensemble learning for tumor-type prediction with a SHAP-based evaluation of CatBoost and voting classifiers",
        "journal": "Scientific Reports, 15, 31079",
        "doi": "https://doi.org/10.1038/s41598-025-31079-x",
        "where": ["Bab 2"]
    },
    # 31. Wu et al. (2025)
    {
        "cite": "Wu et al., 2025",
        "author": "Wu, L., Tao, Y., & Xie, Y.",
        "year": 2025,
        "title": "Prediction of three-year all-cause mortality in patients with heart failure and atrial fibrillation using the CatBoost model",
        "journal": "BMC Cardiovascular Disorders, 25(1), 4928",
        "doi": "https://doi.org/10.1186/s12872-025-04928-w",
        "where": ["Bab 2"]
    },
    # 32. Xie et al. (2026)
    {
        "cite": "Xie et al., 2026",
        "author": "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y.",
        "year": 2026,
        "title": "Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost",
        "journal": "Frontiers in Psychology, 16, 1732946",
        "doi": "https://doi.org/10.3389/fpsyg.2025.1732946",
        "where": ["Bab 1", "Bab 2"]
    },
    # 33. Zhang et al. (2025)
    {
        "cite": "Zhang et al., 2025",
        "author": "Zhang, M., Shen, T., Lou, Y., & Li, X.",
        "year": 2025,
        "title": "Exploring the complex associations between community public spaces and healthy aging: an explainable analysis using CatBoost and SHAP",
        "journal": "BMC Public Health, 25(1), 2200",
        "doi": "https://doi.org/10.1186/s12889-025-23402-y",
        "where": ["Bab 2"]
    },
    # 34. Bhattarai et al. (2024)
    {
        "cite": "Bhattarai et al., 2024",
        "author": "Bhattarai, P., Thakuri, D. S., Nie, Y., & Chand, G. B.",
        "year": 2024,
        "title": "Explainable AI-based Deep-SHAP for mapping the multivariate relationships between regional neuroimaging biomarkers and cognition",
        "journal": "European Journal of Radiology, 174, 111403",
        "doi": "https://doi.org/10.1016/j.ejrad.2024.111403",
        "where": ["Bab 2"]
    }
]

print(f"Total curated clean papers: {len(clean_papers)}")
recent = sum(1 for p in clean_papers if p["year"] >= 2021)
print(f"Papers from 2021-2026: {recent} / {len(clean_papers)} ({recent/len(clean_papers)*100:.2f}%)")
