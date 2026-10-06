# Tinjauan Pustaka / State of the Art (SOTA)

## Tabel Perbandingan State of the Art

| No | Peneliti (Tahun) | Judul Penelitian | Algoritma / Metode | Metode XAI | Domain | Dataset | Hasil Utama | Celah (*Gap*) |
|----|-----------------|------------------|-------------------|------------|--------|---------|-------------|--------------|
| 1 | Taher & Ayon (2024) | Exploring Sleep Disorders: A Comparative Analysis of Machine Learning Algorithms on Sleep Health and Lifestyle Data | Random Forest, AdaBoost, Gradient Boosting, Logistic Regression | ❌ Tidak ada | Gangguan Tidur | Sleep Health and Lifestyle Dataset | Gradient Boosting mencapai akurasi tertinggi 93,80% | Model bersifat *black-box*; tidak dapat menjelaskan faktor risiko spesifik per individu |
| 2 | Lin et al. (2025) | Evaluation of Sleep Quality and Influencing Factors among Medical and Non-Medical Students Using ML Techniques | ANN, Decision Tree, Gradient Boosting Trees, Naive Bayes | ❌ Tidak ada | Kualitas Tidur | Data survei 20.645 mahasiswa, Fujian, Tiongkok | Model ML berhasil memetakan faktor kualitas tidur mahasiswa | Analisis hanya di level populasi; tidak ada penjelasan risiko per individu |
| 3 | Ha et al. (2023) | Predicting the Risk of Sleep Disorders Using a Machine Learning–Based Simple Questionnaire: Development and Validation Study | XGBoost | ✅ SHAP (untuk seleksi fitur) | Gangguan Tidur (OSA, COMISA, Insomnia) | Data klinis 4.622 pasien dari 2 rumah sakit (Samsung MC & EUMCSH) | AUROC >0.897 untuk ketiga gangguan tidur; menghasilkan kuesioner SLEEPS 9 item | Menggunakan XGBoost (bukan CatBoost) yang memerlukan *encoding* manual; fitur berasal dari kuesioner klinis, bukan metrik gaya hidup harian; SHAP hanya digunakan untuk seleksi fitur, bukan untuk penjelasan prediksi per individu |
| 4 | Chen et al. (2024) | Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost | XGBoost dan *Partial Least Squares* | ✅ SHAP | Kualitas Tidur | Data kuesioner gaya hidup mahasiswa | XGBoost mengidentifikasi faktor risiko tidur utama | Transformasi *one-hot encoding* memecah fitur, menyebabkan interpretasi SHAP terfragmentasi dan membingungkan |
| 5 | Srinivasu et al. (2024) | XAI-driven CatBoost Multi-Layer Perceptron Neural Network for Analyzing Breast Cancer | CatBoost + MLP dengan seleksi fitur ANOVA | ✅ SHAP | Kanker Payudara | Breast Cancer Wisconsin Diagnostic (WDBC) | Akurasi 99,3%; SHAP memetakan kontribusi fitur terhadap diagnosis | Domain kanker payudara dengan fitur laboratorium yang tidak *modifiable* |

---

## Narasi Tinjauan Pustaka

### 1. Taher & Ayon (2024)

Taher & Ayon (2024) melakukan analisis komparatif terhadap empat algoritma *machine learning* — Random Forest, AdaBoost, Logistic Regression, dan Gradient Boosting — untuk mengklasifikasikan gangguan tidur berdasarkan data gaya hidup dan kesehatan. Penelitian ini menggunakan *Sleep Health and Lifestyle Dataset* dengan proses *preprocessing* yang meliputi *label encoding* untuk variabel kategorikal dan *MinMax scaling* untuk normalisasi data. Melalui optimasi *hyperparameter* dan validasi *K-Fold Cross Validation*, algoritma **Gradient Boosting** mencapai akurasi tertinggi sebesar **93,80%**, mengungguli Random Forest (90,26%) dan AdaBoost (91,15%).

