# OUTLINE PROPOSAL SKRIPSI

**PROGRAM STUDI TEKNIK INFORMATIKA**  
**FAKULTAS SAINS DAN TEKNOLOGI**  
**UNIVERSITAS ISLAM NAHDLATUL ULAMA (UNISNU) JEPARA**  

---

### IDENTITAS PENELITI
* **Nama Mahasiswa** : Ahmad Novian Dzulfanni  
* **NIM** : 231240001438  
* **Program Studi** : S1 Teknik Informatika  
* **Fakultas** : Sains dan Teknologi (FST)  
* **Bidang Minat** : Sains Data, Pembelajaran Mesin (*Machine Learning*), dan *Explainable Artificial Intelligence* (XAI)  

---

## 1. JUDUL PENELITIAN

**Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Klasifikasi Faktor Risiko Gangguan Tidur Berbasis Metrik Gaya Hidup Digital**

---

## 2. RUMUSAN MASALAH

Bagaimana penerapan *Shapley Additive exPlanations* (SHAP) sebagai metode *Explainable AI* (XAI) pada algoritma CatBoost dapat menghasilkan model klasifikasi risiko gangguan tidur yang akurat dan transparan, sekaligus mampu mengidentifikasi faktor-faktor gaya hidup digital yang paling berpengaruh secara personal dan mudah dipahami?

---

## 3. LATAR BELAKANG

> **Catatan Pengujian Panjang Paragraf:** Seluruh paragraf latar belakang di bawah ini telah disesuaikan secara presisi agar memenuhi batas **120–130 kata per paragraf** (antara 121 hingga 124 kata), dengan gaya bahasa yang mengalir, baku-akademis, serta mudah dipahami oleh dosen penguji maupun pembimbing.

### Paragraf 1: Urgensi Masalah Gangguan Tidur dan Kaitannya dengan Gaya Hidup Digital *(121 kata)*
Gangguan tidur saat ini telah berkembang menjadi masalah kesehatan masyarakat yang serius di era modern. Kondisi ini tidak hanya menurunkan kebugaran tubuh sehari-hari, tetapi juga berhubungan erat dengan peningkatan risiko berbagai penyakit kronis seperti gangguan kardiovaskular, diabetes, hingga depresi. Pada era serba digital, sebagian besar pemicu gangguan tidur berkaitan langsung dengan pola kebiasaan harian yang dapat diukur secara kuantitatif. Faktor-faktor tersebut meliputi durasi paparan layar gawai sebelum tidur, beban kerja, konsumsi kafein, hingga minimnya aktivitas fisik harian. Studi Lin et al. (2025) terhadap 20.645 responden membuktikan bahwa kebiasaan gaya hidup digital merupakan prediktor nyata yang dapat dipetakan secara akurat menggunakan machine learning. Temuan tersebut membuka peluang besar untuk mengembangkan sistem deteksi dini risiko gangguan tidur yang bersifat proaktif berbasis data perilaku.

### Paragraf 2: Karakteristik Data Gaya Hidup dan Keunggulan Algoritma CatBoost *(121 kata)*
Membangun sistem deteksi dini tersebut memerlukan algoritma pembelajaran mesin yang berakurasi tinggi sekaligus mampu mengolah data gaya hidup heterogen. Data gaya hidup memadukan variabel numerik seperti durasi tidur dan detak jantung dengan variabel kategorikal seperti jenis pekerjaan dan tingkat stres. Banyak algoritma konvensional seperti Random Forest atau XGBoost mengalami kendala saat memproses data kategorikal, karena membutuhkan proses encoding manual yang rentan memicu bias serta ledakan dimensi data. Algoritma CatBoost dirancang khusus untuk mengatasi masalah ini melalui mekanisme ordered target statistics yang memproses fitur kategorikal secara langsung tanpa encoding manual. Keunggulan gradient boosting terbukti pada studi Taher & Ayon (2024) yang meraih akurasi 93,80% pada klasifikasi gangguan tidur. Oleh karena itu, CatBoost sangat tepat digunakan karena selaras dengan karakteristik data gaya hidup.

