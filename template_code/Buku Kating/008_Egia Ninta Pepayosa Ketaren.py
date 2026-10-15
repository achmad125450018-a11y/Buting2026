import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html as html_lib

# ============================================================
# 🎨 SUPER PREMIUM UI/UX — BUKU KATING EDITION
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
""", unsafe_allow_html=True)


st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)


# ============================================================
# UTIL FUNCTIONS
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
    img = img.copy()
    max_dim = 1200
    if max(img.size) > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=88, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


def get_cached_images(gambar_urls):
    out = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}..."):
            out.append(image_data_uri(url))
    return out


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

    # 🟡 Emas: ketua, sekretaris, senator, kepala, bendahara
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


def display_images_with_data(gambar_urls, data_list):
    images = get_cached_images(gambar_urls)
    for i, img_src in enumerate(images):
        if i < len(data_list):
            member = data_list[i]
            col1, col2 = st.columns([1, 2], gap="medium")
            with col1:
                render_photo(img_src, alt=member.get("nama", "Foto"))
            with col2:
                render_profile_card(member)
            st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
    st.success("Semua data berhasil dimuat!")


# ============================================================
# NAVBAR
# ============================================================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan", "Baleg", "Senator", "Departemen PSDA",
            "Departemen MIKFES", "Departemen Eksternal", "Departemen Internal",
            "Departemen SSD", "Departemen Medkraf",
        ],
        icons=["people-fill"] * 9,
        default_index=0,
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
    return selected


menu = streamlit_menu()


# ============================================================
# MENU CONTENT
# ============================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1OZ90dYQxs9qhwjS1IPjwAI8hPVZ3JZD-",
        "https://drive.google.com/uc?export=view&id=1PhDbGoXVKxccssC8wPlA61diRd4pNgf_",
        "https://drive.google.com/uc?export=view&id=1yuqzTRWDLty1-ujD5pVts539JmAU1ARo",
        "https://drive.google.com/uc?export=view&id=1OVtrdQ9DYO5r6LoJuapZb67S55IKmYXk",
        "https://drive.google.com/uc?export=view&id=1gPzMBXa36KLARfOs2jXYK4y_eozaEUbt",
        "https://drive.google.com/uc?export=view&id=1xXPJnwo_MRQhECTUKrncNcwc5vFvLvE6"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan suksek selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya sof spoken, lucuu", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk", "pesan": "Sukses selalu dan semangat kakkk!!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Baleg", "jabatan": "Ketua Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1bwy4U200wjwc6YN3tumWFDSW7LunNfmu",
        "https://drive.google.com/uc?export=view&id=1EJBPN6k5XmLVB8xtMNTgo2nWPEQFUkqv",
        "https://drive.google.com/uc?export=view&id=10s33vUvU34kLCr8nyL8rNZfM1k-Z1WCK",
        "https://drive.google.com/uc?export=view&id=1R77leJE5k8iATcKwvKFiw5nCmq-Ezl8C",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1PQpUNK5ZcmAVQ06WLxg8UlpHGsKoPlEC",
        "https://drive.google.com/uc?export=view&id=1_-uYsuZTVLXJ-RgwHKfzpR4r0otEN3Fx",
        "https://drive.google.com/uc?export=view&id=10IDI69GEY5BwBdxi6wm5L5im0UKDLoen",
        "https://drive.google.com/uc?export=view&id=1H77_72UrtmZXICgAMQHerezZ5vIYyYrp"
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Senator Mahasiswa", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Senator Mahasiswa", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Senator Mahasiswa", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Senator Mahasiswa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Senator Mahasiswa", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Senator Mahasiswa", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Senator Mahasiswa", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Senator Mahasiswa", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1s2XoLDNkmd79J8wzApnNqw9wA6lk1-cv",
        "https://drive.google.com/uc?export=view&id=1p8c54qe0t-KydPSN1_njmXyec4iIxPv1",
        "https://drive.google.com/uc?export=view&id=180LnphDPRRURP6I5_axl1o8-rMvM0a7v",
        "https://drive.google.com/uc?export=view&id=1OA-b0s0HelPi3sxZVwL8ClhvTZOd6RwS",
        "https://drive.google.com/uc?export=view&id=10bAdfxrD7ocCcavQarvNOlxpMMwvDIfu",
        "https://drive.google.com/uc?export=view&id=1LGW61YoaqD33BADwm6puWEK6OF5o23ZD",
        "https://drive.google.com/uc?export=view&id=1Wg_IKqKz65eAm9Go4sKAnbBnNVsBWr2J",
        "https://drive.google.com/uc?export=view&id=17gTme8LpUJXymPaVakbNlva-dI-9g-I_",
        "https://drive.google.com/uc?export=view&id=1tY19bSlTXLnJlwfmh06rgIiYNlL5MLUY",
        "https://drive.google.com/uc?export=view&id=1fxkhtAJEXXvdsLWEBLxAzJh__G8RMX0y",
        "https://drive.google.com/uc?export=view&id=1SbfGEpQvEF5JRJOr8eCiNm4fcHe6RL0Y",
        "https://drive.google.com/uc?export=view&id=1CXKxYtEPvKZ7-XB4IcGU8Lt6Meu31efF",
        "https://drive.google.com/uc?export=view&id=1iPjdXfvKW7s0ACiTHMRnV3AibnbNFM3c",
        "https://drive.google.com/uc?export=view&id=1Na9ZnS6uwX_Hq1qJVQuT7m_OeL9WPMJx",
        "https://drive.google.com/uc?export=view&id=1aphZKIhFSh1cXrDmGNNBFrW0168bQOup",
        "https://drive.google.com/uc?export=view&id=1gC-G8jGnV141twsV4142tLba2B0HlDgS",
        "https://drive.google.com/uc?export=view&id=1YU37XRd6LfGjBOCMDxhjje91ifITPXvB",
        "https://drive.google.com/uc?export=view&id=14-bA744kvqPIcYDN4fEYbDuH3SPMmaMd",
        "https://drive.google.com/uc?export=view&id=1rl91DQRXnOId12HESf4-i5g7sTtFaGX5",
        "https://drive.google.com/uc?export=view&id=1Z4-9A7vu0SoSH4V26iOOMWkWce1DiamW",
        "https://drive.google.com/uc?export=view&id=1y6G-InpEMk3i3L1lr8VIjuWy2HZoT7N6",
        "https://drive.google.com/uc?export=view&id=1BlMK8yUPvll8ifkluUTZu87WU-ycClyb"
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Staf Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Murah Senyum", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Nabyla Sharfina", "jabatan": "Staf Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Ramah", "pesan": "Selalu jadi orang baik"}
    ] + [{"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}] * 20
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1XMls4kh0QcWMIDiVzqaJX1kqhkOVWSzQ",
        "https://drive.google.com/uc?export=view&id=1EEZwTqaefUkPSoAnzgNig0A2nqn3zlaw",
        "https://drive.google.com/uc?export=view&id=1rU8FhlY3OoVrBAzlOyAaaxQ1MQhpmj0O",
        "https://drive.google.com/uc?export=view&id=1z91dbs7Sru4gLs8kP-ExLbWDQ7Ws6cD6",
        "https://drive.google.com/uc?export=view&id=1q_k2LJHBu9tsUNbtGJot6XAVoHGt0h7r",
        "https://drive.google.com/uc?export=view&id=1_Kf5fNwcsxG1oVEJvGDTZvdsGhHXFE0J",
        "https://drive.google.com/uc?export=view&id=1ry-WzKXg9EmgLjPwYH8BhXXe8gpokdjo",
        "https://drive.google.com/uc?export=view&id=18d4v1U8gLpdCA8VWmNIch_OpCwTOirNL",
        "https://drive.google.com/uc?export=view&id=1tzn97c-1KiRhIahSxkP4kSt5kGoe8crl",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=15-RA-Yz-i_9Cy6-LwFQxdN_1UKQ8Kyie",
        "https://drive.google.com/uc?export=view&id=1g2nAwUtylUht0-LAByTVUYJ0SrwFtd2o"
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf SSD", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1mG1H52wmXuIwBe4Ob1eyFupDnQLxWXCi",
        "https://drive.google.com/uc?export=view&id=1h8dcFbYl9P8Eo0xmIQtdHPjjXIrgkasq",
        "https://drive.google.com/uc?export=view&id=1niHLisifPanvllny_H371ChoPCDnZJf9",
        "https://drive.google.com/uc?export=view&id=1pdIVt6ZbCmfYMGMWa0wwrUbjhypQLC9F",
        "https://drive.google.com/uc?export=view&id=1d9ycgjc2PJqjmEt3bw7HorlX0Ma84Rek",
        "https://drive.google.com/uc?export=view&id=1EVU9KZqngak_sG_jW0roDyxBTXkHnAQy",
        "https://drive.google.com/uc?export=view&id=1XRFM0IuJEOLBHofYh5rbEL9OeeWHT4jB",
        "https://drive.google.com/uc?export=view&id=1Ne_GdGDiUeHu4cT4ameZpkjtNfVjcObi",
        "https://drive.google.com/uc?export=view&id=17t6Fk5wpCKhWHRJTijuKBHDeHf1hooFf",
        "https://drive.google.com/uc?export=view&id=1mttqVXQzEa-x3lDDn_Sm9pu3qK3qm-O2",
        "https://drive.google.com/uc?export=view&id=1zxtRxWrcSCuWE1n6UlYl-mVe7jLtEA5y",
        "https://drive.google.com/uc?export=view&id=14SuvEak83yiR3YdQfmtI7W_mSbxL5p9_",
        "https://drive.google.com/uc?export=view&id=1AwlD3RESR9TVy-mKCm3Sc4-U9JRuO8lQ",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1Vnhfi110gNpl3qKW-VfwdXjGjmg54aB6",
        "https://drive.google.com/uc?export=view&id=1MDkamNb-fcmJTpYtGqvCWs-l90BHVmQq",
        "https://drive.google.com/uc?export=view&id=1Pjv83uV75agH_7TtIForfU156O7W8jR9",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}
    ]
    display_images_with_data(gambar_urls, data_list)
