Nama : [Nama Anda]
Nim : [NIM Anda]
Kelas : [Kelas Anda]

--------------------------------------------------

**JUDUL**  
Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Identifikasi Faktor Risiko Gangguan Tidur Berbasis Metrik Gaya Hidup Digital

--------------------------------------------------

**RUMUSAN MASALAH**  
Bagaimana penerapan metode Explainable AI (XAI) Shapley Additive exPlanations (SHAP) pada algoritma CatBoost dapat menghasilkan prediksi risiko gangguan tidur yang transparan dan faktor gaya hidup pemicu yang teridentifikasi secara akurat?

--------------------------------------------------

**LATAR BELAKANG**  
Gangguan tidur merupakan masalah kesehatan global yang berdampak serius terhadap kualitas hidup jutaan masyarakat di seluruh dunia. Kondisi ini tidak hanya menurunkan produktivitas harian, tetapi juga memperburuk risiko penyakit kronis seperti kardiovaskular, diabetes tipe 2, dan gangguan mental jangka panjang. Faktor pemicunya sangat beragam, mulai dari intensitas screen time yang tinggi sebelum tidur, tekanan pekerjaan, hingga pola konsumsi kafein yang berlebihan—variabel yang seluruhnya terukur dalam data gaya hidup sehari-hari. Studi komprehensif pada 20.645 mahasiswa di Provinsi Fujian mengungkapkan bahwa frekuensi olahraga, kecanduan gawai, dan kondisi psikologis terbukti menjadi prediktor dominan penurunan kualitas tidur yang dapat dipetakan melalui machine learning (Lin et al., 2025). Oleh karena itu, diperlukan sistem deteksi dini berbasis data gaya hidup yang mampu mengklasifikasikan risiko gangguan tidur secara otomatis, personal, dan mudah diakses.

Dalam upaya membangun sistem deteksi dini yang andal, pemilihan algoritma machine learning yang tepat menjadi faktor penentu keberhasilan prediksi. Data gaya hidup bersifat multidimensional dan kaya akan fitur kategorikal seperti jenis pekerjaan, tingkat stres, dan kategori usia, yang memerlukan algoritma dengan kemampuan penanganan data heterogen yang kuat. Algoritma CatBoost (Categorical Boosting) hadir sebagai solusi unggul karena mampu memproses fitur kategorikal secara langsung (native categorical handling) tanpa memerlukan proses encoding manual yang berisiko menambah bias pada model. Taher & Ayon (2024) membuktikan bahwa algoritma berbasis Gradient Boosting mencapai akurasi terbaik sebesar 93,80% dalam mengklasifikasikan gangguan tidur, melampaui performa Random Forest dan AdaBoost. Dengan demikian, CatBoost dipilih sebagai algoritma utama dalam penelitian ini karena keunggulannya dalam menangani kompleksitas data gaya hidup digital yang heterogen secara efisien.

Meskipun algoritma machine learning seperti CatBoost menawarkan akurasi prediksi yang tinggi, penerapannya di domain kesehatan menghadapi hambatan fundamental berupa sifat black-box yang melekat pada model-model kompleks tersebut. Model black-box tidak mampu menjelaskan alasan logis di balik setiap prediksi yang dihasilkan, sehingga praktisi medis dan pasien kesulitan untuk mempercayai dan menggunakan rekomendasinya dalam pengambilan keputusan klinis. Transparansi model bukan sekadar aspek tambahan, melainkan sebuah kebutuhan etis dan regulasi yang fundamental dalam pengembangan kecerdasan buatan di bidang kesehatan. Tinjauan komprehensif oleh Sadeghi et al. (2024) menegaskan bahwa ketidakmampuan model untuk menjelaskan prediksinya dapat secara signifikan menurunkan kepercayaan dokter dan pasien terhadap sistem berbasis AI. Oleh karena itu, penelitian ini memandang penting untuk mengintegrasikan pendekatan Explainable AI (XAI) sebagai komponen inti dari sistem prediksi gangguan tidur yang dibangun.

Teknologi Explainable Artificial Intelligence (XAI) telah terbukti mampu menjembatani kesenjangan antara kekuatan prediksi model dan kebutuhan transparansi di dunia medis modern. XAI bekerja dengan mengkalkulasi kontribusi aktual setiap variabel terhadap hasil prediksi, sehingga memungkinkan tenaga kesehatan untuk memahami faktor risiko dominan secara spesifik bagi setiap pasien. Emhandyksa & Afifah (2026) secara konkret mendemonstrasikan penerapan XAI berbasis Feature Importance untuk mendeteksi penyakit jantung secara dini, menghasilkan peta faktor risiko yang dapat diinterpretasikan langsung oleh klinisi tanpa memerlukan pemahaman teknis mendalam tentang algoritma yang digunakan. Keberhasilan XAI di domain kardiovaskular ini merupakan bukti empiris yang kuat bahwa pendekatan serupa sangat layak untuk diadaptasi pada domain gangguan tidur, yang hingga kini masih belum dieksploitasi secara spesifik dalam literatur ilmiah yang ada.

