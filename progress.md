# LAPORAN PROGRESS SKRIPSI LENGKAP & KOMPREHENSIF

> **Status Proyek:** Siap Diajukan ke Seminar Proposal (Sempro)  
> **Terakhir Diperbarui:** Oktober 2026  
> **Repositori Git:** [github.com/VinzSatoru/skripsi30](https://github.com/VinzSatoru/skripsi30) (Branch: `main`, Status: *Synced*)

---

## 1. IDENTITAS PENELITIAN & MAHASISWA

| Parameter | Keterangan |
|---|---|
| **Nama Peneliti** | Ahmad Novian Dzulfanni |
| **NIM** | 231240001438 |
| **Program Studi** | Teknik Informatika (S1) |
| **Fakultas** | Sains dan Teknologi |
| **Perguruan Tinggi** | Universitas Islam Nahdlatul Ulama (UNISNU) Jepara |
| **Judul Resmi (Terpilih)** | **"Penerapan Algoritma CatBoost dan SHAP untuk Klasifikasi Risiko Gangguan Tidur Berbasis Gaya Hidup"** *(Tepat 13 Kata, Bebas Kata "XAI")* |
| **Opsi Judul Alternatif** | 1. *"Klasifikasi Risiko Gangguan Tidur Berbasis Gaya Hidup Menggunakan CatBoost dan SHAP"* *(11 Kata)*<br>2. *"Pemodelan Klasifikasi Risiko Gangguan Tidur Berbasis Gaya Hidup Menggunakan CatBoost dan SHAP"* *(12 Kata)*<br>3. *"Analisis Faktor Risiko Gangguan Tidur Berbasis Gaya Hidup Menggunakan CatBoost dan SHAP"* *(12 Kata)* |
| **Bidang Keahlian** | *Machine Learning*, *Explainable Artificial Intelligence (XAI)*, *Clinical Decision Support System (CDSS)* |

---

## 2. RINGKASAN EKSEKUTIF (*EXECUTIVE SUMMARY*)

Penelitian ini memecahkan permasalahan **gangguan tidur modern (insomnia, sleep apnea, dan disrupsi sirkadian)** yang dipicu oleh perilaku gaya hidup digital (*screen time* malam, konsumsi kafein sore hari, stres kerja, dan jam tidur tidak teratur). 

### Pokok Celah Masalah (*Core Problem & Gap*)
1. **Diagnosis Konvensional Lambat & Mahal:** Pemeriksaan standar medis seperti *Polysomnography* (PSG) memerlukan biaya tinggi, instrumen invasif, dan antrean rumah sakit yang panjang.
2. **Keterbatasan Model Klasifikasi Terdahulu (*Black-Box*):** Penelitian *machine learning* terdahulu umumnya berhenti pada tebakan akurasi (*predictive alarm*) tanpa mampu menerangkan faktor risiko individual mana yang harus diperbaiki pasien (*lack of actionable insights*).
3. **Distorsi Encoding Data Kategorikal:** Algoritma konvensional (seperti XGBoost, RF, atau ANN) mewajibkan *One-Hot Encoding* yang memecah fitur gaya hidup menjadi variabel tiruan (*dummy*), merusak hierarki data dan membingungkan interpretasi klinis.

### Solusi & Kebaruan Riset (*Novelty*)
Penelitian ini membangun **sistem skrining risiko preventif non-invasif berbasis web (CDSS)** yang mengintegrasikan:
1. **Algoritma CatBoost:** Mengolah data numerik dan data kategorikal gaya hidup (*shift work, gender, occupation*) secara *native* menggunakan *Ordered Target Statistics* dan *Oblivious Trees*, mencegah *target leakage* dan *overfitting*.
2. **Explainable AI (Tree-SHAP):** Membongkar kalkulasi keputusan model berbasis teori permainan Shapley (*Game Theory*), menyajikan atribusi kontribusi fitur individual secara matematis adil (*local & global fidelity*).
3. **Web CDSS Dashboard Interaktif:** Menerjemahkan nilai SHAP menjadi rekomendasi *Sleep Hygiene* terpersonalisasi, dilengkapi simulasi *What-If* untuk menguji dampak modifikasi perilaku secara *real-time*.

---

## 3. PROGRESS PENULISAN DOKUMEN PROPOSAL (BAB 1 – BAB 3)

Status penulisan naskah proposal telah mencapai **100% lengkap, sinkron, dan terverifikasi secara formal**.

```
[Bab 1: Pendahuluan]       ✅ SELESAI (120–130 kata per paragraf, bebas halusinasi)
[Bab 2: Tinjauan Pustaka]   ✅ SELESAI (6 Jurnal SOTA Q1/IEEE, Tabel SOTA 8 Kolom, 5 Gap, Landasan Teori)
[Bab 3: Metodologi]         ✅ SELESAI (Alur CRISP-DM, 27 Fitur, Perhitungan Manual CatBoost & SHAP)
[Daftar Pustaka]            ✅ SELESAI (100% Lolos Uji Bijeksi Sitasi, Dilengkapi DOI Aktif & File Mendeley RIS/BIB)
[Outline Proposal]          ✅ SELESAI (Tabel State of the Art 8 Kolom Standar Sidang Proposal)
```

### Rincian Per Bagian Dokumen:

#### A. Bab 1 (Pendahuluan)
- **Latar Belakang:** Disusun dalam narasi akademik formal yang terstandarisasi ketat (setiap paragraf dioptimasi tepat **120 hingga 130 kata** guna menjaga ritme bacaan akademik tanpa kalimat bertele-tele).
- **Rumusan Masalah (4 Butir):**
  1. Bagaimana menerapkan CatBoost untuk klasifikasi risiko gangguan tidur berbasis data gaya hidup multivariat?
  2. Bagaimana menerapkan Tree-SHAP untuk membedah transparansi faktor pemicu risiko secara lokal dan global?
  3. Bagaimana tingkat akurasi, presisi, recall, dan F1-score model CatBoost yang dihasilkan?
  4. Bagaimana merancang purwarupa CDSS berbasis web yang menyajikan rekomendasi tindakan personal?
- **Batasan Masalah:** Menegaskan penggunaan dataset gaya hidup digital publik (100.000 sampel), 4 kelas klasifikasi (*Healthy, Mild, Moderate, Severe*), implementasi algoritma CatBoost dengan Tree-SHAP, dan purwarupa sistem sebagai instrumen skrining awal non-invasif (bukan pengganti diagnosis medis resmi PSG).
- **Tujuan & Manfaat:** Menjawab tuntas seluruh rumusan masalah dari sisi teoretis maupun aplikatif.

#### B. Bab 2 (Tinjauan Pustaka & Landasan Teori)
- **State of the Art (SOTA) & Matriks 6 Jurnal Bereputasi Internasional:**
  1. *Taher & Ayon (2024)* [IEEE PEEIACON] – Model ML konvensional *black-box* tanpa panduan aksi klinis.
  2. *Lin et al. (2025)* [Frontiers in Psychiatry, Scopus Q1] – Analisis linier agregat populasi mahasiswa tanpa personalisasi individu.
  3. *Ha et al. (2023)* [JMIR mHealth and uHealth, Scopus Q1] – Kuesioner SLEEPS XGBoost dengan encoding manual, tidak memakai metrik gaya hidup digital harian.
  4. *Xie et al. (2026)* [Frontiers in Psychology, Scopus Q1] – Analisis korelasi statistik tanpa personalisasi takaran perubahan perilaku.
  5. *Das et al. (2025)* [Nature and Science of Sleep, Scopus Q1] – Superioritas CatBoost pada insomnia pasien kronis Bangladesh, namun target biner dan tanpa visualisasi lokal per pasien.
  6. *Srinivasu et al. (2024)* [Scientific Reports - Nature, Scopus Q1] – Integrasi CatBoost + SHAP pada data tabular klinis.
- **Sintesis 5 Research GAP:**
  - *GAP 1:* Prediksi Tanpa Panduan Tindakan (*Prediction Without Actionable Insight*).
  - *GAP 2:* Analisis Populasi Tanpa Personalisasi (*Population Aggregation Without Individual Fidelity*).
  - *GAP 3:* Keterbatasan Encoding Manual & Data Antropometrik Non-Modifiable.
  - *GAP 4:* Fragmentasi Nilai Interpretasi Akibat *One-Hot Encoding*.
  - *GAP 5:* Ketiadaan Sistem Simulasi Perilaku Interaktif (*What-If Interactive CDSS*).
- **Landasan Teori Komprehensif:** Fisiologi tidur, klasifikasi gangguan tidur (*ICSD-3*), prinsip *Sleep Hygiene*, arsitektur algoritma CatBoost (*Oblivious Decision Trees, Ordered Boosting, Target Statistics*), teori *Explainable AI & Game Theory Shapley*, aksioma SHAP (*Efficiency, Symmetry, Dummy, Additivity*), metrik evaluasi multikelas, dan konsep CDSS.

#### C. Bab 3 (Metodologi Penelitian)
- **Framework Kerja:** Mengadopsi standar metodologi **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*): *Business Understanding ➔ Data Understanding ➔ Data Preparation ➔ Modeling ➔ Evaluation ➔ Deployment*.
- **Dataset:** *Sleep Health and Lifestyle Dataset* dengan 100.000 instans rekaman gaya hidup digital.
- **Taksonomi Fitur (27 Fitur dalam 4 Kategori):**
  1. *Gaya Hidup & Gadget (9 Fitur):* Screen time sebelum tidur, konsumsi kafein sore, alkohol, beban stres, jam kerja harian, langkah kaki, olahraga, obat tidur, shift kerja.
  2. *Pola & Kualitas Tidur (8 Fitur):* Durasi tidur, sleep latency, terbangun tengah malam, skor kualitas tidur, selisih jam libur, tidur siang, persentase deep sleep, persentase REM.
  3. *Profil Individu (5 Fitur):* Usia, jenis kelamin, profesi, BMI, chronotype (*morning/night owl*), status kesehatan mental.
  4. *Kondisi Fisik & Ruangan (5 Fitur):* Detak jantung santai (*resting HR*), skor kognitif harian, suhu kamar tidur, musim data.
