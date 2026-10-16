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
            "nav-link-selected": {"background-color": "#3FBAD8"},
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
            st.write(f"Jabatan: {data_list[i]['Jabatan']}")
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
            "https://drive.google.com/uc?export=view&id=1jeqH0Z7W_JS6vlWK9ki8LTvsWGGVdiUD",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Pesan":"Semangat bikin bikin suratnyaa bang, semoga jadi mudah bikin skripsinya"
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
                "Pesan":"Semangat terus kak, sehat selalu"
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
                "Pesan":"Semoga dimudahkan selalu ya kak segala urusannya"
            },                                     
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Senator":
    def senator():
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
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, baik, kalem, keren",
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
                "Kesan": "Abangnya seru, asik, lucu",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "Nim": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobbi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya baik, asik, kalem",
                "Pesan": "Semoga selalu dimudahkan bang"
            },
            {
                "Nama": "Suci Aulia",
                "Nim": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobbi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kakaknya kalem dan baik",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "Nim": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya asik, keren, pinter juga",
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
                "Kesan": "Kakaknya lucu, asik juga",
                "Pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "Nim": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kakaknya lucu, keren juga",
                "Pesan": "Semoga kelompoknya nambah gacor kak"
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
                "Pesan": "Semoga sukses bang"
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
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
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
                "Kesan": "Abangnya lucu dan asik",
                "Pesan": "Semangat skripsinya lancar bang"
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "Nim": "123450123",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Memasak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu, semangat terus kak"
            },
            {
                "Nama": "Afifah Fauziah",
                "Nim": "123450002",
                "Umur": "19",
                "Asal": "Depok",
                "Alamat": "Belakang PB",
                "Hobbi": "Ngumpulin data sama nonton Marvel",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakaknya baik dan asik",
                "Pesan": "Semangat terus ya kak"
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
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Layina Ropiqo",
                "Nim": "124550016",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Menonton Film",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakaknya ramah dan baik",
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
                "Pesan": "Sehat terus bang"
            },
            {
                "Nama": "Talitha Justine",
                "Nim": "124450076",
                "Umur": "19",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Pemda",
                "Hobbi": "Nonton",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya ramah dan baik",
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
                "Kesan": "Kakaknya pinter dan ramah",
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
                "Kesan": "Abangnya lucu, asik dan seru",
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
                "Pesan": "Semoga sehat terus bang"
            },
            {
                "Nama": "Anggun Nita",
                "Nim": "124550009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobbi": "Menonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya ramah dan baik",
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

elif menu == "Departemen internal":
    def internal():
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
                "Asal": "Tangerang Kota",
                "Alamat": "Gerbang Barat",
                "Hobbi": "Begadang",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Abangnya asik, seru di ajak diskusi",
                "Pesan": "Semangat di semester akhir ini bang"
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "Nim": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Suropati",
                "Hobbi": "Suka Menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Ramah kakaknya, seru diajak diskusi",
                "Pesan": "Semangat menjalani kuliah kak"
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "Nim": "123450038",
                "Umur": "21",
                "Asal": "Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca Novel",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Asik banget kakanya",
                "Pesan": "Semangat untuk meraih mimpi"
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "Nim": "124450021",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobbi": "Supporteran",
                "Sosmed": "@farhnghnii.",
                "Kesan": "Abangnya keren jago main alat musik",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "Nim": "124450096",
                "Umur": "18",
                "Asal": "Indragirihulu",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Sleep Call",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "kakaknya asik di ajak ngobrol",
                "Pesan": "Semangat kuliah kak"
            },
            {
                "Nama": "Cerine Sihotang",
                "Nim": "124450049",
                "Umur": "19",
                "Asal": "Semarang",
                "Alamat": "Belwis",
                "Hobbi": "Manjat Pohon Kelapa",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Kakanya keren dan selalu semangat",
                "Pesan": "Semangat menjalani kuliah"
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "Nim": "124450094",
                "Umur": "21",
                "Asal": "Kisaran",
                "Alamat": "Pemda",
                "Hobbi": "Main Biola",
                "Sosmed": "@jay.saputra.tmb",
                "Kesan": "Abangnya asik, seru sekali kalo diajak ngobrol",
                "Pesan": "Semangat menjalani kuliah "
            },
            {
                "Nama": "Najla Nursyifa",
                "Nim": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobbi": "Nonton asmr",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Ramah dan asik",
                "Pesan": "Semangat menjalani kuliah"
            },
            {
                "Nama": "Rozak Ramdani",
                "Nim": "124450100",
                "Umur": "19",
                "Asal": "Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobbi": "Badminton",
                "Sosmed": "@rozakramdani_",
                "Kesan": "Kalem seru diajak ngobrol",
                "Pesan": ""
            },
            {
                "Nama": "Teresa Christiani Purba",
                "Nim": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobbi": "Memasak",
                "Sosmed": "@christiani8872",
                "Kesan": "Asik kakaknya",
                "Pesan": "Semangat nutorin RA kak"
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "Nim": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobbi": "Nonton MU",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Kalem dan keren",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Audina Fitria",
                "Nim": "124450038",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobbi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Ramah kakaknya san seru",
                "Pesan": "Selalu semangat mengejar mimpi"
            },
            {
                "Nama": "Cika Adelia BR Marbun",
                "Nim": "124450107",
                "Umur": "20",
                "Asal": "Riau",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Scroll tiktok",
                "Sosmed": "@cikambrn",
                "Kesan": "Asik dan seru kalo ngobrol",
                "Pesan": "Semangat terus kuliah"
            },
            {
                "Nama": "Gustin H Tampubolon",
                "Nim": "124450068",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Airan",
                "Hobbi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Asik dan seru kakanya",
                "Pesan": "Semangat mengejar mimpi"
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "Nim": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Nangkap lele",
                "Sosmed": "@muhvinz_",
                "Kesan": "Keren abangnya dan seru",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "Nim": "124450036",
                "Umur": "",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Main game di HP temen",
                "Sosmed": "@snasaa._",
                "Kesan": "kakaknya kalem dan asik",
                "Pesan": "Selalu semangat menjalani kuliah"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen Minat dan Bakat":
    def mikat():
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
        ]
        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "Nim": "123450009",
                "Umur": "21",
                "Asal": "Sulawesi Selatan",
                "Alamat": "Panjang, Bandar Lampung",
                "Hobbi": "Main gaplek",
                "Sosmed": "@kevinaj_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "Nim": "123450046",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Way Dadi",
                "Hobbi": "Mendaki Gunung",
                "Sosmed": "@ferazkaa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "Nim": "123450088",
                "Umur": "21",
                "Asal": "Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobbi": "Nonton F1",
                "Sosmed": "@ali_parisi3",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "Nim": "124450058",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Airan",
                "Hobbi": "Belajar",
                "Sosmed": "@aayuandriani_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Dafa Elpriza",
                "Nim": "124450024",
                "Umur": "21",
                "Asal": "Bandung",
                "Alamat": "Way Kandis",
                "Hobbi": "Main Futsal",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Juwita Sari",
                "Nim": "124450066",
                "Umur": "19",
                "Asal": "Lampung Barat",
                "Alamat": "Pemda",
                "Hobbi": "Muter-muter",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "Nim": "124450047",
                "Umur": "19",
                "Asal": "Lampung Tengah",
                "Alamat": "JL. Pulau Damar",
                "Hobbi": "Nemenin Bang Ridwan nonton tinju",
                "Sosmed": "@afdall.03",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "Nim": "124550002",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang ke Metro",
                "Sosmed": "@sllbnzw_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Ridwan",
                "Nim": "123450091",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Belwis",
                "Hobbi": "Nonton tinju",
                "Sosmed": "@mridwaan__",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Andra Ilham Bintang",
                "Nim": "124550060",
                "Umur": "18",
                "Asal": "Sumatera Selatan",
                "Alamat": "Kota Baru",
                "Hobbi": "Nemenin Bryan nonton tinju",
                "Sosmed": "@andra.lhm",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "Nim": "124550003",
                "Umur": "20",
                "Asal": "Nias",
                "Alamat": "Belwis",
                "Hobbi": "Live TikTok",
                "Sosmed": "@bryantel_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "Nim": "124550067",
                "Umur": "17",
                "Asal": "Surabaya",
                "Alamat": "Kemiling",
                "Hobbi": "Main beiblet",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "Nim": "124550055",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Memasak",
                "Sosmed": "@indahjuliaa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "Nim": "124550023",
                "Umur": "18",
                "Asal": "Nusa Tenggarang Barat",
                "Alamat": "Rajabasa",
                "Hobbi": "Nebang Pohon",
                "Sosmed": "@cacalvra",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Eafka Fatih Al Fatih Ghathfaan",
                "Nim": "124550089",
                "Umur": "20",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Kota Baru",
                "Hobbi": "Bangun Pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    mikat()

