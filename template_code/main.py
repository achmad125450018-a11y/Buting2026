import streamlit as st

st.set_page_config(page_title="Buku Kating", layout="wide")

# ============================================================
# 🎨 CSS GLOBAL (Sidebar + Sembunyikan Teks "key")
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

/* 1. Warna & Font Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #701c23 0%, #4e1318 100%) !important;
}
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] svg {
    color: #ffffff !important;
    fill: #ffffff !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] strong {
    font-family: 'Playfair Display', serif !important;
}

/* 2. 💥 HAPUS TOTAL TEKS "KEY" & MENU BAWAAN STREAMLIT 💥 */
header, 
[data-testid="stHeader"], 
#MainMenu, 
.stAppDeployButton,
[data-testid="stStatusWidget"],
[data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
}

/* 3. Sembunyikan tooltip/popover yang mungkin muncul */
div[data-baseweb="popover"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 🧭 NAVIGASI HALAMAN
# ============================================================
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)

Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="Yobel (116)")
Mahasiswa2  = st.Page("Buku Kating/109_Rena Aprilia.py", title="Rena (109)")
Mahasiswa3  = st.Page("Buku Kating/020_Fadhilah Adelyia Putri.py", title="Fadhilah (020)")
Mahasiswa4  = st.Page("Buku Kating/075_Inness Eymard Gultom.py", title="Inness (075)")
Mahasiswa5  = st.Page("Buku Kating/084_Samuel Kristian.py", title="Samuel (084)")
Mahasiswa6  = st.Page("Buku Kating/008_Egia Ninta Pepayosa Ketaren.py", title="Egia (008)")
Mahasiswa7  = st.Page("Buku Kating/028_Dzahra Adila Fatma.py", title="Dzahra (028)")
Mahasiswa8  = st.Page("Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py", title="Achmad (018)")
Mahasiswa9  = st.Page("Buku Kating/033_Kayyisah Mazaya.py", title="Kayyisah (033)")
Mahasiswa10 = st.Page("Buku Kating/074_Alfajri Anwar.py", title="Alfajri (074)")
Mahasiswa11 = st.Page("Buku Kating/037_Nailatun Inayah.py", title="Nailatun (037)")

KREASI  = st.Page("tools/KREASI.py", title="KREASI")
KREASII = st.Page("tools/KREASII.py", title="KREASII")

pg = st.navigation({
    "Halaman Utama": [Homepage],
    "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5,
                    Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11],
    "Try Me !!": [KREASI, KREASII],
})

pg.run()
