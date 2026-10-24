import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Badan Legislatif",
            "Badan Kesenatoran",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
            "Departemen Minbak",
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
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14Ltb0h4v9C6oQMtNlYpbiJyN3UzAj7Lq",
            "https://drive.google.com/uc?export=view&id=17cAvk0CVbXBfy_l2bxCOHiytm_Hwlukt",
            "https://drive.google.com/uc?export=view&id=1pXIHg55_wd-ke61JcGkqLVpU0k8E5bAc",
            "https://drive.google.com/uc?export=view&id=1tapAFvkjFNjSJifoADCN9Igxv1b-d_3R",
            "https://drive.google.com/uc?export=view&id=15ZLEyLFtNxWfjlgRJBXakZOex0DB4dR8",
            "https://drive.google.com/uc?export=view&id=1TvjsRMq2GhnI_V84IbA4AaDtc4L6z_Zc",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bangkinam",
                "alamat": "Sekretariatan HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@Muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyanti",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
           {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hafsa Fazilah Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu lulu",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },          
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Z2O2eUKpon98s1sAOIG2rDjGyx0FrvXl",
            "https://drive.google.com/uc?export=view&id=1gZnYlXnWPWHyQmQLLWRVHFTjgADXe1cw",
            "https://drive.google.com/uc?export=view&id=1ECA0utPmU1lMY2qWTOIhzF4XqQg6nUtr",
            "https://drive.google.com/uc?export=view&id=1Hn-iqkIK5TwFCiNr7bjhHdjn9mSYZcxR",
            "https://drive.google.com/uc?export=view&id=16ij-gTIQiqWjALh9TM-GPykLUfMd-dkG",
            "https://drive.google.com/uc?export=view&id=1uxJ0XF0mTLuRULbTfcvSKL9--khf6wJM",
            "https://drive.google.com/uc?export=view&id=1Vc8A0sKm4-LdgLsDUgZoK1_994b1n8VE",
            "https://drive.google.com/uc?export=view&id=18dEzzF91M65gootLXX-IkOLMNGsC86h0",
            "https://drive.google.com/uc?export=view&id=1CToly3CvSUvqxjauxlJM1aMlusRKiW12",
            "https://drive.google.com/uc?export=view&id=1OjXJd6DX5d-_3vZXAk-HFB32imydJtVb",
            "https://drive.google.com/uc?export=view&id=1QYjHEg-ggWEA2bwbARLNkJ0pZrBkZB2O",
            "https://drive.google.com/uc?export=view&id=1OjXJd6DX5d-_3vZXAk-HFB32imydJtVb",
            "https://drive.google.com/uc?export=view&id=1rPA12tnPceTzCM2VrUI3gC1rJeCxk5FK",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Wan Naswa",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
         {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal":"Krui",
                "Alamat": "Jatimulyo",
                "Hobi": "Memancing",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Kak nisa orangnya baik, humble, kenal kak nisa udah dari semester satu, kak nisa orangnya sangat sangat bertanggung jawab.",  
                "Pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "Kak Monica orangnya murah senyum, baik dan lucu",  
                "Pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BiNk5M6Ci6N4ieWtwpg7HIcHNecztF_L",
            "https://drive.google.com/uc?export=view&id=1PFbWmbXemip08GdLYQXBgtSdlsz4Ohdi",
            "https://drive.google.com/uc?export=view&id=19ziY6jn9BuqaRz-5uLXNI5FcPuVCpIFL",
            "https://drive.google.com/uc?export=view&id=1Hg7JdAHRoXRbQa3_Mf-VqNGCqlVrKmJt",
            "https://drive.google.com/uc?export=view&id=1u-35So1IGuhboLrdhxjRaQajM7tpBMs9",
            "https://drive.google.com/uc?export=view&id=1Zv_yaDB0BGbAxggwQem6sin_Okx2m-Ae",
            "https://drive.google.com/uc?export=view&id=1ywi71_eg5aJyQDmitS-sp_n7Lz5oB4PF",
            "https://drive.google.com/uc?export=view&id=1EGc91St9QmGoQAW98O7rRth2NQYLc67c",
            "https://drive.google.com/uc?export=view&id=1phyGNH6m_o0gjmiOUtTzM8-RcjCV6Fc1",
            "https://drive.google.com/uc?export=view&id=1Lzp48GWSe0HtBxscC2NbSq9uRsjYlUE4",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eyqvx79ZWpnQoyR0lAyRr75Hyf0I-LuI",
            "https://drive.google.com/uc?export=view&id=1eAwxOqcO2CHwEVU9tD7etDWtyl__dwaX",
            "https://drive.google.com/uc?export=view&id=17uksT4DLi3Dl3Wm9eXkLgOboaMnBCNvf",
            "https://drive.google.com/uc?export=view&id=1rETxJSYLJ8b9dvIPSHnTBERaeVyqwE0a",
            "https://drive.google.com/uc?export=view&id=1FvCgEEhwao82YMF_lVNbzx2fH-9e6I89",
            "https://drive.google.com/uc?export=view&id=1qYo-6LdCrtd4Mo0-YNb7r_XZwtrl9jXs",
            "https://drive.google.com/uc?export=view&id=1Ml9GKM4ZJ0j5XPInbqklzBaUHOpXaCq0",
            "https://drive.google.com/uc?export=view&id=1y47hF232Pq91Qw3q8y6ZqeB4KSrndgFs",
            "https://drive.google.com/uc?export=view&id=1Y1XktCO2D4tnUNKvtCtm6cAIfkdLT9zb",
            "https://drive.google.com/uc?export=view&id=1CfquAfSW3Gw41L6Q-lCI5RS23W4MM7-g",
            "https://drive.google.com/uc?export=view&id=1QKaz5MKfppFLCfSOAlkf_CS-HV7FbLx2",
            "https://drive.google.com/uc?export=view&id=1J2v3zGFWZemwxekT6Qw4FOn2mx13Tzu6",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "1234501014",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game",
                "sosmed": "@biyokcb",
                "kesan": "-",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futssal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya ramah banget!!",
                "pesan": "Semangat terus bang!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik banget!!",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Main Game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik banget!!",
                "pesan": "Semangat terus bang!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya baikk banget!!",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@aruccy_",
                "kesan": "Abangnya baik banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Main Gitar",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Msake Up",
                "sosmed": "@sher_renna",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450075",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca Novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Banyak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()
# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LdrnIp0OvtSvDT-IDldV3A22HaVR6Sdx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket pantai",
                "alamat": "Samping kos capo",
                "hobbi": "ngerjain tugas",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Puri",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Samping Pasar",
                "hobbi": "duel boxing sama reno",
                "sosmed": "@friezaazmi",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Samping kost Ezra",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Giring anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Adam dan Hawa",
                "alamat": "Depan kontrakan",
                "hobbi": "nonjokin orang",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal":"Jakarta",
                "alamat": "Sebelah kost kak Vany",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@putrimannaa",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "23",
                "Asal": "Nias",
                "Alamat": "Airan",
                "Hobi": "Main musik",
                "Sosmed": "@dsmanhal",
                "Kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk",  
                "Pesan":"Semoga bang desman selalu didekat hal-hal baikk"# 1
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
                "Pesan":"Semoga semua keinginan kak azzel tercapai"# 1
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450041",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cendrawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlln",
                "Kesan": "Kak Charrlindah orangnya baikk, dan juga ramah",  
                "Pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 1
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "NIM": "124450111",
                "Umur": "17",
                "Asal":"Jayapura",
                "Alamat": "RS airan",
                "Hobi": "Nonton a day in my life",
                "Sosmed": "@jemarrro",
                "Kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus",  
                "Pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal":"Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main Roblox",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "Pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "18",
                "Asal":"Sibolga",
                "Alamat": "Belwis",
                "Hobi": "Membaca peraturan rektor",
                "Sosmed": "@dearrfkvmfl",
                "Kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "Pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "Pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LdrnIp0OvtSvDT-IDldV3A22HaVR6Sdx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Mancing Keributan",
                "sosmed": "@adityafq",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Khoirul Mutthoharoh",
                "nim": "1234500",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "1244500106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Bandar Lampung",
                "hobbi": "lihat lihat perumahan ",
                "sosmed": "@bimo_arkana",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal":"Ikut Kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi Idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal":"Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "1234500552",
                "umur": "21",
                "asal":"Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "123450103",
                "umur": "19",
                "asal":"Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "123450021",
                "umur": "20",
                "asal":"Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "123450093",
                "umur": "Masih muda lah",
                "asal":"Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@jaldii._",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "123450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "123450010",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

# INTERNAL
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y4xJfZhbU-rgFY7ckCA8CUn14vt3SHRE",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450006",
                "umur": "20",
                "asal":"Silikalang Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal":"Untung Suropati",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@risma.mustika_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 2
            },
            {
                "nama": "Muhammad Hanif Zaky",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang Sumatera Barat",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngikutin drama tiktok",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Cika Adelia Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa Minang",
                "sosmed": "@cikamrbn",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama Aqila",
                "sosmed": "snasaa._",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam Itera",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan Belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 11
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir Belwis",
                "hobbi": "Begadang",
                "sosmed": "cerine.ipynb",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 12
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 13
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 14
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 15
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 16
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VXMooslLY5QE2nBf2WQwOr5fw_uRpw-X",
            "https://drive.google.com/uc?export=view&id=1CVSG3ah2UyyPb8RPQHsYxtGeihHTfq5_",
            "https://drive.google.com/uc?export=view&id=1IqJC8v2UCADPBrPmyCeOogm7ZiBBx_oS",
            "https://drive.google.com/uc?export=view&id=1NCW8SfQnfE1KD8o9G3-oucwLOqdTqQqr",
            "https://drive.google.com/uc?export=view&id=1O_G7m-ZYSmpdZ-9ebdDn9wMUFuXa4bOQ",
            "https://drive.google.com/uc?export=view&id=1zWSMHRtBhKmrUmYB9iHbW0xvuWHspCAz",
            "https://drive.google.com/uc?export=view&id=1hImiEgJ_IiyMSpBfuoz3uxjngko8a4xY",
            "https://drive.google.com/uc?export=view&id=1hpABQVcO40hhLyC_zhKcSKfvBhQv7cne",
            "https://drive.google.com/uc?export=view&id=116MOZHTufQvguy5tiNaA81ROnaNMLbLf",
            "https://drive.google.com/uc?export=view&id=1gs0hRsRBginfVw8gu9FMg7kyOdVGdCl3",
            "https://drive.google.com/uc?export=view&id=1-l3-5wgudpCOW3_pFJRu8OLqNslAaZ8I",
            "https://drive.google.com/uc?export=view&id=1qSwAq_iKydbXlPf56AgwyVD4oJeAvMXv",
        ]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "NIM": "123450110",
                "Umur": "21 Tahun",
                "Asal":"Sumbar",
                "Alamat": "Belwis",
                "Hobi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Hanifah Inaya Sari",
                "NIM": "123450123",
                "Umur": "21",
                "Asal":"Balam",
                "Alamat": "Balam",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "19",
                "Asal":"Padang",
                "Alamat": "Hasan 4",
                "Hobi": "Nonton Marvel, Tidur",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "NIM": "124450012",
                "Umur": "21",
                "Asal":"lampung",
                "Alamat": "Pemda",
                "Hobi": "Main game",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "124450016",
                "Umur": "19 tahun",
                "Asal":"Semarang",
                "Alamat": "Balam",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Natar",
                "Hobi": "Mancing",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal":"Sumbar",
                "Alamat": "Kelengkeng 5",
                "Hobi": "Tidur",
                "Sosmed": "@talithaaajtine",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal":"Palembang",
                "Alamat": "Wayhui",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Abdillah Fikri Al pome",
                "NIM": "123450062",
                "Umur": "21",
                "Asal":"Sumsel",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal":"Sumbar",
                "Alamat": "Samping kost rafli",
                "Hobi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal":"Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "124450095",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Nargo Lestari",
                "Hobi": "Olahraga, Makan makanan manis",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LdrnIp0OvtSvDT-IDldV3A22HaVR6Sdx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nonton tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis dan membaca",
                "sosmed": "@n1tg.-",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": " Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "1244500031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450014",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gaada yang tau",
                "asal":"Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "1244500112",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@edsel_0712",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "SUkarame",
                "hobbi": "Nyuluh Manuk",
                "sosmed": "@daffascript_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Piano",
                "sosmed": "@nzlhauly",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Allisha",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

if menu == "Departemen Minbak":
    def Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LdrnIp0OvtSvDT-IDldV3A22HaVR6Sdx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Lari",
                "sosmed": "@kevinaj_",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D.",
                "nim": "123450046",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450121",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Motoran bareng bang bryan",
                "sosmed": "@dafaelpriza_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jalan Pulau Damar",
                "hobbi": "Menjawab soal dari dosen dipapan tulis",
                "sosmed": "@afdal.03",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "1244500024",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@slbnzw",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@mridwaan_22",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@andra.lhm",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@bryantel_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "1244500067",
                "umur": "17",
                "asal":"Semarang",
                "alamat": "Kemiling",
                "hobbi": "Ternak sapi",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Muhammad Rafka fatih Al Ghathfaan",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Tukang Parkir",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },                                                                         
        ]
        display_images_with_data(gambar_urls, data_list)
    Minbak()