**Celah yang ditemukan (GAP 1 — Prediksi Tanpa Panduan Tindakan):**
Model yang dihasilkan mampu memprediksi *bahwa* seseorang berisiko gangguan tidur, tetapi **tidak mampu menjelaskan *mengapa*** orang tersebut berisiko. Dalam konteks klinis, ini berarti seorang dokter menerima informasi "Pasien A berisiko tinggi gangguan tidur", tetapi **tidak mengetahui faktor gaya hidup mana yang harus diintervensi** — apakah karena durasi tidurnya yang terlalu pendek, konsumsi kafeinnya yang berlebihan, atau tingkat stresnya yang tinggi. Tanpa kemampuan menjelaskan prediksi, model hanya berfungsi sebagai alarm tanpa panduan tindakan (*prediction without actionable insight*).

### 2. Lin et al. (2025)

Lin et al. (2025) mengevaluasi kualitas tidur dan faktor-faktor yang mempengaruhinya di kalangan 20.645 mahasiswa kedokteran dan non-kedokteran di Provinsi Fujian, Tiongkok, selama pandemi COVID-19. Penelitian ini menggunakan instrumen *Pittsburgh Sleep Quality Index* (PSQI) dan kuesioner gaya hidup yang dianalisis menggunakan beberapa teknik *machine learning*, termasuk *Artificial Neural Network* (ANN), *Decision Tree*, *Gradient Boosting Trees*, dan *Naive Bayes*. Hasil penelitian menunjukkan bahwa mahasiswa non-kedokteran memiliki kualitas tidur yang lebih buruk, dengan faktor-faktor seperti konsumsi kopi, kebiasaan begadang, dan penggunaan internet berlebihan teridentifikasi sebagai prediktor utama.

**Celah yang ditemukan (GAP 2 — Analisis Populasi Tanpa Personalisasi):**
Temuan Lin et al. hanya berlaku di **tingkat populasi** (*global interpretation*) — yaitu, "secara umum, konsumsi kopi mempengaruhi kualitas tidur mahasiswa." Namun, penelitian ini **tidak mampu memberikan penjelasan di tingkat individu** (*local interpretation*). Artinya, jika dua pasien sama-sama diprediksi berisiko, model tidak dapat menunjukkan bahwa untuk Pasien A, faktor dominannya adalah stres kerja, sedangkan untuk Pasien B, faktor dominannya adalah konsumsi alkohol. Tanpa penjelasan per individu, dokter hanya bisa memberikan saran umum yang sama kepada semua pasien, padahal setiap orang memiliki kombinasi faktor risiko yang berbeda-beda.

### 3. Ha et al. (2023)

Ha et al. (2023) mengembangkan kuesioner sederhana bernama **SLEEPS** untuk memprediksi risiko tiga gangguan tidur — *Obstructive Sleep Apnea* (OSA), *Comorbid Insomnia and Sleep Apnea* (COMISA), dan insomnia — menggunakan algoritma **XGBoost** dan metode **SHAP**. Data diperoleh dari 4.257 pasien Samsung Medical Center dan 365 pasien Ewha Womans University Medical Center Seoul Hospital. SHAP digunakan untuk menyeleksi 9 fitur paling penting dari 30 fitur awal (5 item kuesioner ISI dan 4 karakteristik demografis). Hasilnya, model mencapai **AUROC >0,897** untuk ketiga gangguan tidur dan sebuah website publik dibuat untuk memfasilitasi prediksi risiko.

**Celah yang ditemukan (GAP 3 — Keterbatasan Algoritma, Data, dan Pemanfaatan SHAP):**
Meskipun Ha et al. telah berhasil mengombinasikan XGBoost dan SHAP di domain gangguan tidur, terdapat **tiga celah spesifik** yang tersisa. **Pertama**, algoritma yang digunakan adalah XGBoost yang **memerlukan *encoding* manual** (seperti *one-hot encoding*) untuk fitur kategorikal — proses yang rentan menimbulkan bias ordinal dan meningkatkan dimensi data, berbeda dengan CatBoost yang mampu memproses fitur kategorikal secara *native*. **Kedua**, fitur-fitur yang dianalisis berasal dari **kuesioner klinis dan data antropometrik** (skor ISI, usia, BMI, berat badan), bukan metrik gaya hidup sehari-hari (*daily lifestyle metrics*) seperti konsumsi kafein, durasi paparan layar, atau tingkat aktivitas fisik — yang bersifat *modifiable* dan dapat langsung ditindaklanjuti oleh pasien. **Ketiga**, SHAP hanya dimanfaatkan untuk **seleksi fitur** (*feature selection*), bukan untuk **menjelaskan prediksi individu secara real-time** melalui visualisasi interaktif yang dapat dipahami oleh tenaga kesehatan.

