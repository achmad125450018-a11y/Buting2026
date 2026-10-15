# ============================================================
# 🏪 POISSON QUEUE SIMULATOR — KREASI RESMI KELOMPOK POISSON
# File: kreasi.py
# Jalankan: streamlit run kreasi.py
# Import:   from kreasi import render_kreasi_page
# ============================================================

import streamlit as st
import math
import random
import time
from datetime import datetime, timezone, timedelta

# ============================================================
# 🎨 PREMIUM CSS
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #222222;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(112,28,35,0.06) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(217,195,163,0.20) 0%, transparent 55%),
        linear-gradient(180deg, #f4f0eb 0%, #efe8df 100%);
    background-attachment: fixed;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #701c23 0%, #4e1318 100%) !important;
}
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] svg {
    color: #ffffff !important;
    fill: #ffffff !important;
}

/* ============================================================
   HERO
   ============================================================ */
.queue-hero {
    text-align: center;
    padding: 50px 30px 42px 30px;
    background:
        radial-gradient(circle at 50% 0%, rgba(217,195,163,0.45) 0%, transparent 65%),
        linear-gradient(160deg, #ffffff 0%, #fdf9f3 100%);
    border-radius: 26px;
    border: 1px solid rgba(217,195,163,0.75);
    box-shadow:
        0 14px 40px rgba(112,28,35,0.10),
        0 1px 0 rgba(255,255,255,0.9) inset;
    position: relative;
    overflow: hidden;
    margin-bottom: 36px;
}
.queue-hero::before {
    content: 'λ';
    position: absolute;
    top: -60px; right: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 240px;
    font-style: italic;
    color: rgba(112,28,35,0.055);
    line-height: 1;
    pointer-events: none;
}
.queue-hero::after {
    content: '👥';
    position: absolute;
    bottom: -30px; left: 30px;
    font-size: 160px;
    opacity: 0.05;
    line-height: 1;
    pointer-events: none;
}
.queue-badge {
    display: inline-block;
    padding: 7px 20px;
    background: linear-gradient(135deg, rgba(217,195,163,0.55), rgba(217,195,163,0.15));
    border: 1px solid rgba(217,195,163,0.85);
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.8px;
    text-transform: uppercase;
    color: #701c23;
    margin-bottom: 22px;
    backdrop-filter: blur(8px);
}
.queue-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.1em;
    font-weight: 800;
    color: #701c23;
    margin: 0 0 12px 0;
    letter-spacing: 0.3px;
    line-height: 1.12;
    position: relative;
    z-index: 1;
}
.queue-subtitle {
    font-size: 15px;
    color: #6b5a52;
    max-width: 680px;
    margin: 0 auto;
    line-height: 1.75;
    position: relative;
    z-index: 1;
}
.queue-subtitle b { color: #701c23; font-weight: 700; }

/* ============================================================
   LIVE CLOCK BAR
   ============================================================ */
.live-clock-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 40px;
    flex-wrap: wrap;
    padding: 22px 32px;
    margin-bottom: 32px;
    background:
        radial-gradient(circle at 20% 50%, rgba(184,145,46,0.15) 0%, transparent 55%),
        linear-gradient(135deg, #701c23 0%, #4e1318 100%);
    border-radius: 22px;
    border: 1px solid rgba(217,195,163,0.35);
    box-shadow:
        0 20px 45px rgba(112,28,35,0.28),
        0 0 0 1px rgba(217,195,163,0.15) inset,
        0 0 70px rgba(184,145,46,0.10);
    position: relative;
    overflow: hidden;
}
.live-clock-bar::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(217,195,163,0.12) 1px, transparent 1px);
    background-size: 14px 14px;
    opacity: 0.35;
    pointer-events: none;
}
.live-clock-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    position: relative;
    z-index: 1;
    min-width: 180px;
}
.live-clock-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.6px;
    text-transform: uppercase;
    color: #d9c3a3;
}
.live-clock-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.85em;
    font-weight: 700;
    color: #f4f0eb;
    letter-spacing: 1px;
    text-shadow: 0 2px 14px rgba(0,0,0,0.35);
    line-height: 1;
}
.live-clock-value.time {
    background: linear-gradient(135deg, #e8c874 0%, #ffffff 50%, #e8c874 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.1em;
}
.live-clock-sub {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    color: rgba(244,240,235,0.7);
    letter-spacing: 0.5px;
}
.live-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: #e8c874;
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(232,200,116,0.9);
    animation: pulse-dot 1.2s ease-in-out infinite;
    margin-right: 6px;
    vertical-align: middle;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.7); }
}

/* ============================================================
   INPUT PANEL
   ============================================================ */
