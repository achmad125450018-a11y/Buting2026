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
    Badan Legislatif()
    
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
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
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
    Badan Kesenatoran()
