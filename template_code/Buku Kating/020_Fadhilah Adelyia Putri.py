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
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1sgjaunK9jvDRQLBLqU1MZGNV2dH0brvl",
                  "https://drive.google.com/uc?export=view&id=1FZ1r0dgqeWMuqJixnQiL8FgLH--az6Lt",
                  "https://drive.google.com/uc?export=view&id=1p9zBVMLBVLJ8jpmsgxQALlVoau-RYqtS",
                  "https://drive.google.com/uc?export=view&id=1iwhdyUuWBUktB2HSohiK12y0MbCph1td",
                  "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                  "https://drive.google.com/uc?export=view&id=1BSlFHyegAlfxzr1pK2_By0DmE1a45Wzb",
                  "https://drive.google.com/uc?export=view&id=1MjiNDGsq4fjbxIgKRlFOHB5slnDzRp0v",
                  "https://drive.google.com/uc?export=view&id=1m0SPV3EXTBfNWif3lkaXlYO4x9D32zZZ",
                  "https://drive.google.com/uc?export=view&id=1rGfu4ApUnhCg0axTDiQxk5yJ2eudoXJS",
                  "https://drive.google.com/uc?export=view&id=1AHW6FGGdlA6t9Wo67AINH-jx-2ONGUha",
                  "https://drive.google.com/uc?export=view&id=1_X0MM61QIrR5ajfBmua58ONXJB9uxxB9",
                  "https://drive.google.com/uc?export=view&id=1IdC3Fh3ScYXQUU7-rtA5w7QA5DKINnwa",
                  "https://drive.google.com/uc?export=view&id=1sgWx1hWUtsSu7EjA1hxOhOw7c2gOK1nJ",
    ]
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
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1xLbfVREwCK44RGkYqCnL7QvFnWkvXjcu",
                  "https://drive.google.com/uc?export=view&id=1Xm5AhoCj8PYpHhlK3pCYhvQCm2D92GcD",
                  "https://drive.google.com/uc?export=view&id=1Ny3OeKP61APOGUYDFirgB1-0fi8Hp9P7",
                  "https://drive.google.com/uc?export=view&id=1Z3JcQ3-D9YbF0WwkjG0H0trbF8qioHVI",
                  "https://drive.google.com/uc?export=view&id=1TyWKKDLXxI5o1YW5hirjAjzZgd1HC0gt",
                  "https://drive.google.com/uc?export=view&id=1Qn9QDFtkWykdQ6SILTsH1CZ4UtwY3DoH",
                  "https://drive.google.com/uc?export=view&id=1lHe9tL_UUjqEMAExJTYVS1r2jXA8WitH",
                  "https://drive.google.com/uc?export=view&id=1veZlfxydMvYJ28Qg3yRP_stHODX3UVBU",
                  "https://drive.google.com/uc?export=view&id=16j3ATXaGZuvoSlH1iOieoqQhT2ft66Kr",
                  "https://drive.google.com/uc?export=view&id=1-y0wQrahrngBunp8Ez6uroimBn7G4mQP",
                  "https://drive.google.com/uc?export=view&id=1tDLDCzeLcx_nenPKBqebkFUwXqeuBK1r",
                  "https://drive.google.com/uc?export=view&id=1cXyPVj7QWxTjxd51Moxfew0X8AnK658_",
                  "https://drive.google.com/uc?export=view&id=1Pip7eZSAvGlDrXTonnA4Mual7_cspZqh",
                  "https://drive.google.com/uc?export=view&id=1qT2bvrPbsVSXGV6tFOLOaV4zviZ9yLR2",
                  "https://drive.google.com/uc?export=view&id=1Nss6Sf07xm6vaOns77nOd2SjScJh_TIz",
                  "https://drive.google.com/uc?export=view&id=1lDitxeVxnoz7Hr-b635rSth_aHcrZwrY",
                  "https://drive.google.com/uc?export=view&id=1E2Z_VyAUZjqSNPReAhvTtMEKNdvSrNCO",
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
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
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
        "https://drive.google.com/uc?export=view&id=1LpkJS3AtufYT_fFSiLxTC85bu-Okr21l",
        "https://drive.google.com/uc?export=view&id=1qNPSsCFoOKvNGWAgL4VbLtzPjrqwKa9B",
        "https://drive.google.com/uc?export=view&id=1vQ1WwJfcbh6tO_551LmosgFpFSpp7bQh",
        "https://drive.google.com/uc?export=view&id=1gvLlRqMicevOMx9Q8VRJLE1jheaF3P06",
        "https://drive.google.com/uc?export=view&id=1OpO2kB_r4NbiESEsUUImaXJGz-e1v6nZ",
        "https://drive.google.com/uc?export=view&id=1uQu6Z89m8VllwkNeoPqZGBjV8yKTi8m0",
        "https://drive.google.com/uc?export=view&id=1gqTF8hpm9kCBIhB4eKOLkzaSaINpRAZ3",
        "https://drive.google.com/uc?export=view&id=1gJfCBhx6x5_g38k0OvQHRWx1MQ3lXClp",
        "https://drive.google.com/uc?export=view&id=1TGrX2K9khNx8jN-rKlXfpqCejj6x5rFp",
        "https://drive.google.com/uc?export=view&id=1nmjbsUX8qk8MZtWmVKpt3b7Ppl6Lhj30",
        "https://drive.google.com/uc?export=view&id=16DgO0Dp5giQpOAtOP_3ayAyLizB1IcFj",
        "https://drive.google.com/uc?export=view&id=1t-SB1BCLqv__zv1TIo5Xg_A3B33bL0ta",
        "https://drive.google.com/uc?export=view&id=1ZEG-GMSzeu7_EzovItWj9y5plvHxYBCc",
        "https://drive.google.com/uc?export=view&id=12Kg7x7VYZGE90JWUrvN0_eTc9zjCDnxZ",
        "https://drive.google.com/uc?export=view&id=1fvftKvt8X4V9xXvgh6KulTk9yvXtmG-f",
        "https://drive.google.com/uc?export=view&id=155sWMRWrgn9SZCHdNuG69PDEhokwrTqm",
        "https://drive.google.com/uc?export=view&id=1BZwXBclEc9ovMiu1j3iH2eYEPuVCEnen",
    ]
    data_list = [
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
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kerenn banget", "pesan": "Selalu jadi orang baik"},
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1DYGVoGeFmPO6hU5XEFai0Q9UMrYGoMoM",
                  "https://drive.google.com/uc?export=view&id=1a-wAVnHAglqty0iJxyVajXunk3APq1hl",
                  "https://drive.google.com/uc?export=view&id=10j4ZD4s3HITL5Wo_2XzGFVafXjQjHnx5",
                  "https://drive.google.com/uc?export=view&id=1QuqsdQXROhjyv-6z2PEyRY3UoqrG2os4",
                  "https://drive.google.com/uc?export=view&id=1Qit9Ufu5WctsrS-vA-AXiimLYC6G-lZ8",
                  "https://drive.google.com/uc?export=view&id=1ci3uCjf9ripPWM27pyeD8k4xNgGTyVQv",
                  "https://drive.google.com/uc?export=view&id=1iqXTp2hBemukc0ZdRJkDq5e7T6VsP9Tq",
                  "https://drive.google.com/uc?export=view&id=1ztiNEefPlgn46RpkEpXvG4pOHn5c-yiw",
                  "https://drive.google.com/uc?export=view&id=1Lti4qpba2G8z5QInXZ3Zk-gJEpwgaI2j",
                  "https://drive.google.com/uc?export=view&id=1vsCXw1ah-rNSCCE6lGOxblwHy03uK1fs",
                  "https://drive.google.com/uc?export=view&id=1iGyzvRdRgespZjIr2loonQI38WKQvoug",
                  "https://drive.google.com/uc?export=view&id=1mYqXPeaBs4GYbJGoUgnkvJJ0LvYE71_9",
                  "https://drive.google.com/uc?export=view&id=12VNXZqd_CQrxbKoDLg78MvmOInj1rJn8",
                  "https://drive.google.com/uc?export=view&id=1fMC0Pk3wxA34x_BTPxp601hL-dTJol68",
                  "https://drive.google.com/uc?export=view&id=1-pBYEj5JtPcSGP21OmFrn4AL22jA1EqS",
                  "https://drive.google.com/uc?export=view&id=1HXLn9bsLXJtR4gL9kviDt_vpHGQFOId0",
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
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kak felis keliatannya pemalu tapi aslinya enggaa, lucuu, baikk banget dan pastinya seru bangett", "pesan": "Semangat yaa kak kuliahnyaa, semoga selalu dikelilingi orang orang baik, keep shining kak feliss!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Bang Razan semi introvert gitu, tapi aslinya asikk dan baikk bangettt", "pesan": "Semangat bang kuliahnyaa, sehat dan sukses selaluu!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kakaknyaa baikk dan murah senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kakaknya baikk, murah senyum dan ramah bangett", "pesan": "Semangat ya kak kulliahnyaa, happy selaluu kakk!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat yaa kak kuliahnyaa, sehat selaluu!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kak Bunga baikk, murah senyum dan seruu bangett", "pesan": "Semangat kuliahnya kakk, stay humblee!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kakaknya baikk, murah senyumm dan keliatan asikk", "pesan": "Semangat yaa kak kuliahnya, sehatt selalu!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kakaknya lucuu, baik, dan soft bangett", "pesan": "Semangat kuliahnya kakk, happy selalu yaa!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "kakaknya baikk dan murah senyumm", "pesan": "Semangat kak kuliahnyaa, semoga lancar dan sukses selaluu!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Abangnya baikk dan kalem bangett", "pesan": "Semangat kuliahnya bangg, always happyy!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kakaknya baik, dan murah senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kakaknya baik dan softt", "pesan": "Semangat kuliahnyaa kak, sehat dan sukses selaluu!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")
