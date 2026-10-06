/**
 * SleepRisk XAI Dashboard – Frontend Interactive Logic
 * Powered by CatBoost (Predictor) + SHAP (Explainer)
 * Redesigned with Modern Health-Tech Aesthetics & Human-Centric Clinical Explanations
 */

const API = 'http://localhost:5000/api';
let featureMeta = null;

// ── METADATA LABEL BAHASA MANUSIA & KELOMPOK FITUR ──
const FEATURE_LABELS = {
  // Gaya Hidup & Gadget
  screen_time_before_bed_mins: { 
    label: 'Main HP/Laptop Sebelum Tidur', 
    hint: 'Lama scrolling medsos, chat, atau nonton video di kasur', 
    unit: 'menit', 
    group: 'Gaya Hidup', 
    icon: '📱' 
  },
  caffeine_mg_before_bed: { 
    label: 'Konsumsi Kafein Sore/Malam', 
    hint: '1 cangkir kopi hitam ±80-100 mg, teh/soda ±30-40 mg', 
    unit: 'mg', 
    group: 'Gaya Hidup', 
    icon: '☕' 
  },
  alcohol_units_before_bed: { 
    label: 'Konsumsi Minuman Beralkohol', 
    hint: '1 unit = 1 gelas bir kecil atau 1 sloki minuman keras', 
    unit: 'unit', 
    group: 'Gaya Hidup', 
    icon: '🍷' 
  },
  stress_score: { 
    label: 'Tingkat Beban Pikiran / Stres', 
    hint: 'Skala 1 (sangat santai/bebas) sampai 10 (sangat cemas/tertekan)', 
    unit: '/10', 
    group: 'Gaya Hidup', 
    icon: '🧠' 
  },
  work_hours_that_day: { 
    label: 'Total Jam Kerja Harian', 
    hint: 'Berapa jam Anda bekerja atau lembur pada hari tersebut', 
    unit: 'jam', 
    group: 'Gaya Hidup', 
    icon: '💼' 
  },
  steps_that_day: { 
    label: 'Aktivitas Langkah Kaki Harian', 
    hint: 'Jumlah langkah jalan kaki harian (target normal 6.000-8.000)', 
    unit: 'langkah', 
    group: 'Gaya Hidup', 
    icon: '👟' 
  },
  exercise_day: { 
    label: 'Apakah Berolahraga Hari Ini?', 
    hint: 'Pilih 1 jika berolahraga minimal 20 menit, 0 jika tidak', 
    unit: '0/1', 
    group: 'Gaya Hidup', 
    icon: '🏃' 
  },
  sleep_aid_used: { 
    label: 'Minum Obat / Suplemen Tidur?', 
    hint: 'Pilih 1 jika meminum obat tidur/melatonin, 0 jika tidak', 
    unit: '0/1', 
    group: 'Gaya Hidup', 
    icon: '💊' 
  },
  shift_work: { 
    label: 'Bekerja Sistem Shift Malam?', 
    hint: 'Pilih 1 jika jadwal kerja bergilir/shift malam, 0 jika jam normal', 
    unit: '0/1', 
    group: 'Gaya Hidup', 
    icon: '🔄' 
  },

  // Pola & Kualitas Tidur
  sleep_duration_hrs: { 
    label: 'Durasi Tidur Nyata Semalam', 
    hint: 'Total jam Anda benar-benar tidur lelap (bukan cuma rebahan)', 
    unit: 'jam', 
    group: 'Pola Tidur', 
    icon: '⏱️' 
  },
  sleep_latency_mins: { 
    label: 'Lama Rebahan Sampai Terlelap', 
    hint: 'Berapa menit Anda berguling di kasur sebelum akhirnya tidur', 
    unit: 'menit', 
    group: 'Pola Tidur', 
    icon: '⏳' 
  },
  wake_episodes_per_night: { 
    label: 'Sering Terbangun Tengah Malam', 
    hint: 'Berapa kali Anda terjaga di tengah tidur malam', 
    unit: 'kali', 
    group: 'Pola Tidur', 
    icon: '👀' 
  },
  sleep_quality_score: { 
    label: 'Kualitas Tidur yang Dirasakan', 
    hint: 'Skala 1 (sangat buruk/gelisah) sampai 10 (sangat nyenyak)', 
    unit: '/10', 
    group: 'Pola Tidur', 
    icon: '⭐' 
  },
  weekend_sleep_diff_hrs: { 
    label: 'Beda Jam Tidur Libur vs Kerja', 
    hint: 'Berapa jam selisih jam tidur weekend (sering begadang saat libur)', 
    unit: 'jam', 
    group: 'Pola Tidur', 
    icon: '📅' 
  },
  nap_duration_mins: { 
    label: 'Durasi Tidur Siang', 
    hint: 'Lama tidur siang di hari tersebut (ideal: 20-30 menit)', 
    unit: 'menit', 
    group: 'Pola Tidur', 
    icon: '🛌' 
  },
  deep_sleep_percentage: { 
    label: 'Fase Tidur Nyenyak (Deep Sleep)', 
    hint: 'Proporsi fase pemulihan fisik tubuh (normal: 15-25%)', 
    unit: '%', 
    group: 'Pola Tidur', 
    icon: '🌌' 
  },
  rem_percentage: { 
    label: 'Fase Tidur Mimpi (REM Sleep)', 
    hint: 'Proporsi fase pemulihan memori otak (normal: 20-25%)', 
    unit: '%', 
    group: 'Pola Tidur', 
    icon: '💤' 
  },

  // Profil Individu
  age: { 
    label: 'Usia Anda Saat Ini', 
    hint: 'Usia dalam tahun', 
    unit: 'tahun', 
    group: 'Profil Individu', 
    icon: '👤' 
  },
  gender: { 
    label: 'Jenis Kelamin', 
    hint: 'Pilihan jenis kelamin biologis', 
    group: 'Profil Individu', 
    icon: '⚧' 
  },
  occupation: { 
    label: 'Bidang Profesi / Pekerjaan', 
    hint: 'Jenis profesi utama sehari-hari', 
    group: 'Profil Individu', 
    icon: '💼' 
  },
  bmi: { 
    label: 'Indeks Massa Tubuh (BMI)', 
    hint: 'Berat(kg) / Tinggi(m)². Normal: 18.5 - 24.9', 
    unit: 'kg/m²', 
    group: 'Profil Individu', 
    icon: '⚖️' 
  },
  chronotype: { 
    label: 'Tipe Jam Biologis Anda', 
    hint: 'Morning (bangun pagi), Night Owl (suka begadang), Neutral', 
    group: 'Profil Individu', 
    icon: '🕰️' 
  },
  mental_health_condition: { 
    label: 'Kondisi Suasana Hati / Mental', 
    hint: 'Healthy (stabil), Anxiety (cemas), Depression, Both', 
    group: 'Profil Individu', 
    icon: '🧘' 
  },

  // Kondisi Fisik & Ruangan
  heart_rate_resting_bpm: { 
    label: 'Detak Jantung Santai (Resting)', 
    hint: 'Denyut nadi per menit saat sedang santai (normal: 60-80 bpm)', 
    unit: 'bpm', 
    group: 'Kondisi Fisik', 
    icon: '💓' 
  },
  cognitive_performance_score: { 
    label: 'Tingkat Fokus & Konsentrasi', 
    hint: 'Skor ketajaman berpikir dan fokus harian (skala 0-100)', 
    unit: '/100', 
    group: 'Kondisi Fisik', 
    icon: '🎯' 
  },
  room_temperature_celsius: { 
    label: 'Suhu Kamar Tempat Tidur', 
    hint: 'Suhu AC/ruangan kamar Anda (ideal sejuk: 19-22°C)', 
    unit: '°C', 
    group: 'Kondisi Fisik', 
    icon: '🌡️' 
  },
  season: { 
    label: 'Musim Saat Pengambilan Data', 
    hint: 'Kondisi iklim musim saat ini', 
    group: 'Kondisi Fisik', 
    icon: '🍂' 
  }
};