### 4. Chen et al. (2024)

Chen et al. (2024) menginvestigasi faktor-faktor yang memengaruhi kualitas tidur mahasiswa menggunakan kombinasi algoritma **XGBoost** dan metode **SHAP** untuk interpretabilitas. Karena XGBoost tidak dapat memproses data kategori secara langsung, seluruh fitur gaya hidup yang bersifat nominal ditransformasi menggunakan teknik *one-hot encoding*. Model XGBoost yang dihasilkan berhasil mengidentifikasi durasi tidur, tingkat stres, dan kebiasaan layar gawai sebagai faktor dominan yang memengaruhi kualitas tidur.

**Celah yang ditemukan (GAP 4 — Fragmentasi Interpretasi Klinis akibat *Encoding*):**
Penelitian ini mengekspos kelemahan fundamental dari penggunaan algoritma ML konvensional pada data gaya hidup yang kaya akan fitur kategori. Karena XGBoost mewajibkan transformasi *one-hot encoding*, satu fitur utuh (misalnya "Jenis Pekerjaan" atau "Tingkat Stres") terpecah menjadi puluhan variabel tiruan (*dummy variables*). Akibatnya, saat SHAP membedah prediksi tersebut, **hasil yang keluar sangat terfragmentasi** dan kehilangan konteks medis aslinya. Dokter atau pasien tidak lagi mendapatkan kesimpulan holistik tentang satu kebiasaan secara utuh, melainkan dipaksa menafsirkan pecahan-pecahan variabel biner (seperti "Apakah bukan pekerja shift = 1") yang sangat membingungkan dan tidak intuitif untuk dijadikan panduan intervensi klinis.

### 5. Das et al. (2025)

Das et al. (2025) mengevaluasi performa enam algoritma *machine learning* (KNN, RF, SVM, GBM, XGBoost, dan CatBoost) yang dilengkapi dengan metode **SHAP** untuk memprediksi risiko insomnia pada 1.222 pasien penyakit kronis di Bangladesh. Penelitian yang dipublikasikan pada jurnal bereputasi *Nature and Science of Sleep* (Scopus Q1) ini membuktikan bahwa **CatBoost meraih performa tertinggi** dengan akurasi 71,67%, AUC 77,27%, dan F1-score 71,23%, mengungguli seluruh model lainnya. Analisis SHAP berhasil memetakan faktor durasi tidur malam dan pemenuhan kebutuhan kesehatan mental sebagai prediktor terkuat insomnia.

**Celah yang ditemukan (GAP 5 — Target Biner, Populasi Terbatas, dan Ketiadaan Penjelasan Lokal Real-Time):**
Meskipun Das et al. (2025) telah berhasil membuktikan superioritas CatBoost dan SHAP langsung pada domain insomnia, terdapat empat celah riset spesifik yang tersisa. **Pertama**, target klasifikasi masih bersifat **biner sederhana** (*Insomnia vs Non-Insomnia*), belum membedakan tingkatan keparahan risiko secara bertingkat (*multi-class: Healthy, Mild, Moderate, Severe*). **Kedua**, populasi studi terbatas pada pasien penyakit kronis rumah sakit dengan sampel 1.222 data yang memerlukan teknik *oversampling* sintetis SMOTE, berbeda dengan penelitian ini yang menguji **100.000 rekaman data populasi umum gaya hidup digital** dengan pendekatan *cost-sensitive learning* alami CatBoost. **Ketiga**, visualisasi SHAP hanya disajikan pada **tingkat agregat populasi global** (*Summary Beeswarm Plot*), bukan untuk memberikan **penjelasan lokal (*Waterfall Plot*) per pasien secara interaktif**. **Keempat**, penelitian tersebut berhenti pada laporan artikel ilmiah tanpa diimplementasikan ke dalam **prototipe sistem pendukung keputusan klinis (CDSS) berbasis web**.

