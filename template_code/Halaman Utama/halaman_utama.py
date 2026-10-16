import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


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
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE Markov</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2026</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_container_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;"> kami markov .</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/thumbnail?id=1z6A9ZPeZMH74isErBzSLxXSQbLMHTkRS&sz=w1000"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Buku Kating ini kami bangun dengan Python dan Streamlit, 
                    sekaligus menjadi ajang praktik dari materi yang kami pelajari selama kaderisasi. 
                    Prosesnya tentu tidak mulus karena ada bug yang bikin pusing
                    dan revisi yang datang bertubi-tubi. 
                    Tapi dari situ kami belajar bahwa kerja kelompok itu soal saling percaya dan saling mengisi. 
                    Semoga halaman-halaman ini bisa jadi pengingat untuk kami, 
                    dan jadi bacaan yang berguna untuk adik-adik angkatan berikutnya.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
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
        display_images_with_data(gambar_urls, data_list)

    about_page()
