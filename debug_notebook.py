
# CELL 0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Memuat dataset
df = pd.read_csv('newdata/sleep_health_dataset.csv')
print(f'Dimensi dataset: {df.shape}')
print(df.head())

# CELL 1
# Cek Missing Values
print('Total Missing Values:', df.isnull().sum().sum())

# Cek Duplikasi Baris
print('Total Data Duplikat:', df.duplicated().sum())

# CELL 2
target_dist = df['sleep_disorder_risk'].value_counts()
target_percent = df['sleep_disorder_risk'].value_counts(normalize=True) * 100

dist_df = pd.DataFrame({'Jumlah': target_dist, 'Persentase (%)': target_percent})
print(dist_df)

# CELL 3
# Membuang kolom person_id
df_cleaned = df.drop(columns=['person_id'])

# Memisahkan X dan y
X = df_cleaned.drop(columns=['sleep_disorder_risk'])
y = df_cleaned['sleep_disorder_risk']
print(f'Jumlah Fitur (X): {X.shape[1]}')

# CELL 4
cat_features = X.select_dtypes(include=['object']).columns.tolist()
print('Daftar Fitur Kategorikal:')
print(cat_features)

# CELL 5
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f'Jumlah Data Training: {X_train.shape[0]} baris')
print(f'Jumlah Data Testing: {X_test.shape[0]} baris')

# CELL 6
from catboost import CatBoostClassifier

model_catboost = CatBoostClassifier(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    auto_class_weights='Balanced',
    cat_features=cat_features,
    random_seed=42,
    verbose=100
)

model_catboost.fit(
    X_train, y_train,
    eval_set=(X_test, y_test),
    early_stopping_rounds=50
)

# CELL 7
from sklearn.metrics import accuracy_score, classification_report

y_pred = model_catboost.predict(X_test)

akurasi = accuracy_score(y_test, y_pred)
print(f'Akurasi Model CatBoost: {akurasi * 100:.2f}%\n')

print('Laporan Klasifikasi:')
print(classification_report(y_test, y_pred))

# CELL 8
import shap
from catboost import Pool

# MENCEGAH KERNEL CRASH PADA CATBOOST + SHAP:
# Kita tidak menggunakan shap.TreeExplainer karena library SHAP sering crash (segfault)
# saat memproses fitur kategorikal. Sebaliknya, kita menggunakan fitur Native SHAP dari CatBoost.

# 1. Ubah data testing menjadi CatBoost Pool
X_test_sampled = X_test.sample(1000, random_state=42)
pool_sampled = Pool(X_test_sampled, cat_features=cat_features)

# 2. Dapatkan nilai SHAP langsung dari fungsi bawaan CatBoost
# Output ini dijamin stabil dan menghasilkan array (jumlah_data, jumlah_kelas, jumlah_fitur + 1)
shap_vals_catboost = model_catboost.get_feature_importance(pool_sampled, type='ShapValues')
print("Berhasil menghitung SHAP secara native!")

# CELL 9
# Cek urutan kelas dari CatBoost
print("Urutan Kelas:", model_catboost.classes_)

# Dapatkan index untuk kelas 'Severe'
severe_idx = list(model_catboost.classes_).index('Severe')

# EKSTRAK DATA SHAP KHUSUS KELAS SEVERE
# CatBoost mengembalikan (samples, classes, features + 1 bias)
# Kita ambil semua baris (:), kelas severe, dan semua fitur kecuali kolom terakhir (:-1)
shap_values_severe = shap_vals_catboost[:, severe_idx, :-1]

# Menampilkan summary plot
shap.summary_plot(shap_values_severe, X_test_sampled)


# CELL 10
# Inisialisasi Javascript agar plot interaktif bisa muncul di notebook
shap.initjs()

# Pilih satu pasien secara acak (contoh: baris ke-10 di X_test_sampled)
pasien_ke = 10
data_pasien = X_test_sampled.iloc[pasien_ke]

print(f"Penjelasan Prediksi untuk Pasien Baris ke-{pasien_ke}:")

# Ambil nilai expected_value (bias) yang terletak di kolom paling terakhir (-1)
# Nilai ini sama untuk seluruh sampel, jadi kita ambil dari sampel ke-0 saja
expected_value_severe = shap_vals_catboost[0, severe_idx, -1]

# Generate visualisasi gaya dorong (Force Plot)
shap.force_plot(
    expected_value_severe, 
    shap_values_severe[pasien_ke, :], 
    data_pasien
)

