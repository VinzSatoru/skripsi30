# Simulasi Pertanyaan Kritis Dosen Pembimbing
## Saat Pengajuan Judul & Proposal Outline

**Judul:**  
*"Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Identifikasi Faktor Risiko Gangguan Tidur"*

---

## 1. PERTANYAAN SEPUTAR URGENSI & MOTIVASI

### Q1: "Apa urgensi penelitian ini? Kenapa harus gangguan tidur?"

**Jawaban:**
> "Gangguan tidur merupakan masalah kesehatan global yang prevalensinya terus meningkat. WHO mencatat sekitar 40% populasi global mengalami masalah tidur, dan di Indonesia sendiri prevalensinya mencapai 10-30%. Dampaknya bukan sekadar kantuk, tetapi meningkatkan risiko penyakit kardiovaskular, diabetes tipe 2, serta gangguan mental. Ironisnya, faktor pemicunya—seperti screen time, konsumsi kafein, dan tekanan kerja—sebenarnya sudah tercatat dalam data gaya hidup digital yang kita hasilkan setiap hari, tetapi belum dimanfaatkan secara maksimal untuk deteksi dini. Penelitian ini hadir untuk mengubah data gaya hidup tersebut menjadi sistem identifikasi faktor risiko yang bisa dipahami oleh tenaga kesehatan."

---

### Q2: "Kenapa tidak langsung ke dokter saja? Apa gunanya machine learning untuk masalah tidur?"

**Jawaban:**
> "Dokter memang bisa mendiagnosis gangguan tidur, tetapi sifatnya reaktif—pasien harus datang dan mengeluh dulu. Yang kami tawarkan adalah pendekatan preventif dan personal. Dengan data gaya hidup yang sudah ada (durasi tidur, screen time, kafein, stres), model CatBoost bisa mengklasifikasikan risiko gangguan tidur secara otomatis. Yang lebih penting, SHAP memberikan penjelasan **per individu**—misalnya untuk pasien A, faktor utamanya adalah screen time berlebihan, sementara pasien B karena konsumsi kafein tinggi. Informasi ini bisa menjadi bahan skrining awal sebelum pasien dirujuk ke spesialis."

---

## 2. PERTANYAAN SEPUTAR ALGORITMA & METODE

### Q3: "Kenapa CatBoost? Kenapa bukan Random Forest, XGBoost, atau Neural Network?"

**Jawaban:**
> "Ada tiga alasan teknis utama, Pak/Bu:
> 
> **Pertama**, dataset ini kaya akan fitur kategorikal seperti occupation (12 kategori), chronotype, mental health condition, dan country. CatBoost memiliki kemampuan **native categorical handling** — artinya bisa memproses fitur kategorikal langsung tanpa encoding manual seperti One-Hot Encoding yang bisa menyebabkan curse of dimensionality.
> 
> **Kedua**, CatBoost menggunakan teknik **Ordered Boosting** yang mengurangi overfitting dibandingkan XGBoost, terutama penting untuk dataset dengan kelas imbalanced seperti milik kami (kelas Severe hanya 4,1%).
> 
> **Ketiga**, CatBoost memiliki integrasi yang sangat baik dengan SHAP — library SHAP menyediakan `TreeExplainer` yang dioptimalkan khusus untuk model berbasis tree seperti CatBoost, sehingga perhitungan SHAP values menjadi sangat cepat bahkan pada 100.000 data."

---

### Q4: "Apa itu SHAP? Jelaskan secara sederhana."

**Jawaban:**
> "SHAP adalah singkatan dari SHapley Additive exPlanations. Konsepnya berasal dari **teori permainan** oleh Lloyd Shapley (peraih Nobel Ekonomi 2012).
> 
> Analoginya seperti ini: bayangkan sebuah tim sepak bola memenangkan pertandingan. Pertanyaannya, berapa kontribusi setiap pemain terhadap kemenangan? SHAP menjawab pertanyaan ini dengan cara menghitung kontribusi setiap 'pemain' (fitur) terhadap 'kemenangan' (prediksi).
> 
> Secara teknis, SHAP menghitung kontribusi marginal setiap fitur dengan mempertimbangkan semua kemungkinan kombinasi fitur lainnya. Hasilnya berupa **SHAP values** yang menunjukkan:
> - Fitur mana yang paling berpengaruh (secara global)
> - Untuk setiap individu, fitur mana yang mendorong prediksinya ke arah risiko tinggi atau rendah (secara lokal)
> 
> Inilah yang membedakan SHAP dari Feature Importance biasa — SHAP memberikan penjelasan di level individu, bukan hanya ranking umum."

