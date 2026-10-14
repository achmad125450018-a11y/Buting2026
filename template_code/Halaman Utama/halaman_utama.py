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
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS — MODERN OCEAN & CURTAIN EFFECT UI/UX
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --navy: #0B192C;
    --blue: #1E5164;
    --sky: #008DDA;
    --light: #F4F8FB;
    --border: #D1E4F3;
    --text: #2C3E50;
    --card-bg: #FFFFFF;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--text);
}

.stApp {
    background: 
        radial-gradient(circle at 10% 10%, rgba(0,141,218,0.12), transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(30,81,100,0.10), transparent 40%),
        linear-gradient(180deg, #F8FAFC 0%, #EBF3FA 100%);
    background-attachment: fixed;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}

/* HEADER */
.main-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem !important;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 8px;
    background: linear-gradient(120deg, #0B192C, #008DDA, #41C9E2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    width: 100%;
}

.main-title::after {
    content: '';
    display: block;
    width: 80px;
    height: 4px;
    margin: 15px auto 0;
    border-radius: 10px;
    background: linear-gradient(90deg, #008DDA, #41C9E2);
}

.main-subtitle {
    text-align: center;
    color: #4A627A;
    font-size: .95rem !important;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-top: 14px;
    margin-bottom: 30px;
}

/* SECTION TITLE */
.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    color: var(--navy);
    font-size: 2.1rem;
    font-weight: 700;
    margin-top: 45px;
    margin-bottom: 28px;
}

.section-title::after {
    content: '';
    display: block;
    width: 60px;
    height: 3px;
    border-radius: 10px;
    background: linear-gradient(90deg, var(--sky), #41C9E2);
    margin: 12px auto 0;
}

/* CONTENT BOX */
.content-box {
    position: relative;
    background: rgba(255,255,255,0.92);
    padding: 30px 34px;
    border: 1px solid var(--border);
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(11,25,44,0.06);
    margin-bottom: 32px;
    text-align: justify;
    line-height: 1.9;
    font-size: 15px;
    color: #34495E;
    backdrop-filter: blur(8px);
}

.content-box::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 6px;
    height: 100%;
    border-radius: 20px 0 0 20px;
    background: linear-gradient(180deg, #008DDA, #41C9E2);
}

.content-box b {
    color: var(--sky);
    font-weight: 800;
}

/* HERO IMAGE */
.hero-image-wrapper {
    position: relative;
    width: 100%;
    margin: 0 auto 30px;
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.8);
    box-shadow: 0 20px 40px rgba(11,25,44,0.15);
    background: var(--navy);
}

.hero-image-wrapper img {
    display: block;
    width: 100%;
    height: 420px;
    object-fit: cover;
    transition: transform .6s ease;
}

.hero-image-wrapper:hover img {
    transform: scale(1.03);
}

.hero-image-wrapper .hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        0deg,
        rgba(11,25,44,0.95) 0%,
        rgba(11,25,44,0.4) 50%,
        transparent 100%
    );
    pointer-events: none;
}

.hero-image-wrapper .hero-caption {
    position: absolute;
    bottom: 30px;
    left: 32px;
    right: 32px;
    color: white;
}

.hero-image-wrapper .hero-badge {
    display: inline-block;
    padding: 6px 16px;
    border: 1px solid rgba(255,255,255,0.3);
    background: rgba(0,141,218,0.3);
    backdrop-filter: blur(4px);
    border-radius: 50px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
    color: #E0F4FF;
}

.hero-image-wrapper .hero-caption h3 {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 700;
    margin: 0;
    color: white;
}

.hero-image-wrapper .hero-caption p {
    font-size: 14px;
    margin-top: 8px;
    color: #D2E0FB;
    line-height: 1.6;
}

