# 🛡️ Panduan Defense Sidang Skripsi: SleepRisk XAI

Dokumen ini berisi rangkuman argumen, penjelasan teknis, dan strategi *counter* (jawaban pertahanan) untuk menghadapi pertanyaan kritis dari dosen penguji saat sidang skripsi terkait model CatBoost dan metode Explainable AI (SHAP).

---

## 1. Fokus Utama Penelitian (Jika Ditanya Tujuan)

**Pertanyaan:** *"Apa tujuan sebenarnya dari skripsi ini? Apakah kamu mau membuktikan kebenaran medis dari gangguan tidur?"*

**Jawaban / Counter:**
> "Fokus utama dari skripsi ini **bukanlah** di ranah Ilmu Kedokteran (menciptakan standar diagnosis baru), melainkan di ranah **Teknologi Informasi / Ilmu Komputer**. Penelitian ini memiliki 3 pilar utama:
> 1. **Algoritma:** Menguji keandalan CatBoost dalam mengklasifikasi data campuran (numerik & kategorikal) dengan akurasi tinggi (94.58%).
> 2. **Metode (XAI):** Menerapkan metode *Explainable AI* (SHAP) untuk membuka 'Black-Box' Machine Learning agar keputusannya menjadi transparan.
> 3. **Sistem:** Mengintegrasikan model dan metode tersebut ke dalam sebuah arsitektur Sistem Pendukung Keputusan (*Web Dashboard*) yang real-time dan interaktif.
> 
> Sistem ini adalah cerminan dari dataset yang diberikan. Jika di masa depan diberikan rekam medis asli rumah sakit, arsitektur *software* yang saya bangun ini sudah terbukti siap beroperasi."

---

## 2. Penjelasan Metode SHAP pada CatBoost

**Pertanyaan:** *"Jelaskan secara singkat, bagaimana metode SHAP diterapkan pada algoritma CatBoost?"*

**Jawaban Singkat (Hafalan 1 Kalimat):**
> "CatBoost menerapkan metode **TreeSHAP** berbasis teori permainan koalisi untuk mengukur kontribusi marginal setiap fitur secara aditif dan eksak terhadap perubahan hasil prediksi model dari nilai rata-ratanya."

**Penjelasan 3 Poin Utama (Jika diminta lebih detail):**
1. **TreeSHAP:** CatBoost tidak menggunakan SHAP biasa yang menebak-nebak, melainkan *TreeSHAP* yang menelusuri langsung cabang pohon keputusan secara matematis sehingga hasilnya **100% eksak dan sangat cepat**.
2. **Game Theory:** SHAP meminjam konsep ekonomi (*Shapley Values*) untuk membagi "hadiah" (probabilitas prediksi) secara adil kepada setiap "pemain" (fitur gaya hidup) berdasarkan seberapa besar peran mereka.
3. **Sifat Aditif:** Jika semua nilai SHAP setiap fitur dijumlahkan dengan rata-rata risiko (*Base Value*), hasilnya pasti **sama persis** dengan probabilitas akhir yang dikeluarkan model.

---

## 3. Logika "Risk Level SHAP" (Kasus Kondisi Mental: Sehat vs Depresi)

**Pertanyaan:** *"Kenapa di model kamu, kondisi mental yang 'Healthy' selalu disebut faktor pelindung, padahal bisa saja orang sehat mental tetap kena gangguan tidur parah karena hal lain?"*

**Jawaban / Counter:**
> "Di dalam arsitektur *backend* sistem ini, saya menerapkan teknik **Anchor Calibration** pada algoritma SHAP. Daripada menjelaskan mengapa model memilih kelas spesifik (yang seringkali membingungkan manusia secara logika), sistem saya mengunci jangkar perhitungan SHAP selalu terhadap kelas **'Healthy' (Sehat)**.
>
> Sistem secara matematis menghitung jarak (*distance*) fitur pasien terhadap titik dasar orang sehat. Oleh karena itu, atribut yang baik (seperti mental yang sehat) akan selalu terekam menarik pasien mendekati Sehat (bernilai negatif/pelindung), sedangkan atribut buruk (seperti Depresi) akan selalu terekam mendorong pasien menjauhi Sehat (bernilai positif/risiko), tidak peduli apa pun hasil prediksi akhir sistemnya. Hal ini membuat User Experience (UX) menjadi 100% selaras dengan nalar logika manusia."

---

## 4. Celah Penelitian & Cara Mengatasinya (Loophole Defense)

Jika dosen menyerang kelemahan / celah sistem, gunakan argumen berikut:

### A. Korelasi vs Kausalitas
* **Serangan:** *"Apakah SHAP membuktikan bahwa alkohol yang tinggi PASTI menyebabkan gangguan tidur?"*
* **Counter:** *"Tidak. SHAP hanya menjelaskan pola korelasi statistik yang dipelajari model dari data historis (*post-hoc explanation*), bukan hubungan sebab-akibat (kausalitas) biologis. Sistem ini berfungsi sebagai pendukung keputusan klinis untuk memberi 'petunjuk' kepada dokter, bukan alat vonis mandiri."*

### B. Masalah Tumpang Tindih Fitur (Multikolinearitas)
* **Serangan:** *"Durasi tidur dan kualitas tidur itu saling berhubungan erat. Apakah tidak bias?"*
* **Counter:** *"CatBoost menggunakan struktur pohon keputusan (*oblivious trees*) yang sangat tangguh terhadap fitur yang saling tumpang tindih. Selain itu, algoritma **TreeSHAP** menghitung kontribusi berdasarkan jalur percabangan bersyarat, bukan mengasumsikan fitur-fitur tersebut sepenuhnya independen, sehingga bias multikolinearitas dapat ditekan seminimal mungkin."*

### C. Keaslian Dataset (Generalization Gap)
* **Serangan:** *"Dataset kamu bukan data riil pasien rumah sakit lokal, apakah bisa diandalkan?"*
* **Counter:** *"Fokus skripsi ini adalah membuktikan kelayakan metodologi (Methodological Feasibility). Model dapat dengan mudah dilatih ulang (*retrained*) dengan data lokal di masa depan, dan arsitektur dashboard AI yang saya kembangkan ini akan tetap berfungsi secara sempurna untuk mengekstrak penjelasannya."*

### D. Belum Divalidasi oleh Dokter Ahli
* **Serangan:** *"Kamu mengklaim visualisasi ini mudah dipahami, tapi apakah kamu sudah mengujinya ke dokter?"*
* **Counter:** *"Evaluasi tingkat kejelasan (*Interpretability Evaluation*) oleh pakar medis secara kuantitatif berada di luar batasan skripsi ini. Namun, hal ini sudah saya rumuskan di Bab 5 sebagai **Saran Penelitian Selanjutnya**, di mana sistem ini perlu diuji menggunakan metode *System Usability Scale (SUS)* kepada dokter spesialis tidur."*
