import streamlit as st
from utils import setup_common # <-- Panggil dari utils

st.set_page_config(page_title="Buku Kating", layout="wide")

# 💥 Cukup panggil ini, Sidebar otomatis putih bersih di semua halaman
setup_common()

# ============================================================
# 🧭 NAVIGASI HALAMAN
# ============================================================
st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)
Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="116 - Yobel Imanuel Pasaribu", icon=":material/person:")
# ... (Biarkan daftar Mahasiswa 2-11 seperti aslinya) ...
KREASI  = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

if st.session_state.pindah:
    pg = st.navigation({
        "Halaman Utama": [Homepage],
        "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5,
                        Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11],
        "Try Me !!": [KREASI, KREASII],
    })
else:
    st.write("Maaf Anda kurang beruntung :(")

pg.run()
