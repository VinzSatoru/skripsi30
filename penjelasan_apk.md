# Panduan Sidang: Implementasi CatBoost + SHAP pada Dashboard

Dokumen ini disusun sebagai panduan bagi Anda saat presentasi atau tanya jawab sidang skripsi, khususnya untuk menjelaskan bagaimana logika AI (CatBoost) dan XAI (SHAP) bekerja di dalam dashboard.

---

## Pertanyaan 1: "Bagaimana cara model Anda menangani data kuesioner yang berisi teks (kategorikal) tanpa melakukan *one-hot encoding*?"

**Jawaban:**
"Sistem ini menggunakan algoritma **CatBoost** (Categorical Boosting). Berbeda dengan XGBoost atau Random Forest yang mengharuskan kita mengubah teks menjadi angka secara manual (misalnya dengan *One-Hot Encoding*), CatBoost mampu menangani fitur berjenis kategori secara langsung (*native*). Hal ini diimplementasikan pada backend (`train_model.py` dan `app.py`) dengan cara mendefinisikan parameter `cat_features` saat inisialisasi dataset ke dalam objek `Pool`."

**Bukti Code (di `train_model.py`):**
```python
# Inisialisasi Model CatBoost
model = CatBoostClassifier(
    iterations=500,
    depth=6,
    learning_rate=0.05,
    auto_class_weights='Balanced',
    cat_features=cat_features, # <--- INI KUNCINYA
    eval_metric='Accuracy',
    random_seed=42
)

# Pembuatan Pool yang langsung menerima data teks
train_pool = Pool(X_train, y_train, cat_features=cat_features)
```

---

## Pertanyaan 2: "Setelah input disubmit di Web, bagaimana proses prediksinya berjalan?"

**Jawaban:**
"Ketika user menekan tombol prediksi, data form dikirim ke *backend* Python (`app.py`). Data tersebut disusun menjadi DataFrame pandas. Karena ini CatBoost, sistem langsung mengubahnya menjadi objek `Pool`. Kemudian model menjalankan fungsi `predict_proba()` untuk mendapatkan probabilitas (persentase) untuk setiap penyakit (Healthy, Insomnia, Sleep Apnea)."

**Bukti Code (di `app.py` baris 86-98):**
```python
# Buat CatBoost Pool dari input user (beserta definisi fitur kategorinya)
pool = Pool(input_df, cat_features=cat_features)

# Prediksi hasil (Class) dan Probabilitas (Persentase)
raw_pred = model.predict(pool)[0]
probabilities = model.predict_proba(pool)[0]

# Mapping hasil probabilitas ke nama kelas
prob_dict = {cls: float(prob) for cls, prob in zip(classes, probabilities)}
```

---

## Pertanyaan 3 (PERTANYAAN PALING PENTING): "Bagaimana cara kerja SHAP di dalam sistem Anda? Mengapa klasifikasi multikelas ini bisa dibuat menjadi interpretasi yang universal (Merah = Risiko, Hijau = Pelindung)?"

**Jawaban:**
"Inilah kontribusi teknis / keunggulan utama dari aplikasi ini. Secara *default*, SHAP pada multikelas akan menghasilkan *shap_values* yang berbeda-beda untuk setiap kelas prediksi, yang sangat membingungkan jika ditampilkan semua ke pasien. 

Untuk menyelesaikannya, saya membuat inovasi **Kalibrasi Basis Healthy (*Healthy Anchor Calibration*)**. Logikanya:
1. Sistem menghitung SHAP menggunakan fungsi `get_feature_importance` bawaan CatBoost.
2. Sistem secara spesifik hanya mengambil nilai SHAP untuk kelas **'Healthy' (Sehat)**.
3. Karena kelas *Healthy* adalah kondisi kebalikan dari Risiko (sakit), maka jika nilai SHAP *Healthy* **positif**, berarti fitur itu mendorong ke arah sehat. Jika **negatif**, mendorong ke arah sakit.
4. Agar UI di *frontend* mudah dipahami (Positif/Merah = Bahaya, Negatif/Hijau = Aman), saya **mengalikan nilai SHAP tersebut dengan -1** (*inverted*). Sehingga nilai akhirnya menjadi 'Risk Level SHAP'."

**Bukti Code (di `app.py` baris 100-115):**
```python
# 1. Ekstrak Nilai SHAP langsung dari CatBoost
shap_vals = model.get_feature_importance(pool, type='ShapValues', thread_count=1)

# 2. Cari indeks untuk kelas 'Healthy'
healthy_idx = list(classes).index('Healthy')

# 3 & 4. Inversi Nilai SHAP (Kalikan -1)
# Untuk UI, dinamakan "Risk Level SHAP"
# Nilai Positif (+) = Faktor Risiko (Meningkatkan Risiko Sakit)
# Nilai Negatif (-) = Faktor Pelindung (Menurunkan Risiko)
shap_for_pred = [-1 * val for val in shap_vals[0, healthy_idx, :-1]]
```

---

## Pertanyaan 4: "Bagaimana cara frontend menampilkan nilai SHAP tersebut?"

**Jawaban:**
"Nilai SHAP yang telah dikalibrasi (dikalikan -1) dikirim ke Javascript (`script.js`) dalam format JSON. Di Javascript, array tersebut di-*looping* dan divisualisasikan dalam bentuk batang (*bar*). Jika *value direction* nya 'positive', *bar* diberi warna merah (`bg-red-500`) yang mengindikasikan faktor tersebut harus dikurangi (intervensi). Jika 'negative', *bar* diberi warna hijau (`bg-green-500`) yang berarti kebiasaan tersebut sudah baik."

**Bukti Code (di `script.js` pada fungsi `renderSHAP`):**
```javascript
// Jika nilainya positif (Risiko), warnanya Merah
// Jika nilainya negatif (Pelindung), warnanya Hijau
const isPositive = item.direction === 'positive';
const colorClass = isPositive ? 'bg-red-500' : 'bg-emerald-500';

// Render HTML bar
bar.innerHTML = `
    <div class="h-full rounded ${colorClass}" style="width: ${width}%"></div>
`;
```

---

### Tips Tambahan Saat Sidang:
Jika penguji bertanya mengapa Anda repot-repot menggunakan SHAP dan mengalibrasinya, ingatkan mereka kembali pada **GAP Penelitian Anda (GAP 1)**: *"Model ML biasa hanya berbunyi alarm ('Anda berisiko!'), sedangkan sistem ini tidak hanya membunyikan alarm, tetapi juga memberi tahu letak kebakarannya ('Anda berisiko KARENA konsumsi kafein Anda 200mg!'). Itulah fungsi kode baris 115 di app.py."*
