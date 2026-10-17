# tools/KREASII.py
import streamlit as st
import math
import random
import html

# ============================================================
# 🎨 SUPER PREMIUM UI — KREASII POISSON EDITION
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #222222;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(112,28,35,0.06) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(217,195,163,0.18) 0%, transparent 50%),
        linear-gradient(180deg, #f4f0eb 0%, #efe8df 100%);
    background-attachment: fixed;
}

.kreasii-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 3em !important;
    letter-spacing: 1px;
    margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
    display: block;
}
.kreasii-title::after {
    content: '';
    display: block;
    width: 90px;
    height: 3px;
    margin: 14px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent);
    border-radius: 3px;
}
.kreasii-subtitle {
    text-align: center;
    font-family: 'Inter', sans-serif;
    color: #6b5a52;
    font-weight: 500;
    font-size: 0.95em !important;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 30px;
    margin-top: 8px;
}

.kreasi-card {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 30px 34px;
    border-radius: 20px;
    box-shadow:
        0 1px 0 rgba(255,255,255,0.9) inset,
        0 10px 30px rgba(112,28,35,0.08),
        0 2px 8px rgba(112,28,35,0.04);
    border: 1px solid rgba(217,195,163,0.55);
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}
.kreasi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.kreasi-card::after {
    content: '';
    position: absolute;
    top: -30px; right: -30px;
    width: 140px; height: 140px;
    background: radial-gradient(circle, rgba(217,195,163,0.28) 0%, transparent 70%);
    pointer-events: none;
}
.kreasi-card .card-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: #701c23;
    margin-bottom: 4px;
}
.kreasi-card .card-sub {
    display: inline-block;
    padding: 4px 14px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    border-radius: 999px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: #f4f0eb;
    box-shadow: 0 3px 10px rgba(112,28,35,0.28);
    margin-bottom: 16px;
}
.kreasi-card .card-sub.gold {
    background: linear-gradient(135deg, #b8912e 0%, #e8c874 50%, #b8912e 100%);
    color: #4e1318;
}
.kreasi-card .card-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d9c3a3, transparent);
    margin: 4px 0 18px 0;
}
.kreasi-card .card-body {
    font-size: 14px;
    line-height: 1.8;
    color: #3a2f2b;
}
.kreasi-card .card-body b {
    color: #701c23;
}

/* Timeline visualization */
.timeline-wrap {
    margin: 20px 0;
    padding: 24px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(112,28,35,0.04) 0%, rgba(217,195,163,0.10) 100%);
    border: 1px solid rgba(217,195,163,0.45);
}
.timeline-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #701c23;
    margin-bottom: 14px;
}
.timeline-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}
.timeline-cell {
    width: 26px;
    height: 26px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 700;
    transition: transform 0.2s ease;
}
.timeline-cell:hover {
    transform: scale(1.15);
}
.cell-empty {
    background: rgba(217,195,163,0.20);
    color: #a89790;
}
.cell-event {
    background: linear-gradient(135deg, #701c23, #a8323d);
    color: #ffffff;
    box-shadow: 0 2px 6px rgba(112,28,35,0.35);
}

/* Stats grid */
.stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 8px;
}
.stat-item {
    padding: 16px 20px;
    border-radius: 14px;
    background: linear-gradient(135deg, rgba(217,195,163,0.15) 0%, rgba(217,195,163,0.08) 100%);
    border-left: 3px solid #701c23;
    transition: background 0.3s ease;
}
.stat-item:hover {
    background: linear-gradient(135deg, rgba(217,195,163,0.28) 0%, rgba(217,195,163,0.15) 100%);
}
.stat-label {
    display: block;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    font-size: 9.5px;
    margin-bottom: 4px;
}
.stat-value {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-weight: 700;
    color: #4e1318;
    line-height: 1.1;
}

/* Result panel */
.result-panel {
    background: linear-gradient(135deg, #701c23 0%, #4e1318 60%, #2d0a0d 100%);
    padding: 30px 34px;
    border-radius: 20px;
    color: #ffffff;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 15px 40px rgba(112,28,35,0.30);
}
.result-panel::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(217,195,163,0.15) 1px, transparent 1px);
    background-size: 14px 14px;
    opacity: 0.5;
    pointer-events: none;
}
.result-panel .rp-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #d9c3a3;
    margin-bottom: 6px;
    position: relative;
}
.result-panel .rp-big {
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 6px;
    position: relative;
}
.result-panel .rp-desc {
    font-size: 13px;
    line-height: 1.6;
    color: rgba(244,240,235,0.9);
    position: relative;
}