Metode XAI yang paling komprehensif dan terpercaya untuk menginterpretasikan model berbasis pohon keputusan seperti CatBoost adalah SHAP (Shapley Additive exPlanations). SHAP mengukur kontribusi setiap fitur secara adil menggunakan konsep nilai Shapley dari teori permainan koalisi, sehingga menghasilkan penjelasan yang konsisten baik secara lokal (per individu) maupun global (seluruh populasi). Srinivasu et al. (2024) telah memvalidasi bahwa integrasi teknis antara CatBoost dan SHAP menghasilkan interpretabilitas yang sangat tinggi dalam mengidentifikasi faktor penentu diagnosis kanker payudara. Berdasarkan validasi tersebut, penelitian ini bertujuan menerapkan kombinasi CatBoost dan SHAP pada data gaya hidup digital untuk mengidentifikasi faktor risiko utama gangguan tidur secara transparan. Diharapkan, hasil penelitian ini menjadi fondasi ilmiah bagi pengembangan sistem skrining tidur berbasis AI yang tidak hanya akurat, tetapi juga dapat dipahami dan dipercaya oleh praktisi kesehatan.

--------------------------------------------------

**TINJAUAN PUSTAKA (STATE OF THE ART)**  
1. **Taher & Ayon (2024)** dalam penelitiannya melakukan eksperimen komparatif menggunakan algoritma Random Forest, AdaBoost, dan Gradient Boosting untuk memprediksi gangguan tidur seperti Insomnia dan Sleep Apnea. Hasil penelitian menunjukkan akurasi terbaik sebesar 93,80% pada algoritma Gradient Boosting. Namun, fokus penelitian ini sepenuhnya terbatas pada metrik performa statistik tanpa memberikan mekanisme bagi praktisi medis untuk memahami variabel gaya hidup mana yang paling berpengaruh bagi setiap pasien secara individu. Celah inilah yang akan diisi dengan penerapan XAI untuk memberikan penjelasan logis pada setiap prediksi.

2. **Lin et al. (2025)** menganalisis data kuesioner dari 20.645 mahasiswa menggunakan algoritma ANN, Decision Tree, dan Naive Bayes untuk memetakan hubungan antara faktor gaya hidup digital dengan kualitas tidur. Meskipun model ANN memberikan hasil yang signifikan, sifatnya yang sangat tertutup membuat faktor pemicu gangguan tidur sulit dipahami secara intuitif oleh pengguna awam. Celah penelitian ini adalah belum adanya penggunaan metode interpretabilitas tingkat lanjut seperti SHAP untuk mengekstraksi informasi berbobot dari model kompleks yang mereka bangun.

3. **Sadeghi et al. (2024)** memberikan tinjauan mendalam mengenai urgensi *Explainable AI* di sektor kesehatan, menegaskan bahwa model yang dapat dijelaskan adalah standar baru dalam inovasi medis untuk membangun kepercayaan pengguna. Meskipun penelitian ini memberikan fondasi teori yang kuat mengenai urgensi XAI, implementasi praktis pada klasifikasi risiko gangguan tidur berbasis metrik gaya hidup digital belum dieksplorasi secara spesifik. Skripsi ini akan mengisi kesenjangan antara teori XAI umum dengan aplikasi praktis pada kesehatan tidur preventif.

4. **Emhandyksa & Afifah (2026)** mengusulkan kerangka kerja deteksi dini yang transparan untuk penyakit jantung menggunakan metode XAI. Penelitian ini berhasil membuktikan bahwa dengan XAI, tenaga medis dapat melihat peringkat fitur yang paling berpengaruh terhadap risiko penyakit secara visual. Namun, domain penelitian ini terbatas pada penyakit kardiovaskular murni. Terdapat celah besar untuk menerapkan kerangka kerja transparan ini pada data gaya hidup multidimensional yang memiliki karakteristik data kategorikal yang lebih dominan.

5. **Srinivasu et al. (2024)** menghadirkan pendekatan inovatif dengan mengintegrasikan CatBoost dan SHAP untuk diagnosis medis. Penelitian ini menunjukkan bahwa SHAP dapat memberikan penjelasan tingkat lokal dan global yang sangat akurat untuk model CatBoost. Validasi teknis ini membuktikan bahwa CatBoost adalah mesin yang sangat andal untuk XAI. Namun, hingga saat ini, kombinasi tersebut belum pernah diterapkan secara sistematis untuk membedah profil gaya hidup digital pemicu gangguan tidur, yang menjadi nilai kebaruan (*novelty*) utama dalam penelitian ini.

--------------------------------------------------

**REFERENSI / DAFTAR PUSTAKA**  
1. Taher, A., & Ayon, W. I. Z. (2024). Exploring Sleep Disorders: A Comparative Analysis of Machine Learning Algorithms on Sleep Health and Lifestyle Data. *2024 IEEE PEEIACON*.
2. Lin, Y., et al. (2025). Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. *Frontiers in Psychiatry*, 16, 1533875.
3. Sadeghi, Z., et al. (2024). A review of Explainable Artificial Intelligence in healthcare. *Computers and Electrical Engineering*, 118, 109370.
4. Emhandyksa, M., & Afifah, I. N. (2026). Metode Explainable Artificial Intelligence (XAI) Berbasis Feature Importance Untuk Deteksi Dini Penyakit Jantung. *Journal of Sustainable Supply Chain and Technology*, 1(1), 68-79.
5. Srinivasu, P. N., et al. (2024). XAI-driven CatBoost multi-layer perceptron neural network for analyzing breast cancer. *Scientific Reports*.
