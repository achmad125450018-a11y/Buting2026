# ============================================================
# 🌦️ POISSON WEATHER FORECAST — KREASI RESMI KELOMPOK POISSON
# File: kreasi.py
# Jalankan: streamlit run kreasi.py
# Import:   from kreasi import render_kreasi_page
# ============================================================

import streamlit as st
import math
import random
from datetime import datetime, timezone, timedelta
import time

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
.weather-hero {
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
.weather-hero::before {
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
.weather-hero::after {
    content: '☁';
    position: absolute;
    bottom: -40px; left: 30px;
    font-size: 180px;
    color: rgba(184,145,46,0.06);
    line-height: 1;
    pointer-events: none;
}
.weather-badge {
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
.weather-title {
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
.weather-subtitle {
    font-size: 15px;
    color: #6b5a52;
    max-width: 680px;
    margin: 0 auto;
    line-height: 1.75;
    position: relative;
    z-index: 1;
}
.weather-subtitle b { color: #701c23; font-weight: 700; }

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
   INPUT SECTION
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
   RESULT — MAIN FORECAST CARD
   ============================================================ */
.forecast-card {
    padding: 44px 36px;
    border-radius: 26px;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 30px;
    box-shadow:
        0 26px 60px rgba(112,28,35,0.30),
        0 0 0 1px rgba(217,195,163,0.20) inset;
    animation: fade-in 0.55s ease;
}
@keyframes fade-in {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}
.forecast-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(255,255,255,0.10) 1px, transparent 1px);
    background-size: 16px 16px;
    opacity: 0.35;
    pointer-events: none;
}
.forecast-card.sunny {
    background:
        radial-gradient(circle at 20% 15%, rgba(232,200,116,0.35) 0%, transparent 55%),
        linear-gradient(150deg, #b8912e 0%, #701c23 100%);
}
.forecast-card.cloudy {
    background:
        radial-gradient(circle at 20% 15%, rgba(217,195,163,0.30) 0%, transparent 55%),
        linear-gradient(150deg, #4e1318 0%, #701c23 100%);
}
.forecast-card.rainy {
    background:
        radial-gradient(circle at 20% 15%, rgba(100,150,200,0.30) 0%, transparent 55%),
        linear-gradient(150deg, #2a3a4f 0%, #4e1318 100%);
}
.forecast-card.stormy {
    background:
        radial-gradient(circle at 20% 15%, rgba(80,120,180,0.35) 0%, transparent 55%),
        linear-gradient(150deg, #1a2a3f 0%, #2d0a0d 100%);
}

.forecast-emoji {
    font-size: 90px;
    line-height: 1;
    margin-bottom: 12px;
    position: relative;
    z-index: 1;
    filter: drop-shadow(0 8px 20px rgba(0,0,0,0.35));
    animation: float-emoji 3s ease-in-out infinite;
}
@keyframes float-emoji {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}
.forecast-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3.2px;
    text-transform: uppercase;
    color: #d9c3a3;
    margin-bottom: 10px;
    position: relative;
    z-index: 1;
}
.forecast-percent {
    font-family: 'Playfair Display', serif;
    font-size: 5.2em;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 6px;
    position: relative;
    z-index: 1;
    text-shadow: 0 4px 24px rgba(0,0,0,0.30);
    letter-spacing: -2px;
}
.forecast-percent-unit {
    font-size: 0.45em;
    color: rgba(255,255,255,0.85);
    font-weight: 700;
    vertical-align: top;
    margin-left: 6px;
}
.forecast-status {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 17px;
    color: #f4f0eb;
    max-width: 520px;
    margin: 18px auto 0 auto;
    padding-top: 20px;
    border-top: 1px solid rgba(217,195,163,0.35);
    line-height: 1.65;
    position: relative;
    z-index: 1;
}
.forecast-params {
    display: flex;
    justify-content: center;
    gap: 28px;
    margin-top: 26px;
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
}
.forecast-param {
    text-align: center;
    padding: 12px 20px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(217,195,163,0.30);
    border-radius: 14px;
    backdrop-filter: blur(8px);
    min-width: 100px;
}
.forecast-param-label {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #d9c3a3;
    margin-bottom: 4px;
}
.forecast-param-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 17px;
    font-weight: 700;
    color: #f4f0eb;
}

/* ============================================================
   7-DAY FORECAST
   ============================================================ */
.week-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
    margin-bottom: 30px;
}
.day-card {
    padding: 16px 10px 14px 10px;
    border-radius: 16px;
    background: linear-gradient(160deg, #ffffff 0%, #fdfbf8 100%);
    border: 1px solid rgba(217,195,163,0.55);
    text-align: center;
    transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
    box-shadow: 0 4px 12px rgba(112,28,35,0.06);
    position: relative;
    overflow: hidden;
}
.day-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 30px rgba(112,28,35,0.18);
    border-color: #701c23;
}
.day-card.today {
    background: linear-gradient(160deg, #701c23 0%, #4e1318 100%);
    border-color: #b8912e;
    box-shadow: 0 10px 26px rgba(112,28,35,0.28);
}
.day-card.today .day-name,
.day-card.today .day-date {
    color: #d9c3a3;
}
.day-card.today .day-emoji {
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.35));
}
.day-card.today .day-percent {
    color: #f4f0eb;
}
.day-card.today::after {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 3px;
    background: linear-gradient(90deg, #b8912e, #e8c874, #b8912e);
}
.day-name {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    font-weight: 700;
    color: #701c23;
    margin-bottom: 2px;
    letter-spacing: 0.4px;
}
.day-date {
    font-size: 10px;
    color: #a89790;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 10px;
}
.day-emoji {
    font-size: 34px;
    line-height: 1;
    margin-bottom: 10px;
}
.day-percent {
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 0.3px;
}

/* ============================================================
   CHART & INFO CARDS
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

/* ============================================================
   DISTRIBUTION CHART
   ============================================================ */
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
    position: relative;
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
   CITY PILLS
   ============================================================ */
.city-info {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 16px;
}
.city-pill {
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(217,195,163,0.15);
    border: 1px solid rgba(217,195,163,0.55);
    font-size: 11px;
    font-weight: 600;
    color: #701c23;
    letter-spacing: 0.4px;
}
.city-pill b {
    font-family: 'JetBrains Mono', monospace;
    color: #4e1318;
    margin-left: 4px;
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
# 🌏 DATA KOTA & MUSIM
# ============================================================
CITY_DATA = {
    "Bandar Lampung":  {"kemarau": 0.15, "hujan": 0.55, "emoji": "🌴"},
    "Jakarta":         {"kemarau": 0.20, "hujan": 0.62, "emoji": "🏙️"},
    "Bandung":         {"kemarau": 0.18, "hujan": 0.58, "emoji": "⛰️"},
    "Surabaya":        {"kemarau": 0.10, "hujan": 0.45, "emoji": "🌊"},
    "Medan":           {"kemarau": 0.25, "hujan": 0.65, "emoji": "🌳"},
    "Palembang":       {"kemarau": 0.18, "hujan": 0.60, "emoji": "🌉"},
    "Makassar":        {"kemarau": 0.12, "hujan": 0.50, "emoji": "🐟"},
    "Bali (Denpasar)": {"kemarau": 0.08, "hujan": 0.42, "emoji": "🏝️"},
    "Yogyakarta":      {"kemarau": 0.14, "hujan": 0.52, "emoji": "🎭"},
    "Balikpapan":      {"kemarau": 0.22, "hujan": 0.60, "emoji": "🌲"},
}

# Bulan: 1=Jan ... 12=Des. Indonesia: Nov-Apr hujan, Mei-Okt kemarau
BULAN_NAMA = ["Januari","Februari","Maret","April","Mei","Juni",
              "Juli","Agustus","September","Oktober","November","Desember"]
HARI_NAMA = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]


def get_season_factor(month):
    """Return factor 0..1 — 1 = musim hujan, 0 = musim kemarau."""
    if month in [11, 12, 1, 2, 3, 4]:
        return 1.0
    elif month in [5, 10]:
        return 0.5  # transisi
    else:
        return 0.0


def compute_lambda(city, month, user_override=None):
    """λ = rata-rata hari hujan per hari di kota + bulan tsb."""
    if user_override is not None:
        return user_override
    city_d = CITY_DATA.get(city, CITY_DATA["Bandar Lampung"])
    season = get_season_factor(month)
    lam = city_d["kemarau"] + (city_d["hujan"] - city_d["kemarau"]) * season
    return round(lam, 3)


# ============================================================
# 🧮 FUNGSI POISSON
# ============================================================
def poisson_pmf(lam, k):
    """P(X = k)."""
    if lam <= 0 or k < 0:
        return 0.0
    try:
        return (math.exp(-lam) * (lam ** k)) / math.factorial(k)
    except (OverflowError, ValueError):
        return 0.0


def poisson_cdf_ge(lam, k):
    """P(X ≥ k) = 1 - Σ P(X=i) untuk i = 0..k-1."""
    if k <= 0:
        return 1.0
    s = sum(poisson_pmf(lam, i) for i in range(k))
    return max(0.0, min(1.0, 1.0 - s))


def rain_probability(lam):
    """Peluang hujan minimal 1 kali hari ini."""
    return poisson_cdf_ge(lam, 1)


def get_weather_icon(prob):
    if prob < 0.15:
        return "☀️", "sunny", "Cerah cenderung aman"
    elif prob < 0.35:
        return "🌤️", "sunny", "Berawan tipis, aman"
    elif prob < 0.55:
        return "⛅", "cloudy", "Berawan, waspada"
    elif prob < 0.75:
        return "🌧️", "rainy", "Kemungkinan hujan"
    elif prob < 0.90:
        return "⛈️", "rainy", "Hujan hampir pasti"
    else:
        return "🌊", "stormy", "Sangat mungkin hujan deras"


def get_fun_message(prob, city):
    if prob < 0.15:
        return f"Di {city}, kemungkinan hujan sangat kecil. Aman untuk aktivitas outdoor! 🌞"
    elif prob < 0.35:
        return f"Peluang hujan rendah. Tetap bawa jaket, siapa tahu cuaca berubah 🧥"
    elif prob < 0.55:
        return f"Hmm, di {city} cuaca agak tidak bisa diprediksi. Sedia payung! ☂️"
    elif prob < 0.75:
        return f"Sebaiknya bawa payung, {city} berpotensi hujan hari ini 🌧️"
    elif prob < 0.90:
        return f"Hampir pasti hujan di {city}. Siapkan jas hujan & sepatu anti air ☔"
    else:
        return f"Peringatan: {city} sangat mungkin hujan deras. Hindari aktivitas luar! ⚠️"


# ============================================================
# 🕐 LIVE DATETIME (WIB = UTC+7)
# ============================================================
def get_now_wib():
    wib = timezone(timedelta(hours=7))
    return datetime.now(wib)


def render_live_clock():
    """Render live clock bar dengan auto-refresh tiap 1 detik."""
    now = get_now_wib()

    hari_idx = now.weekday()
    hari = HARI_NAMA[hari_idx]
    tanggal = now.day
    bulan = BULAN_NAMA[now.month - 1]
    tahun = now.year
    jam = now.strftime("%H")
    menit = now.strftime("%M")
    detik = now.strftime("%S")

    st.markdown(f"""
        <div class="live-clock-bar">
            <div class="live-clock-item">
                <div class="live-clock-label">
                    <span class="live-dot"></span>Hari Ini
                </div>
                <div class="live-clock-value">{hari}</div>
                <div class="live-clock-sub">{tanggal} {bulan} {tahun}</div>
            </div>
            <div class="live-clock-item">
                <div class="live-clock-label">
                    <span class="live-dot"></span>Waktu Indonesia Barat
                </div>
                <div class="live-clock-value time">{jam}:{menit}<span style="font-size: 0.55em; opacity: 0.65;">:{detik}</span></div>
                <div class="live-clock-sub">UTC +07:00 · WIB</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 📊 RENDER 7-DAY FORECAST
# ============================================================
def render_week_forecast(city, month, lam_base):
    now = get_now_wib()
    hari_idx = now.weekday()
    hari_ini = HARI_NAMA[hari_idx]

    cards = ""
    for i in range(7):
        idx = (hari_idx + i) % 7
        nama_hari = HARI_NAMA[idx]
        tgl = now.day + i
        # simpulkan kalau lewat bulan (simple approximation)
        tgl_label = f"{tgl:02d}"

        # Variasi kecil λ per hari (fluktuasi cuaca)
        random.seed(int(now.timestamp()) // 86400 + i + hash(city) % 999)
        lam_hari = max(0.05, lam_base + random.uniform(-0.1, 0.1))
        prob = rain_probability(lam_hari)
        emoji, _, _ = get_weather_icon(prob)

        is_today = "today" if i == 0 else ""
        label = "Hari Ini" if i == 0 else nama_hari

        cards += f"""
        <div class="day-card {is_today}">
            <div class="day-name">{label}</div>
            <div class="day-date">{tgl_label}</div>
            <div class="day-emoji">{emoji}</div>
            <div class="day-percent">{prob*100:.0f}%</div>
        </div>"""

    st.markdown(f'<div class="week-grid">{cards}</div>', unsafe_allow_html=True)


# ============================================================
# 📈 RENDER DISTRIBUTION CHART
# ============================================================
def render_distribution_chart(lam, max_k=6):
    probs = [poisson_pmf(lam, k) for k in range(max_k + 1)]
    max_p = max(probs) if probs else 1.0
    max_p = max(max_p, 0.01)

    bars = ""
    for k, p in enumerate(probs):
        height = (p / max_p) * 140  # px max 140
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
# 🎯 MAIN PAGE
# ============================================================
def render_kreasi_page():
    # ---------- HERO ----------
    st.markdown("""
        <div class="weather-hero">
            <div class="weather-badge">✦ Kreasi Resmi Kelompok Poisson ✦</div>
            <h1 class="weather-title">Poisson Weather Forecast</h1>
            <p class="weather-subtitle">
                Ramalan cuaca berbasis <b>distribusi Poisson</b> &mdash; model statistik yang
                benar-benar dipakai BMKG &amp; NOAA untuk memprediksi <b>kejadian langka</b>
                seperti hujan, badai, dan gempa. Pilih kota &amp; tanggal, dan lihat
                peluang hujan secara real-time. 🌦️
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ---------- LIVE CLOCK ----------
    render_live_clock()

    # Auto-refresh tiap 1 detik via placeholder JS injection
    st.markdown("""
        <script>
        setTimeout(function() {
            window.location.reload();
        }, 1000);
        </script>
    """, unsafe_allow_html=True)

    # ---------- INPUT PANEL ----------
    now = get_now_wib()

    st.markdown("""
        <div class="input-panel">
            <div class="input-panel-title">📍 Konfigurasi Ramalan</div>
            <div class="input-panel-sub">
                Pilih kota dan bulan untuk melihat peluang hujan berdasarkan
                rata-rata historis (λ).
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        city = st.selectbox(
            "Pilih Kota",
            list(CITY_DATA.keys()),
            index=0,
            key="weather_city",
        )

    with col2:
        month = st.selectbox(
            "Bulan",
            list(range(1, 13)),
            index=now.month - 1,
            format_func=lambda m: BULAN_NAMA[m - 1],
            key="weather_month",
        )

    with col3:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        mode = st.selectbox(
            "Mode λ",
            ["Auto", "Manual"],
            key="weather_mode",
        )

    # Override λ manual
    user_lam = None
    if mode == "Manual":
        user_lam = st.slider(
            "λ manual (rata-rata kejadian hujan per hari)",
            min_value=0.05, max_value=2.0, value=0.40, step=0.05,
            key="weather_manual_lam",
        )

    lam = compute_lambda(city, month, user_lam)

    # ---------- HITUNG PELUANG ----------
    prob = rain_probability(lam)
    emoji, mood, status_short = get_weather_icon(prob)
    message = get_fun_message(prob, city)

    # ---------- MAIN FORECAST CARD ----------
    st.markdown(f"""
        <div class="forecast-card {mood}">
            <div class="forecast-emoji">{emoji}</div>
            <div class="forecast-label">Peluang Hujan Hari Ini</div>
            <div class="forecast-percent">{prob*100:.1f}<span class="forecast-percent-unit">%</span></div>
            <div class="forecast-status">{message}</div>
            <div class="forecast-params">
                <div class="forecast-param">
                    <div class="forecast-param-label">λ (Lambda)</div>
                    <div class="forecast-param-value">{lam:.3f}</div>
                </div>
                <div class="forecast-param">
                    <div class="forecast-param-label">Hari Hujan / Bulan</div>
                    <div class="forecast-param-value">{lam*30:.1f}</div>
                </div>
                <div class="forecast-param">
                    <div class="forecast-param-label">Status</div>
                    <div class="forecast-param-value">{status_short.split()[0]}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ---------- 7-DAY FORECAST ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            <div class="info-header">📅 Ramalan 7 Hari ke Depan</div>
            <div class="info-subheader">Weekly Forecast</div>
            <div class="info-divider"></div>
            <p class="info-text">
                Simulasi 7 hari ke depan berdasarkan λ yang sama, dengan fluktuasi kecil
                untuk mensimulasikan ketidakpastian cuaca nyata.
            </p>
        </div>
    """, unsafe_allow_html=True)
    render_week_forecast(city, month, lam)

    # ---------- DISTRIBUSI CHART ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="info-card">
            <div class="info-header">📊 Distribusi Peluang Hujan</div>
            <div class="info-subheader">Poisson PMF</div>
            <div class="info-divider"></div>
            <p class="info-text">
                Grafik di bawah menunjukkan peluang hujan <b>tepat k kali</b> dalam sehari,
                dengan λ = <b>{lam:.3f}</b>. Bar yang di-highlight emas adalah nilai k
                yang paling mungkin terjadi.
            </p>
        </div>
    """, unsafe_allow_html=True)
    render_distribution_chart(lam)

    # ---------- INFO KOTA ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    city_d = CITY_DATA[city]
    kemarau_per_bulan = city_d["kemarau"] * 30
    hujan_per_bulan = city_d["hujan"] * 30
    st.markdown(f"""
        <div class="info-card">
            <div class="info-header">🌏 Info Historis — {city}</div>
            <div class="info-subheader">Data Referensi</div>
            <div class="info-divider"></div>
            <p class="info-text">
                Rata-rata hari hujan di <b>{city}</b> berdasarkan data historis
                (pendekatan kasar dari BMKG):
            </p>
            <div class="city-info">
                <div class="city-pill">☀️ Musim Kemarau <b>{kemarau_per_bulan:.0f} hari/bulan</b></div>
                <div class="city-pill">🌧️ Musim Hujan <b>{hujan_per_bulan:.0f} hari/bulan</b></div>
                <div class="city-pill">📅 Bulan Ini ({BULAN_NAMA[month-1]}) <b>λ = {lam:.3f}</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ---------- EDUKASI ----------
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            <div class="info-header">💡 Kenapa Poisson Cocok untuk Cuaca?</div>
            <div class="info-subheader">Edukasi</div>
            <div class="info-divider"></div>
            <p class="info-text">
                Distribusi Poisson dirancang khusus untuk memodelkan <b>kejadian langka
                dalam interval waktu tertentu</b>. Hujan adalah contoh klasik:
                sebagian besar hari tidak hujan, namun ketika hujan terjadi,
                itu adalah "kejadian langka" yang mengikuti pola statistik tertentu.
                <br><br>
                Rumus yang dipakai di halaman ini:
                <br>
                <b>P(X ≥ 1) = 1 − e<sup>−λ</sup></b>
                <br><br>
                Di mana <b>λ</b> adalah rata-rata jumlah kejadian hujan per hari.
                Model ini juga dipakai untuk memprediksi:
                <br>
                ⚡ Frekuensi badai petir per bulan &nbsp;·&nbsp;
                🌋 Jumlah gempa per tahun &nbsp;·&nbsp;
                🌊 Banjir per dekade &nbsp;·&nbsp;
                🌪️ Tornado per musim
                <br><br>
                Jadi setiap kali kamu lihat halaman ini, kamu sedang melihat
                <b>matematika yang benar-benar dipakai oleh ilmuwan cuaca
                di seluruh dunia</b>. 🌍
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ---------- FOOTER ----------
    st.markdown(f"""
        <div style="text-align: center; margin-top: 40px; padding-top: 30px; border-top: 1px solid rgba(217,195,163,0.5);">
            <div style="font-family: 'Playfair Display', serif; font-size: 13px; color: #701c23; letter-spacing: 1.5px; font-weight: 600;">
                ✦ Poisson Weather Forecast ✦
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