### Paragraf 3: Tantangan Model Kotak Hitam (*Black-Box*) dan Urgensi XAI *(123 kata)*
Kendati memiliki akurasi yang tinggi, algoritma berbasis ensemble seperti CatBoost memiliki kelemahan utama karena beroperasi sebagai model kotak hitam atau black-box. Keputusan prediksi dihasilkan dari ratusan pohon keputusan paralel yang rumit, sehingga pengguna tidak dapat memahami alasan di balik penetapan tingkat risiko seseorang secara logis. Dalam dunia medis, ketidakmampuan model menjelaskan proses keputusannya menjadi hambatan besar bagi adopsi teknologi kecerdasan buatan klinis. Dokter maupun pasien membutuhkan landasan rasional yang transparan dan dapat dipertanggungjawabkan sebelum mengambil keputusan medis atau intervensi perilaku harian. Penelitian Ha et al. (2023) menunjukkan bahwa metode Explainable AI mampu meningkatkan keterbukaan prediksi gangguan tidur, meskipun penerapannya masih terbatas pada penyaringan kuesioner awal. Oleh sebab itu, integrasi Explainable AI menjadi kebutuhan mutlak agar model klasifikasi tidak hanya akurat, tetapi juga transparan.

### Paragraf 4: Peran Metode SHAP dalam Memberikan Penjelasan yang Adil dan Konsisten *(123 kata)*
Di antara berbagai pendekatan Explainable AI modern, metode Shapley Additive exPlanations atau SHAP dipandang paling unggul karena memiliki landasan teori permainan kooperatif yang kokoh. Berdasarkan prinsip matematis fundamental yang dirumuskan oleh Lundberg & Lee (2017), metode SHAP mampu menjamin perhitungan kontribusi setiap variabel input secara adil, konsisten, dan aditif. Keunggulan utama metode SHAP adalah kemampuannya menyajikan penjelasan pada tingkat populasi global sekaligus tingkat individu lokal secara mendalam. Efektivitas SHAP dalam menganalisis faktor penentu kualitas tidur juga telah berhasil dibuktikan secara konkret oleh Xie et al. (2026). Melalui analisis SHAP, tenaga medis maupun pasien dapat mengetahui secara pasti variabel gaya hidup mana yang paling mendorong timbulnya risiko gangguan tidur pada setiap individu, seperti tingginya tingkat stres kerja atau durasi paparan layar gawai yang berlebih.

### Paragraf 5: Identifikasi Riset Terdahulu dan Lima Celah Riset (*Research Gap*) *(126 kata)*
Meskipun berbagai penelitian terdahulu menunjukkan hasil positif, terdapat lima celah riset utama yang belum terselesaikan secara simultan. Taher & Ayon (2024) menghasilkan model berakurasi tinggi namun tanpa transparansi faktor risiko individual. Lin et al. (2025) hanya menganalisis faktor tidur pada tingkat populasi umum tanpa personalisasi per individu. Ha et al. (2023) menerapkan metode SHAP sebatas untuk seleksi fitur kuesioner statis menggunakan algoritma XGBoost. Xie et al. (2026) menggunakan teknik one-hot encoding yang memecah fitur kategorikal sehingga penjelasan SHAP terfragmentasi dan membingungkan secara klinis. Terakhir, Das et al. (2025) berhasil membuktikan keunggulan CatBoost-SHAP pada insomnia namun terbatas pada klasifikasi biner pasien kronis tanpa visualisasi lokal per individu. Belum ada penelitian yang menggabungkan keunggulan CatBoost dan SHAP untuk klasifikasi multi-kelas risiko gangguan tidur berbasis gaya hidup secara personal.

### Paragraf 6: Solusi yang Diusulkan dan Luaran Sistem Web CDSS *(123 kata)*
Berdasarkan kelima celah riset tersebut, penelitian ini mengusulkan penerapan metode Explainable AI berbasis SHAP pada algoritma CatBoost untuk klasifikasi risiko gangguan tidur berbasis metrik gaya hidup digital. Algoritma CatBoost dipilih karena memiliki keunggulan dalam mengolah data kategorikal tanpa merusak struktur data aslinya, sehingga nilai kontribusi SHAP tetap utuh dan bermakna secara klinis. Pendekatan ini diharapkan mampu mengenali pola risiko tidur secara akurat sekaligus memetakan faktor pemicu dominan pada setiap individu secara tepat. Selain itu, model yang dikembangkan akan diintegrasikan secara langsung ke dalam purwarupa sistem pendukung keputusan klinis berbasis web yang interaktif. Sistem ini dirancang agar mudah digunakan oleh masyarakat umum untuk mengenali kebiasaan buruknya, sekaligus membantu tenaga medis dalam merancang rekomendasi perubahan gaya hidup yang terarah, efektif, dan berbasis bukti ilmiah terpercaya.

