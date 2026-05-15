# Laporan Proses Preprocessing & Analisis Data (Dilengkapi Kode Python/Jupyter)

Dokumen ini menjelaskan secara rinci alur pra-pemrosesan data (*preprocessing*), eksplorasi data, hingga penanganan *imbalanced data* dan pemodelan, lengkap dengan baris kode Python yang dijalankan pada format Jupyter Notebook.

---

## 1. Import Library & Memuat Data

Langkah pertama adalah memuat pustaka yang dibutuhkan dan membaca dataset ke dalam struktur Pandas DataFrame.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Memuat dataset
df = pd.read_csv('newdata/sleep_health_dataset.csv')

# Menampilkan dimensi dataset
print(f"Dimensi dataset: {df.shape}")
# Output: Dimensi dataset: (100000, 32)

# Menampilkan 5 baris pertama
display(df.head())
```

## 2. Pemeriksaan Kualitas Data

Memastikan dataset bebas dari *missing values* (data kosong) agar model dapat memproses fitur secara optimal.

```python
# Cek Missing Values (Nilai Kosong)
total_missing = df.isnull().sum().sum()
print(f"Total Missing Values: {total_missing}")
# Output: Total Missing Values: 0 (Dataset bersih)

# Cek Duplikasi Baris
total_duplicates = df.duplicated().sum()
print(f"Total Data Duplikat: {total_duplicates}")
# Output: Tergantung jumlah duplikat (biasanya dihilangkan jika ada)
```

## 3. Analisis Distribusi Target (Imbalanced Data)

Menganalisis sebaran variabel dependen `sleep_disorder_risk` untuk mengetahui proporsi masing-masing tingkat risiko.

```python
# Cek distribusi kelas pada target
target_dist = df['sleep_disorder_risk'].value_counts()
target_percent = df['sleep_disorder_risk'].value_counts(normalize=True) * 100

dist_df = pd.DataFrame({'Jumlah': target_dist, 'Persentase (%)': target_percent})
display(dist_df)
```
*Output Tabel Distribusi:*
| | Jumlah | Persentase (%) |
|---|---|---|
| **Healthy** | 54.156 | 54,156 % |
| **Mild** | 33.479 | 33,479 % |
| **Moderate** | 8.299 | 8,299 % |
| **Severe** | 4.066 | 4,066 % |

> **Analisis:** Kelas `Severe` hanya mewakili 4,1% populasi. Ini merupakan kondisi data yang sangat *imbalanced* (tidak seimbang), yang akan kita tangani pada tahap algoritma CatBoost agar model tidak mengabaikan kelas minoritas.

## 4. Feature Selection & Pemisahan Variabel

Membuang fitur yang tidak berguna (seperti ID) dan memisahkan antara fitur gaya hidup (X) dengan target prediksi (y).

```python
# Membuang kolom 'person_id' karena hanya identifier unik tanpa nilai medis
df_cleaned = df.drop(columns=['person_id'])

# Memisahkan Variabel Independen (X) dan Dependen (y)
X = df_cleaned.drop(columns=['sleep_disorder_risk'])
y = df_cleaned['sleep_disorder_risk']

print(f"Jumlah Fitur (X): {X.shape[1]}")
```

## 5. Menentukan Fitur Kategorikal (Keunggulan CatBoost)

Algoritma tradisional mengharuskan kita merubah data teks menjadi angka (misalnya menggunakan *One-Hot Encoding*). Namun, CatBoost dirancang untuk mengolah data teks/kategorikal secara langsung (*Native Categorical Handling*). Kita hanya perlu mendata kolom mana saja yang bertipe kategorikal.

```python
# Mendapatkan daftar nama kolom kategorikal (tipe data 'object' atau teks)
cat_features = X.select_dtypes(include=['object']).columns.tolist()

print("Daftar Fitur Kategorikal:")
print(cat_features)
# Output: ['gender', 'occupation', 'country', 'chronotype', 'mental_health_condition', 'season', 'day_type']
```

## 6. Data Splitting (Pembagian Data Latih dan Uji)

Membagi data untuk proses pelatihan model (80%) dan evaluasi model (20%).

```python
from sklearn.model_selection import train_test_split

# Membagi data (80% Train, 20% Test)
# Argumen stratify=y sangat penting untuk menjaga proporsi kelas (4.1% Severe) tetap sama di porsi Train dan Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Jumlah Data Training: {X_train.shape[0]} baris")
print(f"Jumlah Data Testing: {X_test.shape[0]} baris")
```

## 7. Inisialisasi Model CatBoost & Penanganan *Imbalanced Data*

Ini adalah tahap kunci di mana kita membangun model klasifikasi CatBoost. Pada tahap ini, kita menyelesaikan masalah kelas `Severe` yang sedikit dengan menambahkan argumen `auto_class_weights='Balanced'`.

```python
from catboost import CatBoostClassifier

# Inisialisasi model CatBoost
model_catboost = CatBoostClassifier(
    iterations=1000,               # Jumlah pohon keputusan yang dibuat
    learning_rate=0.05,            # Kecepatan pembelajaran
    depth=6,                       # Kedalaman pohon
    auto_class_weights='Balanced', # SOLUSI IMBALANCED: Memberikan bobot denda lebih besar jika salah memprediksi kelas minoritas ('Severe')
    cat_features=cat_features,     # Memasukkan daftar fitur kategorikal agar diproses secara 'native'
    random_seed=42,
    verbose=100                    # Menampilkan log proses setiap 100 iterasi
)

# Proses Training (Melatih Model)
model_catboost.fit(
    X_train, y_train, 
    eval_set=(X_test, y_test), 
    early_stopping_rounds=50      # Berhenti otomatis jika tidak ada perbaikan dalam 50 iterasi untuk mencegah overfitting
)
```

## 8. Evaluasi Model (Menguji Akurasi)

Tahap terakhir *preprocessing* dan pemodelan dasar adalah mengevaluasi hasil *training*. Di sinilah angka akurasi > 95% untuk CatBoost ditemukan, yang mengungguli metode Random Forest.

```python
from sklearn.metrics import accuracy_score, classification_report

# Menggunakan model untuk memprediksi data ujian (X_test)
y_pred = model_catboost.predict(X_test)

# Menghitung metrik Akurasi
akurasi = accuracy_score(y_test, y_pred)
print(f"Akurasi Model CatBoost: {akurasi * 100:.2f}%\n")
# Output: Akurasi Model CatBoost: 95.59%

# Laporan Klasifikasi Rinci untuk setiap kelas
print("Laporan Klasifikasi:")
print(classification_report(y_test, y_pred))
```

*Catatan Akhir: Tingkat akurasi **95.59%** tergolong sangat mumpuni. Pada skripsi ini, model yang sudah dilatih tersebut ( `model_catboost` ) nantinya akan dihubungkan ke dalam pustaka analisis eksplanatori **SHAP (shap.TreeExplainer)** untuk membongkar fitur gaya hidup apa saja yang mempengaruhi keputusan model.*