---

### Q5: "Kenapa SHAP dan bukan metode XAI lain seperti LIME atau Feature Importance?"

**Jawaban:**
> "Ada tiga metode XAI yang umum: Feature Importance, LIME, dan SHAP. Berikut perbandingannya:
> 
> | Metode | Kelebihan | Kekurangan |
> |---|---|---|
> | Feature Importance | Cepat, sederhana | Hanya ranking global, tidak bisa per individu, bisa bias pada fitur numerik |
> | LIME | Bisa per individu | Tidak konsisten — hasil bisa berubah tiap dijalankan karena berbasis sampling acak |
> | **SHAP** | **Konsisten secara matematis**, bisa global & lokal, adil (berbasis teori Shapley) | Lebih lambat (tapi sudah diatasi dengan TreeExplainer) |
> 
> SHAP dipilih karena memiliki **landasan matematis** yang paling kuat (teori permainan koalisi), menghasilkan penjelasan yang **konsisten** dan **adil**, serta mampu memberikan interpretasi baik di level populasi maupun individu."

---

### Q6: "Apa bedanya penelitian Anda dengan yang menggunakan Feature Importance biasa?"

**Jawaban:**
> "Feature Importance biasa (misalnya dari Random Forest) hanya memberikan ranking umum: 'fitur X paling penting.' Tapi tidak bisa menjawab **bagaimana** dan **untuk siapa**.
> 
> Contoh konkret dari dataset kami:
> - Feature Importance: 'screen time adalah fitur ke-3 terpenting'
> - SHAP: 'Untuk pasien A yang berusia 25 tahun dan seorang programmer, screen time 180 menit/malam **meningkatkan** risiko gangguan tidurnya sebesar 0.35 poin ke arah Severe, sementara kebiasaan olahraganya **menurunkan** risiko sebesar 0.2 poin'
> 
> Dengan SHAP, tenaga kesehatan bisa memberikan rekomendasi yang **personal** — bukan saran umum seperti 'kurangi screen time', tapi 'Anda perlu menurunkan screen time dari 180 ke 60 menit karena itu faktor dominan nomor 1 untuk kasus Anda.'"

---

## 3. PERTANYAAN SEPUTAR DATASET

### Q7: "Datanya dari mana? Apakah valid?"

**Jawaban:**
> "Dataset yang digunakan bersumber dari repositori publik (Kaggle) dengan jumlah 100.000 baris dan 32 kolom. Dataset ini bersifat sintetis tetapi disimulasikan berdasarkan pola distribusi data kesehatan nyata. Dalam konteks penelitian machine learning, penggunaan dataset publik dan sintetis sangat umum dan diterima secara akademis — seperti halnya dataset Iris, MNIST, atau Boston Housing yang telah digunakan dalam ribuan paper akademik. Yang penting adalah dataset ini memiliki fitur-fitur yang relevan secara medis dan memiliki distribusi yang realistis."

---

### Q8: "100.000 data itu banyak sekali. Kenapa tidak pakai data asli dari rumah sakit?"

**Jawaban:**
> "Penggunaan data rumah sakit memerlukan proses ethical clearance dan perizinan yang memakan waktu sangat lama serta di luar cakupan penelitian ini. Selain itu, fokus penelitian ini bukan pada validasi klinis, melainkan pada **pembuktian konsep (proof of concept)** bahwa metode XAI-SHAP mampu mengidentifikasi faktor gaya hidup penyebab gangguan tidur secara transparan. Ukuran 100.000 data justru menjadi keunggulan karena memberikan kekuatan statistik yang sangat tinggi untuk melatih model CatBoost dan menghasilkan SHAP values yang stabil dan reliable."

---

### Q9: "Data ini imbalanced (kelas Severe hanya 4%). Bagaimana mengatasinya?"

