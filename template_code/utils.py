# utils.py
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html as html_lib


# ============================================================
# 🎨 PREMIUM CSS — BUKU KATING
# ============================================================
PREMIUM_CSS = """
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
.profile-subheader.leader {
    background: linear-gradient(135deg, #b8912e 0%, #e8c874 50%, #b8912e 100%);
    color: #4e1318;
    box-shadow: 0 4px 14px rgba(184,145,46,0.45);
    text-shadow: 0 1px 0 rgba(255,255,255,0.25);
}
.profile-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d9c3a3, transparent);
    margin: 4px 0 16px 0;
    position: relative;
    z-index: 1;
}

.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px 18px;
    position: relative;
    z-index: 1;
}
.info-item {
    font-size: 13px;
    line-height: 1.55;
    color: #3a2f2b;
    padding: 8px 12px;
    border-radius: 10px;
    background: rgba(217,195,163,0.10);
    border-left: 2px solid rgba(217,195,163,0.7);
    transition: background 0.3s ease, border-color 0.3s ease;
}
.info-item:hover {
    background: rgba(217,195,163,0.20);
    border-left-color: #701c23;
}
.info-item.full {
    grid-column: 1 / -1;
}
.info-label {
    display: block;
    font-weight: 700;
    color: #701c23;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    font-size: 9.5px;
    margin-bottom: 2px;
}
.info-value {
    color: #2b2320;
    font-weight: 500;
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

.photo-wrapper {
    position: relative;
    padding: 6px;
    border-radius: 18px;
    background: linear-gradient(135deg, #701c23 0%, #d9c3a3 50%, #701c23 100%);
    box-shadow:
        0 12px 28px rgba(112,28,35,0.22),
        0 4px 10px rgba(112,28,35,0.12);
    margin-bottom: 12px;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.photo-wrapper:hover {
    transform: translateY(-4px);
    box-shadow:
        0 18px 38px rgba(112,28,35,0.32),
        0 6px 14px rgba(112,28,35,0.18);
}
.photo-wrapper img {
    display: block;
    width: 100%;
    aspect-ratio: 3 / 4;
    object-fit: cover;
    border-radius: 13px;
}
.photo-corner {
    position: absolute;
    width: 22px; height: 22px;
    border: 2px solid #f4f0eb;
    opacity: 0.9;
    pointer-events: none;
}
.photo-corner.tl { top: 10px; left: 10px; border-right: none; border-bottom: none; border-top-left-radius: 8px; }
.photo-corner.br { bottom: 10px; right: 10px; border-left: none; border-top: none; border-bottom-right-radius: 8px; }

.stAlert { border-radius: 12px !important; }

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #f4f0eb; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #701c23, #a8323d);
    border-radius: 10px;
    border: 2px solid #f4f0eb;
}

.block-container { padding-top: 2rem !important; }
</style>
"""


# ============================================================
# ⚙️ SETUP PAGE
# ============================================================
def setup_buku_kating_page():
    """Inject CSS + title. Panggil di awal setiap file Buku Kating."""
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)


# ============================================================
# 🔧 UTILITY FUNCTIONS
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


@st.cache_data(show_spinner=False, max_entries=50)
def load_image(url):
    """Optimized image loader — stream=True, unduh resolusi w1200."""
    file_id = get_drive_file_id(url)
    candidate_urls = []
    if file_id:
        candidate_urls.extend([
            f"https://drive.google.com/thumbnail?id={file_id}&sz=w1200",
            f"https://drive.google.com/uc?export=download&id={file_id}",
            f"https://drive.google.com/uc?export=view&id={file_id}",
        ])
    candidate_urls.append(url)

    headers = {"User-Agent": "Mozilla/5.0"}
    for candidate in dict.fromkeys(candidate_urls):
        try:
            response = requests.get(
                candidate, headers=headers, timeout=15,
                allow_redirects=True, stream=True,
            )
            response.raise_for_status()
            img_bytes = BytesIO(response.content)
            img = Image.open(img_bytes)
            img = ImageOps.exif_transpose(img).convert("RGB")
            img.load()
            response.close()
            img_bytes.close()
            return img
        except Exception:
            continue
    return None


@st.cache_data(show_spinner=False, max_entries=80)
def image_data_uri(url, max_dim=800, quality=80):
    """
    Convert to compressed base64.
    - Default (Buku Kating): 800px / q80 → hemat memori
    - HD (Home page):        max_dim=1200, quality=85 → tajam
    """
    img = load_image(url)
    if img is None:
        return None
    img = img.copy()
    if max(img.size) > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    return f"data:image/jpeg;base64,{encoded}"


def render_photo(img_src, alt="Foto"):
    if not img_src:
        st.markdown(
            """<div class="photo-wrapper" style="padding:0;">
<div style="width:100%;aspect-ratio:3/4;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#f4f0eb,#e6ddd1);border-radius:13px;color:#701c23;font-weight:600;">Foto tidak tersedia</div>
</div>""",
            unsafe_allow_html=True,
        )
        return
    st.markdown(
        f"""<div class="photo-wrapper">
<div class="photo-corner tl"></div>
<div class="photo-corner br"></div>
<img src="{img_src}" alt="{html_lib.escape(alt, quote=True)}">
</div>""",
        unsafe_allow_html=True,
    )


