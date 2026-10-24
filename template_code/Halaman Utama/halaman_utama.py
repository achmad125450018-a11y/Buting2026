import streamlit as st
from streamlit_option_menu import option_menu
import html
from utils import load_image, image_data_uri

# ============================================================
# 🎨 CUSTOM CSS (Diisolasi dengan Class .home-xxx)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

.home-title {
    text-align: center; font-family: 'Playfair Display', serif; font-weight: 900;
    font-size: 3.6em !important; margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.home-subtitle { text-align: center; color: #6b5a52; font-weight: 500; font-size: 1.15em !important; letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 30px; }
.home-section-title { text-align: center; font-family: 'Playfair Display', serif; color: #701c23; font-weight: 700; font-size: 1.9em; margin-top: 45px; margin-bottom: 30px; }

.home-content-box {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%); padding: 38px 42px; border-radius: 20px;
    border: 1px solid rgba(217,195,163,0.55); margin-bottom: 38px; text-align: justify; line-height: 1.95; color: #3a2f2b;
}

.home-photo-card {
    position: relative; overflow: hidden; border-radius: 16px; border: 1px solid rgba(217,195,163,0.7); height: 210px; background-color: #ffffff;
}
.home-photo-card img { width: 100%; height: 100%; object-fit: cover; }

.home-hero-wrapper { position: relative; max-width: 1000px; margin: 0 auto 28px auto; border-radius: 20px; overflow: hidden; border: 1px solid rgba(217,195,163,0.65); }
.home-hero-wrapper img { width: 100%; height: 380px; object-fit: cover; display: block; }
</style>
""", unsafe_allow_html=True)

def hero_image(url, title="Satu Tim, Satu Cerita", subtitle="Momen kebersamaan."):
    img_src = image_data_uri(url, max_dim=1200, quality=85)
    if img_src:
        st.markdown(f'<div class="home-hero-wrapper"><img src="{img_src}"><h3 style="text-align:center;">{title}</h3><p style="text-align:center;">{subtitle}</p></div>', unsafe_allow_html=True)

# HEADER
st.markdown("<h1 class='home-title'>WEBSITE KATING</h1>", unsafe_allow_html=True)
st.markdown("<p class='home-subtitle'>CEO HMSD Adyatama ITERA 2026</p>", unsafe_allow_html=True)

# LOGO
url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"
col1, col2, col3 = st.columns([1.5, 1, 1.5])
with col2:
    img = load_image(url)
    if img: st.image(img, use_container_width=True)
st.write("")
col1, col2, col3 = st.columns([1.5, 1, 1.5])
with col2:
    img1 = load_image(url1)
    if img1: st.image(img1, use_container_width=True)

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

# NAVBAR HALAMAN UTAMA
menu = option_menu(
    menu_title=None, options=["Home", "About Us"], icons=["house-door", "hand-index"],
    default_index=0, orientation="horizontal",
    styles={"container": {"padding": "10px!important", "background-color": "rgba(255,255,255,0.85)", "border-radius": "14px", "border": "1px solid rgba(217,195,163,0.6)"}, "nav-link-selected": {"background": "linear-gradient(135deg, #701c23 0%, #a8323d 100%)", "color": "#ffffff"}}
)

if menu == "Home":
    st.markdown("<h2 class='home-section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)
    hero_image("https://drive.google.com/uc?export=view&id=1b38uX_AFwdNc3-03NWQPcOX-TIOdxDee")
    st.markdown("""
        <div class='home-content-box'>
            <b>Selamat datang di portal resmi kelompok Poisson!</b><br><br>
            Kelompok kami merupakan wadah kolaborasi, kebersamaan, dan dedikasi tinggi dalam menjalani rangkaian kegiatan pengenalan kampus dan penugasan Buku Kating.
        </div>
    """, unsafe_allow_html=True)

elif menu == "About Us":
    st.markdown("<h2 class='home-section-title'>About Us</h2>", unsafe_allow_html=True)
    st.write("Konten About Us diletakkan di sini (terpisah dari CSS global).")
