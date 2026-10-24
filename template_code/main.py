import streamlit as st
from utils import setup_common

st.set_page_config(page_title="Buku Kating", layout="wide")

# Panggil fungsi CSS untuk Sidebar (dari utils.py)
setup_common()

# ============================================================
# 🧭 NAVIGASI HALAMAN (Ikon Material)
# ============================================================
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)

# Ikon Material Person
Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="116 - Yobel", icon=":material/person:")
Mahasiswa2  = st.Page("Buku Kating/109_Rena Aprilia.py", title="109 - Rena", icon=":material/person:")
Mahasiswa3  = st.Page("Buku Kating/020_Fadhilah Adelyia Putri.py", title="020 - Fadhilah", icon=":material/person:")
Mahasiswa4  = st.Page("Buku Kating/075_Inness Eymard Gultom.py", title="075 - Inness", icon=":material/person:")
Mahasiswa5  = st.Page("Buku Kating/084_Samuel Kristian.py", title="084 - Samuel", icon=":material/person:")
Mahasiswa6  = st.Page("Buku Kating/008_Egia Ninta Pepayosa Ketaren.py", title="008 - Egia", icon=":material/person:")
Mahasiswa7  = st.Page("Buku Kating/028_Dzahra Adila Fatma.py", title="028 - Dzahra", icon=":material/person:")
Mahasiswa8  = st.Page("Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py", title="018 - Achmad", icon=":material/person:")
Mahasiswa9  = st.Page("Buku Kating/033_Kayyisah Mazaya.py", title="033 - Kayyisah", icon=":material/person:")
Mahasiswa10 = st.Page("Buku Kating/074_Alfajri Anwar.py", title="074 - Alfajri", icon=":material/person:")
Mahasiswa11 = st.Page("Buku Kating/037_Nailatun Inayah.py", title="037 - Nailatun", icon=":material/person:")

KREASI  = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

pg = st.navigation({
    "Halaman Utama": [Homepage],
    "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11],
    "Try Me !!": [KREASI, KREASII],
})

pg.run()