.input-panel {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 30px 34px;
    border-radius: 22px;
    border: 1px solid rgba(217,195,163,0.6);
    box-shadow: 0 12px 32px rgba(112,28,35,0.08);
    position: relative;
    overflow: hidden;
    margin-bottom: 30px;
}
.input-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.input-panel-title {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 0.3px;
    margin-bottom: 6px;
    position: relative;
    z-index: 1;
}
.input-panel-sub {
    font-size: 12.5px;
    color: #6b5a52;
    margin-bottom: 20px;
    line-height: 1.6;
    position: relative;
    z-index: 1;
}

/* ============================================================
   SCENARIO PILLS
   ============================================================ */
.scenario-label {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 12.5px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #a89790;
    margin: 26px 0 14px 0;
    position: relative;
}
.scenario-label::before,
.scenario-label::after {
    content: '✦';
    margin: 0 14px;
    color: #d9c3a3;
    font-size: 0.85em;
}

/* ============================================================
   STORE VISUALIZATION
   ============================================================ */
.store-wrapper {
    padding: 34px 30px;
    background:
        radial-gradient(circle at 50% 0%, rgba(217,195,163,0.20) 0%, transparent 60%),
        linear-gradient(160deg, #ffffff 0%, #fdf9f3 100%);
    border-radius: 24px;
    border: 1px solid rgba(217,195,163,0.65);
    box-shadow: 0 14px 36px rgba(112,28,35,0.10);
    position: relative;
    overflow: hidden;
    margin-bottom: 30px;
}
.store-wrapper::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(184,145,46,0.05) 1px, transparent 1px);
    background-size: 20px 20px;
    pointer-events: none;
}
.store-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 10px 18px 10px;
    margin-bottom: 20px;
    border-bottom: 2px dashed rgba(217,195,163,0.6);
    position: relative;
    z-index: 1;
}
.store-title {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 0.3px;
}
.store-status-pill {
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: #f4f0eb;
    box-shadow: 0 4px 12px rgba(112,28,35,0.28);
}
.store-status-pill.busy {
    background: linear-gradient(135deg, #b8912e 0%, #e8c874 100%);
    color: #4e1318;
}
.store-status-pill.critical {
    background: linear-gradient(135deg, #8b1a1a 0%, #c4302b 100%);
    color: #ffffff;
    animation: pulse-alert 1s ease-in-out infinite;
}
@keyframes pulse-alert {
    0%, 100% { box-shadow: 0 4px 12px rgba(139,26,26,0.4); }
    50% { box-shadow: 0 4px 22px rgba(196,48,43,0.75); }
}

/* Counter row */
.counters-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 14px;
    margin-bottom: 26px;
    position: relative;
    z-index: 1;
}
.counter-card {
    padding: 16px 18px;
    border-radius: 16px;
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    border: 1px solid rgba(217,195,163,0.55);
    box-shadow: 0 6px 18px rgba(112,28,35,0.06);
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}
.counter-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #701c23, #b8912e);
}
.counter-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 26px rgba(112,28,35,0.14);
}
.counter-label {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #a89790;
    margin-bottom: 6px;
}
.counter-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 26px;
    font-weight: 700;
    color: #701c23;
    line-height: 1;
    letter-spacing: -0.5px;
}
.counter-unit {
    font-size: 12px;
    color: #a89790;
    font-weight: 600;
    margin-left: 3px;
}

