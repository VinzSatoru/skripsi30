# Metodologi Penelitian: CRISP-DM
*(Cross-Industry Standard Process for Data Mining)*

Penelitian ini menggunakan kerangka kerja CRISP-DM yang merupakan standar industri untuk proyek *data mining* dan *machine learning*. Alur ini bersifat iteratif dan terdiri dari 6 tahapan utama yang disesuaikan dengan konteks penerapan algoritma CatBoost dan interpretasi XAI (SHAP) untuk analisis gangguan tidur.

---

## 1. Business Understanding (Pemahaman Masalah)
Tahap ini berfokus pada pemahaman tujuan penelitian dari perspektif masalah kesehatan dan teknis.

*   **Identifikasi Masalah:** Peningkatan kasus gangguan tidur yang dipicu oleh faktor gaya hidup modern (seperti *screen time* berlebih dan konsumsi kafein). Dibutuhkan sistem deteksi yang tidak hanya akurat, tetapi juga dapat menjelaskan *mengapa* seseorang berisiko.
*   **Tujuan Utama:** Membangun model klasifikasi dengan algoritma CatBoost untuk memprediksi tingkat risiko gangguan tidur (Healthy, Mild, Moderate, Severe).
*   **Tujuan Eksplanatori:** Menerapkan metode SHAP (XAI) untuk membedah *black-box* model dan mengidentifikasi faktor gaya hidup spesifik yang paling dominan bagi setiap individu.
*   **Kriteria Sukses:** Model mencapai akurasi evaluasi yang tinggi, dan visualisasi SHAP mampu memberikan insight medis yang logis dan *actionable* (dapat ditindaklanjuti).

## 2. Data Understanding (Pemahaman Data)
Tahap pengumpulan awal dan eksplorasi data untuk memahami karakteristik *dataset*.

*   **Pengumpulan Data:** Menggunakan dataset sekunder `sleep_health_dataset.csv` (berasal dari Kaggle/repositori publik) yang berisi metrik gaya hidup dan kebiasaan tidur.
*   **Karakteristik Data:** Memiliki volume besar (100.000 baris) dengan 32 atribut (kolom) yang mencakup data metrik (numerik) dan demografi/kategori (kategorikal).
*   **Analisis Distribusi Kelas:** Mengidentifikasi bahwa variabel target `sleep_disorder_risk` bersifat *imbalanced* (tidak seimbang), di mana kelas 'Severe' hanya merepresentasikan 4,1% dari total populasi.
*   **Kualitas Data:** Memastikan bahwa dataset bersih dari nilai yang hilang (*zero missing values*) berdasarkan analisis eksploratif awal.

## 3. Data Preparation (Persiapan Data)
Tahap penyiapan data agar siap diproses oleh algoritma *machine learning*.

*   **Feature Selection:** Menyeleksi atribut yang secara logis berkaitan dengan gaya hidup (*caffeine_mg_before_bed*, *screen_time_before_bed_mins*, *exercise_day*, dll.) dan menghapus atribut identifier yang tidak relevan seperti `person_id`.
*   **Handling Imbalanced Data:** Karena kelas target tidak seimbang, disiapkan strategi penanganan bobot kelas menggunakan parameter internal CatBoost (`auto_class_weights='Balanced'`) agar model tidak bias terhadap kelas mayoritas ('Healthy').
*   **Data Splitting:** Membagi *dataset* ke dalam *Training Set* (untuk melatih model, misal 80%) dan *Testing Set* (untuk evaluasi, misal 20%).
*   *Catatan Khusus:* Karena CatBoost memiliki fitur *native categorical handling*, proses *encoding* manual (seperti One-Hot Encoding) untuk variabel seperti `gender` atau `occupation` dapat diminimalisir untuk menjaga integritas data awal.

## 4. Modeling (Pemodelan)
Tahap penerapan algoritma pada data yang sudah dipersiapkan.

*   **Pemilihan Algoritma:** Menggunakan **CatBoost Classifier** sebagai model utama karena keunggulannya dalam memproses data tabular dengan banyak fitur kategorikal.
*   **Hyperparameter Tuning:** Melakukan optimasi parameter CatBoost (seperti *learning rate*, *depth*, *iterations*) untuk mendapatkan performa klasifikasi terbaik.
*   **Integrasi XAI (SHAP):** Setelah model utama dilatih, objek `TreeExplainer` dari *library* SHAP diinisialisasi dan diintegrasikan dengan model CatBoost untuk mulai menghitung *Shapley values* pada *dataset* uji.

## 5. Evaluation (Evaluasi)
Tahap pengujian menyeluruh terhadap model dan hasil interpretasinya. Tahap ini dibagi menjadi dua aspek evaluasi:

*   **A. Evaluasi Performa Klasifikasi (Kuantitatif):**
    *   Mengukur metrik *Accuracy, Precision, Recall*, dan *F1-Score*.
    *   Menganalisis *Confusion Matrix* untuk melihat tingkat kesalahan prediksi pada setiap kelas (terutama kelas minoritas 'Severe').
*   **B. Evaluasi Interpretabilitas XAI (Kualitatif/Visual):**
    *   **SHAP Summary Plot:** Mengevaluasi urutan (ranking) kepentingan fitur secara global. Manakah faktor gaya hidup yang paling mendominasi secara keseluruhan?
    *   **SHAP Force Plot / Waterfall Plot:** Mengevaluasi interpretasi secara lokal (per individu). Menganalisis *use case* spesifik untuk melihat bagaimana model menjelaskan risiko pasien A dibandingkan pasien B.
    *   **SHAP Dependence Plot:** Menganalisis korelasi antara nilai fitur tertentu (misal: penambahan jam *screen time*) terhadap peningkatan risiko.

## 6. Deployment (Penyebaran / Pelaporan)
Tahap akhir di mana hasil penelitian disusun menjadi output yang siap digunakan atau dilaporkan.

*   **Dokumentasi Insight:** Menerjemahkan visualisasi matematis SHAP ke dalam narasi klinis/medis yang mudah dipahami.
*   **Penyusunan Laporan Skripsi:** Menyajikan seluruh temuan, mulai dari performa model hingga identifikasi faktor risiko, dalam bentuk analisis di Bab IV dan Kesimpulan di Bab V.
*   **Rekomendasi Praktis:** Memberikan rekomendasi berbasis data terkait gaya hidup apa saja yang perlu dihindari oleh individu untuk meminimalisir risiko gangguan tidur.
