"""
Script untuk melatih dan menyimpan model CatBoost ke file.
Jalankan script ini SEKALI sebelum menjalankan app.py.
"""

import pandas as pd
import numpy as np
import json
import os
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

print("=" * 60)
print("  TRAINING CATBOOST MODEL FOR SLEEP DISORDER DASHBOARD")
print("=" * 60)

# ── 1. LOAD DATASET ──────────────────────────────────────────
print("\n[1/5] Loading dataset...")
df = pd.read_csv('../newdata/sleep_health_dataset.csv')
print(f"  Dataset shape: {df.shape}")

# ── 2. PREPROCESSING ─────────────────────────────────────────
print("\n[2/5] Preprocessing...")

# Drop kolom ID, bias geografis, zero importance, dan fitur post-diagnosis yang bisa menyebabkan leakage
DROP_COLS = ['person_id', 'country', 'day_type', 'felt_rested', 'sleep_disorder_risk']
TARGET = 'sleep_disorder_risk'

X = df.drop(columns=DROP_COLS)
y = df[TARGET]

# Identifikasi fitur kategorikal
cat_features = X.select_dtypes(include=['object']).columns.tolist()
print(f"  Fitur total     : {X.shape[1]}")
print(f"  Fitur kategorikal: {len(cat_features)} -> {cat_features}")
print(f"  Distribusi kelas:\n{y.value_counts().to_string()}")

# ── 3. SPLIT DATA ────────────────────────────────────────────
print("\n[3/5] Splitting data (80/20 stratified)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"  Train: {X_train.shape[0]} baris | Test: {X_test.shape[0]} baris")

# ── 4. TRAIN MODEL ────────────────────────────────────────────
print("\n[4/5] Training CatBoost model...")
model = CatBoostClassifier(
    iterations=500,
    depth=6,
    learning_rate=0.05,
    auto_class_weights='Balanced',
    cat_features=cat_features,
    eval_metric='Accuracy',
    random_seed=42,
    verbose=100
)

train_pool = Pool(X_train, y_train, cat_features=cat_features)
test_pool  = Pool(X_test, y_test, cat_features=cat_features)

model.fit(train_pool, eval_set=test_pool, early_stopping_rounds=50)

# ── 5. EVALUATE & SAVE ────────────────────────────────────────
print("\n[5/5] Evaluating and saving model...")
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n  Akurasi: {acc:.4f} ({acc*100:.2f}%)")
print(f"\n  Classification Report:")
print(classification_report(y_test, y_pred))

# Buat folder model
os.makedirs('model', exist_ok=True)

# Simpan model CatBoost
model.save_model('model/catboost_sleep_model.cbm')
print("  Model tersimpan: model/catboost_sleep_model.cbm")

# Simpan metadata fitur
feature_meta = {
    'feature_names': X.columns.tolist(),
    'cat_features': cat_features,
    'classes': model.classes_.tolist(),
    'accuracy': float(acc),
    'feature_ranges': {}
}

# Simpan range & pilihan tiap fitur untuk form input
for col in X.columns:
    if col in cat_features:
        feature_meta['feature_ranges'][col] = {
            'type': 'categorical',
            'options': sorted(df[col].dropna().unique().tolist())
        }
    else:
        feature_meta['feature_ranges'][col] = {
            'type': 'numerical',
            'min': float(df[col].min()),
            'max': float(df[col].max()),
            'mean': float(df[col].mean()),
            'step': 1.0 if df[col].dtype == 'int64' else 0.1
        }

with open('model/feature_meta.json', 'w') as f:
    json.dump(feature_meta, f, indent=2)
print("  Metadata tersimpan: model/feature_meta.json")

print("\n" + "=" * 60)
print("  TRAINING SELESAI! Sekarang jalankan: python app.py")
print("=" * 60)
