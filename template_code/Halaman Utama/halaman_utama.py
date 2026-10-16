import base64
import html
import random
import pandas as pd
import streamlit as st
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.set_page_config(
    page_title="Markov | HMSD Adyatama ITERA 2026",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded",
)


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"Sebagai: {data_list[i]['Sebagai']}")
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Fun Fact: {data_list[i]['Fun Fact']}")
            st.write(f"Motto Hidup: {data_list[i]['Motto Hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@400;600;700&display=swap');
    :root {
        --sage: #A8C3A0;
        --olive: #6B8F5E;
        --moss: #4F6B45;
        --cream: #FBF8F0;
        --clay: #C08552;
        --bark: #4A3F35;
    }
    .stApp {
        background: linear-gradient(160deg, #DCE8D2 0%, #E9F0DE 50%, #F1F2E3 100%);
        background-attachment: fixed;
        color: var(--bark);
        font-family: 'Nunito', sans-serif;
    }
    #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {visibility: hidden;}
    header {background: transparent !important;}
    [data-testid="stSidebarNav"], [data-testid="stSidebarNavItems"] {display: none;}
    .block-container {padding-top: 2rem; padding-bottom: 4rem; max-width: 960px;}
    h1, h2, h3 {font-family: 'Fredoka', sans-serif; color: var(--moss);}
    @keyframes rise {from {opacity: 0; transform: translateY(24px);} to {opacity: 1; transform: translateY(0);}}
    @keyframes sway {0%, 100% {transform: rotate(-6deg);} 50% {transform: rotate(6deg);}}
    .hero {text-align: center; margin-bottom: 1.5rem; animation: rise 0.9s ease both;}
    .hero .leaf {display: inline-block; font-size: 2.6rem; animation: sway 3s ease-in-out infinite; transform-origin: bottom center;}
    .hero h1 {
        font-size: clamp(2.5rem, 8vw, 5rem);
        font-weight: 700;
        line-height: 1.1;
        margin: 0;
        background: linear-gradient(90deg, #4F6B45, #C08552);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p {
        font-family: 'Fredoka', sans-serif;
        font-size: clamp(1rem, 3vw, 1.5rem);
        color: var(--olive);
        margin-top: 0.4rem;
        letter-spacing: 0.08em;
    }
    .centered-title {text-align: center; margin: 1.5rem 0 1rem; animation: rise 0.7s ease both;}
    .panel {
        background: var(--cream);
        border-radius: 22px;
        padding: 1.4rem 1.6rem;
        box-shadow: 0 8px 22px rgba(79, 107, 69, 0.15);
        border: 1px solid rgba(107, 143, 94, 0.25);
        text-align: justify;
        line-height: 1.75;
        animation: rise 0.8s ease both;
    }
    .stat {
        background: var(--cream);
        border-radius: 20px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 6px 16px rgba(79, 107, 69, 0.12);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        animation: rise 0.9s ease both;
    }
    .stat:hover {transform: translateY(-6px) rotate(-1deg); box-shadow: 0 14px 26px rgba(79, 107, 69, 0.22);}
    .stat b {display: block; font-family: 'Fredoka', sans-serif; font-size: 2rem; color: var(--clay);}
    .stat span {font-size: 0.9rem; color: var(--moss);}
    div[data-testid="stImage"] img {
        border-radius: 20px;
        box-shadow: 0 8px 22px rgba(74, 63, 53, 0.18);
        transition: transform 0.35s ease;
    }
    div[data-testid="stImage"] img:hover {transform: scale(1.03);}
    .fact {background: #EFE6D2; border-left: 6px solid var(--clay); border-radius: 14px; padding: 1rem 1.2rem; margin-top: 1rem; animation: rise 0.6s ease both;}
    div.stButton > button {
        background: var(--olive); color: white; border: none; border-radius: 999px;
        padding: 0.6rem 1.6rem; font-family: 'Fredoka', sans-serif; font-size: 1rem;
        transition: transform 0.2s ease, background 0.2s ease;
    }
    div.stButton > button:hover {background: var(--clay); color: white; transform: scale(1.06) rotate(-1deg);}
    div[data-testid="stTextInput"] input {border-radius: 999px;}

    section[data-testid="stSidebar"] {background: #D3E3C8; border-right: 1px solid rgba(107, 143, 94, 0.25);}
    section[data-testid="stSidebar"] div[data-testid="stExpander"] {
        background: transparent; border: none; box-shadow: none; margin-bottom: 0.4rem;
    }
    section[data-testid="stSidebar"] div[data-testid="stExpander"] summary {
        font-family: 'Fredoka', sans-serif; font-size: 1.05rem; font-weight: 600; color: var(--moss);
        border-radius: 12px; padding: 0.5rem 0.6rem;
    }
    section[data-testid="stSidebar"] div[data-testid="stExpander"] summary:hover {background: rgba(255, 255, 255, 0.45);}
    section[data-testid="stSidebar"] div.stButton > button {
        background: transparent; color: var(--bark); border-radius: 12px; width: 100%;
        justify-content: flex-start; text-align: left; padding: 0.4rem 0.8rem;
        font-family: 'Nunito', sans-serif; font-size: 0.92rem; font-weight: 600;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background: rgba(255, 255, 255, 0.6); color: var(--moss); transform: translateX(4px);
    }
    section[data-testid="stSidebar"] div.stButton > button[kind="primary"],
    section[data-testid="stSidebar"] div.stButton > button[data-testid="stBaseButton-primary"] {
        background: #BFD5B1; color: #2F4228; font-weight: 700;
    }

    .grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 1.6rem; margin-top: 1rem;}
    .flip {perspective: 1100px; aspect-ratio: 3 / 4; outline: none; cursor: pointer; animation: rise 0.7s ease both;}
    .flip-inner {
        position: relative; width: 100%; height: 100%;
        transition: transform 0.8s cubic-bezier(0.4, 0.2, 0.2, 1);
        transform-style: preserve-3d;
    }
    .flip:hover .flip-inner, .flip:focus .flip-inner {transform: rotateY(180deg);}
    .face {
        position: absolute; inset: 0;
        backface-visibility: hidden; -webkit-backface-visibility: hidden;
        border-radius: 22px; overflow: hidden;
        box-shadow: 0 10px 24px rgba(79, 107, 69, 0.22);
        border: 1px solid rgba(107, 143, 94, 0.3);
    }
    .front img {width: 100%; height: 100%; object-fit: cover; display: block;}
    .cap {
        position: absolute; left: 0; right: 0; bottom: 0;
        padding: 2.6rem 0.8rem 0.9rem;
        background: linear-gradient(transparent, rgba(47, 66, 40, 0.88));
        text-align: center;
    }
    .cap .name {color: #fff; font-size: 1.05rem; margin: 0;}
    .back {
        transform: rotateY(180deg);
        background: linear-gradient(160deg, #FBF8F0, #E3EDD9);
        padding: 1rem; display: flex; flex-direction: column; justify-content: center;
        text-align: center; gap: 0.5rem;
    }
    .back .bname {font-family: 'Fredoka', sans-serif; font-size: 1.1rem; font-weight: 600; color: var(--moss);}
    .back .row {font-size: 0.85rem; line-height: 1.4;}
    .back .row b {display: block; color: var(--clay); font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase;}
    .name {font-family: 'Fredoka', sans-serif; font-size: 1.15rem; font-weight: 600; text-align: center; color: var(--moss);}
    .badge {
        display: block; width: fit-content; margin: 0.3rem auto 0;
        background: var(--sage); color: #2F4228; padding: 2px 14px; border-radius: 999px;
        font-size: 0.78rem; font-weight: 700;
    }
    .badge.lead {background: var(--clay); color: white;}
    .detail {text-align: left;}
    .detail h2 {margin: 0 0 0.3rem; font-size: 1.8rem;}
    .detail .badge {margin: 0 0 1.2rem;}
    .detail .row {margin-bottom: 1rem; font-size: 1.02rem;}
    .detail .row b {display: block; color: var(--clay); font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase;}
    .chain {display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; margin-top: 1rem;}
    .chain span {background: var(--cream); border: 2px solid var(--olive); border-radius: 999px; padding: 4px 14px; font-weight: 700; color: var(--moss);}
    .chain i {color: var(--clay); font-style: normal;}

    .intro {
        position: fixed; inset: 0; z-index: 99999; pointer-events: none;
        display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1.6rem;
        background: linear-gradient(160deg, #DCE8D2, #F1F2E3);
        animation: introOut 0.8s ease 4.2s forwards;
    }
    @keyframes introOut {to {opacity: 0; visibility: hidden;}}
    .intro h2 {font-family: 'Fredoka', sans-serif; color: var(--moss); margin: 0; text-align: center; font-size: clamp(1.1rem, 4vw, 1.7rem);}
    .intro small {color: var(--olive); font-family: 'Fredoka', sans-serif; letter-spacing: 0.05em;}
    .track {position: relative; width: min(340px, 78vw); height: 64px; margin: 0 28px;}
    .track::before {
        content: ""; position: absolute; left: 0; right: 0; top: 50%; height: 3px;
        background: repeating-linear-gradient(90deg, var(--sage) 0 10px, transparent 10px 18px);
    }
    .node {
        position: absolute; top: 4px; width: 56px; height: 56px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 1.1rem;
        border: 3px solid var(--olive); background: var(--cream); color: var(--moss);
        transform: translateX(-50%);
    }
    .node:nth-child(1) {left: 0%; animation: g1 4s ease both;}
    .node:nth-child(2) {left: 33.33%; animation: g2 4s ease both;}
    .node:nth-child(3) {left: 66.66%; animation: g3 4s ease both;}
    .node:nth-child(4) {left: 100%; animation: g4 4s ease both;}
    @keyframes g1 {0%, 15% {background: var(--clay); color: #fff; transform: translateX(-50%) scale(1.18);} 18%, 100% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);}}
    @keyframes g2 {0%, 28% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);} 30%, 42% {background: var(--clay); color: #fff; transform: translateX(-50%) scale(1.18);} 46%, 58% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);} 60%, 72% {background: var(--clay); color: #fff; transform: translateX(-50%) scale(1.18);} 76%, 100% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);}}
    @keyframes g3 {0%, 43% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);} 45%, 56% {background: var(--clay); color: #fff; transform: translateX(-50%) scale(1.18);} 60%, 90% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);} 92%, 100% {background: var(--clay); color: #fff; transform: translateX(-50%) scale(1.18);}}
    @keyframes g4 {0%, 76% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);} 78%, 90% {background: var(--clay); color: #fff; transform: translateX(-50%) scale(1.18);} 94%, 100% {background: var(--cream); color: var(--moss); transform: translateX(-50%) scale(1);}}
    .token {
        position: absolute; top: -14px; width: 18px; height: 18px; border-radius: 50%;
        background: var(--bark); box-shadow: 0 0 0 5px rgba(192, 133, 82, 0.35);
        transform: translateX(-50%); animation: hop 4s ease-in-out both;
    }
    @keyframes hop {0%, 15% {left: 0%;} 30% {left: 33.33%;} 45% {left: 66.66%;} 60% {left: 33.33%;} 78% {left: 100%;} 92%, 100% {left: 66.66%;}}
    .probs {display: flex; gap: 1.4rem; font-family: 'Fredoka', sans-serif; color: var(--clay); font-size: 0.95rem;}
    </style>
    <div class='hero'>
        <div class='leaf'>🌿</div>
        <h1>WEBSITE Markov</h1>
        <p>CEO HMSD Adyatama ITERA 2026</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if "welcomed" not in st.session_state:
    st.session_state.welcomed = True
    st.markdown(
        "<div class='intro'>"
        "<h2>Menyusun rantai Markov…</h2>"
        "<div class='track'>"
        "<div class='node'>S₁</div><div class='node'>S₂</div><div class='node'>S₃</div><div class='node'>S₄</div>"
        "<div class='token'></div>"
        "</div>"
        "<div class='probs'><span>P₁₂ = 0.6</span><span>P₂₃ = 0.5</span><span>P₃₄ = 0.4</span></div>"
        "<small>P(Xₙ₊₁ | Xₙ) — masa depan hanya bergantung pada saat ini</small>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.toast("Selamat datang di rumah Markov! 🌱", icon="🌿")

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"

gambar_urls = [
    "https://drive.google.com/thumbnail?id=1JGQ4NK_upmvgOqJ6IpantoN2SnzZ3ZQ_&sz=w1000",
    "https://drive.google.com/thumbnail?id=1HZhtm4RD96J_O21uJLXBUk7TTemcG6v9&sz=w1000",
    "https://drive.google.com/thumbnail?id=1YVBdp8vzuXgOMlt1b5SlXwa67Tf4TXRn&sz=w1000",
    "https://drive.google.com/thumbnail?id=1pKi94p09JWRiayOgokLtjifajYilw_o8&sz=w1000",
    "https://drive.google.com/thumbnail?id=1QFBWVdXebtKoJrjItPqAp7QNUyeoTYh3&sz=w1000",
    "https://drive.google.com/thumbnail?id=1FLzTI71N8nbmtGGQ_rRJivFZlJw-ebQI&sz=w1000",
    "https://drive.google.com/thumbnail?id=1-d68goJ0TtR-P4ll1ufSSWn0i4d3yGqn&sz=w1000",
    "https://drive.google.com/thumbnail?id=1IDNTMgmb5hFh9pXRF5QNNhWRB3RB93QV&sz=w1000",
    "https://drive.google.com/thumbnail?id=1toZ-1n0v0nDd_TdJnRjLFJu1B0ALqpb8&sz=w1000",
    "https://drive.google.com/thumbnail?id=189a_DCmlDs-edf1OoDQajifrRWjlbvCA&sz=w1000",
    "https://drive.google.com/thumbnail?id=1yApVmRlFoPOocKIZdpilS9z3Wb_T7GtW&sz=w1000",
    "https://drive.google.com/thumbnail?id=1UhwT9Vvvv6w_hYcPVYbEnCdqrELLiKJt&sz=w1000",
]

data_list = [
    {
        "Nama": "Sapta Daffa Mulya",
        "Sebagai": "Pak Lurah",
        "NIM": "125450056",
        "Fun Fact": "Nama saya sesuai tanggal lahir",
        "Motto Hidup": "Enjoy the flow",
    },
    {
        "Nama": "Ade Putri Kurnia Pratiwi",
        "Sebagai": "Bu Lurah",
        "NIM": "125450073",
        "Fun Fact": "Suka nyapa satpam ITERA sambil teriak",
        "Motto Hidup": "Boleh ngeluh asal jangan nyerah",
    },
    {
        "Nama": "Indah Lestari",
        "Sebagai": "Anggota",
        "NIM": "125450007",
        "Fun Fact": "Gabisa bonceng orang tapi bisa bawa motor",
        "Motto Hidup": "Hari ini berjuang, hari esok kita ber-uang",
    },
    {
        "Nama": "Sakinah Farhana Alqitsi",
        "Sebagai": "Anggota",
        "NIM": "125450016",
        "Fun Fact": "Suka makan pecel",
        "Motto Hidup": "Tetap semangat",
    },
    {
        "Nama": "Muhammad Helmi Fahma",
        "Sebagai": "Anggota",
        "NIM": "125450023",
        "Fun Fact": "Selain manis aku juga humoris",
        "Motto Hidup": "Jalani saja",
    },
    {
        "Nama": "Armeyza Varian",
        "Sebagai": "Anggota",
        "NIM": "125450024",
        "Fun Fact": "Suka ngerjain tugas pas deket deadline",
        "Motto Hidup": "Tetap tersenyum",
    },
    {
        "Nama": "Lian Ilham Nurthoriq",
        "Sebagai": "Pelengkap Markov",
        "NIM": "125450025",
        "Fun Fact": "Suka yang manis, padahal aku udah manis",
        "Motto Hidup": "Belajar untuk hari ini, hidup untuk besok",
    },
    {
        "Nama": "Nisa Aura",
        "Sebagai": "Anggota",
        "NIM": "125450032",
        "Fun Fact": "Gasuka makan kecap",
        "Motto Hidup": "Tetap jalanin walaupun sambil ngeluh",
    },
    {
        "Nama": "Diah Ayu Puspita Sastra",
        "Sebagai": "Anggota",
        "NIM": "125450039",
        "Fun Fact": "Excited sama hal-hal baru",
        "Motto Hidup": "Sebaik-baiknya manusia adalah mereka yang bermanfaat bagi sesamanya",
    },
    {
        "Nama": "Maryam Zahra Rahmadani",
        "Sebagai": "Anggota",
        "NIM": "125450090",
        "Fun Fact": "Makan sei Indonesia tiap hari",
        "Motto Hidup": "Orang lain boleh gila, asal bukan saya",
    },
    {
        "Nama": "Lidya Tirza Hanum",
        "Sebagai": "Anggota",
        "NIM": "125450096",
        "Fun Fact": "Suka menghayal",
        "Motto Hidup": "Tetap percaya pada diri sendiri, bukan dengan orang lain",
    },
    {
        "Nama": "Fadel Hilal Askari",
        "Sebagai": "Anggota",
        "NIM": "125450099",
        "Fun Fact": "Gasuka minyak kayu putih",
        "Motto Hidup": "Sukses berawal dari mimpi. Karena itu, kita perbanyak tidur",
    },
]

members = sorted(zip(gambar_urls, data_list), key=lambda x: x[1]["NIM"])

STATES = ["Cerah", "Berawan", "Hujan"]
MATRIX = [[0.6, 0.3, 0.1], [0.3, 0.4, 0.3], [0.2, 0.4, 0.4]]

if "page" not in st.session_state:
    st.session_state.page = "home"


def go(page):
    st.session_state.page = page


def nav(label, page):
    st.button(
        label,
        key=f"nav_{page}",
        on_click=go,
        args=(page,),
        type="primary" if st.session_state.page == page else "secondary",
        use_container_width=True,
    )


def layout(url):
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.image(load_image(url), use_container_width=True)


@st.cache_data
def to_data_uri(url):
    img = load_image(url).convert("RGB")
    img = ImageOps.fit(img, (480, 640), centering=(0.5, 0.25))
    buf = BytesIO()
    img.save(buf, "JPEG", quality=85)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def flip_card(url, d):
    e = {k: html.escape(v) for k, v in d.items()}
    css = "badge lead" if d["Sebagai"] in ("Pak Lurah", "Bu Lurah") else "badge"
    return (
        "<div class='flip' tabindex='0'><div class='flip-inner'>"
        f"<div class='face front'><img src='{to_data_uri(url)}'>"
        f"<div class='cap'><div class='name'>{e['Nama']}</div><span class='{css}'>{e['Sebagai']}</span></div></div>"
        "<div class='face back'>"
        f"<div class='bname'>{e['Nama']}</div>"
        f"<span class='{css}'>{e['Sebagai']}</span>"
        f"<div class='row'><b>NIM</b>{e['NIM']}</div>"
        f"<div class='row'><b>Fun Fact</b>{e['Fun Fact']}</div>"
        f"<div class='row'><b>Motto Hidup</b>“{e['Motto Hidup']}”</div>"
        "</div></div></div>"
    )


def sidebar_menu():
    with st.sidebar:
        with st.expander("🏠 Halaman Utama", expanded=True):
            nav("Markov", "home")
            nav("About Us", "about")
        with st.expander("📖 Buku Kating", expanded=True):
            for i, (_, d) in enumerate(members):
                nav(f"{d['NIM'][-3:]} - {d['Nama']}", f"m{i}")
        with st.expander("🎲 Try Me !!", expanded=True):
            nav("KREASI", "kreasi")
            nav("KREASII", "kreasii")


def home_page():
    layout(url)
    layout(url1)
    st.markdown("<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True)
    st.markdown(
        """<div class="panel">Kami Markov, dua belas mahasiswa HMSD Adyatama ITERA 2026.
        Seperti rantai Markov, setiap langkah kami dipengaruhi langkah sebelumnya:
        saling bergantung, saling menguatkan, dan terus bergerak maju bersama.</div>""",
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='stat'><b>12</b><span>Anggota</span></div>", unsafe_allow_html=True)
    c2.markdown("<div class='stat'><b>1</b><span>Rantai yang Kuat</span></div>", unsafe_allow_html=True)
    c3.markdown("<div class='stat'><b>∞</b><span>Semangat</span></div>", unsafe_allow_html=True)
    st.write("")
    layout("https://drive.google.com/thumbnail?id=1z6A9ZPeZMH74isErBzSLxXSQbLMHTkRS&sz=w1000")
    st.markdown(
        """<div class="panel">Buku Kating ini kami bangun dengan Python dan Streamlit,
        sekaligus menjadi ajang praktik dari materi yang kami pelajari selama kaderisasi.
        Prosesnya tentu tidak mulus karena ada bug yang bikin pusing
        dan revisi yang datang bertubi-tubi.
        Tapi dari situ kami belajar bahwa kerja kelompok itu soal saling percaya dan saling mengisi.
        Semoga halaman-halaman ini bisa jadi pengingat untuk kami,
        dan jadi bacaan yang berguna untuk adik-adik angkatan berikutnya.</div>""",
        unsafe_allow_html=True,
    )


def about_page():
    st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
    search = st.text_input("Cari anggota", placeholder="🔍 Ketik nama atau NIM...")
    role = st.radio(
        "Peran",
        ["Semua", "Pak Lurah", "Bu Lurah", "Anggota", "Pelengkap Markov"],
        horizontal=True,
        label_visibility="collapsed",
    )
    items = [
        (u, d)
        for u, d in zip(gambar_urls, data_list)
        if (role == "Semua" or d["Sebagai"] == role)
        and (search.lower() in d["Nama"].lower() or search in d["NIM"])
    ]
    if not items:
        st.info("Belum ada anggota yang cocok, coba kata kunci lain 🌾")
        return
    st.markdown(
        "<div class='grid'>" + "".join(flip_card(u, d) for u, d in items) + "</div>",
        unsafe_allow_html=True,
    )


def member_page(i):
    u, d = members[i]
    e = {k: html.escape(v) for k, v in d.items()}
    css = "badge lead" if d["Sebagai"] in ("Pak Lurah", "Bu Lurah") else "badge"
    left, right = st.columns([1, 1.3], gap="large")
    with left:
        st.markdown(flip_card(u, d), unsafe_allow_html=True)
    with right:
        st.markdown(
            f"<div class='panel detail'><h2>{e['Nama']}</h2><span class='{css}'>{e['Sebagai']}</span>"
            f"<div class='row'><b>NIM</b>{e['NIM']}</div>"
            f"<div class='row'><b>Fun Fact</b>{e['Fun Fact']}</div>"
            f"<div class='row'><b>Motto Hidup</b>“{e['Motto Hidup']}”</div></div>",
            unsafe_allow_html=True,
        )


def kreasi_page():
    st.markdown("<h1 class='centered-title'>KREASI</h1>", unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        if st.button("🎲 Ambil Fun Fact Acak", use_container_width=True):
            st.session_state.pick = random.randrange(len(data_list))
            st.balloons()
    if "pick" in st.session_state:
        d = data_list[st.session_state.pick]
        st.markdown(
            f"<div class='fact'><b>{d['Nama']}</b> ({d['Sebagai']})<br>{d['Fun Fact']}<br><i>“{d['Motto Hidup']}”</i></div>",
            unsafe_allow_html=True,
        )


def kreasii_page():
    st.markdown("<h1 class='centered-title'>KREASII</h1>", unsafe_allow_html=True)
    if "chain" not in st.session_state:
        st.session_state.chain = [0]
    st.markdown(
        "<div class='panel'>Simulasi rantai Markov: cuaca besok hanya bergantung pada cuaca hari ini.</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.dataframe(pd.DataFrame(MATRIX, index=STATES, columns=STATES), use_container_width=True)
    a, b = st.columns(2)
    if a.button("➡️ Langkah berikutnya", use_container_width=True):
        now = st.session_state.chain[-1]
        st.session_state.chain.append(random.choices(range(3), weights=MATRIX[now])[0])
    if b.button("🔄 Ulangi", use_container_width=True):
        st.session_state.chain = [0]
        st.rerun()
    chain = "<i>→</i>".join(f"<span>{STATES[s]}</span>" for s in st.session_state.chain)
    st.markdown(f"<div class='chain'>{chain}</div>", unsafe_allow_html=True)


sidebar_menu()

page = st.session_state.page
if page == "home":
    home_page()
elif page == "about":
    about_page()
elif page == "kreasi":
    kreasi_page()
elif page == "kreasii":
    kreasii_page()
else:
    member_page(int(page[1:]))