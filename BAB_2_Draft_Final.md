# BAB II
# LANDASAN TEORI DAN TINJAUAN PUSTAKA

## 2.1 Kajian Teori

Kajian teori memaparkan fondasi keilmuan, konsep fundamental, serta formulasi matematis yang melandasi perancangan sistem deteksi risiko gangguan tidur berbasis algoritma CatBoost dan metode Explainable Artificial Intelligence (XAI) Shapley Additive exPlanations (SHAP). Pembahasan teori mencakup karakteristik klinis gangguan tidur, pengaruh metrik gaya hidup digital, penanganan data tidak seimbang (*class imbalance*), arsitektur algoritma pembelajaran mesin berbasis *gradient boosting*, teori keadilan kontribusi fitur SHAP, hingga perancangan purwarupa sistem pendukung keputusan klinis (*Clinical Decision Support System*).

### 2.1.1 Karakteristik Klinis Gangguan Tidur dan Kualitas Tidur

Tidur merupakan proses fisiologis esensial yang bersifat aktif dan berulang secara periodik untuk memulihkan fungsi homeostasis biologis, mengonsolidasikan memori kognitif, serta menjaga stabilitas sistem imun tubuh (Medic et al., 2017). Gangguan tidur (*sleep disorders*) didefinisikan sebagai deviasi atau kelainan pola tidur yang mengakibatkan penurunan kualitas, kuantitas, serta efisiensi tidur, yang berdampak langsung pada terganggunya fungsi fisiologis dan psikososial individu di siang hari. Berdasarkan *International Classification of Sleep Disorders* (ICSD-3), manifestasi gangguan tidur mencakup spektrum luas, mulai dari insomnia primer, gangguan pernapasan terkait tidur seperti *Obstructive Sleep Apnea* (OSA), gangguan ritme sirkadian, hingga hipersomnia (Ha et al., 2023).

Kualitas tidur diukur melalui keterpaduan parameter kuantitatif dan kualitatif, yang mencakup durasi total tidur (*total sleep time*), latensi awitan tidur (*sleep onset latency*), frekuensi terbangun di malam hari (*wake after sleep onset*), serta efisiensi tidur (*sleep efficiency*). Penurunan efisiensi tidur secara kronis berhubungan erat dengan peningkatan sitokin pro-inflamasi, resistensi insulin, peningkatan beban kardiovaskular, serta percepatan penurunan fungsi kognitif (Das et al., 2025). Selain durasi tidur statis, bukti klinis terkini menunjukkan bahwa variabilitas dan keteraturan jadwal tidur (*sleep regularity*) memegang peranan krusial sebagai prediktor risiko morbiditas dan mortalitas yang bahkan lebih kuat daripada durasi tidur itu sendiri (Windred et al., 2024).

Dalam konteks stratifikasi risiko klinis preventif, tingkat keparahan gangguan tidur dikelompokkan ke dalam empat tingkatan fungsional: *Healthy* (kondisi optimal tanpa indikasi patologis signifikan), *Mild* (gejala ringan yang dipicu oleh fluktuasi kebiasaan harian), *Moderate* (gangguan menengah yang mulai menurunkan produktivitas kognitif dan konsentrasi), serta *Severe* (gangguan berat dengan manifestasi klinis patologis yang memerlukan intervensi medis komprehensif). Klasifikasi berjenjang ini esensial untuk memfasilitasi tindakan triase dan skrining proaktif sebelum pasien berkembang menuju kondisi kronis.

### 2.1.2 Metrik Gaya Hidup Digital dan Pengaruhnya terhadap Ritme Sirkadian

Pergeseran pola interaksi masyarakat modern menuju era digital secara signifikan mengubah kebiasaan harian dan memunculkan fenomena stres psikologis baru yang berdampak negatif terhadap pola tidur. Jam biologis manusia diatur oleh ritme sirkadian yang berpusat pada *suprachiasmatic nucleus* (SCN) di hipotalamus, yang sangat peka terhadap paparan cahaya eksternal dan rutinitas harian. Paparan emisi cahaya biru (*blue light*) bergelombang pendek (450–480 nm) dari layar gawai (*smartphone*, laptop, tablet) menjelang waktu tidur menekan sekresi hormon melatonin oleh kelenjar pineal, sehingga menunda awitan tidur alami dan memperpendek fase tidur lelap (*deep sleep*) (Kumar et al., 2025).

Selain intervensi fotik fisiologis, aktivitas digital memicu fenomena ketergantungan psikologis yang dikenal sebagai *nomophobia* (*no mobile phone phobia*) dan *technostress*, yaitu kondisi tekanan mental akibat tuntutan konektivitas terus-menerus dan kebiasaan memeriksa gawai secara berulang di tempat tidur (Widayati, 2024; Jahrami, 2023). Kondisi ini meningkatkan aktivitas sistem saraf simpatik melalui sekresi hormon kortisol dan adrenalin, yang mengakibatkan kondisi hiperarousal (*physiological hyperarousal*) saat hendak beristirahat. Fenomena ini diperparah pada individu dengan tipe kronotipe malam (*night owl*) yang cenderung menunda jam tidur akibat aktivitas komputasi atau hiburan digital hingga larut malam.

Kombinasi antara paparan layar gawai yang intensif, beban kerja tinggi, asupan kafein berlebih, serta rendahnya tingkat aktivitas fisik harian (*sedentary behavior*) membentuk lingkaran umpan balik negatif terhadap kesehatan tidur (Henrich et al., 2021). Dampak kumulatif dari degradasi tidur akibat gaya hidup ini menimbulkan beban kerugian ekonomi yang nyata melalui penurunan produktivitas tenaga kerja, peningkatan absensi, dan risiko kesalahan fatal pada lingkungan profesional (Uzubuaku, 2023). Oleh karena itu, kuantifikasi metrik gaya hidup digital melalui variabel-variabel terukur menjadi instrumen penting untuk memodelkan risiko gangguan tidur secara presisi (Lin et al., 2025).