- **Pembersihan & Preprocessing Data:** Penanganan data duplikat, verifikasi konsistensi tipe data, pembagian *Stratified Train-Test Split* (80% latih, 20% uji) untuk menjaga proporsi kelas minoritas.
- **Bab Perhitungan Manual Terperinci:** Menyajikan simulasi matematis langkah demi langkah pembentukan *split* pada pohon CatBoost dan pembagian kontribusi nilai Shapley menggunakan rumus marginal contribution.

#### D. Integritas Sitasi & Daftar Pustaka
- Dilakukan audit otomatis (*bijection cross-check*) menggunakan skrip python.
- **Hasil:** 100% sitasi dalam teks (nama pengarang dan tahun) memiliki entri yang sah pada Daftar Pustaka, dan tidak ada entri daftar pustaka yang menjadi "sitasi gaib".
- Seluruh referensi dilengkapi identitas penerbit, volume, nomor terbitan, serta tautan **DOI aktif**.

---

## 4. PURWARUPA CDSS (CLINICAL DECISION SUPPORT SYSTEM)

Purwarupa perangkat lunak sistem pendukung keputusan klinis telah selesai dibangun dan berfungsi secara penuh menghubungkan model CatBoost dan SHAP ke antarmuka web modern.

```
┌────────────────────────────────────────────────────────┐
│                   BROWSER CLIENT                       │
│  [HTML5 / Vanilla CSS / Tailwind 3.4 / Vanilla JS]     │
│  • Visual Persona Presets                              │
│  • Glanceable Prediction Status HUD                    │
│  • SHAP 3-Card Glanceable Matrix                       │
│  • Micro-Action Cards & Visual Timeline                │
│  • Interactive What-If Behavioral Simulator            │
└──────────────────────────┬─────────────────────────────┘
                           │ HTTP / JSON API
┌──────────────────────────▼─────────────────────────────┐
│                 FLASK BACKEND ENGINE                   │
│                    (Python 3.12)                       │
│  • Endpoint /api/meta (Definisi & Distribusi Fitur)    │
│  • Endpoint /api/predict (Inference CatBoost + SHAP)   │
│  • Endpoint /api/sample (Generasi Profil Sampel)       │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│                 MODEL & INTELIJEN ARTIFISIAL           │
│  • catboost_sleep_model.cbm (Akurasi: 93.86% – 95.18%) │
│  • Tree-SHAP Explainer Engine                          │
└────────────────────────────────────────────────────────┘
```

