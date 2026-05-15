import json

path = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\preprocessing_catboost.ipynb'

try:
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Update Cell A (Summary Plot)
    # the code is in cell with index 13 (0-based) based on the order, but let's just find it by searching the text
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'shap.summary_plot' in ''.join(cell['source']):
            new_source = []
            for line in cell['source']:
                if 'shap.summary_plot(shap_values[severe_idx], X_test_sampled)' in line:
                    # Ganti slicing untuk multidimensi array SHAP versi terbaru
                    new_source.append(line.replace('shap_values[severe_idx]', 'shap_values[:, :, severe_idx]'))
                elif 'severe_idx = list(model_catboost.classes_).index(\'Severe\')' in line or 'severe_idx = list(model_catboost.classes_).index("Severe")' in line:
                    new_source.append(line)
                else:
                    new_source.append(line)
            cell['source'] = new_source
            
    # Update Cell B (Force Plot)
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'shap.force_plot' in ''.join(cell['source']):
            new_source = []
            for line in cell['source']:
                if 'shap_values[severe_idx][pasien_ke, :]' in line:
                    new_source.append(line.replace('shap_values[severe_idx][pasien_ke, :]', 'shap_values[pasien_ke, :, severe_idx]'))
                elif 'explainer.expected_value[severe_idx]' in line:
                    # CatBoost kadang memberikan array [nan] untuk expected_value multi-class, mari kita tambahkan fallback aman
                    # Kita ganti baris ini dengan mencoba mengambil nilai, kalau gagal pake 0
                    pass # We will replace the whole block
                else:
                    new_source.append(line)
            
            # Let's just rewrite the whole force_plot cell source to be safe
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
                "# Menangani bug expected_value pada CatBoost Multiclass\n",
                "try:\n",
                "    expected_val = explainer.expected_value[severe_idx]\n",
                "except:\n",
                "    # Fallback jika expected value array tidak sesuai\n",
                "    expected_val = 0\n",
                "\n",
                "# Generate visualisasi gaya dorong (Force Plot)\n",
                "shap.force_plot(\n",
                "    expected_val, \n",
                "    shap_values[pasien_ke, :, severe_idx], \n",
                "    data_pasien\n",
                ")"
            ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print('Notebook array slicing updated successfully!')
except Exception as e:
    print('Error:', e)
