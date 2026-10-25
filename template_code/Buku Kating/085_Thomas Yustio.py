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
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10wzjIFki5a9Yv2G8KIJ37Uaai_swTbNq",
            "https://drive.google.com/uc?export=view&id=1ndSPeTo0eCoLWCIzSLzx3uYwkjzfebhf",
            "https://drive.google.com/uc?export=view&id=1e_dvhaOu8O0hG0hEresf2R2DmQ1d9Byd",
            "https://drive.google.com/uc?export=view&id=1Wliw2KHW-fldg161vIjGo3XpRcPvwCn4",
            "https://drive.google.com/uc?export=view&id=1hJ5Jk9R_wDkL-JEkVCxxxvtpCfw4onzS",
            "https://drive.google.com/uc?export=view&id=1cnvqy7gx_UdRzk3kGQqVoEtBUdSTSHFW",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kesektariatan HMSD",
                "Hobi": "Push IMO",
                "Sosmed": "@jars_mrp",
                "Kesan": "Saya melihat bang Fajar sebagai sosok kahim yang tidak hanya pintar berorganisasi tapi juga dalam akademik",  
                "Pesan":"Semoga bang Fajar selalu diberi kelancaran dalam menjalankan tugas akhir dan sukses sebagai kahim"# 1
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobi": "Dzikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Bang Aqil orangnya baik, asik dan memberikan kesan yang sangat positif selama saya berinteraksi dengan bang Aqil seperti saat wawancara.",  
                "Pesan":"Semoga bang Aqil selalu diberikan kelancaran dalam perkuliahan, pengerjaan tugas akhir, dan dapat menyelesaikan amanat sebagai sekjen"# 1
            },
            {
                "Nama": "Efi Defiyati",
                "NIM": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@eefffiidefi",
                "Kesan": "Kak Efi orangnya ramah, baik dan murah senyum.",  
                "Pesan":"Semoga kak Efi selalu diberikan kelancaran dalam perkuliahan, pengerjaan tugas akhir, dan kegiatan lainnya"# 1
            },
           {
                "Nama": "Qois Olifio",
                "NIM": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobi": "Mainin surat",
                "Sosmed": "@qoisolifio_",
                "Kesan": "Bang Qois orangnya ramah, baik, dan asik ",  
                "Pesan":"semangat terus kuliahnya bang, jangan lupa jaga kesehatan"# 1
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "NIM": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Bertemu Luluk",
                "Sosmed": "@hafsafazilahh",
                "Kesan": "Kak Hafsa orangnya baik, asik, dan ramah sekali",  
                "Pesan":"semangat terus kuliahnya kakak jangan lupa tersenyum dan sehat selalu"# 1
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM": "123450004",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobi": "Keliling Balam",
                "Sosmed": "@luthhifiarmdhni",
                "Kesan": "Kak Luthfia orangnya bak, asik, dan ramah banget",  
                "Pesan":"semangat terus dalam kuliah dan organisasi, jangan lupa jaga kesehatan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YwXU3-HhvqYMd0RaQUnXp2hQcLFlkjDZ",
            "https://drive.google.com/uc?export=view&id=1mQ_4_p-17pm-ILkbdcqj1zC4Xnfq5Ilu",
            "https://drive.google.com/uc?export=view&id=13Njv7jm9vovmFlVDph7NCvJfUXMahjZk",
            "https://drive.google.com/uc?export=view&id=1TkbDnsbJ2SFdYCoj7TN_UIIsSTCSnp9X",
            "https://drive.google.com/uc?export=view&id=1k7LbPvTu-hX8M5r8bk2Yrq9iiCsyi4TW",
            "https://drive.google.com/uc?export=view&id=168sFJITV6TtXBHGudTcLx4AiSrrytBiL",
            "https://drive.google.com/uc?export=view&id=17yYpt5eK5yhfLZVR0tVnKpxx34F2uC3O",
            "https://drive.google.com/uc?export=view&id=1VYPb6Qr74i_ZPho0MQZlI71jv7xZ8gSv",
            "https://drive.google.com/uc?export=view&id=1oRzCRfshVOoiSkwMitAara-AZ0KsAdsT",
            "https://drive.google.com/uc?export=view&id=1Zqwtf8ndzFeXlWNbxV_P6-0Gxe3VtUx3",
            "https://drive.google.com/uc?export=view&id=1JeSTltDuSea0QiTPFPGqErr3m6kknU_9",
            "https://drive.google.com/uc?export=view&id=1eHu8KVNnZ-teCZF4Q4Bw2UWi8-gLZ02g",
            "https://drive.google.com/uc?export=view&id=1lS6NKcLB1Ho8J88qN-LBjaZsM55ZcYTX",
        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450020",
                "Umur": "20",
                "Asal":"Cambridge",
                "Alamat": "GH",
                "Hobi": "wawancara",
                "Sosmed": "@@imridhomanik",
                "Kesan": "Bang Ridho orangnya pintar, banyak pengalaman, dan menginspirasi",  
                "Pesan":"Semangat terus bang menjadi kabaleg bagi kami, dan semangat terus kuliahnya"# 1
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "NIM": "1234450085",
                "Umur": "19",
                "Asal":"Singkawang",
                "Alamat": "Pelangi",
                "Hobi": "Dengar lagu duhai sayang",
                "Sosmed": "@j__eesie",
                "Kesan": "Kak Jue orangnya asik, baik, dan pengertian",  
                "Pesan":"Semoga kak Jue sehat selalu, semangat, dan sukses di semua hall"# 1
            },
            {
                "Nama": "Dharu Cahyo",
                "NIM": "123450023",
                "Umur": "19",
                "Asal":"Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Bang Dharu orangnya asik, keren, dan pintar apalagi exvoltas yang keren bangett",  
                "Pesan":"Semangat PKM nya bang, semoga sukses dan menular ke kami"# 1
            },
            {
                "Nama": "Ghifaro Ananta",
                "NIM": "123450078",
                "Umur": "19",
                "Asal":"Lampung Barat",
                "Alamat": "Sukabumi Balam",
                "Hobi": "Ngopi tiap hari",
                "Sosmed": "@gifarooo",
                "Kesan": "Bang Ghifaro orangnya keren, kece, mantaplah pokoknyaa",  
                "Pesan":"Semangat terus bang, semoga sukses kuliahnya dan semuanyaa"# 1   
            },    
            {
                "Nama": "Wan Nazwa al Hasti Yuska",
                "NIM": "123450077",
                "Umur": "20",
                "Asal":"Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshaysk",
                "Kesan": "Kak Nazwa orangnya baik, ramah, dan keren banget",  
                "Pesan":"Semoga kakak sehat selalu, sukses kuliah dan himpunannyaa"# 1   
            },    
            {
                "Nama": "Siti Sarifah",
                "NIM": "124450015",
                "Umur": "18",
                "Asal":"Banten",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboiboy",
                "Sosmed": "@syt.rifah",
                "Kesan": "Kak Siti kerenn, aku mau seperti kak sitii",  
                "Pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal":"Cibaduyut",
                "Alamat": "Teluk Betung",
                "Hobi": "Makan Pedas",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Bang Jeremia orangnya asik, keren, dan pintar, dan juga keren nyanyinya",  
                "Pesan":"Semangat terus bang, semoga sukses dan sehat selalu"# 1
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal":"Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Gym dan koleksi figur",
                "Sosmed": "@nagatse",
                "Kesan": "Bang Jona orangnya keren, kece, absolute cinemaaa pokoknyaa",  
                "Pesan":"Semoga sehat terus bang, semangat kuliahnya, gym nya jugaa"# 1   
            },    
            {
                "Nama": "GH Mikael Niko A S",
                "NIM": "124450025",
                "Umur": "20",
                "Asal":"Jabung",
                "Alamat": "Jati Agung",
                "Hobi": "COD Musang",
                "Sosmed": "@me._kael",
                "Kesan": "Bang Niko keren banget, kayak adeknya ezra",  
                "Pesan":"Semangat terus bang semoga sukses di baleg terus sampai tahun selanjutnya"# 1   
            },    
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal":"Kotabumi",
                "Alamat": "Sukarame",
                "Hobi": "",
                "Sosmed": "@syt.rifah",
                "Kesan": "Kak Hani kerenn, aku mau seperti kak Hani",  
                "Pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "124450121",
                "Umur": "20",
                "Asal":"Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Gym dan koleksi figur",
                "Sosmed": "@nagatse",
                "Kesan": "Bang Jona orangnya Monica, kece, Gacor pokoknyaa",  
                "Pesan":"Semoga sehat terus bang, semangat kuliahnya, gym nya jugaa"# 1   
            },    
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Pemda",
                "Hobi": "Nginep di kos Putri",
                "Sosmed": "@sekardnwt",
                "Kesan": "Kak Sekar keren banget, baik dan ramah",  
                "Pesan":"Semangat terus kak semoga sukses di baleg terus sampai tahun selanjutnya"# 1   
            },    
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450020",
                "Umur": "20",
                "Asal":"Kotabumi",
                "Alamat": "Sukarame",
                "Hobi": "",
                "Sosmed": "@syt.rifah",
                "Kesan": "Kak Nisa keren banget, my tutor Metnum juga",  
                "Pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nCvkOIQkGQ5XUSUJJorRcoe3zk57avsv",
            "https://drive.google.com/uc?export=view&id=1K0oWaVNbsM907thwaf-Guq9C9pHd0PE_",
            "https://drive.google.com/uc?export=view&id=1YwXU3-HhvqYMd0RaQUnXp2hQcLFlkjDZ", #bang nando
            "https://drive.google.com/uc?export=view&id=1Zznlj_5MPWnoGDeug5RhSqldO7eDzRWP",
            "https://drive.google.com/uc?export=view&id=1dEOC-0XD37er1jms4JWvXQktynoqN1tv",
            "https://drive.google.com/uc?export=view&id=1YwXU3-HhvqYMd0RaQUnXp2hQcLFlkjDZ", #kak lia hanna
            "https://drive.google.com/uc?export=view&id=156ky8ui-NzbXrcwAjsOHK5A9Z_DyElfx",
            "https://drive.google.com/uc?export=view&id=1QCJVH_7ziS6C790Ygt7RvFt3mJtRQP88",
            "https://drive.google.com/uc?export=view&id=1TNeUxVIgMgyTnRaLDEaEFdZmDYf6xFVJ",
            "https://drive.google.com/uc?export=view&id=1YwXU3-HhvqYMd0RaQUnXp2hQcLFlkjDZ", #kak dwi rahma
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, baik, kalem, keren",
                "Pesan": "Sehat selalu kak, semoga lancar jadi senator dan semangat tugas akhirnya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Abangnya seru, asik, lucu, ramah banget asli",
                "Pesan": "Semangat terus bang, sukses kuliahnya"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya baik, asik, kalem",
                "Pesan": "Semoga selalu dimudahkan bang, seamngat kuliahnya"
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kakaknya kalem dan baik",
                "Pesan": "Sehat selalu kak, semangat kuliahnya"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya asik, keren, pinter juga",
                "Pesan": "Sehat selalu bang, semangat terus juga"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "Kakaknya lucu, asik juga",
                "Pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kakaknya lucu, baik, ramah banget, keren juga, suka bunga matahari",
                "Pesan": "Semoga sehat selalu, sukses kuliahnya, lancar selalu jadi mentor kami, jangan lupa tersenyum"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Abangnya keren, asik juga",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kakaknya cantik, ramah, baik",
                "Pesan": "Semangat terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca Buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cN5Q96sTeM7cxXTY8L0qXvWdvAYXi25s",
            "https://drive.google.com/uc?export=view&id=1_5WIQK_9hyd58qIKnGizdwNA1WOu3OGK",
            "https://drive.google.com/uc?export=view&id=1F6gQrJBHc98hC8jusC9TYvUJ4B89Iwv3",
            "https://drive.google.com/uc?export=view&id=1gnxgVEAPmrY5YgZwwjuJR4RIA4QUd9vm",
            "https://drive.google.com/uc?export=view&id=1eiGXDBFscu3cGxeL_4Hp_7Ri5fs8I-ir",
            "https://drive.google.com/uc?export=view&id=1jHtVAqmZjpYkbLiZ8BXBD0i4M2Tr027U",
            "https://drive.google.com/uc?export=view&id=1WBF99Qf7GPUJsdxzFM4KBgrloK9yp_ra",
            "https://drive.google.com/uc?export=view&id=1CpYDh5rSWvQluhk44XSvMDf3Eqj68UTT",
            "https://drive.google.com/uc?export=view&id=1hBS5Tomew2czpO2TWViwX5c80g5G5KaP",
            "https://drive.google.com/uc?export=view&id=1ci7Azm5p5puIGDrNt_uLzUYSGI9zLul1",
            "https://drive.google.com/uc?export=view&id=1z_0GGjrpQ0eU1iTm0C237CDi_mlWVIUT",
            "https://drive.google.com/uc?export=view&id=1Fu3m8adNWwEttIVxRZ3N63iKO9TYItRN",
            "https://drive.google.com/uc?export=view&id=1JR2bjAIH615C18Q3PjyoUSCHCNrphFys",
            "https://drive.google.com/uc?export=view&id=1OzSUYVQZd255F2lHZ6Q1etXHUQuL-5ep",
            "https://drive.google.com/uc?export=view&id=1w3GJxSI7S4A_b2pkKQQ52pbgEDRa1lE2",
            "https://drive.google.com/uc?export=view&id=1H__K3uK8ERuLlsAxSVpsF0pfheHV0lXN",
            "https://drive.google.com/uc?export=view&id=1ge6WUEE-WmhnMjR2DPs7KbETtd_BuxLu",
        ]
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "NIM": "123450097",
                "Umur": "21",
                "Asal": "Pinggir Pantai",
                "Alamat": "Samping Kost Capo",
                "Hobi": "Ngerjain Anak Kader",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Kak Arienta orangnya baik, dan juga ramahh, asik juga",  
                "Pesan":"Semoga kakak sehat selalu, sukses kuliahnya, dan lancar terus tugas akhirnya"# 1
            },
            {
                "Nama": "Vany Salsabila Putri",
                "NIM": "123450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Pudan Kost",
                "Hobi": "Pacaran",
                "Sosmed": "@vany.salsabilaa",
                "Kesan": "Kak vany orangnya humble, ramah, dan baik juga",  
                "Pesan":"Semoga kak vany sukses kuliahnya dan sehat selalu"# 1
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450023",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Bang Nobel orangnya kerenn, Tegas,dan juga baiik, jago main kartu juga",  
                "Pesan":"Semoga bang nobel selalu diberi kelancaran dan kesehatan"# 1
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal":"Malang",
                "Alamat": "Lapangan",
                "Hobi": "Berantem",
                "Sosmed": "@friezazmi",
                "Kesan": "Bang Azmi orangnya kerenn, baik, dan tegas",  
                "Pesan":"Semoga abang sehat selalu dan lancar kuliahnya"
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450059",
                "Umur": "21",
                "Asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "Alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "Hobi": "Cekek Ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Bang Ayake orangnyaa humble, baik, dan asik saat ngobrol",  
                "Pesan":"Semoga bang ayake diberi kelancaran dalam kuliahnya, dan sehat selalu"# 1
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Pulang Kampung",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Bang Caesar orangnya kereen, Tegas dan Humble",  
                "Pesan":"Semoga bang caesar diberi kesehatan dan kelancaran dalam kuliah dan segala kegiatan"# 1
            },
            {
                "Nama": "Euodia Meiliana Fredita",
                "NIM": "124450029",
                "Umur": "18",
                "Asal":"dari mana aja boleh",
                "Alamat": "Didalam Kamar dibalik pintu",
                "Hobi": "Surving",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Kak Euodia orangnya seru, Tegas , dan juga baik",  
                "Pesan":"Semoga kak kakak seallu sehat dan sukses dalam kuliahnya"# 1
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450032",
                "Umur": "Tinggi Bang Azmi - 155",
                "Asal":"Jambi",
                "Alamat": "Belakang Pemancingan",
                "Hobi": "Tidur",
                "Sosmed": "@_haikaaall",
                "Kesan": "Bang Haikal orangnya kerenn, Tegas dan baik",  
                "Pesan":"Semoga bang haikal mencapai target dan segala keinginannya, sehat selalu juga"# 1
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450029",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "Oiya Cefa",
                "Hobi": "Jalan kaki gaboleh naik gojek",
                "Sosmed": "@putrimannaa",
                "Kesan": "Kak Putri orangnya baik dan ramah sekali",  
                "Pesan":"Semoga kakak sehat selalu dan sukses selalu"# 1
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "19",
                "Asal": "Rumah sakit",
                "Alamat": "Depan pemancingan",
                "Hobi": "Makanin anak ayam",
                "Sosmed": "@quenntanaabilaa",
                "Kesan": "Kak Queenta orangnya baik, humble, dan perhatian",  
                "Pesan":"Semoga kak queenta selalu sehat, dan sukses dalam perkuliahannya"# 1
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "23",
                "Asal": "Nias",
                "Alamat": "Airan",
                "Hobi": "Main musik",
                "Sosmed": "@dsmanhal",
                "Kesan": "Bang Desman orangnya kerenn, dan juga asikk, serta baikk",  
                "Pesan":"Semoga bang desman selalu sehat, dan dilancarkan selalu"# 1
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kak Azzel orangnya humble, dan juga baik banget",  
                "Pesan":"Semoga sehat selalu, dilancarkan selalu segala urusannya"# 1
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450041",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cendrawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlln",
                "Kesan": "Kak Charrlindah orangnya baikk, dan juga ramah banget ke kami",  
                "Pesan":"Semoga kak charlindah sukses terus, dan dilancarkan segala urusannya"# 1
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "NIM": "124450111",
                "Umur": "17",
                "Asal":"Jayapura",
                "Alamat": "RS airan",
                "Hobi": "Nonton a day in my life",
                "Sosmed": "@jemarrro",
                "Kesan": "Bang Jemar orangnya kerenn apalagi saat lagi damaskus",  
                "Pesan":"Semoga bang jemar sehat selalu, sukses dalam perkuliahannya"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal":"Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main Roblox",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kak Nabila orangnya humble, dan juga baik",  
                "Pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan, sehat selalu, dan sukses selalu dalam urusan dan kegiatannya"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "18",
                "Asal":"Sibolga",
                "Alamat": "Belwis",
                "Hobi": "Membaca peraturan rektor",
                "Sosmed": "@dearrfkvmfl",
                "Kesan": "Bang Rafli orangnya humble , baik, dan juga ramah, asik juga",  
                "Pesan":"Semoga bang rafli selalu sehat dan lancar selalu segala urusannya"
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@afi.nhr",
                "Kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh banget",  
                "Pesan":"Semoga kak salavi selalu sehat, sukses, dan lancar terus segala urusannya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1r0XuZMS6UQssdXSxNbycuWgiCbW7NqX6",
            "https://drive.google.com/uc?export=view&id=1d9C-2cdh1ZCbFR8N1R8_HCGCtNW1mkQL",
            "https://drive.google.com/uc?export=view&id=1J1p5o7DwFwHjfajSIIErN0VkP6yMZ-j6",
            "https://drive.google.com/uc?export=view&id=12EmMZoZe0QukMt7eJpYSkMoCmWIh9Ct5",
            "https://drive.google.com/uc?export=view&id=1K6UaU1GhkbaxvlTVp1iklAtlCCCzR4zS",
            "https://drive.google.com/uc?export=view&id=1OOGgZ0ZafofSqMjkzDDdXB96rNVGzEuw",
            "https://drive.google.com/uc?export=view&id=1MniMvn3k8O15Yyr1RkTfXExUWu7ShHwf",
            "https://drive.google.com/uc?export=view&id=1W4Wt9XyX4QbuGGiaPNKHI309vCp8WU00",
            "https://drive.google.com/uc?export=view&id=1f-YeYlba9xd7Sjb0W-SlWmhQU2rCn0X8",
            "https://drive.google.com/uc?export=view&id=15_LY9MZ-zmCMsi871AT25-KbdT1M4DZm",
            "https://drive.google.com/uc?export=view&id=1wIQOhXZf1yiX1puqMWZznmH2p8sF4oTF",
            "https://drive.google.com/uc?export=view&id=1l7rjTIUDIhJhDEQaytvUvqHXwBA5qV7Q",
            "https://drive.google.com/uc?export=view&id=1R0MS1k1yrFFnirFU-aYwJ18JTRD6MMI8",
            "https://drive.google.com/uc?export=view&id=1DTWuMTusd2yWzlSDYimEz889QNv5T0uZ",
            "https://drive.google.com/uc?export=view&id=1QATLERM9ERQ3fbr-k9KbJr7yXEXeaWB6",
            "https://drive.google.com/uc?export=view&id=1LNQghMWslXOOZb3xnoKs9PZ5pX3-d4d1",
            "https://drive.google.com/uc?export=view&id=1w2rZg2uh2V21OU44xmh32VUfFV_AuwoI",
            "https://drive.google.com/uc?export=view&id=1pVYJ5Q92gCiwIjI3D1R3iNN-C6OITcSb",
            "https://drive.google.com/uc?export=view&id=18lkvVqQ6YlcjzS1YAM23Dev8mF_ZhUV1",
            "https://drive.google.com/uc?export=view&id=1wQo-v6O-VKZL4dxrZDzCXzCbgSC-Xipr",
            "https://drive.google.com/uc?export=view&id=13VzCdUwso2Zbb0NJWDr-ztT4LIDZrQUu",
            "https://drive.google.com/uc?export=view&id=11xpJyU8Ce9DChGu-5R0ThwNP9Jd4olUw",
        ]
        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Abangnya baik, ramah, dan asik, the best banget deh pokoknya.",
                "Pesan" : "Semoga selalu sehat, sukses kuliahnya, dan lancar dalam segala hal, bang."
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "kakak orangnya baik, ramah, dan asik banget banget banget",
                "Pesan" : "Semoga kakak selalu sehat, sukses kuliahnya, dan lancar dalam segala hal, kak."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "Belum Tahu",
                "Asal" : "Bandar Lampungku",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Abangnya baik, ramah, dan asik banget, keren banget bisa jadi duta",
                "Pesan" : "Semoga apa yang bang Fadil capai dapat menginspirasi dan memotivasi saya dan teman - teman yang lain, bang."
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Abang orangnya baik, ramah, dan asik banget, katanya sih calon kadep heheheh",
                "Pesan" : "Tetap semangat dan sukses selalu dalam segala hal, bang."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Kakaknya baik, ramah, dan asik banget, selalu semangat dalam segala hal.",
                "Pesan" : "Semoga sukses kuliahnya dan lancar selalu kak"
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Aktif dan berani mencoba hal baru.",
                "Pesan" : "Terus berani melangkah, Kak."
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Kakaknya Ramah dan selalu terlihat ceria.",
                "Pesan" : "Semoga tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Kakak orangnya baik, ramah, dan asik banget.",
                "Pesan" : "Semangat terus kakak, semoga sukses kuliahnya dan lancar dalam segala hal."
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Abangnya baik, ramah, dan asik banget, selalu semangat dalam segala hal.",
                "Pesan" : "Tetap semangat dan sukses selalu dalam segala hal, bang."
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "_els.a",
                "Kesan" : "Kakaknya ramah, hangat, dan selalu menyenangkan saat berinteraksi.",
                "Pesan" : "Semoga selalu sehat dan sukses dalam segala hal, dan juga tetap tersenyum kak"
            },
            {
                "Nama": "Fadya Izzatul Aini",
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Kakaknya baik dan selalu membantu.",
                "Pesan" : "Semoga selalu sehat dan sukses dalam segala hal, Kak."
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kakaknya ramah, hangat, dan selalu positive vibes",
                "Pesan" : "Semoga selalu sehat, sukses, dan lancar terus dalam segala hal, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Abangnya selalu baik, ramah, dan keren banget.",
                "Pesan" : "Semoga selalu sehat, sukses kuliahnya, dan lancar dalam segala hal, bang."
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Kakaknya baik banget, ramah, dan selalu membimbing.",
                "Pesan" : "Semoga sehat selalu dan tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Abangnya pintar, baik, dan selalu membimbing dengan sabar.",
                "Pesan" : "Semoga selalu sehat, sukses kuliahnya, dan lancar dalam tugas akhirnya bang."
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "FAIZAANJANII",
                "Kesan" : "Kakaknya keren bisa dapat Ozt di TPB, baik juga, dan selalu membimbing.",
                "Pesan" : "Tetap jadi kakak yang baik dan membimbing adik tingkat, semoga sukses kuliahnya dan lancar dalam segala hal, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Abangnya menginspirasi saya untuk belajar lebih giat dan semangat ikut lomba",
                "Pesan" : "Semoga abangnya dapat membimbing adik - adiknya dalam banyak hal seperti perlombaan"
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Bang Hafidz orangnya asik banget, ramah banget, dan pintar dalam membuat website, keren banget bang",
                "Pesan" : "Semoga ilmu web nya menular ke saya dan teman - teman yang lainnya bang."
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Abangnya keren banget, baik, ramah juga, dan bisa konsisten olahraga + akademik rata kanan",
                "Pesan" : "Semoga kami juga bisa se pintar dan se baik abang."
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Kakaknya baik, ramah, dan asik banget kalau ngobrol.",
                "Pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "124450099",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Abangnya keren banget, baik, asik, dan pintar analisisnya",
                "Pesan" : "Semoga ilmu dari abang dapat berguna bagi saya, dan dapat se baik abang juga dalam membagikannya juga."
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "henryferdianto",
                "Kesan" : "Abangnya keren banget, asik, dan ilmunya luas banget, pengalamannya juga pastinya.",
                "Pesan" : "Semoga sehat selalu bang, sukses dalam"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1U5-4DhMQ1YDpT12-G4noTbDmCG0ABfid",
            "https://drive.google.com/uc?export=view&id=1xNz8wJnDtR57sxgt1oY24TYP85Oj29fF",
            "https://drive.google.com/uc?export=view&id=16XuEjuXGneSSkbAB1xeApnQVihmwJHA5",
            "https://drive.google.com/uc?export=view&id=1h-7z6FKN36Dj1_xW9wD9DWEF_hnis2eh",
            "https://drive.google.com/uc?export=view&id=1Rnl1kb7TiSJyKBjJynwFeAEm7CwT5Qqv",
            "https://drive.google.com/uc?export=view&id=13Otio40lZ7U0GrT3wt8a8EuNshrKK-5K",
            "https://drive.google.com/uc?export=view&id=1E4GXFkECfCkWvm0lltSYs9a0DdKTay3C",
            "https://drive.google.com/uc?export=view&id=1jhwzBurn2mRP_kWD5owNrohv84FjJdrf",
            "https://drive.google.com/uc?export=view&id=1kdwLxMssuWt42qDyQVaW_RQYU5lzgw_S",
            "https://drive.google.com/uc?export=view&id=1c3nNKbmqecgJB93g3pjsv7gkjjQyUgTs",
            "https://drive.google.com/uc?export=view&id=1gXeA93pt6BYuYhZNwThRn7TI-3Pqy6bN",
            "https://drive.google.com/uc?export=view&id=1PzMXmnV1y2FMNwuBM4vyBQu4XIL3Ylt9",
            "https://drive.google.com/uc?export=view&id=1OrBwE1HWPGELsF38yU2t5zjkncdmdQOm",
            "https://drive.google.com/uc?export=view&id=1QPFzqkF9KjGHSy4Hg8XVn3g6oUPwItxA",
            "https://drive.google.com/uc?export=view&id=15anWQsfSIOB6lBUwM7pTbvZMgqk28ETp",
            "https://drive.google.com/uc?export=view&id=1Ml_kv1ykJzYhCrZbibWBmb6fTf8F6OUe",
            "https://drive.google.com/uc?export=view&id=1oyqS5cw_vU_9WBO15-7etbOOGLdCxfae",
            "https://drive.google.com/uc?export=view&id=1lZfit_A85bJGc78g61mUZ2kzILwXSPrE",
            "https://drive.google.com/uc?export=view&id=1n2egtU3OUCTn3nrgan_D3mQmpY-p1AVr",
            "https://drive.google.com/uc?export=view&id=10NKF9wCduTHC1uj1btWv-ZL6rRkPehNC",
            "https://drive.google.com/uc?export=view&id=1DQP0Q5v6lbgt1xnGx8Fu99SVVGKmGJjX",
            "https://drive.google.com/uc?export=view&id=1AUvMCPh-rcwAt9jmtsYt5eKpKBjmzJiq",
        ]
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal": "LAMPUNG!!!",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "123450021",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21 Tahun ini alhamdulillah",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "cepuyuh tayun",
                "Asal": "Ikut kadep",
                "Alamat": "Love Earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1  
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat-lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            { 
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "nelson piquet",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },  
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "-",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga Kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@adityatfq",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },            
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "25",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "-",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh Pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
                
            }, 
            { 
                "Nama": "Danil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari Hobi",
                "Sosmed": "@zydddddd__",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "Masih muda lah",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "-",
                "Sosmed": "@jaldii._",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "123450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nZM6DY46uUmhQEqUSqE24Fbh__5wM8wd",
            "https://drive.google.com/uc?export=view&id=1TGBE7Jn5Pt3TpIIbBHtnnSSUc8wI35oM",
            "https://drive.google.com/uc?export=view&id=17V3WkyQM7y4Op1CR404BdkVJn3weIBZ3",
            "https://drive.google.com/uc?export=view&id=1i_y49WoxpzdLCeH8Jxk94V6flqkn7tfv",
            "https://drive.google.com/uc?export=view&id=1QosLKRw7gGUUENEBRCXhRa8Bhg5xeyI2",
            "https://drive.google.com/uc?export=view&id=1_lf8AOUNHi3D6qrwBQbkRqba2HbrsfCa",
            "https://drive.google.com/uc?export=view&id=17RXMkQY_eIGhHmeBVwTSKXre54tGgzyY",
            "https://drive.google.com/uc?export=view&id=1Qow1fc5_6jdfpSF16uVsuGsHj_WA5APA",
            "https://drive.google.com/uc?export=view&id=1Hi_cBFPMGeFk43h2ceofAZbqXZ6aPjar",
            "https://drive.google.com/uc?export=view&id=1L1Ymf8S6pVNjEo5UZfaHQhQSTU8659zh",
            "https://drive.google.com/uc?export=view&id=1q5VCRiqWh4SYi9dDKRp0nYNCm0DgslfB",
            "https://drive.google.com/uc?export=view&id=15qLgJia3n98DXJFqFp6tmH1OzgJn1nOI",
            "https://drive.google.com/uc?export=view&id=1BPVoclvvfWTD4fjnF4Z47r8SRJYWDk7o",
            "https://drive.google.com/uc?export=view&id=1aATPWI4NYWNHTiNe6O6dipi75C5mAgwc",
            "https://drive.google.com/uc?export=view&id=1DfPBf8U7gLo_yWb4QSPokMsYNXrqkHk5",
            "https://drive.google.com/uc?export=view&id=15u9MHTIdueZI7rD-DnhqrDzxmWI-4IVz",
        ]
        data_list = [
            {
                "Nama": "Haikal Fransiskus Simbolon",
                "NIM": "123450123",
                "Umur": "23",
                "Asal": "Bengkulu",
                "Alamat": "Belwis",
                "Hobi": "Merokok",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Bang haikal orangnya seruu banget.",  
                "Pesan":"Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."# 1
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "untung suropat",
                "Hobi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah",  
                "Pesan":"Semoga kak kharisma selalu dikelilingi dengan orang baik"# 1
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobi": "menyapa satpam gedung f",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kak Hanna seru, baikk, lucu ",  
                "Pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"# 1
            },
            {
                "Nama": "A Farhan Ghani",
                "NIM": "123450121",
                "Umur": "19",
                "Asal":"Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Suka motor bukan ngabers",
                "Sosmed": "@farhanghani",
                "Kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "Pesan":"Semoga bang farhan selalu diberi kelancaran dan kesehatan"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobi": "Ngestalker in orang",
                "Sosmed": "@aisyahkhair",
                "Kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali",  
                "Pesan":"Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"# 1
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "....",
                "Asal":"....",
                "Alamat": "....",
                "Hobi": "....",
                "Sosmed": "@...",
                "Kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget",  
                "Pesan":"Semoga kak cerine selalu dikelilingi orang orang baikk"# 1
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "22",
                "Asal":"kisaran city",
                "Alamat": "Pemda city",
                "Hobi": "Balap liar",
                "Sosmed": "@jay_saputra_tmb",
                "Kesan": "Bang Jaya orangnya keren, baikk, dan seru",  
                "Pesan":"Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal!"
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobi": "...",
                "Sosmed": "@...",
                "Kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii",  
                "Pesan":"Semoga semua keinginan kak najla tercapi secepatnya"# 1
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "18",
                "Asal":"lampung selatan",
                "Alamat": "korpri raya",
                "Hobi": "isengin harvin di kelas",
                "Sosmed": "@rozakramdani__",
                "Kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum",  
                "Pesan":"Semoga bang rozak didekatkan dengan hal-hal baik"# 1
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal":"riau",
                "Alamat": "belwis",
                "Hobi": "masak",
                "Sosmed": "@christiani8872",
                "Kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh",  
                "Pesan":"Semoga kak teresa segera mendapatkan semua keinginannya"# 1
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal":"Padang",
                "Alamat": "Perumnas Way Kandis",
                "Hobi": "Main game fps",
                "Sosmed": "@hndfzky_",
                "Kesan": "Bang Hanif orangnya baikk, dan juga asikk",  
                "Pesan":"Semoga bang hanif selalu menjadi yang terbaik"# 1
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal":"sumbar",
                "Alamat": "sukarame",
                "Hobi": "main ke air terjun",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah",  
                "Pesan":"Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"# 1
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450050",
                "Umur": "20",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@Cikamrbn",
                "Kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk",  
                "Pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"# 1
            },
            {
                "Nama": "Gustin H. Tampubolon",
                "NIM": "124450068",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobi": "...",
                "Sosmed": "@...",
                "Kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh",  
                "Pesan":"Semoga kak gustin selalu didekat hal-hal baik"# 1
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Berkuda",
                "Sosmed": "@Muhvnz_",
                "Kesan": "Bang Harvin orangnya baiikk , dan soft spoken",  
                "Pesan":"Semoga semua keinginan bang harvin tercapai secepatnyaa"# 1
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "natar",
                "Alamat": "natar",
                "Hobi": "nginep di rumah kak yollanda",
                "Sosmed": "@snasha._",
                "Kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh",  
                "Pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
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
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LMYHm5agT8vjCJPIJPPWUtQakSy_XYXU",
            "https://drive.google.com/uc?export=view&id=1F8ggVI3UVGsaGTPWvK2z2xI4KNh5io-p",
            "https://drive.google.com/uc?export=view&id=1fGOipCVp4ZDVUnD45HWuz_J95oRUqt1g",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=13gnMamimJ-jVHFXjSC2Ee6kPAMsIts1h",
            "https://drive.google.com/uc?export=view&id=1RDfjBMq4iai13ChWSKdfkT-IlqUvywTl",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1TAqmLKfZBi7UcnbLqf9w8WtDRQGv1ddH",
            "https://drive.google.com/uc?export=view&id=18QPizjpndVMx1L1h8KP0Uh9BcM9ZcMuv",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM": "123450082",
                "Umur": "20",
                "Asal":"Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Musingin TA",
                "Sosmed": "@naylAsalsabilaa._",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": " Donna Maya Puspita",
                "NIM": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobi": " Berenang",
                "Sosmed": "@donNamaya.p",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "NIM": "123450037",
                "Umur": "20",
                "Asal": "Jakpus, Medan, Palembang",
                "Alamat": " Way Huwi",
                "Hobi": " Tong setan",
                "Sosmed": "@noerruuu",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobi": "Nonton F1",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM": " 124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Mancing",
                "Sosmed": "@ felisyanbl__",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM": "124450031",
                "Umur": "18",
                "Asal": "Rumah",
                "Alamat": "Ryacudu",
                "Hobi": " Bully Felisya Nabila Nugroho",
                "Sosmed": "@muh_razan_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM": "123450086",
                "Umur": "21",
                "Asal":"karawang",
                "Alamat": "Airan",
                "Hobi": "nongkrong depan ruang prodi",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Allisha",
                "NIM": "124450019",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukabumi",
                "Hobi": "Gebuk Snare",
                "Sosmed": "@aallishaa.a",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@ alya.rmdhnti",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobi": "Belajar",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM": "123450041",
                "Umur": "20",
                "Asal":"Terbanggi Besar",
                "Alamat": "Airan Raya 1",
                "Hobi": "menulis, membaca",
                "Sosmed": "@n1tg._",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Nazlah Aulia",
                "NIM": "124450054",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Memanah",
                "Sosmed": "@nzlhauly",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Difanya Husakina",
                "NIM": " 124450043",
                "Umur": "Gada yang tau",
                "Asal": "Rumah bapak ",
                "Alamat": "Gedung F",
                "Hobi": "Ngitungin beras di karung",
                "Sosmed": "@difanyhsa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM": "124450061",
                "Umur": "21",
                "Asal": "Surabaya",
                "Alamat": "Sukarame",
                "Hobi": "nyuluh manuk",
                "Sosmed": "@daffascript_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Scroll fesnuk",
                "Sosmed": "@edsel_0712",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": " Lucia Advencia Rachel Nainggolan",
                "NIM": " 124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": " Mencintai Andrew Garfield",
                "Sosmed": "@ luciarachel_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM": "124450112",
                "Umur": "19",
                "Asal": "Jabung",
                "Alamat": "Rajabasa",
                "Hobi": "bobo",
                "Sosmed": "@Xifasky",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k9qOgC8Jy5T1GmbUjAK9l40qnkTaiMEX",
            "https://drive.google.com/uc?export=view&id=16-8EutSEIHVLuoxbcqpoh4dmPpIc_N5L",
            "https://drive.google.com/uc?export=view&id=12mmvbhn_a3CNZBp2-C1CNtnOM5Za_pja",
            "https://drive.google.com/uc?export=view&id=1hHcAzb2_cugwDJkKU4mVTVX7RfpvGPxU",
            "https://drive.google.com/uc?export=view&id=1mPC9ZSdw6bZhOXTJXaEfnf0Yw-u8ngK6",
            "https://drive.google.com/uc?export=view&id=1Y_tCuB9n0PNpex6mCtz-ch-LZTThztwv",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kesektariatan HMSD",
                "Hobi": "Push IMO",
                "Sosmed": "@jars_mrp",
                "Kesan": "Bang Fajar tegas, ramah, dan enak diajak ngobrol.",
                "Pesan": "Semangat terus, Bang! Semoga tugas akhirnya lancar."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobi": "Dzikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Bang Aqil asik, baik, dan gampang diajak diskusi.",
                "Pesan": "Semoga kuliah dan tugas akhirnya lancar terus, Bang."
            },
            {
                "Nama": "Efi Defiyati",
                "NIM": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@eefffiidefi",
                "Kesan": "Kak Efi ramah, murah senyum, dan seru diajak ngobrol.",
                "Pesan": "Semangat terus, Kak! Semoga semua urusan lancar."
            },
           {
                "Nama": "Qois Olifio",
                "NIM": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobi": "Mainin surat",
                "Sosmed": "@qoisolifio_",
                "Kesan": "Bang Qois asik, penjelasannya juga gampang dipahami.",
                "Pesan": "Semangat terus, Bang! Jangan lupa istirahat."
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "NIM": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Bertemu Luluk",
                "Sosmed": "@hafsafazilahh",
                "Kesan": "Kak Hafsa seru, ramah, dan enak diajak belajar.",
                "Pesan": "Semoga kuliahnya lancar dan selalu happy, Kak!"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM": "123450004",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobi": "Keliling Balam",
                "Sosmed": "@luthhifiarmdhni",
                "Kesan": "Kak Luthfia asik, baik, dan bikin suasana belajar santai.",
                "Pesan": "Sukses terus, Kak! Semoga semua target cepat tercapai."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()

# Tambahkan menu lainnya sesuai kebutuhan