if menu == "Badan Legislatif":
    def legislatif():
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
        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "Nim": "123450060",
                "Umur": "20",
                "Asal": "Kuala Lumpur",
                "Alamat": "GH",
                "Hobbi": "Ke Cafe",
                "Sosmed": "@iamridhomanik",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "Nim": "123450085",
                "Umur": "19",
                "Asal": "Sikawang",
                "Alamat": "Pelangi",
                "Hobbi": "Dengerin Lagu Pilihlah Aku dari Krisdayanti",
                "Sosmed": "@j_eesie",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "Nim": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Ngidupin api Baleg di tiktok",
                "Sosmed": "@ddharu_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "GH Mikael Niko AS",
                "Nim": "124450025",
                "Umur": "20",
                "Asal": "Pasir Sakti",
                "Alamat": "Jati Agung",
                "Hobbi": "Tidur",
                "Sosmed": "@me._kael",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "Nim": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobbi": "Mancing",
                "Sosmed": "@syt.rifa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Givaro Ananta",
                "Nim": "123450078",
                "Umur": "21",
                "Asal": "Lampung Barat",
                "Alamat": "Sukabumi",
                "Hobbi": "minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "Nim": "124450042",
                "Umur": "18",
                "Asal": "kepulauan mentawai, lampung",
                "Alamat": "kadang di kos sekar kadang di kos putri",
                "Hobbi": "memanjat",
                "Sosmed": "@afghanisnt_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Hani Qurrota Aini",
                "Nim": "124450020",
                "Umur": "20",
                "Asal": "City Earth",
                "Alamat": "Sukarame",
                "Hobbi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Jeremia Halim",
                "Nim": "124450101",
                "Umur": "20",
                "Asal": "Cibaduyut",
                "Alamat": "Teluk",
                "Hobbi": "Bernyanyi",
                "Sosmed": "@jeremia_hm",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@monica_tjg",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "Nim": "124450121",
                "Umur": "20",
                "Asal": "depok",
                "Alamat": "pemda raya",
                "Hobbi": "nge gym dan koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "Nim": "124450082",
                "Umur": "20",
                "Asal": "metro",
                "Alamat": "pemda",
                "Hobbi": "main sama kak nisa",
                "Sosmed": "@sekardnwp",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@nshaysk",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    legislatif()

