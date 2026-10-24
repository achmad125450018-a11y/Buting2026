from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1MF33XGfLl-7sYejlox9Dh1lDBbKNyhBH",
        "https://drive.google.com/uc?export=view&id=1zriJA0JQx7GLlS_xuNeyzcUiFPkJlrYe",
        "https://drive.google.com/uc?export=view&id=1t1k47hpLRxpzZm-KAvKzmLXB1YGVq3l-",
        "https://drive.google.com/uc?export=view&id=1zriJA0JQx7GLlS_xuNeyzcUiFPkJlrYe",
        "https://drive.google.com/uc?export=view&id=1oQ9vqAU1oiwHts0FKNy_Wz5m3KMIJINQ",
        "https://drive.google.com/uc?export=view&id=18oFNquLlj00f1LcRm3-axyFNfdtr-T3u"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan sukses selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1C10gN2PYRz4ZRpj3sonblSyJFitJrkFg",
    "https://drive.google.com/uc?export=view&id=17IbT5INbX6KtpbzMEgunt9nue_0rxePc",
    "https://drive.google.com/uc?export=view&id=19X9lPgcp4N5SXWi2alhA0rXEk9HLuaxF",
    "https://drive.google.com/uc?export=view&id=1wnsFRcimuIzXstWSB-KhszQ1IZs-wy8R",
    "https://drive.google.com/uc?export=view&id=1KG5fXe6Irike8U5xH6kw5sMk60bdZk7B",
    "https://drive.google.com/uc?export=view&id=1CArdPFmSdiv_cb5lW0JBHCYW8WVVfc58",
    "https://drive.google.com/uc?export=view&id=1TjYMtcuOFAp3RoolaqYoZknxtirdaXEd",
    "https://drive.google.com/uc?export=view&id=1L-MBzn4QhgjZgMI8LbgVPUhPQpu2-pt5",
    "https://drive.google.com/uc?export=view&id=13n6E8YuWbRV_G7udmfvu5LJt_IgeEDuU",
    "https://drive.google.com/uc?export=view&id=19UveBU3fOGPrH2ObqD_Zk1a1tGVRL6E9",
    "https://drive.google.com/uc?export=view&id=19AfRxOVnFY9hqfcFa2x-hV-mbQ-WXaBi",
    "https://drive.google.com/uc?export=view&id=1V_czWPQPHVMdeXjNa0Q7CIPSaqn5XPbl",
    "https://drive.google.com/uc?export=view&id=1WDpyvup3UTsi4g6DHO6UUyVor1AqUrat"

    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Bang ridho keren, asik banget", "pesan": "Semangat TA nya bangg, semoga lancar dansukses selalu bangg"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Juee baik banget, suka kasi kata kata affirmasi buat semangatin adik asuh tpb <3333", "pesan": "Kak Juee semangat TA nya, semoga lancar dan sukses selalu kak <3"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu mapress kereennn,, aduhh when yahh", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "bang niko keren, asikk, ramah", "pesan": "Semangat kuliahnya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kak Syarifa baikk, ramah, murah senyumm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro keren, seruuu, baik", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa baikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah, sama sama coer dengan bias yg sama^^", "pesan": "Kak Hani semangat kuliahnya, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Bang Jeremia keren, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona keren, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk, ternyata setelah kenal asikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, ramah, murah senyum", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selalu kakk"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=11VzVt8f9Qx4fFk1skcRHAOywZRWCXlAM",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=17VznsQr9AORlXVIRaCIZ2wmlDl9ZL8Y5",
        "https://drive.google.com/uc?export=view&id=1uOYFvMB5TWhmw7_Fj7YuPz3tnVvh4ogP",
        "https://drive.google.com/uc?export=view&id=1DQJecL12ZqLClrXPhBhPj_uEHDxO4dSM",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1pcCONjNIecw6rIWKf4tyuuvM-OipZ70_",
        "https://drive.google.com/uc?export=view&id=1PEn0CzWfyMbTY7wdAdXPKN37-ScAZsxn",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
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
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=14yJr_rGZ2s9lXuNCZaFyVNkrvOGTtUZc",
    "https://drive.google.com/uc?export=view&id=1QkKxp3t2wpV270TJVacUSrxDmtNAcgVf",
    "https://drive.google.com/uc?export=view&id=1mv8xU7Yk6peJ9DI13UC1fE09_wS6XZbu",
    "https://drive.google.com/uc?export=view&id=15LjKUOgMpI_3t7ZHVCUQQ_7HgtN-IwQR",
    "https://drive.google.com/uc?export=view&id=1BzTJyOnonLdkdEh9yQpB8ix1BKUmhd-r",
    "https://drive.google.com/uc?export=view&id=1XySP2PYt_h5_9ihHo2LQj0xiiMKcA_v_",
    "https://drive.google.com/uc?export=view&id=17tkY28AYY7p1x0aYYnvRq-MkUfn_4Ulw",
    "https://drive.google.com/uc?export=view&id=1yd109phc9X7V7xC89sz8e87DijyVjhS1",
    "https://drive.google.com/uc?export=view&id=10VWw0F7VwwLShVvyNQm-BXKGrC-LX1Pi",
    "https://drive.google.com/uc?export=view&id=1TW2WL_oqkH_YtvTFbKgohDzuIj6bF1mE",
    "https://drive.google.com/uc?export=view&id=17HAbsVAUstvYTx3TMJuNGGEnbvVpaWGE",
    "https://drive.google.com/uc?export=view&id=1DwBdY1NqFBZRIHfLnf_dj9ycKHyHoL1L",
    "https://drive.google.com/uc?export=view&id=1PDhuf8I0jUm9TsFMdtDuoGHeNOkJpP1D",
    "https://drive.google.com/uc?export=view&id=1Kox2fLr5u3lJTzuBoz88zB8v4I1tJ6w4",
    "https://drive.google.com/uc?export=view&id=1Gc7LkOdSz3aMx0mSxPYNc4MBoaFYsiWX",
    "https://drive.google.com/uc?export=view&id=1Z-n6ldJuBX_Qta_TOJ252YCJESSumD8S",
    "https://drive.google.com/uc?export=view&id=1iQscJd_L7yhJXYyY0UKmSt7HjVQqc5Ky"

    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nobel Nizam F", "jabatan": "Kepala Divisi Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Caesar Ozora Alrando" , "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Charrlindah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Jeremi Marolop P. Situmorang", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1KhXBVqcWPg0oi9XOKiIk_06rzeEL7roZ",
    "https://drive.google.com/uc?export=view&id=1u64R9N6uSAls5jk1XHu0innG_Ja17jkd",
    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    "https://drive.google.com/uc?export=view&id=1mIvC2NA0AcygBbVSlHqH4bYca_L6a2yT",
    "https://drive.google.com/uc?export=view&id=1n5xRq2jpENB0l2nYfqm4JcNJUmfqQGRo",
    "https://drive.google.com/uc?export=view&id=1ID4_KBx8SFYBuyVoqBSHCDj4fNodIfLi",
    "https://drive.google.com/uc?export=view&id=1t8M8zVYUWKjvo3OqaFRvqYPw8EKQ2Sip",
    "https://drive.google.com/uc?export=view&id=14jqgiQwuKU0fIVaWtM3oZGHlcUJgmssZ",
    "https://drive.google.com/uc?export=view&id=1hMEb550iM4ukh5RCLmYNwTCl5jXlgxig",
    "https://drive.google.com/uc?export=view&id=1JkQfT3nEa1zYAfCqEc01TMakBUe1cqgO",
    "https://drive.google.com/uc?export=view&id=1UdllnylQP4nN2sRYWfC1YPe38SBjgY9A",
    "https://drive.google.com/uc?export=view&id=1tvhF9OgfiJuxYyAXeZ3FJO0P7F0kgcLr",
    "https://drive.google.com/uc?export=view&id=1b9ghXDwnBuUNHLgwlJi7-z3vw803Dlcg",
    "https://drive.google.com/uc?export=view&id=1DYXqniFYq4HvcKc0hN1hV2BH1_1fwH7q",
    "https://drive.google.com/uc?export=view&id=1Fk-I4RoNV36d0fyEzYKseOKDS4CbcVat",
    "https://drive.google.com/uc?export=view&id=1HkaSR3bJ1EsZ7qprHYmwFuVBMk97AB_z",
    "https://drive.google.com/uc?export=view&id=1GW_VSLB3uA77pq6ZncQ8ggramti9YhK_",
    "https://drive.google.com/uc?export=view&id=19Zv-X4G3Doley_h8J5iWatUOqHWy2AY-",
    "https://drive.google.com/uc?export=view&id=1jbS8_9bZmARsn1TuzHESMa-4iEUVRnjQ",
    "https://drive.google.com/uc?export=view&id=1SvPgLtCI0AtrERSK3LdjpXqlTGtatS6p",
    "https://drive.google.com/uc?export=view&id=10_-leGbSPHwsdnKD_ppx6_Tw1Nzz0ZhR",
    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

    ]
    data_list = [
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1P_YxveJIz8irx8uuo5PzHpui094Q3X1i",
        "https://drive.google.com/uc?export=view&id=1JtqLMi6pgjU3gEfS3RWZx65SPyYvDcz4",
        "https://drive.google.com/uc?export=view&id=1JNDTXm67tpoFV3AvIc8GpJ9yUcQD7kdL",
        "https://drive.google.com/uc?export=view&id=1VWBxi6veMmh81aHkkIOZwUqOEZvvIKqT",
        "https://drive.google.com/uc?export=view&id=1yi6QkI0WJ2ATXCOKehc4rK69JTHqmCFZ",
        "https://drive.google.com/uc?export=view&id=1FffMm3Kz9BmEf0tT331GfprA48PrpzFR",
        "https://drive.google.com/uc?export=view&id=18PaYPqNuolvh_edOMRJLFcrwZ-OQjrWa",
        "https://drive.google.com/uc?export=view&id=1OXlnGUKEbYXb-kPCxoK7bYqOcM1HYkAT",
        "https://drive.google.com/uc?export=view&id=1Xy2okVZv1rclkiCLERxEQo0fqGo8BlC0",
        "https://drive.google.com/uc?export=view&id=1B1uJFPEXgUkwTH3nfjI9y2hxNGAQccv7",
        "https://drive.google.com/uc?export=view&id=1z_iJogIwD_bmypmmBGJNI5SUCu0LktNI",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1v7PggWxaiOduwFLIk_Mh-_bDuqoItwbL",
        "https://drive.google.com/uc?export=view&id=1VOCDgD-QTYi4TC1XvR3yCW2iwMunThb8",
        "https://drive.google.com/uc?export=view&id=1xMWieEG3oBw01zhBsx1EqWGeMLpsM8__",
        "https://drive.google.com/uc?export=view&id=1Y-lrzJ_Q0Anc9xStNdbaUkobMwgXNj7j",
        "https://drive.google.com/uc?export=view&id=1mdLAaWzAW8BeqNNE9xMXCR_5tIKwHGc-",
        "https://drive.google.com/uc?export=view&id=1uPgiWNrjon2oauwA9tD8Yr8fiRAFAWYx",
        "https://drive.google.com/uc?export=view&id=17kZM4YEVVqjeBVgDY83XtLMGnvYIxxic",
        "https://drive.google.com/uc?export=view&id=1ejVyBOb7tnoO8A9hCYQ6PY3V0mtRCH-f",
        "https://drive.google.com/uc?export=view&id=1davruIwEPjjgf6A8fM0n6jnjpBeTZmGE",
        "https://drive.google.com/uc?export=view&id=1NGN_5qS9Rlq3DjnLrgedc-xDST-21ESL"
    ]
    data_list =[
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Murah Senyum", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Ramah", "pesan": "Selalu jadi orang baik"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Kepala Divisi Hubungan Luar", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Enak diajak ngobrol", "pesan": "Semangat terus bangg"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Ahli Hubungan Luar", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Kerenn bangett bang", "pesan": "Selalu jadi orang yang kritis"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Hubungan Luar", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Staf Hubungan Luar", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Bandar lampung", "hobbi": "Lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "Ramah", "pesan": "Selalu jadi orang yang ramah tamah"},
        {"nama": "Alfaya Abiyyi", "jabatan": "Staf Hubungan Luar", "nim": "124450006", "umur": "nelson piquet", "asal": "Balam", "alamat": "Balam", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "Keren", "pesan": "Semangat terus"},
        {"nama": "Asri Meilani", "jabatan": "Staf Hubungan Luar", "nim": "124450010", "umur": "20", "asal": "Lampung barat", "alamat": "Korpri raya", "hobbi": "Nonton film", "sosmed": "@asrmeilani", "kesan": "Sangat ramah", "pesan": "Terus jadi orang ramah kak"},
        {"nama": "Bima Ekayasa", "jabatan": "Staf Hubungan Luar", "nim": "124450106", "umur": "-", "asal": "Lampung", "alamat": "Bandar lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "Ramah", "pesan": "Selalu jadi orang yang ramah tamah"},
        {"nama": "Indah Khairunnisa", "jabatan": "Staf Hubungan Luar", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Staf Hubungan Luar", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "Ngefollow-up chat", "sosmed": "@erlsriska", "kesan": "Cantik banget", "pesan": "selalu ramah ya"},
        {"nama": "Yollanda Agustina", "jabatan": "Staf Hubungan Luar", "nim": "124450024", "umur": "-", "asal": "Kerangka bawang sebelah barat", "alamat": "Kayu mulya", "hobbi": "Tanya bang henry", "sosmed": "@yollanda_agustina16", "kesan": "aktif banget", "pesan": "inget istirahat kak"},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Kepala Divisi Pengabdian Masyarakat", "nim": "123450032", "umur": "-", "asal": "Tetangga kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "kesan": "Jail", "pesan": "jangan sering mancing keributan bang"},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staf Ahli Pengabdian Masyarakat", "nim": "123450095", "umur": "-", "asal": "Tangsel", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "kesan": "Lucuu", "pesan": "selalu lucuu kak"},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "gerbar", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "kakaknya lucuu", "pesan": "tetep jadi asprak yang keren ya kak"},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "kesan": "kocak", "pesan": "Selalu tertawa terus kak"},
        {"nama": "Danil N Fadillah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450103", "umur": "-", "asal": "Karawang", "alamat": "belakang polda", "hobbi": "Ngasi makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "softboy", "pesan": "Selalu kalcer bang"},
        {"nama": "Favian Arkaanda", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450021", "umur": "-", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "kesan": "Keren", "pesan": "Semangat terus dan humoriss bang"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450081", "umur": "20", "asal": "Situlah", "alamat": "Pohon mulya", "hobbi": "Nyari hobi", "sosmed": "@zydddddd__", "kesan": "Hebat dan tegas", "pesan": "selalu jadi orang keren dan ramah tamah"},
        {"nama": "Muhammad Rizaldi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450093", "umur": "masih mudalah", "asal": "Rahim ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Gambarr", "sosmed": "@jaldii._", "kesan": "keren jadi mc pplk 2025", "pesan": "selalu ramah ya bang"},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450074", "umur": "20", "asal": "Banyak begal", "alamat": "Pinggir jalan", "hobbi": "Nonton Tinkerbell", "sosmed": "@snova.19", "kesan": "kakaknya lucu", "pesan": "Terus jadi orang ramah kak"},
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kerenn banget", "pesan": "Selalu jadi orang baik"}
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
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
    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

    
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
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"}
    
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")
    
elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1jDEG-im2Qsxw0D3QYT7r-wV8ysUte12r",
        "https://drive.google.com/uc?export=view&id=1lWZ_8Z153AibwM01rkt9-o4gJiGTOZ4k",
        "https://drive.google.com/uc?export=view&id=1UwozLsSossrwwhPwtgMh4MUlhlI8qAIH",
        "https://drive.google.com/uc?export=view&id=11O0E8TNxJ3ai9MNPfZimVe-9_4nh2atM",
        "https://drive.google.com/uc?export=view&id=1ha6ULRBaN5h_SWuaNR46_8FNAGd4vcIh",
        "https://drive.google.com/uc?export=view&id=1TKjulrdydxRsXnQ4IlAXqzSDnW5-cqrf",
        "https://drive.google.com/uc?export=view&id=1EeW5h2G4YVF02qFDhJ0KvqzmJUvVqI_6",
        "https://drive.google.com/uc?export=view&id=15QVwAjAw9ikSzi6nY75zW-nT8BDb1Kn4",
        "https://drive.google.com/uc?export=view&id=1WbxOo7eagnmTHU79WClOSTgBBKFiSSeo",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1J08meeDUoQxSv6Th2tbLHWUQnb8D9YOQ",
        "https://drive.google.com/uc?export=view&id=1iWmFuGpmvSshTVO4RGuioSLbOXOWhvSW"
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
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1-ZcGn0wV7AXDQIGv_aX34akJAd6w44hj",
        "https://drive.google.com/uc?export=view&id=17RTVW5kWVLS5ycGaHckvo6XnhKAKJJlH",
        "https://drive.google.com/uc?export=view&id=1xBjaDtComTuqY56rrAv1DOPOGFUsY2sv",
        "https://drive.google.com/uc?export=view&id=1lyOZpqKd1b9nVZstAZA4vLRTz7SeZzna",
        "https://drive.google.com/uc?export=view&id=1okhUMy1D1CzbJJTnpxswVYyNSbQz2TXc",
        "https://drive.google.com/uc?export=view&id=1IbcbkT6CkMCCuhZxDyxzQug0rU_-hNWR",
        "https://drive.google.com/uc?export=view&id=1-D_Tba9L9GLWtdXIVNVZFC2onpcuQzkp",
        "https://drive.google.com/uc?export=view&id=1q6hg0TjVawxMmbitJ_zV5tsq8yetgFjs",
        "https://drive.google.com/uc?export=view&id=11ECoEZWE-LOXHLR-5hE68rIAi-3kGoMv",
        "https://drive.google.com/uc?export=view&id=1ocd1SyELHuUxoTrIwTgqDIdy-Y6jR4gk",
        "https://drive.google.com/uc?export=view&id=1Yu988LBWpC9rq6MA-e4W_gZX7nToSDM4",
        "https://drive.google.com/uc?export=view&id=1LeVLEdGy14_V4FrucsTJj0ge2dzNRI4C",
        "https://drive.google.com/uc?export=view&id=1qh8w2pIV-z9ZMOzUfRTo_ffkBBX3-zIy",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1SbkF-ECFzzfVNMpIfgynXtgLkw_rWZ8w",
        "https://drive.google.com/uc?export=view&id=1VZ6JdtFLH3gMmoy4A0XXoc5TD-X22kI-",
        "https://drive.google.com/uc?export=view&id=18BXJqwqoBCnjDqoM2aojor4MLf8suhWf",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
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
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1mfLGXyKIio_1TC5qM6eRj8pyNJfsjwgT",
        "https://drive.google.com/uc?export=view&id=1PN8JqZ2N6f9qRjOeVOlWdCd4mnNNtI--",
        "https://drive.google.com/uc?export=view&id=1qR9qg7LSvMBVWYqNEZKiLmg7Q1jgqhM3",
        "https://drive.google.com/uc?export=view&id=1oPf8xBDFjHQAEdD9nsmXJA5ywCSsZUSm",
        "https://drive.google.com/uc?export=view&id=16toA9QDn_boIAyu5uVi3OBQLOtjEmtjx",
        "https://drive.google.com/uc?export=view&id=1cOT5AZZPuBRqoPG7zW0INLjDmTO4UI8O",
        "https://drive.google.com/uc?export=view&id=1IxcdiH-zgZhgetdBBJbWBUZJi3KdkRmM",
        "https://drive.google.com/uc?export=view&id=1bi7Vs2g-8Wk9Ab8SCsAV6Q64tZzA0XDO",
        "https://drive.google.com/uc?export=view&id=1wufJqchT8TCybPuB-t9s8A3NJj04Nqcm",
        "https://drive.google.com/uc?export=view&id=1OagoRIgcLhWt18LJPgg3-Owdg9-3zyp9",
        "https://drive.google.com/uc?export=view&id=1pEgBR4_cYue3-2zEgpyvSNyCROGTfCyM",
        "https://drive.google.com/uc?export=view&id=12vSMsCvlgNGlcMtnIZCzLu0ZBda8NwFf",
        "https://drive.google.com/uc?export=view&id=1TTdTDfg1GuSIz0Q9n3I_nG0rLf1D4Rak",
        "https://drive.google.com/uc?export=view&id=1ORvF_9EZTfnGdeoweibwbUy07y-Fd0tA",
        "https://drive.google.com/uc?export=view&id=1mPNBVYPsYcf52Bb9Q_HoJ_tticObUjXD"
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
