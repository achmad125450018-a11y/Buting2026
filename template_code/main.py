import streamlit as st

st.set_page_config(page_title="Buku Kating", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #701c23 !important;
    }
    [data-testid="stSidebar"] *,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# NAVIGASI (Biarkan sama seperti punyamu)
st.session_state.pindah = True
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)
# ... Mahasiswa 1-11 ...
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