### 2.1.3 Pembelajaran Mesin Terawasi dan Penanganan Ketidakseimbangan Data (*Class Imbalance*)

Pembelajaran mesin terawasi (*supervised machine learning*) merupakan paradigma komputasi di mana algoritma mempelajari fungsi pemetaan matematis dari ruang matriks fitur masukan $X \in \mathbb{R}^{N 	imes M}$ menuju ruang label target luaran $Y \in \{c_1, c_2, \dots, c_K\}$ berdasarkan himpunan data latih berlabel. Pada domain medis, salah satu tantangan paling fundamental dalam pembelajaran terawasi adalah ketidakseimbangan sebaran kelas (*class imbalance*), di mana proporsi sampel populasi sehat (*Healthy*) mendominasi secara masif, sedangkan sampel pasien berisiko tinggi (*Severe*) hanya mencakup sebagian kecil dari total populasi (Taher & Ayon, 2024).

Algoritma pembelajaran mesin standar yang meminimalkan fungsi kerugian global tanpa penyesuaian akan mengalami fenomena *Accuracy Paradox*. Model akan cenderung memprediksi seluruh sampel ke dalam kelas mayoritas guna meraih angka akurasi komputasi yang tinggi, namun gagal mengenali pasien kelas minoritas yang justru memiliki risiko kritis secara klinis (*false negative* tinggi). Pendekatan konvensional untuk menangani masalah ini sering kali mengandalkan teknik manipulasi data (*resampling*), seperti *random undersampling* yang membuang informasi berharga dari kelas mayoritas, atau *Synthetic Minority Over-sampling Technique* (SMOTE) yang menghasilkan sampel sintetis di antara titik-titik data minoritas (Chicco & Jurman, 2020).

Akan tetapi, pada dataset tabular heterogen yang memadukan variabel numerik dan kategorikal, teknik SMOTE rentan menciptakan titik data sintetis yang tidak realistis secara klinis, merusak korelasi antar-variabel, serta meningkatkan risiko *overfitting*. Sebagai alternatif yang lebih kokoh dan mempertahankan struktur data asli, pendekatan *Cost-Sensitive Learning* diterapkan secara internal pada fungsi objektif optimasi model (El Chakik et al., 2026). Mekanisme ini menetapkan matriks biaya penalti kesalahan yang berbanding terbalik dengan frekuensi kemunculan kelas dalam data latih:

$$w_c = rac{N}{K \cdot N_c}$$

di mana $N$ merupakan jumlah observasi keseluruhan, $K$ adalah jumlah kelas target, dan $N_c$ merepresentasikan frekuensi sampel pada kelas $c$. Melalui penalti asimetris ini, setiap kekeliruan klasifikasi pada sampel kelas minoritas Severe diberikan bobot penalti hukuman belasan kali lipat lebih berat, sehingga memaksa algoritma memperluas batas keputusan (*decision boundary*) untuk mengenali karakteristik pasien berisiko tinggi tanpa memanipulasi data riil (Chicco & Jurman, 2022).

### 2.1.4 Arsitektur Algoritma CatBoost (*Categorical Boosting*)

CatBoost (*Categorical Boosting*) merupakan algoritma pembelajaran mesin mutakhir berbasis *Gradient Boosted Decision Trees* (GBDT) yang dikembangkan khusus untuk mengatasi keterbatasan algoritma boosting konvensional saat memproses data tabular berskala besar dan kaya fitur kategorikal (Prokhorenkova et al., 2018). Tidak seperti algoritma *XGBoost* atau *LightGBM* yang menggunakan pohon keputusan asimetris dengan pertumbuhan berbasis kedalaman (*depth-wise*) atau daun (*leaf-wise*), CatBoost memanfaatkan struktur pohon simetris (*symmetric oblivious trees*).

Pada *oblivious decision tree*, kriteria pemisahan (*split criterion*) yang sama diterapkan secara seragam pada seluruh simpul di tingkat kedalaman pohon yang identik. Struktur simetris ini memberikan tiga keunggulan komputasi utama:
1. Berfungsi sebagai regularisasi alami yang mencegah pertumbuhan pohon yang terlampau dalam pada cabang tertentu, sehingga sangat efektif meminimalkan risiko *overfitting*.
2. Memungkinkan evaluasi simpul pohon secara paralel menggunakan instruksi vektor bitwise pada prosesor, yang mempercepat inferensi model secara drastis (*low-latency prediction*).
3. Menjamin stabilitas model saat diintegrasikan dengan modul interpretasi pasca-pemodelan (Hancock & Khoshgoftaar, 2020; Li et al., 2025).

Inovasi fundamental kedua dari CatBoost adalah mekanisme *Ordered Boosting*. Pada algoritma gradient boosting tradisional, gradien residual dihitung menggunakan model yang dilatih pada himpunan data yang sama dengan titik evaluasi, yang menimbulkan pergeseran estimasi gradien (*prediction shift*) dan memicu kebocoran data (*data leakage*). CatBoost mengatasi bias ini dengan mensimulasikan proses pembelajaran sekuensial melalui permutasi acak observasi data, di mana model pendukung pada setiap iterasi hanya diperbarui menggunakan sampel-sampel yang mendahului titik data evaluasi dalam urutan permutasi (Wang et al., 2025; Srinivasu et al., 2024).

