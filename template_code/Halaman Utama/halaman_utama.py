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
# CSS — MODERN BLUE UI/UX
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

/* HEADER */
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

/* CONTENT BOX */
.content-box {
    position: relative;
    background: rgba(255,255,255,.95);
    padding: 30px 34px;
    border: 1px solid var(--border);
    border-radius: 18px;
    box-shadow: 0 8px 28px rgba(16,42,86,.07);
    margin-bottom: 32px;
    text-align: justify;
    line-height: 1.9;
    font-size: 15px;
    color: #40536B;
    overflow: hidden;
}

.content-box::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 5px;
    height: 100%;
    background: linear-gradient(180deg, #246BCE, #8EC5FC);
}

.content-box b {
    color: var(--blue);
    font-weight: 800;
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

/* HERO IMAGE */
.hero-image-wrapper {
    position: relative;
    width: 100%;
    margin: 0 auto 30px;
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,.8);
    box-shadow: 0 18px 45px rgba(16,42,86,.16);
    background: var(--navy);
}

.hero-image-wrapper img {
    display: block;
    width: 100%;
    height: 410px;
    object-fit: cover;
    transition: transform .6s ease;
}

.hero-image-wrapper:hover img {
    transform: scale(1.025);
}

.hero-image-wrapper .hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        0deg,
        rgba(9,30,65,.96) 0%,
        rgba(16,42,86,.45) 45%,
        transparent 100%
    );
    pointer-events: none;
}

.hero-image-wrapper .hero-caption {
    position: absolute;
    bottom: 28px;
    left: 32px;
    right: 32px;
    color: white;
}

.hero-image-wrapper .hero-badge {
    display: inline-block;
    padding: 7px 14px;
    border: 1px solid rgba(255,255,255,.4);
    background: rgba(80,145,225,.28);
    border-radius: 50px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
    color: white;
}

.hero-image-wrapper .hero-caption h3 {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 700;
    margin: 0;
    color: white;
}

.hero-image-wrapper .hero-caption p {
    font-size: 13px;
    margin-top: 8px;
    color: #E3EEFF;
    line-height: 1.6;
}

/* DOCUMENTATION CARDS */
.photo-card {
    position: relative;
    height: 230px;
    margin-bottom: 22px;
    border-radius: 18px;
    overflow: hidden;
    background: white;
    border: 1px solid var(--border);
    box-shadow: 0 7px 22px rgba(16,42,86,.10);
    transition: transform .3s ease, box-shadow .3s ease;
}

.photo-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 16px 32px rgba(36,107,206,.20);
}

.photo-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform .5s ease;
}

.photo-card:hover img {
    transform: scale(1.07);
}

.photo-card::after {
    content: '';
    position: absolute;
    inset: 30% 0 0;
    background: linear-gradient(
        0deg,
        rgba(10,35,75,.98),
        rgba(20,65,125,.4),
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
    padding: 24px 16px 17px;
    color: white;
    text-align: left;
}

.photo-card .overlay-title {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 5px;
    color: white;
}

.photo-card .overlay-desc {
    font-size: 11px;
    line-height: 1.5;
    color: #E2EDFF;
}

/* VIDEO CONTAINER */
.video-box {
    background: rgba(255,255,255,0.95);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(16,42,86,0.08);
    margin-bottom: 30px;
}

/* ============================================================
   KARTU ANGGOTA RINGKAS (LIST ABOUT US)
   ============================================================ */
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

/* ============================================================
   DETAIL ANGGOTA (ZOOM VIEW SESUAI FOTO REFERENSI KEDUA)
   ============================================================ */
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
    margin-bottom: 10px;
    font-size: 14px;
    color: #334963;
    line-height: 1.6;
}

