import streamlit as st
from utils import setup_common

st.set_page_config(page_title="Buku Kating", layout="wide")

# Panggil CSS Sidebar
setup_common()

# Navigasi Halaman
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)

# 💥 Judul diubah (Nama dulu, baru NIM) agar ikon tidak bertabrakan
Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="Yobel (116)", icon=":material/person:")
Mahasiswa2  = st.Page("Buku Kating/109_Rena Aprilia.py", title="Rena (109)", icon=":material/person:")
Mahasiswa3  = st.Page("Buku Kating/020_Fadhilah Adelyia Putri.py", title="Fadhilah (020)", icon=":material/person:")
Mahasiswa4  = st.Page("Buku Kating/075_Inness Eymard Gultom.py", title="Inness (075)", icon=":material/person:")
Mahasiswa5  = st.Page("Buku Kating/084_Samuel Kristian.py", title="Samuel (084)", icon=":material/person:")
Mahasiswa6  = st.Page("Buku Kating/008_Egia Ninta Pepayosa Ketaren.py", title="Egia (008)", icon=":material/person:")
Mahasiswa7  = st.Page("Buku Kating/028_Dzahra Adila Fatma.py", title="Dzahra (028)", icon=":material/person:")
Mahasiswa8  = st.Page("Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py", title="Achmad (018)", icon=":material/person:")
Mahasiswa9  = st.Page("Buku Kating/033_Kayyisah Mazaya.py", title="Kayyisah (033)", icon=":material/person:")
Mahasiswa10 = st.Page("Buku Kating/074_Alfajri Anwar.py", title="Alfajri (074)", icon=":material/person:")
Mahasiswa11 = st.Page("Buku Kating/037_Nailatun Inayah.py", title="Nailatun (037)", icon=":material/person:")

KREASI  = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

pg = st.navigation({
    "Halaman Utama": [Homepage],
    "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11],
    "Try Me !!": [KREASI, KREASII],
})

pg.run()