Keunggulan paling krusial dari CatBoost terletak pada mekanisme penanganan data kategorikal alami melalui *Ordered Target Statistics* (OTS). Pada data tabular medis, metode konvensional seperti *One-Hot Encoding* memecah satu variabel kategorikal menjadi puluhan variabel tiruan biner, yang memicu lonjakan dimensi data (*curse of dimensionality*), menghabiskan memori komputasi, serta memecah signifikansi klinis variabel asli (Chen et al., 2024). CatBoost mentransformasikan kategori menjadi nilai numerik kontinu secara dinamis berdasarkan nilai target historis ditambah bobot prioritas global:

$$\hat{x}_k = rac{\sum_{j=1}^{p-1} [x_{\sigma_j} = x_{\sigma_p}] \cdot y_{\sigma_j} + a \cdot P}{\sum_{j=1}^{p-1} [x_{\sigma_j} = x_{\sigma_p}] + a}$$

di mana $P$ adalah nilai ekspektasi prior dari target keseluruhan, dan $a > 0$ merupakan parameter bobot pembobot prioritas. Mekanisme ini menjaga keutuhan struktur variabel gaya hidup nominal tanpa menimbulkan kebocoran informasi target masa depan (Alqudah et al., 2026).

### 2.1.5 Konsep *Explainable Artificial Intelligence* (XAI) dan Teori Permainan Kooperatif SHAP

Penerapan sistem kecerdasan buatan dalam bidang medis menghadapi hambatan besar terkait sifat model kotak hitam (*black-box model*). Kendati algoritma pembelajaran mesin seperti CatBoost mampu mencapai akurasi klasifikasi yang melampaui metode linier klasik, proses inferensi yang dihasilkan dari interaksi non-linier ratusan pohon keputusan tidak dapat dipahami secara intuitif oleh tenaga medis maupun pasien (Amann et al., 2020; Loh et al., 2024). Ketiadaan transparansi ini berisiko memicu kesalahan penanganan klinis dan menimbulkan penolakan adopsi teknologi oleh praktisi kesehatan.

Guna menjembatani kesenjangan tersebut, bidang *Explainable Artificial Intelligence* (XAI) menghadirkan metodologi untuk membuka proses penalaran internal model prediktif ke dalam representasi yang dapat diinterpretasikan oleh manusia. Di antara berbagai metode XAI modern, pendekatan *Shapley Additive exPlanations* (SHAP) yang diperkenalkan oleh Lundberg & Lee (2017) dipandang sebagai metode paling kokoh karena berakar pada landasan teori permainan kooperatif (*cooperative game theory*) yang dirumuskan oleh penerima Nobel Lloyd Shapley (1953).

Dalam konteks machine learning, prediksi model diposisikan sebagai hasil permainan (*payout*), sedangkan fitur-fitur masukan bertindak sebagai pemain (*players*) yang berkoalisi untuk menghasilkan keputusan tersebut. Nilai Shapley merepresentasikan kontribusi marjinal rata-rata dari suatu fitur $i$ terhadap seluruh kemungkinan kombinasi himpunan bagian fitur $S \subseteq F \setminus \{i\}$:

$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} rac{|S|! (|F| - |S| - 1)!}{|F|!} \left[ f(S \cup \{i\}) - f(S) 
ight]$$

Metode SHAP secara matematis menjamin empat aksioma keadilan fundamental:
1. **Efisiensi (*Efficiency / Additivity*)**: Jumlah kontribusi seluruh nilai SHAP fitur ditambah nilai dasar harapan (*base value* $\phi_0$) persis setara dengan probabilitas keluaran prediksi model: $f(x) = \phi_0 + \sum_{i=1}^M \phi_i$.
2. **Simetri (*Symmetry*)**: Dua fitur yang memberikan kontribusi marginal yang sama terhadap seluruh kombinasi himpunan bagian akan menerima nilai atribusi yang identik.
3. **Pemain Nol (*Dummy / Null Player*)**: Fitur yang tidak memberikan perubahan terhadap prediksi pada kombinasi koalisi apa pun akan menerima nilai kontribusi tepat nol ($\phi_i = 0$).
4. **Aditivitas / Monotonisitas (*Monotonicity*)**: Jika kontribusi marjinal suatu fitur meningkat pada suatu model baru, nilai atribusi fitur tersebut tidak akan pernah menurun (Lundberg et al., 2020).

Untuk model berbasis ansambel pohon seperti CatBoost, varian *TreeExplainer* mengoptimalkan penghitungan nilai Shapley dari kompleksitas waktu eksponensial $O(T L 2^M)$ menjadi kompleksitas waktu polinomial $O(T L D^2)$, di mana $T$ adalah jumlah pohon, $L$ adalah jumlah daun maksimum, dan $D$ adalah kedalaman pohon. Hal ini memungkinkan ekstraksi eksplanasi global (*summary beeswarm plot*) dan eksplanasi lokal individu (*waterfall plot*) secara instan dan presisi (Zhang et al., 2024; Huang et al., 2024).

### 2.1.6 Sistem Pendukung Keputusan Klinis (*Clinical Decision Support System* / CDSS)

Sistem Pendukung Keputusan Klinis (*Clinical Decision Support System* / CDSS) merupakan aplikasi perangkat lunak berbasis teknologi informasi kesehatan yang dirancang untuk membantu tenaga medis, dokter, perawat, maupun pasien dalam pengambilan keputusan klinis preventif maupun terapeutik (Naga Srinivasu et al., 2022). Evolusi CDSS modern bertransisi dari sistem pakar berbasis aturan statis (*rule-based expert systems*) menuju sistem cerdas adaptif yang didorong oleh algoritma pembelajaran mesin dan kapabilitas interpretabilitas XAI (Wahyudi et al., 2026).

