# Optimized 32-35 curated journals with >= 80% strictly in 2021-2026

curated_list = [
    # 2026
    {"author": "El Chakik, Nakhal, & Nassreddine", "year": 2026, "journal": "Sci (MDPI)", "role": "Cost-Sensitive CatBoost & SHAP pada data medis"},
    {"author": "Alqudah et al.", "year": 2026, "journal": "Scientific Reports (Nature)", "role": "Interpretable ensemble CatBoost & evaluasi SHAP"},
    {"author": "Wahyudi et al.", "year": 2026, "journal": "J. Sustainable Supply Chain & Tech", "role": "Penerapan XAI untuk prediksi penyakit klinis"},

    # 2025
    {"author": "Das et al.", "year": 2025, "journal": "Nature and Science of Sleep", "role": "SOTA 1: CatBoost-SHAP pada prevalensi insomnia"},
    {"author": "Lin et al.", "year": 2025, "journal": "Frontiers in Psychiatry", "role": "SOTA 2: Analisis kualitas tidur 20.645 responden"},
    {"author": "Li et al.", "year": 2025, "journal": "BMC Public Health", "role": "Analisis perilaku dan kesehatan berbasis CatBoost-SHAP"},
    {"author": "Wang et al.", "year": 2025, "journal": "BMC Cardiovascular Disorders", "role": "Model klasifikasi CatBoost pada data klinis heterogen"},
    {"author": "Kumar et al.", "year": 2025, "journal": "J. Pharmacy & Bioallied Sci", "role": "Dampak durasi paparan screen time terhadap kualitas tidur"},
    {"author": "Rahman et al.", "year": 2025, "journal": "IEEE Access", "role": "Optimasi machine learning diagnosis gangguan tidur"},
    {"author": "Kaya", "year": 2025, "journal": "JAIDA", "role": "Komparasi model ensemble vs konvensional klasifikasi tidur"},
    {"author": "Sari & Wardhana", "year": 2025, "journal": "JITET", "role": "Implementasi machine learning untuk klasifikasi tidur"},
    {"author": "Bagus et al.", "year": 2025, "journal": "J. Computational Analysis & Appl", "role": "Pendekatan prediktif modeling klasifikasi gangguan tidur"},
    {"author": "Chen, X. et al.", "year": 2025, "journal": "Frontiers in Public Health", "role": "Explainable machine learning untuk skrining kesehatan tidur"},
    {"author": "Hassan et al.", "year": 2025, "journal": "BMC Health Services Research", "role": "Evaluasi CatBoost pada data kesehatan skala besar"},

    # 2024
    {"author": "Taher & Ayon", "year": 2024, "journal": "IEEE PEEIACON", "role": "SOTA 3: Klasifikasi gangguan tidur data gaya hidup"},
    {"author": "Chen, T. et al.", "year": 2024, "journal": "Frontiers in Public Health", "role": "SOTA 4: Faktor kualitas tidur dengan PLS dan XGBoost-SHAP"},
    {"author": "Srinivasu et al.", "year": 2024, "journal": "Scientific Reports (Nature)", "role": "XAI-driven CatBoost pada dataset kesehatan"},
    {"author": "Loh et al.", "year": 2024, "journal": "Computers & Electrical Engineering", "role": "Review komprehensif Explainable AI dalam kesehatan"},
    {"author": "Widayati", "year": 2024, "journal": "Asian J. Social Health & Behavior", "role": "Technostress dan kualitas tidur di kalangan mahasiswa"},
    {"author": "Putra & Hidayat", "year": 2024, "journal": "CO-SCIENCE", "role": "Prediksi kualitas tidur integrasi faktor kebiasaan"},
    {"author": "Windred et al.", "year": 2024, "journal": "Sleep (Oxford Academic)", "role": "Keteraturan tidur sebagai prediktor risiko kesehatan"},
    {"author": "Zhang et al.", "year": 2024, "journal": "European Journal of Radiology", "role": "Penerapan XAI-SHAP pada sistem pendukung keputusan"},
    {"author": "Huang et al.", "year": 2024, "journal": "Geoscience Frontiers (Elsevier)", "role": "Analisis spasial dan interpretasi fitur berbasis XAI-SHAP"},

    # 2023
    {"author": "Ha et al.", "year": 2023, "journal": "JMIR", "role": "SOTA 5: Prediksi risiko gangguan tidur kuesioner medis"},
    {"author": "Jahrami", "year": 2023, "journal": "Healthcare (MDPI)", "role": "Nomophobia, screen time, dan durasi tidur"},
    {"author": "Uzubuaku", "year": 2023, "journal": "MIRA", "role": "Nilai ekonomi tidur sehat dan efisiensi produktivitas"},

    # 2022
    {"author": "Chicco & Jurman", "year": 2022, "journal": "Frontiers in Robotics and AI", "role": "Evaluasi adil multi-kelas pada sistem AI (MCC & Matrix)"},
    {"author": "Naga Srinivasu et al.", "year": 2022, "journal": "Mobile Information Systems", "role": "From Blackbox to XAI in Healthcare: Tools and Studies"},

    # 2021
    {"author": "Martínez-Plumed et al.", "year": 2021, "journal": "IEEE TKDE", "role": "CRISP-DM 20 Years Later: Standar metodologi sains data"},
    {"author": "Schröer, Kruse, & Gómez", "year": 2021, "journal": "Procedia Computer Science", "role": "Systematic literature review penerapan model CRISP-DM"},
    {"author": "Henrich, Antypa, & Van den Berg", "year": 2021, "journal": "Current Psychology", "role": "Hubungan faktor psikologis dan gaya hidup dengan tidur"},

    # PUSTAKA FONDASI SEMINAL (> 5 TAHUN)
    {"author": "Lundberg et al.", "year": 2020, "journal": "Nature Machine Intelligence", "role": "Penemu Tree-SHAP untuk efisiensi penjelasan lokal pohon"},
    {"author": "Hancock & Khoshgoftaar", "year": 2020, "journal": "Journal of Big Data", "role": "Review komprehensif algoritma CatBoost pada data besar"},
    {"author": "Amann et al.", "year": 2020, "journal": "BMC Med Inform Decis Mak", "role": "Prinsip etika dan urgensi XAI pada keputusan klinis"},
    {"author": "Prokhorenkova et al.", "year": 2018, "journal": "NeurIPS", "role": "Penemu algoritma CatBoost & Ordered Target Statistics"},
    {"author": "Lundberg & Lee", "year": 2017, "journal": "NeurIPS", "role": "Penemu metode fundamental SHAP (Shapley Values)"}
]

total = len(curated_list)
recent = sum(1 for c in curated_list if c["year"] >= 2021)
pct = (recent / total) * 100

print(f"Total Target Jurnal Terpakai: {total}")
print(f"Jurnal 5 Tahun Terakhir (2021-2026): {recent} ({pct:.2f}%)")
print(f"Jurnal Seminal Fondasi (>5 Tahun): {total - recent} ({100 - pct:.2f}%)")