def render_profile_card(m):
    nama = html_lib.escape(str(m.get("nama", "-")))
    jabatan_raw = str(m.get("jabatan", "")).strip()
    jabatan = html_lib.escape(jabatan_raw) if jabatan_raw else "—"
    nim = html_lib.escape(str(m.get("nim", "-")))
    umur = html_lib.escape(str(m.get("umur", "-")))
    asal = html_lib.escape(str(m.get("asal", "-")))
    alamat = html_lib.escape(str(m.get("alamat", "-")))
    hobbi = html_lib.escape(str(m.get("hobbi", "-")))
    sosmed = html_lib.escape(str(m.get("sosmed", "-")))
    kesan = html_lib.escape(str(m.get("kesan", "-")))
    pesan = html_lib.escape(str(m.get("pesan", "-")))

    gold_keywords = ["ketua", "sekretaris", "senator", "kepala", "bendahara"]
    is_leader = any(k in jabatan_raw.lower() for k in gold_keywords)
    subheader_class = "profile-subheader leader" if is_leader else "profile-subheader"

    html_block = f"""<div class="profile-card">
<div class="profile-header">{nama}</div>
<div class="{subheader_class}">{jabatan}</div>
<div class="profile-divider"></div>
<div class="info-grid">
<div class="info-item"><span class="info-label">NIM</span><span class="info-value">{nim}</span></div>
<div class="info-item"><span class="info-label">Umur</span><span class="info-value">{umur} Tahun</span></div>
<div class="info-item"><span class="info-label">Asal</span><span class="info-value">{asal}</span></div>
<div class="info-item"><span class="info-label">Alamat</span><span class="info-value">{alamat}</span></div>
<div class="info-item full"><span class="info-label">Hobi</span><span class="info-value">{hobbi}</span></div>
<div class="info-item full"><span class="info-label">Sosial Media</span><span class="info-value">{sosmed}</span></div>
</div>
<div class="quote-box"><span class="quote-label">Kesan</span><div class="quote-text">{kesan}</div></div>
<div class="quote-box" style="margin-top:10px;"><span class="quote-label">Pesan</span><div class="quote-text">{pesan}</div></div>
</div>"""

    st.markdown(html_block, unsafe_allow_html=True)


# ============================================================
# 📸 DISPLAY WITH LAZY LOAD (LOAD MORE)
# ============================================================
def display_images_with_data(gambar_urls, data_list, batch_size=5, key="default"):
    """
    Menampilkan data dengan lazy load.
    - Awalnya tampil `batch_size` foto
    - Tombol "Muat Foto Lagi" untuk load batch berikutnya
    - Memori hanya dipakai untuk foto yang sedang tampil
    """
    total_items = min(len(gambar_urls), len(data_list))
    if total_items == 0:
        st.warning("Tidak ada data untuk ditampilkan.")
        return

    state_key = f"loaded_count_{key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = batch_size
    if st.session_state[state_key] > total_items:
        st.session_state[state_key] = total_items

    load_until = min(st.session_state[state_key], total_items)

    for i in range(load_until):
        with st.spinner(f"Memuat gambar {i+1} dari {total_items}..."):
            img_src = image_data_uri(gambar_urls[i])
        member = data_list[i]
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1:
            render_photo(img_src, alt=member.get("nama", "Foto"))
        with col2:
            render_profile_card(member)
        st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
        img_src = None  # free memory reference

    if load_until < total_items:
        remaining = total_items - load_until
        next_batch = min(batch_size, remaining)
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                f"📸 Muat {next_batch} Foto Lagi  ({load_until}/{total_items})",
                use_container_width=True,
                type="primary",
                key=f"loadmore_{key}",
            ):
                st.session_state[state_key] += batch_size
                st.rerun()
    else:
        st.success("Semua data berhasil dimuat! ✨")


# ============================================================
# 🧭 NAVBAR
# ============================================================
def streamlit_menu(default_index=0):
    return option_menu(
        menu_title=None,
        options=[
            "Kesekjenan", "Baleg", "Senator", "Departemen PSDA",
            "Departemen MIKFES", "Departemen Eksternal", "Departemen Internal",
            "Departemen SSD", "Departemen Medkraf",
        ],
        icons=["people-fill"] * 9,
        default_index=default_index,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "5px!important",
                "background-color": "rgba(255,255,255,0.85)",
                "backdrop-filter": "blur(12px)",
                "border-radius": "14px",
                "box-shadow": "0 8px 24px rgba(112,28,35,0.10), 0 1px 0 rgba(255,255,255,0.9) inset",
                "border": "1px solid rgba(217,195,163,0.6)",
                "margin-bottom": "30px",
            },
            "icon": {"color": "#701c23", "font-size": "15px"},
            "nav-link": {
                "font-size": "13px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "2px",
                "padding": "8px 12px",
                "border-radius": "8px",
                "color": "#701c23",
                "--hover-color": "rgba(217,195,163,0.25)",
                "transition": "all 0.3s ease",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #701c23 0%, #a8323d 100%)",
                "color": "#ffffff",
                "box-shadow": "0 4px 12px rgba(112,28,35,0.32)",
            },
        },
    )
