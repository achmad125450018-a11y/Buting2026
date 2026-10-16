from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1rQKJe_Zt68A83KD8ywHtxynzHyFWnxh3",
        "https://drive.google.com/uc?export=view&id=1UUb42OuOEfD4fel9_FVInxiU_v2YBkpK",
        "https://drive.google.com/uc?export=view&id=1Yaq6RbQMCJjCDltE8fKGnpUUsCypcuKg",
        "https://drive.google.com/uc?export=view&id=1VexjFKg4cxJvh4VboZS9Qo836WUAtnZg",
        "https://drive.google.com/uc?export=view&id=1I9O_OInTjfCaeMklmbScrIaERp8tXDEb",
        "https://drive.google.com/uc?export=view&id=1mwupEwMqo1IFeRVyyk3MX6NmfMf3tVH_",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "20", "asal": "Medan", "alamat": "Korpri", "hobbi": "Main Game, Futsal", "sosmed": "@jars_mrp", "kesan": "Sangat seru", "pesan": "Semangat terus bang dalam menjalankan tugas dan kuliahnyaaa!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya lucuuu bisa diajak bercanda dan bisa diajak bicara serius", "pesan": "Sukses selalu bang semangat menjalankan tugas dan kuliahnya"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya imut murah senyum", "pesan": "Sukses selalu kak dan semangat kuliahnyaa!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken dan pendiam", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum", "pesan": "Sukses selalu dan semangat kuliahnya kaaakk!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baiiik", "pesan": "Sukses selalu dan semangat kuliahnya kaakaaa!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Baleg", "jabatan": "Ketua Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1enHDKPtCOJOcop2buBK1XrKToVI4xZRu",
        "https://drive.google.com/uc?export=view&id=1sTM68iTeccY1N_HNK8-l67p0X_C-MxML",
        "https://drive.google.com/uc?export=view&id=1fOA1GgkNbl8GD90SDJ2ze3r6E74dWhea",
        "https://drive.google.com/uc?export=view&id=15yg4LkBDNLIK3vtCUcJ5nsH6Q7xXXatv",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1kZAXlYUaPhu0uugLMid1W18_QCr9bdD0",
        "https://drive.google.com/uc?export=view&id=1eMUs2LR1894MEr5geYNnF0PLnFzu2Kdg",
        "https://drive.google.com/uc?export=view&id=1BnqiSFg1OYXtZt_qa4DcN5WY1law1NSn",
        "https://drive.google.com/uc?export=view&id=16DGXpCnk-Edumj3KBfbouhGXh698N3pQ",
        "https://drive.google.com/uc?export=view&id=10iYQkpIOJKCnkXoej6Mzc6R6VL4WAvug",
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
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1nBgLRiaIw9HHjM4X1iJ8bAJFknr4xqSS",
        "https://drive.google.com/uc?export=view&id=163qgyzrWISiEhRRSAC6bD9XwJR1zYAq5",
        "https://drive.google.com/uc?export=view&id=1dfRSs0BjMiXKFI4pluvi7pMKW467s5MQ",
        "https://drive.google.com/uc?export=view&id=1_BnmumkHSgvb52Q2WSzeaLaN5OY25_BZ",
        "https://drive.google.com/uc?export=view&id=1VvAgehftFcbgfMCXXrQ7b8tJiBJpczrl",
        "https://drive.google.com/uc?export=view&id=1EQFGvE0KBRvikwBcY-vzMAHxN9_l5UC3",
        "https://drive.google.com/uc?export=view&id=1rFJy2hRQxpoqC4v0cjfCnEYzQ3_Pfg4I",
        "https://drive.google.com/uc?export=view&id=1Hj0x16wRE9p1HKHBd_f7lmuU8H3x5G9s",
        "https://drive.google.com/uc?export=view&id=1HuvPh-rcPfpZbIshComYyQBSuLq66N2L",
        "https://drive.google.com/uc?export=view&id=1PoQL9uRZmAWRchGHa0cWigYhecVv0LX3",
        "https://drive.google.com/uc?export=view&id=1HO5XYAGzBZ9XiDVa0j5S82s31dBoLsXW",
        "https://drive.google.com/uc?export=view&id=1debXmEkqbMc90mUiMCXKFAFqkaruDtVv",
        "https://drive.google.com/uc?export=view&id=17Ec_HDubmMD4v13Hd4xg0Bp19t8zDHPD",
        "https://drive.google.com/uc?export=view&id=1_ZUoy6n8_pL5lI7iWHVU17pcdmd1OKUl",
        "https://drive.google.com/uc?export=view&id=1chH4Ykv6-yfM-Zg9Qe1VU4KtBGweHneU",
        "https://drive.google.com/uc?export=view&id=1gHn_Qu9N-fahwtXkVfZfuHpXjf5gUCDT",
        "https://drive.google.com/uc?export=view&id=1_ga069Zy0JZExhaclkcNZHkDsaHKiDNf",
        "https://drive.google.com/uc?export=view&id=1h9i8zxq8MTeyQovBL8ztIOcpcOOUB2jo",
        "https://drive.google.com/uc?export=view&id=1r-d0gPCHn6cEQb70YPiSCifB9q3OSCWj",
        "https://drive.google.com/uc?export=view&id=1DoDAEgPCQSvA7hxh-InwWAINe5oYsR60",
        "https://drive.google.com/uc?export=view&id=1RNA9Reg6EkvXzXB8HVzlGXALtCJ5cqzD",
        "https://drive.google.com/uc?export=view&id=15bGwYV3FSBkXi5GJskpuXT7iyMq0i1mP",
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Staf Eksternal", "nim": "123450069", "umur": "21", "asal": "LAMPUNG!!!", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Kakaknya baik, super duper excited kalau ngejelasin", "pesan": "Semangat terus kakk jalani kuliahnya!"}
    ] + [{"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}] * 21
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=192FNfcYuc5q9OsvORkkWWordUqZSqapl",
        "https://drive.google.com/uc?export=view&id=1pclsgM1sJtOcQLA1-DWX1mjKbuw0u4LE",
        "https://drive.google.com/uc?export=view&id=1aR1jv-4z698LHJzCXtSYfip_IEnj83pM",
        "https://drive.google.com/uc?export=view&id=1pJ1l5lKpaB5qaYd99mHBanldCHu6i_wX",
        "https://drive.google.com/uc?export=view&id=1w8q9B9qMhdESsjqIYa0ET0tlrNDJjZ9f",
        "https://drive.google.com/uc?export=view&id=1XioMqKOay16dTBS7ocrfioj9IChE31dK",
        "https://drive.google.com/uc?export=view&id=1qs7jkIZ2XlmG2hqm2ubP4h-5EV4Z67Ft",
        "https://drive.google.com/uc?export=view&id=1CSQKtNQ5GDGDmAji4EJASXHZMh-YWsH8",
        "https://drive.google.com/uc?export=view&id=1whS3EDf9omJIiUUO4oiUVNsNPpP8nvqJ",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1OsZsT1gdVWiL-nRavT_bG7m_CzOyj_Ot",
        "https://drive.google.com/uc?export=view&id=1R-pUvNb3vBVWHkIeeRMEXyD9H65j7b0h",
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
        "https://drive.google.com/uc?export=view&id=181RDGn_iiBENpZJ3iZS9nr3yjrYWps9m",
        "https://drive.google.com/uc?export=view&id=1ov6ukwiBHW2Qjmuh-tIghJCrBfa6I9gN",
        "https://drive.google.com/uc?export=view&id=13UhbqTV9aQt0v7e0cbzGGmVwEeGMHhfp",
        "https://drive.google.com/uc?export=view&id=1l7bYUZYJ-Y8lUzI1Qy6m6x7qlvmTNk7d",
        "https://drive.google.com/uc?export=view&id=16Iol9OOCg7Os0lLjzrel6mePSUns7U9Z",
        "https://drive.google.com/uc?export=view&id=112xLxPZvc6k6KyfJ45AjEtYtq-GCz77O",
        "https://drive.google.com/uc?export=view&id=1VRT1vrrPRgDmctNb1WRQDdx70t81PiBM",
        "https://drive.google.com/uc?export=view&id=1zuSoxDmbkZVw_1fsd_xgA0fd0Zy-ucxy",
        "https://drive.google.com/uc?export=view&id=1ahGBJGBoV8jHfCXMc38IM9yCtURp46ox",
        "https://drive.google.com/uc?export=view&id=1BKnHIuctPE7U52BMiaCe-82R717hDqN4",
        "https://drive.google.com/uc?export=view&id=1LFrxdbHgoSdfY7DyjS9y7gOyIo5XPpC3",
        "https://drive.google.com/uc?export=view&id=1i6ga_nRectbsFAejWQvglEclL3Vqt3go",
        "https://drive.google.com/uc?export=view&id=1S333-oDtAWEbSJpGwmC5uhA4zygR-8KA",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1fF9FEg710knxXzQ1Ws8ddLIHsdQgBFB3",
        "https://drive.google.com/uc?export=view&id=1jOyXAqVy64N9UomdGIacImSIpP7tlQ4v",
        "https://drive.google.com/uc?export=view&id=1d89zyNcITNAjpI6ASmPwVBBd1EA6__CW",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
