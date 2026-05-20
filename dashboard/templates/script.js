/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SleepRisk XAI Dashboard — Main JavaScript
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

const API = 'http://localhost:5000/api';

let featureMeta = null;

// ── Label & Description per fitur ──────────────
const FEATURE_LABELS = {
  age:                      { label: 'Usia', unit: 'tahun', group: 'Profil Individu' },
  gender:                   { label: 'Jenis Kelamin', group: 'Profil Individu' },
  occupation:               { label: 'Pekerjaan', group: 'Profil Individu' },
  bmi:                      { label: 'BMI', unit: 'kg/m²', group: 'Profil Individu' },
  country:                  { label: 'Negara', group: 'Profil Individu' },
  chronotype:               { label: 'Kronotipen', group: 'Profil Individu' },
  mental_health_condition:  { label: 'Kondisi Mental', group: 'Profil Individu' },
  sleep_duration_hrs:       { label: 'Durasi Tidur', unit: 'jam', group: 'Pola Tidur' },
  sleep_quality_score:      { label: 'Kualitas Tidur', unit: '/10', group: 'Pola Tidur' },
  rem_percentage:           { label: 'REM Sleep', unit: '%', group: 'Pola Tidur' },
  deep_sleep_percentage:    { label: 'Deep Sleep', unit: '%', group: 'Pola Tidur' },
  sleep_latency_mins:       { label: 'Latensi Tidur', unit: 'menit', group: 'Pola Tidur' },
  wake_episodes_per_night:  { label: 'Terbangun/Malam', unit: 'kali', group: 'Pola Tidur' },
  nap_duration_mins:        { label: 'Durasi Tidur Siang', unit: 'menit', group: 'Pola Tidur' },
  weekend_sleep_diff_hrs:   { label: 'Beda Tidur Akhir Pekan', unit: 'jam', group: 'Pola Tidur' },
  caffeine_mg_before_bed:   { label: 'Kafein Sebelum Tidur', unit: 'mg', group: 'Gaya Hidup' },
  alcohol_units_before_bed: { label: 'Alkohol Sebelum Tidur', unit: 'unit', group: 'Gaya Hidup' },
  screen_time_before_bed_mins: { label: 'Screen Time Sebelum Tidur', unit: 'menit', group: 'Gaya Hidup' },
  exercise_day:             { label: 'Olahraga Hari Ini', unit: '(0/1)', group: 'Gaya Hidup' },
  steps_that_day:           { label: 'Langkah Kaki', unit: 'langkah', group: 'Gaya Hidup' },
  stress_score:             { label: 'Skor Stres', unit: '/10', group: 'Gaya Hidup' },
  work_hours_that_day:      { label: 'Jam Kerja Hari Ini', unit: 'jam', group: 'Gaya Hidup' },
  sleep_aid_used:           { label: 'Penggunaan Obat Tidur', unit: '(0/1)', group: 'Gaya Hidup' },
  shift_work:               { label: 'Kerja Shift', unit: '(0/1)', group: 'Gaya Hidup' },
  heart_rate_resting_bpm:   { label: 'Detak Jantung Istirahat', unit: 'bpm', group: 'Kondisi Fisik' },
  room_temperature_celsius: { label: 'Suhu Kamar', unit: '°C', group: 'Lingkungan' },
  season:                   { label: 'Musim', group: 'Lingkungan' },
  day_type:                 { label: 'Tipe Hari', group: 'Lingkungan' },
  cognitive_performance_score: { label: 'Skor Kognitif', unit: '/100', group: 'Kondisi Fisik' },
};

const RISK_INFO = {
  Healthy:  { emoji: '✅', desc: 'Pola tidur Anda tergolong sehat. Pertahankan gaya hidup saat ini!', color: 'healthy' },
  Mild:     { emoji: '⚠️', desc: 'Ada indikasi gangguan tidur ringan. Beberapa kebiasaan perlu diperbaiki.', color: 'mild' },
  Moderate: { emoji: '🔶', desc: 'Risiko gangguan tidur sedang terdeteksi. Disarankan untuk berkonsultasi.', color: 'moderate' },
  Severe:   { emoji: '🚨', desc: 'Risiko gangguan tidur tinggi terdeteksi. Segera konsultasikan ke tenaga medis!', color: 'severe' },
};

