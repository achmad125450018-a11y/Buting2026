from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1fVbdcNtDL9EnqIOj_mgNN44LK8k7bcBo",
        "https://drive.google.com/uc?export=view&id=1h5eAUDPuBkfK5B2wPaIiGl5tJyoVnJeH",
        "https://drive.google.com/uc?export=view&id=12EPPbJo4eqKPPGcCGeDTkaDcJuoy524g",
        "https://drive.google.com/uc?export=view&id=1l3_Y7sxDN3fww3K1Bd4xK3Me0IeF46e5",
        "https://drive.google.com/uc?export=view&id=1HpFYt0K8iMSx-CS6yJi_WrFfujRdIiOv",
        "https://drive.google.com/uc?export=view&id=1JtuaMMWi0pW6-pX2X1wNGl2W9f-B6227",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan suksek selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya sof spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1O9sLac8Jr5gmmjLM7nwNX4rq0-L0Caeu",
        "https://drive.google.com/uc?export=view&id=1b5liNx6c5vaHlW9siu_GbCzPJ2pHQT5j",
        "https://drive.google.com/uc?export=view&id=1gSqLICQv6JrSLT4bQI1z1OROP-Zi1CEX",
        "https://drive.google.com/uc?export=view&id=1TqkuimLvIKpMOetoKtnmMw4f4UFSpxsJ",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1hLDsKBT8gTYk40oK-iUmbsNoITqfXylm",
        "https://drive.google.com/uc?export=view&id=1Vtiuy0lfHpLrc3BIfRhtLbrReVMsbeS1",
        "https://drive.google.com/uc?export=view&id=1duG5OJhw34J-g6E6fn_NDXekj3bR028Q",
        "https://drive.google.com/uc?export=view&id=1S7gJPfWM78mlS0KLa08V85j7IVekvxKg",
        "https://drive.google.com/uc?export=view&id=12Gkcnl6yQMw_tYqWAEPEHmav51vRjc73",
        "https://drive.google.com/uc?export=view&id=1AE7gha77N1NTg1vh927w_jRn7yPYSSwr",
        "https://drive.google.com/uc?export=view&id=1Frabe4ucvCGxGP7ahBT_vI_mRauoBQsM",
        "https://drive.google.com/uc?export=view&id=1YV3sqsc316u8go2QlHPNXquhNb5eJ4vY",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "12345085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin Lagu Semusim", "sosmed": "@j__eesie", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Givaro Ananta","jabatan": "Kepala Komisi II", "nim": "123450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum Kopi", "sosmed": "@givarooo", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen Kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "City Earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "Gym / Koleksi Figur", "sosmed": "@nagatsee", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa,putri,suci", "sosmed": "@sekardnwp", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa Angin", "sosmed": "@nahaysh", "kesan": "Mantap", "pesan": "Jaya selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1orLImq551nHraZ0X4AAOAPZTM9rL5Z-V",
        "https://drive.google.com/uc?export=view&id=1nrDS8IP8A5HoO05xYB4uyhY4Dvbn4R4r",
        "https://drive.google.com/uc?export=view&id=1671S6yjjHBDnfCvGEN9d5CF7GKmMfZV5",
        "https://drive.google.com/uc?export=view&id=1j9CkpEJdOSqdSjg4rK6QDlB93oMpoveD",
        "https://drive.google.com/uc?export=view&id=1gBB7ZZueTgIWA7GZ7xHlmu1Cg-yf7ZCq",
        "https://drive.google.com/uc?export=view&id=1OXsekTpgD8RC5bnRiYrse_PNFvx-k2P4",
        "https://drive.google.com/uc?export=view&id=1Hx97FsSOMD11sTICLZBPqFdnmxdqmHIo",
        "https://drive.google.com/uc?export=view&id=1UgVoMefovNv7B2cQGgndy8zG_8JAwLim",
        "https://drive.google.com/uc?export=view&id=17FiNMgKcw8_-nSKVQosy10XopH6C7R2h",
        "https://drive.google.com/uc?export=view&id=1pMRQWN1UpXrM2ZIGFkRP3R6Z9NfyFmZI",
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
        "https://drive.google.com/uc?export=view&id=1_LaGRBuUgTJOT9T0zBdeBHyF6msZbaHV",
        "https://drive.google.com/uc?export=view&id=1Qh_48LGHS3R_Az31JRQVcjpTdhb-jJdn",
        "https://drive.google.com/uc?export=view&id=1IFOYEs4gfA5VX5E7gjV2NOEgCX5nK1yF",
        "https://drive.google.com/uc?export=view&id=18DquKiwmaLetQsXaWmsCmpiGQDOVpJZb",
        "https://drive.google.com/uc?export=view&id=1fJyi-RIP7xvBvy5kQHM3baknCu1KdoMA",
        "https://drive.google.com/uc?export=view&id=1zD2NS6YbBX-boYSERjvG_3CMzj6nmOus",
        "https://drive.google.com/uc?export=view&id=1B7NXVqsoDcvWvzHnQebAVw4--DcQ3HwV",
        "https://drive.google.com/uc?export=view&id=1Aapb8JmfykOuQpbeZgLlUd977EiZoHBQ",
        "https://drive.google.com/uc?export=view&id=1ScQc817uB_RvnSJmiYGCL8rqcnGsS-6G",
        "https://drive.google.com/uc?export=view&id=1w-fkHkB3sVAtXiNN5dVhSOCprLvb2Iy-",
        "https://drive.google.com/uc?export=view&id=10wZTJWb5inqC8iuZEaH2fMDpL0lRuhT9",
        "https://drive.google.com/uc?export=view&id=1SLw0z6kqLKP_No8tg0Ih9vlXre-uivK6",
        "https://drive.google.com/uc?export=view&id=19lmiBeWoFiOx8GMAVXY2TOCsweZ0oM6S",
        "https://drive.google.com/uc?export=view&id=1tm0PM2oQ23KvmzSpOGhUSAZ4I7-wh_cS",
        "https://drive.google.com/uc?export=view&id=1qj2Uqsd-yx0SeAHe51_7ab-6U0xeHMUI",
        "https://drive.google.com/uc?export=view&id=152xyIO1wvVB6q063wP8UgzJSSOlc84WV",
        "https://drive.google.com/uc?export=view&id=1PYxrVse-acDNec6GHf4D_lwVHw8G_e-5",
    ]
    data_list = [
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Anggota PSDA", "jabatan": "Staf PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1GkDmPwPuCOcrh9rdxRru46n4I9K_p45D",
        "https://drive.google.com/uc?export=view&id=19xOFTy_4sH8rHikkvBwojL6XVsKBnEjW",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1JrUW6LiSm9fp1p0tEsyyvVv_0riGsJTC",
        "https://drive.google.com/uc?export=view&id=1UuMEF3oE4ApRe3JlZQm5wvFsvQ6g8cau",
        "https://drive.google.com/uc?export=view&id=1qHFEjQPEF_M4L4tO8Mh77zEnxq2WqXVE",
        "https://drive.google.com/uc?export=view&id=1Jk6zW99DGwmFJSijVvGgdeSNf1Ldjoih",
        "https://drive.google.com/uc?export=view&id=1FC1Pq2kAxzfoMK97NYRNG2fY8EfsntbO",
        "https://drive.google.com/uc?export=view&id=1w26kbJ1NXEE0DAPFHXmIHmiKSIDToTzH",
        "https://drive.google.com/uc?export=view&id=1nR7gOcXS-SJcSEjA3xm7hgjo0J-33vV2",
        "https://drive.google.com/uc?export=view&id=1jcHJCz6pfkpJ2dCW6UBU5MdszbAXo_pf",
        "https://drive.google.com/uc?export=view&id=1aVJGtf9Y6DyklDgplQdIPFxhrKKbMBLj",
        "https://drive.google.com/uc?export=view&id=1cjWfkHRe4OTVg0IpZ2PSFlSRk1IU7LG_",
        "https://drive.google.com/uc?export=view&id=1Z00qpZi7alGUIMQ-pXcjZ0SA8o9lFfc1",
        "https://drive.google.com/uc?export=view&id=1ZhacuK_MlZGpbQOjmtEfnzr2pQ5x15Hk",
        "https://drive.google.com/uc?export=view&id=1nK8-letlsIefUIDqY5BozWfkcqGlZyxp",
        "https://drive.google.com/uc?export=view&id=1zEl7TGcp2qTR64C3HplEWtQcvNQTvO7b",
        "https://drive.google.com/uc?export=view&id=139gqZ6DlhTJrY1J-VhF8z3ATpRzwAb0Q",
        "https://drive.google.com/uc?export=view&id=1DaoqBbB8T1wg1oaKYLcbrshOvc_sLbC_",
        "https://drive.google.com/uc?export=view&id=1np7Jo873sq3CcGvckBfge23lK1Gk8uc0",
        "https://drive.google.com/uc?export=view&id=1Q8_kk-s_vEpJDVzZl4u0mqM0KzuoWn0d",
        "https://drive.google.com/uc?export=view&id=1Cslt_o6sjlnuuVY75FiTsI-4Xr3PDGDJ",
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
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=12gltKb0u47SSXS0AdybpTW8gsgT-PJJ7",
        "https://drive.google.com/uc?export=view&id=1lKLds4z1vjwe7Vi5CxS496W8asrxsA8N",
        "https://drive.google.com/uc?export=view&id=1X0LFmPLuHFFpC9YvabA7yqX8higuMaxH",
        "https://drive.google.com/uc?export=view&id=1yNVj4PUy4IjllMMoTL2iBgoQpwkB07GE",
        "https://drive.google.com/uc?export=view&id=1enSvuub0CvSkA9AcDczoEjwRYji244U5",
        "https://drive.google.com/uc?export=view&id=1Krq4AaG1RYRvQfMpzJKYn8eFhJ2U9Qhg",
        "https://drive.google.com/uc?export=view&id=1kMB9sFOC9iUewwf3g1eqyPFcdInZ7iHl",
        "https://drive.google.com/uc?export=view&id=1WlGL_3JBoGKfvaJ1YpDhGhhk_ERvOb9F",
        "https://drive.google.com/uc?export=view&id=1WiPRZhlIFAFXZ0ANa5EjSUZwbQ932uWe",
        "https://drive.google.com/uc?export=view&id=1TMBqCe-jDE9bzheeVHLOg03LA4h-ahlM",
        "https://drive.google.com/uc?export=view&id=1K03xYUbFS2H0wPceTPIsU8dmUGkb6cIy",
        "https://drive.google.com/uc?export=view&id=1zRYV33hR4IyUB6f6IidO9nsFxKPzJ5Ew",
        "https://drive.google.com/uc?export=view&id=1MD5UVO9m-tv2UB0fJP1nI-PnrQKHzedP",
        "https://drive.google.com/uc?export=view&id=1-sZTRl503zi5uxv7VaSmIaicniZ0y3gQ",
        "https://drive.google.com/uc?export=view&id=17wRsf488SsSgX4y4uaH7sc-FEG5_SfAb",
        "https://drive.google.com/uc?export=view&id=1GbJddaGIbazKoGDbjeboQa-erGo7EtGk",
        "https://drive.google.com/uc?export=view&id=1JxAD3i-UAVGnpeTVafzaWLWIGBpm4phB",
        "https://drive.google.com/uc?export=view&id=12FIKj2LHvh-wF_73K6pQzSKJG0aSIlP6",
        "https://drive.google.com/uc?export=view&id=10apMk99cPTt5xRKzcHRAxozyoumGrIzR",
        "https://drive.google.com/uc?export=view&id=1z_GJHeWW7LHy3iaNyB-8sxeqA49k-M3q",
        "https://drive.google.com/uc?export=view&id=1aXUBI_O2xlkBooDPS9FEyEeDgS4ABAmO",
        "https://drive.google.com/uc?export=view&id=1PwgN6MoB47GwYwfAT--wknoszLzoAKsD",
    ] 
    data_list = [
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "jabatan": "Staf Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
    ] 
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1jPeN_evGbdLn57baXWnzuh7PE0ndbjOp",
        "https://drive.google.com/uc?export=view&id=1ruhlJAoITApJXBmfzOouKyEZbcLrGr1a",
        "https://drive.google.com/uc?export=view&id=11xkVLH44BIbI-jGBRWpvmn41r2pjEH9M",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1xgC1SHX5OkCAjXjoH7WtCaYL98MHr1_T",
        "https://drive.google.com/uc?export=view&id=1xSPT55idf0TIlwZegAsRiBUPiZJliREa",
        "https://drive.google.com/uc?export=view&id=1EzXI_JlohfhDghLRPVK0Tfr4T7ZYdaf7",
        "https://drive.google.com/uc?export=view&id=1coginEB51EMcRpWXHozBNQ5rAGkXjxOY",
        "https://drive.google.com/uc?export=view&id=1-tqf_KAjuPJsZVc_dgSf7UvN2FeRA881",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1urI1RZH3NLqvgf0hUMWW3by9Tg4lNPvG",
        "https://drive.google.com/uc?export=view&id=1BKF-MEFLeYSJHElB2jdG57FTLaKAl2OU",
        "https://drive.google.com/uc?export=view&id=1jqbpBPbwlcnZcVcs9WJlZGE1W2Jr1L5S",
        "https://drive.google.com/uc?export=view&id=1JSBdDGSFCk-rPQSZZeBD6U828hwj0R4p",
        "https://drive.google.com/uc?export=view&id=1-pa4mws5yadAjdVtISU6jZbGWD30cPed",
        "https://drive.google.com/uc?export=view&id=1sE8MJVefRvSpJMtyMVPZjnMv2mx32h07",
    ]
    data_list = [
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Anggota Internal", "jabatan": "Staf Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=14hcL8FhtwwqBQfkM9B5YZQJGqqLb8D-S",
        "https://drive.google.com/uc?export=view&id=1rjhAWLRLAhtn1DJFyChOW-w0gVbDNJdz",
        "https://drive.google.com/uc?export=view&id=1JuDaB8f6ypNAey0_RH8X4aW7TKBBG3fl",
        "https://drive.google.com/uc?export=view&id=1x-Vxo9k_fqZBOSCcK1C44EgpbOywa4Gg",
        "https://drive.google.com/uc?export=view&id=1wrwo39xhMDWyZS22SR6yUR3P2F-MtQgO",
        "https://drive.google.com/uc?export=view&id=10FauwZ8w62Uf2ICNgxi8gZVjsXVnN3vN",
        "https://drive.google.com/uc?export=view&id=1oZHVrvfsoxEpKFXcdkNew_Za6fX5aHTZ",
        "https://drive.google.com/uc?export=view&id=1mo5kbI30uTnxNsqu24RaBcfgxGakDsm9",
        "https://drive.google.com/uc?export=view&id=15Oba8SQ5vqA5pfV7EJcIld5ZePLEe8sz",
        "https://drive.google.com/uc?export=view&id=1cDh7BJEOpzfEkv0lP9zyILk1p7rvg5d5",
        "https://drive.google.com/uc?export=view&id=1NjG9jhrTbZBnkseLVLPQhuVy-yJP6Skn",
        "https://drive.google.com/uc?export=view&id=1qAtFg84Mbmj_ZJNVLt-400ggYtD1fln-",
    ] 
    data_list = [
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "jabatan": "Staf SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
    ] 
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1Dwc_wTvKyiNZGs8zr5PaFaq13TJodwP_",
        "https://drive.google.com/uc?export=view&id=1yJ3rK3Sk67MlxzxFtnticSMfXMfMSO0f",
        "https://drive.google.com/uc?export=view&id=1FMgfIziI6s_eHdPhAvcz4KXNRdIMNAdA",
        "https://drive.google.com/uc?export=view&id=1PkJKppQTOfrSQxXOdirqs-1ZppTW85bp",
        "https://drive.google.com/uc?export=view&id=1pc-hFmULGT_Mm4lwV06anerlPDEgf5Wd",
        "https://drive.google.com/uc?export=view&id=1Qkd1wvcA4GZQLyrLrhRyKy3fUcHsvpAW",
        "https://drive.google.com/uc?export=view&id=1KEVZNBNwc2l_WA5rIkQ-3c1OiD67ZM6g",
        "https://drive.google.com/uc?export=view&id=1o9qCmQLOhGAdCSKXeeruEj5RhAWUmNTC",
        "https://drive.google.com/uc?export=view&id=1RQOcsXdD-kFYOYE9bdMR1EOsh69VRz9g",
        "https://drive.google.com/uc?export=view&id=1lXzPqbD9WSV4zhfVeqQESdCUMakW0-ky",
        "https://drive.google.com/uc?export=view&id=1V1Og56j1hLWclP0i2ejvAU_OpZOsHcxN",
        "https://drive.google.com/uc?export=view&id=1HzatuJUprH-pEYcOM1OdNwubhxnSmfX3",
        "https://drive.google.com/uc?export=view&id=1r_Ki_IqYCBgD6Im3aUuzvkiKbv-KKs4T",
        "https://drive.google.com/uc?export=view&id=1hfVRRVwvASqOeOx-U1ISic5YZkqQ2RWs",
        "https://drive.google.com/uc?export=view&id=1jRD4vuZKTI-48jW3tZCzLxul3QETXOxA",
        "https://drive.google.com/uc?export=view&id=1qfAhxaNh2zGah9AQF35JLOjplJB4qxXQ",
        "https://drive.google.com/uc?export=view&id=1__yIZ-MbRX1TiWLK1uqerEU92WbvPBHh",
        "https://drive.google.com/uc?export=view&id=1loJIhnxwnh8QaKUMLtXeDf8D8I_N4FY5"
    ]
    data_list = [
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
         {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}
    ] 
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1vR91vzjU2omTqVhtKP72-HovGkFTdrTG",
        "https://drive.google.com/uc?export=view&id=1H5QGKx6l6Y-e8OWE0nVXmbuVl4Rt_dSB",
        "https://drive.google.com/uc?export=view&id=1y15WBuyGjVY7Xd2NZCECFhlU-Vm0-nkZ",
        "https://drive.google.com/uc?export=view&id=1zdAdOf8GOrSCBTiUY56_jpduvjt0rsuI",
        "https://drive.google.com/uc?export=view&id=1RMCI13NYmGVHaT3VQVfh4SL3Tk47m6CF",
        "https://drive.google.com/uc?export=view&id=1Fy4pqqKjRVE6jFcl6XRl-T92sYdTDHQM",
        "https://drive.google.com/uc?export=view&id=143oD8Py7dlZ77ssZlOA82_hCxT0DG6ym",
        "https://drive.google.com/uc?export=view&id=1nMQ-fvmI0Rp2vLvJvbWEelTFeB0snRqm",
        "https://drive.google.com/uc?export=view&id=1mgPPWEwwNx4DzSpE5gvmJj6-LKyb_iyj",
        "https://drive.google.com/uc?export=view&id=1fBT6pDA2td_9-H8c0GvvGTvcrdSO-srw",
        "https://drive.google.com/uc?export=view&id=1OJkN0JqY6tEXMtnG-r8SbMXe9d9VQQtG",
        "https://drive.google.com/uc?export=view&id=123Pve9GZmND-dRAMQDl7esXRiMEKiQeQ",
        "https://drive.google.com/uc?export=view&id=1v_Pw_sgl2g0ps7WRknO7VnHxGXJ5V3Ry",
        "https://drive.google.com/uc?export=view&id=1P3aDaDOEmZ_iNu3lx3Y060Sb3mpM1Or_",
        "https://drive.google.com/uc?export=view&id=1DLsCFea4IGFaZmdKcMftMroFr3ILqYaK",
    ]
    data_list = [
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")

