import json

path = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\preprocessing_catboost.ipynb'

try:
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # 1. Update Cell 13: Calculate SHAP Values using Pool
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'import shap' in ''.join(cell['source']):
            cell['source'] = [
                "import shap\n",
                "from catboost import Pool\n",
                "\n",
                "# 1. Membangun Explainer menggunakan model yang sudah dilatih\n",
                "explainer = shap.TreeExplainer(model_catboost)\n",
                "\n",
                "# 2. Menghitung SHAP values untuk data testing\n",
                "X_test_sampled = X_test.sample(1000, random_state=42)\n",
                "\n",
                "# MENCEGAH KERNEL CRASH: Kita harus mengubah data pandas menjadi CatBoost Pool\n",
                "# karena dataset kita mengandung fitur kategorikal (teks)\n",
                "pool_sampled = Pool(X_test_sampled, cat_features=cat_features)\n",
                "\n",
                "# Menghitung shap values dari objek pool\n",
                "shap_values = explainer.shap_values(pool_sampled)\n"
            ]

    # 2. Update Cell 15: Summary Plot
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'shap.summary_plot' in ''.join(cell['source']):
            cell['source'] = [
                "# Cek urutan kelas dari CatBoost\n",
                "print(\"Urutan Kelas:\", model_catboost.classes_)\n",
                "\n",
                "# Mendapatkan index array untuk kelas 'Severe'\n",
                "severe_idx = list(model_catboost.classes_).index('Severe')\n",
                "\n",
                "# Menampilkan summary plot khusus untuk mendeteksi risiko 'Severe'\n",
                "# Gunakan slicing [:, :, severe_idx] untuk versi SHAP & CatBoost terbaru\n",
                "shap.summary_plot(shap_values[:, :, severe_idx], X_test_sampled)\n"
            ]

    # 3. Update Cell 17: Force Plot
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'shap.force_plot' in ''.join(cell['source']):
            cell['source'] = [
                "# Inisialisasi Javascript agar plot interaktif bisa muncul di notebook\n",
                "shap.initjs()\n",
                "\n",
                "# Pilih satu pasien secara acak (contoh: baris ke-10 di X_test_sampled)\n",
                "pasien_ke = 10\n",
                "data_pasien = X_test_sampled.iloc[pasien_ke]\n",
                "\n",
                "print(f\"Penjelasan Prediksi untuk Pasien Baris ke-{pasien_ke}:\")\n",
                "\n",
                "# Menangani nilai expected_value untuk Force Plot\n",
                "try:\n",
                "    expected_val = explainer.expected_value[severe_idx]\n",
                "except:\n",
                "    expected_val = 0 # Fallback aman\n",
                "\n",
                "# Generate visualisasi gaya dorong (Force Plot)\n",
                "shap.force_plot(\n",
                "    expected_val, \n",
                "    shap_values[pasien_ke, :, severe_idx], \n",
                "    data_pasien\n",
                ")\n"
            ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print('Notebook updated successfully to prevent kernel crash!')
except Exception as e:
    print('Error:', e)
