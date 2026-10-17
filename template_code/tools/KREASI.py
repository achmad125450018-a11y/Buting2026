# tools/KREASI.py
import streamlit as st
import math
import html

# ============================================================
# 🎨 SUPER PREMIUM UI — KREASI POISSON EDITION
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

.kreasi-title {
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
.kreasi-title::after {
    content: '';
    display: block;
    width: 90px;
    height: 3px;
    margin: 14px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent);
    border-radius: 3px;
}
.kreasi-subtitle {
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
    letter-spacing: 0.3px;
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
    font-size: 22px;
    font-style: italic;
    color: #701c23;
    letter-spacing: 0.5px;
}

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
    font-size: 48px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 8px;
    position: relative;
}
.result-panel .rp-desc {
    font-size: 13.5px;
    line-height: 1.7;
    color: rgba(244,240,235,0.92);
    position: relative;
}

.prob-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-top: 14px;
}
.prob-row {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 14px;
    border-radius: 10px;
    background: rgba(217,195,163,0.10);
    border-left: 3px solid #d9c3a3;
    transition: background 0.25s ease;
}
.prob-row:hover {
    background: rgba(217,195,163,0.20);
}
.prob-row.highlight {
    background: rgba(112,28,35,0.12);
    border-left-color: #701c23;
}
.prob-label {
    min-width: 62px;
    font-size: 12px;
    font-weight: 700;
    color: #4e1318;
    letter-spacing: 0.3px;
}
.prob-bar-wrap {
    flex: 1;
    height: 12px;
    background: rgba(217,195,163,0.22);
    border-radius: 99px;
    overflow: hidden;
}
.prob-bar {
    height: 100%;
    background: linear-gradient(90deg, #701c23, #a8323d);
    border-radius: 99px;
}
.prob-value {
    min-width: 58px;
    text-align: right;
    font-size: 12px;
    font-weight: 700;
    color: #701c23;
    font-family: 'Playfair Display', serif;
}

.input-panel {
    padding: 4px 0;
}
.input-readout {
    font-size: 12px;
    color: #701c23;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 8px;
    padding: 10px 14px;
    background: rgba(217,195,163,0.15);
    border-radius: 10px;
    border-left: 3px solid #701c23;
}

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

.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #701c23 0%, #a8323d 100%) !important;
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
# 🧮 FUNGSI POISSON — PURE MATH, HEMAT MEMORI
# ============================================================
def poisson_pmf(k, lam):
    """P(X = k) = (λ^k · e^(-λ)) / k!"""
    if k < 0:
        return 0.0
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def poisson_cdf(k, lam):
    """P(X ≤ k) = Σ P(X=i) untuk i=0..k"""
    total = 0.0
    for i in range(k + 1):
        total += (lam ** i) * math.exp(-lam) / math.factorial(i)
    return total


# ============================================================
# HEADER
# ============================================================
st.markdown("<h1 class='kreasi-title'>PREDIKSI CUACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='kreasi-subtitle'>✦ Distribusi Poisson · Keluarga Poisson ✦</p>", unsafe_allow_html=True)


# ============================================================
# SECTION 1: PENJELASAN
# ============================================================
st.markdown("""
<div class="kreasi-card">
    <div class="card-title">Apa itu Distribusi Poisson?</div>
    <div class="card-sub">Teori Singkat</div>
    <div class="card-divider"></div>
    <div class="card-body">
        <b>Distribusi Poisson</b> adalah distribusi probabilitas diskrit yang menyatakan peluang
        terjadinya sejumlah <b>kejadian langka</b> dalam suatu interval waktu atau ruang tertentu,
        jika kejadian-kejadian tersebut terjadi secara <b>independen</b> dengan laju rata-rata <b>λ (lambda)</b>.
        <br><br>
        Dalam konteks cuaca, Poisson sangat cocok untuk memodelkan <b>jumlah hari hujan</b>
        atau <b>jumlah kejadian hujan ekstrem</b> pada rentang waktu tertentu, karena hujan
        termasuk fenomena langka yang terjadi secara acak dan independen antar hari.
    </div>
    <div class="formula-box">
        <div class="formula">P(X = k) = (λ<sup>k</sup> · e<sup>−λ</sup>) / k!</div>
    </div>
    <div class="card-body" style="font-size: 13px;">
        <b>k</b> = jumlah hari hujan yang diprediksi ·
        <b>λ</b> = rata-rata hari hujan per bulan ·
        <b>e</b> ≈ 2.71828
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SECTION 2: INPUT
# ============================================================
st.markdown("""
<div class="kreasi-card">
    <div class="card-title">Simulasi Prediksi Hujan</div>
    <div class="card-sub gold">Interactive Calculator</div>
    <div class="card-divider"></div>
    <div class="card-body">
        Atur rata-rata hari hujan per bulan di kotamu, lalu pilih berapa hari hujan
        yang ingin kamu ketahui peluangnya.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    lam = st.slider(
        "Rata-rata hari hujan per bulan (λ)",
        min_value=0.5, max_value=20.0, value=8.0, step=0.5,
    )
    st.markdown(
        f'<div class="input-readout">λ saat ini: {lam} hari/bulan</div>',
        unsafe_allow_html=True,
    )

with col2:
    k = st.slider(
        "Jumlah hari hujan yang diprediksi (k)",
        min_value=0, max_value=30, value=8, step=1,
    )
    st.markdown(
        f'<div class="input-readout">k saat ini: {k} hari</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# SECTION 3: HASIL
# ============================================================
if st.button("🌧️ Hitung Peluang", use_container_width=True):
    # Hitung probabilitas
    prob_exact = poisson_pmf(k, lam)
    prob_cdf = poisson_cdf(k, lam)
    prob_lebih = 1.0 - prob_cdf

    # Kategori
    if prob_exact >= 0.15:
        kategori, emoji = "Sangat Mungkin", "🌊"
    elif prob_exact >= 0.08:
        kategori, emoji = "Mungkin", "🌧️"
    elif prob_exact >= 0.03:
        kategori, emoji = "Kurang Mungkin", "☁️"
    else:
        kategori, emoji = "Sangat Langka", "🌤️"

    # Panel hasil
    st.markdown(
        f"""
    <div class="result-panel">
        <div class="rp-label">Peluang Tepat {k} Hari Hujan</div>
        <div class="rp-big">{prob_exact*100:.2f}%</div>
        <div class="rp-desc">
            {emoji} Kategori: <b style="color:#d9c3a3;">{kategori}</b><br>
            Dengan rata-rata <b>λ = {lam}</b> hari hujan per bulan, peluang tepat
            <b>{k} hari hujan</b> adalah <b>{prob_exact*100:.2f}%</b>.
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Distribusi bar chart (k = 0..min(20, max(k, lam*3)))
    max_k_display = min(20, max(k + 5, int(lam * 3) + 1))

    # Cari nilai maksimum probabilitas untuk scaling bar
    max_prob = max(poisson_pmf(i, lam) for i in range(max_k_display + 1))

    rows_html = ""
    for i in range(max_k_display + 1):
        p = poisson_pmf(i, lam)
        bar_width = (p / max_prob * 100) if max_prob > 0 else 0
        highlight_class = " highlight" if i == k else ""
        rows_html += (
            f'<div class="prob-row{highlight_class}">'
            f'<div class="prob-label">{i} hari</div>'
            f'<div class="prob-bar-wrap">'
            f'<div class="prob-bar" style="width: {bar_width:.1f}%;"></div>'
            f'</div>'
            f'<div class="prob-value">{p*100:.2f}%</div>'
            f'</div>'
        )

    st.markdown(
        f"""
    <div class="kreasi-card">
        <div class="card-title">Distribusi Peluang</div>
        <div class="card-sub">P(X = k) untuk k = 0 – {max_k_display}</div>
        <div class="card-divider"></div>
        <div class="prob-grid">{rows_html}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Interpretasi
    st.markdown(
        f"""
    <div class="kreasi-card">
        <div class="card-title">Interpretasi Hasil</div>
        <div class="card-sub gold">Analisis</div>
        <div class="card-divider"></div>
        <div class="card-body">
            📊 <b>Peluang tepat {k} hari hujan:</b> {prob_exact*100:.2f}%<br>
            📉 <b>Peluang ≤ {k} hari hujan:</b> {prob_cdf*100:.2f}%<br>
            📈 <b>Peluang &gt; {k} hari hujan:</b> {prob_lebih*100:.2f}%<br>
            🎯 <b>Kategori:</b> {emoji} {kategori}
            <br><br>
            <i>Catatan: Model Poisson mengasumsikan kejadian hujan bersifat independen.
            Di dunia nyata, cuaca bisa dipengaruhi banyak faktor lain — jadi hasil ini
            hanya gambaran probabilistik, bukan prediksi mutlak.</i>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

else:
    st.markdown(
        """
    <div class="kreasi-card" style="opacity: 0.7;">
        <div class="card-body" style="text-align: center; color: #6b5a52;">
            🌧️ <i>Klik tombol "Hitung Peluang" untuk melihat hasil prediksi</i>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============================================================
# SECTION 4: REFERENSI CEPAT
# ============================================================
st.markdown("""
<div class="kreasi-card" style="margin-top: 24px;">
    <div class="card-title">Referensi Cepat</div>
    <div class="card-sub">Contoh Nilai λ</div>
    <div class="card-divider"></div>
    <div class="card-body">
        <b>λ = 2–4</b> → daerah kering (misal Nusa Tenggara)<br>
        <b>λ = 8–12</b> → daerah tropis normal (misal Lampung)<br>
        <b>λ = 15–20</b> → daerah sangat basah (misal Kalimantan, Papua)<br>
        <br>
        <i>Nilai λ tiap daerah bisa berbeda tiap bulan, tergantung musim.</i>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div style="text-align: center; margin-top: 60px; padding: 20px; color: #a89790; font-size: 12px; letter-spacing: 1px;">
    ✦ KREASI · Prediksi Cuaca · Keluarga Poisson · HMSD Adyatama ITERA 2026 ✦
</div>
""", unsafe_allow_html=True)