**Jawaban:**
> "Benar, distribusi target memang tidak seimbang: Healthy (54,2%), Mild (33,5%), Moderate (8,3%), dan Severe (4,1%). Strategi penanganan yang akan saya gunakan adalah parameter `auto_class_weights='Balanced'` pada CatBoost, yang secara otomatis memberikan bobot lebih besar pada kelas minoritas saat proses training. Pendekatan ini dipilih karena:
> 1. Tidak mengubah distribusi data asli (berbeda dengan SMOTE yang menciptakan data sintetis tambahan)
> 2. Lebih kompatibel dengan analisis SHAP — karena SHAP menganalisis data asli, bukan data sintetis
> 3. Terintegrasi langsung dalam CatBoost tanpa library tambahan
> 
> Sebagai analisis tambahan, saya juga bisa membandingkan performa model dengan dan tanpa penanganan imbalanced sebagai bahan diskusi di Bab IV."

---

## 4. PERTANYAAN SEPUTAR NOVELTY & GAP

### Q10: "Apa novelty penelitian Anda? Apa bedanya dengan penelitian yang sudah ada?"

**Jawaban:**
> "Novelty penelitian ini terletak pada **tiga aspek** yang belum pernah digabungkan dalam satu penelitian:
> 
> 1. **Domain**: Penerapan XAI pada klasifikasi gangguan tidur berbasis gaya hidup — literatur yang ada masih didominasi domain kardiovaskular dan kanker (Emhandyksa & Afifah, 2026; Srinivasu et al., 2024)
> 2. **Metode**: Kombinasi CatBoost + SHAP — penelitian sebelumnya oleh Taher & Ayon (2024) menggunakan Gradient Boosting tanpa XAI, dan Lin et al. (2025) menggunakan ANN yang bersifat black-box
> 3. **Tujuan**: Bukan sekadar mencapai akurasi tinggi, tapi **mengidentifikasi dan meranking faktor gaya hidup** yang paling berpengaruh terhadap risiko gangguan tidur — informasi yang secara langsung actionable bagi tenaga kesehatan
> 
> Jadi gap-nya jelas: belum ada yang menerapkan SHAP pada CatBoost khusus untuk membedah faktor gaya hidup pemicu gangguan tidur."

---

### Q11: "Bukankah sudah banyak penelitian tentang sleep disorder dan machine learning?"

**Jawaban:**
> "Benar, sudah banyak penelitian ML untuk sleep disorder, tapi mayoritas berhenti pada **metrik akurasi** saja — 'model kami akurat 93%' tanpa menjelaskan MENGAPA model memprediksi demikian. Ini yang disebut sebagai masalah black-box.
> 
> Penelitian saya berbeda karena tidak berhenti di angka akurasi. Dengan SHAP, saya menambahkan lapisan **transparansi** yang menghasilkan output berupa:
> - Summary Plot: ranking faktor gaya hidup secara global
> - Force Plot: penjelasan per individu mengapa seseorang diklasifikasikan berisiko tinggi
> - Dependence Plot: bagaimana hubungan antara satu fitur (misal kafein) dengan risiko gangguan tidur
> 
> Informasi ini yang belum tersedia di penelitian-penelitian sebelumnya."

---

## 5. PERTANYAAN SEPUTAR METODOLOGI

### Q12: "Metode penelitian apa yang Anda gunakan? CRISP-DM itu apa?"

**Jawaban:**
> "Penelitian ini menggunakan pendekatan kuantitatif eksperimental dengan metodologi **CRISP-DM** (Cross-Industry Standard Process for Data Mining) yang terdiri dari 6 fase:
> 1. **Business Understanding**: Memahami masalah gangguan tidur dan kebutuhan interpretabilitas
> 2. **Data Understanding**: Eksplorasi dan analisis awal dataset 100.000 baris
> 3. **Data Preparation**: Preprocessing, handling imbalanced data, dan feature selection
> 4. **Modeling**: Training model CatBoost dengan hyperparameter tuning
> 5. **Evaluation**: Mengukur performa (Accuracy, Precision, Recall, F1-Score) + analisis SHAP
> 6. **Deployment**: Menyajikan hasil interpretasi SHAP dalam bentuk visualisasi yang actionable
> 
> CRISP-DM dipilih karena merupakan standar industri yang paling banyak digunakan untuk proyek data mining, dan bersifat iteratif sehingga memungkinkan perbaikan model secara bertahap."

