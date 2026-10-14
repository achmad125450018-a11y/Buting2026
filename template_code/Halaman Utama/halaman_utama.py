import streamlit as st
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
# CSS — SIDEBAR BLUE REFERENSI & MODERN UI
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --navy: #0C2B64;
    --navy-light: #16428E;
    --blue: #246BCE;
    --sky: #8EC5FC;
    --light: #EAF3FF;
    --border: #D8E7FA;
    --text: #334963;
    --card-radius: 20px;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--text);
}

.stApp {
    background: 
        radial-gradient(circle at 5% 5%, rgba(91,164,255,.15), transparent 35%),
        radial-gradient(circle at 95% 60%, rgba(36,107,206,.08), transparent 38%),
        linear-gradient(180deg, #F7FAFF 0%, #EAF2FC 100%);
    background-attachment: fixed;
}

.block-container {
    max-width: 1150px;
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
}

/* ============================================================
   STYLING SIDEBAR
   ============================================================ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #09204A 0%, #123C82 50%, #1A54BA 100%) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

section[data-testid="stSidebar"] .stMarkdown {
    color: #FFFFFF;
}

/* Sidebar Title Header */
.sidebar-category-title {
    font-size: 13px;
    font-weight: 800;
    color: #FFFFFF;
    text-transform: capitalize;
    margin-top: 18px;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
    opacity: 0.95;
}

/* Item Menu Sidebar */
.sidebar-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    margin-bottom: 4px;
    border-radius: 12px;
    color: #E0ECFF;
    font-size: 13.5px;
    font-weight: 500;
    transition: all 0.25s ease;
    cursor: pointer;
    text-decoration: none;
}

.sidebar-item:hover {
    background: rgba(255, 255, 255, 0.12);
    color: #FFFFFF;
    transform: translateX(4px);
}

.sidebar-item.active {
    background: linear-gradient(90deg, #3B82F6, #2563EB) !important;
    color: #FFFFFF !important;
    font-weight: 700;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
}

/* Search input di sidebar */
div[data-testid="stSidebar"] input {
    background-color: rgba(255, 255, 255, 0.12) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
}

div[data-testid="stSidebar"] input::placeholder {
    color: #A3C7FF !important;
}

/* ============================================================
   HEADER HERO & CONTENT
   ============================================================ */
.hero-header-box {
    position: relative;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 25px;
    box-shadow: 0 18px 45px rgba(16,42,86,.16);
    background: var(--navy);
    min-height: 340px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 20px;
}

.hero-header-bg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.45;
    filter: brightness(0.8);
}

.hero-header-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
}

.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem !important;
    font-weight: 800;
    color: #FFFFFF !important;
    letter-spacing: 1px;
    line-height: 1.15;
    margin-bottom: 8px;
    text-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

.main-subtitle {
    color: #E3EEFF;
    font-size: .95rem !important;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 10px;
    margin-bottom: 25px;
}

/* SECTION TITLE */
.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    color: var(--navy);
    font-size: 2rem;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 24px;
}

.section-title::after {
    content: '';
    display: block;
    width: 55px;
    height: 3px;
    border-radius: 10px;
    background: linear-gradient(90deg, var(--blue), var(--sky));
    margin: 10px auto 0;
}

/* CONTENT BOX */
.content-box {
    position: relative;
    background: rgba(255,255,255,.95);
    padding: 30px 34px;
    border: 1px solid var(--border);
    border-radius: var(--card-radius);
    box-shadow: 0 8px 28px rgba(16,42,86,.07);
    margin-bottom: 30px;
    text-align: justify;
    line-height: 1.9;
    font-size: 15px;
    color: #40536B;
}

.content-box b {
    color: var(--blue);
    font-weight: 800;
}

.feature-section {
    background: rgba(255,255,255,.95);
    border-radius: var(--card-radius);
    padding: 20px;
    border: 1px solid var(--border);
    box-shadow: 0 8px 28px rgba(16,42,86,.07);
    margin-bottom: 30px;
}

.feature-img-box {
    border-radius: 16px;
    overflow: hidden;
    height: 270px;
    width: 100%;
}

.feature-img-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* DOKUMENTASI CARDS */
.photo-card {
    position: relative;
    height: 210px;
    margin-bottom: 22px;
    border-radius: 18px;
    overflow: hidden;
    background: white;
    border: 1px solid var(--border);
    box-shadow: 0 7px 22px rgba(16,42,86,.10);
    transition: transform .3s ease, box-shadow .3s ease;
}