/* Queue lane */
.queue-lane {
    position: relative;
    z-index: 1;
    padding: 26px 20px;
    background: linear-gradient(180deg, rgba(217,195,163,0.10) 0%, rgba(217,195,163,0.03) 100%);
    border-radius: 18px;
    border: 1px dashed rgba(217,195,163,0.7);
    margin-bottom: 22px;
    min-height: 130px;
}
.queue-lane-title {
    font-family: 'Playfair Display', serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2.4px;
    text-transform: uppercase;
    color: #701c23;
    margin-bottom: 16px;
    text-align: center;
}
.queue-people {
    display: flex;
    gap: 10px;
    justify-content: center;
    align-items: flex-end;
    flex-wrap: wrap;
    min-height: 80px;
}
.person {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    animation: person-in 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.person-avatar {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    border: 2px solid rgba(217,195,163,0.85);
    box-shadow: 0 6px 14px rgba(112,28,35,0.15);
    background: linear-gradient(135deg, #ffffff, #fdf9f3);
    transition: all 0.3s ease;
}
.person-avatar.served {
    border-color: #b8912e;
    background: linear-gradient(135deg, #e8c874 0%, #b8912e 100%);
    animation: served-pulse 1s ease-in-out infinite alternate;
}
.person-avatar.waiting {
    border-color: #701c23;
}
.person-avatar.impatient {
    border-color: #c4302b;
    animation: impatient-shake 0.4s ease-in-out infinite;
}
.person-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5px;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 0.5px;
}
@keyframes person-in {
    from { opacity: 0; transform: translateX(30px) scale(0.7); }
    to { opacity: 1; transform: translateX(0) scale(1); }
}
@keyframes served-pulse {
    from { transform: scale(1); }
    to { transform: scale(1.08); }
}
@keyframes impatient-shake {
    0%, 100% { transform: rotate(0deg); }
    25% { transform: rotate(-4deg); }
    75% { transform: rotate(4deg); }
}

.empty-queue {
    text-align: center;
    padding: 24px;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #a89790;
    font-size: 14px;
}

/* ============================================================
   CHART DISTRIBUTION
   ============================================================ */
.info-card {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 26px 30px;
    border-radius: 20px;
    border: 1px solid rgba(217,195,163,0.55);
    box-shadow: 0 10px 30px rgba(112,28,35,0.07);
    position: relative;
    overflow: hidden;
    margin-bottom: 22px;
}
.info-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.info-header {
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    font-weight: 700;
    color: #701c23;
    margin-bottom: 6px;
    position: relative;
    z-index: 1;
}
.info-subheader {
    display: inline-block;
    padding: 3px 12px;
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    border-radius: 999px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: #f4f0eb;
    box-shadow: 0 3px 10px rgba(112,28,35,0.28);
    margin-bottom: 14px;
    position: relative;
    z-index: 1;
}
.info-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d9c3a3, transparent);
    margin: 4px 0 14px 0;
    position: relative;
    z-index: 1;
}
.info-text {
    font-size: 13.5px;
    line-height: 1.85;
    color: #3a2f2b;
    position: relative;
    z-index: 1;
    margin: 0;
}
.info-text b { color: #701c23; font-weight: 700; }

.dist-chart {
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 8px;
    padding: 26px 10px 10px 10px;
    min-height: 200px;
    position: relative;
}
.dist-bar {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    flex: 1;
    max-width: 60px;
}
.dist-bar-fill {
    width: 100%;
    background: linear-gradient(180deg, #a8323d 0%, #701c23 100%);
    border-radius: 8px 8px 4px 4px;
    transition: all 0.4s ease;
    box-shadow: 0 6px 16px rgba(112,28,35,0.20);
    min-height: 4px;
}
.dist-bar-fill.highlight {
    background: linear-gradient(180deg, #e8c874 0%, #b8912e 100%);
    box-shadow: 0 6px 20px rgba(184,145,46,0.35);
}
.dist-bar-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 0.3px;
}
.dist-bar-value {
    font-size: 9px;
    color: #a89790;
    font-weight: 600;
}

/* ============================================================
   RECOMMENDATION CARD
   ============================================================ */
.recom-card {
    padding: 30px 32px;
    border-radius: 22px;
    position: relative;
    overflow: hidden;
    margin-bottom: 22px;
    box-shadow: 0 18px 42px rgba(112,28,35,0.22);
    background:
        radial-gradient(circle at 20% 15%, rgba(232,200,116,0.25) 0%, transparent 55%),
        linear-gradient(150deg, #701c23 0%, #4e1318 100%);
    color: #f4f0eb;
}
.recom-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(217,195,163,0.10) 1px, transparent 1px);
    background-size: 14px 14px;
    opacity: 0.4;
    pointer-events: none;
}
.recom-title {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2.6px;
    text-transform: uppercase;
    color: #d9c3a3;
    margin-bottom: 12px;
    position: relative;
    z-index: 1;
}
.recom-main {
    font-family: 'Playfair Display', serif;
    font-size: 1.9em;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.25;
    margin-bottom: 8px;
    position: relative;
    z-index: 1;
    text-shadow: 0 3px 16px rgba(0,0,0,0.30);
}
.recom-sub {
    font-size: 13.5px;
    line-height: 1.75;
    color: rgba(244,240,235,0.9);
    position: relative;
    z-index: 1;
    max-width: 640px;
}

/* ============================================================
   STREAMLIT OVERRIDES
   ============================================================ */
.stButton > button {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 14px;
    border-radius: 12px;
    border: 1px solid rgba(217,195,163,0.7);
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    color: #701c23;
    transition: all 0.25s ease;
    padding: 12px 16px;
    box-shadow: 0 4px 12px rgba(112,28,35,0.08);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: #ffffff;
    border-color: #701c23;
    box-shadow: 0 8px 22px rgba(112,28,35,0.30);
    transform: translateY(-1px);
}

.stSelectbox label, .stSlider label, .stNumberInput label {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    color: #701c23 !important;
    font-size: 12.5px !important;
    letter-spacing: 0.4px !important;
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
# 🏪 SKENARIO DATA
# ============================================================
SCENARIOS = {
    "🏦 Bank Teller": {
        "lambda_range": (5, 40),
        "default_lambda": 18,     # pelanggan/jam
        "default_service": 4,     # menit/pelanggan
        "emojis": ["🧑‍💼", "👩‍💼", "🧓", "👨‍🦱", "👩‍🦰", "🧔", "👱‍♀️", "👨‍💻", "👩‍🦱", "🧑"],
        "context": "Nasabah datang untuk setor, tarik, atau buka rekening.",
    },
    "🛒 Minimarket Kasir": {
        "lambda_range": (10, 60),
        "default_lambda": 28,
        "default_service": 3,
        "emojis": ["🛒", "🧺", "🥤", "🍫", "🍞", "🧃", "🥫", "🍜", "🧀", "🍕"],
        "context": "Pembeli datang dengan keranjang belanjaan berbeda-beda.",
    },
    "🏥 Loket BPJS": {
        "lambda_range": (5, 35),
        "default_lambda": 15,
        "default_service": 5,
        "emojis": ["🧑‍🦱", "👨‍🦳", "🧕", "👩‍⚕️", "🧑‍🦰", "👨‍🦰", "👵", "👴", "🧓", "👩"],
        "context": "Pasien datang untuk administrasi & konsultasi.",
    },
    "🍜 Kantin Kampus": {
        "lambda_range": (20, 120),
        "default_lambda": 55,
        "default_service": 2,
        "emojis": ["🎓", "🍜", "🍚", "🥘", "🍲", "🥗", "🍛", "🧋", "☕", "🍱"],
        "context": "Mahasiswa menyerbu kantin saat jam istirahat kuliah.",
    },
    "🎬 Bioskop Tiket": {
        "lambda_range": (15, 80),
        "default_lambda": 35,
        "default_service": 2,
        "emojis": ["🍿", "🎬", "🥤", "🎟️", "🧑", "👫", "👨‍👩‍👧", "🎥", "🎞️", "🌭"],
        "context": "Penonton beli tiket sebelum film mulai tayang.",
    },
    "⛽ SPBU": {
        "lambda_range": (8, 50),
        "default_lambda": 22,
        "default_service": 3,
        "emojis": ["🚗", "🏍️", "🚙", "🚕", "🚐", "🛻", "🚌", "🚓", "🚚", "🛵"],
        "context": "Kendaraan datang untuk isi bahan bakar.",
    },
}


# ============================================================
# 🕐 LIVE DATETIME (WIB)
# ============================================================
HARI_NAMA = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
BULAN_NAMA = ["Januari","Februari","Maret","April","Mei","Juni",
              "Juli","Agustus","September","Oktober","November","Desember"]


def get_now_wib():
    wib = timezone(timedelta(hours=7))
    return datetime.now(wib)


def render_live_clock():
    now = get_now_wib()
    hari = HARI_NAMA[now.weekday()]
    tanggal = now.day
    bulan = BULAN_NAMA[now.month - 1]
    tahun = now.year
    jam = now.strftime("%H")
    menit = now.strftime("%M")
    detik = now.strftime("%S")

    st.markdown(f"""
        <div class="live-clock-bar">
            <div class="live-clock-item">
                <div class="live-clock-label"><span class="live-dot"></span>Hari Ini</div>
                <div class="live-clock-value">{hari}</div>
                <div class="live-clock-sub">{tanggal} {bulan} {tahun}</div>
            </div>
            <div class="live-clock-item">
                <div class="live-clock-label"><span class="live-dot"></span>Waktu Indonesia Barat</div>
                <div class="live-clock-value time">{jam}:{menit}<span style="font-size: 0.55em; opacity: 0.65;">:{detik}</span></div>
                <div class="live-clock-sub">UTC +07:00 · WIB</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🧮 RUMUS POISSON & TEORI ANTRIAN
# ============================================================
def poisson_pmf(lam, k):
    """P(X = k)."""
    if lam <= 0 or k < 0:
        return 0.0
    try:
        return (math.exp(-lam) * (lam ** k)) / math.factorial(k)
    except (OverflowError, ValueError):
        return 0.0


def utilization(lambda_per_hour, service_per_hour):
    """ρ = λ / μ. Jika ≥ 1 → overload."""
    if service_per_hour <= 0:
        return float("inf")
    return lambda_per_hour / service_per_hour


def expected_queue_length(lam, mu):
    """Rata-rata panjang antrian untuk M/M/1: Lq = λ² / (μ(μ-λ))."""
    if mu <= lam:
        return float("inf")
    return (lam ** 2) / (mu * (mu - lam))


def expected_waiting_time(lam, mu):
    """Rata-rata waktu tunggu di antrian (jam): Wq = Lq / λ."""
    Lq = expected_queue_length(lam, mu)
    if Lq == float("inf") or lam == 0:
        return float("inf")
    return Lq / lam


def avg_people_in_system(lam, mu):
    """Rata-rata jumlah orang dalam sistem (antri + dilayani): L = λ / (μ - λ)."""
    if mu <= lam:
        return float("inf")
    return lam / (mu - lam)


def prob_queue_gt_n(lam, mu, n):
    """P(Lq > n) = ρ^(n+1) untuk M/M/1."""
    rho = utilization(lam, mu)
    if rho >= 1:
        return 1.0
    return rho ** (n + 1)


def needed_servers(lam_per_hour, service_minutes, target_wait_minutes=5):
    """
    Estimasi jumlah server minimum agar rata-rata waktu tunggu ≤ target_wait.
    Pendekatan iteratif sederhana.
    """
    mu_per_server = 60.0 / service_minutes  # pelayanan per server per jam
    for n in range(1, 21):
        capacity = n * mu_per_server
        if capacity <= lam_per_hour:
            continue
        rho = lam_per_hour / capacity
        # Aproksimasi M/M/n (pakai simple ratio untuk demo)
        if rho < 0.7:
            wait_min = (rho / (1 - rho)) * service_minutes / n * 2
        else:
            wait_min = (rho / (1 - rho)) * service_minutes / max(1, n)
        if wait_min <= target_wait_minutes:
            return n
    return 21  # fallback


def recommend_cashiers(lam, service_minutes):
    """Return (jumlah kasir optimal, status string)."""
    n = needed_servers(lam, service_minutes, target_wait_minutes=5)
    if n <= 2:
        status = "santai"
    elif n <= 4:
        status = "normal"
    elif n <= 6:
        status = "sibuk"
    else:
        status = "sangat sibuk"
    return n, status


# ============================================================
# 👥 SIMULASI ANTRIAN
# ============================================================
def simulate_queue(lam_per_hour, service_minutes, num_cashiers, duration_hours=1.0):
    """
    Simulasi Monte Carlo kedatangan pelanggan (Poisson) + pelayanan (Eksponensial).
    Return dict berisi statistik.
    """
    mu_per_hour = 60.0 / service_minutes  # pelayanan per kasir per jam
    total_capacity = num_cashiers * mu_per_hour
    expected_arrivals = lam_per_hour * duration_hours

    # Kedatangan Poisson: sampel dari Poisson
    # Untuk simplicity, pakai normal approx untuk λ besar (lam ≥ 10)
    if expected_arrivals < 30:
        # Inverse transform (exact-ish)
        L = math.exp(-expected_arrivals)
        k = 0
        p = 1.0
        while True:
            k += 1
            p *= random.random()
            if p <= L:
                arrivals = k - 1
                break
    else:
        arrivals = max(0, int(random.gauss(expected_arrivals, math.sqrt(expected_arrivals))))

    # Waktu tunggu rata-rata
    rho = min(0.99, lam_per_hour / total_capacity)
    avg_wait_min = (rho / max(0.01, 1 - rho)) * service_minutes / num_cashiers
    avg_queue_len = rho / max(0.01, 1 - rho) * num_cashiers

    return {
        "arrivals": arrivals,
        "capacity": total_capacity,
        "rho": rho,
        "avg_wait_min": avg_wait_min,
        "avg_queue_len": avg_queue_len,
    }


# ============================================================
# 🎨 RENDER STORE VISUAL
# ============================================================
def render_store_visual(scenario_key, lam, service_min, num_cashiers, state):
    """Render visual toko + antrian."""
    emojis = SCENARIOS[scenario_key]["emojis"]
    queue_len = state.get("queue_len", 0)
    served_count = state.get("served_count", 0)
    critical_count = state.get("critical_count", 0)

    # Status
    rho = utilization(lam, num_cashiers * (60.0 / service_min))
    if rho >= 1.0:
        status_text, status_cls = "🔴 OVERLOAD", "critical"
    elif rho >= 0.8:
        status_text, status_cls = "🟠 SIBUK", "busy"
    elif rho >= 0.5:
        status_text, status_cls = "🟡 NORMAL", ""
    else:
        status_text, status_cls = "🟢 SANTAI", ""

    # Counter row
    rho_percent = min(100, rho * 100) if rho != float("inf") else 100
    st.markdown(f"""
        <div class="store-wrapper">
            <div class="store-header">
                <div class="store-title">🏪 {scenario_key}</div>
                <div class="store-status-pill {status_cls}">{status_text}</div>
            </div>
            <div class="counters-row">
                <div class="counter-card">
                    <div class="counter-label">👥 Antrian</div>
                    <div class="counter-value">{queue_len}<span class="counter-unit">orang</span></div>
                </div>
                <div class="counter-card">
                    <div class="counter-label">✓ Terlayani</div>
                    <div class="counter-value">{served_count}<span class="counter-unit">org</span></div>
                </div>
                <div class="counter-card">
                    <div class="counter-label">📊 Utilisasi (ρ)</div>
                    <div class="counter-value">{rho_percent:.0f}<span class="counter-unit">%</span></div>
                </div>
                <div class="counter-card">
                    <div class="counter-label">🏦 Kasir Aktif</div>
                    <div class="counter-value">{num_cashiers}<span class="counter-unit">unit</span></div>
                </div>
                <div class="counter-card">
                    <div class="counter-label">🔥 Kritis</div>
                    <div class="counter-value">{critical_count}<span class="counter-unit">org</span></div>
                </div>
            </div>
    """, unsafe_allow_html=True)

    # Queue lane — visual orang
    queue_lane_html = ""
    if queue_len > 0:
        people_html = ""
        for idx in range(queue_len):
            emoji = emojis[idx % len(emojis)]
            # orang pertama = sedang dilayani
            if idx == 0:
                cls = "served"
            elif idx >= 7:
                cls = "impatient"
            else:
                cls = "waiting"
            people_html += f"""
                <div class="person">
                    <div class="person-avatar {cls}">{emoji}</div>
                    <div class="person-id">#{idx + 1:02d}</div>
                </div>"""
        queue_lane_html = f'<div class="queue-people">{people_html}</div>'
    else:
        queue_lane_html = '<div class="empty-queue">✨ Antrian kosong, kasir menunggu pelanggan...</div>'

    st.markdown(f"""
            <div class="queue-lane">
                <div class="queue-lane-title">🍽️ Garis Antrian</div>
                {queue_lane_html}
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 📊 RENDER DISTRIBUSI CHART
# ============================================================
def render_distribution_chart(lam, max_k=None):
    if max_k is None:
        max_k = max(6, int(lam * 1.8))
        max_k = min(max_k, 20)

    probs = [poisson_pmf(lam, k) for k in range(max_k + 1)]
    max_p = max(probs) if probs else 1.0
    max_p = max(max_p, 0.01)

    bars = ""
    for k, p in enumerate(probs):
        height = (p / max_p) * 140
        height = max(height, 3)
        cls = "dist-bar-fill"
        if k == int(round(lam)):
            cls += " highlight"
        bars += f"""
        <div class="dist-bar">
            <div class="dist-bar-value">{p*100:.1f}%</div>
            <div class="{cls}" style="height:{height:.0f}px;"></div>
            <div class="dist-bar-label">k={k}</div>
        </div>"""

    st.markdown(f'<div class="dist-chart">{bars}</div>', unsafe_allow_html=True)


# ============================================================
# 💡 REKOMENDASI KASIR
# ============================================================
def render_recommendation(lam, service_min, num_cashiers):
    optimal, status = recommend_cashiers(lam, service_min)

    if num_cashiers < optimal:
        diff = optimal - num_cashiers
        emoji = "⚠️"
        msg = f"Kamu <b>kekurangan {diff} kasir</b> dari jumlah optimal. Antrian bakal panjang dan pelanggan bisa kabur!"
    elif num_cashiers > optimal + 2:
        diff = num_cashiers - optimal
        emoji = "💰"
        msg = f"Kamu <b>kelebihan {diff} kasir</b>. Ada kasir yang nganggur — bisa dihemat biaya operasional."
    elif num_cashiers == optimal:
        emoji = "✨"
        msg = f"Jumlah kasir kamu <b>sempurna!</b> Sesuai rekomendasi sistem antrian M/M/1."
    else:
        emoji = "✅"
        msg = f"Jumlah kasir kamu <b>cukup optimal</b>, sedikit lebih dari yang dibutuhkan."

    st.markdown(f"""
        <div class="recom-card">
            <div class="recom-title">💡 Rekomendasi Sistem</div>
            <div class="recom-main">{emoji} Butuh {optimal} kasir untuk λ = {lam:.0f}/jam</div>
            <div class="recom-sub">
                {msg}<br><br>
                <b>Status:</b> {status.upper()} &nbsp;·&nbsp;
                <b>Target:</b> rata-rata tunggu ≤ 5 menit &nbsp;·&nbsp;
                <b>Asumsi:</b> pelayanan {service_min} menit/pelanggan
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 📊 STATISTIK TEORITIS
# ============================================================
def render_theoretical_stats(lam, service_min, num_cashiers):
    mu_total = num_cashiers * (60.0 / service_min)
    rho = utilization(lam, mu_total)
    Lq = expected_queue_length(lam, mu_total)
    Wq = expected_waiting_time(lam, mu_total)
    L = avg_people_in_system(lam, mu_total)

    def fmt_inf(v, suffix="", digits=1):
        if v == float("inf"):
            return "∞"
        return f"{v:.{digits}f}{suffix}"

    st.markdown(f"""
        <div class="info-card">
            <div class="info-header">📐 Statistik Antrian (Teori M/M/1)</div>
            <div class="info-subheader">Queueing Theory</div>
            <div class="info-divider"></div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 14px; position: relative; z-index: 1;">
                <div style="padding: 14px 16px; background: rgba(217,195,163,0.12); border-radius: 12px; border-left: 3px solid #701c23;">
                    <div style="font-size: 9.5px; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: #a89790; margin-bottom: 4px;">Utilisasi (ρ)</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 700; color: #701c23;">{fmt_inf(rho * 100, "%")}</div>
                </div>
                <div style="padding: 14px 16px; background: rgba(217,195,163,0.12); border-radius: 12px; border-left: 3px solid #b8912e;">
                    <div style="font-size: 9.5px; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: #a89790; margin-bottom: 4px;">Panjang Antrian (Lq)</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 700; color: #701c23;">{fmt_inf(Lq, " org")}</div>
                </div>
                <div style="padding: 14px 16px; background: rgba(217,195,163,0.12); border-radius: 12px; border-left: 3px solid #b8912e;">
                    <div style="font-size: 9.5px; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: #a89790; margin-bottom: 4px;">Waktu Tunggu (Wq)</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 700; color: #701c23;">{fmt_inf(Wq * 60, " mnt")}</div>
                </div>
                <div style="padding: 14px 16px; background: rgba(217,195,163,0.12); border-radius: 12px; border-left: 3px solid #701c23;">
                    <div style="font-size: 9.5px; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: #a89790; margin-bottom: 4px;">Total di Sistem (L)</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 700; color: #701c23;">{fmt_inf(L, " org")}</div>
                </div>
                <div style="padding: 14px 16px; background: rgba(217,195,163,0.12); border-radius: 12px; border-left: 3px solid #b8912e;">
                    <div style="font-size: 9.5px; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: #a89790; margin-bottom: 4px;">P(Antri &gt; 5)</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 700; color: #701c23;">{prob_queue_gt_n(lam, mu_total, 5) * 100:.1f}%</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🎯 MAIN PAGE
# ============================================================
def render_kreasi_page():
    # ---------- HERO ----------
    st.markdown("""
        <div class="queue-hero">
            <div class="queue-badge">✦ Kreasi Resmi Kelompok Poisson ✦</div>
            <h1 class="queue-title">Poisson Queue Simulator</h1>
            <p class="queue-subtitle">
                Simulasi <b>sistem antrian layanan</b> menggunakan <b>distribusi Poisson</b>
                &mdash; model matematika yang benar-benar dipakai bank, rumah sakit, dan
                minimarket untuk mengatur jumlah kasir optimal. Atur λ dan lihat langsung
                bagaimana antrian terbentuk, bergerak, dan dilayani. 🎯
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ---------- LIVE CLOCK ----------
    render_live_clock()
    st.markdown("""
        <script>
        setTimeout(function() { window.location.reload(); }, 30000);
        </script>
    """, unsafe_allow_html=True)

    # ---------- SCENARIO PILLS ----------
    st.markdown('<div class="scenario-label">Pilih Skenario Layanan</div>', unsafe_allow_html=True)

    scenario_keys = list(SCENARIOS.keys())
    current = st.session_state.get("queue_scenario", scenario_keys[0])

    s_cols = st.columns(len(scenario_keys))
    for idx, key in enumerate(scenario_keys):
        with s_cols[idx]:
            is_active = "✓" if key == current else ""
            if st.button(f"{key} {is_active}", key=f"scn_{idx}", use_container_width=True):
                if key != current:
                    st.session_state.queue_scenario = key
                    # reset state sim
                    st.session_state.queue_len = 0
                    st.session_state.served_count = 0
                    st.session_state.critical_count = 0
                    st.session_state.tick = 0
                    st.rerun()

    scenario = st.session_state.get("queue_scenario", scenario_keys[0])
    scen_data = SCENARIOS[scenario]

    # ---------- INPUT PANEL ----------
    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="input-panel">
            <div class="input-panel-title">⚙️ Konfigurasi Simulasi</div>
            <div class="input-panel-sub">
                {scen_data['context']}<br>
                <b>Atur λ (rata-rata kedatangan/jam)</b>, <b>waktu pelayanan per pelanggan</b>,
                dan <b>jumlah kasir aktif</b>. Simulasi akan menghitung panjang antrian,
                waktu tunggu, dan rekomendasi jumlah kasir optimal.
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    lam_min, lam_max = scen_data["lambda_range"]
    with c1:
        lam = st.slider(
            "λ — Kedatangan (orang/jam)",
            min_value=lam_min,
            max_value=lam_max,
            value=scen_data["default_lambda"],
            step=1,
            key="queue_lam",
        )

    with c2:
        service_min = st.slider(
            "⏱️ Waktu Pelayanan (menit/orang)",
            min_value=1,
            max_value=15,
            value=scen_data["default_service"],
            step=1,
            key="queue_service",
        )

    with c3:
        num_cashiers = st.slider(
            "🏦 Jumlah Kasir Aktif",
            min_value=1,
            max_value=12,
            value=3,
            step=1,
            key="queue_cashiers",
        )

    # ---------- AUTO SIM TICK ----------
    if "queue_state" not in st.session_state:
        st.session_state.queue_state = {
            "queue_len": 0,
            "served_count": 0,
            "critical_count": 0,
        }

    state = st.session_state.queue_state

    # Simulasi tiap render: beberapa "tick" untuk dapat hasil stabil
    mu_per_hour = num_cashiers * (60.0 / service_min)
    rho = lam / mu_per_hour if mu_per_hour > 0 else 2.0

    # Simulate beberapa event
    random.seed(int(time.time() * 1000) % 100000)
    for _ in range(random.randint(2, 5)):
        # Peluang arrival berdasarkan λ/menit
        arrival_prob = lam / 60.0 * 5  # ~5 detik window
        if random.random() < min(arrival_prob, 0.95):
            state["queue_len"] += 1
        # Pelayanan: peluang layani ~ kasir × (1/service) per 5 detik
        service_prob = num_cashiers * (5.0 / 60.0) / service_min * 8
        if state["queue_len"] > 0 and random.random() < min(service_prob, 0.9):
            state["queue_len"] -= 1
            state["served_count"] += 1

    # Track kritis
    if state["queue_len"] >= 8:
        state["critical_count"] = min(99, state["critical_count"] + 1)

    # ---------- STORE VISUAL ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    render_store_visual(scenario, lam, service_min, num_cashiers, state)

    # ---------- RECOMMENDATION ----------
    render_recommendation(lam, service_min, num_cashiers)

    # ---------- THEORETICAL STATS ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    render_theoretical_stats(lam, service_min, num_cashiers)

    # ---------- DISTRIBUTION CHART ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="info-card">
            <div class="info-header">📊 Distribusi Peluang Kedatangan</div>
            <div class="info-subheader">Poisson PMF</div>
            <div class="info-divider"></div>
            <p class="info-text">
                Grafik di bawah menunjukkan peluang <b>tepat k orang datang</b> dalam
                satu jam, dengan λ = <b>{lam}</b>. Bar yang di-highlight emas adalah
                nilai k yang paling mungkin terjadi (k ≈ λ).
            </p>
        </div>
    """, unsafe_allow_html=True)
    render_distribution_chart(lam)

    # ---------- KONTROL SIMULASI ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    bcol1, bcol2 = st.columns(2)
    with bcol1:
        if st.button("🔄 Reset Simulasi", use_container_width=True, key="reset_sim"):
            st.session_state.queue_state = {
                "queue_len": 0,
                "served_count": 0,
                "critical_count": 0,
            }
            st.rerun()
    with bcol2:
        if st.button("⚡ Tambah 5 Orang Tiba-tiba", use_container_width=True, key="burst"):
            st.session_state.queue_state["queue_len"] += 5
            st.rerun()

    # ---------- EDUKASI ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            <div class="info-header">💡 Kenapa Antrian Pakai Distribusi Poisson?</div>
            <div class="info-subheader">Edukasi</div>
            <div class="info-divider"></div>
            <p class="info-text">
                Kedatangan pelanggan adalah contoh sempurna dari <b>kejadian langka dalam
                interval waktu tertentu</b>. Dalam 1 jam, ada kalanya sepi (0 orang),
                ada kalanya ramai (10+ orang). Distribusi Poisson menangkap pola ini
                dengan parameter tunggal: <b>λ (lambda)</b> = rata-rata kedatangan per jam.
                <br><br>
                Rumus yang dipakai: <b>P(X = k) = (λ<sup>k</sup> · e<sup>−λ</sup>) / k!</b>
                <br><br>
                Dari sini kita bisa hitung:
                <br>
                📊 <b>Panjang antrian rata-rata</b> &nbsp;·&nbsp;
                ⏱️ <b>Waktu tunggu rata-rata</b> &nbsp;·&nbsp;
                🎯 <b>Jumlah kasir optimal</b> &nbsp;·&nbsp;
                🔥 <b>Peluang overload</b>
                <br><br>
                Model antrian seperti ini (<b>M/M/1</b> dan <b>M/M/c</b>) benar-benar
                dipakai di bank, rumah sakit, call center, dan sistem logistik
                di seluruh dunia. Setiap kali kamu ngantri di kasir, kamu sedang
                berinteraksi dengan matematika Poisson. 🎯
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ---------- FOOTER ----------
    now = get_now_wib()
    st.markdown(f"""
        <div style="text-align: center; margin-top: 40px; padding-top: 30px; border-top: 1px solid rgba(217,195,163,0.5);">
            <div style="font-family: 'Playfair Display', serif; font-size: 13px; color: #701c23; letter-spacing: 1.5px; font-weight: 600;">
                ✦ Poisson Queue Simulator ✦
            </div>
            <div style="font-size: 10px; color: #a89790; letter-spacing: 2px; text-transform: uppercase; margin-top: 6px;">
                Kreasi Kelompok Poisson · {now.day} {BULAN_NAMA[now.month-1]} {now.year} · {now.strftime('%H:%M:%S')} WIB
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# RUN
# ============================================================
if __name__ == "__main__":
    render_kreasi_page()
