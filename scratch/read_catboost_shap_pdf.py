import fitz
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

fpath = r'c:\Users\ahmad\OneDrive\ドキュメント\skripsi\jurnal\Jurnal tambahan BAB 3\Explainable Semi-Supervised Learning Framework for Alzheimer’s Disease Prediction Using SHAP-Based Feature Selection and Cost-Sensitive CatBoost.pdf'
doc = fitz.open(fpath)
print(doc[0].get_text())