---

## Sintesis dan Identifikasi 5 Research GAP

Berdasarkan tinjauan terhadap kelima penelitian di atas, teridentifikasi **lima celah riset (*research gap*) yang spesifik dan saling melengkapi**:

### GAP 1: Prediksi Tanpa Panduan Tindakan (*Prediction Without Actionable Insight*)
Taher & Ayon (2024) meneliti klasifikasi gangguan tidur menggunakan algoritma *machine learning* konvensional seperti Gradient Boosting yang dioptimasi pada dataset kesehatan dan gaya hidup, namun celah yang ditemukan adalah model klasifikasi tersebut beroperasi sepenuhnya sebagai *black-box* yang hanya mampu mendeteksi tingkat risiko secara global tanpa mampu menjelaskan faktor penyebab spesifik secara individual, sehingga tidak memberikan panduan intervensi klinis yang dapat langsung ditindaklanjuti oleh dokter maupun pasien.

### GAP 2: Analisis Populasi Tanpa Personalisasi Individu
Lin et al. (2025) meneliti faktor-faktor eksternal yang memengaruhi kualitas tidur menggunakan berbagai pemodelan *machine learning* prediktif berbasis kuesioner pada skala yang sangat besar, namun celah riset yang ditemukan adalah analisis prediksi tersebut hanya relevan pada kesimpulan tingkat populasi umum secara agregat dan belum mampu memberikan penjelasan secara personal untuk masing-masing individu dengan kombinasi risiko gaya hidup yang sangat unik dan berbeda-beda.

### GAP 3: Keterbatasan Algoritma, Jenis Data, dan Pemanfaatan SHAP
Ha et al. (2023) meneliti prediksi risiko gangguan tidur klinis menggunakan algoritma XGBoost dan metode SHAP berbasis data kuesioner medis, namun celah yang ditemukan adalah model tersebut memerlukan tahapan *encoding* manual yang rentan terhadap bias ordinal, masih sangat bergantung pada data kuesioner medis statis, serta hanya memanfaatkan metode SHAP sebatas untuk tahapan seleksi fitur di awal alih-alih digunakan untuk memberikan penjelasan prediksi interaktif secara *real-time*.

### GAP 4: Fragmentasi Interpretasi Klinis akibat *Encoding* Kategorikal
Chen et al. (2024) meneliti faktor risiko kualitas tidur menggunakan XGBoost dan metode SHAP, namun celah riset utama yang ditemukan adalah algoritma tersebut memaksa penggunaan *one-hot encoding* yang memecah belah struktur data gaya hidup nominal, sehingga penjelasan kontribusi SHAP yang dihasilkan menjadi sangat terfragmentasi, kehilangan konteks utuhnya, dan sulit diterjemahkan menjadi panduan klinis yang intuitif bagi tenaga kesehatan maupun pasien.

### GAP 5: Klasifikasi Biner, Populasi Terbatas, dan Ketiadaan XAI Lokal Real-Time
Das et al. (2025) memvalidasi keunggulan CatBoost dan SHAP langsung pada kasus insomnia, namun pemodelan masih terbatas pada klasifikasi biner pasien komorbid rumah sakit, analisis SHAP hanya di tingkat agregat global, serta belum dikembangkan menjadi sistem pendukung keputusan klinis berbasis web yang interaktif.

### Tabel Pemetaan GAP

