import json

path = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\preprocessing_catboost.ipynb'

try:
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # 1. Update Cell 13: Calculate SHAP Values natively using CatBoost
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and ('import shap' in ''.join(cell['source']) or 'TreeExplainer' in ''.join(cell['source'])):
            cell['source'] = [
                "import shap\n",
                "from catboost import Pool\n",
                "\n",
                "# MENCEGAH KERNEL CRASH PADA CATBOOST + SHAP:\n",
                "# Kita tidak menggunakan shap.TreeExplainer karena library SHAP sering crash (segfault)\n",
                "# saat memproses fitur kategorikal. Sebaliknya, kita menggunakan fitur Native SHAP dari CatBoost.\n",
                "\n",
                "# 1. Ubah data testing menjadi CatBoost Pool\n",
                "X_test_sampled = X_test.sample(1000, random_state=42)\n",
                "pool_sampled = Pool(X_test_sampled, cat_features=cat_features)\n",
                "\n",
                "# 2. Dapatkan nilai SHAP langsung dari fungsi bawaan CatBoost\n",
                "# Output ini dijamin stabil dan menghasilkan array (jumlah_data, jumlah_kelas, jumlah_fitur + 1)\n",
                "shap_vals_catboost = model_catboost.get_feature_importance(pool_sampled, type='ShapValues')\n",
                "print(\"Berhasil menghitung SHAP secara native!\")"
            ]

    # 2. Update Cell 15: Summary Plot
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'shap.summary_plot' in ''.join(cell['source']):
            cell['source'] = [
                "# Cek urutan kelas dari CatBoost\n",
                "print(\"Urutan Kelas:\", model_catboost.classes_)\n",
                "\n",
                "# Dapatkan index untuk kelas 'Severe'\n",
                "severe_idx = list(model_catboost.classes_).index('Severe')\n",
                "\n",
                "# EKSTRAK DATA SHAP KHUSUS KELAS SEVERE\n",
                "# CatBoost mengembalikan (samples, classes, features + 1 bias)\n",
                "# Kita ambil semua baris (:), kelas severe, dan semua fitur kecuali kolom terakhir (:-1)\n",
                "shap_values_severe = shap_vals_catboost[:, severe_idx, :-1]\n",
                "\n",
                "# Menampilkan summary plot\n",
                "shap.summary_plot(shap_values_severe, X_test_sampled)\n"
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
                "# Ambil nilai expected_value (bias) yang terletak di kolom paling terakhir (-1)\n",
                "# Nilai ini sama untuk seluruh sampel, jadi kita ambil dari sampel ke-0 saja\n",
                "expected_value_severe = shap_vals_catboost[0, severe_idx, -1]\n",
                "\n",
                "# Generate visualisasi gaya dorong (Force Plot)\n",
                "shap.force_plot(\n",
                "    expected_value_severe, \n",
                "    shap_values_severe[pasien_ke, :], \n",
                "    data_pasien\n",
                ")\n"
            ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print('Notebook successfully rewritten to use Native CatBoost SHAP!')
except Exception as e:
    print('Error:', e)
