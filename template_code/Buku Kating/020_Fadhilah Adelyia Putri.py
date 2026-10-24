from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1CxIZrD4d0ndKYYsU5BiLO3dSUujkpGo0",
        "https://drive.google.com/uc?export=view&id=1KABZHicsQhrbKk9Rn-4R7ZnaOv1ERWyK",
        "https://drive.google.com/uc?export=view&id=1cxBQGTmEKr9m4gnUzJUT4qPLaTIKANHy",
        "https://drive.google.com/uc?export=view&id=1SDvdHICaO1zicBACVnFCM4QprM3ho4xQ",
        "https://drive.google.com/uc?export=view&id=1aXFVEo72vZQsK9Jq6wNsSohvOZCPbiMH",
        "https://drive.google.com/uc?export=view&id=1aLJM0YHPVfNX-sYdbhuV0Ao0pB6O8BPw",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abang KAHIM kerenn, baik, keliatan asik tapi tetep serius", "pesan": "Semangat kuliahnya bang, sehat selalu dan dilancarkan segala sesuatunya"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Zikir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya tinggi banget, baik dan keliatan asikk", "pesan": "Semangat kuliahnya bang, sehat dan sukses selaluu"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakak asprak ADS, baik dan murah senyumm", "pesan": "Semangat ngasprak dan kuliahnya kak, semoga sealalu dikelilingi orang baik!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya baik dan softspoken", "pesan": "Semangat kuliahnya bang!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya baik, seru dan murah senyum", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
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
        "https://drive.google.com/uc?export=view&id=1DETQnJqFwGbXP6iy1b1qmrrRkqFUcaVo",
        "https://drive.google.com/uc?export=view&id=11ffq8OLtrk1AP2Gu4I2uvmJVJ-EF_7Ox",
        "https://drive.google.com/uc?export=view&id=1acT3EJxDF8coGEDmghOpmxY7wr5xI7Jn",
        "https://drive.google.com/uc?export=view&id=1e_R4fjRJDmv7N7GcVb-suR3nUAEBEHN0",
        "https://drive.google.com/uc?export=view&id=1kcnzxpSgt3E9ie2dik2UzMtP6hpWa73j",
        "https://drive.google.com/uc?export=view&id=1xp9EL9gvNrq1qlMxGpH_e-EktG-IsHd0",
        "https://drive.google.com/uc?export=view&id=1h3nZYbLt2tvSZ5ykbtqze1cdypQBaeEp",
        "https://drive.google.com/uc?export=view&id=1bgy1WnHxZ2xbbrB9Lufl7hBPjQFAR2LX",
        "https://drive.google.com/uc?export=view&id=1kJC2xhzIoNqAyR0wxLUS-qB_8l4vfRoe",
        "https://drive.google.com/uc?export=view&id=1U8x2-hxZtBQv9Oj1JR-XNil7WdgU1rUD",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Kakaknya KEREN banget, baik dan murah senyumm ", "pesan": "Keep shining kakk dan jaga kesehatan!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Senator Mahasiswa", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya baik, asik", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Senator Mahasiswa", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Abangnya kaya ga asing, baik dan asik", "pesan": "semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Suci Aulia", "jabatan": "Senator Mahasiswa", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Kakaknya keliatan judes tapi aslinya baik banget dan seru poll", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Senator Mahasiswa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Abangnya baik dan asik", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Senator Mahasiswa", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Kakak asprak ADS, baik, soft dan murah senyumm", "pesan": "Semangat ya kak ngasprak dan kuliahnya, semoga lancar dan sukses selalu!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Senator Mahasiswa", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Kak Aqila Mentor MPLS waktu SMP hehe, baik, murah senyum dan asik bangett", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Senator Mahasiswa", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Abangnya keliatan galak tapi aslinya baik dan seruu", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Senator Mahasiswa", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Kakaknya cantik, baik, murah senyum dan soft bangett", "pesan": "Semangat kuliahnya kak, sukses selalu dan jaga kesehatan!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
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
        "https://drive.google.com/uc?export=view&id=178LB2DVG8scN41c5vjQXYK_w_juO0vKB",
        "https://drive.google.com/uc?export=view&id=1FcgLXvmHOwCygYuiC97W7hkbHNanwAVn",
        "https://drive.google.com/uc?export=view&id=1667OlZUtAfk_7e4HT3JZKXiTJXhtPTvs",
        "https://drive.google.com/uc?export=view&id=1NISYLMZhNgS-eah01Xay9o1vBMoqRPTW",
        "https://drive.google.com/uc?export=view&id=1WxLNdBh-o0Lzz12xURXFym0yyG0vd2ZR",
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
        {"nama": "Arini Puteri Elandra", "jabatan": "Staf Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Murah Senyum", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Nabyla Sharfina", "jabatan": "Staf Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Ramah", "pesan": "Selalu jadi orang baik"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Staf Eksternal", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Enak diajak ngobrol", "pesan": "Semangat terus bangg"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Eksternal", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Kerenn bangett bang", "pesan": "Selalu jadi orang yang kritis"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Eksternal", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
    ] + [{"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}] * 17
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1BhdfxZ5MTEUPq9pDtFj8U07nSSGXLcaE",
        "https://drive.google.com/uc?export=view&id=1iLUTk8NJ9yCO5_iZSer3xfayWAw9Z4k4",
        "https://drive.google.com/uc?export=view&id=1PiE8wDcFZkLE7owHvdDy0K2QxU_152nK",
        "https://drive.google.com/uc?export=view&id=1Mzv-8XXND22Z11I_GoRdBPAm_bSllyM3",
        "https://drive.google.com/uc?export=view&id=1sPr_B0HCz5k9cl_nN6YDQZA7QqEFfOuH",
        "https://drive.google.com/uc?export=view&id=1Dpzbrpi38aldg2HM3hXKiunizhV-5zAu",
        "https://drive.google.com/uc?export=view&id=1VrNMk75wRwaxnLPHmQtqt4oM6GlJ5XPx",
        "https://drive.google.com/uc?export=view&id=1YDRhkY73wzh8JOBAZ29QfxHDiISzewJz",
        "https://drive.google.com/uc?export=view&id=1VSvp0Gd1U6T_xDZc0cV6hDHPmyDTpr0s",
        "https://drive.google.com/uc?export=view&id=1zoV9doobRoVqoZYeKGYiffNoTIsJjI-L",
        "https://drive.google.com/uc?export=view&id=1Zk0aamzxvHUOhgcqDNca7Ib5JR2AJCka",
        "https://drive.google.com/uc?export=view&id=1_W_xaP5R0DpbJVOP1Gsw2brnZZP2lqp4",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Abangnya baik banget, keliatan enjoy, dan murah senyum", "pesan": "Semangat Kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Kakaknya baik, seru, dan bisa mencairkan suasa", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Kakaknya baik banget, seruu, dan dan ramah", "pesan": "Semangat ya kak kuliahnyaa, sehat dan sukses selalu!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Abangnya keliatan introvert, tapi ternyata engga juga", "pesan": "Semangat kuliahnya bang!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat kuliahnya ya kakk!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf SSD", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Bang Iqbal asprak ALPRO, abangnya baik dan asik bangett", "pesan": "Semangat kuliahnya bang, lancar dann sukses selalu!"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat kuliahnya kakk, lancar dan sukses selalu!"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Kakak Asprak ALPRO, kakaknya baik dan seru poll", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Abangnya baik dan soft banget, positif vibes", "pesan": "Semangat kuliahnya bang, lancar dan sukses selalu!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "Abangnya baik banget", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Kakanya baik dan murah senyum", "pesan": "Semangat kak kuliahnya, sehat dan sukses selalu"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Kakaknya keliatan jutek tapi aslinya baik banget, asik dan murah senyum", "pesan": "Semangat kak kuliahnya, lancar dan sukses selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1L6q29YL71uErYyYaiqVXr5F1gUyHoL2V",
        "https://drive.google.com/uc?export=view&id=1UFZla3EbVvVtXXRVNoJNkvivlhh5Tn2W",
        "https://drive.google.com/uc?export=view&id=1Zf3cdGtDr8z5Ppgib-BwKs8Rme0qtmsC",
        "https://drive.google.com/uc?export=view&id=1naClJRDBxvaJikDlCziPDvGQGl1W3BYZ",
        "https://drive.google.com/uc?export=view&id=1oFLAn17vPp1Vb7FZbyHmiZTOcZToH2jV",
        "https://drive.google.com/uc?export=view&id=18Se0uK_CdPI9ln8LejNrDW9UWBaauV2i",
        "https://drive.google.com/uc?export=view&id=1yrSebZrNjlm8faL6kooOqXS7DXLg1Joh",
        "https://drive.google.com/uc?export=view&id=1kJEe2TmZtmv_krPiYaFC0Fk05TSTgx3s",
        "https://drive.google.com/uc?export=view&id=1jjkDjpTRaxio1dcGpBiGbQCm1ykJ_WbY",
        "https://drive.google.com/uc?export=view&id=1QLfaIFrxUofHm3XYiI0f9Xa6jciuTafT",
        "https://drive.google.com/uc?export=view&id=1hFyr6RHpC1ZiO_TtfP1nku03WYjNYQJQ",
        "https://drive.google.com/uc?export=view&id=1Ru_F8iLPsD0ndLJKjw9UgV0BZzbBwnoq",
        "https://drive.google.com/uc?export=view&id=1lsm71YyT55uJx83BEKwiSOkf1PJO5NaL",
        "https://drive.google.com/uc?export=view&id=1kOAncxa8XK3F7wna9qd-ekHYpcxR-Yem",
        "https://drive.google.com/uc?export=view&id=1Qs9u6GjeC2dLfZPGdR0lufvMQMuCvfFv",
        "https://drive.google.com/uc?export=view&id=1lhYkERzKQ4pzjyvrCceg80TwebZsGJ1-",
        "https://drive.google.com/uc?export=view&id=1buGWtvPT6o5hoi7-AqkPAWlAsiklO9zX",
        "https://drive.google.com/uc?export=view&id=119ADDJ1GijRQPu5RV0E09bWf8mWBtNXA",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kak Nayla kerenn, baik bangettt, soft dan positif vibes!", "pesan": "Semangat yaa kak kuliahnya, terus berkembang dan jaga kesehatan!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kak Donna baik banget, ramah, dan murah senyum bangett!", "pesan": "Semangat kuliahnya kakk, stay humble!"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Bang labo baik banget, suka bercanda dan asikkk polll", "pesan": "Semangat TA nya bang, semoga dilancarkan dan sukses selaluu!"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kak anasss, baikk bangett, ramahh, dan seruu poll ", "pesan": "Semangat yaa kak kuliahnyaa, sehat dan sukses selalu, stay amazing kak anass!!"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kak felis keliatannya pemalu tapi aslinya enggaa, lucuu, baikk banget dan pastinya seru bangett", "pesan": "Semangat yaa kak kuliahnyaa, semoga sellau dikelilingi orang baik, keep shining kak feliss!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Bang Razan semi introvert gitu, tapi aslinya asikk dan baikk bangettt", "pesan": "Semangat bang kuliahnyaa, sehat dan sukses selaluu!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kakaknyaa baikk dan murah senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kakaknya baikk, murah senyum dan ramah bangett", "pesan": "Semangat ya kak kulliahnyaa, happy selaluu ya kakk!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat yaa kak kuliahnyaa, sehat selaluu!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kak Bunga baikk, murah senyum dan seruu bangett", "pesan": "Semangat kuliahnya kakk, stay humblee!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kakaknya baikk, murah senyumm dan keliatan asikk", "pesan": "Semangat yaa kak kuliahnya, sehatt selalu!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kakaknya lucuu, baik, dan soft bangett", "pesan": "Semangat kulliahnya kakk, happy selalu yaa!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "kakaknya baikk dan murah senyumm", "pesan": "Semangat kak kuliahnyaa, semoga lancar dan sukses selaluu!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Abangnya baikk dan kalem bangett", "pesan": "Semangat kuliahnya bangg, always happyy!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kakaknya baik, dan mura senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kakaknya baik dan softt", "pesan": "Semangat kuliahnyaa kak, sehat dan sukses selaluu!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")