Integrasi model prediktif CatBoost dan modul penjelasan SHAP ke dalam antarmuka purwarupa CDSS berbasis web interaktif menghadirkan nilai terapan tinggi:
1. **Skrining Cepat dan Non-Invasif**: Memungkinkan pengguna melakukan evaluasi profil risiko gangguan tidur mandiri berdasarkan metrik perilaku harian tanpa memerlukan instrumen laboratorium yang invasif (Rahman et al., 2025; Kaya 2025).
2. **Transparansi Diagnostik**: Menyajikan grafik kontribusi fitur spesifik pasien, sehingga tenaga kesehatan dapat memverifikasi apakah keluaran risiko model selaras dengan kondisi klinis riil (Chen et al., 2024).
3. **Rekomendasi Tindakan Terarah (*Actionable Insights*)**: Mentransformasikan fitur-fitur berisiko tinggi yang teridentifikasi oleh SHAP menjadi saran perbaikan kebiasaan hidup (*sleep hygiene interventions*) yang dipersonalisasi dan berbasis bukti ilmiah (Putra & Hidayat, 2024).

---

## 2.2 Kajian Hasil Penelitian yang Relevan (State of the Art)

Kajian hasil penelitian yang relevan menyajikan sintesis kritis terhadap studi-studi terdahulu yang berfokus pada klasifikasi gangguan tidur, penerapan algoritma gradient boosting, serta implementasi Explainable AI. Telaah ini bertujuan memetakan posisi keilmuan, mengidentifikasi keterbatasan yang ada, serta menegaskan kontribusi kebaruan (*novelty*) penelitian yang diusulkan.

### 2.2.1 Sintesis Naratif Penelitian Terdahulu

Penelitian terdahulu mengenai klasifikasi gangguan tidur berbasis data kesehatan dan gaya hidup telah dilakukan oleh **Taher & Ayon (2024)**. Dalam studi komparasi menggunakan algoritma Random Forest, AdaBoost, dan Gradient Boosting, mereka membuktikan bahwa algoritma ensemble Gradient Boosting mencapai akurasi tertinggi sebesar 93,80% dalam mendeteksi risiko gangguan tidur. Namun demikian, model yang dibangun beroperasi sepenuhnya sebagai kotak hitam (*black-box*) tanpa integrasi metode interpretabilitas. Model hanya mampu memprediksi label risiko secara agregat tanpa memberikan penjelasan mengenai faktor kebiasaan mana yang mendorong timbulnya risiko pada setiap individu, sehingga membatasi pemanfaatan klinisnya dalam perumusan rencana tindakan perbaikan.

Pada skala populasi yang lebih luas, **Lin et al. (2025)** mengevaluasi kualitas tidur dan faktor-faktor eksternal yang memengaruhinya terhadap 20.645 responden mahasiswa menggunakan algoritma Artificial Neural Network (ANN), Decision Tree, dan Naive Bayes. Hasil penelitian membuktikan adanya korelasi statistik yang kuat antara intensitas paparan gawai harian, kebiasaan begadang, serta konsumsi kafein terhadap degradasi kualitas tidur. Meskipun demikian, analisis interpretabilitas yang disajikan hanya berlaku secara makro pada tingkat populasi umum. Model belum mampu memfasilitasi analisis risiko terpersonalisasi untuk masing-masing individu dengan profil gaya hidup digital yang heterogen.

Upaya penerapan Explainable AI pada domain gangguan tidur klinis dieksplorasi oleh **Ha et al. (2023)**. Penelitian tersebut mengembangkan model prediksi risiko tiga kategori gangguan tidur (*Obstructive Sleep Apnea*, insomnia, dan kombinasi keduanya) berbasis data kuesioner medis dari 4.622 pasien rumah sakit menggunakan algoritma XGBoost dan metode SHAP, dengan raihan nilai AUROC di atas 0,897. Meskipun model menunjukkan performa diskriminasi yang baik, algoritma XGBoost yang digunakan mewajibkan transformasi encoding manual pada fitur kategorikal. Selain itu, metode SHAP hanya dimanfaatkan secara terbatas pada tahap seleksi fitur awal (*feature selection*), bukan sebagai modul eksplanasi lokal yang interaktif dan dapat diakses pengguna secara langsung.

Keterbatasan proses encoding pada interpretasi SHAP dipertegas oleh temuan **Xie et al. (2026)** yang meneliti faktor-faktor penentu kualitas tidur mahasiswa menggunakan kombinasi regresi *Partial Least Squares* (PLS) dan XGBoost yang dilengkapi SHAP. Penelitian ini mengonfirmasi bahwa durasi tidur, tingkat stres, dan penggunaan gawai merupakan prediktor dominan. Namun, keharusan menerapkan teknik *One-Hot Encoding* pada XGBoost mengakibatkan variabel kategorikal nominal terpecah menjadi variabel tiruan biner yang terpisah. Akibatnya, visualisasi atribusi nilai SHAP menjadi terfragmentasi, kehilangan konteks semantiknya, serta menyulitkan klinisi dalam menyusun rekomendasi perubahan perilaku harian yang komprehensif.

Penelitian mutakhir oleh **Das et al. (2025)** yang dipublikasikan pada jurnal *Nature and Science of Sleep* melakukan studi komparasi terhadap 1.222 pasien penyakit kronis di Bangladesh menggunakan enam algoritma pembelajaran mesin dan metode SHAP. Studi tersebut membuktikan bahwa algoritma CatBoost meraih performa tertinggi (Akurasi 71,67%, AUC 77,27%, F1-score 71,23%) dibanding model lainnya dalam mendeteksi insomnia klinis. Namun demikian, pemodelan yang dilakukan masih terbatas pada target klasifikasi biner (*Insomnia vs Non-Insomnia*) pada kelompok spesifik pasien rumah sakit dengan penanganan ketidakseimbangan kelas menggunakan oversampling sintetis SMOTE. Selain itu, penjelasan SHAP yang dihasilkan hanya berupa visualisasi global (*Beeswarm Plot*) tanpa penyediaan visualisasi lokal per individu (*Waterfall Plot*), serta belum diwujudkan ke dalam purwarupa sistem terapan berbasis web.

