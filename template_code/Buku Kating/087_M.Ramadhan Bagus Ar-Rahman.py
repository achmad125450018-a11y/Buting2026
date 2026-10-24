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
            "https://drive.google.com/uc?export=view&id=1JW5Q6J0-l32PUXZ4fmDbIwv-z8uJD-aw",
            "https://drive.google.com/uc?export=view&id=137c5EKVfSQvxD8cQ_htbjel-yHPUU_M5",
            "https://drive.google.com/uc?export=view&id=18Tfshe_-1nTp82E9psDJK0f4nk2r0Ke3",
            "https://drive.google.com/uc?export=view&id=1IvA_nI4wpruLlaCVw1ZL-JnDiMi1K03R",
            "https://drive.google.com/uc?export=view&id=1K3sEk-WQWh1kF9zRNe4ajtM_QR37NRiT",
            "https://drive.google.com/uc?export=view&id=1709lIORxWXXRmt_r0Bk0GcYqI55IYWgy",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sektariatan HMSD",
                "hobbi": "push imo, mencuci",
                "sosmed": "@jars_mrp",
                "kesan": "tegas dan berwibawa bang ginda ituuu",  
                "pesan":"jadi kahim berat bang, semangat menjalankan amanahnya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau, Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Masak",
                "sosmed": "@muhammadaqil1111",
                "kesan": "tegas dan berwibawa juga si bang aqil itu",  
                "pesan":"Semangat yowww banggg dengan amanahnya"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangatloh kakak dengan jabatannyaa"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "keliatannya berwibawa banggg",  
                "pesan":"semangat yaa banggg dengan tugas tugas nyaa"# 1  
            },
            {
                "nama": "Haffsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "lucuuuuu",  
                "pesan":"semangat trs kakkk"# 1  
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450003",
                "umur": "20",
                "asal":"Jawa Barat, Bekasi",
                "alamat": "Airan",
                "hobbi": "Bertemu haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "friendlyyyyyyy",  
                "pesan":"semangat kak dengan tugasnyaa"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=1XNSXzeYpf8dhblsV8pFvjT1yYG18MFhn",
            "https://drive.google.com/uc?export=1i8wsWgHJnUyUvkKDC1tqEzGnEQ82FlmT",
            "https://drive.google.com/uc?export=1CN3B8cT4CHIFU4RDGQbvTJ7osGg-yPzH",
            "https://drive.google.com/uc?export=1DVIWHiNruGq7mzPlTwF-GWQvCVK38lDF",
            "https://drive.google.com/uc?export=1kLzuln39ncDIwiCh-KMUHv8Mtm31ytYx",
            "https://drive.google.com/uc?export=1Fjq65rzSjIOrQ9QKlwVUyA3zyMX62gsj",
            "https://drive.google.com/uc?export=1Cxvy9NgLhTx1JG4GugzjQwYwt2W54xwp",
            "https://drive.google.com/uc?export=1lz9cuT5sq1qIU-jAHOCyRysaQB50LeTv",
            "https://drive.google.com/uc?export=1GR7rcXMVJjBRlD9H0OATbzO8gPng7fy-",
            "https://drive.google.com/uc?export=1VJHORmrZM1NbJmDwTxUtAuLJQrJeRmJn",
            "https://drive.google.com/uc?export=1P7CN9dF8V_-iKQgd2X3VzXS4PDAFbgW9",
            "https://drive.google.com/uc?export=1KG-TG2-t8Yd7qRJm17GpRc53b8qQh4cr",
            "https://drive.google.com/uc?export=1GiBU6W-U9flBGhClMuEM9el3VxQboR0o",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik ",
                "nim": "123450060",
                "umur": "20",
                "asal":"Manado",
                "alamat": "GH",
                "hobbi": "bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sakawang",
                "alamat": "Pelangi",
                "hobbi": "Ngerepeat lagu begin again taylor",
                "sosmed": "@j__eesie",
                "kesan": "lucuuuuu bgtttt",  
                "pesan":"semangat menjalankan amanahnya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton ags, tapi udah tamat",
                "sosmed": "@ddharu_",
                "kesan": "lucu suka nonton agssss",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jatimulyo",
                "hobbi": "Jogging malam hari",
                "sosmed": "@me._kael",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung pesagih",
                "alamat": "sukabumi",
                "hobbi": "minum kopi",
                "sosmed": "@givarooo",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Sumbar,Padang",
                "alamat": "Kedaton",
                "hobbi": "memburu",
                "sosmed": "@afghanisnt_",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kota bumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Ngoding",
                "sosmed": "@jeremia_hm",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym Koleksi Figur",
                "sosmed": "@nagatseee",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Mamuju",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=1SvUi2X7S5FzPLDIa6D-C8taWKWxnLaT7",
            "https://drive.google.com/uc?export=1pVXXQowJfMgINjAz8xzJ3c-lqtnRZ-ND",
            "https://drive.google.com/uc?export=1k_dim-RF2oR2_bYUvek_VkaS1gy-7gt2",
            "https://drive.google.com/uc?export=1p1dYrOozNrHl395tY_Yi4V-MA2pawlIQ",
            "https://drive.google.com/uc?export=1AOn9Xw74XKmhPkp9dRQlf3u8FDZdJCcl",
            "https://drive.google.com/uc?export=1-kCR7qbrTDoMI5fmJMc1_1M817boX-6z",
            "https://drive.google.com/uc?export=1wOIX0pm-lwcBN0yy7qnxTXk-XEB6ptsi",
            "https://drive.google.com/uc?export=1q76Q4DJj7A_B7NJ9Z0iqEPcQwQg7EAwI",
            "https://drive.google.com/uc?export=1hZtnE3Ufye4VSN2AL08TmVeBiW82Qyzq",
            "https://drive.google.com/uc?export=1ijdv9nYdilslXMpnT5x5gyvrz_KOBd_z",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Airan",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "lucuuuuu bgtttt",  
                "pesan":"semangat menjalankan amanahnya kak"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Main badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang nando orgnya lucuuuu",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Pesisir Barat",
                "alamat": "Kota Baru",
                "hobbi": "Sekarang jadi kameramen",
                "sosmed": "@sciia___",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Kedaton",
                "hobbi": "Asrama TB 3",
                "sosmed": "@wielhawny",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Ngerjain dl",
                "sosmed": "@lia.h_264",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "mendokumentasikan bayyes",
                "sosmed": "@aqilazayyaan",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "1244500114",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "Gunung terang",
                "hobbi": "Dokumentasi lanyard datavora",
                "sosmed": "@hazelhandhaka",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang bawang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=15bGfYVoiqTkyGIoMFODDmq_7ee86AllF", #kak arienta
            "https://drive.google.com/uc?export=1wO05b9uvAsLIlSWs8dbwJ81__pFEKG2s", #kak vany
            "https://drive.google.com/uc?export=1vdhGc5xb-gpvsAhAJd_i4KekmDEz8ekG", #bg nobel
            "https://drive.google.com/uc?export=1uZiq2JZhlSoEuxap498rpwUUvqQJYVRa", #bg azmi
            "https://drive.google.com/uc?export=15bGfYVoiqTkyGIoMFODDmq_7ee86AllF", #bg ayake
            "https://drive.google.com/uc?export=1oQX-KuDyYFzU_me1x-a941wk26ysVbIT", #bg caesar
            "https://drive.google.com/uc?export=1_X3sgHjKvC7stBiQ2OFP0uBTLqw3Jpl0", #ka eudia
            "https://drive.google.com/uc?export=10IcvDkUL4bpDfa-0O0TTuaWw0nRTDPUP", #bg haikal
            "https://drive.google.com/uc?export=1q9XtvSbuiZWLb4Opzr-1lJ7u8qoOoY0p", #ka putri
            "https://drive.google.com/uc?export=1p1TKGd8FNwBwwZAsJmh3EcozCYZjqBUx", #ka queenta
            "https://drive.google.com/uc?export=1DXDxXW7BQhrLdTexVII67Y2UW9vvChTy", #bg desman
            "https://drive.google.com/uc?export=1OaLPUeF7Ub-TKOEjHasVSZdu55MyoNia", #ka azzelya
            "https://drive.google.com/uc?export=1q2TCdcQEXFWMLyZKfs0eqzYsBYPJfi4Y", #ka charlindah
            "https://drive.google.com/uc?export=1OPjbd9fsouyIZAKdU3oV4FHPOb3fsj5C", #bg jeremy
            "https://drive.google.com/uc?export=1A5gqa__vCQzrYXhF8ETqvGiqMDXLcYQt", #ka nabila
            "https://drive.google.com/uc?export=1DheYcOlDSOM66lq9fMSgbURJJxfVc7So", #bg rafli
            "https://drive.google.com/uc?export=1aKhDJYIQsEYhcLYCXOA2WFZrykL9mBIf", #ka salavi
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "baik banget",  
                "pesan":"semangat menjalankan amanahnya kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":" Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": " Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek ayam",
                "sosmed": "@ykeall",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Darimana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "123450059",
                "umur": "19",
                "asal":"Rumah Sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": " 123450114",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main Musik",
                "sosmed": "@dsmanhal",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pillates",
                "sosmed": "@azzelytn",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal":"Jakarta pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": " Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": " 124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Salavi Naharani",
                "nim": " 124450090",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "MJatimulyo",
                "hobbi": "Minum air putihr",
                "sosmed": "@afi.nhr",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

if menu == "Minbak": 
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AROZ1ZksKOlTJOIb-wrIeT_kLwakBQ9Y",  # Bang Kevin
            "https://drive.google.com/uc?export=view&id=1Jbn7SV3XcCg_nDfNR6xxAcAvWgR2Z9Co",  # Kak Gusti
            "https://drive.google.com/uc?export=view&id=1rqthI7tWNH-w5ZWL_NwyyHcWXR2SLqOr",  # Bang Ali
            "https://drive.google.com/uc?export=view&id=1yEK3Vur-DrP5cwMuvnfLQKY1mBzyFf2X",  # Kak Ayu
            "https://drive.google.com/uc?export=view&id=1XWFr94HpzeX-EW59CKoDB3tTU7KeJiAH",  # Bang Dafa
            "https://drive.google.com/uc?export=view&id=1Ot_OU6yfsx3yaBf6Zch7PDodxDP_Kgac",  # Kak Salsabila
            "https://drive.google.com/uc?export=view&id=1Z-yvjqn8xAPQFxgO10nJd7h-_zo_HQbi",  # Bang Afdal
            "https://drive.google.com/uc?export=view&id=1uLu_5BA8b_smKxuN4qzuaHMzB1BEmcUF",  # Kak Juwita
            "https://drive.google.com/uc?export=view&id=1NyRHbUsr1hQtDZvpb_Qbqse1T4MyN3yU",  # Bang Ridwan
            "https://drive.google.com/uc?export=view&id=1l85jOa_F-0xbfWfC5onPuD9ywWlwYR85",  # Bang Andra
            "https://drive.google.com/uc?export=view&id=1yKojXNHZk73sCU-61eq-tLVUkqqjHXuY",  # Bang Bryan
            "https://drive.google.com/uc?export=view&id=1B1T25IhCGs1q1zx88EYZ0uGE3KRP1aQw",  # Bang Ghiyats
            "https://drive.google.com/uc?export=view&id=1mRjdtvYnLcZnw3IFfuSQOoRTfIU8Pgbn",  # Kak Indah
            "https://drive.google.com/uc?export=view&id=1yfoBOXzwGgv-1SlhEI0dEqyXVWfweDb9",  # Kak Jacinda
            "https://drive.google.com/uc?export=view&id=1lDvqd8ftwBLQXgCaNkXwJFe_u-Z3GFqH",  # Bang Rafka
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Maluku",
                "alamat": "Panjang",
                "hobbi": "Menari",
                "sosmed": "@kevinaj__",
                "kesan": "Abangnya keren, asik dan cool banget.",  
                "pesan":"Semangat kuliahnya bang, jangan kasih kendor."# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya stylish banget dan cantikk",  
                "pesan":"Semangat jalann kuliahnya kakk, kayak semnagat mendaki."# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abangnya keren dan komuikasinya bagus banget.",  
                "pesan":"Tips komunikasi yang bagus bang."# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakaknya ramah dan baik banget.",  
                "pesan":"Tetap jadi orang yang ramah dan bai hati ya kak."
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Kelihatan pendiem tapi lama kelamaan asik.",  
                "pesan":"Suka mancing di mana bang?"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya softspoken banget dan ramah ke kami.",  
                "pesan":"Tetap semangat dan jangan menyerah kak."# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Pendiem dan kayaknya suka jajan ya.",  
                "pesan":"Pernah surving di mana bang? Tipsnya sonhg."# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknya asik, ramah tapi kayak mirip sama seseorang di minbak.",  
                "pesan":"Tips jago main basket dong kak biar jago kayak kakak."# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Abangnya keren dan kayaknya santai banget.",  
                "pesan":"Ajakin nonton Fadyl Badminton juga."# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Abangnya lucu, mau aja diajak pose imut.",  
                "pesan":"Semangat terus bang jalanin  perkuliahannya bang."# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya pendiem banget sihh.",  
                "pesan":"Tips biar bisa tetap diem dan tenang di situasi yang gedebak-gedebuk."# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124....",
                "umur": "..",
                "asal":"...",
                "alamat": "B...",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Abangnya kayak pendiem auranya, tapi ternyata asik parah.",
                "pesan":"Semangat terus bang, jangan main game mulu."# 1  
            },
            
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakaknya cantik dan kayaknya anak olharaga banget.",  
                "pesan":"Tips semangat berolahraga."# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakaknya asik, ramah dan murah senyum banget.",  
                "pesan":"Nggak capek ramah terus kak?"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya pendiem dan pemalu ya.",  
                "pesan":"Semangat berolahraga bang. Salam olahraga!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()

    