const RISK_INFO = {
  Healthy: { 
    emoji: '🟢', 
    label: 'Kondisi Tidur Sehat & Prima', 
    shortLabel: 'Sehat (Optimal)',
    desc: 'Kebugaran fisiologis sangat optimal. Ritme tidur dan kebiasaan harian efektif menjaga stamina fisik.', 
    urgency: 'Optimal (Pertahankan)',
    color: 'emerald' 
  },
  Mild: { 
    emoji: '🟡', 
    label: 'Gejala Gangguan Tidur Ringan', 
    shortLabel: 'Ringan (Mild)',
    desc: 'Terdeteksi sedikit disrupsi dari kebiasaan gadget atau kafein. Penyesuaian kecil cepat memulihkan ritme.', 
    urgency: 'Penyesuaian Ringan',
    color: 'amber' 
  },
  Moderate: { 
    emoji: '🟠', 
    label: 'Kualitas Tidur Terganggu (Sedang)', 
    shortLabel: 'Sedang (Moderate)',
    desc: 'Disrupsi tidur menurunkan fokus harian dan memicu lelah konstan. Terapkan jadwal istirahat disiplin.', 
    urgency: 'Intervensi Bertahap',
    color: 'orange' 
  },
  Severe: { 
    emoji: '🔴', 
    label: 'Risiko Gangguan Tidur Tinggi', 
    shortLabel: 'Tinggi (Severe)',
    desc: 'Beban disrupsi tidur berada pada tingkat tinggi. Fokus perbaiki pemicu utama dan evaluasi klinis bila menetap.', 
    urgency: 'Prioritas Aksi Cepat',
    color: 'rose' 
  },
};

const PROB_COLORS = {
  Healthy:  '#10b981',
  Mild:     '#f59e0b',
  Moderate: '#f97316',
  Severe:   '#ef4444',
};

// ── PRESET DATA DEMO CEPAT ────────────────────────
const PRESETS = {
  healthy: {
    age: 28, gender: "Female", occupation: "Teacher", bmi: 22.4, sleep_duration_hrs: 7.5, sleep_quality_score: 8.5,
    rem_percentage: 23.0, deep_sleep_percentage: 21.0, sleep_latency_mins: 15, wake_episodes_per_night: 1,
    caffeine_mg_before_bed: 0, alcohol_units_before_bed: 0, screen_time_before_bed_mins: 20, exercise_day: 1,
    steps_that_day: 7800, nap_duration_mins: 20, stress_score: 3.2, work_hours_that_day: 7.5, chronotype: "Morning",
    mental_health_condition: "Healthy", heart_rate_resting_bpm: 64, sleep_aid_used: 0, shift_work: 0,
    room_temperature_celsius: 20.5, weekend_sleep_diff_hrs: 0.5, season: "Autumn", cognitive_performance_score: 88.0
  },
  mild: {
    age: 24, gender: "Male", occupation: "Software Engineer", bmi: 24.1, sleep_duration_hrs: 5.8, sleep_quality_score: 5.5,
    rem_percentage: 21.0, deep_sleep_percentage: 17.5, sleep_latency_mins: 35, wake_episodes_per_night: 3,
    caffeine_mg_before_bed: 60, alcohol_units_before_bed: 0, screen_time_before_bed_mins: 85, exercise_day: 0,
    steps_that_day: 4100, nap_duration_mins: 0, stress_score: 6.8, work_hours_that_day: 9.5, chronotype: "Neutral",
    mental_health_condition: "Healthy", heart_rate_resting_bpm: 72, sleep_aid_used: 0, shift_work: 0,
    room_temperature_celsius: 23.0, weekend_sleep_diff_hrs: 2.2, season: "Summer", cognitive_performance_score: 55.0
  },
  severe: {
    age: 42, gender: "Male", occupation: "Nurse", bmi: 28.5, sleep_duration_hrs: 4.2, sleep_quality_score: 2.0,
    rem_percentage: 18.0, deep_sleep_percentage: 12.0, sleep_latency_mins: 45, wake_episodes_per_night: 5,
    caffeine_mg_before_bed: 120, alcohol_units_before_bed: 1.5, screen_time_before_bed_mins: 110, exercise_day: 0,
    steps_that_day: 8500, nap_duration_mins: 45, stress_score: 8.5, work_hours_that_day: 12.0, chronotype: "Night Owl",
    mental_health_condition: "Both", heart_rate_resting_bpm: 82, sleep_aid_used: 1, shift_work: 1,
    room_temperature_celsius: 25.0, weekend_sleep_diff_hrs: 3.5, season: "Spring", cognitive_performance_score: 20.0
  }
};

// ── INIT ──────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  await loadMeta();
});

// ── LOAD METADATA & BUILD FORM ────────────────────
async function loadMeta() {
  try {
    const res = await fetch(`${API}/meta`);
    if (!res.ok) throw new Error('Server belum siap');
    featureMeta = await res.json();

    const accBadge = document.getElementById('model-accuracy-badge');
    if (accBadge) {
      accBadge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-500"></span> Akurasi Model: <strong>${(featureMeta.accuracy * 100).toFixed(2)}%</strong>`;
    }

    buildForm(featureMeta);
    document.getElementById('btn-predict').disabled = false;
  } catch (e) {
    document.getElementById('form-fields-container').innerHTML = `
      <div class="py-12 px-6 rounded-2xl bg-rose-50 border border-rose-200 text-center">
        <span class="text-3xl">⚠️</span>
        <h3 class="text-base font-bold text-rose-800 mt-2">Koneksi Backend Gagal</h3>
        <p class="text-xs sm:text-sm text-rose-600 mt-1 max-w-md mx-auto">
          Pastikan server backend Flask (<code class="bg-rose-100 px-1 py-0.5 rounded font-mono text-rose-800">python app.py</code>) sudah aktif di port 5000.
        </p>
      </div>`;
  }
}