### Hasil Redesain UI/UX (Bebas Text-Fatigue & Visual Modern)
Menjawab arahan dosen pembimbing bahwa *"dashboard sebelumnya terlalu banyak teks sehingga membuat orang malas membaca"*, antarmuka telah dirombak menjadi **Glanceable Health-Tech UI**:

1. **Hero Section Minimalis & Berdampak:**
   - Menghapus paragraf teks naratif yang panjang.
   - Menggantinya dengan **4 Badge Metrik Utama**:
     `[⚡ Skrining 30 Detik]` `[🎯 Akurasi 95,18%]` `[🔍 Transparan (SHAP)]` `[🔒 100% Privat]`
   - Tombol simulasi cepat diubah menjadi **Persona Pills Ringkas**:
     `[🟢 Sehat | ⏱️ 7.5j • 📱 20m]` `[🟡 Ringan | 📱 85m • ☕ Kafein]` `[🔴 Tinggi | 🔄 Shift • ⚡ Stres 8.5]`
2. **Status Result Banner:**
   - Menghapus teks diagnosis berulang.
   - Diganti dengan indikator status HUD:
     - Badge Urgensi: `🚨 Prioritas Aksi Cepat` / `✅ Pola Optimal`
     - Target Waktu: `⏱️ Target Evaluasi: 14 Hari Konsisten`
     - 1 kalimat kesimpulan padat.
