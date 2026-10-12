# BAB I
# PENDAHULUAN

## 1.1 Latar Belakang Masalah

Gangguan tidur saat ini telah berkembang menjadi masalah kesehatan masyarakat yang serius di era modern. Kondisi ini tidak hanya menurunkan kebugaran tubuh sehari-hari, tetapi juga berhubungan erat dengan peningkatan risiko berbagai penyakit kronis seperti gangguan kardiovaskular, diabetes, hingga depresi. Pada era serba digital, sebagian besar pemicu gangguan tidur berkaitan langsung dengan pola kebiasaan harian yang dapat diukur secara kuantitatif. Faktor-faktor tersebut meliputi durasi paparan layar gawai sebelum tidur, beban kerja, konsumsi kafein, hingga minimnya aktivitas fisik harian. Studi Lin et al. (2025) terhadap 20.645 responden membuktikan bahwa kebiasaan gaya hidup digital merupakan prediktor nyata yang dapat dipetakan secara akurat menggunakan machine learning. Temuan tersebut membuka peluang besar untuk mengembangkan sistem deteksi dini risiko gangguan tidur yang bersifat proaktif berbasis data perilaku.

Membangun sistem deteksi dini tersebut memerlukan algoritma pembelajaran mesin yang berakurasi tinggi sekaligus mampu mengolah data gaya hidup heterogen. Data gaya hidup memadukan variabel numerik seperti durasi tidur dan detak jantung dengan variabel kategorikal seperti jenis pekerjaan dan tingkat stres. Banyak algoritma konvensional seperti Random Forest atau XGBoost mengalami kendala saat memproses data kategorikal, karena membutuhkan proses encoding manual yang rentan memicu bias serta ledakan dimensi data. Algoritma CatBoost dirancang khusus untuk mengatasi masalah ini melalui mekanisme ordered target statistics yang memproses fitur kategorikal secara langsung tanpa encoding manual. Keunggulan gradient boosting terbukti pada studi Taher & Ayon (2024) yang meraih akurasi 93,80% pada klasifikasi gangguan tidur. Oleh karena itu, CatBoost sangat tepat digunakan karena selaras dengan karakteristik data gaya hidup.

Kendati memiliki akurasi yang tinggi, algoritma berbasis ensemble seperti CatBoost memiliki kelemahan utama karena beroperasi sebagai model kotak hitam atau black-box. Keputusan prediksi dihasilkan dari ratusan pohon keputusan paralel yang rumit, sehingga pengguna tidak dapat memahami alasan di balik penetapan tingkat risiko seseorang secara logis. Dalam dunia medis, ketidakmampuan model menjelaskan proses keputusannya menjadi hambatan besar bagi adopsi teknologi kecerdasan buatan klinis. Dokter maupun pasien membutuhkan landasan rasional yang transparan dan dapat dipertanggungjawabkan sebelum mengambil keputusan medis atau intervensi perilaku harian. Penelitian Ha et al. (2023) menunjukkan bahwa metode Explainable AI mampu meningkatkan keterbukaan prediksi gangguan tidur, meskipun penerapannya masih terbatas pada penyaringan kuesioner awal. Oleh sebab itu, integrasi Explainable AI menjadi kebutuhan mutlak agar model klasifikasi tidak hanya akurat, tetapi juga transparan.

Di antara berbagai pendekatan Explainable AI modern, metode Shapley Additive exPlanations atau SHAP dipandang paling unggul karena memiliki landasan teori permainan kooperatif yang kokoh. Berdasarkan prinsip matematis fundamental yang dirumuskan oleh Lundberg & Lee (2017), metode SHAP mampu menjamin perhitungan kontribusi setiap variabel input secara adil, konsisten, dan aditif. Keunggulan utama metode SHAP adalah kemampuannya menyajikan penjelasan pada tingkat populasi global sekaligus tingkat individu lokal secara mendalam. Efektivitas SHAP dalam menganalisis faktor penentu kualitas tidur juga telah berhasil dibuktikan secara konkret oleh Xie et al. (2026). Melalui analisis SHAP, tenaga medis maupun pasien dapat mengetahui secara pasti variabel gaya hidup mana yang paling mendorong timbulnya risiko gangguan tidur pada setiap individu, seperti tingginya tingkat stres kerja atau durasi paparan layar gawai yang berlebih.

Meskipun berbagai penelitian terdahulu menunjukkan hasil positif, terdapat lima celah riset utama yang belum terselesaikan secara simultan. Taher & Ayon (2024) menghasilkan model berakurasi tinggi namun tanpa transparansi faktor risiko individual. Lin et al. (2025) hanya menganalisis faktor tidur pada tingkat populasi umum tanpa personalisasi per individu. Ha et al. (2023) menerapkan metode SHAP sebatas untuk seleksi fitur kuesioner statis menggunakan algoritma XGBoost. Xie et al. (2026) menggunakan teknik one-hot encoding yang memecah fitur kategorikal sehingga penjelasan SHAP terfragmentasi dan membingungkan secara klinis. Terakhir, Das et al. (2025) berhasil membuktikan keunggulan CatBoost-SHAP pada insomnia namun terbatas pada klasifikasi biner pasien kronis tanpa visualisasi lokal per individu. Belum ada penelitian yang menggabungkan keunggulan CatBoost dan SHAP untuk klasifikasi multi-kelas risiko gangguan tidur berbasis gaya hidup secara personal.