/* DOCUMENTATION CARDS */
.photo-card {
    position: relative;
    height: 240px;
    margin-bottom: 24px;
    border-radius: 20px;
    overflow: hidden;
    background: white;
    border: 1px solid var(--border);
    box-shadow: 0 8px 20px rgba(11,25,44,0.08);
    transition: transform .3s ease, box-shadow .3s ease;
}

.photo-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 35px rgba(0,141,218,0.22);
}

.photo-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform .5s ease;
}

.photo-card:hover img {
    transform: scale(1.08);
}

.photo-card::after {
    content: '';
    position: absolute;
    inset: 20% 0 0;
    background: linear-gradient(
        0deg,
        rgba(11,25,44,0.95),
        rgba(11,25,44,0.3),
        transparent
    );
    pointer-events: none;
}

.photo-card .overlay {
    position: absolute;
    z-index: 1;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 20px 18px;
    color: white;
    text-align: left;
}

.photo-card .overlay-title {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 4px;
    color: #FFFFFF;
}

.photo-card .overlay-desc {
    font-size: 11.5px;
    line-height: 1.4;
    color: #E0F2FE;
}

/* VIDEO CONTAINER */
.video-container {
    background: #FFFFFF;
    padding: 20px;
    border-radius: 24px;
    border: 1px solid var(--border);
    box-shadow: 0 10px 30px rgba(11,25,44,0.08);
    margin-bottom: 35px;
}

/* ============================================================
   EFEK TIRAI TERBUKA (CURTAIN / GATE OPEN EFFECT) - ABOUT US
   ============================================================ */
.curtain-card {
    position: relative;
    width: 100%;
    height: 400px;
    margin-bottom: 25px;
    border-radius: 20px;
    overflow: hidden;
    background: #0B192C;
    border: 1px solid var(--border);
    box-shadow: 0 10px 25px rgba(11,25,44,0.12);
}

