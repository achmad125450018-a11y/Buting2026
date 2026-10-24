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
# CSS TEMA MODERN DUAL-TONE BLUE
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

:root {
    --navy-bg: #113685;
    --navy-card: #1545a9;
    --navy-border: #2458c8;
    --light-blue: #a3c4f3;
    --text-white: #ffffff;
    --text-dim: #cad8f2;
}

.stApp {
    background: #0d214d;
    color: var(--text-white);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.centered-title {
    text-align: center;
    color: #ffffff;
    font-size: 2.8rem;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 5px;
    text-transform: uppercase;
}

.subtitle {
    text-align: center;
    color: var(--light-blue);
    font-size: 15px;
    margin-bottom: 30px;
}

/* CONTAINER PROFIL UTAMA */
.profile-card-container {
    display: flex;
    background: linear-gradient(135deg, #133f99, #0d2c70);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    border: 1px solid var(--navy-border);
    margin-bottom: 35px;
}

/* SISI KIRI (FOTO CUTOUT / PUTIH) */
.profile-photo-section {
    flex: 1;
    min-width: 280px;
    max-width: 380px;
    background-color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    position: relative;
}

.profile-photo-section img {
    width: 100%;
    height: 100%;
    max-height: 420px;
    object-fit: cover;
    border-radius: 12px;
}

/* SISI KANAN (DESAIN KARTU BIRU) */
.profile-info-section {
    flex: 1.8;
    padding: 35px 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.profile-main-name {
    font-size: 3rem;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 25px;
}

/* DUA KOLOM DENGAN GARIS PEMBATAS TIPIS */
.profile-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 20px;
}

.info-group {
    margin-bottom: 15px;
}

.info-label {
    font-size: 11px;
    text-transform: uppercase;
    color: var(--light-blue);
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 3px;
}

.info-value {
    font-size: 14px;
    color: #ffffff;
    font-weight: 600;
    line-height: 1.5;
}

hr {
    border-color: rgba(255, 255, 255, 0.1) !important;
    margin: 35px 0 !important;
}

[data-testid="stSidebar"] {
    background: #0a1838 !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

@media (max-width: 768px) {
    .profile-card-container {
        flex-direction: column;
    }
    .profile-photo-section {
        max-width: 100%;
        height: 350px;
    }
    .profile-info-section {
        padding: 25px 20px;
    }
    .profile-main-name {
        font-size: 2.2rem;
    }
    .profile-grid {
        grid-template-columns: 1fr;
        gap: 15px;
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
            "Departemen Minbak",
        ],
        icons=["people-fill"] * 10,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "8px",
                "background-color": "#0a1838",
                "border-radius": "18px",
                "box-shadow": "0 5px 20px rgba(0,0,0,0.3)",
                "border": "1px solid #1f3e82",
            },
            "icon": {
                "color": "#a3c4f3",
                "font-size": "16px",
            },
            "nav-link": {
                "font-size": "12px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "3px",
                "padding": "11px 10px",
                "border-radius": "12px",
                "color": "#cad8f2",
                "--hover-color": "#15357a",
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
        return img
    except Exception:
        return None


def get_cached_images(gambar_urls):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            images.append(load_image(url))
    return images


# ==================================================
# FUNGSI MENAMPILKAN PROFIL (TAMPILAN BLUE CARD GRID)
# ==================================================
def display_images_with_data(gambar_urls, data_list):
    images = get_cached_images(gambar_urls)

    for i, img in enumerate(images):
        if i >= len(data_list):
            break

        data = data_list[i]

        img_html = ""
        if img is not None:
            buffered = BytesIO()
            img.save(buffered, format="JPEG")
            import base64
            img_b64 = base64.b64encode(buffered.getvalue()).decode()
            img_html = f"<img src='data:image/jpeg;base64,{img_b64}' alt='Foto Profil' />"
        else:
            img_html = "<div style='color:#102b60; font-weight:bold;'>Gambar tidak tersedia</div>"

        # HTML KARTU BIRU MODERN
        card_html = f"""
        <div class='profile-card-container'>
            <div class='profile-photo-section'>
                {img_html}
            </div>
            <div class='profile-info-section'>
                <div class='profile-main-name'>{data['nama']}</div>
                
                <div class='profile-grid'>
                    <div>
                        <div class='info-group'>
                            <div class='info-label'>NIM</div>
                            <div class='info-value'>{data['nim']}</div>
                        </div>
                        <div class='info-group'>
                            <div class='info-label'>Umur</div>
                            <div class='info-value'>{data['umur']} Tahun</div>
                        </div>
                        <div class='info-group'>
                            <div class='info-label'>Asal</div>
                            <div class='info-value'>{data['asal']}</div>
                        </div>
                        <div class='info-group'>
                            <div class='info-label'>Alamat</div>
                            <div class='info-value'>{data['alamat']}</div>
                        </div>
                    </div>
                    <div>
                        <div class='info-group'>
                            <div class='info-label'>Hobbi</div>
                            <div class='info-value'>{data['hobbi']}</div>
                        </div>
                        <div class='info-group'>
                            <div class='info-label'>Sosial Media</div>
                            <div class='info-value'>{data['sosmed']}</div>
                        </div>
                        <div class='info-group'>
                            <div class='info-label'>Kesan</div>
                            <div class='info-value'>{data['kesan']}</div>
                        </div>
                        <div class='info-group'>
                            <div class='info-label'>Pesan</div>
                            <div class='info-value'>{data['pesan']}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
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
        "https://drive.google.com/uc?export=view&id=1jCOveFLfhMxHNvSoBp6Ij6EIyrGcneiG",
        "https://drive.google.com/uc?export=view&id=12-VrSY-nKmYGIYzVTzGtNEQq2xOsdPdT",
        "https://drive.google.com/uc?export=view&id=1lziaSHmaQ1c3wwETltw3VCltI_jM2_uP",
        "https://drive.google.com/uc?export=view&id=1bQZbeCPN1r7xhpQefVfC6ZgIa_nsAV63",
        "https://drive.google.com/uc?export=view&id=1WDXUSvDdBuGOhVr96X3dT2E29QWfXB9M",
        "https://drive.google.com/uc?export=view&id=1oe09QwIvgqNvOQyURnL7cl7HjmltgyF3"
    ]

    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan sukses selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jenderal", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# BALEG
# ==================================================
elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1Zoz_J6ziRXd09_Hcjd6z47eUvfirQQkP",
        "https://drive.google.com/uc?export=view&id=1XZCFYmuCiHlH9G738GscIlkBZ4zaKEJu",
        "https://drive.google.com/uc?export=view&id=1LBt1DvzTgeNaedPzXwo3An1yD5lEWXWP",
        "https://drive.google.com/uc?export=view&id=1fXM4d0Exh81HF61mjHdEyPKx1WVbE_oU",
        "https://drive.google.com/uc?export=view&id=1SWdFBrm_10IXZDIDDhD1OrQJSq6FPhn_",
        "https://drive.google.com/uc?export=view&id=1DYlRzqlg3Fj3mjDtU6-QJLyOBi5D2n_L",
        "https://drive.google.com/uc?export=view&id=1X5wL1E3_YzemWv7PSUls_xL9eDPFrgAJ",
        "https://drive.google.com/uc?export=view&id=1TnmsP7Y3HC4fK6AGC37Y20Tr-XShJfVf",
        "https://drive.google.com/uc?export=view&id=1kO1S7hGEVHGsBIYSO28OY07HXd9boryu",
        "https://drive.google.com/uc?export=view&id=1DlNSJskHXvDz_D4MPw2wvIbW1Db8PYMP",
        "https://drive.google.com/uc?export=view&id=1uOg9WTZ1k_GffeeB8-yp98g3m7-PCxG2",
        "https://drive.google.com/uc?export=view&id=1OIZfKyQNHsuVZKkifScPf3gXstU8GTxT",
        "https://drive.google.com/uc?export=view&id=1SWdFBrm_10IXZDIDDhD1OrQJSq6FPhn_"
    ]

    data_list = [
        {"nama": "Ridho Benedictus Togi Manik", "jabatan": "Ketua Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I Legislasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Gh Mikael Niko A S", "jabatan": "Staf Komisi I Legislasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Siti Sarifah Sumamah", "jabatan": "Staf Komisi I Legislasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II  Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staf Komisi II  Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staf Komisi II  Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jeremia Halim", "jabatan": "Staf Komisi II  Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Sekar Dini Widya Putri", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Wan Nashwa Alhasni Yuska", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# SENATOR
# ==================================================
elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1uJGy2YN27wGxajieTcoFo58qPA175Iee",
        "https://drive.google.com/uc?export=view&id=1qKFONa6CVTGmAW99PWctyVxlU0PDrrJF",
        "https://drive.google.com/uc?export=view&id=1BF128CflWaMPUooYDyGSHyhzubJGnpBA",
        "https://drive.google.com/uc?export=view&id=1Y9s_cosqgKEJRuWrOdGp67Y8y1J2U8aS",
        "https://drive.google.com/uc?export=view&id=15icF5DhrgfnVoNr_okyV4hxi0r7dUUbM",
        "https://drive.google.com/uc?export=view&id=1k9Y1_lIAuSofI3EvyQTyjTdC91usuo_2",
        "https://drive.google.com/uc?export=view&id=1mIGmOwcV7YMuOVBADDer8Mt92Lx-WXE0",
        "https://drive.google.com/uc?export=view&id=11gyd3ZIqTtJTk-Jner7epdV5BGid5NKb",
        "https://drive.google.com/uc?export=view&id=1YkTM4scvquljazUmsUoWEjLgEVfhTABv",
        "https://drive.google.com/uc?export=view&id=1inP427vKqp2VSlJN0KdloETmFS9ftM4E"
    ]

    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Senator", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Senator", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Senator", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Senator", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Senator", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Senator", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Senator", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Senator", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN PSDA
# ==================================================
elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1VaJn5rnqrzbqAEGgnDp_yslqIs41ikQe",
        "https://drive.google.com/uc?export=view&id=1pULnnJpETfMhXm4Rr-ZLy45R_2cuVYsY",
        "https://drive.google.com/uc?export=view&id=1DrI7DNTRaRDspSawzT8j3GCwB8KtkRiB",
        "https://drive.google.com/uc?export=view&id=1lBuecx_CwX9Xw5fUY87_NbxlusuRlU4s",
        "https://drive.google.com/uc?export=view&id=1MQOVuTNJ2dwoQx8AVY0FwsRRCukgWSig",
        "https://drive.google.com/uc?export=view&id=1jcJqyZEvHzZOVIV-4ATj5FTfzrvlpa8e",
        "https://drive.google.com/uc?export=view&id=1OUfSVUn0LEVvpupqBfcQe9HottK8AQfr",
        "https://drive.google.com/uc?export=view&id=1AWHeggIAICnKu4oXG3pL3VBVm9tEtuKD",
        "https://drive.google.com/uc?export=view&id=1CFw8KBEdjsjEmMxztWl6cEUKh4yfUHAB",
        "https://drive.google.com/uc?export=view&id=1cDHKlKywRK7HU19fsZ-OaHI20CLAzDCn",
        "https://drive.google.com/uc?export=view&id=1Z7GspVrVlp-hrJFxLMszw7fy_gzK6V6x",
        "https://drive.google.com/uc?export=view&id=1ROn65eHppS5t4jC6JddRMCMDmc39Iqbk",
        "https://drive.google.com/uc?export=view&id=1JBdR0z93l35Blf8Ig81-DBhUCd0zHHsw",
        "https://drive.google.com/uc?export=view&id=1zGO8eQgPJFFX7YMh8E-44roUZSpcevYN",
        "https://drive.google.com/uc?export=view&id=1XwRr3DXSp_IuYySZ8uUPXIiyjaPvaFMK",
        "https://drive.google.com/uc?export=view&id=1-kLqiQ1ByImPriwmJwm9CpgbDHRdlfVk",
        "https://drive.google.com/uc?export=view&id=1BLZCo0CmKpo2dqsS4mBJZT9-9NQ2lBGR",
    ]

    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nobel Nizam F", "jabatan": "Kepala Divisi Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Caesar Ozora Alrando" , "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Charrlindah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Jeremi Marolop P. Situmorang", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
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
        {"nama": "Anggota MIKFES", "jabatan": "Kepala Departemen MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"}
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
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}
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
        {"nama": "Anggota Internal", "jabatan": "Kepala Departemen Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"}
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN SSD
# ==================================================
elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=18JSNBTQscbktXdbDx_Al5bgey0Gg6YAZ",
        "https://drive.google.com/uc?export=view&id=158H-trhaJpCtMS2Bg3cf3eB-gEMPmif-",
        "https://drive.google.com/uc?export=view&id=16HTWzkSqhBof_C9zKmUJexi9xx3MVxBD",
        "https://drive.google.com/uc?export=view&id=1ZDTM5Bfl1n41BFClCtUCwBih-pNryGR1",
        "https://drive.google.com/uc?export=view&id=110qsPkeMV1uAiU4QUvbfYEwFa5wfKguI",
        "https://drive.google.com/uc?export=view&id=1cav2--KYM0wOySn2nV-NAYpjjxd60r2b",
        "https://drive.google.com/uc?export=view&id=1-wUN2jY95DuenGt1alDkGblT2-pn4sey",
        "https://drive.google.com/uc?export=view&id=1ZBXbwYdIlY6_BlNIFLhF8w3U_SGl6DkK",
        "https://drive.google.com/uc?export=view&id=1cXYtX6sw7mnAIC-e3wI_uChXMtSU1uX0",
        "https://drive.google.com/uc?export=view&id=1_e3lJCi1kxP2-EYNIpiiIrAtpNkhXDsp",
        "https://drive.google.com/uc?export=view&id=1kY-bJ09YT-f-z9cWWpDXkE23VekeORPM",
        "https://drive.google.com/uc?export=view&id=1DhYuF2hf5h-fhJJHyJaj0Xj3x2g05Z2R",
    ]

    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Kepala Departemen", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Seketaris Departemen", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf SSD", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN MEDKRAF
# ==================================================
elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1H4xJ6bAIcqVHbw9v7LDxCu_XYAqYkNx6",
        "https://drive.google.com/uc?export=view&id=1nwAHwtnJS-7PYeuID8ekF-Xh-S570jx0",
        "https://drive.google.com/uc?export=view&id=1k8r6AXMP2v5YKH2zO5i8pwdLoTmDDtj_",
        "https://drive.google.com/uc?export=view&id=12JvUhziFx3OkSoTDxVaEhlnuMLcIrsGi",
        "https://drive.google.com/uc?export=view&id=1S-ZS_T726leoOrMSgpnP1i3ZYRROPeD_",
        "https://drive.google.com/uc?export=view&id=1ukcj_8UXDzCSy9kJp_nuCtBhN6-GX2mH",
        "https://drive.google.com/uc?export=view&id=1eD9m3X0Jt8NnuKdm17YjXXmpZy9Etxuv",
        "https://drive.google.com/uc?export=view&id=1L9stpCgAD838ljQHDg6qrjUjRdfNCD4G",
        "https://drive.google.com/uc?export=view&id=1Xoe1ooDihg_cWFynRKfgi46a5GDx3PFo",
        "https://drive.google.com/uc?export=view&id=1GARg2ycsJTh5rW4qR_ijXJbawccehJyk",
        "https://drive.google.com/uc?export=view&id=1Q6koQdG6dHXau7pE25j0x0kG31nocwPp",
        "https://drive.google.com/uc?export=view&id=1ZmfpMBwlMEmWeZ-9NyspXzPB6gTpqskL",
        "https://drive.google.com/uc?export=view&id=19TVQMduvpZkRUh0oajdP-cv22eNFc6HW",
        "https://drive.google.com/uc?export=view&id=1WHjzOU27ojepHU1Ju8ELUdEz2HKRre1C",
        "https://drive.google.com/uc?export=view&id=1YJNRGgQCLiTksJHTLSt7N6dZpvRnEeUl",
        "https://drive.google.com/uc?export=view&id=1TWCBMRuME-z3baBWVL8KtCI0dDwS8gZP",
        "https://drive.google.com/uc?export=view&id=1YdmIni_COiuWGHeZz6uCCaslm6L4DpQt",
        "https://drive.google.com/uc?export=view&id=1kEiNRomfsl9b9oGMbzWKlxXJRi1lCYrA",
    ]

    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Kepala Departemen", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Seketaris Departemen", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
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
        {"nama": "Daffa Kharisma Adzana", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN MINBAK
# ==================================================
elif menu == "Departemen Minbak":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]

    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Gusti Putu Ferazka D.", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ali Aristo Muthahhari Parisi", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Juwita Sari", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Ridwan", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]

    display_images_with_data(gambar_urls, data_list)
