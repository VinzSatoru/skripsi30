import json

path = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\preprocessing_catboost.ipynb'

try:
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Update Cell 7: Ensure CatBoost fit doesn't crash kernel with widgets
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'model_catboost.fit' in ''.join(cell['source']):
            new_source = []
            for line in cell['source']:
                if 'early_stopping_rounds=50' in line:
                    # Menambahkan plot=False untuk mencegah crash widget
                    new_source.append("    early_stopping_rounds=50,\n")
                    new_source.append("    plot=False # Mencegah Jupyter crash akibat widget CatBoost\n")
                else:
                    new_source.append(line)
            cell['source'] = new_source

    # Update Cell 9: Ensure SHAP feature importance uses 1 thread to avoid openmp crash
    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and 'get_feature_importance' in ''.join(cell['source']):
            new_source = []
            for line in cell['source']:
                if "type='ShapValues'" in line:
                    new_source.append(line.replace("type='ShapValues'", "type='ShapValues', thread_count=1"))
                else:
                    new_source.append(line)
            cell['source'] = new_source

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print('Notebook safety updates applied!')
except Exception as e:
    print('Error:', e)
