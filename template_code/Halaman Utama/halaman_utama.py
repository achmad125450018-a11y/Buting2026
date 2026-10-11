import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html

# ============================================================
# 🎨 SUPER PREMIUM UI/UX — POISSON EDITION
# ============================================================
st.markdown("""
<style>
    /* ---------- FONT IMPORT ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ---------- GLOBAL ---------- */
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

    /* ---------- MAIN HEADER ---------- */
    .main-title {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        font-size: 3.6em !important;
        letter-spacing: 1px;
        margin-bottom: 6px;
        background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 2px 20px rgba(112,28,35,0.15);
        position: relative;
        display: inline-block;
        width: 100%;
    }
    .main-title::after {
        content: '';
        display: block;
        width: 90px;
        height: 3px;
        margin: 14px auto 0;
        background: linear-gradient(90deg, transparent, #701c23, transparent);
        border-radius: 3px;
    }

    .main-subtitle {
        text-align: center;
        font-family: 'Inter', sans-serif;
        color: #6b5a52;
        font-weight: 500;
        font-size: 1.15em !important;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 30px;
        margin-top: 6px;
    }

    /* ---------- SECTION TITLE ---------- */
    .section-title {
        text-align: center;
        font-family: 'Playfair Display', serif;
        color: #701c23;
        font-weight: 700;
        font-size: 1.9em;
        margin-top: 45px;
        margin-bottom: 30px;
        position: relative;
        display: block;
    }
    .section-title::before,
    .section-title::after {
        content: '✦';
        color: #d9c3a3;
        margin: 0 18px;
        font-size: 0.7em;
        vertical-align: middle;
    }

    /* ---------- CONTENT BOX (GLASS PREMIUM) ---------- */
    .content-box {
        background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
        padding: 38px 42px;
        border-radius: 20px;
        box-shadow:
            0 1px 0 rgba(255,255,255,0.9) inset,
            0 10px 30px rgba(112,28,35,0.07),
            0 2px 8px rgba(112,28,35,0.04);
        border: 1px solid rgba(217,195,163,0.55);
        margin-bottom: 38px;
        text-align: justify;
        line-height: 1.95;
        font-size: 15.5px;
        color: #3a2f2b;
        position: relative;
        overflow: hidden;
    }
    .content-box::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 5px; height: 100%;
        background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
    }
    .content-box b {
        color: #701c23;
        font-weight: 700;
        letter-spacing: 0.2px;
    }

    /* ---------- PHOTO CARD (PREMIUM) ---------- */
    .photo-card {
        position: relative;
        overflow: hidden;
        border-radius: 16px;
        box-shadow:
            0 4px 14px rgba(112,28,35,0.10),
            0 1px 3px rgba(0,0,0,0.05);
        border: 1px solid rgba(217,195,163,0.7);
        margin-bottom: 22px;
        height: 210px;
        background-color: #ffffff;
        transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1),
                    box-shadow 0.4s ease;
    }
    .photo-card:hover {
        transform: translateY(-6px);
        box-shadow:
            0 18px 40px rgba(112,28,35,0.22),
            0 4px 12px rgba(112,28,35,0.12);
    }
    .photo-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1),
                    filter 0.5s ease;
        filter: saturate(1) brightness(1);
    }
    .photo-card:hover img {
        transform: scale(1.1);
        filter: saturate(1.15) brightness(1.05);
    }
    /* Shimmer effect */
    .photo-card::after {
        content: '';
        position: absolute;
        top: 0; left: -75%;
        width: 50%; height: 100%;
        background: linear-gradient(
            120deg,
            transparent 0%,
            rgba(255,255,255,0.35) 50%,
            transparent 100%
        );
        transform: skewX(-20deg);
        transition: left 0.7s ease;
        pointer-events: none;
    }
    .photo-card:hover::after {
        left: 125%;
    }
    .photo-card .overlay {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        background: linear-gradient(
            to top,
            rgba(112,28,35,0.97) 0%,
            rgba(112,28,35,0.85) 55%,
            transparent 100%
        );
        color: #ffffff;
        padding: 26px 14px 14px 14px;
        opacity: 0;
        transform: translateY(10px);
        transition: opacity 0.4s ease, transform 0.4s ease;
        text-align: center;
    }
    .photo-card:hover .overlay {
        opacity: 1;
        transform: translateY(0);
    }
    .photo-card .overlay-title {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 15px;
        color: #f4f0eb;
        margin-bottom: 4px;
        letter-spacing: 0.4px;
    }
    .photo-card .overlay-desc {
        font-size: 11.5px;
        line-height: 1.4;
        color: rgba(244,240,235,0.92);
        font-weight: 400;
    }

    /* ---------- FLIP CARD (ABOUT US PREMIUM) ---------- */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 400px;
        perspective: 1400px;
        margin-bottom: 28px;
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.9s cubic-bezier(0.4, 0.2, 0.2, 1);
        transform-style: preserve-3d;
        border-radius: 18px;
        box-shadow:
            0 8px 24px rgba(112,28,35,0.12),
            0 2px 6px rgba(112,28,35,0.06);
    }
    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
        box-shadow:
            0 20px 50px rgba(112,28,35,0.28),
            0 6px 14px rgba(112,28,35,0.15);
    }
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 18px;
        padding: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .flip-card-front {
        background: linear-gradient(160deg, #ffffff 0%, #fdfaf6 100%);
        color: #701c23;
        border: 1px solid rgba(217,195,163,0.8);
        box-shadow: 0 0 0 1px rgba(255,255,255,0.6) inset;
    }
    .flip-card-front img {
        width: 165px;
        height: 205px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 14px;
        border: 2px solid #701c23;
        box-shadow: 0 6px 18px rgba(112,28,35,0.22);
        transition: transform 0.5s ease, box-shadow 0.5s ease;
    }
    .flip-card:hover .flip-card-front img {
        transform: scale(1.03);
        box-shadow: 0 10px 26px rgba(112,28,35,0.32);
    }
    .flip-card-front h4 {
        margin: 6px 0 0 0;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        color: #701c23;
        font-size: 16.5px;
        letter-spacing: 0.3px;
        line-height: 1.3;
    }
    .flip-card-front .flip-hint {
        font-size: 10.5px;
        color: #a89790;
        margin-top: 8px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .flip-card-back {
        background: linear-gradient(150deg, #701c23 0%, #4e1318 100%);
        color: #ffffff;
        transform: rotateY(180deg);
        text-align: left;
        align-items: flex-start;
        padding: 26px 24px;
        box-sizing: border-box;
        border: 1px solid rgba(217,195,163,0.35);
        box-shadow: 0 0 30px rgba(112,28,35,0.4) inset;
    }
    .flip-card-back h4 {
        font-family: 'Playfair Display', serif;
        color: #d9c3a3;
        font-weight: 700;
        margin-bottom: 14px;
        border-bottom: 1px solid rgba(217,195,163,0.35);
        padding-bottom: 8px;
        width: 100%;
        font-size: 17px;
        letter-spacing: 0.3px;
    }
    .flip-card-back p {
        font-size: 12.8px;
        margin: 6px 0;
        line-height: 1.55;
        color: rgba(255,255,255,0.93);
    }
    .flip-card-back .label {
        font-weight: 700;
        color: #d9c3a3;
        letter-spacing: 0.3px;
    }

    /* ---------- NAVBAR GLASSMORPHISM ---------- */
    div[data-testid="stHorizontalBlock"] > div:has(> div > div > nav) {
        backdrop-filter: blur(12px);
    }

    /* ---------- SCROLLBAR PREMIUM ---------- */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #f4f0eb; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #701c23, #a8323d);
        border-radius: 10px;
        border: 2px solid #f4f0eb;
    }
    ::-webkit-scrollbar-thumb:hover { background: #701c23; }

    /* ---------- FOOTER SPACING ---------- */
    .block-container { padding-top: 2rem !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# UTIL FUNCTIONS
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
    """Mengunduh gambar dari Google Drive atau URL gambar langsung."""
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
                candidate, headers=headers, timeout=25, allow_redirects=True,
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
    """Mengubah gambar menjadi data URI agar bisa dipakai oleh HTML img."""
    img = load_image(url)
    if img is None:
        return None
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=88, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


# ============================================================
# HEADER
# ============================================================
st.markdown("""
    <div>
        <h1 class='main-title'>WEBSITE KATING</h1>
        <p class='main-subtitle'>CEO HMSD Adyatama ITERA 2026</p>
    </div>
""", unsafe_allow_html=True)

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"

def layout_logo(url):
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    with col2:
        img = load_image(url)
        if img is not None:
            st.image(img, use_container_width=True)
        else:
            st.warning("Gambar gagal dimuat. Pastikan file Google Drive dapat diakses oleh siapa saja yang memiliki link.")

layout_logo(url)
st.write("")
layout_logo(url1)

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "10px!important",
                "background-color": "rgba(255,255,255,0.85)",
                "backdrop-filter": "blur(12px)",
                "border-radius": "14px",
                "box-shadow": "0 8px 24px rgba(112,28,35,0.10), 0 1px 0 rgba(255,255,255,0.9) inset",
                "border": "1px solid rgba(217,195,163,0.6)",
                "margin-bottom": "38px",
            },
            "icon": {"color": "#701c23", "font-size": "18px"},
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "0 6px",
                "padding": "10px 22px",
                "border-radius": "10px",
                "color": "#701c23",
                "--hover-color": "rgba(217,195,163,0.25)",
                "transition": "all 0.3s ease",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #701c23 0%, #a8323d 100%)",
                "color": "#ffffff",
                "box-shadow": "0 6px 16px rgba(112,28,35,0.35)",
            },
        },
    )
    return selected

menu = streamlit_menu()


# ============================================================
# HOME PAGE
# ============================================================
if menu == "Home":
    def home_page():
        st.markdown("<h2 class='section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content-box'>
                <b>Selamat datang di portal resmi kelompok Poisson!</b><br><br>
                Kelompok kami merupakan wadah kolaborasi, kebersamaan, dan dedikasi tinggi dalam menjalani rangkaian kegiatan pengenalan kampus dan penugasan Buku Kating. Di sini, kami tidak hanya belajar menyelesaikan setiap tantangan akademik secara bersama-sama, tetapi juga membangun ikatan kekeluargaan yang erat, saling mendukung dalam setiap proses adaptasi, serta menjunjung tinggi nilai solidaritas dan profesionalisme sebagai bagian dari keluarga besar HMSD Adyatama ITERA.
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<h3 class='section-title' style='font-size:22px;'>Dokumentasi Kegiatan Poisson</h3>", unsafe_allow_html=True)

        kegiatan_poisson = [
            {"url": "https://drive.google.com/uc?export=view&id=1dDPrlobxQlHnAwMZKdoSuGcJviyfueTn", "judul": "First Moment", "desc": "Awal dari cerita yang panjang"},
            {"url": "https://drive.google.com/uc?export=view&id=1Oi4CMuo7gzPc9cobE01SUmZQbR0bcfA2", "judul": "Our Journey", "desc": "Langkah demi langkah bersama"},
            {"url": "https://drive.google.com/uc?export=view&id=1j02Eq5ZqVHUFdGnEvLV5oDiHxZvoLCdc", "judul": "Growing Together", "desc": "Tumbuh bersama melalui setiap proses"},
            {"url": "https://drive.google.com/uc?export=view&id=1Y9aO6QYXVf3dkHCWwpAZPf6KNrLguEmx", "judul": "The Story", "desc": "Setiap foto menyimpan cerita."},
            {"url": "https://drive.google.com/uc?export=view&id=1FXn8y19dNrGSnjTvgRe9QmQpRwx5slv9", "judul": "Good Times", "desc": "Keluh kesah, tawa dan cerita yang tak bisa dilupakan"},
            {"url": "https://drive.google.com/uc?export=view&id=1bxRGpALCGFINoBxPCsA9MpiW6cxpyPaa", "judul": "Until Forever", "desc": "Bukan akhir, hanya bagian dari perjalanan"}
        ]

        for i in range(0, len(kegiatan_poisson), 3):
            cols = st.columns(3)
            for j in range(3):
                idx = i + j
                if idx < len(kegiatan_poisson):
                    item = kegiatan_poisson[idx]
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
                            st.warning(f"Foto '{item['judul']}' gagal dimuat. Periksa izin Google Drive.")

        st.markdown("""
            <div class='content-box'>
                <b>Komitmen Kami:</b><br>
                Kami berkomitmen penuh untuk terus bergerak seirama, saling menguatkan dalam menghadapi dinamika perkuliahan, serta menyelesaikan seluruh rangkaian tanggung jawab dengan hasil yang terbaik dan membanggakan.
            </div>
        """, unsafe_allow_html=True)

    home_page()


# ============================================================
# ABOUT US PAGE
# ============================================================
elif menu == "About Us":
    def about_page():
        st.markdown("<h2 class='section-title'>About Us</h2>", unsafe_allow_html=True)

        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OZWQEzUE1biYVl5igEDRCdqYE1Kdculc",
            "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
            "https://drive.google.com/uc?export=view&id=1DF_qQCOIFDvyjG5SEOL8DURaTbjy1OWc",
            "https://drive.google.com/uc?export=view&id=19FctJT5o6JBmGICiSu15NAIwLR4VFhW_",
            "https://drive.google.com/uc?export=view&id=1jDU86oPLsjea0l0FiwbVjF6Esuekw4MG",
            "https://drive.google.com/uc?export=view&id=1OOVOfx6v2WEL_lPFwtqt_2Pnp9dmZNAU",
            "https://drive.google.com/uc?export=view&id=1OcyHkxkcelFVtIa2oc0fF1aO85im1_Vp",
            "https://drive.google.com/uc?export=view&id=1K1XEcndMVCAyAFS2i6j8SlWriPLSNAau",
            "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
            "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
            "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
        ]

        data_list = [
            {"nama": "Yobel Imanuel Pasaribu", "sebagai": "Pak Lurah", "nim": "125450116", "fun_fact": "Bawa bantal guling dari kecil sampe sekaran", "motto_hidup": "New semester new me"},
            {"nama": "Rena Aprilia", "sebagai": "Bu Lurah", "nim": "125450109", "fun_fact": "Suka nyemilin es batu saat santai", "motto_hidup": "Konsisten adalah kunci sukses"},
            {"nama": "Samuel Kristian", "sebagai": "Anggota", "nim": "125450084", "fun_fact": "Hafal seluruh lirik lagu daerah", "motto_hidup": "Tetap semangat pantang menyerah"},
            {"nama": "Nailatun Inayah", "sebagai": "Anggota", "nim": "125450037", "fun_fact": "Bisa tidur di segala jenis kendaraan", "motto_hidup": "Jalanin dulu aja dengan ikhlas"},
            {"nama": "Alfajri Anwar", "sebagai": "Anggota", "nim": "125450074", "fun_fact": "Suka begadang demi nonton bola", "motto_hidup": "Usaha tidak mengkhianati hasil"},
            {"nama": "Inness Eymard Gultom", "sebagai": "Anggota", "nim": "125460075", "fun_fact": "Pecinta kucing garis keras", "motto_hidup": "Jadilah versi terbaik dirimu"},
            {"nama": "Kayyisah Mazaya", "sebagai": "Anggota", "nim": "125450033", "fun_fact": "Selalu membawa tumbler sendiri", "motto_hidup": "Fokus pada prosesnya"},
            {"nama": "Fadhilah Adelyia Putri", "sebagai": "Anggota", "nim": "125450020", "fun_fact": "Sering salah panggil nama dosen", "motto_hidup": "Senyum adalah ibadah"},
            {"nama": "Dzahra Adila Fatma", "sebagai": "Anggota", "nim": "125450028", "fun_fact": "Hobi koleksi sepatu sneakers", "motto_hidup": "Hari ini harus lebih baik"},
            {"nama": "Egia Ninta Pepayosa Ketaren", "sebagai": "Anggota", "nim": "125450008", "fun_fact": "Suka minum es teh manis jumbo", "motto_hidup": "Selalu bersyukur setiap hari"},
            {"nama": "Achmad Fardhan Al Basri Bandarudin", "sebagai": "Anggota", "nim": "125450018", "fun_fact": "Main game online sampai pagi", "motto_hidup": "Pantang pulang sebelum selesai"}
        ]

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
                            st.markdown(f"""
                                <div class="flip-card">
                                    <div class="flip-card-inner">
                                        <div class="flip-card-front">
                                            <img src="{img_src}" alt="{html.escape(member['nama'], quote=True)}">
                                            <h4>{nama}</h4>
                                            <div class="flip-hint">Hover untuk detail</div>
                                        </div>
                                        <div class="flip-card-back">
                                            <h4>{nama}</h4>
                                            <p><span class="label">Sebagai:</span> {sebagai}</p>
                                            <p><span class="label">NIM:</span> {nim}</p>
                                            <p><span class="label">Fun Fact:</span> {fun_fact}</p>
                                            <p><span class="label">Motto:</span> {motto}</p>
                                        </div>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.warning(f"Foto untuk {member['nama']} gagal dimuat. Periksa izin Google Drive.")

    about_page()