// ── BUILD FORM DYNAMICALLY WITH RICH UI ──────────
function buildForm(meta) {
  const container = document.getElementById('form-fields-container');
  const ranges    = meta.feature_ranges;
  const features  = meta.feature_names;

  // Kelompokkan fitur berdasarkan kategori
  const groups = {};
  features.forEach(f => {
    const g = (FEATURE_LABELS[f] || {}).group || 'Lainnya';
    if (!groups[g]) groups[g] = [];
    groups[g].push(f);
  });

  let html = '';
  for (const [grpName, fields] of Object.entries(groups)) {
    html += `
      <div class="group-section" data-group="${grpName}">
        <div class="flex items-center gap-2 mb-3">
          <span class="text-xs font-bold uppercase tracking-wider text-slate-500 bg-slate-100 px-3 py-1 rounded-lg">
            ${grpName} (${fields.length} parameter)
          </span>
          <div class="h-px flex-1 bg-slate-200/70"></div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">`;

    fields.forEach(f => {
      const info  = FEATURE_LABELS[f] || { label: f, hint: '', unit: '', icon: '📌' };
      const range = ranges[f];
      const unitPill = info.unit ? `<span class="text-[10px] font-bold text-sky-700 bg-sky-50 px-2 py-0.5 rounded-md border border-sky-100">${info.unit}</span>` : '';

      html += `
        <div class="form-group flex flex-col justify-between p-4 bg-slate-50/70 rounded-2xl border border-slate-200/80 hover:border-sky-300 focus-within:border-sky-500 focus-within:ring-3 focus-within:ring-sky-100 focus-within:bg-white transition-all shadow-2xs" id="group-${f}">
          <div>
            <div class="flex items-center justify-between gap-1 mb-1">
              <label for="field-${f}" class="text-xs font-bold text-slate-800 flex items-center gap-1.5 cursor-pointer">
                <span>${info.icon}</span> ${info.label}
              </label>
              ${unitPill}
            </div>
            ${info.hint ? `<p class="text-[11px] text-slate-500 mb-2.5 leading-snug">${info.hint}</p>` : ''}
          </div>`;

      if (range.type === 'categorical') {
        html += `
          <select id="field-${f}" name="${f}" class="w-full px-3 py-2.5 text-xs font-medium text-slate-800 bg-white border border-slate-200 rounded-xl focus:outline-none focus:border-sky-500 cursor-pointer shadow-2xs">
            <option value="">Pilih salah satu...</option>
            ${range.options.map(opt => `<option value="${opt}">${opt}</option>`).join('')}
          </select>`;
      } else {
        html += `
          <input type="number" id="field-${f}" name="${f}"
            min="${range.min}" max="${range.max}" step="any"
            placeholder="Contoh rata-rata: ${range.mean.toFixed(1)}"
            class="w-full px-3 py-2.5 text-xs font-medium text-slate-800 bg-white border border-slate-200 rounded-xl focus:outline-none focus:border-sky-500 shadow-2xs" />`;
      }

      html += `</div>`;
    });

    html += `
        </div>
      </div>`;
  }

  container.innerHTML = html;

  // Event Listeners
  document.getElementById('btn-predict').addEventListener('click', handlePredict);
  document.getElementById('btn-reset').addEventListener('click', resetForm);
  document.getElementById('btn-sample').addEventListener('click', loadSample);
  document.getElementById('btn-print-report').addEventListener('click', handlePrintReport);
  document.getElementById('btn-copy-plan').addEventListener('click', handleCopyPlan);
  document.getElementById('btn-reset-whatif').addEventListener('click', handleResetWhatIf);

  // Preset Buttons
  document.getElementById('btn-preset-healthy').addEventListener('click', () => applyPreset('healthy'));
  document.getElementById('btn-preset-mild').addEventListener('click', () => applyPreset('mild'));
  document.getElementById('btn-preset-severe').addEventListener('click', () => applyPreset('severe'));

  // Category Tabs Filter Logic
  setupCategoryTabs();
}

// ── SETUP CATEGORY TABS ───────────────────────────
function setupCategoryTabs() {
  const tabs = document.querySelectorAll('#category-tabs .tab-btn');
  tabs.forEach(tab => {
    tab.addEventListener('click', function () {
      tabs.forEach(t => {
        t.classList.remove('bg-slate-900', 'text-white', 'shadow-2xs');
        t.classList.add('bg-slate-100', 'text-slate-600');
      });
      this.classList.remove('bg-slate-100', 'text-slate-600');
      this.classList.add('bg-slate-900', 'text-white', 'shadow-2xs');

      const grp = this.dataset.group;
      const sections = document.querySelectorAll('.group-section');
      sections.forEach(sec => {
        if (grp === 'all' || sec.dataset.group === grp) {
          sec.style.display = 'block';
        } else {
          sec.style.display = 'none';
        }
      });
    });
  });
}

// ── APPLY DEMO PRESET ─────────────────────────────
function applyPreset(type) {
  const data = PRESETS[type];
  if (!data) return;

  featureMeta.feature_names.forEach(f => {
    const el = document.getElementById(`field-${f}`);
    if (el && data[f] !== undefined) {
      el.value = data[f];
      el.classList.remove('input-error');
    }
  });

  // Animasi feedback visual
  const card = document.getElementById('form-fields-container');
  card.classList.add('ring-2', 'ring-sky-400');
  setTimeout(() => card.classList.remove('ring-2', 'ring-sky-400'), 500);
}

// ── LOAD RANDOM SAMPLE DATA ───────────────────────
async function loadSample() {
  const btn = document.getElementById('btn-sample');
  const origText = btn.innerHTML;
  btn.innerHTML = '<span>⏳</span> Memuat...';
  btn.disabled = true;

  try {
    const res  = await fetch(`${API}/sample`);
    const data = await res.json();

    featureMeta.feature_names.forEach(f => {
      const el = document.getElementById(`field-${f}`);
      if (el && data[f] !== undefined) {
        el.value = data[f];
        el.classList.remove('input-error');
      }
    });
  } catch (e) {
    console.error(e);
  } finally {
    btn.innerHTML = origText;
    btn.disabled = false;
  }
}

// ── VALIDATE FORM ─────────────────────────────────
function validateForm() {
  const missing = [];
  let firstMissingEl = null;

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
      el.classList.add('input-error');

      el.addEventListener('input', function () {
        this.classList.remove('input-error');
      }, { once: true });

      if (!firstMissingEl) firstMissingEl = el;
    }
  });

  if (firstMissingEl) {
    firstMissingEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    setTimeout(() => firstMissingEl.focus(), 300);
  }

  return missing;
}

// ── RESET FORM ────────────────────────────────────
function resetForm() {
  featureMeta.feature_names.forEach(f => {
    const el = document.getElementById(`field-${f}`);
    if (el) {
      el.value = '';
      el.classList.remove('input-error');
    }
  });
  const resPanel = document.getElementById('result-panel');
  if (resPanel) resPanel.classList.add('hidden');
}

