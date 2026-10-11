import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
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
            "Departemen MINBAK",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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
            "nav-link-selected": {"background-color": "#8D4C06"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['Nim']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Yro_FiWM13COyTiubMR23sjR5v5EdKZB",
            "https://drive.google.com/uc?export=view&id=16i6ZBe3fFC7PIMT-OxHi-nSfBgLHSTzf",
            "https://drive.google.com/uc?export=view&id=1TPHBkQDDpCpF-uHuOkZkE2j58QgWKesb",
            "https://drive.google.com/uc?export=view&id=1HNkx2-8WrgbVhufU7vIdeKPlkhi66NlR",
            "https://drive.google.com/uc?export=view&id=1mhlOxKmXscotUGYn4hwjj7fO6X6TuBPX",
            "https://drive.google.com/uc?export=view&id=1OUaA6I7TtdOwh1Y_aApoar95wnbYhHcc",
        ] 
        

        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Nim": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "push rank sampe imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Abangnya keren, kalem, asik juga waktu jadi pemateri",  
                "Pesan":"Semangat terus bang semoga skripsinya dimudahkan"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "Nim": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "Zikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Abangnya asik, lucu, suka bercanda juga, kalau jadi pemateri asik",  
                "Pesan":"Sehat selalu bang semoga dimudahkan segala urusan"
            },
            {
                "Nama": "Efi Defiyati",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kakaknya baik sama kalem",  
                "Pesan":"Semangat terus dan sehat selalu kak"
            },
            {
                "Nama": "Qois Olifio",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_ ",
                "Kesan": "Abangnya keren, kalem, lucu",  
                "Pesan":"Semangat  bang, semoga lancar bikin skripsinya"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Nim": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Bertemu Kesekjenan",
                "Sosmed": "@hafsafadhilaa",
                "Kesan": "Kakaknya cantik, baik, kalem, asik juga",  
                "Pesan":"Semangat terus kak, sehat selalu, jangan lupa istirahat"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "Nim": "123450004",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Airan",
                "Hobbi": "Mintain Duit",
                "Sosmed": "@luthfiaarmdhni ",
                "Kesan": "Kakaknya lucu, baik, keren, asik juga",  
                "Pesan":"Semangat terus kak, semoga dimudahkan kuliahnya kak segala urusannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x6d-BunsI4-mBwmf8BbzzIa4eZB044it",
            "https://drive.google.com/uc?export=view&id=1k8djGjDJrGByw5IxevM6GQ7dPpC1ypID",
            "https://drive.google.com/uc?export=view&id=10lRmV4O8jWfKrWajgXpXCgdoj0ZBNQf5",
            "https://drive.google.com/uc?export=view&id=11Xf7Tdwx2_WlXHvK6Pynh7ttb6FU5P3J",
            "https://drive.google.com/uc?export=view&id=1z0d5DSj0wxZlFbUC5UWJAZoA5SIKLTzQ",
            "https://drive.google.com/uc?export=view&id=1ZJwKIhmpWkY1rXEAv_eLPdxNbeBkmVSc",
            "https://drive.google.com/uc?export=view&id=1ZRWj7EtnH09DCTomZLL5rdh3B8t5wOPG",
            "https://drive.google.com/uc?export=view&id=1i2l8DGp7sjpGejD3enQe1J_qbjhujgCk",
            "https://drive.google.com/uc?export=view&id=1V3MzDHolrVrsxg8Z2oqUGyB_D3EPMtZX",
            "https://drive.google.com/uc?export=view&id=16AqH7RncpBDuJNWUgE7mkZykSIK-9-xs",
        ]

        data_list =[
            {
                "Nama": "Fathinah Nur Azizah",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, pembawaannya adem, positif bangat auranya.",
                "Pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "Nim": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobbi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Abangnya asikkkk, ramah juga",
                "Pesan": "Semangat terus bang, jangan lupa makan"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "Nim": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobbi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya kalem, suka bercanda",
                "Pesan": "Semangat teruss bang"
            },
            {
                "Nama": "Suci Aulia",
                "Nim": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobbi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kakaknya ramah bangatt, baik sama cantikk",
                "Pesan": "Sehat selalu kak, lancar selalu kuliahnya"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "Nim": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya kalem gitu, trus abnagnya kelihatan bangat aura pintarnya",
                "Pesan": "Sehat selalu bang, semangat terus juga"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "Nim": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobbi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "Kakaknya baik, ramah jugaa",
                "Pesan": "Semoga kuliahnya lancar ya kak, Semangat teruss pokonya"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "Nim": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kakaknya imuttz, asik juga ",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "Nim": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobbi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Abangnya keren, asik juga",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "Nim": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kakaknya cantik, ramah, baik",
                "Pesan": "Semangat terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "Nim": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobbi": "Baca Buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kakaknya cantikk, baik dan ramah juga",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xwkUIMV3fL999bHm088cp_NH93kzJfta",
            "https://drive.google.com/uc?export=view&id=1_C76qpPna82TFWLKIg0dzoav49sEE5P2",
            "https://drive.google.com/uc?export=view&id=1Vf-pHC9E3YFfDZhUjMz0nVQcrZY999Jq",
            "https://drive.google.com/uc?export=view&id=1b8yMuQPOcrRzO2CovPdWduQY4Q6ZsB7t",
            "https://drive.google.com/uc?export=view&id=14Of9LVad4xHw2qppq6-_o60Gr959L8la",
            "https://drive.google.com/uc?export=view&id=1RYr-paGITdtu_CuhbREurR9cJhVgejIA",
            "https://drive.google.com/uc?export=view&id=1kaBhTpr66WEz_3dUbWDsjIysuPmgr3SP",
            "https://drive.google.com/uc?export=view&id=1Zok1NtqzafW7f_zUbtkfKmadfdpXrKD2",
            "https://drive.google.com/uc?export=view&id=1w8xWQAztVQQyHX6cm41-We_1J4-IZ1LC",
            "https://drive.google.com/uc?export=view&id=1cVBLZ77vS9g_uN2c1EMyYkgXEQpvGdij",
            "https://drive.google.com/uc?export=view&id=1LfHk8XXaSddwUXk83Od2i0j-04osuFBi",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # sisa
        ]
      
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "Nim": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Mencari dan membaca jurnal, 2 minggu mewawancarai anak kader angkatan 25 Datavora tercinta, mencari pak Luki",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Abangnya asik",
                "Pesan": "Semangat terusbang, semoga skripsinya lancar bang"
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "Nim": "123450123",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Memasak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya cantik, baik dan ramah",
                "Pesan": "Sehat selalu kak "
            },
            {
                "Nama": "Afifah Fauziah",
                "Nim": "123450002",
                "Umur": "19",
                "Asal": "Depok",
                "Alamat": "Belakang PB",
                "Hobbi": "Ngumpulin data sama nonton Marvel",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakaknya cantik, baik dan asik",
                "Pesan": "Semangat terus ya kak, semoga lancar kuliahnya"
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "Nim": "124550012",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sebelah kost Ayake",
                "Hobbi": "Scroll Facebook",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Abangnya baik dan santai",
                "Pesan": "Semangat terus bang ,Semoga sukses"
            },
            {
                "Nama": "Layina Ropiqo",
                "Nim": "124550016",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Menonton Film",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakaknya cantik, ramah dan baik",
                "Pesan": "Semangat terus ya kak"
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "Nim": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobbi": "Nonton Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya kalem dan baik",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Talitha Justine",
                "Nim": "124450076",
                "Umur": "19",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Pemda",
                "Hobbi": "Nonton",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya cantik, ramah, dan baik",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Anadia Carana",
                "Nim": "123450019",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Kost The Icon",
                "Hobbi": "Belajar",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya kelihatan bangat aura pinter dan ramah nya",
                "Pesan": "Sukses terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "Nim": "123450062",
                "Umur": "21",
                "Asal": "Oku, Sumatera Selatan",
                "Alamat": "Airan",
                "Hobbi": "Godain cewe bang Homey",
                "Sosmed": "@pomest_",
                "Kesan": "Abangnya asik dan seru",
                "Pesan": "Semangat terus bang, semoga skripsinya lancar"
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "Nim": "124550008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping Kost Rafli",
                "Hobbi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Abangnya baik dan asik",
                "Pesan": "Jangan lupa bahagia, Semoga sehat terus bang"
            },
            {
                "Nama": "Anggun Nita",
                "Nim": "124550009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobbi": "Menonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya bukan cuman cantik, kakaknya ramah dan baik juga",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
            {
                "Nama": "Della Anisa Fitri",
                "Nim": "124450095",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestari",
                "Hobbi": "Lagi suka olahraga",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Internal":
    def Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            
        ]
        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "Nim": "123450106",
                "Umur": "20",
                "Asal":"Tangerang Kota",
                "Alamat": "Gerbang Barat",
                "Hobbi": "Begadang",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Abang asik, baik, sama bisa diajak diskusi",  
                "Pesan":"semangat abang, sehat selalu"
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "Nim": "123450034",
                "Umur": "21",
                "Asal":"Way Kanan",
                "Alamat": "Untung Suropati",
                "Hobbi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "kakaknya cantik, ramah dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, lancar skripsi"
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "Nim": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca Novel",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kakaknya cantik, asik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak"
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Tetangga Singapore",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_",
                "Kesan": "Abangnya asik, ramah dan seru",  
                "Pesan":"semangat terus kuliahnya abang"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "Nim": "124450096",
                "Umur": "18",
                "Asal":"Indragirihulu",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Sleep Call",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "kakaknya cantik, asikkkk, dan ramah",  
                "Pesan":"semangat kakak, sehat selalu"
            },
            {
                "Nama": "Cerine Sihotang",
                "Nim": "124450049",
                "Umur": "19",
                "Asal":"Semarang",
                "Alamat": "Belwis",
                "Hobbi": "Manjat pohon kelapa",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "kakaknya asikk, cantik, dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, Sehat selalu"
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "Nim": "124450094",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Pemda",
                "Hobbi": "Main Biola",
                "Sosmed": "@jay.saputra.tmb",
                "Kesan": "abangnya asik, seru orangnya, ramah jugaa",  
                "Pesan":"semangat selalu bangg, sehat selalu"
            },
            {
                "Nama": "Najla Nursyifa",
                "Nim": "124450051",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Nonton asmr",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kakaknya Cantik, asik, ramah, dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, sehat selalu"
            },
            {
                "Nama": "Rozak Ramdani",
                "Nim": "124450100",
                "Umur": "19",
                "Asal":"Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobbi": "Badminton",
                "Sosmed": "@rozakramdani_",
                "Kesan": "Abangnya seru dan baik",  
                "Pesan":"semoga sehat selalu abang"
            },
            {
                "Nama": "Teresa Christiani Purba",
                "Nim": "124450046",
                "Umur": "19",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobbi": "Memasak",
                "Sosmed": "@christiani8872",
                "Kesan": "kakanya baik, cantik, asik juga kayaknya",  
                "Pesan":"semoga selalu dikelilingi orang baik dan sehat selalu kak"
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "Nim": "123450064",
                "Umur": "Padang",
                "Alamat": "Way Kandis",
                "Hobbi": "Nonton MU",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang, lancar kuliahnya"
            },
            {
                "Nama": "Audina Fitria",
                "Nim": "124450038",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobbi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kakaknya cantikk, asik,  dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, sehat selalu"
            },
            {
                "Nama": "Cika Adelia BR Marbun",
                "Nim": "124450107",
                "Umur": "20",
                "Asal":"Riau",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Scroll tiktok",
                "Sosmed": "@cikambrn",
                "Kesan": "Kakaknya seru dan baik",  
                "Pesan":"Jaga kesehatan kakak, semoga bahagia selalu"
            },
            {
                "Nama": "Gustin H Tampubolon",
                "Nim": "124450068",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobbi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "kakanya baik, seru orangnya",  
                "Pesan":"semoga selalu dikelilingi orang baik, lancar kuliahnya kak"
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "Nim": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Nangkap lele",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang"
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "Nim": "124450036",
                "Umur": "21",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Main game di HP temen",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang, sehat"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Internal()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "Nim": "123450082",
                "Umur": "20",
                "Asal": "Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwu",
                "Hobbi": "Musingin TA",
                "Sosmed": "@naylasalsabilaa._",
                "Kesan": "Kakaknya cantik, ramah , dan baik juga",
                "Pesan": "Sehat selaluu kakk"
            },
            {
                "Nama": "Donna Maya Puspita",
                "Nim": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobbi": "Berenang",
                "Sosmed": "@donnamaya.p",
                "Kesan": "Kakaknya ramah bangat, baikk jugaa",
                "Pesan": "Semoga selalu dimudahkan kak, sehat selalu ya"
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "Nim": "123450037",
                "Umur": "20",
                "Asal": "Medan, Jakarta Utara, Palembang",
                "Alamat": "Way Huwi",
                "Hobbi": "Buka Tutup Laptop",
                "Sosmed": "@noerruuu",
                "Kesan": " Abangnya baik",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "Nim": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Ballet",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakaknya cantik dan ramah",
                "Pesan": "Lancar Kuliahnya kakk"
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "Nim": "124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Mancing emosi",
                "Sosmed": "felisyanbl",
                "Kesan": "kakaknya maniss, cantik juga",
                "Pesan": "Lancar kuliahnya kak"
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "Nim": "124450031",
                "Umur": "18",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Dukung silver arrow alias mercedes",
                "Sosmed": "@muh_razan_",
                "Kesan": "Abangnya baik",
                "Pesan": "Semangat terus dan sehat selalu bang"
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "Nim": "123450086",
                "Umur": "17",
                "Asal": "Bali",
                "Alamat": "Airan",
                "Hobbi": "Nongkrong depan prodi",
                "Sosmed": "saniayyllstr",
                "Kesan": "Kakaknya cantikk, ramah juga",
                "Pesan": "Semanagt terus kak"
            },
            {
                "Nama": "Allisha",
                "Nim": "124450019",
                "Umur": "3 Tahun",
                "Asal": "Surga",
                "Alamat": "Rumah Asha",
                "Hobbi": "Ice skating",
                "Sosmed": "@aallishaa.aa",
                "Kesan": "Kakaknya baik, asik juga ",
                "Pesan": "Semoga apa yang kakak inginkan segera terwujud"
            },
            {
                "Nama": "Alya Ramadhanti",
                "Nim": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobbi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Kakaknya baikkk",
                "Pesan": "Lancar terus kak kulainya, semangat selalu"
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "Nim": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobbi": "Mengkoding",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kakaknya asik bangat, ramah juga, cantikkk",
                "Pesan": "Semangat terus kakk, semoga sehat selalu"
            },
            {
                "Nama": "Difanya Husakina",
                "Nim": "124450043",
                "Umur": "7.137 hari per hari ini",
                "Asal": "Sumsel",
                "Alamat": "Kafe Kali",
                "Hobbi": "Bobo cantik",
                "Sosmed": "@difanyhsa",
                "Kesan": "Kakaknya cantikkk, ramah, dan baik",
                "Pesan": "Sehat selalu kak, Semangat terus"
            },
            {
                "Nama": "Nazlah Auliya",
                "Nim": "124450054",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Mimpi diatas kasur",
                "Sosmed": "nzlhauly_",
                "Kesan": "kakaknya cantik, baikk, dan ramah",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Raihana Adelia Putri",
                "Nim": "123450041",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan Raya 1",
                "Hobbi": "Menulis, membaca",
                "Sosmed": "n1tg._",
                "Kesan": " Kakaknya cantikk, imutt",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "Nim": "124450061",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@daffascript_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "Nim": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobbi": "Scrolling Fesbuk",
                "Sosmed": "@eddel_0712",
                "Kesan": "Abangnya baik",
                "Pesan": "Sehat selalu bang dan semangat terus"
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "Nim": "124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Nonton Star Wars",
                "Sosmed": "luciarachel_",
                "Kesan": "Kakaknya cantikk",
                "Pesan": "Sehat selalu kak, lancar kuliahnya"
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "Nim": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobbi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "kakaknya baik dan ramah",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "Nim": "124450112",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@xifasky",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
    
