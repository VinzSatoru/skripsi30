# Skripsi: Penerapan Algoritma CatBoost dan SHAP untuk Klasifikasi Risiko Gangguan Tidur Berbasis Gaya Hidup

[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-CatBoost-0284c7.svg)](https://catboost.ai/)
[![Explainable AI](https://img.shields.io/badge/XAI-Tree--SHAP-6366f1.svg)](https://shap.readthedocs.io/)
[![CDSS Web](https://img.shields.io/badge/App-Flask%20%7C%20Tailwind%203.4-10b981.svg)](http://localhost:5000)
[![Repository Status](https://img.shields.io/badge/Status-Siap%20Sempro-success.svg)](https://github.com/VinzSatoru/skripsi30)

Repositori resmi penelitian Skripsi Program Studi S1 Teknik Informatika, Fakultas Sains dan Teknologi, Universitas Islam Nahdlatul Ulama (UNISNU) Jepara.

* **Peneliti:** Ahmad Novian Dzulfanni  
* **NIM:** 231240001438  
* **Tahun:** 2026  

---

## 🧭 Peta Struktur Folder Repositori (Terorganisir & Rapi)

Struktur folder telah dikelompokkan secara tematis agar mudah ditelusuri tanpa kebingungan:

```text
skripsi/
│
├── 📄 README.md                            # Panduan repositori & direktori navigasi
├── 📄 progress.md                          # Laporan komprehensif seluruh progress riset skripsi
│
├── 📁 01_Naskah_Proposal_Master/           # ⭐ BERKAS RESMI SIAP AJUKAN / CETAK
│   ├── PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx # Naskah Proposal Lengkap Bab 1–3 (Final Bebas Halusinasi)
│   ├── OUTLINE_PROPOSAL_REVISI_FINAL.docx   # Outline Proposal Resmi (Tabel Komparatif 6 Kolom)
│   ├── OUTLINE_PROPOSAL_REVISI_FINAL.md     # Versi Markdown dari Outline Proposal
│   ├── PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx # Lembar Argumen Sempro & Tanya Jawab Penguji
│   └── PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.md   # Teks panduan argumentasi sempro
│
├── 📁 02_Draft_Per_Bab/                    # Naskah mentah & revisi terpisah per bab
│   ├── 📁 Bab_1/
│   │   ├── BAB_1_Draft_Final.docx          # Dokumen draft Bab 1 Word
│   │   ├── BAB_1_Draft_Final.md            # Naskah Bab 1 Markdown (120-130 kata/paragraf)
│   │   └── Latar_Belakang_Revisi.md        # Catatan penyesuaian latar belakang
│   ├── 📁 Bab_2/
│   │   ├── BAB_2_Draft_Final.docx          # Dokumen draft Bab 2 Word
│   │   ├── BAB_2_Draft_Final.md            # Naskah Bab 2 Markdown (Landasan Teori & SOTA)
│   │   ├── BAB_2_Draft_Final_Revisi.docx   # Versi revisi draft Bab 2
│   │   └── SOTA_GAP.md                     # Rangkuman State of the Art & 5 Research GAP
│   └── 📁 Bab_3/
│       ├── BAB_3_Draft_Final.docx          # Dokumen draft Bab 3 Word
│       ├── BAB_3_Draft_Final.md            # Naskah Bab 3 Markdown (Metodologi CRISP-DM)
│       ├── BAB_3_Draft_Final_Revisi.docx   # Versi revisi draft Bab 3
│       ├── CRISP-DM.md                     # Catatan tahapan kerja CRISP-DM
│       └── Preprocessing.md                # Dokumentasi tahapan rekayasa fitur & data
│
├── 📁 03_Catatan_dan_Panduan_Sidang/        # Bank pertanyaan, panduan kampus, & suplemen
│   ├── pertanyaan.md                       # Kumpulan pertanyaan prediksi dosen penguji & jawaban
│   ├── penjelasan_apk.md                   # Panduan penjelasan teknis CDSS kepada penguji
│   ├── counter.md                          # Log audit penghitungan kata naskah
│   ├── k3027_panduan-skripsi.pdf           # Buku Pedoman Skripsi Fakultas Sains dan Teknologi UNISNU
│   └── skripsi_softfile_perpus.pdf         # Contoh skripsi acuan format perpustakaan
│
├── 📁 04_Eksperimen_dan_Model/             # Eksperimen Machine Learning & Kode Analisis
│   ├── preprocessing_catboost.ipynb        # Jupyter Notebook eksperimen CatBoost & Tree-SHAP
│   └── 📁 scripts_notebook/                # Script utilitas pembaruan & debugging notebook
│       ├── debug_notebook.py
│       ├── update_notebook.py
│       ├── update_notebook_native.py
│       ├── update_notebook_pool.py
│       └── update_notebook_safety.py
│
├── 📁 05_Arsip_dan_Backup/                 # Berkas arsip riwayat pengerjaan lama
│   ├── 📁 arsip_outline/                   # Arsip versi outline terdahulu (1438, revisi lama)
│   ├── 📁 arsip_bab1/                      # Arsip versi draft Bab 1 lama
│   └── 📁 arsip_proposal_temp/             # File Word sementara & backup otomatis
│
├── 📁 dashboard/                           # Purwarupa CDSS Web Application (Flask + Frontend)
│   ├── app.py                              # Backend API Flask (REST API localhost:5000)
│   ├── train_model.py                      # Skrip pelatihan ulang model CatBoost
│   ├── 📁 model/                           # Bobot model .cbm & metadata fitur .json
│   └── 📁 templates/                       # Antarmuka web modern (HTML, JS, CSS)
│
├── 📁 newdata/                             # Dataset Sleep Health and Lifestyle (100.000 sampel)
├── 📁 jurnal/                              # Kumpulan PDF artikel jurnal referensi bereputasi
├── 📁 gambar_bab3/                         # Diagram alur, visualisasi flowchart, dan grafik
├── 📁 scratch/                             # Skrip automasi internal, audit sitasi, & verifikasi naskah
└── 📁 catboost_info/                       # File log performa proses training CatBoost
```

---

## 🚀 Cara Menjalankan Purwarupa Dashboard CDSS

Purwarupa ini berfungsi sebagai instrumen skrining risiko gangguan tidur preventif dengan penjelasan transparansi SHAP secara *real-time*.

### 1. Masuk ke Direktori Dashboard
```powershell
cd dashboard
```

### 2. Jalankan Backend Server (Flask)
```powershell
python app.py
```

### 3. Buka pada Peramban (Browser)
Akses alamat lokal berikut:
```text
http://localhost:5000
```

> **Fitur Unggulan CDSS:**
> * ⚡ **Skrining 30 Detik:** Form 27 parameter gaya hidup terkelompok rapi.
> * 🎯 **CatBoost Engine:** Akurasi klasifikasi 93.86% – 95.18% pada 4 kelas risiko.
> * 🔍 **Transparansi Tree-SHAP:** 3-Card Glanceable Matrix (Pemicu Utama Beban, Modal Pelindung, dan Prioritas Cepat).
> * 💡 **Target Gaya Hidup Terukur:** Rekomendasi konkret *Sleep Hygiene* dengan *Visual Comparison Pills*.
> * 🎛️ **What-If Behavioral Simulator:** Uji dampak pergeseran kebiasaan terhadap penurunan risiko secara *live*.

---

## 🔬 Menjalankan Notebook Eksperimen

Untuk meninjau atau mereproduksi eksperimen pemodelan data:
```powershell
cd 04_Eksperimen_dan_Model
jupyter notebook preprocessing_catboost.ipynb
```

---

## 📌 Dokumen Utama yang Disiapkan untuk Pembimbing / Penguji

Ketika hendak bimbingan atau ujian Seminar Proposal (Sempro), berkas yang digunakan berada pada folder **`01_Naskah_Proposal_Master/`**:
1. [**`PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx`**](file:///c:/Users/ahmad/OneDrive/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/skripsi/01_Naskah_Proposal_Master/PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx) ➔ Naskah yang diserahkan/dicetak.
2. [**`OUTLINE_PROPOSAL_REVISI_FINAL.docx`**](file:///c:/Users/ahmad/OneDrive/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/skripsi/01_Naskah_Proposal_Master/OUTLINE_PROPOSAL_REVISI_FINAL.docx) ➔ Ringkasan matriks gap riset 6 kolom komparatif.
3. [**`PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx`**](file:///c:/Users/ahmad/OneDrive/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/skripsi/01_Naskah_Proposal_Master/PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx) ➔ Kisi-kisi jawaban argumentasi ujian.
4. [**`progress.md`**](file:///c:/Users/ahmad/OneDrive/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/skripsi/progress.md) ➔ Laporan lengkap status progress skripsi.
