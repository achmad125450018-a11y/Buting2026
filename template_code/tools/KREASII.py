# ============================================================
# 🎲 KREASI POISSON + 🎮 POISSON TIC-TAC-TOE
# File: kreasi.py
# Jalankan: streamlit run kreasi.py
# Atau: import dari app utama dengan `from kreasi import render_kreasi_page`
# ============================================================

import streamlit as st
import math
import random

# ============================================================
# 🎨 PREMIUM CSS — POISSON EDITION
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

/* ---------- TITLE ---------- */
.centered-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-weight: 800;
    font-size: 3em !important;
    letter-spacing: 1px;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
    display: block;
}
.centered-title::after {
    content: '';
    display: block;
    width: 90px;
    height: 3px;
    margin: 14px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent);
    border-radius: 3px;
}

/* ---------- GENERIC CARD ---------- */
.profile-card {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 28px 32px;
    border-radius: 20px;
    box-shadow:
        0 1px 0 rgba(255,255,255,0.9) inset,
        0 10px 30px rgba(112,28,35,0.08),
        0 2px 8px rgba(112,28,35,0.04);
    border: 1px solid rgba(217,195,163,0.55);
    margin-bottom: 22px;
    position: relative;
    overflow: hidden;
}
.profile-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.profile-card::after {
    content: '';
    position: absolute;
    top: -30px; right: -30px;
    width: 140px; height: 140px;
    background: radial-gradient(circle, rgba(217,195,163,0.28) 0%, transparent 70%);
    pointer-events: none;
}
.profile-header {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: #701c23;
    margin-bottom: 6px;
    letter-spacing: 0.3px;
    line-height: 1.25;
    position: relative;
    z-index: 1;
}
.profile-subheader {
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
    position: relative;
    z-index: 1;
}
.profile-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d9c3a3, transparent);
    margin: 4px 0 16px 0;
    position: relative;
    z-index: 1;
}
.quote-box {
    position: relative;
    z-index: 1;
    margin-top: 14px;
    padding: 14px 18px 14px 22px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(112,28,35,0.04) 0%, rgba(217,195,163,0.10) 100%);
    border: 1px solid rgba(217,195,163,0.45);
}
.quote-box::before {
    content: '"';
    position: absolute;
    top: -6px;
    left: 8px;
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    color: rgba(112,28,35,0.15);
    line-height: 1;
}
.quote-label {
    display: block;
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: #701c23;
    margin-bottom: 4px;
}
.quote-text {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 13.5px;
    line-height: 1.6;
    color: #4e1318;
}

/* ============================================================
   KREASI HERO
   ============================================================ */
