import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Website Kating | Bayesian",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS — WARNA SIDEBAR SESUAI FOTO REFERENSI & STYLE HALAMAN
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --navy: #102A56;
    --blue: #246BCE;
    --sky: #8EC5FC;
    --light: #EAF3FF;
    --border: #D8E7FA;
    --text: #334963;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--text);
}

.stApp {
    background: 
        radial-gradient(circle at 5% 5%, rgba(91,164,255,.17), transparent 35%),
        radial-gradient(circle at 95% 60%, rgba(36,107,206,.10), transparent 38%),
        linear-gradient(180deg, #F7FAFF 0%, #EAF2FC 100%);
    background-attachment: fixed;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}

/* ============================================================
   STYLING KELIR SIDEBAR SEPERTI PADA FOTO REFERENSI
   ============================================================ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A2252 0%, #0D2B68 40%, #154CB0 80%, #1B5FD1 100%) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

section[data-testid="stSidebar"] .stMarkdown {
    color: #FFFFFF !important;
}

/* Judul Kategori Sidebar */
.sidebar-category-title {
    font-size: 13px;
    font-weight: 700;
    color: #FFFFFF !important;
    margin-top: 20px;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}

/* Tombol Menu Sidebar yang Disesuaikan Warna Referensi */
div[data-testid="stSidebar"] .stButton > button {
    background-color: transparent !important;
    color: #E2EDFF !important;
    border: none !important;
    text-align: left !important;
    justify-content: flex-start !important;
    font-weight: 500 !important;
    border-radius: 10px !important;
    padding: 8px 12px !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stSidebar"] .stButton > button:hover {
    background-color: rgba(255, 255, 255, 0.12) !important;
    color: #FFFFFF !important;
}

/* Efek Highlight Aktif */
div[data-testid="stSidebar"] .stButton > button[aria-selected="true"], 
div[data-testid="stSidebar"] .active-sidebar-btn > button {
    background: rgba(76, 132, 224, 0.75) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* HEADER HALAMAN UTAMA */
.main-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 3.4rem !important;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 8px;
    background: linear-gradient(120deg, #102A56, #246BCE, #65B2FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    width: 100%;
}

.main-title::after {
    content: '';
    display: block;
    width: 75px;
    height: 4px;
    margin: 15px auto 0;
    border-radius: 10px;
    background: linear-gradient(90deg, #246BCE, #8EC5FC);
}

.main-subtitle {
    text-align: center;
    color: #52719B;
    font-size: .92rem !important;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 14px;
    margin-bottom: 30px;
}

/* SECTION TITLE */
.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    color: var(--navy);
    font-size: 2rem;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 28px;
}

.section-title::after {
    content: '';
    display: block;
    width: 55px;
    height: 3px;
    border-radius: 10px;
    background: linear-gradient(90deg, var(--blue), var(--sky));
    margin: 12px auto 0;
}

/* STATS HIGHLIGHT CARDS */
.stat-card {
    background: rgba(255,255,255,0.9);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(16,42,86,0.05);
    margin-bottom: 25px;
    transition: transform 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
}

.stat-number {
    font-size: 32px;
    font-weight: 800;
    color: var(--blue);
    font-family: 'Playfair Display', serif;
}

.stat-label {
    font-size: 12px;
    font-weight: 700;
    color: var(--navy);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* SPLIT-SCREEN HERO & DESKRIPSI */
.hero-split-card {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 12px 35px rgba(16,42,86,0.08);
    margin-bottom: 35px;
    position: relative;
    overflow: hidden;
}

.hero-split-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, var(--navy), var(--blue), var(--sky));
}

.hero-img-container {
    position: relative;
    border-radius: 18px;
    overflow: hidden;
    height: 360px;
    box-shadow: 0 10px 25px rgba(16,42,86,0.15);
}

.hero-img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.hero-img-container:hover img {
    transform: scale(1.04);
}

.hero-img-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(0deg, rgba(16,42,86,0.85) 0%, transparent 60%);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 20px 24px;
    color: white;
}

.hero-badge-tag {
    display: inline-block;
    align-self: flex-start;
    padding: 5px 14px;
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.4);
    border-radius: 30px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.hero-img-overlay h3 {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    margin: 0;
    color: #FFFFFF;
}

.hero-img-overlay p {
    font-size: 12px;
    margin: 4px 0 0;
    color: #EAF3FF;
}

