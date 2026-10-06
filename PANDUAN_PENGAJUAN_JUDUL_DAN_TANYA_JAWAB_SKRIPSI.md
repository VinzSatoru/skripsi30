# PANDUAN STRATEGIS PENGAJUAN JUDUL SKRIPSI, ANTISIPASI TANYA-JAWAB KRITIS, DAN GLOSARIUM TEKNIS

**Program Studi S1 Teknik Informatika — Fakultas Sains dan Teknologi**  
**Universitas Islam Nahdlatul Ulama (UNISNU) Jepara**

* **Nama Mahasiswa:** Ahmad Novian Dzulfanni
* **NIM:** 231240001438
* **Judul Skripsi:** *Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Klasifikasi Faktor Risiko Gangguan Tidur Berbasis Metrik Gaya Hidup Digital*
* **Berkas Dokumen Word Resmi:** [`PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx`](file:///c:/Users/ahmad/OneDrive/ドキュメント/skripsi/PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx)

---

## DAFTAR ISI
1. [BAGIAN 1: STRATEGI & DRAFT KALIMAT PENGAJUAN JUDUL](#bagian-1-strategi--draft-kalimat-pengajuan-judul)
   * 1.1 Pola Pikir Evaluasi Dosen / Kaprodi
   * 1.2 Opsi A: Naskah Tatap Muka Langsung (Elevator Pitch ±90 Detik)
   * 1.3 Opsi B: Naskah Pesan Daring (WhatsApp / Email Formal)
2. [BAGIAN 2: BANK 10 PERTANYAAN JEBAKAN DOSEN & JAWABAN SKAKMAT ILMIAH](#bagian-2-bank-10-pertanyaan-jebakan-dosen--jawaban-skakmat-ilmiah)
   * Q1: Alasan Pemilihan CatBoost vs XGBoost / Random Forest
   * Q2: Urgensi Explainable AI (SHAP) dibanding Akurasi Semata
   * Q3: Kesiapan, Validitas, dan Skala Dataset (100.000 Data)
   * Q4: Fokus Skripsi: Machine Learning vs Web App (CRISP-DM)
   * Q5: Penanganan Imbalanced Data (Cost-Sensitive Learning vs SMOTE)
   * Q6: Jumlah Training / Iterasi / Early Stopping
   * Q7: Variabel X, Variabel Y, dan Status Variabel Z
   * Q8: Peta Kebaruan (Novelty) terhadap 5 Jurnal SOTA (Termasuk Das et al., 2025)
   * Q9: Evaluasi Macro F1-Score & Recall Severe (89%)
   * Q10: Kaitan Purwarupa Web dengan Manfaat Klinis Nyata
3. [BAGIAN 3: GLOSARIUM LENGKAP ISTILAH ASING & TEKNIS](#bagian-3-glosarium-lengkap-istilah-asing--teknis)
4. [BAGIAN 4: CHECKLIST FISIK & TIPS PSIKOLOGIS SAAT MENGHADAP](#bagian-4-checklist-fisik--tips-psikologis-saat-menghadap)

---

## BAGIAN 1: STRATEGI & DRAFT KALIMAT PENGAJUAN JUDUL

### 1.1 Pola Pikir Evaluasi Dosen / Kaprodi
Saat seorang mahasiswa mengajukan judul skripsi, dosen penguji/Kaprodi biasanya menyaring kelayakan dengan 4 pertanyaan bawah sadar:
1. *Apakah masalahnya nyata, mendesak, dan berbobot di ranah Informatika?*
2. *Apakah mahasiswanya benar-benar paham alasan memilih metode tersebut (bukan sekadar ikut tren)?*
3. *Apakah datanya sudah siap dan valid (agar tidak macet di tengah jalan)?*
4. *Apakah ada luaran produk terapan yang konkret?*

---

### 1.2 OPSI A: Naskah Tatap Muka Langsung (Elevator Pitch ±90 Detik)
> *Gunakan intonasi yang tenang, tatap mata dosen, dan bicara dengan tempo teratur:*

"Selamat pagi/siang, Bapak/Ibu [Nama Kaprodi/Dosen]. Mohon izin mengonsultasikan rencana judul dan topik skripsi saya.

Judul yang saya ajukan adalah:  
**'Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Klasifikasi Faktor Risiko Gangguan Tidur Berbasis Metrik Gaya Hidup Digital'**.

Latar belakang saya mengangkat topik ini adalah tingginya tren gangguan tidur di era modern yang sangat dipengaruhi oleh kebiasaan harian (seperti durasi layar gawai, beban kerja, dan stres). Berdasarkan kajian terhadap 5 jurnal internasional bereputasi terkini—termasuk jurnal *Nature and Science of Sleep* tahun 2025—penelitian deteksi risiko tidur saat ini memiliki dua keterbatasan utama:
1. Banyak algoritma konvensional (seperti XGBoost atau Random Forest) yang mengolah data kategorikal gaya hidup menggunakan *One-Hot Encoding* sehingga memecah keutuhan fitur dan menimbulkan ledakan dimensi data.
2. Model yang dibangun umumnya beroperasi sebagai kotak hitam (*black-box*), sehingga tidak dapat menjelaskan faktor risiko personal pada masing-masing individu secara transparan.

Oleh karena itu, pada penelitian ini saya mengusulkan algoritma **CatBoost** karena memiliki keunggulan *native handling categorical data* tanpa distorsi *One-Hot Encoding*, yang kemudian diintegrasikan dengan metode **Explainable AI berbasis SHAP** untuk menghasilkan penjelasan kontribusi faktor risiko secara lokal per individu (*waterfall plot*) yang adil dan matematis.

Untuk kesiapan teknis, dataset sudah sangat siap sebanyak **100.000 rekaman data gaya hidup** dengan klasifikasi 4 level risiko (*Healthy, Mild, Moderate, Severe*). Luaran akhirnya tidak hanya model komputasi, melainkan diimplementasikan langsung ke dalam **purwarupa Web Clinical Decision Support System (CDSS)** yang interaktif.

Berkas formulir outline resmi dan pemetaan 5 Research GAP-nya sudah saya susun rapi, Pak/Bu. Mohon arahan dan persetujuannya agar saya dapat melanjutkan ke tahap sidang proposal. Terima kasih, Pak/Bu."

---

### 1.3 OPSI B: Naskah Pesan Daring (Format WhatsApp / Email Formal)

```text
Assalamu’alaikum Warahmatullahi Wabarakatuh / Selamat Pagi Bapak/Ibu [Nama Kaprodi],

Mohon maaf mengganggu waktu Bapak/Ibu. Saya Ahmad Novian Dzulfanni (NIM: 231240001438), mahasiswa S1 Teknik Informatika peminatan Sains Data dan Machine Learning.

Izin menyampaikan pengajuan rencana judul dan topik skripsi untuk dimohonkan telaah serta persetujuannya:

📌 Usulan Judul:
"Penerapan Metode XAI-SHAP pada Algoritma CatBoost untuk Klasifikasi Faktor Risiko Gangguan Tidur Berbasis Metrik Gaya Hidup Digital"

📌 Urgensi Masalah:
Peningkatan gangguan tidur era digital sangat dipicu oleh faktor gaya hidup yang dapat dimodifikasi (screen time, kafein, stres). Namun, model machine learning medis saat ini umumnya bersifat kotak hitam (black-box) sehingga tidak mampu menjelaskan alasan di balik keputusan prediksi per individu.

📌 Solusi Metodologi & Kebaruan (Novelty):
1. Menggunakan CatBoost yang memproses data gaya hidup heterogen secara native tanpa merusak data lewat One-Hot Encoding.
2. Menerapkan XAI-SHAP untuk membedah kontribusi faktor risiko secara transparan dan adil bagi setiap individu (waterfall plot real-time).
3. Menutup celah riset dari 5 jurnal internasional terkini (termasuk Das et al., Nature and Science of Sleep 2025) dengan menghadirkan klasifikasi multi-kelas 4 tingkat risiko.

📌 Kesiapan Riset & Luaran:
- Dataset: 100.000 data gaya hidup digital terstruktur.
- Luaran Akhir: Model klasifikasi CatBoost-SHAP + Purwarupa Web Clinical Decision Support System (CDSS) interaktif.

Bersama pesan ini, saya lampirkan dokumen formulir Outline Proposal resmi (OUTLINE_PROPOSAL_REVISI_FINAL.docx) yang telah memuat tabel matriks Research GAP lengkap sebagai bahan pertimbangan Bapak/Ibu.

Besar harapan saya topik ini dapat disetujui untuk melangkah ke tahap seminar proposal. Terima kasih banyak atas waktu dan bimbingan Bapak/Ibu.

Wassalamu’alaikum Warahmatullahi Wabarakatuh.
Ahmad Novian Dzulfanni (231240001438)
```

---

## BAGIAN 2: BANK 10 PERTANYAAN JEBAKAN DOSEN & JAWABAN SKAKMAT ILMIAH

### Pertanyaan 1: Kenapa harus pakai CatBoost? Kenapa tidak Random Forest, SVM, atau XGBoost yang lebih populer?
> **Jawaban Anda:**  
> "Data gaya hidup memadukan fitur numerik dan kategorikal (seperti jenis pekerjaan, gender, dan kondisi mental). Algoritma konvensional seperti XGBoost dan Random Forest mewajibkan *One-Hot Encoding* yang memecah satu kolom kategori menjadi puluhan kolom biner artifisial, sehingga memicu ledakan dimensi data dan membuat penjelasan SHAP terpecah-pecah.  
> CatBoost memiliki mekanisme bawaan *Ordered Target Statistics* yang memproses data kategorikal secara native tanpa *One-Hot Encoding*, serta menggunakan *Symmetric Oblivious Trees* yang bertindak sebagai regularisasi alami pencegah *overfitting* dan mempercepat komputasi inferensi."

### Pertanyaan 2: Kenapa butuh Explainable AI (SHAP)? Bukankah di Machine Learning yang penting akurasinya tinggi?
> **Jawaban Anda:**  
> "Di bidang kesehatan, akurasi tinggi saja belum cukup, Pak/Bu. Model ensemble seperti CatBoost terdiri atas ratusan pohon keputusan yang rumit sehingga bersifat *black-box*. Jika sistem mendeteksi seorang pasien berisiko tinggi tanpa penjelasan, dokter dan pasien tidak akan percaya dan tidak tahu apa yang harus diperbaiki.  
> SHAP yang berbasis *cooperative game theory* (*Shapley Values*) menjamin perhitungan kontribusi setiap variabel secara adil, konsisten, dan aditif. Melalui analisis lokal (*waterfall plot*), pasien bisa tahu pasti bahwa risikonya tinggi akibat *screen time* 8 jam dan stres level 7, sehingga rekomendasi *sleep hygiene* yang diberikan tepat sasaran."

### Pertanyaan 3: Datanya dari mana? Jangan-jangan data sekunder sedikit atau data main-main?
> **Jawaban Anda:**  
> "Data penelitian kami berskala besar dan terstruktur, yaitu 100.000 rekaman data gaya hidup digital yang mencakup 28 fitur relevan (durasi tidur, detak jantung, *screen time*, kafein, langkah harian, hingga kondisi mental). Data ini bebas dari nilai hilang (*missing values*) dan memiliki sebaran target 4 kelas (*Healthy, Mild, Moderate, Severe*) yang sangat representatif untuk simulasi sistem deteksi dini."

### Pertanyaan 4: Fokus skripsimu ini di mana? Menguji algoritma Machine Learning atau membuat aplikasi Web?
> **Jawaban Anda:**  
> "Fokus utama penelitian saya 80% berada pada eksperimen Sains Data dan *Machine Learning* terapan dengan mengadopsi standar industri CRISP-DM secara utuh.  
> Tahap 1 sampai 5 (*Business Understanding* hingga *Evaluation*) berfokus penuh pada perancangan CatBoost, penanganan *imbalanced data*, dan validasi matematis XAI-SHAP.  
> Sedangkan purwarupa Web CDSS adalah tahap ke-6 (*Deployment*) sebagai *Proof of Concept* (pembuktian terapan) agar kecerdasan model tidak berhenti di notebook, melainkan bisa dioperasikan secara nyata oleh dokter dan pasien. Jadi sistem web adalah media hilirisasi dari otak model *Machine Learning*-nya."

### Pertanyaan 5: Data kamu sangat tidak seimbang (Severe cuma 4%), bagaimana cara mengatasinya dan kenapa tidak pakai SMOTE atau Undersampling?
> **Jawaban Anda:**  
> "Kami menerapkan pendekatan *Cost-Sensitive Learning* bawaan CatBoost melalui `auto_class_weights='Balanced'`. Kami tidak menggunakan *Undersampling* karena tidak ingin membuang 50.000 data riil orang sehat, dan tidak menggunakan SMOTE karena pembuatan data sintetis pada kombinasi data kategorikal berisiko merusak relasi logis variabel medis dan memicu *overfitting*.  
> Secara matematis, mekanisme *Balanced Loss* memberikan penalti hukuman 13 kali lipat lebih berat pada kelas *Severe* (bobot 6,15) dibanding kelas *Healthy* (bobot 0,46), sehingga algoritma dipaksa secara matematis untuk memprioritaskan pendeteksian pasien risiko parah tanpa memanipulasi data aslinya."

### Pertanyaan 6: Kamu training data berapa kali sehingga dapat akurasi yang sesuai?
> **Jawaban Anda:**  
> "Proses training dilakukan melalui dua aspek terstruktur:  
> 1. Secara Eksperimen Metodologis: Kami menguji skenario *hyperparameter tuning* secara sistematis membandingkan *learning rate* (0.01 s/d 0.05), *depth* (4, 6, 8), dan skema pembobotan kelas untuk memperoleh kombinasi parameter terbaik.  
> 2. Secara Algoritma Internal: CatBoost dilatih dengan batas maksimum 1.000 iterasi pohon, tetapi dikontrol oleh *Early Stopping* sebanyak 50 putaran evaluasi terhadap 20.000 data uji validasi. Begitu performa validasi tidak lagi membaik dalam 50 putaran, proses pelatihan langsung berhenti otomatis di titik konvergensi optimal untuk mencegah *overfitting*."

### Pertanyaan 7: Pada dataset ini, apa atribut yang menjadi X, Y, dan Z?
> **Jawaban Anda:**  
> "Dalam konvensi *supervised learning*, hanya terdapat variabel X dan Y:  
> * **Variabel Y (Target):** 1 kolom yaitu `sleep_disorder_risk` yang terdiri dari 4 kelas klasifikasi (*Healthy, Mild, Moderate, Severe*).  
> * **Variabel X (Fitur Prediktor):** 27–28 variabel masukan yang mencakup parameter gaya hidup digital, metrik tidur, kondisi fisiologis, dan lingkungan.  
> * **Variabel Z:** Tidak ada variabel Z dalam dataset asli. Namun jika dikaitkan dengan metode XAI, nilai Z merepresentasikan Matriks Kontribusi SHAP yang dihitung untuk menjelaskan pengaruh masing-masing fitur X terhadap keputusan Y.  
> Selain itu, atribut `person_id`, `country`, dan `day_type` sengaja dibuang (*drop*) untuk mencegah bias geografis dan menghapus atribut tanpa nilai prediktif."

### Pertanyaan 8: Apa kebaruan (novelty) risetmu dibanding penelitian yang sudah ada sebelumnya?
> **Jawaban Anda:**  
> "Penelitian ini mengisi celah dari 5 jurnal internasional bereputasi terkini yang 100% homogen di domain gangguan tidur:  
> 1. Taher & Ayon (2024) hanya model *black-box* tanpa penjelasan faktor risiko personal.  
> 2. Lin et al. (2025) hanya menganalisis faktor tidur pada tingkat populasi umum secara agregat.  
> 3. Ha et al. (2023) menggunakan data kuesioner statis dan SHAP hanya untuk seleksi fitur awal.  
> 4. Chen et al. (2024) memakai XGBoost dengan *One-Hot Encoding* yang membuat eksplanasi SHAP terfragmentasi.  
> 5. Das et al. (2025 di *Nature and Science of Sleep*) membuktikan CatBoost-SHAP unggul, namun terbatas pada target biner pasien rumah sakit dan visualisasi global saja.  
> Kebaruan penelitian ini adalah mengintegrasikan CatBoost native dengan SHAP waterfall lokal per individu untuk klasifikasi multi-kelas 4 level risiko pada 100.000 data gaya hidup serta diimplementasikan ke Web CDSS interaktif."

### Pertanyaan 9: Kenapa kamu mengevaluasi performa menggunakan Macro F1-Score dan Recall Severe, bukan cuma Akurasi?
> **Jawaban Anda:**  
> "Karena dataset kami mengalami ketidakseimbangan kelas (*Healthy* 54% vs *Severe* 4%), evaluasi hanya dengan akurasi akan menimbulkan fenomena *Accuracy Paradox* di mana model terlihat pintar padahal hanya menebak kelas mayoritas.  
> Oleh karena itu, kami memvalidasi performa dengan:  
> 1. **Recall Severe sebesar 89%:** Membuktikan bahwa dari seluruh pasien yang benar-benar sakit parah, hampir 90% berhasil dideteksi dengan tepat tanpa kecolongan (minim *False Negative*).  
> 2. **Macro F1-Score sebesar 89%:** Memberikan bobot hak suara yang sama rata (masing-masing 25%) pada tiap kelas tanpa memandang jumlah data, membuktikan keandalan model merata di semua level risiko."

### Pertanyaan 10: Bagaimana kaitan purwarupa Web ini dengan dunia klinis nyata?
> **Jawaban Anda:**  
> "Web CDSS ini berfungsi sebagai jembatan komunikasi antara pasien dan tenaga medis. Pasien dapat melakukan skrining mandiri secara cepat berdasarkan kebiasaan hariannya, sementara dokter mendapatkan visualisasi grafik *waterfall* yang membedah kebiasaan buruk spesifik pasien tersebut.  
> Dengan demikian, rekomendasi intervensi medis yang diberikan bersifat personal, tepat sasaran, dan didukung bukti komputasi yang transparan, bukan sekadar tebakan umum."

---

## BAGIAN 3: GLOSARIUM LENGKAP ISTILAH ASING & TEKNIS

| No | Istilah Teknis | Definisi Ilmiah Akademis | Bahasa Manusia (Analogi Dosen) |
|:---:|---|---|---|
| **1** | **Explainable AI (XAI)** | Cabang ilmu AI yang berfokus agar keluaran keputusan algoritma *machine learning* dapat dipahami dan dipercaya oleh manusia secara transparan. | Membuka 'kap mesin' AI agar kita tahu alasan logis mengapa sistem mengeluarkan diagnosis tertentu. |
| **2** | **SHAP (Shapley Additive exPlanations)** | Kerangka kerja interpretasi model berbasis *cooperative game theory* yang menghitung kontribusi marjinal setiap fitur terhadap hasil prediksi secara adil dan konsisten. | Seperti menilai kontribusi masing-masing pemain bola dalam tim untuk menentukan siapa yang paling berjasa mencetak gol. |
| **3** | **CatBoost (Categorical Boosting)** | Algoritma *gradient boosting decision trees* yang dirancang khusus untuk menangani fitur kategorikal secara *native* menggunakan *Ordered Target Statistics*. | Algoritma pohon keputusan canggih yang sangat pintar mengolah data teks/kategori tanpa perlu diubah manual jadi angka biner. |
| **4** | **Ordered Target Statistics** | Mekanisme pengkodean fitur kategorikal pada CatBoost berdasarkan urutan acak data untuk mencegah *target leakage* dan *overfitting*. | Cara cerdas mengubah teks kategori jadi angka bobot tanpa 'mengintip' kunci jawaban data pengujian. |
| **5** | **Symmetric Oblivious Trees** | Arsitektur pohon keputusan biner yang menerapkan kriteria pembagian (*split*) yang persis sama di seluruh simpul pada level kedalaman yang sama. | Pohon keputusan yang bentuk cabangnya seimbang dan rapi kiri-kanan, sehingga proses eksekusi sangat cepat dan tahan hafalan data. |
| **6** | **Black-Box Model** | Model *machine learning* yang proses penalaran keputusannya sangat rumit sehingga tidak bisa dilihat secara kasat mata oleh manusia. | Sistem yang menerima masukan lalu mengeluarkan hasil, tapi proses di dalamnya seperti ruang gelap gulita tanpa jendela. |
| **7** | **Imbalanced Data** | Kondisi dataset di mana jumlah sampel pada satu kelas target jauh lebih banyak dibandingkan kelas lainnya (Healthy 54% vs Severe 4%). | Kondisi ketika populasi orang sehat melimpah ruah dibanding orang yang sakit parah dalam data survei. |
| **8** | **Accuracy Paradox** | Kondisi menipu di mana skor akurasi sangat tinggi pada data tidak seimbang, padahal model hanya menebak kelas mayoritas dan gagal mengenali kelas minoritas. | Dokter yang selalu menebak 'kamu sehat' ke semua orang. Akurasinya 90% karena mayoritas memang sehat, tapi 10 orang sakit parah dibiarkan tanpa diobati. |
| **9** | **Cost-Sensitive Learning (`Balanced`)** | Pendekatan pelatihan yang memberi bobot penalti kerugian (*loss*) jauh lebih berat pada kelas minoritas dibanding kelas mayoritas saat terjadi kesalahan. | Aturan ujian di mana salah soal orang sakit parah dikurangi 6 poin, sedangkan salah soal orang sehat hanya dikurangi 0,4 poin. |
| **10** | **Stratified Sampling 80:20** | Teknik membagi dataset menjadi data latih dan data uji dengan mempertahankan persentase proporsi masing-masing kelas target secara identik. | Memotong kue lapis sehingga potongan latihan dan potongan pengujian sama-sama memiliki proporsi rasa yang seimbang persis dengan kue aslinya. |
| **11** | **Macro-averaged F1-Score** | Metrik yang menghitung F1-score tiap kelas secara individual lalu merata-ratakannya dengan bobot hak suara yang sama rata (25% per kelas). | Sistem pemilu di mana suara daerah terpencil memiliki kekuatan suara yang setara dengan daerah padat penduduk. |
| **12** | **Recall (Sensitivitas)** | Metrik yang mengukur proporsi kasus positif aktual yang berhasil diidentifikasi secara tepat oleh model: $\frac{TP}{TP + FN}$. | Dari 100 orang yang benar-benar sakit parah, berapa orang yang berhasil dijaring oleh sistem dan tidak lolos dari pemeriksaan. |
| **13** | **Precision (Presisi)** | Metrik yang mengukur seberapa banyak tebakan positif model yang memang terbukti benar di kenyataan: $\frac{TP}{TP + FP}$. | Dari 100 orang yang divonis sakit oleh sistem, berapa orang yang benar-benar sakit sesungguhnya. |
| **14** | **Confusion Matrix 4x4** | Tabel kontingensi yang memetakan perbandingan antara kelas aktual dengan kelas prediksi model untuk melihat rincian letak kesalahan klasifikasinya. | Tabel rekapitulasi nilai ujian yang menunjukkan di bagian mana sistem menjawab benar dan di mana sistem salah menebak. |
| **15** | **Waterfall Plot (SHAP)** | Visualisasi penjelasan lokal yang membedah bagaimana nilai dasar prediksi bergeser naik/turun akibat kontribusi fitur seorang pasien. | Struk rincian tagihan belanja yang menjelaskan dari saldo awal, item apa yang menambah biaya dan item apa yang memberi diskon hingga keluar harga akhir. |
| **16** | **Summary Plot / Beeswarm** | Visualisasi agregat yang merangkum tingkat kepentingan (*importance*) seluruh fitur dan arah pengaruhnya pada tingkat keseluruhan populasi. | Peta survei nasional yang memperlihatkan faktor apa saja yang secara umum paling sering membuat masyarakat sulit tidur lelap. |
| **17** | **Data Leakage / Target Leakage** | Kondisi keliru di mana variabel masukan memuat informasi yang seharusnya baru diketahui setelah target terjadi, memicu akurasi palsu. | Mahasiswa yang bisa menjawab soal ujian karena lembar kunci jawabannya tidak sengaja tertempel di balik lembar soal. |
| **18** | **Early Stopping** | Mekanisme yang memantau performa validasi di setiap iterasi dan menghentikan pelatihan otomatis jika skor validasi tidak lagi membaik. | Berhenti memasak sayur tepat saat kuah sudah mendidih matang sempurna, sehingga masakan tidak gosong atau terlalu lembek. |
| **19** | **CRISP-DM** | Standar proses penambangan data industri yang terdiri dari 6 tahapan berulang dari *Business Understanding* hingga *Deployment*. | Buku panduan resep kerja resmi para ilmuwan data dunia agar proyek AI terarah rapi dari perencanaan sampai jadi aplikasi siap pakai. |
| **20** | **CDSS (Clinical Decision Support System)** | Perangkat lunak interaktif yang membantu tenaga medis menganalisis data klinis guna mendukung pengambilan keputusan preventif/diagnostik. | Aplikasi asisten cerdas bagi dokter yang memberikan saran analisis risiko dan alasan medisnya, tetapi vonis akhir tetap di tangan dokter. |
| **21** | **Modifiable Lifestyle Factors** | Variabel perilaku sehari-hari yang berada di bawah kendali kehendak individu untuk diperbaiki (*screen time*, olahraga, kafein). | Kebiasaan buruk yang sebenarnya bisa kita ubah sendiri jika kita sadar, berbeda dengan faktor takdir seperti genetik keluarga. |

---

## BAGIAN 4: CHECKLIST FISIK & TIPS PSIKOLOGIS SAAT MENGHADAP

1. **Berkas Fisik yang Wajib Dibawa dalam Map Rapi:**
   * Cetak Formulir Outline Proposal Resmi ([`OUTLINE_PROPOSAL_REVISI_FINAL.docx`](file:///c:/Users/ahmad/OneDrive/ドキュメント/skripsi/OUTLINE_PROPOSAL_REVISI_FINAL.docx)).
   * Pastikan halaman **Tabel Research GAP (5 Jurnal SOTA)** dan **Matriks Novelty** mudah dibuka langsung.
   * Siapkan laptop/gawai yang siap membuka purwarupa Web CDSS jika dosen penasaran ingin melihat demonya.

2. **Prinsip "Show, Don't Tell" (Tunjukkan Buktinya, Jangan Cuma Bicara):**
   * Saat dosen menanyakan kebaruan, langsung buka halaman Tabel Research GAP dan tunjukkan nama **Das et al. (2025)** di jurnal *Nature and Science of Sleep*.
   * Saat dosen menanyakan data, sebutkan angka pasti: *"100.000 data terbagi 80:20 stratified"*. Dosen sangat menyukai angka yang spesifik dan pasti.

3. **Sikap Saat Terjadi Perdebatan atau Dosen Menyela:**
   * Jangan pernah memotong kalimat dosen. Dengarkan sampai selesai, anggukkan kepala sebagai tanda menghargai.
   * Awali respons dengan: *"Terima kasih atas masukannya, Bapak/Ibu. Izin menjelaskan pertimbangan teknis di balik keputusan tersebut..."*
   * Jika dosen menyarankan perubahan kecil pada redaksi kata judul, terimalah dengan lapang dada: *"Baik Bapak/Ibu, saran penyempurnaan redaksinya sangat baik dan akan segera saya sesuaikan."*