Berdasarkan kelima celah riset tersebut, penelitian ini mengusulkan penerapan metode Explainable AI berbasis SHAP pada algoritma CatBoost untuk klasifikasi risiko gangguan tidur berbasis metrik gaya hidup digital. Algoritma CatBoost dipilih karena memiliki keunggulan dalam mengolah data kategorikal tanpa merusak struktur data aslinya, sehingga nilai kontribusi SHAP tetap utuh dan bermakna secara klinis. Pendekatan ini diharapkan mampu mengenali pola risiko tidur secara akurat sekaligus memetakan faktor pemicu dominan pada setiap individu secara tepat. Selain itu, model yang dikembangkan akan diintegrasikan secara langsung ke dalam purwarupa sistem pendukung keputusan klinis berbasis web yang interaktif. Sistem ini dirancang agar mudah digunakan oleh masyarakat umum untuk mengenali kebiasaan buruknya, sekaligus membantu tenaga medis dalam merancang rekomendasi perubahan gaya hidup yang terarah, efektif, dan berbasis bukti ilmiah terpercaya.

## 1.2 Rumusan Masalah

Berdasarkan identifikasi masalah dan celah riset pada latar belakang di atas, rumusan masalah dalam penelitian ini dirumuskan sebagai berikut:
1. Bagaimana mengimplementasikan algoritma CatBoost dengan penanganan ketidakseimbangan kelas berbasis *cost-sensitive learning* untuk klasifikasi multikelas tingkat risiko gangguan tidur berbasis metrik gaya hidup digital?
2. Bagaimana menerapkan metode *Explainable Artificial Intelligence* (XAI) berbasis *Shapley Additive exPlanations* (SHAP) guna mengekstraksi penjelasan global dan lokal dari keputusan prediksi model secara transparan, adil, dan konsisten?
3. Bagaimana merancang purwarupa *Clinical Decision Support System* (CDSS) berbasis web yang interaktif guna menyajikan visualisasi prediksi risiko dan rekomendasi intervensi gaya hidup yang dapat dipahami oleh pengguna awam dan klinisi?

## 1.3 Tujuan Penelitian

Mengacu pada rumusan masalah yang telah ditetapkan, tujuan dari penelitian ini adalah:
1. Mengembangkan model klasifikasi multikelas empat tingkat risiko gangguan tidur (*Healthy, Mild, Moderate, Severe*) menggunakan algoritma CatBoost dengan mekanisme *Ordered Target Statistics* dan pembobotan penalti kelas (*cost-sensitive weights*) untuk mengatasi ketidakseimbangan data.
2. Menerapkan metode XAI-SHAP (*TreeExplainer*) guna menguraikan kontribusi fitur secara global pada tingkat populasi (*summary beeswarm plot*) dan secara lokal pada tingkat individu (*waterfall plot*), sehingga memberikan transparansi terhadap faktor risiko dominan pasien.
3. Membangun purwarupa sistem pendukung keputusan klinis (*Clinical Decision Support System*) berbasis web yang mengintegrasikan inferensi model CatBoost dan eksplanasi visual SHAP ke dalam rekomendasi tindakan preventif yang aplikatif.

## 1.4 Manfaat Penelitian

Penelitian ini diharapkan mampu memberikan kontribusi yang nyata baik secara teoretis maupun praktis:

### 1.4.1 Manfaat Teoretis
1. **Bagi Pengembangan Ilmu Pengetahuan**: Memberikan kontribusi akademis dalam domain informatika medis (*health informatics*) dan kecerdasan buatan terapan, khususnya mengenai efektivitas integrasi algoritma CatBoost dengan metode XAI-SHAP dalam menangani data perilaku gaya hidup heterogen tanpa fragmentasi fitur akibat *encoding*.
2. **Bagi Peneliti**: Memperluas pemahaman metodologis dan keterampilan teknis dalam perancangan model pembelajaran mesin yang akuntabel, mulai dari rekayasa fitur data tabular skala besar, penanganan data tidak seimbang, pembuktian aksioma matematika SHAP, hingga diseminasi model ke lingkungan produksi.

### 1.4.2 Manfaat Praktis
1. **Bagi Tenaga Kesehatan dan Klinisi**: Menyediakan instrumen skrining awal yang objektif dan terukur untuk membantu tenaga medis mengidentifikasi pola kebiasaan berisiko pasien secara cepat, serta mempermudah perancangan intervensi klinis yang dipersonalisasi berdasarkan faktor pemicu dominan.
2. **Bagi Masyarakat Umum**: Meningkatkan literasi dan kesadaran preventif masyarakat mengenai dampak kebiasaan digital harian (seperti durasi paparan layar gawai dan tingkat stres) terhadap kualitas tidur, serta memfasilitasi evaluasi mandiri melalui sistem antarmuka berbasis web yang informatif.

---

## DAFTAR PUSTAKA

Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Psychology*, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946

Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025). Prevalence and factors associated with insomnia among chronic disease patients in Bangladesh: A machine learning study. *Nature and Science of Sleep*, 17, 2725–2741. https://doi.org/10.2147/NSS.S547335

Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023). Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study. *Journal of Medical Internet Research*, 25, e46520. https://doi.org/10.2196/46520

Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L. (2025). Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. *Frontiers in Psychiatry*, 16, 1533875. https://doi.org/10.3389/fpsyt.2025.1533875

Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems (NeurIPS)*, 30, 4765–4774.

Taher, A., & Ayon, W. I. Z. (2024). Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data. *2024 IEEE PEEIACON*, 1–6. https://doi.org/10.1109/PEEIACON63765.2024.10844781