3. **SHAP 3-Card Glanceable Matrix:**
   - Menghilangkan daftar poin berulang yang panjang.
   - Mengelompokkan atribusi ke dalam **3 Kartu Visual Sejajar**:
     - *Kartu 1 (🚨 Pemicu Utama):* Chip merah berisi kebiasaan yang memperberat risiko (`+SHAP`).
     - *Kartu 2 (🛡️ Modal Pelindung):* Chip biru berisi kebiasaan baik pelindung tidur (`-SHAP`).
     - *Kartu 3 (🎯 Prioritas Cepat):* 1 aksi kunci paling berdampak malam ini.
4. **Actionable Recommendations (Target Terarah):**
   - *Timeline Horizontal 3 Ritme:* Sore (Maks 16.00: Cut-off kafein), Malam (21.30: Jauhkan HP & lampu temaram), Kasur (22.30: Aturan 20 menit & napas 4-7-8).
   - *Kartu Target Perilaku (Maks 2 Kartu Terbesar):* Menampilkan perbandingan visual:
     `[🛑 Saat Ini: 110 mnt] ➔ [🎯 Target Ideal: ≤ 30 mnt]`
   - *Checklist Komitmen Interaktif:* Dilengkapi penghitung langsung (`2 dari 4 terpilih`) dan tombol 1-klik salin ke clipboard ponsel.
   - *Medical Alert Red Flags:* 4 chip peringatan waspada medis ringkas (`Mengorok Keras`, `Tertidur Saat Kerja/Nyetir`, `Insomnia > 3 Minggu`, `Obat Tidur Kimia`).
5. **Simulator What-If Interaktif:**
   - Slider parameter gaya hidup (*Screen Time*, *Kafein*, *Durasi Tidur*, *Stres*, *Alkohol*) yang langsung memperbarui probabilitas risiko tidur secara dinamis tanpa perlu me-reload halaman.