if menu == "Departemen MIKFES":
    def mikfes():
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "Nim": "124450104",
                "Umur": "21",
                "Asal": "Balam",
                "Alamat": "-5.386541,105.262255",
                "Hobbi": "Nyapu wico lantai 2, lantai 3, lantai 4, lantai 5 gedung F",
                "Sosmed": "@biyokcb",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Tanty widiyastuti",
                "Nim": "123450094",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan",
                "Hobbi": "membaca",
                "Sosmed": "IG @tvnty_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Fadil Prasetyo",
                "Nim": "123450048",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "IG @fadilalfarizzii",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Manuel Frederika",
                "Nim": "124450039",
                "Umur": "20",
                "Asal": "batam",
                "Alamat": "way kandis",
                "Hobbi": "tenis meja",
                "Sosmed": "@manuelfdk_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "Nim": "124450005",
                "Umur": "17",
                "Asal": "Lampung Tengah",
                "Alamat": "Korpri",
                "Hobbi": "Tidur",
                "Sosmed": "@violaadrtr_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Risa Romadona",
                "Nim": "124450127",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Rolling skate",
                "Sosmed": "risarmdna",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Vannisa Ramadhani",
                "Nim": "124450078",
                "Umur": "19",
                "Asal": "Kepulaun Riau",
                "Alamat": "Teluk Betung",
                "Hobbi": "Nonton film action tom cruise liam nesson jackie chan",
                "Sosmed": "@vunnycaa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Yulia Kristine Malau",
                "Nim": "12440119",
                "Umur": "20",
                "Asal": "jambi",
                "Alamat": "sabah balau",
                "Hobbi": "main alat musik",
                "Sosmed": "krnylee",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "Nim": "123450119",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Dengerin Musik",
                "Sosmed": "IG @keyashafi_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Elsa Sitorus",
                "Nim": "124450088",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Pemda",
                "Hobbi": "Rebahan",
                "Sosmed": "_els.a",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Fadya Izzatul 'Aini",
                "Nim": "124450062",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Main ML",
                "Sosmed": "fadyaizzatul_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Lovianora Saragih",
                "Nim": "124450105",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "IG @from_loviaa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "Nim": "124450092",
                "Umur": "20",
                "Asal": "Kalianda",
                "Alamat": "Kotabaru",
                "Hobbi": "Main game, tidur, dengerin musik",
                "Sosmed": "ig: aruccy_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Sherena Florencia",
                "Nim": "124450027",
                "Umur": "19",
                "Asal": "Bengkulu Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Menunda Pekerjaan",
                "Sosmed": "sher_renna",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "Nim": "123450096",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "belwis",
                "Hobbi": "futsal",
                "Sosmed": "IG @razyn.hfd",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Faiza Try Anjani",
                "Nim": "124450075",
                "Umur": "19",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobbi": "Belajar",
                "Sosmed": "faizaanjanii",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Gathfan Nadhif Ali",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@gathfannad",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "Nim": "124450064",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Metro Kibang, LamTim",
                "Hobbi": "Ngoding & Ngegame",
                "Sosmed": "@apiszzaja_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "Nim": "124450053",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Campang Raya",
                "Hobbi": "nge-gym, baca novel",
                "Sosmed": "IG @kelelep_comberan",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "Nim": "124450087",
                "Umur": "19",
                "Asal": "Sumsel",
                "Alamat": "Sukarame",
                "Hobbi": "Nari",
                "Sosmed": "@melva_fbrt",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Stafiqul Falakh",
                "Nim": "124450099",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Membaca",
                "Sosmed": "@syaafiqui",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "Nim": "124450115",
                "Umur": "2000",
                "Asal": "Kota Bumi",
                "Alamat": "Rajabasa",
                "Hobbi": "Nongkrong",
                "Sosmed": "henryferdianto",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()
    
# Tambahkan menu lainnya sesuai kebutuhan