// ── HANDLE PREDICT ────────────────────────────────
async function handlePredict(e) {
  if (e) e.preventDefault();

  const missing = validateForm();
  if (missing.length > 0) {
    alert('Mohon lengkapi parameter berikut sebelum melanjutkan:\n• ' + missing.slice(0, 8).join('\n• ') + (missing.length > 8 ? `\n... dan ${missing.length - 8} lainnya` : ''));
    return;
  }

  const btnText    = document.querySelector('.btn-text');
  const btnLoading = document.querySelector('.btn-loading');
  const btnPredict = document.getElementById('btn-predict');

  btnText.classList.add('hidden');
  btnLoading.classList.remove('hidden');
  btnLoading.classList.add('flex');
  btnPredict.disabled = true;

  try {
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

    const res = await fetch(`${API}/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    const result = await res.json();

    if (!result.success) throw new Error(result.error);

    displayResult(result, formData);
  } catch (err) {
    alert('Terjadi kendala saat memproses prediksi: ' + err.message);
    console.error(err);
  } finally {
    btnText.classList.remove('hidden');
    btnLoading.classList.add('hidden');
    btnLoading.classList.remove('flex');
    btnPredict.disabled = false;
  }
}

// ── GLOBAL STATE UNTUK SIMULASI ───────────────────
let currentInputData = null;
let baselineResult   = null;
let whatIfTimeout    = null;

// ── DISPLAY RESULT ────────────────────────────────
function displayResult(result, inputData) {
  currentInputData = { ...inputData };
  baselineResult   = result;

  const panel = document.getElementById('result-panel');
  panel.classList.remove('hidden');
  panel.scrollIntoView({ behavior: 'smooth', block: 'start' });

  // Update Tanggal
  const dateEl = document.getElementById('print-date');
  if (dateEl) {
    const now = new Date();
    dateEl.textContent = now.toLocaleDateString('id-ID', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric',
      hour: '2-digit', minute: '2-digit'
    }) + ' WIB';
  }

  const info = RISK_INFO[result.prediction] || { emoji: '📊', label: result.prediction, desc: '', color: 'slate' };

  // Prediction card styling
  const predCard = document.getElementById('prediction-card');
  const predEl   = document.getElementById('pred-result');
  predEl.innerHTML = `<span>${info.emoji}</span> <span>${info.label}</span>`;
  
  // Status badges & concise summary (No text bloat)
  const urgencyBadge = result.prediction === 'Severe' 
    ? '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-200/90 text-rose-950">🚨 Prioritas Aksi Cepat</span>'
    : result.prediction === 'Moderate'
    ? '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-orange-200/90 text-orange-950">⚡ Disrupsi Nyata</span>'
    : result.prediction === 'Mild'
    ? '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-200/90 text-amber-950">⚠️ Penyesuaian Ringan</span>'
    : '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-200/90 text-emerald-950">✅ Pola Optimal</span>';

  document.getElementById('pred-desc').innerHTML = `
    <div class="flex flex-wrap items-center gap-2 my-1.5">
      ${urgencyBadge}
      <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-white/80 border border-slate-200/70 text-slate-700">⏱️ Target Evaluasi: 14 Hari Konsisten</span>
    </div>
    <p class="text-xs sm:text-sm font-medium opacity-90 leading-snug">${info.desc}</p>
  `;

  // Confidence
  const probVal = ((result.probabilities[result.prediction] || 0) * 100).toFixed(1);
  document.getElementById('pred-confidence').textContent = `${probVal}%`;

  // Apply theme class
  predCard.className = 'rounded-3xl p-6 sm:p-8 border transition-all duration-300 ' + 
    (result.prediction === 'Healthy'  ? 'pred-healthy' :
     result.prediction === 'Mild'     ? 'pred-mild' :
     result.prediction === 'Moderate' ? 'pred-moderate' : 'pred-severe');

  // Probability bars
  renderProbBars(result.probabilities);

  // SHAP chart
  renderShapChart(result.shap_top10, result.prediction);

  // Interpretation (Bahasa Manusiawi)
  renderInterpretation(result, inputData);

  // Rekomendasi Klinis Praktis (Langkah Konkret)
  renderActionPlan(result, inputData);

  // Simulator What-If
  initWhatIfSimulation(result, inputData);
}

// ── RENDER PROBABILITY CARDS ──────────────────────
function renderProbBars(probs) {
  const container = document.getElementById('prob-bars');
  const order = ['Healthy', 'Mild', 'Moderate', 'Severe'];
  
  container.innerHTML = order.map(cls => {
    const pct = ((probs[cls] || 0) * 100).toFixed(1);
    const col = PROB_COLORS[cls] || '#6366f1';
    const info = RISK_INFO[cls] || {};

    return `
      <div class="p-4 rounded-2xl border border-slate-200/80 bg-white hover:border-slate-300 shadow-2xs transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between gap-1 mb-1.5">
            <span class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
              <span>${info.emoji}</span> ${info.shortLabel || cls}
            </span>
            <span class="text-base font-extrabold text-slate-900">${pct}%</span>
          </div>
          <div class="w-full h-2.5 rounded-full bg-slate-100 overflow-hidden my-2">
            <div class="h-full rounded-full transition-all duration-700" style="width: ${pct}%; background-color: ${col};"></div>
          </div>
        </div>
        <span class="text-[11px] text-slate-400 mt-1">${cls === 'Healthy' ? 'Peluang tidur normal & prima' : 'Peluang gangguan tidur'}</span>
      </div>`;
  }).join('');
}

// ── RENDER SHAP CHART (DIVERGENT BARS) ────────────
function renderShapChart(shapTop10, predictionClass) {
  const container = document.getElementById('shap-chart');
  const maxAbs    = Math.max(...shapTop10.map(d => Math.abs(d.shap)), 0.001);

  container.innerHTML = shapTop10.map(item => {
    const isPos   = item.shap >= 0;
    const pct     = (Math.abs(item.shap) / maxAbs * 48).toFixed(1);

    const info    = FEATURE_LABELS[item.feature] || { label: item.feature, unit: '', icon: '📌' };
    const valSign = isPos ? `+${item.shap.toFixed(3)}` : item.shap.toFixed(3);
    const unitTxt = info.unit ? ` ${info.unit}` : '';

    const barBg = isPos ? 'bg-rose-500' : 'bg-sky-500';
    const valColor = isPos ? 'text-rose-600 font-bold' : 'text-sky-600 font-bold';

    const barStyle = isPos
      ? `left: 50%; width: ${pct}%;`
      : `right: 50%; width: ${pct}%;`;

    return `
      <div class="flex items-center gap-3 py-1.5 text-xs">
        <!-- Feature Name -->
        <div class="w-48 sm:w-64 shrink-0 truncate text-slate-700 font-semibold" title="${info.label}: ${item.value}${unitTxt}">
          ${info.icon} ${info.label}
          <span class="text-[11px] text-slate-400 font-normal font-mono">(${item.value}${unitTxt})</span>
        </div>

        <!-- Divergent Bar Track -->
        <div class="relative flex-1 h-6 bg-white border border-slate-200 rounded-lg overflow-hidden shadow-2xs">
          <!-- Center Zero Line -->
          <div class="absolute left-1/2 top-0 bottom-0 w-0.5 bg-slate-300 z-10"></div>
          <!-- Bar -->
          <div class="absolute top-1 bottom-1 rounded-sm transition-all duration-500 ${barBg}" style="${barStyle}"></div>
        </div>

        <!-- SHAP Value -->
        <div class="w-16 shrink-0 text-right font-mono text-[11px] ${valColor}">
          ${valSign}
        </div>
      </div>`;
  }).join('');
}

// ── RENDER INTERPRETATION (GLANCEABLE 3-CARD MATRIX) ──
function renderInterpretation(result, inputData) {
  const box    = document.getElementById('interpretation-box');
  const shap   = result.shap_top10;
  const topPos = shap.filter(d => d.shap > 0).slice(0, 3);
  const topNeg = shap.filter(d => d.shap < 0).slice(0, 2);

  // Pemicu Utama Chips
  const posChips = topPos.length > 0 ? topPos.map(d => {
    const info = FEATURE_LABELS[d.feature] || { label: d.feature, unit: '', icon: '⚠️' };
    const unit = info.unit ? ` ${info.unit}` : '';
    return `
      <div class="flex items-center justify-between p-2 rounded-lg bg-rose-50 border border-rose-200/80 text-xs">
        <span class="font-semibold text-rose-950 flex items-center gap-1.5 truncate">
          <span>${info.icon}</span> ${info.label}
        </span>
        <span class="font-mono font-bold text-rose-700 bg-white px-2 py-0.5 rounded shadow-2xs shrink-0">
          ${d.value}${unit} (+${d.shap.toFixed(2)})
        </span>
      </div>`;
  }).join('') : '<p class="text-xs text-slate-400 italic">Tidak terdeteksi pemicu risiko signifikan.</p>';

  // Modal Pelindung Chips
  const negChips = topNeg.length > 0 ? topNeg.map(d => {
    const info = FEATURE_LABELS[d.feature] || { label: d.feature, unit: '', icon: '🛡️' };
    const unit = info.unit ? ` ${info.unit}` : '';
    return `
      <div class="flex items-center justify-between p-2 rounded-lg bg-sky-50 border border-sky-200/80 text-xs">
        <span class="font-semibold text-sky-950 flex items-center gap-1.5 truncate">
          <span>${info.icon}</span> ${info.label}
        </span>
        <span class="font-mono font-bold text-sky-700 bg-white px-2 py-0.5 rounded shadow-2xs shrink-0">
          ${d.value}${unit} (${d.shap.toFixed(2)})
        </span>
      </div>`;
  }).join('') : '<p class="text-xs text-slate-400 italic">Pertahankan kebiasaan positif harian.</p>';

  // Fokus Aksi Tercepat (1 kalimat terarah dari fitur ranking #1)
  let focusAction = 'Pertahankan jadwal bangun dan tidur yang konsisten.';
  if (topPos.length > 0) {
    const topFeat = topPos[0].feature;
    if (topFeat === 'screen_time_before_bed_mins') {
      focusAction = 'Pangkas scrolling HP di kasur malam ini; jauhkan gawai 45 mnt sebelum jam tidur.';
    } else if (topFeat === 'caffeine_mg_before_bed') {
      focusAction = 'Hentikan asupan kafein (kopi/teh/soda) setelah pukul 16.00 sore.';
    } else if (topFeat === 'sleep_duration_hrs') {
      focusAction = 'Majukan jam naik kasur 30–45 menit lebih awal untuk mencukupi defisit tidur.';
    } else if (topFeat === 'stress_score') {
      focusAction = 'Lakukan dekompresi pikiran: catat to-do esok hari dan latihan pernapasan rileks 4-7-8.';
    } else if (topFeat === 'wake_episodes_per_night') {
      focusAction = 'Batasi minum air 1 jam sebelum tidur dan atur suhu ruangan sejuk (20–22°C).';
    } else {
      const topInfo = FEATURE_LABELS[topFeat] || { label: topFeat };
      focusAction = `Prioritaskan penyesuaian pada parameter ${topInfo.label} untuk menurunkan risiko.`;
    }
  }

  box.innerHTML = `
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5">
      <!-- Card 1: Pemicu Terbesar -->
      <div class="p-3.5 rounded-2xl bg-white border border-rose-200 shadow-2xs space-y-2.5">
        <div class="flex items-center justify-between pb-1.5 border-b border-rose-100">
          <span class="text-xs font-bold text-rose-900 flex items-center gap-1">
            <span>🚨</span> Pemicu Utama Beban
          </span>
          <span class="text-[10px] font-extrabold bg-rose-100 text-rose-700 px-1.5 py-0.5 rounded">+Risiko</span>
        </div>
        <div class="space-y-1.5">${posChips}</div>
      </div>

      <!-- Card 2: Modal Pelindung -->
      <div class="p-3.5 rounded-2xl bg-white border border-sky-200 shadow-2xs space-y-2.5">
        <div class="flex items-center justify-between pb-1.5 border-b border-sky-100">
          <span class="text-xs font-bold text-sky-900 flex items-center gap-1">
            <span>🛡️</span> Modal Pelindung Tubuh
          </span>
          <span class="text-[10px] font-extrabold bg-sky-100 text-sky-700 px-1.5 py-0.5 rounded">-Risiko</span>
        </div>
        <div class="space-y-1.5">${negChips}</div>
      </div>

      <!-- Card 3: Prioritas Cepat -->
      <div class="p-3.5 rounded-2xl bg-indigo-50/60 border border-indigo-200 shadow-2xs flex flex-col justify-between space-y-2">
        <div>
          <div class="flex items-center justify-between pb-1.5 border-b border-indigo-100">
            <span class="text-xs font-bold text-indigo-900 flex items-center gap-1">
              <span>🎯</span> Prioritas Tindakan Malam Ini
            </span>
            <span class="text-[10px] font-extrabold bg-indigo-100 text-indigo-700 px-1.5 py-0.5 rounded">Aksi Cepat</span>
          </div>
          <p class="text-xs text-indigo-950 font-medium leading-relaxed mt-2">
            ${focusAction}
          </p>
        </div>
        <div class="pt-2 border-t border-indigo-100 text-[10px] text-indigo-700/80 font-medium flex items-center gap-1">
          <span>💡</span> Nilai SHAP dihitung adil via Game Theory Shapley.
        </div>
      </div>
    </div>`;
}

// ── DATABASE REKOMENDASI TERSIMPEL & TEPAT SASARAN ─
const HUMAN_ADVICE = {
  screen_time_before_bed_mins: (val) => ({
    problem: 'Paparan Layar HP di Kasur',
    icon: '📱',
    current: `${val} menit`,
    target: '≤ 30 menit',
    action: 'Letakkan ponsel di meja luar jangkauan kasur pada 21.30 WIB.',
    timing: '45 mnt sebelum kasur',
    benefit: 'Melatonin rilis alami & tidur lebih nyenyak'
  }),
  caffeine_mg_before_bed: (val) => ({
    problem: 'Konsumsi Kafein Sore/Malam',
    icon: '☕',
    current: `${val} mg`,
    target: '0 mg setelah 16.00',
    action: 'Ganti kopi/teh pekat sore hari dengan air mineral atau teh chamomile.',
    timing: 'Cut-off 16.00 WIB',
    benefit: 'Mencegah kerusakan fase Deep Sleep'
  }),
  sleep_duration_hrs: (val) => ({
    problem: 'Durasi Tidur Masih Kurang',
    icon: '⏱️',
    current: `${val} jam`,
    target: '7.0 – 8.0 jam',
    action: 'Majukan jam rebahan 30 menit lebih awal, jam bangun tetap konsisten.',
    timing: 'Mulai malam ini',
    benefit: 'Memulihkan energi & ketajaman kognitif'
  }),
  stress_score: (val) => ({
    problem: 'Beban Pikiran & Stres Harian',
    icon: '🧠',
    current: `${val}/10`,
    target: '≤ 4.0/10',
    action: 'Tuliskan daftar tugas esok hari di kertas & terapkan teknik napas 4-7-8.',
    timing: 'Saat di tempat tidur',
    benefit: 'Menurunkan denyut nadi & kortisol'
  }),
  sleep_latency_mins: (val) => ({
    problem: 'Lama Rebahan Sebelum Terlelap',
    icon: '⏳',
    current: `${val} menit`,
    target: '15 – 20 menit',
    action: 'Aturan 20 Menit: Jika 20 mnt belum tidur, duduk di lampu temaram.',
    timing: 'Rebahan > 20 mnt',
    benefit: 'Mengikis asosiasi cemas di tempat tidur'
  }),
  wake_episodes_per_night: (val) => ({
    problem: 'Terbangun Tengah Malam',
    icon: '👀',
    current: `${val} kali`,
    target: '≤ 1 kali',
    action: 'Stop minum air 1 jam sebelum tidur dan pasang suhu kamar sejuk 20–22°C.',
    timing: '1 jam sebelum tidur',
    benefit: 'Siklus tidur lelap tanpa terputus'
  }),
  alcohol_units_before_bed: (val) => ({
    problem: 'Konsumsi Alkohol Malam',
    icon: '🍷',
    current: `${val} unit`,
    target: '0 unit',
    action: 'Hindari alkohol sebelum tidur; gunakan relaksasi audio alami.',
    timing: 'Malam hari',
    benefit: 'Fase tidur REM stabil & bangun segar'
  }),
  work_hours_that_day: (val) => ({
    problem: 'Jam Kerja/Lembur Panjang',
    icon: '💼',
    current: `${val} jam`,
    target: '≤ 8.5 jam/hari',
    action: 'Beri jeda minimal 60 menit antara tutup laptop dengan jam kasur.',
    timing: 'Selesai kerja',
    benefit: 'Mendinginkan sistem saraf simpatik'
  })
};

// ── RENDER REKOMENDASI TINDAK LANJUT (VISUAL, ACTIONABLE, GLANCEABLE) ─
function renderActionPlan(result, inputData) {
  const container = document.getElementById('action-plan-cards');
  const shap = result.shap_top10;
  const riskFactors = shap.filter(d => d.shap > 0);

  let html = '';

  // 1. TIMELINE AKSI 3 WAKTU (HORIZONTAL STRIP - BUKAN PARAGRAF PANJANG)
  html += `
    <div class="p-5 sm:p-6 rounded-3xl bg-gradient-to-br from-emerald-50/70 via-white to-teal-50/40 border border-emerald-200/80 shadow-2xs space-y-4">
      <div class="flex items-center justify-between gap-3">
        <div class="flex items-center gap-2">
          <span class="w-8 h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center text-sm font-bold shadow-2xs">🌟</span>
          <div>
            <h4 class="text-sm sm:text-base font-extrabold text-slate-900">Jadwal Aksi Ringkas: 3 Ritme Menuju Tidur Lelap</h4>
            <p class="text-[11px] text-slate-500">Terapkan jadwal waktu terarah ini mulai malam ini</p>
          </div>
        </div>
        <span class="text-[10px] font-extrabold text-emerald-800 bg-emerald-100 px-2.5 py-1 rounded-full">3 Ritme Sehat</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <!-- Sore Hari -->
        <div class="p-3.5 rounded-2xl bg-white border border-emerald-100/90 shadow-2xs space-y-2">
          <div class="flex items-center justify-between text-xs font-bold text-amber-700">
            <span class="flex items-center gap-1.5"><span>🌅</span> Sore (Maks 16.00)</span>
            <span class="text-[10px] bg-amber-50 text-amber-700 px-1.5 py-0.5 rounded border border-amber-200">Fase 1</span>
          </div>
          <div class="space-y-1 text-xs">
            <div class="flex items-center gap-1.5 font-semibold text-slate-800">
              <span class="text-emerald-600">✓</span> Cut-off kafein / kopi sore
            </div>
            <div class="flex items-center gap-1.5 text-slate-600 text-[11px]">
              <span class="text-sky-500">✓</span> Jalan santai 15 menit
            </div>
          </div>
        </div>

        <!-- 1 Jam Sebelum Kasur -->
        <div class="p-3.5 rounded-2xl bg-white border border-emerald-100/90 shadow-2xs space-y-2">
          <div class="flex items-center justify-between text-xs font-bold text-indigo-700">
            <span class="flex items-center gap-1.5"><span>🌙</span> Malam (21.30)</span>
            <span class="text-[10px] bg-indigo-50 text-indigo-700 px-1.5 py-0.5 rounded border border-indigo-200">Fase 2</span>
          </div>
          <div class="space-y-1 text-xs">
            <div class="flex items-center gap-1.5 font-semibold text-slate-800">
              <span class="text-emerald-600">✓</span> Jauhkan HP dari area kasur
            </div>
            <div class="flex items-center gap-1.5 text-slate-600 text-[11px]">
              <span class="text-sky-500">✓</span> Nyalakan lampu temaram hangat
            </div>
          </div>
        </div>

        <!-- Di Kasur -->
        <div class="p-3.5 rounded-2xl bg-white border border-emerald-100/90 shadow-2xs space-y-2">
          <div class="flex items-center justify-between text-xs font-bold text-sky-700">
            <span class="flex items-center gap-1.5"><span>🛏️</span> Di Kasur (22.30)</span>
            <span class="text-[10px] bg-sky-50 text-sky-700 px-1.5 py-0.5 rounded border border-sky-200">Fase 3</span>
          </div>
          <div class="space-y-1 text-xs">
            <div class="flex items-center gap-1.5 font-semibold text-slate-800">
              <span class="text-emerald-600">✓</span> Aturan 20 Menit jika terjaga
            </div>
            <div class="flex items-center gap-1.5 text-slate-600 text-[11px]">
              <span class="text-sky-500">✓</span> Napas rileks 4-7-8 (4 putaran)
            </div>
          </div>
        </div>
      </div>
    </div>`;

  // 2. KARTU TARGET SPESIFIK KEBIASAAN (MAKS 2 KARTU PALING DOMINAN)
  html += `
    <div class="space-y-3 pt-1">
      <div class="flex items-center justify-between">
        <h4 class="text-sm font-extrabold text-slate-900 flex items-center gap-2">
          <span>🎯</span> Target Perbaikan Spesifik (Berdasarkan Nilai SHAP Anda)
        </h4>
        <span class="text-[11px] font-semibold text-slate-400">Paling Berdampak</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">`;

  let renderedCount = 0;
  for (const factor of riskFactors) {
    if (renderedCount >= 2) break; // Cukup 2 kartu paling berdampak agar tidak malas baca!
    const rule = HUMAN_ADVICE[factor.feature];
    if (rule) {
      const adv = rule(factor.value);
      html += `
        <div class="p-4 sm:p-5 rounded-2xl bg-white border border-slate-200/90 shadow-2xs hover:border-sky-300 transition-all flex flex-col justify-between space-y-3">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-slate-100">
              <span class="font-bold text-xs sm:text-sm text-slate-900 flex items-center gap-1.5">
                <span>${adv.icon}</span> ${adv.problem}
              </span>
              <span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-rose-100 text-rose-700">Fokus #${renderedCount + 1}</span>
            </div>

            <!-- Visual Comparison Pill -->
            <div class="flex items-center justify-between gap-2 p-2.5 my-2.5 bg-slate-50 rounded-xl border border-slate-200/60 text-xs">
              <div class="text-center flex-1">
                <span class="block text-[10px] text-slate-400 font-semibold uppercase">Saat Ini</span>
                <span class="font-extrabold text-rose-600 font-mono">${adv.current}</span>
              </div>
              <div class="text-slate-300 font-bold">➔</div>
              <div class="text-center flex-1">
                <span class="block text-[10px] text-emerald-600 font-semibold uppercase">Target Ideal</span>
                <span class="font-extrabold text-emerald-700 font-mono bg-emerald-50 px-2 py-0.5 rounded">${adv.target}</span>
              </div>
            </div>

            <!-- 1-Line Concrete Step -->
            <div class="text-xs text-slate-700 leading-snug">
              <strong>⚡ Aksi:</strong> ${adv.action}
            </div>
          </div>

          <!-- Bottom Benefit Chip -->
          <div class="flex items-center justify-between text-[11px] pt-2 border-t border-slate-100 text-slate-500">
            <span class="text-emerald-700 font-semibold">🌱 ${adv.benefit}</span>
            <span class="text-slate-400 font-mono">${adv.timing}</span>
          </div>
        </div>`;
      renderedCount++;
    }
  }

  if (renderedCount === 0) {
    html += `
      <div class="col-span-2 p-5 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-center space-y-1">
        <span class="text-2xl">🎉</span>
        <h5 class="font-extrabold text-sm">Pola Hidup Anda Sudah Sangat Baik!</h5>
        <p class="text-xs text-emerald-700">Tidak ada kebiasaan buruk yang dominan. Pertahankan jadwal tidur saat ini.</p>
      </div>`;
  }

  html += `
      </div>
    </div>`;

  // 3. CHECKLIST KOMITMEN INTERAKTIF DENGAN COUNTER & 1-KLIK SALIN
  html += `
    <div class="p-5 rounded-2xl bg-white border border-indigo-100 shadow-2xs space-y-3.5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2 border-b border-slate-100">
        <div>
          <h4 class="text-xs sm:text-sm font-bold text-slate-900 flex items-center gap-1.5">
            <span>✅</span> Komitmen Aksi Cepat Malam Ini
          </h4>
          <p class="text-[11px] text-slate-400">Pilih 2–3 target realistis untuk malam ini:</p>
        </div>
        <span id="checklist-counter" class="text-[11px] font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-lg self-start sm:self-auto">
          2 dari 4 terpilih
        </span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs" id="checklist-items">
        <label class="action-item flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50 transition-all">
          <input type="checkbox" class="action-check" checked onchange="updateChecklistCounter()" />
          <span class="text-slate-800 font-medium truncate">Jauhkan HP 45 mnt sebelum jam tidur</span>
        </label>
        <label class="action-item flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50 transition-all">
          <input type="checkbox" class="action-check" checked onchange="updateChecklistCounter()" />
          <span class="text-slate-800 font-medium truncate">Stop kafein (kopi/teh) setelah pukul 16.00</span>
        </label>
        <label class="action-item flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50 transition-all">
          <input type="checkbox" class="action-check" onchange="updateChecklistCounter()" />
          <span class="text-slate-800 font-medium truncate">Nyalakan lampu temaram kuning hangat di kamar</span>
        </label>
        <label class="action-item flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 cursor-pointer hover:bg-slate-50 transition-all">
          <input type="checkbox" class="action-check" onchange="updateChecklistCounter()" />
          <span class="text-slate-800 font-medium truncate">Latihan napas rileks 4-7-8 sebanyak 4 putaran</span>
        </label>
      </div>
    </div>`;

  // 4. RED FLAGS RINGKAS (CHIPS - BUKAN PARAGRAF PANJANG)
  html += `
    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
      <div class="flex items-center justify-between text-xs font-bold text-slate-800">
        <span class="flex items-center gap-1.5"><span>🏥</span> Kapan Perlu Konsultasi Dokter Spesialis?</span>
        <span class="text-[10px] text-slate-400 font-normal">Tanda Waspada</span>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2 text-[11px] text-slate-700">
        <div class="p-2 bg-white rounded-lg border border-slate-200/70 flex items-center gap-1.5">
          <span>⚠️</span> Mengorok keras & tersedak
        </div>
        <div class="p-2 bg-white rounded-lg border border-slate-200/70 flex items-center gap-1.5">
          <span>⚠️</span> Tertidur saat kerja / nyetir
        </div>
        <div class="p-2 bg-white rounded-lg border border-slate-200/70 flex items-center gap-1.5">
          <span>⚠️</span> Insomnia menetap > 3 minggu
        </div>
        <div class="p-2 bg-white rounded-lg border border-slate-200/70 flex items-center gap-1.5">
          <span>⚠️</span> Ketergantungan obat tidur kimia
        </div>
      </div>
    </div>`;

  container.innerHTML = html;
}

// ── UPDATE CHECKLIST COUNTER ──────────────────────
function updateChecklistCounter() {
  const total = document.querySelectorAll('#checklist-items .action-check').length;
  const checked = document.querySelectorAll('#checklist-items .action-check:checked').length;
  const counterEl = document.getElementById('checklist-counter');
  if (counterEl) {
    counterEl.textContent = `${checked} dari ${total} terpilih`;
  }
}
window.updateChecklistCounter = updateChecklistCounter;

// ── WHAT-IF SIMULATION SETUP ──────────────────────
const MODIFIABLE_CONFIG = [
  { key: 'screen_time_before_bed_mins', label: 'Main HP Sebelum Tidur', min: 0, max: 180, step: 5, unit: 'menit', icon: '📱' },
  { key: 'caffeine_mg_before_bed', label: 'Kafein Sore/Malam', min: 0, max: 300, step: 10, unit: 'mg', icon: '☕' },
  { key: 'sleep_duration_hrs', label: 'Durasi Tidur Harian', min: 4.0, max: 9.5, step: 0.25, unit: 'jam', icon: '⏱️' },
  { key: 'stress_score', label: 'Tingkat Beban Stres', min: 1.0, max: 10.0, step: 0.5, unit: '/10', icon: '⚡' },
  { key: 'alcohol_units_before_bed', label: 'Konsumsi Alkohol Malam', min: 0, max: 5, step: 0.5, unit: 'unit', icon: '🍷' }
];

function initWhatIfSimulation(result, inputData) {
  const container = document.getElementById('whatif-sliders');
  const beforeBadge = document.getElementById('whatif-before-badge');
  const beforeProb  = document.getElementById('whatif-before-prob');
  const afterBadge  = document.getElementById('whatif-after-badge');
  const afterProb   = document.getElementById('whatif-after-prob');
  const deltaDesc   = document.getElementById('whatif-delta-desc');

  const beforeCls = result.prediction;
  const beforePct = ((result.probabilities[beforeCls] || 0) * 100).toFixed(1);
  const healthyPct= ((result.probabilities['Healthy'] || 0) * 100).toFixed(1);

  beforeBadge.textContent = RISK_INFO[beforeCls] ? RISK_INFO[beforeCls].shortLabel : beforeCls;
  beforeBadge.style.backgroundColor = PROB_COLORS[beforeCls];
  beforeProb.textContent  = `Peluang: ${beforePct}% (Sehat: ${healthyPct}%)`;

  afterBadge.textContent  = beforeBadge.textContent;
  afterBadge.style.backgroundColor = PROB_COLORS[beforeCls];
  afterProb.textContent   = beforeProb.textContent;
  deltaDesc.innerHTML     = 'Coba geser salah satu slider di sebelah kiri untuk melihat bagaimana perubahan kebiasaan langsung menaikkan peluang kesembuhan tidur Anda!';

  // Render Sliders
  let html = '';
  MODIFIABLE_CONFIG.forEach(cfg => {
    const curVal = inputData[cfg.key] !== undefined ? inputData[cfg.key] : cfg.min;
    html += `
      <div class="space-y-1.5">
        <div class="flex items-center justify-between text-xs font-semibold">
          <span class="text-slate-800 flex items-center gap-1.5"><span>${cfg.icon}</span> ${cfg.label}</span>
          <span class="font-mono text-sky-700 bg-sky-50 px-2 py-0.5 rounded-md border border-sky-200/80" id="val-${cfg.key}">${curVal} ${cfg.unit}</span>
        </div>
        <input type="range" id="slider-${cfg.key}"
          min="${cfg.min}" max="${cfg.max}" step="${cfg.step}" value="${curVal}"
          data-key="${cfg.key}" data-unit="${cfg.unit}" />
      </div>`;
  });

  container.innerHTML = html;

  // Event Listeners on Sliders
  MODIFIABLE_CONFIG.forEach(cfg => {
    const slider = document.getElementById(`slider-${cfg.key}`);
    slider.addEventListener('input', function () {
      document.getElementById(`val-${cfg.key}`).textContent = `${this.value} ${cfg.unit}`;

      clearTimeout(whatIfTimeout);
      whatIfTimeout = setTimeout(triggerWhatIfSimulation, 250);
    });
  });
}

// ── TRIGGER WHAT-IF SIMULATION API ───────────────
async function triggerWhatIfSimulation() {
  if (!currentInputData) return;

  const simData = { ...currentInputData };
  MODIFIABLE_CONFIG.forEach(cfg => {
    const slider = document.getElementById(`slider-${cfg.key}`);
    if (slider) simData[cfg.key] = parseFloat(slider.value);
  });

  try {
    const res = await fetch(`${API}/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(simData)
    });
    const simResult = await res.json();
    if (!simResult.success) return;

    const afterBadge = document.getElementById('whatif-after-badge');
    const afterProb  = document.getElementById('whatif-after-prob');
    const deltaDesc  = document.getElementById('whatif-delta-desc');

    const afterCls = simResult.prediction;
    const afterPct = ((simResult.probabilities[afterCls] || 0) * 100).toFixed(1);
    const newHealthyPct = ((simResult.probabilities['Healthy'] || 0) * 100).toFixed(1);
    const oldHealthyPct = ((baselineResult.probabilities['Healthy'] || 0) * 100).toFixed(1);

    afterBadge.textContent = RISK_INFO[afterCls] ? RISK_INFO[afterCls].shortLabel : afterCls;
    afterBadge.style.backgroundColor = PROB_COLORS[afterCls];
    afterProb.textContent  = `Peluang: ${afterPct}% (Sehat: ${newHealthyPct}%)`;

    const diff = (parseFloat(newHealthyPct) - parseFloat(oldHealthyPct)).toFixed(1);
    const diffSign = diff > 0 ? `+${diff}%` : `${diff}%`;

    if (diff > 0) {
      deltaDesc.innerHTML = `
        <span class="text-emerald-700 font-extrabold flex items-center gap-1 mb-1">
          <span>🎉</span> Kabar Baik: Peluang Tidur Sehat Meningkat!
        </span>
        Peluang kategori Sehat Anda melonjak sebesar <strong class="text-emerald-800 text-sm font-black underline">${diffSign}</strong> (dari ${oldHealthyPct}% menjadi ${newHealthyPct}%). Perubahan kebiasaan ini terbukti sangat efektif menekan risiko insomnia Anda.`;
    } else if (diff < 0) {
      deltaDesc.innerHTML = `
        <span class="text-rose-700 font-extrabold flex items-center gap-1 mb-1">
          <span>⚠️</span> Perhatian: Beban Tidur Meningkat!
        </span>
        Peluang kategori Sehat menurun sebesar <strong>${diffSign}</strong>. Mengubah parameter ke arah ini memperberat beban tidur Anda.`;
    } else {
      deltaDesc.innerHTML = `Pergeseran angka saat ini belum mengubah peluang kategori Sehat Anda (${newHealthyPct}%). Coba ubah durasi tidur atau kurangi waktu main HP lebih banyak.`;
    }
  } catch (err) {
    console.error(err);
  }
}

// ── RESET WHAT-IF SLIDERS ────────────────────────
function handleResetWhatIf() {
  if (!currentInputData || !baselineResult) return;
  initWhatIfSimulation(baselineResult, currentInputData);
}

// ── COPY PLAN ACTION TO CLIPBOARD ────────────────
function handleCopyPlan() {
  if (!baselineResult) return;

  const checkedLabels = [];
  document.querySelectorAll('#checklist-items .action-check:checked').forEach(chk => {
    const text = chk.closest('label').querySelector('span').textContent;
    checkedLabels.push('• ' + text);
  });

  const planText = 
`📋 RENCANA AKSI TIDUR NYENYAK SAYA (SleepRisk AI)
--------------------------------------------------
Status Hasil Skrining: ${baselineResult.prediction}
Kepastian Model: ${((baselineResult.probabilities[baselineResult.prediction] || 0) * 100).toFixed(1)}%

🌟 3 Langkah Mudah Mulai Malam Ini:
1. Sore Hari: Hentikan kafein 6 jam sebelum tidur & jalan santai 15 menit.
2. 1 Jam Sebelum Kasur: Jauhkan HP & gunakan lampu temaram.
3. Di Kasur: Aturan 20 menit (jika belum ngantuk, bangun dan duduk santai).

✅ Komitmen Aksi yang Saya Pilih:
${checkedLabels.join('\n')}

Catatan: Skrining awal berbasis AI CatBoost + SHAP. Konsultasikan ke dokter jika gangguan tidur berlanjut >3 minggu.`;

  navigator.clipboard.writeText(planText).then(() => {
    const btn = document.getElementById('btn-copy-plan');
    const orig = btn.innerHTML;
    btn.innerHTML = '<span>✅</span> Tersalin!';
    btn.classList.add('bg-emerald-100', 'text-emerald-800');
    setTimeout(() => {
      btn.innerHTML = orig;
      btn.classList.remove('bg-emerald-100', 'text-emerald-800');
    }, 2000);
  }).catch(() => {
    alert('Gagal menyalin otomatis. Silakan salin manual.');
  });
}

// ── PRINT REPORT ─────────────────────────────────
function handlePrintReport() {
  window.print();
}
