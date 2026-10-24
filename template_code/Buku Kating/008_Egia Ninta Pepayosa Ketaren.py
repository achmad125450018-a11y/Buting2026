# 008_Egia Ninta Pepayosa Ketaren.py
from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

# ============================================================
# MENU CONTENT
# ============================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1OZ90dYQxs9qhwjS1IPjwAI8hPVZ3JZD-",
        "https://drive.google.com/uc?export=view&id=1PhDbGoXVKxccssC8wPlA61diRd4pNgf_",
        "https://drive.google.com/uc?export=view&id=1yuqzTRWDLty1-ujD5pVts539JmAU1ARo",
        "https://drive.google.com/uc?export=view&id=1OVtrdQ9DYO5r6LoJuapZb67S55IKmYXk",
        "https://drive.google.com/uc?export=view&id=1gPzMBXa36KLARfOs2jXYK4y_eozaEUbt",
        "https://drive.google.com/uc?export=view&id=1xXPJnwo_MRQhECTUKrncNcwc5vFvLvE6"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan suksek selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya sof spoken, lucuu", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk", "pesan": "Sukses selalu dan semangat kakkk!!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
         "https://drive.google.com/uc?export=view&id=1K3APaB-ogB1cG988B3FWPiHR6J4qNaT0",
         "https://drive.google.com/uc?export=view&id=1fEqWzilkD0Z2gGVvlDVkjyfkvUL2Pvi0",
         "https://drive.google.com/uc?export=view&id=1D7goVhrmAdDUtKtLvjIk4L1vvvQ4SiD3",
         "https://drive.google.com/uc?export=view&id=1IiQewwd3HBrczU5IKMbdOYF8TEjP-xKK",
         "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
         "https://drive.google.com/uc?export=view&id=1NGb8jEpFfaQWZHg6JYV01vezOk2S1cd9",
         "https://drive.google.com/uc?export=view&id=1AEIhq1wNtbHTWIOWi2a3fDDFw87rF-Ed",
         "https://drive.google.com/uc?export=view&id=10lIyjmiZzYPjepl1IYiNkt95gFSOUUMe",
         "https://drive.google.com/uc?export=view&id=1nZGRlmzbLvtOQITWaqLq92m3zZBUiYwJ",
         "https://drive.google.com/uc?export=view&id=1fMHnzEjdH9x-3slXFVpo7SIgjAUB2SiL",
         "https://drive.google.com/uc?export=view&id=1bcurpxHcBev5Hft0z3tF3i7q5YO3RFrB",
         "https://drive.google.com/uc?export=view&id=1UkJ5A_eo66m8EJMWyHfgpy2-olBMCoBv",
         "https://drive.google.com/uc?export=view&id=1HNQFtFLEF6c-1X8d9n5J7NDm7oPAEx6y",
         
    ]
    data_list = [
        {"nama": "Anggota Baleg", "jabatan": "Ketua Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1bwy4U200wjwc6YN3tumWFDSW7LunNfmu",
        "https://drive.google.com/uc?export=view&id=1EJBPN6k5XmLVB8xtMNTgo2nWPEQFUkqv",
        "https://drive.google.com/uc?export=view&id=10s33vUvU34kLCr8nyL8rNZfM1k-Z1WCK",
        "https://drive.google.com/uc?export=view&id=1R77leJE5k8iATcKwvKFiw5nCmq-Ezl8C",
        "https://drive.google.com/uc?export=view&id=1awaYdg6TEcZ2P7E2KkmswUJA4rNVyNoA",
        "https://drive.google.com/uc?export=view&id=17b9QyXuHtyBeEvGLfS-omWt02e5RfT8D",
        "https://drive.google.com/uc?export=view&id=1PQpUNK5ZcmAVQ06WLxg8UlpHGsKoPlEC",
        "https://drive.google.com/uc?export=view&id=1_-uYsuZTVLXJ-RgwHKfzpR4r0otEN3Fx",
        "https://drive.google.com/uc?export=view&id=10IDI69GEY5BwBdxi6wm5L5im0UKDLoen",
        "https://drive.google.com/uc?export=view&id=1H77_72UrtmZXICgAMQHerezZ5vIYyYrp",

    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Senator Mahasiswa", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Senator Mahasiswa", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Senator Mahasiswa", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Senator Mahasiswa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Senator Mahasiswa", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Senator Mahasiswa", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Senator Mahasiswa", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Senator Mahasiswa", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=11gpV6qdfhF-QweCN9rkhCIzuDy9P9waD",
        "https://drive.google.com/uc?export=view&id=1zHcgsAuRM_ssrFjUp7cWqMhzORdBjZWz",
        "https://drive.google.com/uc?export=view&id=1IxLDaIjg1y0USqbb4jxHeJ-OtDXByknW",
        "https://drive.google.com/uc?export=view&id=1XU1wxQ2LwwcGTIVG9HJdP_n1wWoQhu49",
        "https://drive.google.com/uc?export=view&id=15fCy7cH0XZQ-FystUV6Db522vY2wyXjE",
        "https://drive.google.com/uc?export=view&id=1Q3zDq_gkf-L-rNNJ1o8Z2KpaP478pBdS",
        "https://drive.google.com/uc?export=view&id=1OmD-pPuMenMVvFxwvedhpg4d7f3PUVS1",
        "https://drive.google.com/uc?export=view&id=1AjzhTBiZ98CnTjp4xLhuo8OQmtlqyAvR",
        "https://drive.google.com/uc?export=view&id=1mipAyg58x9N1gtJUgg3VDr5sNAuB_dbJ",
        "https://drive.google.com/uc?export=view&id=1NXhEpZz8Ex7NtKqliQ1MYAO3iQ1jmWSq",
        "https://drive.google.com/uc?export=view&id=1ZN73joBSJaKv8nQzOGyR3eWdKTcbJnqW",
        "https://drive.google.com/uc?export=view&id=1v3_y7uWYuiE_bE2ZxvfbVaOe6FteiBL9",
        "https://drive.google.com/uc?export=view&id=1q1VvlqdASswyOhluNkBHNeezE__Jhm0z",
        "https://drive.google.com/uc?export=view&id=1n5kcXRx7wkgNHtrDzd0r3OULxsXE2hAH",
    ]
    data_list = [
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = [
         "https://drive.google.com/uc?export=view&id=1aMlbW-y2Yk6woTnUd8IINyhJwTN5EwaI",
         "https://drive.google.com/uc?export=view&id=1pi5nDGnwVW_jcznF9C6CQelcbhmJ8cXa",
         "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
         "https://drive.google.com/uc?export=view&id=1MliK-HTQGjpZ3-DSAqAspkunyfkMbObP",
         "https://drive.google.com/uc?export=view&id=1McXh_tJ8D-kjrZZWw4byoWl6JF2cx9W7",
         "https://drive.google.com/uc?export=view&id=1nDjL2DvUaduudxinJBdBnldk6PiuTgwq",
         "https://drive.google.com/uc?export=view&id=1nq1PFhp4gLle5wFwsom0FLUE98YXusFC",
         "https://drive.google.com/uc?export=view&id=1hHu5Or0psvMYnu73lxdG35ubzW22YCCD",
         "https://drive.google.com/uc?export=view&id=1rJk0qMbKl-0rGJWYADFWJpx9uZcpnmxT",
         "https://drive.google.com/uc?export=view&id=1Sa8sVuGZ_5A1t2dzp0e9KNiYjEfgL7Un",
         "https://drive.google.com/uc?export=view&id=1iM3Avpu0kr-fiCiXQasfmPrmunGve7QJ",
         "https://drive.google.com/uc?export=view&id=1vKZ26lqcXWWsBRMHr5dJQ7jRAnYEPLvU",
         "https://drive.google.com/uc?export=view&id=1rl1liYQ6SFHSBjaXfD8yKzmTb-Vy3DOh",
         "https://drive.google.com/uc?export=view&id=199x7OWNAkY7FRT1QR13kPDhGQhYWNcJ4",
         "https://drive.google.com/uc?export=view&id=1juZp3jgup49ynEjNqZkItLkJP4yBSQFk",
         "https://drive.google.com/uc?export=view&id=1_Lao8CfS6sX3hPcq0NH1IuCz67Bl9vKl",
         "https://drive.google.com/uc?export=view&id=1Zp2S_vUhHG7EXyvQweQruonqAJIbaBWS",
         "https://drive.google.com/uc?export=view&id=1HTXzPckqDeWFQ6IYY4jyNFGaO1sB28jA",
         "https://drive.google.com/uc?export=view&id=1IHN_WgoHWSfoSZhu1rvLvAbpMPV0iFFL",
         "https://drive.google.com/uc?export=view&id=198wDkdmzgpMJSrhE9lol_r9qxblqd5J9",
         "https://drive.google.com/uc?export=view&id=1nkxiz2kk9MVhiza5MGqjawo2VSQ8ZAFG",
         "https://drive.google.com/uc?export=view&id=1t61O78i6va3AG3WFWFdrgGK3DciybiTe",
    ]
    data_list = [
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1s2XoLDNkmd79J8wzApnNqw9wA6lk1-cv",
        "https://drive.google.com/uc?export=view&id=1p8c54qe0t-KydPSN1_njmXyec4iIxPv1",
        "https://drive.google.com/uc?export=view&id=180LnphDPRRURP6I5_axl1o8-rMvM0a7v",
        "https://drive.google.com/uc?export=view&id=1OA-b0s0HelPi3sxZVwL8ClhvTZOd6RwS",
        "https://drive.google.com/uc?export=view&id=10bAdfxrD7ocCcavQarvNOlxpMMwvDIfu",
        "https://drive.google.com/uc?export=view&id=1LGW61YoaqD33BADwm6puWEK6OF5o23ZD",
        "https://drive.google.com/uc?export=view&id=1Wg_IKqKz65eAm9Go4sKAnbBnNVsBWr2J",
        "https://drive.google.com/uc?export=view&id=17gTme8LpUJXymPaVakbNlva-dI-9g-I_",
        "https://drive.google.com/uc?export=view&id=1tY19bSlTXLnJlwfmh06rgIiYNlL5MLUY",
        "https://drive.google.com/uc?export=view&id=1fxkhtAJEXXvdsLWEBLxAzJh__G8RMX0y",
        "https://drive.google.com/uc?export=view&id=1SbfGEpQvEF5JRJOr8eCiNm4fcHe6RL0Y",
        "https://drive.google.com/uc?export=view&id=1CXKxYtEPvKZ7-XB4IcGU8Lt6Meu31efF",
        "https://drive.google.com/uc?export=view&id=1iPjdXfvKW7s0ACiTHMRnV3AibnbNFM3c",
        "https://drive.google.com/uc?export=view&id=1Na9ZnS6uwX_Hq1qJVQuT7m_OeL9WPMJx",
        "https://drive.google.com/uc?export=view&id=1aphZKIhFSh1cXrDmGNNBFrW0168bQOup",
        "https://drive.google.com/uc?export=view&id=1gC-G8jGnV141twsV4142tLba2B0HlDgS",
        "https://drive.google.com/uc?export=view&id=1YU37XRd6LfGjBOCMDxhjje91ifITPXvB",
        "https://drive.google.com/uc?export=view&id=14-bA744kvqPIcYDN4fEYbDuH3SPMmaMd",
        "https://drive.google.com/uc?export=view&id=1rl91DQRXnOId12HESf4-i5g7sTtFaGX5",
        "https://drive.google.com/uc?export=view&id=1Z4-9A7vu0SoSH4V26iOOMWkWce1DiamW",
        "https://drive.google.com/uc?export=view&id=1y6G-InpEMk3i3L1lr8VIjuWy2HZoT7N6",
        "https://drive.google.com/uc?export=view&id=1BlMK8yUPvll8ifkluUTZu87WU-ycClyb",
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Staf Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Murah Senyum", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Nabyla Sharfina", "jabatan": "Staf Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Ramah", "pesan": "Selalu jadi orang baik"},
    ] + [{"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}] * 20
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=10O1Caz42SEbjnXeI9gG2Y4hY_QkgSdU8",
        "https://drive.google.com/uc?export=view&id=1XGvXqgOJb22CgCi9I7HQ9AFcxpPg-IXo",
        "https://drive.google.com/uc?export=view&id=1ooethe_x7ljdmbb7bBzlAGicP2GUawi7",
        "https://drive.google.com/uc?export=view&id=1C2rw5WfpXZffwbCYMj1HvXfDmciKTcHa",
        "https://drive.google.com/uc?export=view&id=1YLIMKJnw_RKujj6JNRBsxIwAzCCwE1r0",
        "https://drive.google.com/uc?export=view&id=1BGH5nzNfUQWJlwOfDWD18NxWMsj23r5i",
        "https://drive.google.com/uc?export=view&id=1OKubH1K9FFAHwaydYatfj6kRsMSrT-Am",
        "https://drive.google.com/uc?export=view&id=1JQPthYyZfaxQMmSnsUgAr8sIJC_nIsLS",
        "https://drive.google.com/uc?export=view&id=1DWF4I9MjG-pigYN6cvamPV8SE044UsSy",
        "https://drive.google.com/uc?export=view&id=16yATY5lIAG_R6SOPDSwI4ESL85i1oEkJ",
        "https://drive.google.com/uc?export=view&id=1UApvD-3wAmTP78jmaS0HBqgJazoewXp9",
        "https://drive.google.com/uc?export=view&id=1bYlhIR1eTZDJ7q6DvhzCtM_WBAVnUhOL",
        "https://drive.google.com/uc?export=view&id=10AQRs6idn65qdb0dRSs5FNZiMAvWDnAe",
        "https://drive.google.com/uc?export=view&id=1SRbQ_POWNIvr75UQCV9ITtzWdNulxY6I",
        "https://drive.google.com/uc?export=view&id=1CGK_JAnrzMLBIsZ8aA4Q-RkOcC8TkAsz",
        "https://drive.google.com/uc?export=view&id=1sW9wnx_3pZyYTBhczlL5mnOepLeG4Fvf",
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "A Farhan Ghani", "jabatan": "Staf Ahli Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Aisyah Khairun Nisa", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Cerine Sihotang", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Jaya Saputra Tamba", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Najla Nursyifa", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Rozak Ramdani", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Teresa Christiani Purba", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Audina Fitria", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Gustin H. Tampubolon", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
    
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1XMls4kh0QcWMIDiVzqaJX1kqhkOVWSzQ",
        "https://drive.google.com/uc?export=view&id=1EEZwTqaefUkPSoAnzgNig0A2nqn3zlaw",
        "https://drive.google.com/uc?export=view&id=1rU8FhlY3OoVrBAzlOyAaaxQ1MQhpmj0O",
        "https://drive.google.com/uc?export=view&id=1z91dbs7Sru4gLs8kP-ExLbWDQ7Ws6cD6",
        "https://drive.google.com/uc?export=view&id=1q_k2LJHBu9tsUNbtGJot6XAVoHGt0h7r",
        "https://drive.google.com/uc?export=view&id=1_Kf5fNwcsxG1oVEJvGDTZvdsGhHXFE0J",
        "https://drive.google.com/uc?export=view&id=1ry-WzKXg9EmgLjPwYH8BhXXe8gpokdjo",
        "https://drive.google.com/uc?export=view&id=18d4v1U8gLpdCA8VWmNIch_OpCwTOirNL",
        "https://drive.google.com/uc?export=view&id=1tzn97c-1KiRhIahSxkP4kSt5kGoe8crl",
        "https://drive.google.com/uc?export=view&id=10m29TXmNnHql0sowOmnuNqGz0WPKt2_P",
        "https://drive.google.com/uc?export=view&id=1a2DLQdH5tqfYSm1k9MMx39i4hmx836pD",
        "https://drive.google.com/uc?export=view&id=1g2nAwUtylUht0-LAByTVUYJ0SrwFtd2o",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
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
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1ulGIf34qaoBzEOYvhPCB6uSvBrz0F9pW",
        "https://drive.google.com/uc?export=view&id=1h8dcFbYl9P8Eo0xmIQtdHPjjXIrgkasq",
        "https://drive.google.com/uc?export=view&id=1MWtuNt7cLjzoqVyIQnJcgQjhC6sruQLR",
        "https://drive.google.com/uc?export=view&id=1pdIVt6ZbCmfYMGMWa0wwrUbjhypQLC9F",
        "https://drive.google.com/uc?export=view&id=1d9ycgjc2PJqjmEt3bw7HorlX0Ma84Rek",
        "https://drive.google.com/uc?export=view&id=1EVU9KZqngak_sG_jW0roDyxBTXkHnAQy",
        "https://drive.google.com/uc?export=view&id=1XRFM0IuJEOLBHofYh5rbEL9OeeWHT4jB",
        "https://drive.google.com/uc?export=view&id=1Ne_GdGDiUeHu4cT4ameZpkjtNfVjcObi",
        "https://drive.google.com/uc?export=view&id=17t6Fk5wpCKhWHRJTijuKBHDeHf1hooFf",
        "https://drive.google.com/uc?export=view&id=1i943gu9P0Hn-4iX3Ff_xs5267MzrNro7",
        "https://drive.google.com/uc?export=view&id=1zxtRxWrcSCuWE1n6UlYl-mVe7jLtEA5y",
        "https://drive.google.com/uc?export=view&id=14SuvEak83yiR3YdQfmtI7W_mSbxL5p9_",
        "https://drive.google.com/uc?export=view&id=1AwlD3RESR9TVy-mKCm3Sc4-U9JRuO8lQ",
        "https://drive.google.com/uc?export=view&id=1FukwdS0qWoZV48NsuvHvJSI36PTsmtF_",
        "https://drive.google.com/uc?export=view&id=1Vnhfi110gNpl3qKW-VfwdXjGjmg54aB6",
        "https://drive.google.com/uc?export=view&id=1MDkamNb-fcmJTpYtGqvCWs-l90BHVmQq",
        "https://drive.google.com/uc?export=view&id=1Pjv83uV75agH_7TtIForfU156O7W8jR9",
        "https://drive.google.com/uc?export=view&id=1m6mewOwuNMcAbijrIln-TAvqfOcGpq_b",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
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
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")
    
elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1silR0Ryhzbsq39uwHuKolYsfgaGyhv6u",
        "https://drive.google.com/uc?export=view&id=1GCdyZhntF9j9E9Fs_9Keev2JTvy7PJyx",
        "https://drive.google.com/uc?export=view&id=18QXf1YlRrk2Ro7yDZik34PIe7elAqbqR",
        "https://drive.google.com/uc?export=view&id=1MAcuTYtIDoH8Fn1Vcmu_VSOXO4ZIdiay",
        "https://drive.google.com/uc?export=view&id=1TbwAFdq0MhsYEqeESeINOcuV6FDMnhBQ",
        "https://drive.google.com/uc?export=view&id=1Tas_IO7W_IWBDhIGghLpodKui88Tbddi",
        "https://drive.google.com/uc?export=view&id=14NvxlhWKdUmu0fi0MrDeddiLA2UTrWBw",
        "https://drive.google.com/uc?export=view&id=1Ub-5L059GFHU1SocfHnst1bWULKDZiAe",
        "https://drive.google.com/uc?export=view&id=13L_9-3DMghSI54YnLgt9_YKJxdmvPApM",
        "https://drive.google.com/uc?export=view&id=1U67liSEUH3ah3llGmySNWwirKIw_Zw3P",
        "https://drive.google.com/uc?export=view&id=1v1K34TXTE_fPDkdFca5LY2sVV48PZZ0_",
        "https://drive.google.com/uc?export=view&id=1biJbOOmJ4pOZWhhDRTXc7oSsJqYECzZB",
        "https://drive.google.com/uc?export=view&id=1VUrn0Ns8lO10h1jSG6VuQl8VG9vsQmHF",
        "https://drive.google.com/uc?export=view&id=1ED7Q3ErtdA6W4RARR7wHX9aGsKKVDukC",
        "https://drive.google.com/uc?export=view&id=1EoQKQ-v5HEB_nM2i0kKxd_eMXfezDHAN"
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
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")