| Kriteria | Taher & Ayon (2024) | Lin et al. (2025) | Ha et al. (2023) | Chen et al. (2024) | Das et al. (2025) | **Penelitian Ini** |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Domain Gangguan Tidur | ✅ | ✅ | ✅ | ✅ | ✅ | **✅ (100% Homogen)** |
| Algoritma CatBoost (*native* kategorikal) | ❌ | ❌ | ❌ (XGBoost) | ❌ (XGBoost) | ✅ | **✅** |
| Target Multi-Kelas 4 Tingkat Risiko | ❌ (Biner) | ❌ (Skor PSQI) | ❌ (Biner) | ❌ (Regresi) | ❌ (Biner) | **✅ (4 Tingkat)** |
| Skala Dataset (100.000 Rekaman Data) | ❌ (374 data) | ✅ (20.645 data) | ❌ (4.622 data) | ❌ (Kuesioner) | ❌ (1.222 data) | **✅ (100.000 Data)** |
| Data Gaya Hidup Digital (*Modifiable*) | ✅ | ✅ | ❌ (Kuesioner klinis) | ✅ | ❌ (Pasien Kronis RS) | **✅** |
| Metode SHAP Berhasil Diimplementasikan | ❌ | ❌ | ✅ (seleksi fitur saja) | ✅ (Terfragmentasi) | ✅ (Summary Global) | **✅** |
| SHAP untuk Penjelasan Individu Real-Time | ❌ | ❌ | ❌ | ❌ | ❌ (Hanya Global) | **✅ (Waterfall Plot)** |
| Implementasi Sistem Web Interaktif (CDSS) | ❌ | ❌ | ✅ (Website statis) | ❌ | ❌ | **✅ (CDSS Tailwind)** |
| **Seluruh Kriteria Terpenuhi** | ❌ | ❌ | ❌ | ❌ | ❌ | **✅ (PENUH)** |

### Pernyataan Research GAP

> Penelitian-penelitian terdahulu telah membuktikan bahwa *machine learning* mampu mengklasifikasi risiko gangguan tidur secara akurat (Taher & Ayon, 2024; Lin et al., 2025), dan bahwa kombinasi algoritma CatBoost dengan SHAP terbukti paling unggul dalam memprediksi insomnia (Das et al., 2025). Namun, terdapat **lima celah riset yang belum terisi secara simultan**: (1) model klasifikasi gangguan tidur yang ada **hanya mendeteksi risiko tanpa menjelaskan faktor penyebab spesifik** yang dapat ditindaklanjuti; (2) analisis risiko masih di **level populasi umum, bukan personalisasi individu**; (3) penelitian terdekat di domain tidur menggunakan **XGBoost (bukan CatBoost)** dengan fitur kuesioner medis statis dan SHAP hanya untuk seleksi fitur (Ha et al., 2023); (4) keharusan menggunakan *one-hot encoding* pada XGBoost (Chen et al., 2024) menyebabkan **hasil SHAP terfragmentasi** sehingga merusak interpretasi klinis yang holistik; dan (5) penelitian CatBoost-SHAP pada tidur (Das et al., 2025) masih **terbatas pada target biner pasien kronis rumah sakit** tanpa eksplanasi lokal *real-time* dan tanpa implementasi sistem terapan. Penelitian ini mengisi kelima celah tersebut secara simultan.

---

## Referensi Lengkap (5 Jurnal)

1. Taher, A., & Ayon, W. I. Z. (2024). Exploring Sleep Disorders: A Comparative Analysis of Machine Learning Algorithms on Sleep Health and Lifestyle Data. *2024 IEEE PEEIACON*.
2. Lin, Y., et al. (2025). Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. *Frontiers in Psychiatry*, 16, 1533875.
3. Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the Risk of Sleep Disorders Using a Machine Learning–Based Simple Questionnaire: Development and Validation Study. *Journal of Medical Internet Research*, 25, e46520.
4. Chen, T., et al. (2024). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Public Health*, 12, 1373504.
5. Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A. A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025). Prevalence and Factors Associated with Insomnia Among Chronic Disease Patients in Bangladesh: A Machine Learning Study. *Nature and Science of Sleep*, 17, 2541–2567. https://doi.org/10.2147/NSS.S547335