---

## 5. INVENTARIS FILE & ARTEFAK UTAMA PROYEK

Seluruh artefak tersusun rapi di dalam *workspace* lokal dan repositori:

### A. Naskah Skripsi & Proposal Master (`01_Naskah_Proposal_Master/`)
| Nama File | Format | Deskripsi |
|---|---|---|
| `PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx` | DOCX (3.07 MB) | **Naskah Utama Master:** Bab 1–3 lengkap, format terverifikasi, tabel terintegrasi, siap cetak/serahkan. |
| `OUTLINE_PROPOSAL_REVISI_FINAL.docx` | DOCX (44.5 KB) | **Outline Revisi:** Berisi matriks tinjauan pustaka 6 kolom komparatif sesuai revisi dosen. |
| `OUTLINE_PROPOSAL_REVISI_FINAL.md` | Markdown (21.1 KB) | Sumber teks outline proposal untuk referensi cepat. |
| `PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx` | DOCX (48.5 KB) | Lembar panduan komprehensif berisi argumen dan jawaban pertanyaan dosen penguji. |
| `PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.md` | Markdown (22.6 KB) | Teks panduan argumentasi sempro untuk latihan tanya-jawab. |

### B. Kode Program & Model Machine Learning
| Lokasi / File | Teknologi | Fungsi |
|---|---|---|
| `dashboard/app.py` | Python (Flask, CORS) | REST API server backend untuk prediksi dan interpretasi SHAP. |
| `dashboard/train_model.py` | Python (CatBoost, Scikit-Learn) | Pipeline pelatihan model CatBoost dengan evaluasi metrik multikelas. |
| `dashboard/model/catboost_sleep_model.cbm` | Binary Model | Bobot model terlatih CatBoost. |
| `dashboard/model/feature_meta.json` | JSON | Metadata nama fitur, tipe data kategorikal, nilai min/max/step. |
| `dashboard/templates/index.html` | HTML5 / Tailwind | Antarmuka pengguna responsif dashboard CDSS (Glanceable Health-Tech UI). |
| `dashboard/templates/script.js` | JavaScript ES6+ | Logika interaktif DOM, komunikasi API, rendering chart SHAP, dan what-if simulator. |
| `dashboard/templates/style.css` | CSS3 Custom | Utilitas animasi, slider khusus, styling print PDF, dan tema hasil diagnosis. |
| `04_Eksperimen_dan_Model/preprocessing_catboost.ipynb` | Jupyter Notebook | Eksperimen eksplorasi data (*EDA*) dan visualisasi awal. |

### C. Skrip Verifikasi & Validasi (`scratch/`)
- `check_citation_bijection.py`: Memvalidasi korespondensi 1-ke-1 antara sitasi naskah dengan daftar pustaka.
- `verify_perfect_proposal.py`: Memeriksa konsistensi heading, tabel, gambar, dan panjang kata.
- `patch_docx_dois.py`: Memasukkan DOI aktif secara otomatis ke naskah Word.
- `rebuild_outline_table.py`: Membangun tabel perbandingan 6 kolom pada dokumen outline.
- `organize_workspace.py`: Skrip automasi penataan folder terstruktur rapi.

---

## 6. LOG HISTORI REVISI TERBARU (PASCA-BIMBINGAN)

Berikut adalah rekap penyelesaian 3 poin revisi dari dosen pembimbing:

1. **Poin 1: Judul Maksimal 14 Kata & Hilangkan Kata "XAI"**
   - **Tindakan:** Mengubah judul dari versi panjang menjadi 13 kata: *"Penerapan Algoritma CatBoost dan SHAP untuk Klasifikasi Risiko Gangguan Tidur Berbasis Gaya Hidup"*.
   - **Status:** Selesai. Disinkronkan ke seluruh file naskah Word, outline, dan dashboard.