.kreasi-hero {
    text-align: center;
    margin-bottom: 40px;
    padding: 50px 30px;
    background:
        radial-gradient(circle at 50% 0%, rgba(217,195,163,0.35) 0%, transparent 60%),
        linear-gradient(160deg, #ffffff 0%, #fdf9f3 100%);
    border-radius: 24px;
    border: 1px solid rgba(217,195,163,0.7);
    box-shadow: 0 10px 30px rgba(112,28,35,0.08);
    position: relative;
    overflow: hidden;
}
.kreasi-hero::before {
    content: 'λ';
    position: absolute;
    top: -40px; right: 30px;
    font-family: 'Playfair Display', serif;
    font-size: 180px;
    color: rgba(112,28,35,0.06);
    line-height: 1;
    pointer-events: none;
}
.kreasi-badge {
    display: inline-block;
    padding: 6px 18px;
    background: linear-gradient(135deg, rgba(217,195,163,0.4), rgba(217,195,163,0.15));
    border: 1px solid rgba(217,195,163,0.8);
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #701c23;
    margin-bottom: 18px;
}
.kreasi-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.6em;
    font-weight: 800;
    color: #701c23;
    margin: 0 0 10px 0;
    letter-spacing: 0.4px;
}
.kreasi-subtitle {
    font-size: 15px;
    color: #6b5a52;
    max-width: 620px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ============================================================
   POISSON CALCULATOR RESULT
   ============================================================ */
.poisson-result {
    background:
        radial-gradient(circle at 20% 20%, rgba(217,195,163,0.18) 0%, transparent 55%),
        linear-gradient(150deg, #701c23 0%, #4e1318 100%);
    padding: 40px 30px;
    border-radius: 22px;
    color: #f4f0eb;
    text-align: center;
    box-shadow: 0 20px 50px rgba(112,28,35,0.28);
    position: relative;
    overflow: hidden;
    margin-top: 20px;
}
.poisson-result::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(217,195,163,0.15) 1px, transparent 1px);
    background-size: 14px 14px;
    opacity: 0.4;
    pointer-events: none;
}
.poisson-result-label {
    position: relative;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #d9c3a3;
    margin-bottom: 14px;
    z-index: 1;
}
.poisson-result-value {
    position: relative;
    font-family: 'Playfair Display', serif;
    font-size: 4.2em;
    font-weight: 900;
    color: #f4f0eb;
    line-height: 1;
    margin-bottom: 8px;
    letter-spacing: -1px;
    z-index: 1;
}
.poisson-result-formula {
    position: relative;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 14px;
    color: rgba(244,240,235,0.75);
    margin-bottom: 22px;
    z-index: 1;
}
.poisson-result-message {
    position: relative;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 16px;
    color: #f4f0eb;
    line-height: 1.6;
    max-width: 520px;
    margin: 0 auto;
    padding-top: 20px;
    border-top: 1px solid rgba(217,195,163,0.35);
    z-index: 1;
}

/* ============================================================
   POISSON ART GENERATOR
   ============================================================ */
.art-canvas-wrapper {
    display: flex;
    justify-content: center;
    padding: 20px;
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    border-radius: 20px;
    border: 1px solid rgba(217,195,163,0.55);
    box-shadow: 0 10px 30px rgba(112,28,35,0.08);
    margin-bottom: 20px;
}

/* ============================================================
   RANDOM QUOTE
   ============================================================ */