.desc-box-modern {
    background: #F8FCFF;
    border-left: 4px solid var(--blue);
    padding: 22px 26px;
    border-radius: 14px;
    font-size: 15px;
    line-height: 1.85;
    color: #334963;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.desc-box-modern b {
    color: var(--blue);
    font-size: 17px;
}

/* THEATER VIDEO BOX */
.video-theater-card {
    background: linear-gradient(135deg, #102A56, #1A4280);
    border-radius: 24px;
    padding: 28px;
    color: white;
    box-shadow: 0 15px 35px rgba(16,42,86,0.18);
    margin-bottom: 40px;
    position: relative;
}

.video-theater-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 18px;
}

.video-theater-header h3 {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    margin: 0;
    color: #FFFFFF;
}

/* GALLERY PHOTO CARDS */
.photo-card-grid {
    position: relative;
    height: 250px;
    margin-bottom: 24px;
    border-radius: 20px;
    overflow: hidden;
    background: #FFFFFF;
    border: 1px solid var(--border);
    box-shadow: 0 8px 25px rgba(16,42,86,0.08);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.photo-card-grid:hover {
    transform: translateY(-8px);
    box-shadow: 0 18px 38px rgba(36,107,206,0.22);
}

.photo-card-grid img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
}

.photo-card-grid:hover img {
    transform: scale(1.08);
}

.photo-card-grid .card-gradient-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(0deg, rgba(16,42,86,0.92) 0%, rgba(16,42,86,0.2) 60%, transparent 100%);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 20px 18px;
    color: white;
}

.photo-card-grid .card-title {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 4px;
}

.photo-card-grid .card-desc {
    font-size: 12px;
    line-height: 1.4;
    color: #D2E4FF;
    opacity: 0.9;
}

/* BANNER KOMITMEN */
.komitmen-banner-card {
    background: linear-gradient(120deg, #FFFFFF 0%, #EAF3FF 100%);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 30px 35px;
    box-shadow: 0 10px 30px rgba(16,42,86,0.07);
    margin-top: 20px;
    position: relative;
    overflow: hidden;
}

.komitmen-banner-card::before {
    content: '"';
    position: absolute;
    right: 25px;
    bottom: -20px;
    font-family: 'Playfair Display', serif;
    font-size: 140px;
    color: rgba(36,107,206,0.08);
    line-height: 1;
    pointer-events: none;
}

.komitmen-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 12px;
}

.komitmen-text {
    font-size: 15px;
    line-height: 1.8;
    color: #334963;
}

/* ABOUT US CARDS & DETAIL */
.member-card-preview {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(16,42,86,0.06);
    margin-bottom: 15px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.member-card-preview:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 30px rgba(36,107,206,0.18);
}

.member-card-preview img {
    width: 110px;
    height: 135px;
    object-fit: cover;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 2px solid var(--blue);
}

.member-card-preview h4 {
    font-size: 15px;
    font-weight: 800;
    color: var(--navy);
    margin: 0 0 6px;
}

.member-card-preview .badge-role {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    background: var(--light);
    color: var(--blue);
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 10px;
}