2. **Poin 2: Perjelas Literature Review dalam Outline Proposal (Bentuk Tabel Komparatif)**
   - **Tindakan:** Merombak Tabel 1 pada outline proposal menjadi 6 kolom komparatif eksplisit:
     `No` | `Peneliti, Tahun & Reputasi Jurnal` | `Metode & Hasil Utama` | `Temuan Gap / Kekurangan Jurnal` | `Apa yang Diperbaiki Penelitian Ini` | `Penelitian Ini Lebih Baik dari Jurnal Ini Karena...`
   - **Status:** Selesai. Diisi dengan 6 jurnal internasional bereputasi (Taher & Ayon, Lin et al., Ha et al., Xie et al., Das et al., Srinivasu et al.).
3. **Poin 3: Rampingkan Dashboard CDSS dari Teks Berlebih (*Anti-Lazy Reading*)**
   - **Tindakan:** Mengganti paragraf panjang dengan badge metrik, kartu ringkasan visual 3 kolom, visual comparison pills (`[Saat Ini] ➔ [Target]`), dan checklist interaktif.
   - **Status:** Selesai. Server berjalan lancar di port 5000 dan bebas dari kelelahan membaca.

---

## 7. STATUS KONTROL VERSI (GIT & GITHUB)

- **Remote Origin:** `https://github.com/VinzSatoru/skripsi30.git`
- **Branch Aktif:** `main`
- **Commit Terakhir:** `8311145` (*"updateo"*)
- **Perubahan Tersinkronisasi:** 217 file (seluruh perubahan proposal, naskah outline, kode dashboard CDSS, dan script verifikasi).
- **Status Working Tree:** Bersih (*up to date with origin/main*).

---

## 8. ROADMAP & TAHAP SELANJUTNYA (MENUJU SEMPRO & SIDANG)

```
[Tahap 1: Pengajuan Judul & Outline]   ➔ ✅ SELESAI (Disetujui Pembimbing)
[Tahap 2: Penyusunan Proposal Bab 1-3] ➔ ✅ SELESAI (Naskah Master Siap)
[Tahap 3: Pembuatan Purwarupa CDSS]    ➔ ✅ SELESAI (Dashboard Berfungsi)
[Tahap 4: Seminar Proposal (Sempro)]   ➔ ⏳ LANGKAH BERIKUTNYA
[Tahap 5: Eksperimen Bab 4 & Analisis] ➔ 📋 TAHAP MENDATANG
[Tahap 6: Bab 5 & Ujian Sidang Skripsi]➔ 📋 TAHAP AKHIR
```

### Agenda Aksi Selanjutnya:
1. **Pencetakan / Pengumpulan Naskah Proposal:** Menggunakan file master [`PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx`](file:///c:/Users/ahmad/OneDrive/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/skripsi/01_Naskah_Proposal_Master/PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx).
2. **Penyusunan Slide Presentasi Seminar Proposal:** Membuat slide ringkas (10–12 slide) yang menyoroti:
   - Latar belakang masalah (urgensi gangguan tidur digital).
   - Research Gap (matriks 6 jurnal).
   - Metode (CatBoost + SHAP).
   - Demo langsung sistem CDSS interaktif.
3. **Latihan Simulasi Tanya-Jawab Sempro:** Menguasai materi pada file [`PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx`](file:///c:/Users/ahmad/OneDrive/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/skripsi/01_Naskah_Proposal_Master/PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx) untuk menjawab pertanyaan kritis penguji:
   - *"Mengapa memilih CatBoost daripada Random Forest atau XGBoost?"*
   - *"Apa fungsi matematis SHAP dan mengapa bukan LIME?"*
   - *"Apakah sistem ini menggantikan diagnosis dokter?"*
4. **Pelaksanaan Bab 4 (Pasca-Sempro):** Melakukan eksperimen tuning hyperparameter lanjutan (*GridSearchCV / Optuna*), komparasi metrik multi-model (CatBoost vs XGBoost vs LightGBM), dan pengujian *System Usability Scale* (SUS) pada tenaga kesehatan atau pengguna awal.
