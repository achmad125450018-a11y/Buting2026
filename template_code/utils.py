import streamlit as st
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html as html_lib

def setup_buku_kating_page():
    """Inject CSS + title. Panggil di awal setiap file Buku Kating."""
    PREMIUM_CSS = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #222222; }
    .stApp {
        background: radial-gradient(circle at 15% 10%, rgba(112,28,35,0.06) 0%, transparent 45%),
                    radial-gradient(circle at 85% 90%, rgba(217,195,163,0.18) 0%, transparent 50%),
                    linear-gradient(180deg, #f4f0eb 0%, #efe8df 100%);
        background-attachment: fixed;
    }
    .centered-title {
        text-align: center; font-family: 'Playfair Display', serif; font-weight: 800;
        font-size: 3em !important; margin-bottom: 8px;
        background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .profile-card {
        background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
        padding: 28px 32px; border-radius: 20px; border: 1px solid rgba(217,195,163,0.55);
        box-shadow: 0 10px 30px rgba(112,28,35,0.08); margin-bottom: 22px;
    }
    </style>
    """
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

def get_drive_file_id(url):
    try:
        parsed = urlparse(url); query = parse_qs(parsed.query)
        if query.get("id"): return query["id"][0]
        parts = parsed.path.split("/")
        if "d" in parts:
            idx = parts.index("d")
            if idx + 1 < len(parts): return parts[idx + 1]
    except: pass
    return None

@st.cache_data(show_spinner=False, max_entries=50)
def load_image(url):
    file_id = get_drive_file_id(url)
    candidate_urls = []
    if file_id:
        candidate_urls.extend([
            f"https://drive.google.com/thumbnail?id={file_id}&sz=w1200",
            f"https://drive.google.com/uc?export=download&id={file_id}",
            f"https://drive.google.com/uc?export=view&id={file_id}",
        ])
    candidate_urls.append(url)
    for candidate in dict.fromkeys(candidate_urls):
        try:
            response = requests.get(candidate, headers={"User-Agent": "Mozilla/5.0"}, timeout=15, stream=True)
            response.raise_for_status()
            img_bytes = BytesIO(response.content)
            img = ImageOps.exif_transpose(Image.open(img_bytes)).convert("RGB")
            img.load(); response.close(); img_bytes.close()
            return img
        except: continue
    return None

@st.cache_data(show_spinner=False, max_entries=80)
def image_data_uri(url, max_dim=800, quality=80):
    img = load_image(url)
    if img is None: return None
    img = img.copy()
    if max(img.size) > max_dim: img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buffer = BytesIO(); img.save(buffer, format="JPEG", quality=quality, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8"); buffer.close()
    return f"data:image/jpeg;base64,{encoded}"

def render_photo(img_src, alt="Foto"):
    if not img_src:
        st.markdown('<div style="width:100%;aspect-ratio:3/4;display:flex;align-items:center;justify-content:center;background:#eee;border-radius:13px;">Foto tidak tersedia</div>', unsafe_allow_html=True)
        return
    st.markdown(f'<div class="photo-wrapper"><img src="{img_src}" alt="{html_lib.escape(alt, quote=True)}" style="width:100%;border-radius:13px;"></div>', unsafe_allow_html=True)

def render_profile_card(m):
    # (Fungsi render_profile_card tetap sama seperti sebelumnya)
    nama = html_lib.escape(str(m.get("nama", "-")))
    jabatan = html_lib.escape(str(m.get("jabatan", "-")))
    html_block = f'<div class="profile-card"><h3>{nama}</h3><p>{jabatan}</p></div>'
    st.markdown(html_block, unsafe_allow_html=True)

def display_images_with_data(gambar_urls, data_list, batch_size=5, key="default"):
    # (Fungsi display_images_with_data tetap sama seperti sebelumnya)
    total_items = min(len(gambar_urls), len(data_list))
    for i in range(min(batch_size, total_items)):
        col1, col2 = st.columns([1, 2])
        with col1: render_photo(image_data_uri(gambar_urls[i]), data_list[i].get("nama"))
        with col2: render_profile_card(data_list[i])

def streamlit_menu(default_index=0):
    from streamlit_option_menu import option_menu
    return option_menu(
        menu_title=None, options=["Kesekjenan", "Baleg", "Senator", "Departemen PSDA", "Departemen MIKFES", "Departemen Eksternal", "Departemen Internal", "Departemen SSD", "Departemen Medkraf", "Departemen MINBAK"],
        icons=["people-fill"] * 10, default_index=default_index, orientation="horizontal",
        styles={"container": {"padding": "5px!important", "background-color": "rgba(255,255,255,0.85)", "border-radius": "14px", "border": "1px solid rgba(217,195,163,0.6)"}, "nav-link-selected": {"background": "linear-gradient(135deg, #701c23 0%, #a8323d 100%)", "color": "#ffffff"}}
    )