/* Latar Belakang Detail (Muncul saat tirai terbuka) */
.curtain-card .card-details {
    position: absolute;
    inset: 0;
    padding: 25px 20px;
    background: linear-gradient(145deg, #0B192C, #1E3E62);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    z-index: 1;
}

.curtain-card .card-details h4 {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    margin: 0 0 4px 0;
    color: #FFFFFF;
}

.curtain-card .card-details .det-role {
    font-size: 10px;
    font-weight: 800;
    color: #41C9E2;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.curtain-card .card-details .info-box {
    background: rgba(255, 255, 255, 0.07);
    border-left: 3px solid #008DDA;
    padding: 8px 12px;
    border-radius: 8px;
    margin-bottom: 8px;
}

.curtain-card .card-details .info-label {
    font-size: 8px;
    font-weight: 800;
    color: #93C5FD;
    text-transform: uppercase;
    letter-spacing: 1px;
    display: block;
    margin-bottom: 2px;
}

.curtain-card .card-details .info-val {
    font-size: 11px;
    color: #F0F7FF;
    line-height: 1.4;
    word-break: break-word;
}

/* TIRAI ATAS & BAWAH */
.curtain-top, .curtain-bottom {
    position: absolute;
    left: 0;
    right: 0;
    width: 100%;
    height: 50%;
    background: linear-gradient(160deg, #FFFFFF, #EBF4FC);
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
    border-bottom: 1px solid rgba(0,141,218,0.2);
    padding-top: 20px;
}

.curtain-bottom {
    bottom: 0;
    border-top: 1px solid rgba(0,141,218,0.2);
    padding-bottom: 20px;
}

/* Elemen Foto Di Tirai Atas */
.curtain-top .photo-frame {
    width: 130px;
    height: 155px;
    border-radius: 14px;
    overflow: hidden;
    border: 3px solid #008DDA;
    box-shadow: 0 8px 20px rgba(0,87,146,0.2);
    margin-top: 25px;
}

.curtain-top .photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Teks Pada Tirai Bawah */
.curtain-bottom h4 {
    font-size: 15px;
    font-weight: 800;
    color: var(--navy);
    margin: 0 0 6px 0;
    text-align: center;
    padding: 0 10px;
}

.curtain-bottom .role-badge {
    padding: 5px 12px;
    border-radius: 30px;
    background: #008DDA;
    color: white;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.curtain-bottom .role-badge.anggota {
    background: #DCEBFF;
    color: #005792;
}

.curtain-bottom .hint {
    font-size: 8.5px;
    color: #88A0C0;
    margin-top: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* ANIMASI HOVER TERBUKA */
.curtain-card:hover .curtain-top {
    transform: translateY(-100%);
}

.curtain-card:hover .curtain-bottom {
    transform: translateY(100%);
}

/* NAVBAR & SCROLLBAR */
::-webkit-scrollbar {
    width: 9px;
}

::-webkit-scrollbar-track {
    background: #EDF4FF;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #008DDA, #41C9E2);
    border-radius: 10px;
}

@media (max-width: 768px) {
    .main-title { font-size: 2.3rem !important; }
    .hero-image-wrapper img { height: 280px; }
    .curtain-card { height: 380px; }
    .curtain-top .photo-frame { width: 110px; height: 135px; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNGSI UTILITAS GAMBAR
# ============================================================
def get_drive_file_id(url):
    """Mengambil ID file dari beberapa format link Google Drive."""
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
    """Mengunduh gambar Google Drive atau URL gambar langsung."""
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
    """Mengubah gambar menjadi data URI untuk HTML."""
    img = load_image(url)
    if img is None:
        return None

    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=88, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


def hero_image(
    url,
    badge="✦ Keluarga Bayesian ✦",
    title="Satu Tim, Satu Cerita",
    subtitle="Momen kebersamaan yang menjadi awal dari segalanya."
):
    """Menampilkan foto utama dengan overlay dan caption."""
    img_src = image_data_uri(url)

    if not img_src:
        st.warning("Foto hero gagal dimuat. Periksa izin Google Drive.")
        return

    st.markdown(f"""
        <div class="hero-image-wrapper">
            <img src="{img_src}" alt="{html.escape(title, quote=True)}">
            <div class="hero-overlay"></div>
            <div class="hero-caption">
                <div class="hero-badge">{html.escape(badge)}</div>
                <h3>{html.escape(title)}</h3>
                <p>{html.escape(subtitle)}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


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
# NAVBAR
# ============================================================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "people"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "10px!important",
                "background-color": "rgba(255,255,255,0.92)",
                "border-radius": "16px",
                "box-shadow": "0 8px 25px rgba(11,25,44,0.08)",
                "border": "1px solid #D1E4F3",
                "margin-bottom": "35px",
            },
            "icon": {
                "color": "#008DDA",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "0 6px",
                "padding": "10px 22px",
                "border-radius": "10px",
                "color": "#0B192C",
                "--hover-color": "#EBF3FA",
            },
            "nav-link-selected": {
                "background-color": "#008DDA",
                "color": "#FFFFFF",
                "box-shadow": "0 5px 14px rgba(0,141,218,0.3)",
            },
        },
    )
    return selected


menu = streamlit_menu()


# ============================================================
# HALAMAN HOME
# ============================================================
if menu == "Home":

    def home_page():
        # JUDUL DESKRIPSI
        st.markdown("<h2 class='section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)

        # FOTO HERO
        hero_image(
            url="https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
            badge="✦ Keluarga Bayesian ✦",
            title="Gapai Cita, Kejar mimpi, Di angkasa",
            subtitle="Momen kebersamaan yang tidak akan terlupakan."
        )

        # DESKRIPSI KELOMPOK
        st.markdown("""
            <div class="content-box">
                <b>Selamat datang di portal resmi kelompok Bayesian!</b><br><br>
                isi aja apa aja ini bingung.
            </div>
        """, unsafe_allow_html=True)

        # ==========================================
        # VIDEO KELOMPOK (FITUR BARU)
        # ==========================================
        st.markdown("""
            <h3 class="section-title" style="font-size:24px;">
                Video Profil & Kenangan
            </h3>
        """, unsafe_allow_html=True)

        st.markdown('<div class="video-container">', unsafe_allow_html=True)
        # Anda bisa mengganti URL video ini dengan link YouTube/MP4 kelompok Anda
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
        st.video(video_url)
        st.markdown('</div>', unsafe_allow_html=True)

        # JUDUL DOKUMENTASI
        st.markdown("""
            <h3 class="section-title" style="font-size:24px;">
                Dokumentasi Kegiatan Bayesian
            </h3>
        """, unsafe_allow_html=True)

        # DATA DOKUMENTASI — ISI TETAP
        kegiatan_Bayesian = [
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "First Moment", "desc": "Awal dari cerita yang panjang"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Our Journey", "desc": "Langkah demi langkah bersama"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Growing Together", "desc": "Tumbuh bersama melalui setiap proses"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "The Story", "desc": "Setiap foto menyimpan cerita."},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Good Times", "desc": "Keluh kesah, tawa dan cerita yang tak bisa dilupakan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq", "judul": "Until Forever", "desc": "Bukan akhir, hanya bagian dari perjalanan"}
        ]

        # MENAMPILKAN FOTO DALAM 3 KOLOM
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
                        else:
                            st.warning(f"Foto '{item['judul']}' gagal dimuat.")

        # KOMITMEN KELOMPOK
        st.markdown("""
            <div class="content-box">
                <b>Komitmen Kami:</b><br>
                Kami berkomitmen penuh dalam segala hal .................
            </div>
        """, unsafe_allow_html=True)

    home_page()


# ============================================================
# HALAMAN ABOUT US (TERBUKA SEPERTI TIRAI / GATE)
# ============================================================
elif menu == "About Us":

    def about_page():
        st.markdown("<h2 class='section-title'>About Us</h2>", unsafe_allow_html=True)

        # FOTO ANGGOTA — URL TETAP
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",
        ]

        # DATA ANGGOTA — ISI TETAP
        data_list = [
            {"nama": "Thomas Yustio", "sebagai": "Pak Lurah", "nim": "125450--", "fun_fact": "--", "motto_hidup": "--"},
            {"nama": "Syalom Nauli Jubilate ", "sebagai": "Bu Lurah", "nim": "125450--", "fun_fact": "--", "motto_hidup": "--"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"},
            {"nama": "Rizqy Ramadhan", "sebagai": "Anggota", "nim": "125450066", "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah", "motto_hidup": "Tetap lah bernafas"}
        ]

        # MENAMPILKAN KARTU ANGGOTA DENGAN EFEK TIRAI TERBUKA (3 KOLOM)
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
                            nim = html.escape(member["nim"])
                            fun_fact = html.escape(member["fun_fact"])
                            motto = html.escape(member["motto_hidup"])

                            role_class = (
                                "anggota"
                                if member["sebagai"].lower() == "anggota"
                                else ""
                            )

                            st.markdown(f"""
                                <div class="curtain-card">
                                    <!-- LAYAR DALAM / DETAIL (Terungkap saat tirai membuka) -->
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

                                    <!-- TIRAI ATAS (Foto Profil) -->
                                    <div class="curtain-top">
                                        <div class="photo-frame">
                                            <img src="{img_src}" alt="{html.escape(member['nama'], quote=True)}">
                                        </div>
                                    </div>

                                    <!-- TIRAI BAWAH (Nama & Jabatan) -->
                                    <div class="curtain-bottom">
                                        <h4>{nama}</h4>
                                        <span class="role-badge {role_class}">{sebagai}</span>
                                        <div class="hint">▼ Arahkan kursor untuk buka ▼</div>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)

                        else:
                            st.warning(f"Foto untuk {member['nama']} gagal dimuat.")

    about_page()