### 2.2.2 Tabel Matriks Perbandingan Penelitian Terdahulu (*Research Gap Matrix*)

Berdasarkan sintesis kritis terhadap literatur yang relevan, perbandingan sistematis antara penelitian terdahulu dan posisi kebaruan penelitian ini disajikan pada Tabel 2.1.

**Tabel 2.1** Matriks Komparasi Penelitian Terdahulu, Celah Riset (*Research Gap*), dan Solusi Kebaruan

| No | Peneliti & Tahun | Metode / Algoritma | Dataset & Variabel | Temuan Utama | Celah Riset (*Research Gap*) | Solusi & Kontribusi Penelitian Ini (Ahmad, 2026) |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Taher & Ayon (2024)** | Random Forest, AdaBoost, Gradient Boosting | Data gaya hidup dan tidur (*Sleep Health & Lifestyle*) | Gradient Boosting mencapai akurasi 93,80% pada klasifikasi gangguan tidur. | Model bekerja murni sebagai *black-box* tanpa XAI; hanya menghasilkan label prediksi tanpa arahan intervensi individual. | Menerapkan metode XAI-SHAP untuk membuka transparansi model dan memetakan kontribusi faktor risiko spesifik per individu. |
| **2** | **Lin et al. (2025)** | ANN, Decision Tree, Naive Bayes | 20.645 data survei kuesioner mahasiswa | Menemukan korelasi signifikan antara durasi layar, kafein, begadang, dan kualitas tidur. | Analisis faktor risiko hanya bersifat agregat populasi umum; tidak mampu memberikan penjelasan personal per individu. | Mengimplementasikan analisis SHAP lokal (*waterfall plot*) yang membedah profil risiko unik masing-masing individu secara interaktif. |
| **3** | **Ha et al. (2023)** | XGBoost + SHAP | 4.622 data kuesioner klinis dari dua rumah sakit | Model meraih AUROC >0,897 untuk klasifikasi OSA, insomnia, dan COMISA. | Model memerlukan *encoding* manual, menggunakan data kuesioner statis, dan SHAP hanya dipakai untuk seleksi fitur awal. | Mengadopsi CatBoost dengan *native categorical handling*, data kebiasaan yang fleksibel diubah (*modifiable*), dan SHAP waktu-nyata. |
| **4** | **Xie et al. (2026)** | PLS + XGBoost + SHAP | Survei gaya hidup dan tidur mahasiswa | Mengidentifikasi durasi tidur, tingkat stres, dan penggunaan gawai sebagai prediktor utama. | XGBoost mewajibkan *one-hot encoding*, memicu fragmentasi fitur pada nilai SHAP sehingga membingungkan secara klinis. | Menggunakan CatBoost (*ordered target statistics*) tanpa *one-hot encoding*, menjaga keutuhan semantik fitur pada visualisasi SHAP. |
| **5** | **Das et al. (2025)** | CatBoost, XGBoost, RF, SVM, GBM, KNN + SHAP | 1.222 data pasien penyakit kronis di RS (*Nature & Sci Sleep*) | CatBoost meraih performa tertinggi (Akurasi 71,67%, AUC 77,27%) dalam prediksi insomnia. | Target klasifikasi terbatas biner, populasi terbatas pasien RS, eksplanasi SHAP hanya global, dan tanpa purwarupa aplikasi web. | Membangun klasifikasi multikelas 4 tingkatan (*Healthy, Mild, Moderate, Severe*) pada 100.000 data, XAI lokal dinamis, dan purwarupa Web CDSS. |

---

## 2.3 Kerangka Berpikir (*Conceptual Framework*)

Kerangka berpikir penelitian ini dibangun berdasarkan alur logis pemecahan masalah kesehatan tidur di era digital melalui pendekatan pembelajaran mesin yang akuntabel. Permasalahan utama diawali dari tingginya prevalensi gangguan tidur yang dipicu oleh pola kebiasaan harian modern, seperti tingginya paparan layar gawai menjelang tidur, beban stres profesional, serta pola istirahat yang tidak teratur. Upaya deteksi dini yang ada saat ini menghadapi dua kendala utama: ketergantungan pada prosedur klinis invasif yang mahal serta kecenderungan model kecerdasan buatan konvensional yang bekerja sebagai kotak hitam (*black-box*) tanpa transparansi alasan medis.

Guna mengatasi permasalahan tersebut, kerangka penelitian ini mengintegrasikan data metrik gaya hidup digital berskala besar (100.000 rekaman data heterogen) ke dalam pipeline pemrosesan data mining CRISP-DM. Masalah ketidakseimbangan sebaran kelas target diatasi secara internal menggunakan pendekatan *Cost-Sensitive Learning* pembobotan penalti kelas terbalik, yang melatih algoritma CatBoost Classifier untuk mengenali pola pasien kelas minoritas berisiko tinggi (*Severe*) secara akurat tanpa merusak data asli melalui manipulasi oversampling. Algoritma CatBoost secara alami memproses atribut kategorikal melalui *Ordered Target Statistics*, sehingga menjaga keutuhan struktur matriks fitur.

