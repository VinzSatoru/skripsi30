"""
Flask Backend API untuk Sleep Disorder Risk Dashboard
Menggabungkan CatBoost (Prediksi) + SHAP (Penjelasan)
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from catboost import CatBoostClassifier, Pool
import pandas as pd
import numpy as np
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# ── LOAD MODEL & METADATA ────────────────────────────────────
print("[INFO] Loading CatBoost model...")
MODEL_PATH = 'model/catboost_sleep_model.cbm'
META_PATH  = 'model/feature_meta.json'

model = None
feature_meta = None

def load_model():
    global model, feature_meta
    if not os.path.exists(MODEL_PATH):
        print(f"[ERROR] Model tidak ditemukan di {MODEL_PATH}")
        print("[INFO] Jalankan train_model.py terlebih dahulu!")
        return False
    
    model = CatBoostClassifier()
    model.load_model(MODEL_PATH)
    
    with open(META_PATH, 'r') as f:
        feature_meta = json.load(f)
    
    print(f"[INFO] Model loaded! Akurasi training: {feature_meta['accuracy']*100:.2f}%")
    print(f"[INFO] Kelas: {feature_meta['classes']}")
    return True

model_loaded = load_model()

# ── ROUTES ───────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('templates', 'style.css')

@app.route('/script.js')
def script():
    return send_from_directory('templates', 'script.js')

@app.route('/api/meta')
def get_meta():
    """Mengembalikan metadata fitur untuk membangun form input"""
    if not model_loaded:
        return jsonify({'error': 'Model belum dilatih. Jalankan train_model.py dulu!'}), 500
    return jsonify(feature_meta)

@app.route('/api/predict', methods=['POST'])
def predict():
    """Prediksi risiko gangguan tidur + penjelasan SHAP"""
    if not model_loaded:
        return jsonify({'error': 'Model belum dilatih!'}), 500
    
    try:
        # Ambil data dari request
        data = request.json
        
        # Buat DataFrame dengan urutan kolom yang benar
        feature_names = feature_meta['feature_names']
        cat_features   = feature_meta['cat_features']
        
        input_df = pd.DataFrame([{col: data.get(col) for col in feature_names}])
        
        # Konversi tipe data numerik
        for col in feature_names:
            if col not in cat_features:
                input_df[col] = pd.to_numeric(input_df[col], errors='coerce')
        
        # Buat CatBoost Pool
        pool = Pool(input_df, cat_features=cat_features)
        
        # ── Prediksi ──────────────────────────────────────────
        raw_pred = model.predict(pool)[0]
        if isinstance(raw_pred, (np.ndarray, list)) and len(raw_pred) == 1:
            prediction = str(raw_pred[0])
        else:
            prediction = str(raw_pred)
        probabilities = model.predict_proba(pool)[0]
        classes = feature_meta['classes']
        
        prob_dict = {cls: float(prob) for cls, prob in zip(classes, probabilities)}
        
        # ── SHAP Values (Native CatBoost) ────────────────────
        shap_vals = model.get_feature_importance(pool, type='ShapValues', thread_count=1)
        # shap_vals shape: (1, n_classes, n_features + 1)
        
        # Ekstrak indeks untuk kelas 'Healthy' sebagai baseline universal
        healthy_idx = list(classes).index('Healthy')
        
        # Kita ambil SHAP dari kelas Healthy.
        # Karena kelas Healthy = 0 (Tidak Berisiko), maka:
        # SHAP Healthy Positif = Mendorong ke arah Sehat
        # SHAP Healthy Negatif = Menarik dari Sehat (Mendorong ke arah Risiko)
        #
        # Untuk UI, kita akan KALIKAN dengan -1, sehingga dinamakan "Risk Level SHAP"
        # Nilai Positif (+) = Faktor Risiko (Meningkatkan Risiko)
        # Nilai Negatif (-) = Faktor Pelindung (Menurunkan Risiko)
        shap_for_pred = [-1 * val for val in shap_vals[0, healthy_idx, :-1]]
        
        # Buat daftar kontribusi fitur yang diurutkan
        shap_contributions = []
        for fname, sval in zip(feature_names, shap_for_pred):
            raw_val = input_df[fname].iloc[0]
            val_clean = str(raw_val) if fname in cat_features else float(raw_val)
            shap_contributions.append({
                'feature': fname,
                'value': val_clean,
                'shap': float(sval),
                'direction': 'positive' if sval > 0 else 'negative'
            })
        
        # Urutkan dari yang paling berpengaruh (absolut)
        shap_contributions.sort(key=lambda x: abs(x['shap']), reverse=True)
        
        # Ambil top 10 yang paling berpengaruh
        top_shap = shap_contributions[:10]
        
        return jsonify({
            'success': True,
            'prediction': str(prediction),
            'probabilities': prob_dict,
            'shap_top10': top_shap,
            'model_accuracy': feature_meta['accuracy']
        })
    
    except Exception as e:
        import traceback
        return jsonify({
            'success': False,
            'error': str(e),
            'trace': traceback.format_exc()
        }), 500

@app.route('/api/sample')
def get_sample():
    """Mengembalikan data sampel dari dataset"""
    try:
        df = pd.read_csv('../newdata/sleep_health_dataset.csv')
        sample = df.sample(1, random_state=np.random.randint(0, 999)).iloc[0]
        feature_names = feature_meta['feature_names']
        sample_data = {col: str(sample[col]) if col in feature_meta['cat_features'] 
                      else float(sample[col]) for col in feature_names}
        return jsonify(sample_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("  Sleep Disorder Risk Dashboard - Backend")
    print("  Buka browser: http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