const PROB_COLORS = {
  Healthy:  '#10b981',
  Mild:     '#f59e0b',
  Moderate: '#f97316',
  Severe:   '#ef4444',
};

// ── INIT ────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  await loadMeta();
});

// ── LOAD META & BUILD FORM ──────────────────────
async function loadMeta() {
  try {
    const res = await fetch(`${API}/meta`);
    if (!res.ok) throw new Error('Server belum siap');
    featureMeta = await res.json();

    document.getElementById('model-accuracy-badge').textContent =
      `Akurasi: ${(featureMeta.accuracy * 100).toFixed(2)}%`;

    buildForm(featureMeta);
    document.getElementById('btn-predict').disabled = false;
  } catch (e) {
    document.getElementById('form-fields-container').innerHTML = `
      <div class="loading-placeholder">
        <span style="font-size:2rem">⚠️</span>
        <p style="color:#ef4444;font-weight:600">Koneksi ke server gagal</p>
        <p style="font-size:0.82rem">Pastikan <code>app.py</code> sudah berjalan di port 5000.</p>
      </div>`;
  }
}

// ── BUILD FORM DYNAMICALLY ──────────────────────
function buildForm(meta) {
  const container = document.getElementById('form-fields-container');
  const ranges    = meta.feature_ranges;
  const features  = meta.feature_names;

  // Kelompokkan fitur berdasarkan group
  const groups = {};
  features.forEach(f => {
    const g = (FEATURE_LABELS[f] || {}).group || 'Lainnya';
    if (!groups[g]) groups[g] = [];
    groups[g].push(f);
  });

  let html = '<div class="form-grid">';
  for (const [grpName, fields] of Object.entries(groups)) {
    html += `<div class="form-section-title">${grpName}</div>`;
    fields.forEach(f => {
      const info  = FEATURE_LABELS[f] || { label: f, unit: '' };
      const range = ranges[f];
      const unit  = info.unit ? `<em>${info.unit}</em>` : '';
      html += `<div class="form-group" id="group-${f}">`;
      html += `<label for="field-${f}">${info.label} ${unit}</label>`;

      if (range.type === 'categorical') {
        html += `<select id="field-${f}" name="${f}">`;
        html += `<option value="">Pilih...</option>`;
        range.options.forEach(opt => {
          html += `<option value="${opt}">${opt}</option>`;
        });
        html += `</select>`;
      } else {
        // Gunakan step="any" agar tidak ada masalah validasi angka desimal / negatif
        html += `<input type="number" id="field-${f}" name="${f}"
          min="${range.min}" max="${range.max}" step="any"
          placeholder="${range.mean.toFixed(1)}" />`;
      }
      html += `</div>`;
    });
  }
  html += '</div>';
  container.innerHTML = html;

  // Event listeners — tombol analisis menggunakan click handler langsung, bukan form submit
  document.getElementById('btn-predict').addEventListener('click', handlePredict);
  document.getElementById('btn-reset').addEventListener('click', resetForm);
  document.getElementById('btn-sample').addEventListener('click', loadSample);
}

// ── LOAD SAMPLE DATA ────────────────────────────
async function loadSample() {
  try {
    const btn = document.getElementById('btn-sample');
    btn.textContent = '⏳ Memuat...';
    btn.disabled = true;

    const res  = await fetch(`${API}/sample`);
    const data = await res.json();

    featureMeta.feature_names.forEach(f => {
      const el = document.getElementById(`field-${f}`);
      if (el && data[f] !== undefined) el.value = data[f];
    });

    btn.textContent = '🎲 Isi Sampel Acak';
    btn.disabled = false;
  } catch (e) {
    console.error(e);
    const btn = document.getElementById('btn-sample');
    btn.textContent = '🎲 Isi Sampel Acak';
    btn.disabled = false;
  }
}

