import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

OUT_DIR = r"c:\Users\ahmad\OneDrive\ドキュメント\skripsi\gambar_bab3"
os.makedirs(OUT_DIR, exist_ok=True)

# Set global matplotlib style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 1.0

# ==============================================================================
# 1. GAMBAR 3.1: KERANGKA KERJA CRISP-DM
# ==============================================================================
def create_crisp_dm_figure():
    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # Title header
    fig.text(0.5, 0.965, "KERANGKA KERJA CRISP-DM PENELITIAN GANGGUAN TIDUR", 
             ha='center', va='center', fontsize=15, fontweight='bold', color='#0F172A')
    fig.text(0.5, 0.935, "Klasifikasi Risiko Multi-Kelas Menggunakan CatBoost dan Interpretasi Fitur XAI Tree-SHAP", 
             ha='center', va='center', fontsize=11, color='#475569')

    phases = [
        {
            "num": "1",
            "title": "Business Understanding",
            "x": 0.8, "y": 5.4, "w": 4.1, "h": 3.4,
            "border": "#2563EB", "fill": "#F8FAFC", "header_bg": "#1E40AF",
            "items": [
                "• Identifikasi masalah prevalensi gangguan tidur",
                "• Perumusan 4 tingkat risiko: Healthy, Mild,",
                "  Moderate, dan Severe",
                "• Kebutuhan interpretabilitas klinis (XAI)",
                "• Perancangan luaran prototipe Web CDSS"
            ]
        },
        {
            "num": "2",
            "title": "Data Understanding",
            "x": 5.45, "y": 5.4, "w": 4.1, "h": 3.4,
            "border": "#0284C7", "fill": "#F8FAFC", "header_bg": "#0369A1",
            "items": [
                "• Eksplorasi 100.000 rekaman & 32 atribut awal",
                "• Pemeriksaan kualitas (0 missing values, 0 dup)",
                "• Analisis statistik deskriptif & sebaran data",
                "• Identifikasi kelas imbalanced berat",
                "  (Severe hanya 4,066% populasi)"
            ]
        },
        {
            "num": "3",
            "title": "Data Preparation",
            "x": 10.1, "y": 5.4, "w": 4.1, "h": 3.4,
            "border": "#0D9488", "fill": "#F8FAFC", "header_bg": "#0F766E",
            "items": [
                "• Eliminasi identifier person_id",
                "• Eliminasi day_type (importance nol) &",
                "  country (mencegah bias geografis)",
                "• Registrasi 5 Fitur Kategorikal Native CatBoost",
                "• Stratified Train-Test Split (80% : 20%)"
            ]
        },
        {
            "num": "4",
            "title": "Modeling",
            "x": 10.1, "y": 1.0, "w": 4.1, "h": 3.4,
            "border": "#6366F1", "fill": "#F8FAFC", "header_bg": "#4338CA",
            "items": [
                "• Pelatihan CatBoost Classifier",
                "• Arsitektur Symmetric Oblivious Trees (depth=6)",
                "• Cost-Sensitive auto_class_weights='Balanced'",
                "• Konfigurasi 1000 iterasi & learning rate 0,05",
                "• Integrasi modul komputasi SHAP TreeExplainer"
            ]
        },
        {
            "num": "5",
            "title": "Evaluation",
            "x": 5.45, "y": 1.0, "w": 4.1, "h": 3.4,
            "border": "#D97706", "fill": "#F8FAFC", "header_bg": "#B45309",
            "items": [
                "• Evaluasi metrik uji pada 20.000 data sampel",
                "• Accuracy, Precision, Recall, Macro-F1 Score",
                "• Analisis Multi-Class Confusion Matrix (4x4)",
                "• Evaluasi validasi global (Summary Beeswarm)",
                "• Evaluasi eksplanasi lokal (Waterfall Plot)"
            ]
        },
        {
            "num": "6",
            "title": "Deployment",
            "x": 0.8, "y": 1.0, "w": 4.1, "h": 3.4,
            "border": "#059669", "fill": "#F8FAFC", "header_bg": "#047857",
            "items": [
                "• Rancang bangun prototipe Web CDSS interaktif",
                "• Antarmuka pengguna responsif (Tailwind CSS)",
                "• Modul prediksi risiko & probabilitas real-time",
                "• Visualisasi kontribusi atribut via grafik SHAP",
                "• Personalisasi rekomendasi sleep hygiene"
            ]
        }
    ]

    for p in phases:
        shadow = patches.FancyBboxPatch((p["x"]+0.04, p["y"]-0.04), p["w"], p["h"],
                                        boxstyle="round,pad=0,rounding_size=0.15",
                                        facecolor="#E2E8F0", edgecolor="none", zorder=1)
        ax.add_patch(shadow)

        box = patches.FancyBboxPatch((p["x"], p["y"]), p["w"], p["h"],
                                    boxstyle="round,pad=0,rounding_size=0.15",
                                    facecolor=p["fill"], edgecolor=p["border"], linewidth=1.8, zorder=2)
        ax.add_patch(box)

        header_h = 0.75
        header_box = patches.FancyBboxPatch((p["x"], p["y"] + p["h"] - header_h), p["w"], header_h,
                                           boxstyle="round,pad=0,rounding_size=0.15",
                                           facecolor=p["header_bg"], edgecolor=p["border"], linewidth=1.5, zorder=3)
        ax.add_patch(header_box)

        circ = plt.Circle((p["x"] + 0.45, p["y"] + p["h"] - header_h/2), 0.24,
                          facecolor='#FFFFFF', edgecolor='none', zorder=4)
        ax.add_patch(circ)
        ax.text(p["x"] + 0.45, p["y"] + p["h"] - header_h/2, p["num"],
                ha='center', va='center', fontsize=11, fontweight='bold', color=p["header_bg"], zorder=5)

        ax.text(p["x"] + 0.85, p["y"] + p["h"] - header_h/2, f"Fase {p['num']}: {p['title']}",
                ha='left', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF', zorder=5)

        item_y = p["y"] + p["h"] - header_h - 0.35
        for item in p["items"]:
            ax.text(p["x"] + 0.25, item_y, item,
                    ha='left', va='top', fontsize=9.2, color='#1E293B', zorder=5)
            item_y -= 0.45

    # Connectors
    ax.annotate("", xy=(5.4, 7.1), xytext=(4.95, 7.1),
                arrowprops=dict(arrowstyle="-|>", color="#2563EB", lw=2.5, mutation_scale=18))
    ax.annotate("", xy=(10.05, 7.1), xytext=(9.6, 7.1),
                arrowprops=dict(arrowstyle="-|>", color="#0284C7", lw=2.5, mutation_scale=18))
    ax.annotate("", xy=(12.15, 4.45), xytext=(12.15, 5.35),
                arrowprops=dict(arrowstyle="-|>", color="#0D9488", lw=2.5, mutation_scale=18))
    ax.annotate("", xy=(9.6, 2.7), xytext=(10.05, 2.7),
                arrowprops=dict(arrowstyle="-|>", color="#6366F1", lw=2.5, mutation_scale=18))
    ax.annotate("", xy=(4.95, 2.7), xytext=(5.4, 2.7),
                arrowprops=dict(arrowstyle="-|>", color="#D97706", lw=2.5, mutation_scale=18))

    # Feedback Loops
    ax.annotate("", xy=(10.05, 3.4), xytext=(9.6, 3.4),
                arrowprops=dict(arrowstyle="-|>", color="#DC2626", lw=1.8, linestyle="--", mutation_scale=15))
    ax.text(9.82, 3.65, "Tuning Ulang", ha='center', va='bottom', fontsize=8.5, color="#DC2626", fontweight='bold')

    ax.plot([7.5, 7.5, 2.85, 2.85], [0.95, 0.45, 0.45, 0.95], color="#B45309", lw=1.6, linestyle=":")
    ax.annotate("", xy=(2.85, 0.95), xytext=(2.85, 0.7),
                arrowprops=dict(arrowstyle="-|>", color="#B45309", lw=1.6, linestyle=":", mutation_scale=14))
    ax.text(5.17, 0.25, "Siklus Iteratif: Penyelarasan Hasil Evaluasi dengan Kebutuhan Klinis", 
            ha='center', va='center', fontsize=8.5, color="#B45309", fontstyle='italic')

    plt.tight_layout()
    save_path = os.path.join(OUT_DIR, "Gambar_3_1_CRISP_DM.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {save_path}")


# ==============================================================================
# 2. GAMBAR 3.2: ALUR KOMPUTASI DAN INTERPRETASI XAI TREE-SHAP
# ==============================================================================
def create_shap_flowchart():
    fig, ax = plt.subplots(figsize=(15, 9), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9)
    ax.axis('off')

    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # Title
    fig.text(0.5, 0.96, "ALUR KOMPUTASI DAN INTERPRETASI XAI TREE-SHAP", 
             ha='center', va='center', fontsize=15, fontweight='bold', color='#0F172A')
    fig.text(0.5, 0.925, "Mekanisme Dekomposisi Nilai Shapley untuk Model Ensemble Pohon Simetris CatBoost", 
             ha='center', va='center', fontsize=11, color='#475569')

    # Function to draw card
    def draw_card(x, y, w, h, title, items, border_col, header_col, bg_col="#F8FAFC", title_size=10):
        shadow = patches.FancyBboxPatch((x+0.03, y-0.03), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor="#E2E8F0", edgecolor="none", zorder=1)
        ax.add_patch(shadow)
        card = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                     facecolor=bg_col, edgecolor=border_col, linewidth=1.6, zorder=2)
        ax.add_patch(card)
        
        hh = 0.65
        h_box = patches.FancyBboxPatch((x, y + h - hh), w, hh, boxstyle="round,pad=0,rounding_size=0.12",
                                       facecolor=header_col, edgecolor=border_col, linewidth=1.2, zorder=3)
        ax.add_patch(h_box)
        
        ax.text(x + w/2, y + h - hh/2, title, ha='center', va='center', fontsize=title_size,
                fontweight='bold', color='#FFFFFF', zorder=4)
        
        cur_y = y + h - hh - 0.28
        for it in items:
            ax.text(x + 0.2, cur_y, it, ha='left', va='top', fontsize=8.8, color='#1E293B', zorder=4)
            cur_y -= 0.38

    # 1. Inputs (Left)
    draw_card(0.6, 5.2, 3.4, 2.8, "Model CatBoost Terlatih", [
        "• Algoritma Gradient Boosting",
        "• Symmetric Oblivious Trees",
        "• Native Categorical Encoded",
        "• Fungsi Kerugian MultiClass",
        "• auto_class_weights='Balanced'"
    ], "#3B82F6", "#1D4ED8")

    draw_card(0.6, 1.2, 3.4, 2.8, "Matriks Data Uji (X_test)", [
        "• 20.000 Sampel Independen",
        "• 28 Fitur Prediktor Terpilih",
        "• Parameter Gaya Hidup Digital",
        "• Indikator Fisiologis & Medis",
        "• Stratified Target Distribution"
    ], "#0284C7", "#0369A1")

    # 2. Core SHAP Engine (Center)
    draw_card(4.7, 2.5, 4.4, 4.2, "SHAP TreeExplainer Engine", [
        "• Pustaka SHAP (Lundberg et al., 2020)",
        "• Komputasi Nilai Shapley Eksak",
        "• Kompleksitas Waktu Polinomial: O(TLD²)",
        "• Properti Aditif Matematis:",
        "    f(x) = φ₀ + Σ φᵢ  (Aksioma Efisiensi)",
        "• Keadilan Teori Permainan Kooperatif:",
        "  - Efisiensi, Simetri, Dummy, Aditivitas",
        "• Dekomposisi Margin Logit Multi-Kelas"
    ], "#0D9488", "#0F766E")

    # 3. Outputs (Right): Global & Local
    draw_card(9.8, 4.9, 4.6, 3.1, "Tingkat Global (Populasi)", [
        "• SHAP Summary Beeswarm Plot:",
        "  - Distribusi pengaruh nilai fitur tinggi vs rendah",
        "  - Arah korelasi terhadap setiap tingkat risiko",
        "• Global Feature Importance Bar Plot:",
        "  - Ranking kontribusi absolut rata-rata: mean(|φ|)",
        "  - Identifikasi faktor risiko gaya hidup dominan"
    ], "#D97706", "#B45309")

    draw_card(9.8, 1.1, 4.6, 3.1, "Tingkat Lokal (Individu Pasien)", [
        "• SHAP Individual Waterfall Plot:",
        "  - Kontribusi marginal setiap fitur per pasien",
        "  - Base Value E[f(x)] menuju skor prediksi f(x)",
        "• SHAP Force Plot:",
        "  - Gaya dorong (merah) vs penahan (biru) risiko",
        "• Transparansi alasan diagnostik klinis"
    ], "#6366F1", "#4338CA")

    # Connecting Arrows
    # Input 1 -> TreeExplainer
    ax.annotate("", xy=(4.65, 5.8), xytext=(4.05, 6.2),
                arrowprops=dict(arrowstyle="-|>", color="#1D4ED8", lw=2.2, mutation_scale=16))
    # Input 2 -> TreeExplainer
    ax.annotate("", xy=(4.65, 3.8), xytext=(4.05, 3.2),
                arrowprops=dict(arrowstyle="-|>", color="#0369A1", lw=2.2, mutation_scale=16))

    # TreeExplainer -> Global
    ax.annotate("", xy=(9.75, 6.2), xytext=(9.15, 5.2),
                arrowprops=dict(arrowstyle="-|>", color="#B45309", lw=2.2, mutation_scale=16))
    ax.text(9.3, 5.9, "Agregasi\nGlobal", ha='center', va='center', fontsize=8.5, color='#B45309', fontweight='bold')

    # TreeExplainer -> Local
    ax.annotate("", xy=(9.75, 2.7), xytext=(9.15, 3.8),
                arrowprops=dict(arrowstyle="-|>", color="#4338CA", lw=2.2, mutation_scale=16))
    ax.text(9.3, 3.1, "Inferensi\nIndividu", ha='center', va='center', fontsize=8.5, color='#4338CA', fontweight='bold')

    # Bottom CDSS Box
    cdss_box = patches.FancyBboxPatch((0.6, 0.15), 13.8, 0.65, boxstyle="round,pad=0,rounding_size=0.08",
                                     facecolor="#ECFDF5", edgecolor="#059669", linewidth=1.5, zorder=2)
    ax.add_patch(cdss_box)
    ax.text(7.5, 0.475, "Integrasi pada Clinical Decision Support System (CDSS): Mendukung Validasi Medis & Rekomendasi Sleep Hygiene Terpersonalisasi",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#065F46', zorder=3)

    plt.tight_layout()
    save_path = os.path.join(OUT_DIR, "Gambar_3_2_Alur_XAI_SHAP.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {save_path}")


# ==============================================================================
# 3. GAMBAR 3.3: MOCKUP ANTARMUKA PROTOTIPE WEB CDSS
# ==============================================================================
def create_cdss_mockup():
    # We will build a publication-grade composite mockup featuring:
    # 1. The CDSS Dashboard Header
    # 2. Form Input Parameters
    # 3. Real Prediction Badge (Severe Risk 94.8%)
    # 4. Realistic SHAP Waterfall Chart
    # 5. Personalized Clinical Recommendations
    fig = plt.figure(figsize=(16, 11), dpi=300)
    fig.patch.set_facecolor('#F1F5F9')

    # Create grid layout
    gs = fig.add_gridspec(12, 16, hspace=0.6, wspace=0.6)

    # Top Header Banner
    ax_head = fig.add_subplot(gs[0:2, :])
    ax_head.axis('off')
    banner = patches.FancyBboxPatch((0.01, 0.05), 0.98, 0.9, boxstyle="round,pad=0,rounding_size=0.03",
                                    facecolor="#FFFFFF", edgecolor="#E2E8F0", linewidth=1.5)
    ax_head.add_patch(banner)
    ax_head.text(0.04, 0.65, "Clinical Decision Support System (CDSS) - Analisis Risiko Gangguan Tidur", 
                 fontsize=15, fontweight='bold', color="#0F172A", va='center')
    ax_head.text(0.04, 0.3, "Deteksi Dini & Transparansi Faktor Risiko Menggunakan Algoritma CatBoost dan Explainable AI (XAI-SHAP)", 
                 fontsize=10.5, color="#64748B", va='center')
    
    # Status badges on header
    badge1 = patches.FancyBboxPatch((0.72, 0.28), 0.12, 0.44, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor="#ECFDF5", edgecolor="#10B981", linewidth=1)
    ax_head.add_patch(badge1)
    ax_head.text(0.78, 0.5, "● Model: CatBoost 93.9%", fontsize=8.5, fontweight='bold', color="#047857", ha='center', va='center')

    badge2 = patches.FancyBboxPatch((0.85, 0.28), 0.12, 0.44, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor="#EFF6FF", edgecolor="#3B82F6", linewidth=1)
    ax_head.add_patch(badge2)
    ax_head.text(0.91, 0.5, "● XAI: Tree-SHAP Exact", fontsize=8.5, fontweight='bold', color="#1D4ED8", ha='center', va='center')

    # Left Column: Input Form (gs[2:12, 0:6])
    ax_form = fig.add_subplot(gs[2:12, 0:6])
    ax_form.axis('off')
    f_box = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0,rounding_size=0.02",
                                   facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.5)
    ax_form.add_patch(f_box)

    ax_form.text(0.08, 0.94, "FORM PARAMETER GAYA HIDUP & MEDIS", fontsize=11, fontweight='bold', color="#1E3A8A")
    ax_form.plot([0.08, 0.92], [0.91, 0.91], color="#E2E8F0", lw=1.5)

    form_fields = [
        ("Usia (Tahun)", "24 Tahun"),
        ("Jenis Kelamin", "Laki-laki (Male)"),
        ("Profesi / Pekerjaan", "Software Engineer"),
        ("Durasi Layar Sebelum Tidur", "145 Menit (> 2 Jam)"),
        ("Asupan Kafein (Sebelum Tidur)", "180 mg (2 Cangkir Kopi)"),
        ("Tingkat Stres Harian (1-10)", "8 (Stres Berat)"),
        ("Durasi Tidur Harian", "5.2 Jam / Hari"),
        ("Kualitas Tidur Subjektif (1-10)", "4 (Kurang Nyenyak)"),
        ("Jumlah Langkah Harian", "3.200 Langkah (Sedentari)"),
        ("Kondisi Kesehatan Mental", "Anxiety (Kecemasan)"),
        ("Tipe Ritme Sirkadian", "Night Owl (Begadang)"),
        ("Waktu Mulai Terlelap (Latency)", "45 Menit (Lambat)")
    ]

    cur_yf = 0.85
    for label, val in form_fields:
        ax_form.text(0.08, cur_yf, label, fontsize=8.5, color="#475569", fontweight='semibold')
        cur_yf -= 0.025
        # Field box
        field_bg = patches.FancyBboxPatch((0.08, cur_yf - 0.03), 0.84, 0.038, boxstyle="round,pad=0,rounding_size=0.008",
                                          facecolor="#F8FAFC", edgecolor="#CBD5E1", linewidth=1)
        ax_form.add_patch(field_bg)
        ax_form.text(0.12, cur_yf - 0.012, val, fontsize=8.2, color="#0F172A")
        cur_yf -= 0.048

    # Button Simulation
    btn_box = patches.FancyBboxPatch((0.08, 0.04), 0.84, 0.055, boxstyle="round,pad=0,rounding_size=0.012",
                                     facecolor="#2563EB", edgecolor="none")
    ax_form.add_patch(btn_box)
    ax_form.text(0.5, 0.067, "▶  PROSES PREDIKSI & ANALISIS XAI-SHAP", fontsize=9.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # Right Top: Prediction Result Badge (gs[2:5, 6:16])
    ax_pred = fig.add_subplot(gs[2:5, 6:16])
    ax_pred.axis('off')
    p_box = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0,rounding_size=0.02",
                                   facecolor="#FEF2F2", edgecolor="#EF4444", linewidth=1.6)
    ax_pred.add_patch(p_box)

    ax_pred.text(0.05, 0.82, "HASIL PREDIKSI KLASIFIKASI MODEL CATBOOST", fontsize=11, fontweight='bold', color="#991B1B")
    ax_pred.plot([0.05, 0.95], [0.74, 0.74], color="#FECACA", lw=1.2)

    # Big Badge
    badge_res = patches.FancyBboxPatch((0.05, 0.18), 0.42, 0.48, boxstyle="round,pad=0,rounding_size=0.03",
                                       facecolor="#DC2626", edgecolor="none")
    ax_pred.add_patch(badge_res)
    ax_pred.text(0.26, 0.48, "SEVERE RISK", fontsize=15, fontweight='bold', color="#FFFFFF", ha='center', va='center')
    ax_pred.text(0.26, 0.30, "(Risiko Gangguan Tidur Berat)", fontsize=8.5, color="#FEE2E2", ha='center', va='center')

    # Confidence Metrics
    ax_pred.text(0.52, 0.58, "Probabilitas Prediksi Kelas Severe:", fontsize=9.5, color="#7F1D1D")
    ax_pred.text(0.52, 0.38, "94,8 %", fontsize=18, fontweight='bold', color="#DC2626")
    ax_pred.text(0.52, 0.22, "Tingkat Kepastian Diagnostik: SANGAT TINGGI | Indikasi: Insomnia / OSA", fontsize=8.5, color="#991B1B", fontstyle='italic')

    # Probability bars mini
    probs = [("Healthy", "1.2%", "#10B981"), ("Mild", "2.1%", "#3B82F6"), ("Moderate", "1.9%", "#F59E0B"), ("Severe", "94.8%", "#EF4444")]
    px = 0.78
    for c_name, c_val, c_col in probs:
        ax_pred.text(px, 0.55, c_name, fontsize=7.8, color="#475569", ha='center')
        ax_pred.text(px, 0.35, c_val, fontsize=8.2, fontweight='bold', color=c_col, ha='center')
        px += 0.052

    # Right Middle: SHAP Waterfall Plot (gs[5:9, 6:16])
    ax_shap = fig.add_subplot(gs[5:9, 6:16])
    ax_shap.axis('off')
    s_box = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0,rounding_size=0.02",
                                   facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.5)
    ax_shap.add_patch(s_box)

    ax_shap.text(0.05, 0.88, "ANALISIS TRANSPARANSI FAKTOR RISIKO (LOCAL SHAP WATERFALL EXPLANATION)", 
                 fontsize=10.5, fontweight='bold', color="#1E3A8A")
    ax_shap.text(0.05, 0.77, "Nilai Dasar E[f(x)] = 0.12  ───▶  Nilai Prediksi Akhir f(x) = 0.95 (Kontribusi Marginal Pasien)", 
                 fontsize=8.5, color="#475569")
    ax_shap.plot([0.05, 0.95], [0.72, 0.72], color="#E2E8F0", lw=1.2)

    # Draw waterfall bars inside ax_shap
    shap_features = [
        ("screen_time_before_bed_mins = 145", "+0.38", 0.38, True),
        ("caffeine_mg_before_bed = 180", "+0.24", 0.24, True),
        ("stress_score = 8", "+0.16", 0.16, True),
        ("sleep_latency_mins = 45", "+0.11", 0.11, True),
        ("sleep_duration_hrs = 5.2", "+0.07", 0.07, True),
        ("exercise_day = 1 (Minim)", "+0.04", 0.04, True),
        ("steps_that_day = 3200", "-0.05", 0.05, False),
        ("age = 24 (Faktor Usia)", "-0.12", 0.12, False)
    ]

    sy = 0.64
    for fname, val_str, mag, is_pos in shap_features:
        ax_shap.text(0.05, sy, fname, fontsize=8.2, color="#1E293B", va='center')
        
        # Bar representation
        bar_len = mag * 0.48
        b_color = "#EF4444" if is_pos else "#3B82F6"
        bx = 0.48
        if not is_pos:
            bx = 0.48 - bar_len
        
        bar_p = patches.Rectangle((bx, sy - 0.018), bar_len, 0.034, facecolor=b_color, edgecolor="none", zorder=3)
        ax_shap.add_patch(bar_p)
        
        tx = (bx + bar_len + 0.015) if is_pos else (bx - 0.055)
        ax_shap.text(tx, sy, val_str, fontsize=8, fontweight='bold', color=b_color, va='center', zorder=4)
        sy -= 0.068

    # Legend
    ax_shap.plot([0.48, 0.48], [0.12, 0.68], color="#94A3B8", linestyle="--", lw=1)
    ax_shap.text(0.48, 0.08, "Center Line (0.00)", fontsize=7.5, color="#64748B", ha='center')
    ax_shap.text(0.68, 0.08, "■ Meningkatkan Risiko (Merah)", fontsize=7.8, color="#DC2626")
    ax_shap.text(0.18, 0.08, "■ Menurunkan Risiko (Biru)", fontsize=7.8, color="#2563EB")

    # Right Bottom: Clinical Recommendations (gs[9:12, 6:16])
    ax_rec = fig.add_subplot(gs[9:12, 6:16])
    ax_rec.axis('off')
    r_box = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0,rounding_size=0.02",
                                   facecolor="#ECFDF5", edgecolor="#10B981", linewidth=1.5)
    ax_rec.add_patch(r_box)

    ax_rec.text(0.05, 0.82, "REKOMENDASI INTERVENSI KLINIS SLEEP HYGIENE TERPERSONALISASI", 
                 fontsize=10.5, fontweight='bold', color="#065F46")
    ax_rec.plot([0.05, 0.95], [0.72, 0.72], color="#A7F3D0", lw=1.2)

    recs = [
        "1. Intervensi Screen Time: Turunkan durasi gawai dari 145 menit menjadi maksimal 30 menit sebelum tidur (potensi reduksi risiko -35%).",
        "2. Intervensi Kafein: Hentikan konsumsi kopi berkafein 180 mg setelah pukul 14.00 WIB untuk menormalkan fase tidur gelombang lambat (Deep Sleep).",
        "3. Intervensi Relaksasi Stres: Terapkan protokol pernapasan 4-7-8 atau mindfulness 15 menit menjelang istirahat malam guna meredakan kecemasan."
    ]

    ry = 0.58
    for r in recs:
        ax_rec.text(0.05, ry, r, fontsize=8.2, color="#064E3B", va='top')
        ry -= 0.20

    plt.tight_layout()
    save_path = os.path.join(OUT_DIR, "Gambar_3_3_Mockup_CDSS.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {save_path}")


