# Complete curated bibliography for the entire Proposal (Bab 1, 2, 3)

combined_bib = [
    # 1. Chen et al. (2024) - Frontiers in Public Health
    {"author": "Chen et al.", "year": 2024, "type": "Jurnal 5 Thn Terakhir"},
    # 2. Das et al. (2025) - Nature and Science of Sleep
    {"author": "Das et al.", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 3. Ha et al. (2023) - JMIR
    {"author": "Ha et al.", "year": 2023, "type": "Jurnal 5 Thn Terakhir"},
    # 4. Lin et al. (2025) - Frontiers in Psychiatry
    {"author": "Lin et al.", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 5. Taher & Ayon (2024) - IEEE PEEIACON
    {"author": "Taher & Ayon", "year": 2024, "type": "Jurnal 5 Thn Terakhir"},
    # 6. Loh et al. (2024) - Computers and Electrical Engineering
    {"author": "Loh et al.", "year": 2024, "type": "Jurnal 5 Thn Terakhir"},
    # 7. Li et al. (2025) - BMC Public Health
    {"author": "Li et al.", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 8. Kumar et al. (2025) - J. Pharmacy and Bioallied Sciences
    {"author": "Kumar et al.", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 9. Alqudah et al. (2026) - Scientific Reports
    {"author": "Alqudah et al.", "year": 2026, "type": "Jurnal 5 Thn Terakhir"},
    # 10. Wang et al. (2025) - BMC Cardiovascular Disorders
    {"author": "Wang et al.", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 11. Widayati (2024) - Asian J. Social Health and Behavior
    {"author": "Widayati", "year": 2024, "type": "Jurnal 5 Thn Terakhir"},
    # 12. Srinivasu et al. (2024) - Scientific Reports
    {"author": "Srinivasu et al.", "year": 2024, "type": "Jurnal 5 Thn Terakhir"},
    # 13. El Chakik et al. (2026) - Sci MDPI
    {"author": "El Chakik et al.", "year": 2026, "type": "Jurnal 5 Thn Terakhir"},
    # 14. Chicco & Jurman (2022) - Frontiers in Robotics and AI
    {"author": "Chicco & Jurman", "year": 2022, "type": "Jurnal 5 Thn Terakhir"},
    # 15. Martínez-Plumed et al. (2021) - IEEE TKDE
    {"author": "Martínez-Plumed et al.", "year": 2021, "type": "Jurnal 5 Thn Terakhir"},
    # 16. Schröer, Kruse, & Gómez (2021) - Procedia Computer Science
    {"author": "Schröer et al.", "year": 2021, "type": "Jurnal 5 Thn Terakhir"},
    # 17. Rahman et al. (2025) - IEEE Access
    {"author": "Rahman et al.", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 18. Kaya (2025) - JAIDA
    {"author": "Kaya", "year": 2025, "type": "Jurnal 5 Thn Terakhir"},
    # 19. Putra & Hidayat (2024) - CO-SCIENCE
    {"author": "Putra & Hidayat", "year": 2024, "type": "Jurnal 5 Thn Terakhir"},
    
    # Pustaka Klasik / Fondasi (Pengecualian yang dibolehkan untuk teori dasar / penemu metode):
    # 20. Lundberg & Lee (2017) - NeurIPS (Seminal SHAP)
    {"author": "Lundberg & Lee", "year": 2017, "type": "Pustaka Fondasi Seminal"},
    # 21. Prokhorenkova et al. (2018) - NeurIPS (Penemu CatBoost)
    {"author": "Prokhorenkova et al.", "year": 2018, "type": "Pustaka Fondasi Seminal"},
    # 22. Hancock & Khoshgoftaar (2020) - J. Big Data
    {"author": "Hancock & Khoshgoftaar", "year": 2020, "type": "Pustaka Fondasi Seminal"},
]

total = len(combined_bib)
recent = sum(1 for b in combined_bib if b["year"] >= 2021)
pct = (recent / total) * 100

print(f"Total Jurnal Tergabung: {total}")
print(f"Jurnal 5 Tahun Terakhir (2021-2026): {recent}")
print(f"Jurnal Klasik/Fondasi (>5 Tahun): {total - recent}")
print(f"Persentase Jurnal 5 Tahun Terakhir: {pct:.2f}%")