---

## 4. TINJAUAN PUSTAKA (STATE OF THE ART)

Berikut adalah tinjauan terhadap lima penelitian terkini yang menjadi landasan dan pembanding utama dalam penelitian ini:

### 1. Xie et al. (2026)
* **Fokus dan Temuan:** Meneliti faktor-faktor yang memengaruhi kualitas tidur mahasiswa menggunakan kombinasi regresi *Partial Least Squares* (PLS) dan algoritma XGBoost yang dilengkapi metode SHAP. Penelitian ini berhasil mengidentifikasi bahwa durasi tidur, tingkat stres, dan kebiasaan penggunaan gawai merupakan faktor penentu utama kualitas tidur.
* **Celah Riset (*Gap*):** Algoritma XGBoost mewajibkan proses *one-hot encoding* untuk variabel kategorikal. Akibatnya, saat SHAP diterapkan, fitur gaya hidup nominal terpecah menjadi variabel tiruan biner, sehingga penjelasan kontribusi fitur menjadi terfragmentasi, kehilangan konteks aslinya, dan sulit diterjemahkan menjadi panduan perubahan perilaku yang praktis bagi pasien.

### 2. Ha et al. (2023)
* **Fokus dan Temuan:** Mengembangkan model prediksi risiko tiga jenis gangguan tidur klinis (*Obstructive Sleep Apnea*, insomnia, dan gabungan keduanya) menggunakan algoritma XGBoost dan metode SHAP berdasarkan data kuesioner medis dari 4.622 pasien di dua rumah sakit. Model menunjukkan performa yang baik dengan nilai AUROC di atas 0,897.
* **Celah Riset (*Gap*):** Model masih bergantung pada *encoding* manual dan data kuesioner medis statis, bukan metrik kebiasaan harian yang dapat diubah secara langsung oleh individu. Selain itu, metode SHAP hanya digunakan sebatas untuk seleksi fitur di tahap awal (*feature selection*), bukan untuk memberikan penjelasan prediksi interaktif per individu secara *real-time*.

### 3. Lin et al. (2025)
* **Fokus dan Temuan:** Menganalisis faktor eksternal yang memengaruhi kualitas tidur pada 20.645 mahasiswa menggunakan beberapa model *machine learning* seperti *Artificial Neural Network* (ANN), *Decision Tree*, dan *Naive Bayes*. Hasil penelitian menunjukkan adanya hubungan signifikan antara kebiasaan konsumsi kopi, begadang, dan intensitas penggunaan gawai dengan penurunan kualitas tidur.
* **Celah Riset (*Gap*):** Model yang dikembangkan bersifat *black-box* dan interpretasi yang dihasilkan hanya berlaku secara umum pada tingkat populasi (agregat). Model belum mampu memberikan penjelasan secara personal untuk masing-masing individu yang memiliki variasi faktor risiko berbeda-beda.

### 4. Das et al. (2025)
* **Fokus dan Temuan:** Menganalisis prevalensi dan faktor risiko insomnia pada 1.222 pasien penyakit kronis di Bangladesh menggunakan enam algoritma pembelajaran mesin (KNN, RF, SVM, GBM, XGBoost, dan CatBoost) serta metode SHAP. Penelitian yang dipublikasikan pada *Nature and Science of Sleep* ini membuktikan bahwa algoritma CatBoost meraih performa tertinggi (akurasi 71,67%, AUC 77,27%, dan F1-score 71,23%) dibanding model lainnya, dengan SHAP mengonfirmasi durasi tidur malam dan pemenuhan kebutuhan kesehatan mental sebagai prediktor terkuat.
* **Celah Riset (*Gap*):** Pemodelan klasifikasi yang dilakukan masih terbatas pada target biner (*Insomnia vs Non-Insomnia*) pada kelompok spesifik pasien komorbid rumah sakit dengan penanganan ketidakseimbangan kelas menggunakan oversampling sintetis SMOTE. Selain itu, eksplanasi SHAP yang disajikan hanya terbatas pada tingkat populasi global (*Summary Beeswarm Plot*) tanpa visualisasi lokal per individu (*Waterfall Plot*) secara interaktif, serta tidak dikembangkan ke dalam bentuk purwarupa sistem web terapan (*Clinical Decision Support System*).