---

### Q13: "Evaluasi modelnya pakai apa saja?"

**Jawaban:**
> "Evaluasi dilakukan dengan dua pendekatan:
> 
> **A. Evaluasi Performa Model (Kuantitatif):**
> - Accuracy, Precision, Recall, F1-Score (per kelas)
> - Confusion Matrix
> - Classification Report
> - Cross-Validation (k-fold) untuk memastikan model tidak overfitting
> 
> **B. Evaluasi Interpretabilitas (XAI):**
> - SHAP Summary Plot → ranking fitur global
> - SHAP Force Plot → penjelasan per individu
> - SHAP Dependence Plot → hubungan fitur-target
> - SHAP Interaction Values → interaksi antar fitur
> 
> Kombinasi kedua evaluasi ini menjawab dua pertanyaan sekaligus: 'Seberapa akurat model?' DAN 'Mengapa model memprediksi demikian?'"

---

## 6. PERTANYAAN "JEBAKAN"

### Q14: "Apakah ini penelitian kuantitatif atau kualitatif?"

**Jawaban:**
> "Ini adalah penelitian **kuantitatif** murni dengan pendekatan eksperimental komputasi. Seluruh proses penelitian menggunakan data numerik dan terukur — mulai dari dataset (100.000 baris angka), proses analisis (algoritma machine learning), hingga hasilnya berupa metrik numerik (akurasi, SHAP values). Tidak ada proses wawancara, observasi, atau analisis teks yang bersifat kualitatif."

---

### Q15: "Outputnya apa? Apakah Anda membuat aplikasi?"

**Jawaban:**
> "Output utama penelitian ini adalah:
> 1. **Model CatBoost** yang sudah terlatih untuk mengklasifikasikan risiko gangguan tidur
> 2. **Analisis SHAP** berupa visualisasi ranking faktor gaya hidup dan penjelasan per individu
> 3. **Insight medis** berupa daftar faktor gaya hidup yang paling berpengaruh terhadap gangguan tidur
> 
> Penelitian ini fokus pada pembuktian konsep dan analisis, bukan pada pembuatan aplikasi. Namun, hasil analisis ini bisa menjadi **fondasi** untuk pengembangan sistem skrining tidur di penelitian selanjutnya."

---

### Q16: "Kalau hasilnya akurasi rendah bagaimana?"

**Jawaban:**
> "Pertanyaan yang sangat valid. Namun, perlu dipahami bahwa fokus utama penelitian ini bukan pada pencapaian akurasi tertinggi, melainkan pada **interpretabilitas** — memahami faktor apa saja yang menyebabkan gangguan tidur.
> 
> Meskipun demikian, berdasarkan studi awal yang sudah saya lakukan, CatBoost pada dataset ini mencapai akurasi **di atas 90%**. Ini karena dataset memiliki fitur-fitur yang sangat relevan secara medis (stress score, sleep quality, screen time, dll) dan ukuran data 100.000 yang memberikan kekuatan statistik tinggi.
> 
> Bahkan jika akurasi tidak setinggi itu pun, selama SHAP berhasil mengidentifikasi faktor-faktor dominan secara konsisten, penelitian ini tetap memberikan kontribusi yang berharga karena menjawab pertanyaan 'MENGAPA', bukan sekadar 'BERAPA'."

---

## TIPS MENGHADAPI DOSEN

1. **Jangan menghafal jawaban** — pahami konsepnya, lalu jelaskan dengan kata-kata sendiri
2. **Bawa print-out proposal** dan contoh visualisasi SHAP (summary plot, force plot) untuk ditunjukkan
3. **Jika tidak tahu jawabannya**, katakan: *"Itu poin yang sangat menarik, Pak/Bu. Saya akan mendalami hal itu dan menjadikannya bahan analisis di Bab IV"*
4. **Selalu kaitkan dengan gap penelitian**: setiap jawaban harus kembali ke poin bahwa kombinasi SHAP + CatBoost pada domain gangguan tidur **belum pernah dilakukan**
5. **Tunjukkan bahwa Anda sudah eksplorasi data**: sebutkan jumlah data (100K), jumlah fitur (32), dan distribusi target untuk menunjukkan Anda sudah riset