// ── VALIDATE FORM ───────────────────────────────
function validateForm() {
  const missing = [];
  let firstMissingEl = null;

  // Reset semua peringatan error sebelumnya
  featureMeta.feature_names.forEach(f => {
    const el = document.getElementById(`field-${f}`);
    if (el) el.classList.remove('input-error');
  });

  featureMeta.feature_names.forEach(f => {
    const el = document.getElementById(`field-${f}`);
    if (!el) return;
    if (el.value === '' || el.value === null || el.value === undefined) {
      const info = FEATURE_LABELS[f] || { label: f };
      missing.push(info.label);
      
      // Tambahkan class error untuk highlight merah dan animasi getar
      el.classList.add('input-error');
      
      // Hapus highlight merah secara otomatis ketika user mulai mengetik/memilih
      el.addEventListener('input', function() {
        this.classList.remove('input-error');
      }, { once: true });

      if (!firstMissingEl) firstMissingEl = el;
    }
  });

  // Jika ada form yang kosong, scroll ke input pertama yang kosong dan beri fokus
  if (firstMissingEl) {
    firstMissingEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    setTimeout(() => firstMissingEl.focus(), 300);
  }

  return missing;
}

// ── HANDLE PREDICT ──────────────────────────────
async function handlePredict(e) {
  if (e) e.preventDefault();

  // Validasi manual
  const missing = validateForm();
  if (missing.length > 0) {
    alert('Mohon lengkapi field berikut:\n• ' + missing.join('\n• '));
    return;
  }

  const btnText    = document.querySelector('.btn-text');
  const btnLoading = document.querySelector('.btn-loading');
  const btnPredict = document.getElementById('btn-predict');

  btnText.style.display    = 'none';
  btnLoading.style.display = 'flex';
  btnPredict.disabled      = true;

  try {
    // Kumpulkan data form
    const formData = {};
    featureMeta.feature_names.forEach(f => {
      const el = document.getElementById(`field-${f}`);
      if (!el) return;
      if (featureMeta.cat_features.includes(f)) {
        formData[f] = el.value;
      } else {
        formData[f] = parseFloat(el.value);
      }
    });

    const res  = await fetch(`${API}/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    const result = await res.json();

    if (!result.success) throw new Error(result.error);

    displayResult(result, formData);
  } catch (err) {
    alert('Error: ' + err.message);
    console.error(err);
  } finally {
    btnText.style.display    = 'inline';
    btnLoading.style.display = 'none';
    btnPredict.disabled      = false;
  }
}

// ── DISPLAY RESULT ──────────────────────────────
function displayResult(result, inputData) {
  const panel = document.getElementById('result-panel');
  panel.style.display = 'block';
  panel.scrollIntoView({ behavior: 'smooth', block: 'start' });

  const info  = RISK_INFO[result.prediction] || {};

  // Prediction card
  const predEl = document.getElementById('pred-result');
  predEl.textContent = `${info.emoji} ${result.prediction}`;
  predEl.className   = `pred-result ${info.color}`;
  document.getElementById('pred-desc').textContent = info.desc || '';

  // Probability bars
  renderProbBars(result.probabilities);

  // SHAP chart
  renderShapChart(result.shap_top10, result.prediction);

  // Interpretation
  renderInterpretation(result, inputData);
}

// ── RENDER PROBABILITY BARS ─────────────────────
function renderProbBars(probs) {
  const container = document.getElementById('prob-bars');
  const order = ['Healthy', 'Mild', 'Moderate', 'Severe'];
  container.innerHTML = order.map(cls => {
    const pct = ((probs[cls] || 0) * 100).toFixed(1);
    const col = PROB_COLORS[cls] || '#6366f1';
    return `
      <div class="prob-row">
        <div class="prob-class">${cls}</div>
        <div class="prob-bar-bg">
          <div class="prob-bar-fill" style="width:${pct}%;background:${col}"></div>
        </div>
        <div class="prob-val">${pct}%</div>
      </div>`;
  }).join('');
}

// ── RENDER SHAP CHART ───────────────────────────
function renderShapChart(shapTop10, predictionClass) {
  const container = document.getElementById('shap-chart');
  const maxAbs    = Math.max(...shapTop10.map(d => Math.abs(d.shap)), 0.001);

  container.innerHTML = shapTop10.map(item => {
    const isPos   = item.shap >= 0;
    const pct     = (Math.abs(item.shap) / maxAbs * 48).toFixed(1); // max 48% of half width
    
    // Karena backend sudah mengirimkan "Risk Level SHAP":
    // Positif (+) = Faktor Risiko (Merah)
    // Negatif (-) = Faktor Pelindung (Biru)
    const visualDir = isPos ? 'pos' : 'neg';

    const label   = (FEATURE_LABELS[item.feature] || {}).label || item.feature;
    const valSign = isPos ? `+${item.shap.toFixed(4)}` : item.shap.toFixed(4);
    
    const barStyle= visualDir === 'pos'
      ? `left:50%;width:${pct}%`
      : `right:50%;width:${pct}%`;

    return `
      <div class="shap-row">
        <div class="shap-fname" title="${item.feature} = ${item.value}">${label}</div>
        <div class="shap-axis">
          <div class="shap-zero"></div>
          <div class="shap-bar ${visualDir}" style="${barStyle}"></div>
        </div>
        <div class="shap-val ${visualDir}">${valSign}</div>
      </div>`;
  }).join('');
}

// ── RENDER INTERPRETATION ───────────────────────
function renderInterpretation(result, inputData) {
  const box      = document.getElementById('interpretation-box');
  const shap     = result.shap_top10;
  const topPos   = shap.filter(d => d.shap > 0).slice(0, 3);
  const topNeg   = shap.filter(d => d.shap < 0).slice(0, 2);

  // Sekarang logikanya universal:
  // SHAP > 0 (Positif) = Mendorong ke arah Gangguan Tidur (Risiko Naik)
  // SHAP < 0 (Negatif) = Melindungi dari Gangguan Tidur (Mendorong ke arah Sehat)
  const posText = "faktor risiko (meningkatkan probabilitas gangguan)";
  const negText = "faktor pelindung (mendukung kesehatan tidur)";

  const posItems = topPos.map(d => {
    const lbl = (FEATURE_LABELS[d.feature] || {}).label || d.feature;
    return `<li><strong>${lbl}</strong> (nilai: ${d.value}) → ${posText} (+${d.shap.toFixed(4)})</li>`;
  }).join('');

  const negItems = topNeg.map(d => {
    const lbl = (FEATURE_LABELS[d.feature] || {}).label || d.feature;
    return `<li><strong>${lbl}</strong> (nilai: ${d.value}) → ${negText} (${d.shap.toFixed(4)})</li>`;
  }).join('');

  box.innerHTML = `
    <strong>📖 Interpretasi SHAP untuk Prediksi Ini:</strong>
    <p style="margin-top:10px">Model CatBoost memprediksi risiko <strong>${result.prediction}</strong>
    berdasarkan kombinasi faktor gaya hidup berikut:</p>
    ${posItems ? `<ul style="margin-top:8px">${posItems}</ul>` : ''}
    ${negItems ? `
    <p style="margin-top:12px">Sedangkan fitur yang bekerja berlawanan arah (menurunkan kecenderungan prediksi ini):</p>
    <ul style="margin-top:8px">${negItems}</ul>` : ''}
    <p style="margin-top:12px;font-size:0.82rem;color:var(--text-muted)">
      * Nilai SHAP merupakan kontribusi marginal setiap fitur terhadap prediksi kelas <strong>${result.prediction}</strong>,
      dihitung menggunakan metode Shapley Additive exPlanations (SHAP) berbasis teori permainan koalisi.
    </p>`;
}

// ── RESET FORM ──────────────────────────────────
function resetForm() {
  document.getElementById('prediction-form').reset();
  document.getElementById('result-panel').style.display = 'none';
}