### 5. Taher & Ayon (2024)
* **Fokus dan Temuan:** Melakukan studi komparasi algoritma *machine learning* (*Random Forest*, *AdaBoost*, dan *Gradient Boosting*) untuk klasifikasi gangguan tidur berbasis data kesehatan dan gaya hidup harian. Algoritma *Gradient Boosting* meraih performa terbaik dengan tingkat akurasi 93,80%.
* **Celah Riset (*Gap*):** Model klasifikasi beroperasi sepenuhnya sebagai kotak hitam (*black-box*) tanpa adanya metode *Explainable AI*. Model hanya mampu mendeteksi tingkat risiko secara umum tanpa dapat menjelaskan faktor penyebab spesifik pada masing-masing individu, sehingga tidak memberikan arahan intervensi yang dapat ditindaklanjuti secara langsung.

---

## 5. TABEL RESEARCH GAP PENELITIAN TERDAHULU

> **Panduan Copy-Paste ke Microsoft Word:**  
> Tabel di bawah ini dapat langsung di-blok dan di-salin (*copy*) lalu ditempelkan (*paste*) langsung ke Microsoft Word. Word akan secara otomatis merendernya sebagai tabel utuh yang rapi dan dapat diedit. Alternatif file dokumen langsung yang sudah berformat Word siap pakai tersedia pada berkas [OUTLINE_PROPOSAL_REVISI_FINAL.docx](file:///c:/Users/ahmad/OneDrive/ドキュメント/skripsi/OUTLINE_PROPOSAL_REVISI_FINAL.docx).

| No | Peneliti & Tahun | Metode / Algoritma | Hasil & Temuan Utama | Celah Riset (*Research Gap*) | Solusi pada Penelitian Ini (Ahmad, 2026) |
|:---:|---|---|---|---|---|
| **1** | **Taher & Ayon (2024)** | Random Forest, AdaBoost, Gradient Boosting pada dataset gaya hidup dan tidur | Gradient Boosting mencapai akurasi tertinggi 93,80% dalam mendeteksi risiko gangguan tidur. | Model bekerja murni sebagai *black-box* tanpa XAI; hanya mendeteksi tingkat risiko global tanpa mampu menjelaskan faktor penyebab spesifik per individu (*lack of actionable insight*). | Menerapkan metode XAI-SHAP untuk membuka kotak hitam model dan menjelaskan kontribusi faktor gaya hidup secara personal bagi setiap individu. |
| **2** | **Lin et al. (2025)** | ANN, Decision Tree, Naive Bayes pada 20.645 data kuesioner mahasiswa | Menemukan korelasi signifikan antara durasi layar, konsumsi kafein, kebiasaan begadang, dan kualitas tidur. | Analisis hanya relevan pada tingkat populasi umum secara agregat; tidak mampu memberikan penjelasan risiko secara personal untuk masing-masing individu dengan variasi risiko unik. | Mengimplementasikan analisis SHAP lokal (*force/waterfall plot*) yang membedah profil risiko unik per individu secara interaktif. |
| **3** | **Ha et al. (2023)** | XGBoost + SHAP pada 4.622 data kuesioner medis klinis dua rumah sakit | Model mencapai AUROC >0,897 untuk klasifikasi OSA, COMISA, dan insomnia. | Menggunakan XGBoost yang butuh *encoding* manual, datanya berupa kuesioner medis statis, dan SHAP hanya digunakan untuk seleksi fitur awal bukan penjelasan individual *real-time*. | Menggunakan CatBoost yang memproses data kategorikal secara *native*, memanfaatkan data gaya hidup fleksibel (*modifiable*), dan menerapkan SHAP untuk interpretasi *real-time*. |
| **4** | **Xie et al. (2026)** | PLS + XGBoost + SHAP pada survei gaya hidup mahasiswa | Mengidentifikasi durasi tidur, tingkat stres, dan penggunaan gawai sebagai prediktor utama kualitas tidur. | XGBoost mewajibkan *one-hot encoding* sehingga fitur terpecah menjadi variabel tiruan biner; visualisasi SHAP menjadi terfragmentasi dan sulit dipahami secara klinis. | Mengadopsi CatBoost (*ordered target statistics*) tanpa *one-hot encoding*, menjaga keutuhan fitur sehingga hasil penjelasan SHAP tetap utuh, kohesif, dan intuitif. |
| **5** | **Das et al. (2025)** | CatBoost, XGBoost, RF, SVM, GBM, KNN + SHAP pada 1.222 data pasien (*Nature and Science of Sleep*) | CatBoost meraih performa terbaik (Akurasi 71,67%, AUC 77,27%) dalam memprediksi insomnia klinis. | Target klasifikasi hanya biner (2 kelas), populasi terbatas pada pasien penyakit kronis di RS, eksplanasi SHAP hanya di tingkat global, dan tanpa implementasi sistem web operasional. | Membangun klasifikasi multi-kelas 4 level risiko (*Healthy, Mild, Moderate, Severe*) pada 100.000 data gaya hidup digital, XAI-SHAP lokal (*waterfall*) dinamis, dan prototipe Web CDSS interaktif. |

---

### Versi Tab-Separated Values (TSV) untuk Alternatif Copy-Paste ke Word:
*Jika tabel markdown di atas mengalami kendala perataan saat ditempel ke Word, salin blok teks di bawah ini, tempel (*paste*) ke Word, lalu pilih menu: **Insert > Table > Convert Text to Table**:*

```text
No	Peneliti & Tahun	Metode / Algoritma	Hasil & Temuan Utama	Celah Riset (Research Gap)	Solusi pada Penelitian Ini (Ahmad, 2026)
1	Taher & Ayon (2024)	Gradient Boosting, Random Forest, AdaBoost	Akurasi tertinggi 93,80% pada klasifikasi gangguan tidur	Model bekerja sebagai black-box murni tanpa XAI; hanya mendeteksi tingkat risiko tanpa menjelaskan faktor spesifik per individu	Menerapkan metode XAI-SHAP untuk membuka kotak hitam model dan menjelaskan kontribusi faktor gaya hidup per individu
2	Lin et al. (2025)	ANN, Decision Tree, Naive Bayes	Korelasi signifikan antara durasi layar, kopi, begadang, dan kualitas tidur	Analisis hanya pada tingkat populasi umum agregat; tidak mampu memberikan penjelasan risiko personal per individu	Mengimplementasikan analisis SHAP lokal yang membedah profil risiko unik per individu secara interaktif
3	Ha et al. (2023)	XGBoost + SHAP	AUROC >0,897 untuk klasifikasi OSA, COMISA, dan insomnia klinis	Butuh encoding manual, data kuesioner medis statis, dan SHAP hanya untuk seleksi fitur awal	Menggunakan CatBoost (native kategorikal), data gaya hidup modifiable, dan SHAP untuk interpretasi individual real-time
4	Xie et al. (2026)	PLS + XGBoost + SHAP	Mengidentifikasi durasi tidur, stres, dan layar gawai sebagai prediktor utama	One-hot encoding memecah fitur kategorikal; penjelasan SHAP terfragmentasi dan membingungkan secara klinis	Menggunakan CatBoost tanpa one-hot encoding sehingga nilai kontribusi SHAP tetap utuh, kohesif, dan bermakna klinis
5	Das et al. (2025)	CatBoost + 5 Model ML + SHAP	CatBoost terbaik (Akurasi 71,67%, AUC 77,27%) pada prediksi insomnia	Hanya klasifikasi biner, populasi terbatas pasien kronis RS, SHAP hanya agregat global, dan tanpa sistem web CDSS	Membangun klasifikasi multi-kelas 4 level risiko pada 100.000 data gaya hidup digital, XAI-SHAP lokal waterfall real-time, dan Web CDSS
```

---

## 6. TABEL PEMETAAN NOVELTY (ORISINALITAS RISET)

| Kriteria / Parameter Evaluasi | Taher & Ayon (2024) | Lin et al. (2025) | Ha et al. (2023) | Xie et al. (2026) | Das et al. (2025) | **Penelitian Ini (Ahmad, 2026)** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Domain Kasus:** Kesehatan dan Gangguan Tidur | ✅ | ✅ | ✅ | ✅ | ✅ | **✅ (100% Homogen)** |
| **Algoritma Utama:** CatBoost (*Native Categorical Handling*) | ❌ | ❌ | ❌ *(XGBoost)* | ❌ *(XGBoost)* | ✅ | **✅** |
| **Target Klasifikasi:** Multi-Kelas 4 Tingkat Risiko (*Healthy, Mild, Moderate, Severe*) | ❌ *(Biner)* | ❌ *(Skor PSQI)* | ❌ *(Biner per tipe)* | ❌ *(Regresi)* | ❌ *(Biner)* | **✅ (Multi-Kelas 4 Tingkat)** |
| **Skala Dataset:** Skalabilitas Data Besar (100.000 Rekaman) | ❌ *(374 data)* | ✅ *(20.645 data)* | ❌ *(4.622 data)* | ❌ *(Kuesioner)* | ❌ *(1.222 data)* | **✅ (100.000 Rekaman Data)** |
| **Karakter Fitur:** Metrik Gaya Hidup Digital Fleksibel (*Modifiable*) | ✅ | ✅ | ❌ *(Kuesioner Statis)* | ✅ | ❌ *(Penyakit Kronis)* | **✅** |
| **Metodologi XAI:** Implementasi Tree-SHAP untuk Eksplanasi Fitur | ❌ | ❌ | ✅ *(Hanya seleksi fitur)* | ✅ *(Terfragmentasi OHE)* | ✅ *(Summary Global)* | **✅** |
| **Tingkat Eksplanasi:** Penjelasan Lokal per Individu (*Waterfall Plot Real-Time*) | ❌ | ❌ | ❌ | ❌ | ❌ *(Hanya Global)* | **✅** |
| **Fungsi Klinis:** Rekomendasi Intervensi *Sleep Hygiene* Terpersonalisasi | ❌ | ❌ | ❌ | ❌ | ❌ | **✅** |
| **Produk Terapan:** Purwarupa Sistem Pendukung Keputusan Web Interaktif (CDSS) | ❌ | ❌ | ✅ *(Web Prediksi Saja)* | ❌ | ❌ | **✅** |
| **Tingkat Keterpenuhan (*Novelty*)** | **Belum** | **Belum** | **Belum** | **Belum** | **Belum** | **PENUH (Mengisi Semua Celah)** |

---

## 7. REFERENSI / DAFTAR PUSTAKA

1. **Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026).** Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Psychology*, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946

2. **Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A. A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025).** Prevalence and Factors Associated with Insomnia Among Chronic Disease Patients in Bangladesh: A Machine Learning Study. *Nature and Science of Sleep*, 17, 2541–2567. https://doi.org/10.2147/NSS.S547335

3. **Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023).** Predicting the Risk of Sleep Disorders Using a Machine Learning–Based Simple Questionnaire: Development and Validation Study. *Journal of Medical Internet Research*, 25, e46520. https://doi.org/10.2196/46520

4. **Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L. (2025).** Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. *Frontiers in Psychiatry*, 16, 1533875. https://doi.org/10.3389/fpsyt.2025.1533875

5. **Lundberg, S. M., & Lee, S. I. (2017).** A Unified Approach to Interpreting Model Predictions. *Advances in Neural Information Processing Systems (NeurIPS)*, 30. https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html

6. **Taher, A., & Ayon, W. I. Z. (2024).** Exploring Sleep Disorders: A Comparative Analysis of Machine Learning Algorithms on Sleep Health and Lifestyle Data. *2024 IEEE PEEIACON*, 1–6. https://doi.org/10.1109/PEEIACON63629.2024.10800593
