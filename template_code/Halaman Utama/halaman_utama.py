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

/* CONTENT */
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

/* FLIP CARDS */
.flip-card {
    width: 100%;
    height: 390px;
    perspective: 1400px;
    margin-bottom: 24px;
    position: relative;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform .8s ease;
    transform-style: preserve-3d;
    border-radius: 20px;
    box-shadow: 0 10px 28px rgba(16,42,86,.10);
}

.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border-radius: 20px;
    overflow: hidden;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
}

.flip-card-front {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px 16px;
    background: linear-gradient(160deg, #FFFFFF, #EDF5FF);
    border: 1px solid #D4E5FB;
    color: var(--navy);
}

.flip-card-front::before {
    content: '';
    position: absolute;
    width: 180px;
    height: 180px;
    top: -90px;
    right: -65px;
    border-radius: 50%;
    background: rgba(91,164,255,.12);
}

.flip-card-front .photo-frame {
    position: relative;
    z-index: 1;
    width: 150px;
    height: 180px;
    padding: 4px;
    margin-bottom: 16px;
    border-radius: 16px;
    background: linear-gradient(135deg, #102A56, #4A9BF5);
    box-shadow: 0 8px 24px rgba(36,107,206,.23);
}

.flip-card-front .photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    border-radius: 12px;
}

.flip-card-front h4 {
    position: relative;
    z-index: 1;
    max-width: 95%;
    font-size: 14px;
    line-height: 1.5;
    font-weight: 800;
    color: var(--navy);
    margin: 0 0 10px;
}

.flip-card-front .role-badge {
    position: relative;
    z-index: 1;
    display: inline-block;
    padding: 6px 14px;
    border-radius: 30px;
    background: linear-gradient(135deg, #102A56, #246BCE);
    color: white;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.flip-card-front .role-badge.anggota {
    background: #DCEBFF;
    color: #174A91;
}

.flip-card-front .flip-hint {
    position: relative;
    z-index: 1;
    font-size: 9px;
    margin-top: 10px;
    color: #7790B0;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.flip-card-back {
    transform: rotateY(180deg);
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    padding: 20px 17px;
    background: linear-gradient(145deg, #153B72, #0B2044);
    border: 1px solid #3B6EAD;
    color: white;
}

.flip-card-back::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(
        rgba(180,215,255,.15) 1px,
        transparent 1px
    );
    background-size: 14px 14px;
    pointer-events: none;
}

.flip-card-back h4 {
    position: relative;
    z-index: 1;
    font-size: 15px;
    font-weight: 800;
    line-height: 1.5;
    color: white;
    margin: 0 0 5px;
}

.flip-card-back .back-role {
    position: relative;
    z-index: 1;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #A8D2FF;
    margin-bottom: 13px;
}

.flip-card-back .divider {
    position: relative;
    z-index: 1;
    height: 2px;
    width: 100%;
    margin-bottom: 13px;
    background: linear-gradient(90deg, #5CA9FF, transparent);
}

.flip-card-back p {
    position: relative;
    z-index: 1;
    font-size: 11px;
    line-height: 1.5;
    padding: 8px 10px;
    margin: 0 0 8px;
    background: rgba(255,255,255,.08);
    border-left: 3px solid #72B7FF;
    border-radius: 7px;
    color: #F1F6FF;
    overflow-wrap: anywhere;
}

.flip-card-back .label {
    display: block;
    color: #9CCBFF;
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 3px;
}

/* NAVBAR */
div[data-testid="stImage"] img {
    border-radius: 16px;
}

.stApp div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 9px;
}

::-webkit-scrollbar-track {
    background: #EDF4FF;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #246BCE, #8EC5FC);
    border-radius: 10px;
    border: 2px solid #EDF4FF;
}

/* MOBILE */
@media (max-width: 768px) {
    .block-container {
        padding: 1.2rem 1rem 2rem !important;
    }

    .main-title {
        font-size: 2.3rem !important;
    }

    .main-subtitle {
        font-size: .72rem !important;
        letter-spacing: 1.2px;
    }

    .section-title {
        font-size: 1.55rem;
        margin-top: 30px;
    }

    .hero-image-wrapper img {
        height: 280px;
    }

    .hero-image-wrapper .hero-caption {
        left: 18px;
        right: 18px;
        bottom: 18px;
    }

    .hero-image-wrapper .hero-caption h3 {
        font-size: 23px;
    }

    .content-box {
        padding: 24px 22px;
        font-size: 14px;
    }

    .photo-card {
        height: 190px;
    }

    .flip-card {
        height: 365px;
    }
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
# HALAMAN ABOUT US
# ============================================================
elif menu == "About Us":

    def about_page():

        st.markdown(
            "<h2 class='section-title'>About Us</h2>",
            unsafe_allow_html=True
        )

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
            {
                "nama": "Thomas Yustio",
                "sebagai": "Pak Lurah",
                "nim": "125450--",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Syalom Nauli Jubilate ",
                "sebagai": "Bu Lurah",
                "nim": "125450--",
                "fun_fact": "--",
                "motto_hidup": "--"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas"
            }
        ]

        # MENAMPILKAN KARTU ANGGOTA DALAM 3 KOLOM
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
                                <div class="flip-card">
                                    <div class="flip-card-inner">

                                        <div class="flip-card-front">
                                            <div class="photo-frame">
                                                <img
                                                    src="{img_src}"
                                                    alt="{html.escape(member['nama'], quote=True)}"
                                                >
                                            </div>

                                            <h4>{nama}</h4>

                                            <span class="role-badge {role_class}">
                                                {sebagai}
                                            </span>

                                            <div class="flip-hint">
                                                Arahkan kursor untuk detail
                                            </div>
                                        </div>

                                        <div class="flip-card-back">
                                            <h4>{nama}</h4>

                                            <div class="back-role">
                                                {sebagai}
                                            </div>

                                            <div class="divider"></div>

                                            <p>
                                                <span class="label">NIM</span>
                                                {nim}
                                            </p>

                                            <p>
                                                <span class="label">Fun Fact</span>
                                                {fun_fact}
                                            </p>

                                            <p>
                                                <span class="label">Motto Hidup</span>
                                                {motto}
                                            </p>
                                        </div>

                                    </div>
                                </div>
                            """, unsafe_allow_html=True)

                        else:
                            st.warning(
                                f"Foto untuk {member['nama']} gagal dimuat. "
                                "Periksa izin Google Drive."
                            )

    about_page()