.detail-header-badge {
    display: inline-block;
    padding: 8px 18px;
    background: #EAF3FF;
    color: #174A91;
    font-weight: 800;
    font-size: 11px;
    letter-spacing: 1.5px;
    border-radius: 8px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.detail-container {
    display: flex;
    gap: 30px;
    background: #FFFFFF;
    border-radius: 24px;
    padding: 25px;
    border: 1px solid var(--border);
    box-shadow: 0 12px 35px rgba(16,42,86,0.08);
}

.detail-img-box {
    flex: 0 0 320px;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.detail-img-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.detail-info-box {
    flex: 1;
    border-left: 4px solid #246BCE;
    padding-left: 25px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.detail-info-box h2 {
    font-size: 26px;
    font-weight: 800;
    color: var(--navy);
    margin-top: 0;
    margin-bottom: 20px;
    border-bottom: 1px solid #E2EDFF;
    padding-bottom: 10px;
}

.info-item {
    margin-bottom: 14px;
    font-size: 14px;
    color: #334963;
    line-height: 1.6;
}

.info-item b {
    color: var(--navy);
    display: inline-block;
    width: 120px;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 9px; }
::-webkit-scrollbar-track { background: #EDF4FF; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #246BCE, #8EC5FC);
    border-radius: 10px;
}

@media (max-width: 768px) {
    .main-title { font-size: 2.3rem !important; }
    .hero-img-container { height: 260px; }
    .detail-container { flex-direction: column; }
    .detail-img-box { width: 100%; height: 320px; }
    .detail-info-box { border-left: none; border-top: 4px solid #246BCE; padding-left: 0; padding-top: 20px; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNGSI UTILITAS GAMBAR
# ============================================================
def get_drive_file_id(url):
    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        if query.get("id"):
            return query["id"][0]
        parts = parsed.path.split("/")
        if "d" in parts:
            idx = parts.index("d")
            if idx + 1 < len(parts):
                return parts[idx + 1]
    except Exception:
        pass
    return None


@st.cache_data(show_spinner=False)
def load_image(url):
    file_id = get_drive_file_id(url)
    candidate_urls = []
    if file_id:
        candidate_urls.extend([
            f"https://drive.google.com/thumbnail?id={file_id}&sz=w1600",
            f"https://drive.google.com/uc?export=download&id={file_id}",
            f"https://drive.google.com/uc?export=view&id={file_id}",
        ])
    candidate_urls.append(url)
    headers = {"User-Agent": "Mozilla/5.0"}

    for candidate in dict.fromkeys(candidate_urls):
        try:
            response = requests.get(candidate, headers=headers, timeout=25, allow_redirects=True)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img = ImageOps.exif_transpose(img).convert("RGB")
            img.load()
            return img
        except Exception:
            continue
    return None


@st.cache_data(show_spinner=False)
def image_data_uri(url):
    img = load_image(url)
    if img is None:
        return None
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=88, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


# ============================================================
# DATA ANGGOTA KATING (DATA LIST LENGKAP UTUH)
# ============================================================
buku_kating = [
    {"nim": "085", "nama": "Thomas Yustio", "sebagai": "Pak Lurah", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "050", "nama": "Syalom Nauli Jubilate", "sebagai": "Bu Lurah", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "026", "nama": "Chavia Chairunissa", "sebagai": "Anggota 01", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "038", "nama": "Aqila Chika Aurelia", "sebagai": "Anggota 02", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "042", "nama": "Sefina Amanda Putri", "sebagai": "Anggota 03", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "047", "nama": "Aura Putri Ghefira", "sebagai": "Anggota 04", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "052", "nama": "Ezra Hamizan", "sebagai": "Anggota 05", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "061", "nama": "Afdhi Hafiidz Habibie", "sebagai": "Anggota 06", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "066", "nama": "Rizqy Ramadhan", "sebagai": "Anggota 07", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
    {"nim": "091", "nama": "Alan Garcia Sinaga", "sebagai": "Anggota 08", "fun_fact": "--", "motto_hidup": "--"},
]

gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz"
] * len(buku_kating)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
with st.sidebar:
    st.markdown("""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; margin-top:5px;">
            <span style="font-size:22px; font-weight:800; color:white;">«</span>
        </div>
    """, unsafe_allow_html=True)

    if "menu_selected" not in st.session_state:
        st.session_state["menu_selected"] = "Bayesian"
    if "zoomed_member_idx" not in st.session_state:
        st.session_state["zoomed_member_idx"] = None

    # CATEGORY 1: HALAMAN UTAMA
    st.markdown('<div class="sidebar-category-title">Halaman Utama</div>', unsafe_allow_html=True)
    if st.button("🏠 Bayesian", key="btn_bayesian", use_container_width=True):
        st.session_state["menu_selected"] = "Bayesian"
        st.session_state["zoomed_member_idx"] = None

    # CATEGORY 2: BUKU KATING
    st.markdown('<div class="sidebar-category-title">Buku Kating</div>', unsafe_allow_html=True)

    for idx, kating in enumerate(buku_kating):
        display_label = f"👤 {kating['nim']} - {kating['nama']}"
        
        if st.button(display_label, key=f"side_kat_{kating['nim']}", use_container_width=True):
            st.session_state["menu_selected"] = "About Us"
            st.session_state["zoomed_member_idx"] = idx

    # CATEGORY 3: TRY ME !!
    st.markdown('<div class="sidebar-category-title">Try Me !!</div>', unsafe_allow_html=True)
    if st.button("🔍 KREASI", key="btn_kreasi1", use_container_width=True):
        st.session_state["menu_selected"] = "KREASI"
    if st.button("🔍 KREASII", key="btn_kreasi2", use_container_width=True):
        st.session_state["menu_selected"] = "KREASII"


# ============================================================
# HEADER WEBSITE
# ============================================================
st.markdown("""
<div>
    <h1 class="main-title">WEBSITE KATING</h1>
    <p class="main-subtitle">CEO HMSD Adyatama ITERA 2026</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# LOGO
# ============================================================
url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"

def layout_logo(url):
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    with col2:
        img = load_image(url)
        if img is not None:
            st.image(img, use_container_width=True)
        else:
            st.warning("Gambar gagal dimuat. Pastikan file Google Drive dapat diakses publik.")

layout_logo(url)
st.write("")
layout_logo(url1)

st.markdown("<div style='margin-top: 35px;'></div>", unsafe_allow_html=True)


# ============================================================
# HALAMAN HOME / BAYESIAN
# ============================================================
menu = st.session_state["menu_selected"]

if menu == "Bayesian":

    def home_page():
        # STATISTIK RINGKAS KELOMPOK
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="stat-card"><div class="stat-number">10</div><div class="stat-label">Anggota Kelompok</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="stat-card"><div class="stat-number">2026</div><div class="stat-label">Adyatama ITERA</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="stat-card"><div class="stat-number">100%</div><div class="stat-label">Semangat & Kekeluargaan</div></div>', unsafe_allow_html=True)

        # JUDUL DESKRIPSI KELOMPOK
        st.markdown("<h2 class='section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)

        # SPLIT-SCREEN LAYOUT
        hero_url = "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"
        hero_img_src = image_data_uri(hero_url)

        col_hero_left, col_hero_right = st.columns([1.1, 1])

        with col_hero_left:
            if hero_img_src:
                st.markdown(f"""
                    <div class="hero-split-card">
                        <div class="hero-img-container">
                            <img src="{hero_img_src}" alt="Keluarga Bayesian">
                            <div class="hero-img-overlay">
                                <span class="hero-badge-tag">✦ Keluarga Bayesian ✦</span>
                                <h3>Gapai Cita, Kejar mimpi, Di angkasa</h3>
                                <p>Momen kebersamaan yang tidak akan terlupakan.</p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        with col_hero_right:
            st.markdown("""
                <div class="desc-box-modern">
                    <b>Selamat datang di portal resmi kelompok Bayesian!</b><br><br>
                    isi aja apa aja ini bingung.
                </div>
            """, unsafe_allow_html=True)

        # THEATER VIDEO SHOWCASE
        st.markdown("""
            <h3 class="section-title" style="font-size:24px;">
                Video Profil & Kenangan Bayesian
            </h3>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="video-theater-card">
                <div class="video-theater-header">
                    <span>🎬</span>
                    <h3>Cinema & Memories</h3>
                </div>
        """, unsafe_allow_html=True)
        
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.markdown('</div>', unsafe_allow_html=True)

        # DOKUMENTASI KEGIATAN GALERI
        st.markdown("""
            <h3 class="section-title" style="font-size:24px;">
                Dokumentasi Kegiatan Bayesian
            </h3>
        """, unsafe_allow_html=True)

        tab_all, tab_highlights = st.tabs(["📷 Semua Momen", "⭐ Momen Pilihan"])

        kegiatan_Bayesian = [
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "First Moment", "desc": "Awal dari cerita yang panjang"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Our Journey", "desc": "Langkah demi langkah bersama"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Growing Together", "desc": "Tumbuh bersama melalui setiap proses"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "The Story", "desc": "Setiap foto menyimpan cerita."},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Good Times", "desc": "Keluh kesah, tawa dan cerita yang tak bisa dilupakan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Until Forever", "desc": "Bukan akhir, hanya bagian dari perjalanan"}
        ]

        def render_gallery(data_items):
            for i in range(0, len(data_items), 3):
                cols = st.columns(3)
                for j in range(3):
                    idx = i + j
                    if idx < len(data_items):
                        item = data_items[idx]
                        with cols[j]:
                            img_src = image_data_uri(item["url"])
                            if img_src:
                                st.markdown(f"""
                                    <div class="photo-card-grid">
                                        <img src="{img_src}" alt="{html.escape(item['judul'])}">
                                        <div class="card-gradient-overlay">
                                            <div class="card-title">{html.escape(item['judul'])}</div>
                                            <div class="card-desc">{html.escape(item['desc'])}</div>
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)

        with tab_all:
            render_gallery(kegiatan_Bayesian)

        with tab_highlights:
            render_gallery(kegiatan_Bayesian[:3])

        # BANNER KOMITMEN KELOMPOK
        st.markdown("""
            <div class="komitmen-banner-card">
                <div class="komitmen-title">Komitmen Kami:</div>
                <div class="komitmen-text">
                    Kami berkomitmen penuh dalam segala hal .................
                </div>
            </div>
        """, unsafe_allow_html=True)

    home_page()


# ============================================================
# HALAMAN ABOUT US / BUKU KATING (KHUSUS BIODATA DIBATASI)
# ============================================================
elif menu == "About Us":

    def about_page():

        st.markdown("<h2 class='section-title'>About Us — Buku Kating</h2>", unsafe_allow_html=True)

        # DATA ANGGOTA LENGKAP UTUH (ISI DATA LIST TIDAK DIUBAH)
        data_list = [
            {
                "nama": "Thomas Yustio",
                "sebagai": "Pak Lurah",
                "nim": "125450085",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Syalom Nauli Jubilate",
                "sebagai": "Bu Lurah",
                "nim": "125450050",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Chavia Chairunissa",
                "sebagai": "Anggota 01",
                "nim": "125450026",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Aqila Chika Aurelia",
                "sebagai": "Anggota 02",
                "nim": "125450038",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Sefina Amanda Putri",
                "sebagai": "Anggota 03",
                "nim": "125450042",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Aura Putri Ghefira",
                "sebagai": "Anggota 04",
                "nim": "125450047",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Ezra Hamizan",
                "sebagai": "Anggota 05",
                "nim": "125450052",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Afdhi Hafiidz Habibie",
                "sebagai": "Anggota 06",
                "nim": "125450061",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 07",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Alan Garcia Sinaga",
                "sebagai": "Anggota 08",
                "nim": "125450091",
                "fun_fact": "--",
                "motto_hidup": "--"
            }
        ]

        if st.session_state["zoomed_member_idx"] is not None:
            idx = st.session_state["zoomed_member_idx"]
            m = data_list[idx]
            img_src = image_data_uri(gambar_urls[idx])

            if st.button("← Kembali ke Daftar Anggota"):
                st.session_state["zoomed_member_idx"] = None
                st.rerun()

            st.write("")

            role_badge_text = m["sebagai"].upper()
            st.markdown(f'<div class="detail-header-badge">{role_badge_text}</div>', unsafe_allow_html=True)

            if img_src:
                # DITAMPILKAN HANYA NAMA, SEBAGAI, NIM, FUN FACT, MOTTO HIDUP
                st.markdown(f"""
                <div class="detail-container">
                    <div class="detail-img-box">
                        <img src="{img_src}" alt="{html.escape(m['nama'])}">
                    </div>
                    <div class="detail-info-box">
                        <h2>{html.escape(m['nama'])}</h2>
                        <div class="info-item"><b>Sebagai:</b> {html.escape(m['sebagai'])}</div>
                        <div class="info-item"><b>NIM:</b> {html.escape(m['nim'])}</div>
                        <div class="info-item"><b>Fun Fact:</b> {html.escape(m['fun_fact'])}</div>
                        <div class="info-item"><b>Motto Hidup:</b> {html.escape(m['motto_hidup'])}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            for i in range(0, len(data_list), 3):
                cols = st.columns(3)

                for j in range(3):
                    idx = i + j

                    if idx < len(data_list):
                        member = data_list[idx]
                        img_url = gambar_urls[idx]

                        with cols[j]:
                            img_src = image_data_uri(img_url)

                            if img_src:
                                nama = html.escape(member["nama"])
                                sebagai = html.escape(member["sebagai"])

                                st.markdown(f"""
                                    <div class="member-card-preview">
                                        <img src="{img_src}" alt="{nama}">
                                        <h4>{nama}</h4>
                                        <div class="badge-role">{sebagai}</div>
                                    </div>
                                """, unsafe_allow_html=True)

                                if st.button(f"🔍 Lihat Detail Profil", key=f"zoom_btn_{idx}", use_container_width=True):
                                    st.session_state["zoomed_member_idx"] = idx
                                    st.rerun()

                            else:
                                st.warning(f"Foto untuk {member['nama']} gagal dimuat.")

    about_page()

# HALAMAN TRY ME !!
elif menu in ["KREASI", "KREASII"]:
    st.markdown(f"<h2 class='section-title'>Menu Modul: {menu}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="desc-box-modern">
            <b>Selamat Datang di Halaman {menu}!</b><br><br>
            Ruang eksperimen interaktif untuk fitur tambahan dan ekspansi kelompok.
        </div>
    """, unsafe_allow_html=True)