.photo-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 32px rgba(36,107,206,.20);
}

.photo-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.photo-card::after {
    content: '';
    position: absolute;
    inset: 30% 0 0;
    background: linear-gradient(0deg, rgba(10,35,75,.95), transparent);
    pointer-events: none;
}

.photo-card .overlay {
    position: absolute;
    z-index: 1;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 16px;
    color: white;
}

.photo-card .overlay-title {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 3px;
}

.photo-card .overlay-desc {
    font-size: 11px;
    line-height: 1.4;
    color: #E2EDFF;
}

/* ============================================================
   KARTU GERBANG / TIRAI TERBUKA (ABOUT US)
   ============================================================ */
.curtain-card {
    position: relative;
    width: 100%;
    height: 390px;
    margin-bottom: 24px;
    border-radius: 20px;
    overflow: hidden;
    background: #0B2044;
    border: 1px solid var(--border);
    box-shadow: 0 10px 28px rgba(16,42,86,.10);
}

.curtain-card .card-details {
    position: absolute;
    inset: 0;
    padding: 22px 18px;
    background: linear-gradient(145deg, #153B72, #0B2044);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    z-index: 1;
}

.curtain-card .card-details h4 {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    margin: 0 0 2px 0;
    color: #FFFFFF;
}

.curtain-card .card-details .det-role {
    font-size: 9px;
    font-weight: 800;
    color: #A8D2FF;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

.curtain-card .card-details .info-box {
    background: rgba(255, 255, 255, 0.08);
    border-left: 3px solid #72B7FF;
    padding: 8px 10px;
    border-radius: 7px;
    margin-bottom: 7px;
}

.curtain-card .card-details .info-label {
    font-size: 8px;
    font-weight: 800;
    color: #9CCBFF;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    display: block;
    margin-bottom: 2px;
}

.curtain-card .card-details .info-val {
    font-size: 11px;
    color: #F1F6FF;
    line-height: 1.4;
    word-break: break-word;
}

.curtain-top, .curtain-bottom {
    position: absolute;
    left: 0;
    right: 0;
    width: 100%;
    height: 50%;
    background: linear-gradient(160deg, #FFFFFF, #EDF5FF);
    z-index: 2;
    transition: transform 0.6s cubic-bezier(0.77, 0, 0.175, 1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.curtain-top {
    top: 0;
    border-bottom: 1px solid var(--border);
}

.curtain-bottom {
    bottom: 0;
    border-top: 1px solid var(--border);
}

.curtain-top .photo-frame {
    width: 125px;
    height: 150px;
    border-radius: 14px;
    overflow: hidden;
    background: linear-gradient(135deg, #102A56, #4A9BF5);
    padding: 3px;
    box-shadow: 0 8px 20px rgba(36,107,206,.2);
    margin-top: 20px;
}

.curtain-top .photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 11px;
}

.curtain-bottom h4 {
    font-size: 14px;
    font-weight: 800;
    color: var(--navy);
    margin: 0 0 6px 0;
    text-align: center;
}

.curtain-bottom .role-badge {
    padding: 5px 13px;
    border-radius: 30px;
    background: linear-gradient(135deg, #102A56, #246BCE);
    color: white;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.curtain-bottom .role-badge.anggota {
    background: #DCEBFF;
    color: #174A91;
}

.curtain-bottom .hint {
    font-size: 8.5px;
    color: #7790B0;
    margin-top: 8px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.curtain-card:hover .curtain-top {
    transform: translateY(-100%);
}

.curtain-card:hover .curtain-bottom {
    transform: translateY(100%);
}

.video-container {
    background: rgba(255,255,255,.95);
    padding: 18px;
    border-radius: var(--card-radius);
    border: 1px solid var(--border);
    box-shadow: 0 8px 28px rgba(16,42,86,.07);
    margin-bottom: 30px;
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
# DATA KATING & ANGGOTA (SAMA DENGAN REFERENSI GAMBAR)
# ============================================================
buku_kating = [
    {"nim": "085", "nama": "Thomas Yustio", "sebagai": "Pak Lurah", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "050", "nama": "Syalom Nauli Jubilate", "sebagai": "Bu Lurah", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "026", "nama": "Chavia Chairunissa", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "038", "nama": "Aqila Chika Aurelia", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "042", "nama": "Sefina Amanda Putri", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "047", "nama": "Aura Putri Ghefira", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "052", "nama": "Ezra Hamizan", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "061", "nama": "Afdhi Hafiidz Habibie", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
    {"nim": "066", "nama": "Rizqy Ramadhan", "sebagai": "Anggota", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
    {"nim": "091", "nama": "Alan Garcia Sinaga", "sebagai": "Anggota", "fun_fact": "--", "motto_hidup": "--"},
]

gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz"
] * len(buku_kating)


# ============================================================
# SIDEBAR DENGAN TAMPILAN SESUAI REFERENSI
# ============================================================
with st.sidebar:
    st.markdown("""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <span style="font-size:22px; font-weight:800; color:white;">Menu Navigasi</span>
            <span style="font-size:18px; color:#A8D2FF;">«</span>
        </div>
    """, unsafe_allow_html=True)

    # Inisialisasi Session State Menu
    if "menu_selected" not in st.session_state:
        st.session_state["menu_selected"] = "Bayesian"
    if "selected_member" not in st.session_state:
        st.session_state["selected_member"] = None

    # CATEGORY 1: HALAMAN UTAMA
    st.markdown('<div class="sidebar-category-title">Halaman Utama</div>', unsafe_allow_html=True)
    if st.button("🏠 Bayesian (Home)", key="nav_home", use_container_width=True):
        st.session_state["menu_selected"] = "Bayesian"
        st.session_state["selected_member"] = None

    # CATEGORY 2: BUKU KATING
    st.markdown('<div class="sidebar-category-title">Buku Kating</div>', unsafe_allow_html=True)

    # Search bar mini untuk mempermudah cari nama kating
    search_query = st.text_input("", placeholder="🔍 Cari kating...", key="sidebar_search", label_visibility="collapsed")

    for kating in buku_kating:
        display_name = f"{kating['nim']} - {kating['nama']}"

        # Filter pencarian jika diisi
        if search_query and search_query.lower() not in display_name.lower():
            continue

        btn_label = f"👤  {display_name}"
        is_active = (st.session_state["selected_member"] == kating["nama"])

        if st.button(btn_label, key=f"kating_{kating['nim']}", use_container_width=True):
            st.session_state["menu_selected"] = "About Us"
            st.session_state["selected_member"] = kating["nama"]

    # CATEGORY 3: TRY ME !!
    st.markdown('<div class="sidebar-category-title">Try Me !!</div>', unsafe_allow_html=True)
    if st.button("🔍 KREASI", key="nav_kreasi", use_container_width=True):
        st.session_state["menu_selected"] = "KREASI"
    if st.button("🔍 KREASI II", key="nav_kreasi2", use_container_width=True):
        st.session_state["menu_selected"] = "KREASI II"


# ============================================================
# HEADER WEBPAGE (DESAIN HERO BESAR)
# ============================================================
hero_bg_url = "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"
hero_bg_src = image_data_uri(hero_bg_url) or ""

st.markdown(f"""
<div class="hero-header-box">
    <img class="hero-header-bg" src="{hero_bg_src}" alt="Hero Background">
    <div class="hero-header-content">
        <h1 class="main-title">WEBSITE KATING</h1>
        <p class="main-subtitle">CEO HMSD Adyatama ITERA 2026</p>
    </div>
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
            st.warning("Gambar gagal dimuat. Periksa izin Google Drive.")

layout_logo(url)
st.write("")
layout_logo(url1)

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)


# ============================================================
# NAVIGATION HANDLER (DARI SIDEBAR)
# ============================================================
menu = st.session_state["menu_selected"]

# HALAMAN HOME / BAYESIAN
if menu == "Bayesian":
    col_img, col_txt = st.columns([1.1, 1])

    with col_img:
        img_src = image_data_uri("https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq")
        if img_src:
            st.markdown(f"""
            <div class="feature-section">
                <div class="feature-img-box">
                    <img src="{img_src}" alt="Hero Image">
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_txt:
        st.markdown("""
        <div style="padding-top: 5px;">
            <h2 class="section-title" style="text-align:left; margin-top:0;">
                Gapai Cita, Kejar Mimpi, Di Angkasa
            </h2>
            <div class="content-box">
                <b>Selamat datang di portal resmi kelompok Bayesian!</b><br><br>
                isi aja apa aja ini bingung.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h3 class="section-title">Dokumentasi Video Bayesian</h3>', unsafe_allow_html=True)
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<h3 class="section-title">Dokumentasi Kegiatan Bayesian</h3>', unsafe_allow_html=True)

    kegiatan_Bayesian = [
        {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "First Moment", "desc": "Awal dari cerita yang panjang"},
        {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Our Journey", "desc": "Langkah demi langkah bersama"},
        {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Growing Together", "desc": "Tumbuh bersama melalui setiap proses"},
        {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "The Story", "desc": "Setiap foto menyimpan cerita."},
        {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Good Times", "desc": "Keluh kesah, tawa dan cerita yang tak bisa dilupakan"},
        {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Until Forever", "desc": "Bukan akhir, hanya bagian dari perjalanan"}
    ]

    for i in range(0, len(kegiatan_Bayesian), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(kegiatan_Bayesian):
                item = kegiatan_Bayesian[idx]
                with cols[j]:
                    img_src = image_data_uri(item["url"])
                    if img_src:
                        st.markdown(f"""
                            <div class="photo-card">
                                <img src="{img_src}" alt="{html.escape(item['judul'], quote=True)}">
                                <div class="overlay">
                                    <div class="overlay-title">{html.escape(item['judul'])}</div>
                                    <div class="overlay-desc">{html.escape(item['desc'])}</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="content-box">
            <b>Komitmen Kami:</b><br>
            Kami berkomitmen penuh dalam segala hal .................
        </div>
    """, unsafe_allow_html=True)

# HALAMAN ABOUT US / BUKU KATING
elif menu == "About Us":
    selected_person = st.session_state.get("selected_member")

    if selected_person:
        st.markdown(f"<h2 class='section-title'>Profil Detail: {selected_person}</h2>", unsafe_allow_html=True)
        if st.button("← Kembali ke Semua Anggota"):
            st.session_state["selected_member"] = None
            st.rerun()

    else:
        st.markdown("<h2 class='section-title'>About Us — Buku Kating</h2>", unsafe_allow_html=True)

    # Filter Anggota jika dipilih spesifik dari sidebar
    display_list = [k for k in buku_kating if k["nama"] == selected_person] if selected_person else buku_kating

    for i in range(0, len(display_list), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(display_list):
                member = display_list[idx]
                img_url = gambar_urls[idx % len(gambar_urls)]

                with cols[j]:
                    img_src = image_data_uri(img_url)

                    if img_src:
                        nama = html.escape(member["nama"])
                        sebagai = html.escape(member["sebagai"])
                        nim = html.escape(f"125450{member['nim']}")
                        fun_fact = html.escape(member["fun_fact"])
                        motto = html.escape(member["motto_hidup"])

                        role_class = "anggota" if member["sebagai"].lower() == "anggota" else ""

                        st.markdown(f"""
                            <div class="curtain-card">
                                <div class="card-details">
                                    <h4>{nama}</h4>
                                    <div class="det-role">{sebagai}</div>
                                    
                                    <div class="info-box">
                                        <span class="info-label">NIM</span>
                                        <span class="info-val">{nim}</span>
                                    </div>
                                    
                                    <div class="info-box">
                                        <span class="info-label">Fun Fact</span>
                                        <span class="info-val">{fun_fact}</span>
                                    </div>
                                    
                                    <div class="info-box">
                                        <span class="info-label">Motto Hidup</span>
                                        <span class="info-val">{motto}</span>
                                    </div>
                                </div>

                                <div class="curtain-top">
                                    <div class="photo-frame">
                                        <img src="{img_src}" alt="{html.escape(member['nama'], quote=True)}">
                                    </div>
                                </div>

                                <div class="curtain-bottom">
                                    <h4>{nama}</h4>
                                    <span class="role-badge {role_class}">{sebagai}</span>
                                    <div class="hint">Arahkan kursor untuk buka gerbang</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

# HALAMAN TRY ME !! (KREASI)
elif menu in ["KREASI", "KREASI II"]:
    st.markdown(f"<h2 class='section-title'>Fitur Inovasi: {menu}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="content-box">
            <b>Selamat Datang di Modul {menu}!</b><br><br>
            Halaman ini disiapkan khusus untuk eksperimen, kuis interaktif, atau fitur pencarian kating secara instan.
        </div>
    """, unsafe_allow_html=True)