# ==============================================================================
# 4. GAMBAR 3.4: DISTRIBUSI SEBARAN KELAS TARGET (COMPLEMENTARY / TABEL 3.5)
# ==============================================================================
def create_target_distribution_figure():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')

    classes = ['Healthy', 'Mild', 'Moderate', 'Severe']
    counts = [54156, 33479, 8299, 4066]
    percentages = [54.156, 33.479, 8.299, 4.066]
    colors = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444']

    bars = ax.bar(classes, counts, color=colors, width=0.55, edgecolor='#0F172A', linewidth=1.2, zorder=3)

    # Gridlines
    ax.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1', zorder=0)
    ax.set_axisbelow(True)

    # Labels on top of bars
    for bar, count, pct in zip(bars, counts, percentages):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1200, 
                f"{count:,} Rekaman\n({pct:.2f}%)", 
                ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#1E293B')

    ax.set_ylim(0, 62000)
    ax.set_ylabel('Jumlah Sampel Rekaman (Entri)', fontsize=11, fontweight='bold', color='#1E293B', labelpad=10)
    ax.set_xlabel('Tingkatan Risiko Gangguan Tidur (sleep_disorder_risk)', fontsize=11, fontweight='bold', color='#1E293B', labelpad=10)
    ax.set_title('Distribusi Ketidakseimbangan Kelas Target (Class Imbalance) pada Dataset 100.000 Baris', 
                 fontsize=12, fontweight='bold', color='#0F172A', pad=15)

    # Annotation for Severe Class
    ax.annotate('Kelas Minoritas Kritis (4,066%)\nDitangani dengan auto_class_weights="Balanced"',
                xy=(3, 4066), xytext=(2.3, 20000),
                arrowprops=dict(arrowstyle="->", color="#DC2626", lw=1.8, connectionstyle="arc3,rad=-0.2"),
                fontsize=9, fontweight='bold', color="#DC2626",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#FEF2F2", edgecolor="#EF4444", lw=1))

    plt.tight_layout()
    save_path = os.path.join(OUT_DIR, "Gambar_3_4_Distribusi_Target.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {save_path}")


if __name__ == "__main__":
    create_crisp_dm_figure()
    create_shap_flowchart()
    create_cdss_mockup()
    create_target_distribution_figure()
    print("\n[SUCCESS] All BAB 3 figures generated successfully!")
