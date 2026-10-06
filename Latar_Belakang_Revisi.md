# Latar Belakang (Revisi — Paragraf Tambahan untuk SOTA + GAP dan Tujuan)

## Instruksi
- Paragraf 1–4 **TIDAK DIUBAH**, tetap menggunakan teks asli dari OUTLINE_1438.pdf.
- **Paragraf 3** perlu penyesuaian kecil: ganti referensi **Sadeghi et al. (2024)** dengan **Ha et al. (2023)** karena jurnal SOTA telah diperbarui.
- Paragraf 5 dan 6 di bawah ini adalah **paragraf baru** yang ditambahkan setelah paragraf 4.

---

## Paragraf 1 & 2: TIDAK BERUBAH (dari OUTLINE_1438.pdf)

*(Tetap gunakan paragraf asli Anda.)*

---

## Paragraf 3: PENYESUAIAN REFERENSI

Paragraf asli Anda membahas urgensi XAI dan mengutip Sadeghi et al. (2024). Karena Sadeghi sudah diganti dengan Ha et al. (2023) di daftar SOTA, paragraf ini perlu disesuaikan. Berikut versi revisinya:

Namun, akurasi prediksi yang tinggi saja tidak cukup untuk menjadikan sebuah model layak digunakan dalam pengambilan keputusan medis. Inilah paradoks terbesar *machine learning* modern; semakin kompleks model, semakin sulit prediksinya untuk dipahami manusia. CatBoost, seperti algoritma *ensemble* berbasis pohon lainnya, beroperasi sebagai *black-box* yang menghasilkan keputusan dari ratusan pohon yang bekerja paralel tanpa menjelaskan mengapa seseorang dikategorikan berisiko tinggi. Kondisi ini bukan sekadar masalah teknis; ia menyentuh dimensi etika dan kepercayaan yang fundamental dalam penerapan AI di dunia kesehatan. Ha et al. (2023) menunjukkan bahwa penggunaan metode *Explainable AI* berbasis SHAP pada algoritma XGBoost mampu meningkatkan interpretabilitas prediksi gangguan tidur, meskipun penerapannya masih terbatas pada seleksi fitur kuesioner klinis, bukan penjelasan prediksi gaya hidup per individu secara *real-time*. Atas dasar itulah, *Explainable AI* (XAI) diposisikan sebagai komponen inti dalam penelitian ini.

---

## Paragraf 4: PENYESUAIAN REFERENSI (dari OUTLINE_1438.pdf)

*(Pada paragraf asli Anda yang membahas SHAP, pastikan Anda **mengganti** sitasi Emhandyksa & Afifah dengan Chen et al. (2024), serta Srinivasu et al.)*

---

## Paragraf 5 — State of the Art + Research GAP (BARU)

Meskipun penelitian-penelitian terdahulu telah memberikan kontribusi signifikan, terdapat lima celah riset yang belum terisi secara simultan. Taher & Ayon (2024) dan Lin et al. (2025) membuktikan efektivitas *machine learning* untuk klasifikasi gangguan tidur, namun model yang dihasilkan masih bersifat *black-box* tanpa penjelasan faktor risiko spesifik per individu. Ha et al. (2023) telah menggabungkan XGBoost dan SHAP di domain tidur, namun menggunakan algoritma yang memerlukan *encoding* manual, fitur kuesioner klinis yang tidak *modifiable*, dan SHAP hanya untuk seleksi fitur. Srinivasu et al. (2024) memvalidasi keunggulan CatBoost-SHAP, namun pada domain kanker payudara dengan fitur laboratorium yang tidak dapat diubah pasien. Selain itu, keharusan menggunakan *one-hot encoding* pada algoritma XGBoost, seperti yang dilakukan oleh Chen et al. (2024), memicu hasil interpretasi SHAP yang terfragmentasi dan membingungkan secara medis. Dengan demikian, **belum ada penelitian yang mengintegrasikan CatBoost dengan SHAP untuk menganalisis faktor risiko gangguan tidur berbasis metrik gaya hidup secara individual dan interaktif tanpa memecah struktur data aslinya**.

---

## Paragraf 6 — Tujuan dan Harapan Penelitian (BARU)

Berdasarkan celah riset yang telah diidentifikasi, penelitian ini bertujuan untuk menerapkan metode *Explainable AI* berbasis SHAP pada algoritma CatBoost guna menghasilkan model klasifikasi risiko gangguan tidur yang tidak hanya akurat, tetapi juga transparan dan dapat diinterpretasikan secara menyeluruh. Lundberg & Lee (2017) menyatakan bahwa SHAP merupakan satu-satunya metode interpretabilitas yang secara matematis menjamin tiga properti fundamental: konsistensi lokal, *missingness*, dan akurasi aditif, menjadikannya fondasi yang ideal untuk mengurai kontribusi setiap fitur gaya hidup secara adil dan terukur. Melalui pendekatan ini, penelitian diharapkan mampu mengidentifikasi faktor gaya hidup dominan yang berkontribusi terhadap risiko gangguan tidur secara individual untuk setiap pasien, sekaligus menghasilkan purwarupa sistem pendukung keputusan berbasis web yang interaktif dan siap diadaptasi dengan data rekam medis klinis lokal di masa mendatang.

---

## Referensi Tambahan yang Digunakan

- Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the Risk of Sleep Disorders Using a Machine Learning–Based Simple Questionnaire: Development and Validation Study. *Journal of Medical Internet Research*, 25, e46520.
- Chen, T., et al. (2024). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Public Health*, 12, 1373504.
- Lundberg, S. M., & Lee, S. I. (2017). A Unified Approach to Interpreting Model Predictions. *Advances in Neural Information Processing Systems (NeurIPS)*, 30.

---

## Ringkasan Struktur Akhir Latar Belakang

| Paragraf | Kategori | Sitasi | Status |
|:---:|---|---|:---:|
| 1 | Masalah (masalah, data, akibat, solusi) | Lin et al. (2025) | ASLI |
| 2 | Metode/Algoritma (CatBoost) | Taher & Ayon (2024) | ASLI |
| 3 | Metode/Algoritma (Urgensi XAI) | Ha et al. (2023) | **REVISI** (ganti Sadeghi → Ha) |
| 4 | Metode/Algoritma (SHAP) | Chen et al. (2024); Srinivasu et al. (2024) | **REVISI** (ganti Emhandyksa → Chen) |
| **5** | **State of the Art + Research GAP** | Seluruh 5 jurnal | **BARU** |
| **6** | **Tujuan dan Harapan** | Lundberg & Lee (2017) | **BARU** |