/* Formula box */
.formula-box {
    margin: 16px 0;
    padding: 20px 24px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(112,28,35,0.05) 0%, rgba(217,195,163,0.10) 100%);
    border: 1px dashed rgba(112,28,35,0.35);
    text-align: center;
}
.formula-box .formula {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-style: italic;
    color: #701c23;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 26px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    font-size: 14px !important;
    box-shadow: 0 6px 18px rgba(112,28,35,0.35) !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
    margin-top: 10px !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 24px rgba(112,28,35,0.5) !important;
    background: linear-gradient(135deg, #a8323d 0%, #701c23 100%) !important;
}

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #f4f0eb; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #701c23, #a8323d);
    border-radius: 10px;
    border: 2px solid #f4f0eb;
}

.block-container { padding-top: 2rem !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# 🧮 FUNGSI POISSON
# ============================================================
def poisson_pmf(k, lam):
    if k < 0:
        return 0.0
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def poisson_cdf(k, lam):
    return sum(poisson_pmf(i, lam) for i in range(k + 1))


def simulate_poisson_events(lam, total_periods, seed=None):
    """Simulasi event Poisson menggunakan metode inverse transform."""
    if seed is not None:
        random.seed(seed)
    events = []
    for _ in range(total_periods):
        # Knuth algorithm untuk sampling dari distribusi Poisson
        L = math.exp(-lam)
        k = 0
        p = 1.0
        while True:
            k += 1
            p *= random.random()
            if p <= L:
                break
        events.append(k - 1)
    return events


# ============================================================
# HEADER
# ============================================================
st.markdown("<h1 class='kreasii-title'>KREASII POISSON</h1>", unsafe_allow_html=True)
st.markdown("<p class='kreasii-subtitle'>✦ Simulasi Kejadian Langka & Simulasi Monte Carlo ✦</p>", unsafe_allow_html=True)


# ============================================================
# SECTION 1: PENJELASAN
# ============================================================
st.markdown("""
<div class="kreasi-card">
    <div class="card-title">Simulasi Monte Carlo dengan Poisson</div>
    <div class="card-sub">Teori & Praktik</div>
    <div class="card-divider"></div>
    <div class="card-body">
        <b>Simulasi Monte Carlo</b> adalah teknik untuk memodelkan sistem yang melibatkan
        unsur acak dengan cara menjalankan eksperimen berulang-ulang menggunakan bilangan random.
        Dalam konteks Poisson, kita bisa mensimulasikan <b>berapa kali suatu kejadian langka terjadi</b>
        (misal gempa kecil, kecelakaan, atau kedatangan pelanggan) dalam periode waktu tertentu.
        <br><br>
        Di bawah ini kamu dapat mengatur <b>λ (laju rata-rata)</b> dan <b>jumlah periode simulasi</b>,
        lalu melihat hasilnya dalam bentuk visualisasi timeline dan statistik.
    </div>
    <div class="formula-box">
        <div class="formula">X ~ Poisson(λ) → P(X = k) = (λ<sup>k</sup> · e<sup>−λ</sup>) / k!</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SECTION 2: KONTROL SIMULASI
# ============================================================
st.markdown("""
<div class="kreasi-card">
    <div class="card-title">Atur Parameter Simulasi</div>
    <div class="card-sub gold">Setup</div>
    <div class="card-divider"></div>
    <div class="card-body">
        Tentukan laju rata-rata kejadian (λ) dan jumlah periode simulasi yang ingin dijalankan.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    lam_sim = st.slider("λ — rata-rata kejadian per periode", min_value=0.5, max_value=15.0, value=4.0, step=0.5)
with col2:
    n_periods = st.slider("Jumlah periode simulasi", min_value=10, max_value=100, value=40, step=10)

seed_choice = st.checkbox("Gunakan seed acak (reproducible)", value=True)


# ============================================================
# SECTION 3: JALANKAN SIMULASI
# ============================================================
if st.button("🎲 Jalankan Simulasi", use_container_width=True):
    seed = 42 if seed_choice else None
    events = simulate_poisson_events(lam_sim, n_periods, seed=seed)

    total_events = sum(events)
    rata_empiris = total_events / n_periods
    max_event = max(events)
    periode_kosong = events.count(0)

    # Panel utama
    st.markdown(f"""
    <div class="result-panel">
        <div class="rp-label">Hasil Simulasi Monte Carlo</div>
        <div class="rp-big">{rata_empiris:.2f}</div>
        <div class="rp-desc">
            Rata-rata kejadian per periode dari simulasi (<b>{n_periods} periode</b>)
            dengan <b>λ = {lam_sim}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Statistik
    st.markdown(f"""
    <div class="kreasi-card">
        <div class="card-title">Statistik Hasil</div>
        <div class="card-sub gold">Empiris vs Teori</div>
        <div class="card-divider"></div>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-label">Total Kejadian</span>
                <div class="stat-value">{total_events}</div>
            </div>
            <div class="stat-item">
                <span class="stat-label">Rata-rata Empiris</span>
                <div class="stat-value">{rata_empiris:.2f}</div>
            </div>
            <div class="stat-item">
                <span class="stat-label">Kejadian Maksimum</span>
                <div class="stat-value">{max_event}</div>
            </div>
            <div class="stat-item">
                <span class="stat-label">Periode Kosong</span>
                <div class="stat-value">{periode_kosong} <span style="font-size:12px;">dari {n_periods}</span></div>
            </div>
        </div>
        <div class="card-body" style="margin-top: 16px; font-size: 13px;">
            📌 <b>λ teori</b> = {lam_sim} · 
            <b>Rata-rata empiris</b> = {rata_empiris:.2f} ·
            Selisih ≈ {abs(rata_empiris - lam_sim):.2f}
            <br>
            <i>Semakin banyak periode simulasi, hasil empiris akan semakin dekat ke λ teori
            (Hukum Bilangan Besar).</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Timeline
    st.markdown("""
    <div class="kreasi-card">
        <div class="card-title">Timeline Kejadian</div>
        <div class="card-sub">Visualisasi per Periode</div>
        <div class="card-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    timeline_html = '<div class="timeline-wrap"><div class="timeline-label">Setiap kotak = 1 periode · isi = jumlah kejadian</div><div class="timeline-grid">'
    for i, ev in enumerate(events):
        if ev == 0:
            cls = "cell-empty"
        else:
            cls = "cell-event"
        timeline_html += f'<div class="timeline-cell {cls}" title="Periode {i+1}: {ev} kejadian">{ev}</div>'
    timeline_html += '</div></div>'
    st.markdown(timeline_html, unsafe_allow_html=True)

    # Perbandingan distribusi
    st.markdown("""
    <div class="kreasi-card" style="margin-top: 24px;">
        <div class="card-title">Perbandingan Empiris vs Teori</div>
        <div class="card-sub gold">Validasi</div>
        <div class="card-divider"></div>
        <div class="card-body">
            Tabel perbandingan frekuensi kejadian hasil simulasi dengan peluang teori.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hitung frekuensi empiris
    freq = {}
    for ev in events:
        freq[ev] = freq.get(ev, 0) + 1

    max_k = max(max(events), 10)
    table_rows = ""
    for i in range(0, max_k + 1):
        f_emp = freq.get(i, 0)
        p_emp = f_emp / n_periods
        p_theory = poisson_pmf(i, lam_sim)
        table_rows += f"""
        <div class="prob-row" style="display:flex; align-items:center; gap:14px; padding:10px 14px; border-radius:10px; background: rgba(217,195,163,0.10); border-left: 3px solid #d9c3a3; margin-bottom: 6px;">
            <div style="min-width:50px; font-size:12px; font-weight:700; color:#4e1318;">k = {i}</div>
            <div style="flex:1; font-size:12px; color:#3a2f2b;">
                Empiris: <b>{f_emp}×</b> ({p_emp*100:.1f}%) &nbsp;|&nbsp;
                Teori: <b>{p_theory*100:.2f}%</b>
            </div>
            <div style="min-width:70px; text-align:right; font-size:11px; font-weight:700; color:#701c23; font-family:'Playfair Display',serif;">
                {f_emp/n_periods*100:.1f}% vs {p_theory*100:.2f}%
            </div>
        </div>
        """

    st.markdown(f'<div style="margin-top: 12px;">{table_rows}</div>', unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="kreasi-card" style="margin-top: 16px; opacity: 0.7;">
        <div class="card-body" style="text-align: center; color: #6b5a52;">
            🎲 <i>Klik "Jalankan Simulasi" untuk memulai simulasi Monte Carlo</i>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div style="text-align: center; margin-top: 60px; padding: 20px; color: #a89790; font-size: 12px; letter-spacing: 1px;">
    ✦ KREASII · Keluarga Poisson · HMSD Adyatama ITERA 2026 ✦
</div>
""", unsafe_allow_html=True)
