import streamlit as st

st.set_page_config(page_title="Buku Kating", layout="wide")

# ============================================================
# 🎨 CSS GLOBAL & JAVASCRIPT HACK
# ============================================================
st.markdown("""
<style>
    /* 1. Warna Sidebar */
    [data-testid="stSidebar"] {
        background-color: #701c23 !important;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        fill: #ffffff !important;
    }

    /* 2. 💥 HANCURKAN BATAS LEBAR STREAMLIT 💥 */
    [data-testid="stAppViewBlockContainer"], .block-container {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    iframe[title="streamlit_component"] {
        width: 100% !important;
        max-width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 💥 JAVASCRIPT HACK (Ini yang wajib biar game lebar) 💥
st.components.v1.html("""
<script>
    const observer = new MutationObserver(() => {
        const iframes = window.parent.document.querySelectorAll('iframe[title="streamlit_component"]');
        iframes.forEach(iframe => {
            iframe.style.width = '100%';
            iframe.style.maxWidth = '100%';
            iframe.style.height = '600px'; 
            
            let parent = iframe.parentElement;
            while (parent) {
                parent.style.maxWidth = '100%';
                parent.style.width = '100%';
                parent = parent.parentElement;
            }
        });
    });
    observer.observe(window.parent.document.body, { childList: true, subtree: true });
</script>
""", height=0, width=0)

# ============================================================
# 🧭 NAVIGASI HALAMAN
# ============================================================
st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)
Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="116 - Yobel Imanuel Pasaribu", icon=":material/person:")
Mahasiswa2  = st.Page("Buku Kating/109_Rena Aprilia.py", title="109 - Rena Aprilia", icon=":material/person:")
Mahasiswa3  = st.Page("Buku Kating/020_Fadhilah Adelyia Putri.py", title="020 - Fadhilah Adelyia Putri", icon=":material/person:")
Mahasiswa4  = st.Page("Buku Kating/075_Inness Eymard Gultom.py", title="075 - Inness Eymard Gultom", icon=":material/person:")
Mahasiswa5  = st.Page("Buku Kating/084_Samuel Kristian.py", title="084 - Samuel Kristian", icon=":material/person:")
Mahasiswa6  = st.Page("Buku Kating/008_Egia Ninta Pepayosa Ketaren.py", title="008 - Egia Ninta Pepayosa Ketaren", icon=":material/person:")
Mahasiswa7  = st.Page("Buku Kating/028_Dzahra Adila Fatma.py", title="028 - Dzahra Adila Fatma", icon=":material/person:")
Mahasiswa8  = st.Page("Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py", title="018 - Achmad Fardhan Al Basri Bandarudin", icon=":material/person:")
Mahasiswa9  = st.Page("Buku Kating/033_Kayyisah Mazaya.py", title="033 - Kayyisah Mazaya", icon=":material/person:")
Mahasiswa10 = st.Page("Buku Kating/074_Alfajri Anwar.py", title="074 - Alfajri Anwar", icon=":material/person:")
Mahasiswa11 = st.Page("Buku Kating/037_Nailatun Inayah.py", title="037 - Nailatun Inayah", icon=":material/person:")

KREASI  = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

# ============================================================
# 🚀 JALANKAN APLIKASI
# ============================================================
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