.info-item b {
    color: var(--navy);
    display: inline-block;
    width: 110px;
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
            response = requests.get(
                candidate,
                headers=headers,
                timeout=25,
                allow_redirects=True
            )
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
            st.warning(
                "Gambar gagal dimuat. Pastikan file Google Drive "
                "dapat diakses oleh siapa saja yang memiliki link."
            )


layout_logo(url)
st.write("")
layout_logo(url1)

st.markdown(
    "<div style='margin-top: 35px;'></div>",
    unsafe_allow_html=True
)


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
                "box-shadow": "0 8px 25px rgba(16,42,86,0.09)",
                "border": "1px solid #D8E7FA",
                "margin-bottom": "35px",
            },
            "icon": {
                "color": "#246BCE",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "0 6px",
                "padding": "10px 22px",
                "border-radius": "10px",
                "color": "#102A56",
                "--hover-color": "#EAF3FF",
            },
            "nav-link-selected": {
                "background-color": "#246BCE",
                "color": "#FFFFFF",
                "box-shadow": "0 5px 14px rgba(36,107,206,0.25)",
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

        # STATISTIK RINGKAS KELOMPOK
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="stat-card"><div class="stat-number">10</div><div class="stat-label">Anggota Kelompok</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="stat-card"><div class="stat-number">2026</div><div class="stat-label">Adyatama ITERA</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="stat-card"><div class="stat-number">100%</div><div class="stat-label">Semangat & Kekeluargaan</div></div>', unsafe_allow_html=True)

        # JUDUL DESKRIPSI
        st.markdown(
            "<h2 class='section-title'>Deskripsi Kelompok</h2>",
            unsafe_allow_html=True
        )

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

        # DOKUMENTASI VIDEO KELOMPOK
        st.markdown("""
            <h3 class="section-title" style="font-size:24px;">
                Video Profil & Kenangan Bayesian
            </h3>
        """, unsafe_allow_html=True)

        st.markdown('<div class="video-box">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.markdown('</div>', unsafe_allow_html=True)

        # JUDUL DOKUMENTASI
        st.markdown("""
            <h3 class="section-title" style="font-size:24px;">
                Dokumentasi Kegiatan Bayesian
            </h3>
        """, unsafe_allow_html=True)

        # DATA DOKUMENTASI — ISI TETAP
        kegiatan_Bayesian = [
            {
                "url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
                "judul": "First Moment",
                "desc": "Awal dari cerita yang panjang"
            },
            {
                "url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
                "judul": "Our Journey",
                "desc": "Langkah demi langkah bersama"
            },
            {
                "url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
                "judul": "Growing Together",
                "desc": "Tumbuh bersama melalui setiap proses"
            },
            {
                "url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
                "judul": "The Story",
                "desc": "Setiap foto menyimpan cerita."
            },
            {
                "url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
                "judul": "Good Times",
                "desc": "Keluh kesah, tawa dan cerita yang tak bisa dilupakan"
            },
            {
                "url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
                "judul": "Until Forever",
                "desc": "Bukan akhir, hanya bagian dari perjalanan"
            }
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
                                    <img
                                        src="{img_src}"
                                        alt="{html.escape(item['judul'], quote=True)}"
                                    >
                                    <div class="overlay">
                                        <div class="overlay-title">
                                            {html.escape(item['judul'])}
                                        </div>
                                        <div class="overlay-desc">
                                            {html.escape(item['desc'])}
                                        </div>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)

                        else:
                            st.warning(
                                f"Foto '{item['judul']}' gagal dimuat. "
                                "Periksa izin Google Drive."
                            )

        # KOMITMEN KELOMPOK
        st.markdown("""
            <div class="content-box">
                <b>Komitmen Kami:</b><br>
                Kami berkomitmen penuh dalam segala hal .................
            </div>
        """, unsafe_allow_html=True)

    home_page()


# ============================================================
# HALAMAN ABOUT US (INTERAKTIF: CLICK TO ZOOM VIEW)
# ============================================================
elif menu == "About Us":

    def about_page():

        st.markdown(
            "<h2 class='section-title'>About Us — Buku Kating</h2>",
            unsafe_allow_html=True
        )

        # FOTO ANGGOTA — URL TETAP
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz"
        ] * 10

        # DATA ANGGOTA — ISI TETAP
        data_list = [
            {
                "nama": "Thomas Yustio",
                "sebagai": "Pak Lurah",
                "nim": "125450--",
                "umur": "21 Tahun",
                "asal": "Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "--",
                "sosmed": "@thomas_yustio",
                "kesan": "--",
                "pesan": "--",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Syalom Nauli Jubilate ",
                "sebagai": "Bu Lurah",
                "nim": "125450--",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "--",
                "sosmed": "@syalom_nauli",
                "kesan": "--",
                "pesan": "--",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 01",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 02",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 03",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 04",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 05",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 06",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 07",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 08",
                "nim": "125450066",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Bernafas",
                "sosmed": "@rizqy_rmdhn",
                "kesan": "Sangat seru dan penuh tantangan selama berkegiatan.",
                "pesan": "Semangat dan sukses selalu!",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            }
        ]

        # SESSION STATE UNTUK MELAKUKAN ZOOM DETIL PROFILE
        if "zoomed_member_idx" not in st.session_state:
            st.session_state["zoomed_member_idx"] = None

        # JIKA DITEKAN: TAMPILAN ZOOM SESUAI FOTO KEDUAMU
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
                st.markdown(f"""
                <div class="detail-container">
                    <div class="detail-img-box">
                        <img src="{img_src}" alt="{html.escape(m['nama'])}">
                    </div>
                    <div class="detail-info-box">
                        <h2>{html.escape(m['nama'])}</h2>
                        <div class="info-item"><b>NIM:</b> {html.escape(m['nim'])}</div>
                        <div class="info-item"><b>Umur:</b> {html.escape(m.get('umur', '20 Tahun'))}</div>
                        <div class="info-item"><b>Asal:</b> {html.escape(m.get('asal', 'Indonesia'))}</div>
                        <div class="info-item"><b>Alamat:</b> {html.escape(m.get('alamat', 'Kesekretariatan HMSD'))}</div>
                        <div class="info-item"><b>Hobbi:</b> {html.escape(m.get('hobbi', '--'))}</div>
                        <div class="info-item"><b>Sosial Media:</b> {html.escape(m.get('sosmed', '--'))}</div>
                        <div class="info-item"><b>Fun Fact:</b> {html.escape(m['fun_fact'])}</div>
                        <div class="info-item"><b>Kesan:</b> {html.escape(m.get('kesan', '--'))}</div>
                        <div class="info-item"><b>Pesan:</b> {html.escape(m.get('pesan', '--'))}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # JIKA BELUM DITEKAN: DAFTAR KARTU ANGGOTA
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

                                # BUTTON UNTUK PENCET / ZOOM CARD
                                if st.button(f"🔍 Lihat Detail Profil", key=f"zoom_btn_{idx}", use_container_width=True):
                                    st.session_state["zoomed_member_idx"] = idx
                                    st.rerun()

                            else:
                                st.warning(f"Foto untuk {member['nama']} gagal dimuat.")

    about_page()