Pada tahap interpretabilitas, modul *Tree-SHAP* diterapkan untuk membongkar mekanisme pengambilan keputusan model. Prinsip teori permainan kooperatif menjamin bahwa setiap variabel masukan menerima skor atribusi kontribusi marjinal yang adil, konsisten, dan memenuhi aksioma efisiensi aditif lokal. Keluaran inferensi model CatBoost beserta visualisasi waterfall plot SHAP kemudian diintegrasikan ke dalam antarmuka purwarupa *Clinical Decision Support System* (CDSS) berbasis web interaktif. Sistem ini tidak hanya menyajikan tingkat risiko tidur seseorang, melainkan juga memvisualisasikan faktor pemicu dominan dan menghasilkan rekomendasi perbaikan pola hidup (*sleep hygiene*) yang terpersonalisasi.

Bagan alur logis kerangka berpikir penelitian ini diilustrasikan secara sistematis pada Gambar 2.1:

```text
+---------------------------------------------------------------------------------------------------+
|                                  IDENTIFIKASI MASALAH & CELAH RISET                               |
|  - Prevalensi gangguan tidur meningkat di era digital akibat screen time, stres, & pola hidup buruk|
|  - Model Machine Learning konvensional bersifat Black-Box (tidak transparan bagi tenaga medis)    |
|  - Celah Riset: Fragmentasi One-Hot Encoding pada XAI & belum adanya CDSS multikelas interaktif   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                                        DATA INPUT PENELITIAN                                      |
|  - Sleep Health and Lifestyle Dataset (100.000 Baris Data Tabular Sekunder)                       |
|  - Variabel Heterogen: Numerik (Durasi Tidur, Detak Jantung, Stres) & Kategorikal (Profesi, Gender)|
|  - Distribusi Target 4 Kelas Imbalanced (Healthy 54,2%, Mild 33,5%, Moderate 8,3%, Severe 4,1%)   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                               PROSES KOMPUTASI & PEMODELAN ADAPTIF                                |
|  1. Pra-pemrosesan Data: Eliminasi ID non-prediktif, Stratified 80:20 Data Splitting              |
|  2. CatBoost Handling: Native Categorical Handling via Ordered Target Statistics (Tanpa One-Hot)  |
|  3. Cost-Sensitive Learning: auto_class_weights='Balanced' (Penalti Severe 13,32x lebih berat)   |
|  4. Pemodelan: Symmetric Oblivious Decision Trees & Ordered Boosting (Mencegah Overfitting)       |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                               EVALUASI MODEL & INTERPRETASI XAI-SHAP                               |
|  - Evaluasi Kinerja: Accuracy (95,18%), Severe Recall (89,05%), Macro F1-Score (89,25%)           |
|  - Verifikasi Matematis Manual: Pembuktian Aksioma Aditivitas Efisiensi SHAP f(x) = f0 + Σ phi_i   |
|  - Ekstraksi SHAP: Global Summary Beeswarm Plot (Populasi) & Local Waterfall Plot (Personal)      |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                                       LUARAN TERAPAN PENELITIAN                                   |
|  - Purwarupa Clinical Decision Support System (CDSS) Berbasis Web Interaktif                      |
|  - Visualisasi Transparan Faktor Risiko Dominan Personal per Pasien                               |
|  - Rekomendasi Intervensi Sleep Hygiene Terpersonalisasi Berbasis Bukti Ilmiah                    |
+---------------------------------------------------------------------------------------------------+
```
**Gambar 2.1** Bagan Alir Kerangka Berpikir Integrasi CatBoost dan XAI-SHAP untuk Deteksi Risiko Gangguan Tidur

---

## 2.4 Pertanyaan Penelitian (*Research Questions*)

Berdasarkan rumusan masalah dan kerangka berpikir yang telah dibangun, pertanyaan penelitian operasional yang akan dijawab dan dibuktikan secara empiris dalam penelitian ini adalah sebagai berikut:
1. Apakah penerapan algoritma CatBoost dengan mekanisme *Ordered Target Statistics* dan penanganan ketidakseimbangan kelas berbasis *Cost-Sensitive Learning* mampu menghasilkan performa klasifikasi multikelas yang unggul, khususnya dalam mencapai nilai *Recall* kelas minoritas Severe di atas 85% dan *Macro F1-Score* di atas 85%?
2. Bagaimana efektivitas metode XAI berbasis *Tree-SHAP* dalam mengidentifikasi dan memetakan variabel gaya hidup digital yang paling berkontribusi secara global pada tingkat populasi serta secara lokal pada tingkat individu tanpa kehilangan keutuhan semantik fitur?
3. Bagaimana purwarupa *Clinical Decision Support System* (CDSS) berbasis web yang dirancang mampu menyajikan visualisasi probabilitas prediksi risiko dan penjelasan faktor pemicu dominan secara intuitif guna mendukung pengambilan keputusan intervensi klinis?

---

## DAFTAR PUSTAKA BAB II

Berikut adalah daftar pustaka rujukan Bab 2 yang disusun menggunakan format standar **APA Style 7th Edition**. Seluruh pustaka dilengkapi dengan tautan resmi *Digital Object Identifier* (DOI) aktif serta keterangan status ketersediaan berkas fisik di repositori lokal:

1. **Alqudah, A., et al. (2026)**. Interpretable ensemble learning for tumor-type prediction with a SHAP-based evaluation of CatBoost and voting classifiers. *Scientific Reports*, 16, 31079. https://doi.org/10.1038/s41598-025-31079-x  
   *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/`]*

2. **Amann, J., Blasimme, A., Vayena, E., Frey, D., & Madai, V. I. (2020)**. Explainability for artificial intelligence in healthcare: a multidisciplinary perspective. *BMC Medical Informatics and Decision Making*, 20(1), 310. https://doi.org/10.1186/s12911-020-01332-6  
   *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/s12911-020-01332-6.pdf`]*