.random-quote-card {
    background:
        radial-gradient(circle at 30% 20%, rgba(217,195,163,0.2) 0%, transparent 55%),
        linear-gradient(150deg, #701c23 0%, #4e1318 100%);
    padding: 40px 36px;
    border-radius: 22px;
    color: #f4f0eb;
    text-align: center;
    box-shadow: 0 20px 50px rgba(112,28,35,0.28);
    position: relative;
    overflow: hidden;
    margin-top: 20px;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.random-quote-card::before {
    content: '"';
    position: absolute;
    top: -20px;
    left: 20px;
    font-family: 'Playfair Display', serif;
    font-size: 140px;
    color: rgba(217,195,163,0.18);
    line-height: 1;
}
.random-quote-text {
    position: relative;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 20px;
    color: #f4f0eb;
    line-height: 1.7;
    z-index: 1;
    margin-bottom: 18px;
}
.random-quote-author {
    position: relative;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #d9c3a3;
    z-index: 1;
}

/* ============================================================
   POISSON TIC-TAC-TOE
   ============================================================ */
.ttt-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
    padding: 30px 20px;
}

.ttt-board {
    display: grid;
    grid-template-columns: repeat(3, 110px);
    grid-template-rows: repeat(3, 110px);
    gap: 10px;
    padding: 14px;
    background: linear-gradient(135deg, #701c23 0%, #4e1318 100%);
    border-radius: 22px;
    box-shadow:
        0 24px 50px rgba(112,28,35,0.35),
        0 0 0 1px rgba(217,195,163,0.5) inset;
    position: relative;
    overflow: hidden;
    margin: 0 auto;
}
.ttt-board::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(217,195,163,0.12) 1px, transparent 1px);
    background-size: 14px 14px;
    opacity: 0.5;
    pointer-events: none;
}
.ttt-cell {
    background: linear-gradient(160deg, #ffffff 0%, #fdf9f3 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 64px;
    font-weight: 900;
    color: #701c23;
    transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    border: 1px solid rgba(217,195,163,0.5);
    position: relative;
    box-shadow: 0 4px 12px rgba(112,28,35,0.10);
}
.ttt-cell.x-mark {
    color: #701c23;
    text-shadow: 0 3px 12px rgba(112,28,35,0.28);
}
.ttt-cell.o-mark {
    color: #b8912e;
    text-shadow: 0 3px 12px rgba(184,145,46,0.35);
}
.ttt-cell.winning {
    background: linear-gradient(160deg, #e8c874 0%, #b8912e 100%) !important;
    color: #ffffff !important;
    text-shadow: 0 3px 12px rgba(0,0,0,0.25);
    animation: pulse-win 1s ease-in-out infinite alternate;
}
@keyframes pulse-win {
    from { transform: scale(1); }
    to { transform: scale(1.06); }
}

.ttt-status {
    font-family: 'Playfair Display', serif;
    font-size: 1.5em;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 0.4px;
    text-align: center;
    padding: 12px 28px;
    background: linear-gradient(135deg, rgba(217,195,163,0.15), rgba(217,195,163,0.05));
    border: 1px solid rgba(217,195,163,0.5);
    border-radius: 999px;
    box-shadow: 0 4px 12px rgba(112,28,35,0.06);
    margin: 0 auto;
    display: block;
    width: fit-content;
}

.ttt-lambda-panel {
    width: 100%;
    max-width: 500px;
    padding: 20px 24px;
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    border-radius: 18px;
    border: 1px solid rgba(217,195,163,0.6);
    box-shadow: 0 10px 24px rgba(112,28,35,0.08);
    margin: 0 auto;
}
.ttt-lambda-title {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
    text-align: center;
}
.ttt-lambda-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
}
.ttt-lambda-cell {
    padding: 8px;
    background: rgba(217,195,163,0.15);
    border-radius: 8px;
    text-align: center;
    font-size: 11px;
    font-weight: 600;
    color: #701c23;
    border: 1px solid rgba(217,195,163,0.4);
    transition: all 0.3s ease;
}
.ttt-lambda-cell.high {
    background: linear-gradient(135deg, rgba(184,145,46,0.25), rgba(232,200,116,0.15));
    border-color: rgba(184,145,46,0.6);
    color: #4e1318;
}
.ttt-lambda-cell.medium {
    background: rgba(217,195,163,0.25);
}
.ttt-lambda-cell.low {
    background: rgba(217,195,163,0.08);
    color: #a89790;
}
.ttt-lambda-value {
    display: block;
    font-family: 'Playfair Display', serif;
    font-size: 15px;
    font-weight: 800;
    margin-top: 2px;
}

.ttt-scores {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 10px;
}
.ttt-score-card {
    padding: 12px 22px;
    border-radius: 14px;
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    border: 1px solid rgba(217,195,163,0.55);
    text-align: center;
    min-width: 100px;
    box-shadow: 0 4px 12px rgba(112,28,35,0.06);
}
.ttt-score-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: #a89790;
    margin-bottom: 4px;
}
.ttt-score-value {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-weight: 800;
    color: #701c23;
}

.ttt-legend {
    font-size: 12px;
    color: #6b5a52;
    text-align: center;
    max-width: 500px;
    line-height: 1.6;
    margin: 8px auto 0 auto;
}
.ttt-legend b { color: #701c23; }

/* ---------- SCROLLBAR ---------- */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #f4f0eb; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #701c23, #a8323d);
    border-radius: 10px;
    border: 2px solid #f4f0eb;
}

.block-container { padding-top: 2rem !important; }

