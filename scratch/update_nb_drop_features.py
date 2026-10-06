import json

with open("preprocessing_catboost.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Cell 6 is markdown
nb['cells'][6]['source'] = [
    "# 4. Feature Selection & Pemisahan Variabel\n",
    "Membuang kolom `person_id` (identifier unik), `country` (bias geografis), dan `day_type` (zero importance), lalu memisahkan fitur independen (X) dan dependen (y)."
]

# Cell 7 is code
nb['cells'][7]['source'] = [
    "# Membuang kolom person_id, country, dan day_type\n",
    "df_cleaned = df.drop(columns=['person_id', 'country', 'day_type'])\n",
    "\n",
    "# Memisahkan X dan y\n",
    "X = df_cleaned.drop(columns=['sleep_disorder_risk'])\n",
    "y = df_cleaned['sleep_disorder_risk']\n",
    "print(f'Jumlah Fitur (X): {X.shape[1]}')"
]

with open("preprocessing_catboost.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully!")