3. **Bagus, A., et al. (2025)**. Predictive modeling approach for sleep disorder classification using lifestyle parameters. *Journal of Computational Analysis and Applications*, 33(4), 112–124.  
   *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/B1+Predictive+Modeling+Approach+for+Sleep+Disorder.pdf`]*

4. **Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026)**. Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Psychology*, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946  
   *[Status di Berkas: Tersedia di folder jurnal/Xie_Chen_2026_Sleep_Quality_PLSR_XGBoost.pdf]*

5. **Chen, X., et al. (2025)**. Development and validation of an explainable machine learning model for health risk screening. *Frontiers in Public Health*, 13, 1619406. https://doi.org/10.3389/fpubh.2025.1619406  
   *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/fpubh-13-1619406.pdf`]*

6. **Chicco, D., & Jurman, G. (2020)**. The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. *BMC Genomics*, 21, 6. https://doi.org/10.1186/s12864-019-6413-7  
   *[Status di Berkas: Rujukan Eksternal - Belum Ada di File Lokal]*

7. **Chicco, D., & Jurman, G. (2022)**. An invitation to greater use of Matthews correlation coefficient in robotics and artificial intelligence. *Frontiers in Robotics and AI*, 9, 876814. https://doi.org/10.3389/frobt.2022.876814  
   *[Status di Berkas: Tersedia di folder `jurnal/Jurnal tambahan BAB 3/An Invitation to Greater Use of Matthews...pdf`]*

8. **Das, P., Arif, M., Hasan, M. E., ALmerab, M. M., Al Habib, A., Al Mamun, F., Mamun, M. A., & Gozal, D. (2025)**. Prevalence and factors associated with insomnia among chronic disease patients in Bangladesh: A machine learning study. *Nature and Science of Sleep*, 17, 2725–2741. https://doi.org/10.2147/NSS.S547335  
   *[Status di Berkas: Tersedia di folder `jurnal/NSS-547335-prevalence-and-factors-associated-with-insomnia-among-chroni.pdf`]*

9. **El Chakik, A., Nakhal, B., & Nassreddine, G. (2026)**. Explainable semi-supervised learning framework for Alzheimer’s disease prediction using SHAP-based feature selection and cost-sensitive CatBoost. *Sci*, 8(3), 171. https://doi.org/10.3390/sci8070171  
   *[Status di Berkas: Tersedia di folder `jurnal/Jurnal tambahan BAB 3/Explainable Semi-Supervised Learning Framework...pdf`]*

10. **Ha, S., Choi, S. J., Lee, S., Wijaya, R. H., Kim, J. H., Joo, E. Y., & Kim, J. K. (2023)**. Predicting the risk of sleep disorders using a machine learning–based simple questionnaire: Development and validation study. *Journal of Medical Internet Research*, 25, e46520. https://doi.org/10.2196/46520  
    *[Status di Berkas: Tersedia di folder `jurnal/Predicting the Risk of Sleep Disorders Using a Machine.pdf`]*

11. **Hancock, J. T., & Khoshgoftaar, T. M. (2020)**. CatBoost for big data: an interdisciplinary review. *Journal of Big Data*, 7(1), 94. https://doi.org/10.1186/s40537-020-00369-8  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/CatBoost for big data an interdisciplinary review.pdf`]*

12. **Henrich, L. C., Antypa, N., & Van den Berg, J. F. (2021)**. Sleep quality in students: Associations with psychological and lifestyle factors. *Current Psychology*, 41, 4221–4230. https://doi.org/10.1007/s12144-021-01801-9  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/s12144-021-01801-9.pdf`]*

13. **Huang, Y., et al. (2024)**. On the use of explainable AI for susceptibility modeling: Examining spatial pattern and feature contribution. *Geoscience Frontiers*, 15(4), 101800. https://doi.org/10.1016/j.gsf.2024.101800  
    *[Status di Berkas: Tersedia di folder `jurnal/XAI-SHAP.pdf`]*

14. **Jahrami, H. (2023)**. The relationship between Nomophobia, insomnia, Chronotype, phone in proximity, screen time, and sleep duration in adults: A cross-sectional study. *Healthcare*, 11(10), 1503. https://doi.org/10.3390/healthcare11101503  
    *[Status di Berkas: Rujukan Eksternal - Belum Ada di File Lokal]*

15. **Kaya, C. (2025)**. Comparative analysis of conventional and ensemble machine learning techniques for sleep disorder classification. *Journal of Artificial Intelligence and Data Science (JAIDA)*, 5(2), 132–139.  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/Comparative Analysis of Conventional and Ensemble...pdf`]*

16. **Kumar, R., et al. (2025)**. Impact of excessive screen time on sleep quality and sleep duration among university students. *Journal of Pharmacy and Bioallied Sciences*, 17(2), 944. https://doi.org/10.4103/jpbs.jpbs_944_25  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/impact-of-excessive-screen-time-on-sleep-quality-and-sleep.pdf`]*

17. **Li, X., et al. (2025)**. Exploring the complex associations between community public spaces and healthy aging: An explainable analysis using CatBoost and SHAP. *BMC Public Health*, 25, 23402. https://doi.org/10.1186/s12889-025-23402-y  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/Exploring the complex associations...pdf`]*

18. **Lin, Y., Chen, X., Wang, J., Zhang, H., Liu, M., & Wu, L. (2025)**. Evaluation of sleep quality and influencing factors among medical and non-medical students using machine learning techniques. *Frontiers in Psychiatry*, 16, 1533875. https://doi.org/10.3389/fpsyt.2025.1533875  
    *[Status di Berkas: Tersedia di folder `jurnal/MACHINELEARNING-SLEEPHEALTH.pdf`]*