/* ---------- STREAMLIT BUTTON OVERRIDE ---------- */
.stButton > button {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    border-radius: 10px;
    border: 1px solid rgba(217,195,163,0.7);
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    color: #701c23;
    transition: all 0.25s ease;
    padding: 10px 16px;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: #ffffff;
    border-color: #701c23;
    box-shadow: 0 6px 18px rgba(112,28,35,0.28);
}
.stButton > button:disabled {
    background: rgba(217,195,163,0.15);
    color: #a89790;
    border-color: rgba(217,195,163,0.3);
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 📊 FUNGSI KALKULATOR POISSON
# ============================================================
def poisson_probability(lam, k):
    """Hitung P(X=k) untuk distribusi Poisson dengan λ."""
    if lam < 0 or k < 0:
        return 0.0
    try:
        return (math.exp(-lam) * (lam ** k)) / math.factorial(k)
    except (OverflowError, ValueError):
        return 0.0


def get_fun_message(prob):
    """Return pesan lucu berdasarkan nilai probabilitas."""
    if prob < 0.01:
        return "Peluangnya setipis senyum kamu ke aku 😔 hampir mustahil!"
    elif prob < 0.05:
        return "Kemungkinannya kecil, tapi bukan berarti tidak mungkin. Semangat! 💪"
    elif prob < 0.20:
        return "Lumayan langka nih, kayak ketemu dosen killer di jam konsultasi 🌅"
    elif prob < 0.50:
        return "Masih di bawah setengah, tapi udah cukup realistis kok ✨"
    elif prob < 0.80:
        return "Wah lumayan sering ya! Pasti bakal kejadian dalam waktu dekat 🎯"
    elif prob < 0.99:
        return "Hampir pasti terjadi! Kamu beruntung banget hari ini 🍀"
    else:
        return "Sudah hampir pasti 100%! Seperti kepastian tugas selalu ada 📚"


def render_kalkulator_poisson():
    st.markdown("""
        <div class="kreasi-hero">
            <div class="kreasi-badge">✦ Poisson Interactive ✦</div>
            <h1 class="kreasi-title">Kalkulator Poisson</h1>
            <p class="kreasi-subtitle">
                Karena nama kelompok kami terinspirasi dari distribusi Poisson dalam statistika,
                kami hadirkan kalkulator kecil ini untuk menghitung peluang kejadian langka
                di sekitar kita. Coba masukkan angka dan lihat hasilnya! 🎲
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        lam = st.number_input(
            "Rata-rata kejadian (λ)",
            min_value=0.1,
            max_value=50.0,
            value=2.5,
            step=0.1,
            help="Contoh: rata-rata berapa kali kejadian ini terjadi per hari.",
            key="calc_lam",
        )

    with col_b:
        k = st.number_input(
            "Jumlah kejadian yang mau dihitung (k)",
            min_value=0,
            max_value=50,
            value=3,
            step=1,
            help="Berapa kali kamu ingin kejadian itu terjadi.",
            key="calc_k",
        )

    prob = poisson_probability(lam, k)
    percent = prob * 100
    message = get_fun_message(prob)

    st.markdown(f"""
        <div class="poisson-result">
            <div class="poisson-result-label">Peluang Kejadian</div>
            <div class="poisson-result-value">{percent:.2f}%</div>
            <div class="poisson-result-formula">P(X = {k}) = (e<sup>-{lam}</sup> · {lam}<sup>{k}</sup>) / {k}!</div>
            <div class="poisson-result-message">{message}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

    st.markdown("""
        <div class="profile-card">
            <div class="profile-header">Apa itu Distribusi Poisson?</div>
            <div class="profile-subheader">Fun Fact</div>
            <div class="profile-divider"></div>
            <p style="font-size: 14px; line-height: 1.85; color: #3a2f2b; margin: 0;">
                Distribusi Poisson adalah distribusi probabilitas yang menghitung peluang
                terjadinya sejumlah kejadian langka dalam interval waktu atau ruang tertentu.
                Contoh nyata: jumlah panggilan telepon per jam, jumlah kecelakaan per hari,
                jumlah gempa bumi per tahun.
                <br><br>
                Rumusnya sederhana namun elegan: <b>P(X = k) = (λ<sup>k</sup> · e<sup>-λ</sup>) / k!</b>
                Di mana <b>λ</b> (lambda) adalah rata-rata kejadian, dan <b>k</b> adalah jumlah yang ingin dihitung.
                Itulah alasan kami memilih nama <b>Poisson</b> &mdash; karena kejadian langka adalah
                hal yang kami rayakan. ✨
            </p>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 💭 FUNGSI RANDOM QUOTE POISSON
# ============================================================
POISSON_QUOTES = [
    "Kebetulan adalah cara Tuhan menyapa tanpa mengetuk pintu.",
    "Hidup ini seperti distribusi Poisson — kejadian langka justru yang paling berkesan.",
    "Setiap pertemuan adalah λ yang tak terduga.",
    "Jangan takut dengan probabilitas kecil. Angka 0.01% tetap bukan nol.",
    "Statistika mengajarkan kita: tidak ada yang benar-benar mustahil, hanya belum terjadi.",
    "Hal-hal besar dalam hidup jarang datang dua kali — itulah definisi kejadian langka.",
    "Jika semesta punya distribusi, mungkin ia sedang menghitung kebahagiaan kita.",
    "Pertemuan kita hari ini punya peluang yang sangat kecil — dan itu membuatnya spesial.",
    "Kejadian langka adalah alasan kita tetap percaya pada keajaiban.",
    "Dalam setiap λ, tersimpan cerita yang belum kita tulis.",
    "Kebetulan yang berulang bukan lagi kebetulan — itu pola.",
    "Poisson mengajarkan: kejadian jarang bukan berarti tidak akan pernah terjadi.",
    "Hidup adalah eksperimen dengan λ yang selalu berubah.",
    "Percayalah, kejadian terbaikmu mungkin sedang menunggu giliran di ujung distribusi.",
    "Kita tidak bisa prediksi kapan, tapi kita bisa siap menyambutnya.",
]


def render_random_quote():
    st.markdown("""
        <div class="profile-card">
            <div class="profile-header">💭 Poisson Says</div>
            <div class="profile-subheader">Random Quote</div>
            <div class="profile-divider"></div>
            <p style="font-size: 13.5px; line-height: 1.85; color: #3a2f2b; margin: 0 0 16px 0;">
                Klik tombol di bawah untuk mendapatkan kutipan acak tentang <b>kebetulan,
                kejadian langka, dan keajaiban kecil</b> dalam hidup &mdash; semua terinspirasi
                dari filosofi distribusi Poisson.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if "quote_index" not in st.session_state:
        st.session_state.quote_index = random.randint(0, len(POISSON_QUOTES) - 1)

    col_left, col_mid, col_right = st.columns([1, 2, 1])
    with col_mid:
        if st.button("🎲 Acak Quote Baru", use_container_width=True):
            st.session_state.quote_index = random.randint(0, len(POISSON_QUOTES) - 1)
            st.rerun()

    quote_text = POISSON_QUOTES[st.session_state.quote_index]
    st.markdown(f"""
        <div class="random-quote-card">
            <div class="random-quote-text">{quote_text}</div>
            <div class="random-quote-author">— Poisson, Kelompok Kating —</div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🎨 FUNGSI POISSON ART GENERATOR
# ============================================================
def render_poisson_art():
    st.markdown("""
        <div class="profile-card">
            <div class="profile-header">🎨 Poisson Art Generator</div>
            <div class="profile-subheader">Generative Art</div>
            <div class="profile-divider"></div>
            <p style="font-size: 13.5px; line-height: 1.85; color: #3a2f2b; margin: 0;">
                Setiap nilai <b>λ</b> menghasilkan pola seni yang berbeda. Titik-titik mewakili
                kejadian acak yang tersebar menurut distribusi Poisson. Semakin tinggi λ,
                semakin padat "kejadiannya". Setiap λ adalah karya yang unik — begitu juga
                setiap momen dalam hidup kita. ✨
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        lam_art = st.slider("λ (lambda)", 0.5, 20.0, 8.0, 0.5, key="art_lam")
    with col_b:
        n_points = st.slider("Jumlah titik", 50, 800, 400, 50, key="art_npoints")
    with col_c:
        color_theme = st.selectbox(
            "Warna",
            ["Maroon & Cream", "Gold & Dark", "Ivory & Wine"],
            key="art_theme",
        )

    # Generate scatter
    if color_theme == "Maroon & Cream":
        palette = ["#701c23", "#a8323d", "#d9c3a3", "#4e1318", "#b8912e"]
        bg_color = "#fdf9f3"
    elif color_theme == "Gold & Dark":
        palette = ["#b8912e", "#e8c874", "#f4f0eb", "#701c23", "#2d0a0d"]
        bg_color = "#2d0a0d"
    else:
        palette = ["#f4f0eb", "#d9c3a3", "#701c23", "#a8323d", "#fdfbf8"]
        bg_color = "#701c23"

    # Koordinat acak (uniform, tapi ukuran/opacity proporsional λ)
    random.seed(int(lam_art * 100) + n_points + hash(color_theme) % 1000)
    xs = [random.random() for _ in range(n_points)]
    ys = [random.random() for _ in range(n_points)]
    sizes = [max(4, random.gauss(lam_art * 2, lam_art * 0.6)) for _ in range(n_points)]
    colors = [random.choice(palette) for _ in range(n_points)]
    opacities = [min(1.0, max(0.15, random.random() * 0.9)) for _ in range(n_points)]

    # Render via HTML/SVG
    svg_size = 500
    circles = ""
    for x, y, s, c, o in zip(xs, ys, sizes, colors, opacities):
        cx = x * svg_size
        cy = y * svg_size
        r = min(20, max(2, s))
        circles += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{c}" opacity="{o:.2f}" />'

    st.markdown(f"""
        <div class="art-canvas-wrapper">
            <svg width="{svg_size}" height="{svg_size}" viewBox="0 0 {svg_size} {svg_size}"
                 style="border-radius: 14px; background: {bg_color}; box-shadow: inset 0 0 40px rgba(0,0,0,0.08);">
                {circles}
            </svg>
        </div>
        <div style="text-align: center; font-family: 'Playfair Display', serif; font-style: italic; font-size: 14px; color: #6b5a52;">
            "Karya untuk λ = {lam_art} · {n_points} titik"
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# 🎮 POISSON TIC-TAC-TOE
# ============================================================
def ttt_new_board():
    return [""] * 9


def ttt_check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], [a, b, c]
    if all(board):
        return "draw", []
    return None, []


def ttt_lambda_map(board):
    base_lambda = [3.0, 2.0, 3.0,
                   2.0, 4.0, 2.0,
                   3.0, 2.0, 3.0]
    lam_map = {}
    for i in range(9):
        if board[i] != "":
            lam_map[i] = 0.0
            continue
        lam = base_lambda[i]
        r1, c1 = divmod(i, 3)
        # Bonus tetangga O dan X
        for j in range(9):
            if board[j] == "O":
                r2, c2 = divmod(j, 3)
                if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1 and i != j:
                    lam += 0.6
            elif board[j] == "X":
                r2, c2 = divmod(j, 3)
                if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1 and i != j:
                    lam += 0.4
        # Bonus besar: win / block move
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]:
            if i in line:
                o_count = sum(1 for p in line if board[p] == "O")
                x_count = sum(1 for p in line if board[p] == "X")
                empty = sum(1 for p in line if board[p] == "")
                if x_count == 0 and o_count == 2 and empty == 1:
                    lam += 15.0
                elif o_count == 0 and x_count == 2 and empty == 1:
                    lam += 10.0
                elif x_count == 0 and o_count == 1 and empty == 2:
                    lam += 1.5
        lam_map[i] = max(lam, 0.1)
    return lam_map


def ttt_ai_move(board):
    lam_map = ttt_lambda_map(board)
    positions = [i for i, v in lam_map.items() if v > 0]
    if not positions:
        return None
    weights = [lam_map[i] for i in positions]
    return random.choices(positions, weights=weights, k=1)[0]


def ttt_render_board(board, winning_line=None):
    cells_html = ""
    for i in range(9):
        val = board[i]
        cls = "ttt-cell"
        if val == "X":
            cls += " x-mark"
        elif val == "O":
            cls += " o-mark"
        if winning_line and i in winning_line:
            cls += " winning"
        symbol = val if val else "&nbsp;"
        cells_html += f'<div class="{cls}">{symbol}</div>'
    st.markdown(f'<div class="ttt-board">{cells_html}</div>', unsafe_allow_html=True)


def ttt_render_lambda_panel(lam_map):
    cells = ""
    for i in range(9):
        lam = lam_map.get(i, 0.0)
        if lam == 0:
            cells += '<div class="ttt-lambda-cell low">—</div>'
        else:
            cls = "high" if lam >= 4 else ("medium" if lam >= 2.5 else "low")
            cells += f'<div class="ttt-lambda-cell {cls}">λ<span class="ttt-lambda-value">{lam:.1f}</span></div>'
    st.markdown(f"""
        <div class="ttt-lambda-panel">
            <div class="ttt-lambda-title">🧠 Otak AI — Peta λ (Poin Strategis)</div>
            <div class="ttt-lambda-grid">{cells}</div>
        </div>
    """, unsafe_allow_html=True)


def render_ttt_game():
    # Init session state
    for key, default in [
        ("ttt_board", ttt_new_board()),
        ("ttt_score_x", 0),
        ("ttt_score_o", 0),
        ("ttt_score_draw", 0),
        ("ttt_finished", False),
        ("ttt_winner", None),
        ("ttt_winning_line", []),
    ]:
        if key not in st.session_state:
            st.session_state[key] = default

    # Hero
    st.markdown("""
        <div class="kreasi-hero">
            <div class="kreasi-badge">✦ Poisson Games ✦</div>
            <h1 class="kreasi-title">Poisson Tic-Tac-Toe</h1>
            <p class="kreasi-subtitle">
                Kamu melawan <b>AI λ</b> &mdash; sebuah AI yang memilih langkah berdasarkan
                distribusi Poisson. Setiap sel kosong punya nilai tarik (λ) yang berbeda.
                AI lebih sering memilih sel strategis, tapi kadang "blunder" juga.
                Bisa kamu kalahkan? 🎯
            </p>
        </div>
    """, unsafe_allow_html=True)

    board = st.session_state.ttt_board
    winner = st.session_state.ttt_winner
    winning_line = st.session_state.ttt_winning_line

    if winner == "X":
        status_text = "🎉 Kamu menang! AI λ kalah telak!"
    elif winner == "O":
        status_text = "🤖 AI λ menang! Coba lagi!"
    elif winner == "draw":
        status_text = "🤝 Seri! Pertandingan sengit!"
    else:
        status_text = "Giliran kamu (X) — klik tombol di bawah papan"

    st.markdown(f'<div style="text-align: center;"><div class="ttt-status">{status_text}</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # Papan visual
    ttt_render_board(board, winning_line)

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # Tombol kontrol (3x3 grid)
    st.markdown(
        "<div style='text-align: center; font-size: 12px; color: #6b5a52; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 12px;'>Pilih Sel</div>",
        unsafe_allow_html=True,
    )

    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            i = row * 3 + col
            with cols[col]:
                label = board[i] if board[i] else "·"
                disabled = st.session_state.ttt_finished or board[i] != ""
                if st.button(label, key=f"ttt_btn_{i}", disabled=disabled, use_container_width=True):
                    if not st.session_state.ttt_finished and board[i] == "":
                        # User move
                        st.session_state.ttt_board[i] = "X"
                        w, line = ttt_check_winner(st.session_state.ttt_board)
                        if w:
                            st.session_state.ttt_finished = True
                            st.session_state.ttt_winner = w
                            st.session_state.ttt_winning_line = line
                            if w == "X":
                                st.session_state.ttt_score_x += 1
                            elif w == "O":
                                st.session_state.ttt_score_o += 1
                            elif w == "draw":
                                st.session_state.ttt_score_draw += 1
                        else:
                            # AI move
                            ai_idx = ttt_ai_move(st.session_state.ttt_board)
                            if ai_idx is not None:
                                st.session_state.ttt_board[ai_idx] = "O"
                                w2, line2 = ttt_check_winner(st.session_state.ttt_board)
                                if w2:
                                    st.session_state.ttt_finished = True
                                    st.session_state.ttt_winner = w2
                                    st.session_state.ttt_winning_line = line2
                                    if w2 == "X":
                                        st.session_state.ttt_score_x += 1
                                    elif w2 == "O":
                                        st.session_state.ttt_score_o += 1
                                    elif w2 == "draw":
                                        st.session_state.ttt_score_draw += 1
                        st.rerun()

    # Panel λ AI
    st.markdown("<div style='margin-top: 34px;'></div>", unsafe_allow_html=True)
    lam_map = ttt_lambda_map(st.session_state.ttt_board)
    ttt_render_lambda_panel(lam_map)

    st.markdown("""
        <div class="ttt-legend">
            <b>λ tinggi</b> = sel strategis (tengah, sudut, atau bikin 3-in-a-row).<br>
            AI memilih dengan <b>probabilitas proporsional λ</b> &mdash; bukan selalu pilih yang tertinggi,
            jadi kadang blunder juga. 🤞
        </div>
    """, unsafe_allow_html=True)

    # Skor
    st.markdown("<div style='margin-top: 34px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="ttt-scores">
            <div class="ttt-score-card">
                <div class="ttt-score-label">Kamu (X)</div>
                <div class="ttt-score-value">{st.session_state.ttt_score_x}</div>
            </div>
            <div class="ttt-score-card">
                <div class="ttt-score-label">AI λ (O)</div>
                <div class="ttt-score-value">{st.session_state.ttt_score_o}</div>
            </div>
            <div class="ttt-score-card">
                <div class="ttt-score-label">Seri</div>
                <div class="ttt-score-value">{st.session_state.ttt_score_draw}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Tombol Reset
    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    col_reset, col_reset_all = st.columns(2)
    with col_reset:
        if st.button("🔄 Main Lagi", use_container_width=True, key="ttt_reset_game"):
            st.session_state.ttt_board = ttt_new_board()
            st.session_state.ttt_finished = False
            st.session_state.ttt_winner = None
            st.session_state.ttt_winning_line = []
            st.rerun()
    with col_reset_all:
        if st.button("🗑️ Reset Semua Skor", use_container_width=True, key="ttt_reset_all"):
            st.session_state.ttt_board = ttt_new_board()
            st.session_state.ttt_finished = False
            st.session_state.ttt_winner = None
            st.session_state.ttt_winning_line = []
            st.session_state.ttt_score_x = 0
            st.session_state.ttt_score_o = 0
            st.session_state.ttt_score_draw = 0
            st.rerun()


# ============================================================
# 🎯 MAIN — Render Semua Section
# ============================================================
def render_kreasi_page():
    """Entry point — panggil ini dari app utama atau langsung."""
    st.markdown("<h1 class='centered-title'>KREASI POISSON</h1>", unsafe_allow_html=True)

    # Section 1: Kalkulator
    render_kalkulator_poisson()

    st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

    # Section 2: Random Quote
    render_random_quote()

    st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

    # Section 3: Art Generator
    render_poisson_art()

    st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

    # Section 4: Tic-Tac-Toe
    render_ttt_game()


# ============================================================
# RUN (jika dijalankan langsung: `streamlit run kreasi.py`)
# ============================================================
if __name__ == "__main__":
    render_kreasi_page()
