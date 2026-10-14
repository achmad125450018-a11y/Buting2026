import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================
st.set_page_config(
    page_title="Buku Kating HMSD",
    page_icon="💙",
    layout="wide"
)

# ==================================================
# CSS TEMA BIRU
# ==================================================
st.markdown("""
<style>
:root {
    --navy: #102b60;
    --blue: #1769e8;
    --light-blue: #eaf3ff;
    --text: #263957;
}

.stApp {
    background: linear-gradient(180deg, #f4f8ff, #ffffff 55%, #eef5ff);
    color: var(--text);
}

.block-container {
    max-width: 1200px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

.centered-title {
    text-align: center;
    color: var(--navy);
    font-size: 2.5rem;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #6680a8;
    font-size: 15px;
    margin-bottom: 28px;
}

.profile-card {
    background: linear-gradient(145deg, #ffffff, #f6f9ff);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #dfebff;
    border-left: 5px solid var(--blue);
    box-shadow: 0 8px 25px rgba(23, 72, 145, 0.08);
    margin: 5px 0 18px 0;
    overflow-wrap: anywhere;
}

.profile-header {
    font-size: 21px;
    font-weight: 800;
    color: var(--navy);
    margin-bottom: 14px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e5efff;
}

.profile-card p {
    color: #435674;
    font-size: 14px;
    line-height: 1.8;
    margin: 7px 0;
}

.info-label {
    font-weight: 750;
    color: var(--navy);
}

div[data-testid="stImage"] img {
    border-radius: 20px;
    border: 3px solid white;
    box-shadow: 0 8px 24px rgba(20, 61, 120, 0.14);
    object-fit: cover;
}

hr {
    border-color: #dce9fc !important;
    margin: 25px 0 !important;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #102b60, #1769e8) !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.8rem 2rem;
    }

    .centered-title {
        font-size: 1.8rem;
    }

    .profile-card {
        padding: 17px;
        border-radius: 16px;
    }

    .profile-header {
        font-size: 18px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 class='centered-title'>BUKU KATING</h1>"
    "<p class='subtitle'>Kenali lebih dekat keluarga besar HMSD</p>",
    unsafe_allow_html=True
)

# ==================================================
# MENU NAVIGASI
# ==================================================
def streamlit_menu():
    return option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
        ],
        icons=["people-fill"] * 9,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "8px",
                "background-color": "#ffffff",
                "border-radius": "18px",
                "box-shadow": "0 5px 20px rgba(16,43,96,0.09)",
                "border": "1px solid #e0ebff",
            },
            "icon": {
                "color": "#1769e8",
                "font-size": "16px",
            },
            "nav-link": {
                "font-size": "12px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "3px",
                "padding": "11px 10px",
                "border-radius": "12px",
                "color": "#263957",
                "--hover-color": "#eaf3ff",
            },
            "nav-link-selected": {
                "background-color": "#1769e8",
                "color": "#ffffff",
                "font-weight": "700",
            },
        },
    )

# ==================================================
# FUNGSI MEMUAT GAMBAR
# ==================================================
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return None

        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img = img.resize((300, 400))
        return img
    except Exception:
        return None


def get_cached_images(gambar_urls):
    images = []

    for i, url in enumerate(gambar_urls):
        with st.spinner(
            f"Memuat gambar {i + 1} dari {len(gambar_urls)}"
        ):
            images.append(load_image(url))

    return images


# ==================================================
# FUNGSI MENAMPILKAN PROFIL
# ==================================================
def display_images_with_data(gambar_urls, data_list):
    images = get_cached_images(gambar_urls)

    for i, img in enumerate(images):
        if i >= len(data_list):
            break

        data = data_list[i]

        st.markdown(
            f"""
            <div style="
                background:linear-gradient(120deg,#eaf3ff,#ffffff);
                padding:12px 18px;
                border-radius:14px;
                margin:12px 0 15px;
                border:1px solid #dfebff;
                color:#1769e8;
                font-size:13px;
                font-weight:700;
                letter-spacing:1px;">
                ANGGOTA {i + 1:02d}
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([1, 2], gap="large")

        with col1:
            if img is not None:
                st.image(img, use_container_width=True)
            else:
                st.warning("Gagal memuat gambar.")

        with col2:
            st.markdown(
                f"""
                <div class='profile-card'>
                    <div class='profile-header'>
                        {data['nama']}
                    </div>
                    <p><span class='info-label'>NIM:</span> {data['nim']}</p>
                    <p><span class='info-label'>Umur:</span> {data['umur']} Tahun</p>
                    <p><span class='info-label'>Asal:</span> {data['asal']}</p>
                    <p><span class='info-label'>Alamat:</span> {data['alamat']}</p>
                    <p><span class='info-label'>Hobbi:</span> {data['hobbi']}</p>
                    <p><span class='info-label'>Sosial Media:</span> {data['sosmed']}</p>
                    <p><span class='info-label'>Kesan:</span> {data['kesan']}</p>
                    <p><span class='info-label'>Pesan:</span> {data['pesan']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

    st.success("Semua data berhasil dimuat!")


# ==================================================
# PILIH MENU
# ==================================================
menu = streamlit_menu()


# ==================================================
# KESEKJENAN
# ==================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q"
    ]

    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan sukses selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# BALEG
# ==================================================
elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q"
    ]

    data_list = [
        {"nama": "Anggota Baleg", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# SENATOR
# ==================================================
elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q"
    ]

    data_list = [
        {"nama": "Fathinah Nur Azizah", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN PSDA
# ==================================================
elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]

    data_list = [
        {"nama": "Anggota PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN MIKFES
# ==================================================
elif menu == "Departemen MIKFES":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]

    data_list = [
        {"nama": "Anggota MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN EKSTERNAL
# ==================================================
elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q",
        "https://drive.google.com/uc?export=view&id=10D1nknaRhz28mkquGqZ-Kb_Ki7CHNO0Q"
    ]

    data_list = [
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}
        for _ in gambar_urls
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN INTERNAL
# ==================================================
elif menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]

    data_list = [
        {"nama": "Anggota Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"}
    ]

    display_images_with_data(gambar_urls, data_list)