19. **Loh, H. W., Ooi, C. P., Seoni, S., Barua, P. D., Molinari, F., & Acharya, U. R. (2024)**. A review of Explainable Artificial Intelligence in healthcare: Concepts, algorithms, and applications. *Computers and Electrical Engineering*, 118, 109370. https://doi.org/10.1016/j.compeleceng.2024.109370  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/A review of Explainable Artificial Intelligence in healthcare.pdf`]*

20. **Lundberg, S. M., & Lee, S. I. (2017)**. A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems (NeurIPS)*, 30, 4765–4774. https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html  
    *[Status di Berkas: Rujukan Eksternal - Belum Ada di File Lokal]*

21. **Lundberg, S. M., Erion, G. G., Chen, H., DeGrave, A. J., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S. I. (2020)**. From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence*, 2(1), 56–67. https://doi.org/10.1038/s42256-019-0138-9  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/From local explanations to global understanding...pdf`]*

22. **Medic, G., Wille, M., & Hemels, M. E. (2017)**. Short- and long-term health consequences of sleep disruption. *Nature and Science of Sleep*, 9, 151–161. https://doi.org/10.2147/NSS.S134864  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/NSS-134864-short--and-long-term-health-consequences...pdf`]*

23. **Naga Srinivasu, P., et al. (2022)**. From Blackbox to Explainable AI in healthcare: Existing tools and case studies. *Mobile Information Systems*, 2022, 8167821. https://doi.org/10.1155/2022/8167821  
    *[Status di Berkas: Tersedia di folder `jurnal/XAI-health dataset(2).pdf`]*

24. **Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018)**. CatBoost: unbiased boosting with categorical features. *Advances in Neural Information Processing Systems (NeurIPS)*, 31, 6638–6648. https://doi.org/10.48550/arXiv.1706.09516  
    *[Status di Berkas: Rujukan Eksternal - Belum Ada di File Lokal]*

25. **Putra, J. L., & Hidayat, W. F. (2024)**. Prediksi kualitas tidur: Pendekatan machine learning yang mengintegrasikan faktor kesehatan dan lingkungan. *Computer Science (CO-SCIENCE)*, 4(2), 157–162.  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/jordy_lp,+publish_Jordy+Lasmana+Putra_157-162.pdf`]*

26. **Rahman, M. A., et al. (2025)**. Improving sleep disorder diagnosis through optimized machine learning approaches. *IEEE Access*, 13, 22051–22070. https://doi.org/10.1109/ACCESS.2025.3535535  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/Improving_Sleep_Disorder_Diagnosis_Through_Optimized...pdf`]*

27. **Sari, M., & Wardhana, A. (2025)**. Penerapan machine learning untuk analisis dan klasifikasi kesehatan tidur. *Jurnal Informatika dan Teknik Elektro Terapan (JITET)*, 13(3), 7281. https://doi.org/10.23960/jitet.v13i3.7281  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/7281-Article Text-16339-1-10-20250713.pdf`]*

28. **Srinivasu, P. N., Shafi, J., Arif, M., Debtera, B., & Gudi, A. (2024)**. XAI-driven CatBoost multi-layer perceptron neural network for medical data analysis. *Scientific Reports*, 14, 28674. https://doi.org/10.1038/s41598-024-79620-8  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/XAI-driven CatBoost multi-layer perceptron...pdf`]*

29. **Taher, A., & Ayon, W. I. Z. (2024)**. Exploring sleep disorders: A comparative analysis of machine learning algorithms on sleep health and lifestyle data. *2024 IEEE PEEIACON*, 1–6. https://doi.org/10.1109/PEEIACON63765.2024.10844781  
    *[Status di Berkas: Tersedia di folder `jurnal/ExploringSleepDisordersAComparativeAnalysis...pdf`]*

30. **Uzubuaku, I. A. (2023)**. Sleep health as an economic asset: Evaluating roles of adequate sleep in global labor efficiency. *Multidisciplinary Innovations & Research Analysis (MIRA)*, 4(4), 71–85.  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal_BAB1/MIRA+volume+4+issue+4+2023.pdf`]*

31. **Wahyudi, R., et al. (2026)**. Application of Explainable AI in Disease Prediction Models for Healthcare Decision Systems. *Journal of Sustainable Supply Chain and Technology*, 2(1), 45–58.  
    *[Status di Berkas: Tersedia di folder `jurnal/XAI-Prediksi penyakit jantung.pdf`]*

32. **Wang, Y., et al. (2025)**. Prediction of three-year all-cause mortality using the CatBoost model. *BMC Cardiovascular Disorders*, 25, 4928. https://doi.org/10.1186/s12872-025-04928-w  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/Prediction of three-year all-cause mortality...pdf`]*

33. **Widayati, K. A. (2024)**. Technostress and sleep quality among university students. *Asian Journal of Social Health and Behavior*, 7(4), 197–205. https://doi.org/10.4103/shb.shb_177_24  
    *[Status di Berkas: Tersedia di folder `jurnal/jurnal tambahan BAB2/technostress-and-sleep-quality-among-university-students-in.pdf`]*

34. **Windred, D. P., Burns, A. C., Rutter, M. K., & Phillips, A. J. K. (2024)**. Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. *Sleep*, 47(1), zsad253. https://doi.org/10.1093/sleep/zsad253  
    *[Status di Berkas: Rujukan Eksternal - Belum Ada di File Lokal]*

35. **Zhang, L., et al. (2024)**. Explainable Artificial Intelligence in clinical radiology and diagnostic support. *European Journal of Radiology*, 174, 111403. https://doi.org/10.1016/j.ejrad.2024.111403  
    *[Status di Berkas: Tersedia di folder `jurnal/XAI-SHAP(2).pdf`]*
