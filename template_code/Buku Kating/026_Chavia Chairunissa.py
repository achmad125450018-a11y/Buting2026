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
            "Departemen Minbak"
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
            "https://drive.google.com/uc?export=view&id=1sh-jJCj-9ip7RN0EuLslhsyHznUKiDwK",
            "https://drive.google.com/uc?export=view&id=1G2cPYH26LW1EnJaU-MLqjKb4Pm4kadfD",
            "https://drive.google.com/uc?export=view&id=1vhIHJwUBW1pOpeKVr5RP1_KSrhrZPxgW",
            "https://drive.google.com/uc?export=view&id=1g_M9Z_OdQzzX-OqKgKOndO7KCYd2hZQz",
            "https://drive.google.com/uc?export=view&id=1qiqCtguThFK9DJsaoFM0mgMbBTjk5ulO",
            "https://drive.google.com/uc?export=view&id=10jdr1K2Yf6-nkj7JY6RSPFFOTXDQOUrK",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "bang ginda keren panutan super keren.  ",  
                "pesan":"Semoga TA nya lancar terus yaa bang! "# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil kaya gangster gangster, keren abiezz, terus kaya orang jago gitu loh.",  
                "pesan":"Semoga bang Aqil sehat selalu yaa, happy teruss ta nya lancar"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefffiidefi",
                "kesan": "Kak Efi vibes nya cewe keren bangett.",  
                "pesan":"Semoga kuliah nya lancar terus yaa, bahagia terus kakk"# 1
            },
           {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "kakanya keren bangett, jarang jarang cwo jadi sekre",  
                "pesan":"semangat dan sehat teruss ya kakk"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu Luluk",
                "sosmed": "@hafsafazilahh",
                "kesan": "kak hafsa humble banget.",  
                "pesan":"happy terus ya kak!!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthhifiarmdhni",
                "kesan": "kak lutfia imut banget",  
                "pesan":"lancar lancar ya kak kuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kL92wnsyEoYz2qy1Le0deAwXrv3gbffG",
            "https://drive.google.com/uc?export=view&id=1js_7BVgeNmLX0cFnIybVzbkxNVDR0CWQ",
            "https://drive.google.com/uc?export=view&id=14CaGMZoaOe_vbUI4-I6AoEfVYDd_PLXh",
            "https://drive.google.com/uc?export=view&id=1s0yPm4twbVjOMoZU8jct0mZUQWDXwUMM",
            "https://drive.google.com/uc?export=view&id=1wIVkZ8caciA-RizItHmHRKtWQqT9xNk8",
            "https://drive.google.com/uc?export=view&id=1XntscKxFUy5H1kKTTLHVbkM8VZoqbOOF",
            "https://drive.google.com/uc?export=view&id=1bvQKt8algRM-1HduZTPZOudFfcbOF5lS",
            "https://drive.google.com/uc?export=view&id=1pa7BM4k8rYB7XT7rUtbT8yffyN1xvv4h",
            "https://drive.google.com/uc?export=view&id=1n6GP5C4_OenEYBUjmAZ-tw3KkwjhmY0T",
            "https://drive.google.com/uc?export=view&id=1GD1ysL8trSl8ffBqA8qaE6daG99ogII6",
            "https://drive.google.com/uc?export=view&id=1FOZgIT1u4ItS0KFuuy4XSEef-1MrBwWe",
            "https://drive.google.com/uc?export=view&id=1YZeOgSHtcPeNf7W8bEOCe2U_jY5n7nKB",
            "https://drive.google.com/uc?export=view&id=12OYIEQ5prwP2x64qOfVK-uMqCci7kWId",
            
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
                "kesan": "bang ridho baik, lucu juga terus orangnya sangat sangat fun ya ",
                "pesan": "sehat selalu ya bang ridho, sukses teruss"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "kak jue bener bener lucu imut outfit nya gemes banget",
                "pesan": "semangat TA nya ya kak!!!"  # 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Kakak nya baik, lucu juga",
                "pesan": "happy terus ya kak !!!"  # 1
            },
            {
                "nama": "Wan Naswa",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "outfit kakanya lucu banget gemes",
                "pesan": "happy dan semangat terus yaa kak !!!"  # 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "23",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "bang dharu orangnya baik banget humble juga",
                "pesan": "semangat dan sehat terus ya bang!!!"  # 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "bang givaro orangnya baik, lucu juga",
                "pesan": "semangat terus TA nya ya bang"  # 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "abangnya baik, outfitnya juga bagus banget",
                "pesan": "happy terus yaa bang  !"  # 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "bang jona lucu banget sih, orangnya baik juga",
                "pesan": "semangat dan sehat selalu ya bang !!!"  # 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "kakaknya keren banget, dan baik banget",
                "pesan": "happy terus ya kak!!!"  # 1
            },
         {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya dari city earth aka kotabumi, satu kampunk",
                "pesan": "happy dan semangat terus ya kak!!!"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "abangnya keren banget",
                "pesan": "happy dan semangat terus ya bang !!!"  # 1
            }, 
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, humble",  
                "pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica baik lucu juga",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
    

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NNyH3s5-ZgN1MtU5W_DPqlPwYrJK6gGr",
            "https://drive.google.com/uc?export=view&id=1FK9mia17rzt0TYToZz1621UQiHXykaKz",
            "https://drive.google.com/uc?export=view&id=1wkLdr85KLet_qIGhUj74GT6YRtF1fmSj",
            "https://drive.google.com/uc?export=view&id=1WYy-bAC5gReQoFA4xhiOSFOTprjphmkq",
            "https://drive.google.com/uc?export=view&id=1Lu4H8nOTZiExCSSv7tXdy0dCe-UAwlbM",
            "https://drive.google.com/uc?export=view&id=1KXWrm_ldT6-xK_MLAZ3xeJ1TAksgj1Jp",
            "https://drive.google.com/uc?export=view&id=1kQ2GC1UH7xFZPRR6Rzbf8_Nqc5Gelnon",
            "https://drive.google.com/uc?export=view&id=14wIKTYzQVMJEBam8tbqoDunopqo_xXAq",
            "https://drive.google.com/uc?export=view&id=1WdUXIqfbGNSldeDmIFkUmQWfMqR56Fen",
            "https://drive.google.com/uc?export=view&id=1KQAZVUce4lupdlfED8Zj253VlANNF_LE",
        ]

        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "-",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal": "Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    # PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GIr1rN2MwLUQ0fR2EtSp3HUZ9ZXikQdL",
            "https://drive.google.com/uc?export=view&id=1wIm3JHO1sV77lFPzDXGAjKUCRNktMNfm",
            "https://drive.google.com/uc?export=view&id=10LXA2Vna6XC054gBkk9BAOuYYmWeOnL9",
            "https://drive.google.com/uc?export=view&id=1oatTr0-wdkODSR8KtvDAxPAO48L46HJ4",
            "https://drive.google.com/uc?export=view&id=12NKepI-O7NBPIQtinARjkbfTyhtLJkZc",
            "https://drive.google.com/uc?export=view&id=1fzgj033vC8aCGNK7itMAILU1S-xGAx5n",
            "https://drive.google.com/uc?export=view&id=1eUAY-oxSuf5LbRC4PPA6TDOh8kdu2LD5",
            "https://drive.google.com/uc?export=view&id=1GHaEHkZzQD1gLwdX0azNLEN5XqkHsbh3",
            "https://drive.google.com/uc?export=view&id=1NpWXYOqSCix4Oi3iisrN8fY0TSor3CFX",
            "https://drive.google.com/uc?export=view&id=1NuTkFQmuJcLxA15OHjyXhEr_YaowcA33",
            "https://drive.google.com/uc?export=view&id=1umjMtOImZFMEX9gi4FkcUVHSbAkTknyO",
            "https://drive.google.com/uc?export=view&id=1pq2z-qzLJWsqoaTs-Jbi3Q75F6xv7-p6",
            "https://drive.google.com/uc?export=view&id=1LLyWO13MjsNQZXn5PmrDXHM7i4sbMtyQ",
            "https://drive.google.com/uc?export=view&id=1i9oyRv937PfwJaVv9NxMLEErRLzmgF-_",
            "https://drive.google.com/uc?export=view&id=1yrGQ8aDT5_R4D9pX-BwJDFLJndZbriEw",
            "https://drive.google.com/uc?export=view&id=1hVBXY0c4efMRKDf0WhVSBKCA9IWQCliJ",
            "https://drive.google.com/uc?export=view&id=1s9RS7GKRY3zzfEQ_SBJHSZ-ks4vcb17f",
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
                "sosmed": "@wielhawn",
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
                "sosmed": "@helmy_inst",
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
                "sosmed": "@barus.fernando",
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
                "sosmed": "@barus.fernando",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },  
            {
                "nama": "Desman Velius Halawa",
                "nim": "1234500114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "GH Raya",
                "hobbi": "lompat batu",
                "sosmed": "@desmanhal_",
                "kesan": "Kakaknya baik banget dan ramah juga",  
                "pesan":"Semangat terus kak!"# 11
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel orangnya humble, dan juga baik",  
                "pesan":"Semoga semua keinginan kak azzel tercapai"# 12
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "orangnya baikk, dan juga ramah",  
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 13
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar orangnya asik banget",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila kuliahnya lancar"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1M9Zkza-2FonsbpJT4AuvRrWjmqJRcHVj",
            "https://drive.google.com/uc?export=view&id=1foUQybl9ncvEB5vro7yWv8I1hIfejwvY",
            "https://drive.google.com/uc?export=view&id=1iO0jvULlTIhPqRIZwlidL-vX0zqsM_66",
            "https://drive.google.com/uc?export=view&id=1wECUhrE-bNqTE6ill7r6Y9J9eqrgM9w0",
            "https://drive.google.com/uc?export=view&id=1pECiUXwWt0XYu-JaszXfS9QVnLzhhlsN",
            "https://drive.google.com/uc?export=view&id=19zXlno-kwf5NEsZWUQ5S2x8Yj3iEYOuR",
            "https://drive.google.com/uc?export=view&id=1wQft-mH16rBhsg28PNyXOA7gJdu98uT3",
            "https://drive.google.com/uc?export=view&id=1XIkKFnVBLXTy8McDAvQWYLbwG_ZZETz8",
            "https://drive.google.com/uc?export=view&id=1oybRJar2tAyj5nwe2vRZ0G8qmKoiBfFm",
            "https://drive.google.com/uc?export=view&id=18dXiKNZmiopWzdeEG5cG_ww8wiDRvJOs",
            "https://drive.google.com/uc?export=view&id=10ay-q5mk8dm3m728sfweT-36qXfLzDdE",
            "https://drive.google.com/uc?export=view&id=1W088T77RUIXCceINolX1kUyyf43ZF-rd",
            "https://drive.google.com/uc?export=view&id=1bj0b5ZfKocGsBVH6Kbw5RuJnEhusWO-d",
            "https://drive.google.com/uc?export=view&id=1jvaxtkKqGLywRSbivcml32MxWZc-Y_cD",
            "https://drive.google.com/uc?export=view&id=1jvaxtkKqGLywRSbivcml32MxWZc-Y_cD",
            "https://drive.google.com/uc?export=view&id=1qTJ7tgsx6mzsIL7OpHBEDlMDtJH1wnZT",
            "https://drive.google.com/uc?export=view&id=16jpo4QLo0k7W9hkeRVXGla95hXLkUs5p",
            "https://drive.google.com/uc?export=view&id=1x19xJX6c4DOpbeesyd0ATuF0Xj6faIjx",
            "https://drive.google.com/uc?export=view&id=1iNIwwiejEPShgHiyD70LQeSUBDHslMws",
            "https://drive.google.com/uc?export=view&id=1CLi-XuWRZ5L149SZ1VdrKuvq20LAV_aQ",
            "https://drive.google.com/uc?export=view&id=1Z-aqT7svpnua4o4UqoG1MXdJPp3PcjHE",
            "https://drive.google.com/uc?export=view&id=1JwqwHhcR7ZLrLs3oqcbZgzyjirNvemJe",
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
                "kesan": "abangnya baik dan ramah",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "kakaknya mirip arafah lucu banget",
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
                "kesan": "Abangnya ramah banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik banget sering becandaan",
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
                "kesan": "Abangnya baik banget",
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
                "kesan": "Abangnya baikk banget",
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
                "nama": "sherena Florencia",
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
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "Belum Tahu",
                "asal" : "Bandar Lampungku",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "abangnya baik dan ramah",
                "pesan" : "semangat terus kuliahnya bang"
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Energik dan cepat akrab dengan siapa aja",
                "pesan" : "Tetap semangat bang"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah dan selalu terlihat ceria.",
                "pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "Murah senyum dan enak diajak ngobrol",
                "pesan" : "Tetap semangat dalam menjalani perkuliahan, Kak"
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "28",
                "sosmed" : "henryferdianto",
                "kesan" : "Humornya unik dan bikin suasana cair.",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
            
      ]

        display_images_with_data(gambar_urls, data_list)
    mikfes()
        if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_sljO0hUkuvsTc_1YFJMxqkSnIWwcfDb",
            "https://drive.google.com/uc?export=view&id=1PQMTyOytX3ydqMs7wJZxEFByqmvxFFl1",
            "https://drive.google.com/uc?export=view&id=1m1deWMiqdyE9VJMZO3vzVOjLQvFkBWwf",
            "https://drive.google.com/uc?export=view&id=1H1e5qIEdVbn5YWnV4kQkMQgt5r9KFNMR",
            "https://drive.google.com/uc?export=view&id=1IbbiH7czF16o8TNy85D0R3kWsJZRitpx",
            "https://drive.google.com/uc?export=view&id=1-SLRGklfLxPxjRY48GHuljAkL1HbqWLq",
            "https://drive.google.com/uc?export=view&id=1TUPXtQW0PG_wK_n3tQIpR9G8LF5HekFw",
            "https://drive.google.com/uc?export=view&id=10PPsoZQSeVS1bWl5S4nkxYPUCj6_4V6p",
            "https://drive.google.com/uc?export=view&id=1HEhm00V7f14YLGIVeMAo7DGbkRuBrDkN",
            "https://drive.google.com/uc?export=view&id=1Z-lrkIES_QRc3IsagpJ2bxmmpOZquPz5",
            "https://drive.google.com/uc?export=view&id=1NMZdxHRoIZzwNT4cJK33tqTX3Md73Ub5",
            "https://drive.google.com/uc?export=view&id=1pnPtbbt_Azbq6t3E6jQV_AnSfkoBNah4",
            "https://drive.google.com/uc?export=view&id=1XQS4pFXFYV_JF39wa0RkQLttSQQOTcK7",
            "https://drive.google.com/uc?export=view&id=1xtM1nMbO7_2otrdVUIkDi2nxKwMLEWYU",
            "https://drive.google.com/uc?export=view&id=1t7_V0o1Gxo5gDhaOuvWv0jNDzesoCqMZ",
            "https://drive.google.com/uc?export=view&id=1C52hlxuA9n8h6kw1IB34F9a9eqLhFxg4",
            "https://drive.google.com/uc?export=view&id=1BgQDyPndCpHSmP_rxw2bKnFSCCE31UaF",
            "https://drive.google.com/uc?export=view&id=1bbNUzgblXH7WnPXpQDnq1RhWgcoU9jBS",
            "https://drive.google.com/uc?export=view&id=1m-xqkqrD0saAtcbvmYppRNWdSSC-Vo-1",
            "https://drive.google.com/uc?export=view&id=1XCX0d7e6cmi9QhbsVeI5l727H147S0CW",
            "https://drive.google.com/uc?export=view&id=1VOuHzGbBHQ59IChv7JniXyPi__RZA1oz",
            "https://drive.google.com/uc?export=view&id=1RDCNryVlyH7LuKD2lRdpCZS4oOmzfPmU",            
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
                "kesan": "kakaknya baik banget ramah, santai, dan keibuan vibesnya",  
                "pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya lucu banget dan cantik",  
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
                "kesan": "abangnya baik banget dan ramah",  
                "pesan":"Semangat terus bang"# 3
            },
            {
                "nama": "Khoirul Mutthoharoh",
                "nim": "1234500",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya imut banget, lucu, dan baik banget",  
                "pesan":"Semoga ceria selalu dan lancar urusannya kak"# 4
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
                "kesan": "bang bima keren banget, ramah, dan baik",  
                "pesan":"Semangat terus bang kulaihnya semoga lancar selalu"# 8
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Bandar Lampung",
                "hobbi": "lihat lihat perumahan ",
                "sosmed": "@bimo_arkana",
                "kesan": "abangnya baik dan ramah",  
                "pesan":"Semangat terus bang"# 9
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal":"Ikut Kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi Idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya ramah, lucu, dan ceria",  
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
                "kesan": "Kakaknya baik banget, waktu ngobrol juga asik banget",  
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
                "kesan": "Kakaknya imutt banget gemes dan ternyata punya kembaran!!",  
                "pesan":"Semangat terus kak kuliahnyaa"
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
                "kesan": "abangnya baik banget",  
                "pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "123450021",
                "umur": "20",
                "asal":"Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "abangnya baik banget dan ramah juga!!",  
                "pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "abangnya baik banget!!",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "abangnya baik banget!!",  
                "pesan":"Semangat terus bang kuliahnya"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "123450093",
                "umur": "Masih muda lah",
                "asal":"Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@jaldii._",
                "kesan": "abangnya baik banget, lucu banget!",  
                "pesan":"Semangat terus bang kuliahnyaa"
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
                "kesan": "Abangnya keren banget dan baik",  
                "pesan":"Semangat terus bang menyuarakan aspirasi!"
            },                                                                          
       
            
        ]
        display_images_with_data(gambar_urls, data_list)
   eksternal ()
        
