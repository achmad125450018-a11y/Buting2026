import streamlit as st
import importlib.util
import sys
import os

st.set_page_config(page_title="Buku Kating", layout="wide")

# ============================================================
# CSS SIDEBAR
# ============================================================
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


# ============================================================
# DAFTAR HALAMAN (path + judul)
# ============================================================
HALAMAN = {
    "07 - POISSON": "Halaman Utama/halaman_utama.py",
    "116 - Yobel Imanuel Pasaribu": "Buku Kating/116_Yobel Imanuel Pasaribu.py",
    "109 - Rena Aprilia": "Buku Kating/109_Rena Aprilia.py",
    "020 - Fadhilah Adelyia Putri": "Buku Kating/020_Fadhilah Adelyia Putri.py",
    "075 - Inness Eymard Gultom": "Buku Kating/075_Inness Eymard Gultom.py",
    "084 - Samuel Kristian": "Buku Kating/084_Samuel Kristian.py",
    "008 - Egia Ninta Pepayosa Ketaren": "Buku Kating/008_Egia Ninta Pepayosa Ketaren.py",
    "028 - Dzahra Adila Fatma": "Buku Kating/028_Dzahra Adila Fatma.py",
    "018 - Achmad Fardhan Al Basri Bandarudin": "Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py",
    "033 - Kayyisah Mazaya": "Buku Kating/033_Kayyisah Mazaya.py",
    "074 - Alfajri Anwar": "Buku Kating/074_Alfajri Anwar.py",
    "037 - Nailatun Inayah": "Buku Kating/037_Nailatun Inayah.py",
    "KREASI": "tools/KREASI.py",
    "KREASII": "tools/KREASII.py",
}


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
# Init halaman aktif
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "07 - POISSON"

with st.sidebar:
    st.markdown("### 📖 Buku Kating")

    # Group: Halaman Utama
    st.markdown("**Halaman Utama**")
    if st.button("🏠 07 - POISSON", use_container_width=True,
                 type="primary" if st.session_state.halaman_aktif == "07 - POISSON" else "secondary"):
        st.session_state.halaman_aktif = "07 - POISSON"
        st.rerun()

    # Group: Buku Kating
    st.markdown("**Buku Kating**")
    anggota_list = [
        "116 - Yobel Imanuel Pasaribu",
        "109 - Rena Aprilia",
        "020 - Fadhilah Adelyia Putri",
        "075 - Inness Eymard Gultom",
        "084 - Samuel Kristian",
        "008 - Egia Ninta Pepayosa Ketaren",
        "028 - Dzahra Adila Fatma",
        "018 - Achmad Fardhan Al Basri Bandarudin",
        "033 - Kayyisah Mazaya",
        "074 - Alfajri Anwar",
        "037 - Nailatun Inayah",
    ]
    for nama in anggota_list:
        is_active = st.session_state.halaman_aktif == nama
        if st.button(f"👤 {nama}", key=f"btn_{nama}", use_container_width=True,
                     type="primary" if is_active else "secondary"):
            st.session_state.halaman_aktif = nama
            st.rerun()

    # Group: Try Me
    st.markdown("**Try Me !!**")
    for nama in ["KREASI", "KREASII"]:
        is_active = st.session_state.halaman_aktif == nama
        if st.button(f"🔍 {nama}", key=f"btn_{nama}", use_container_width=True,
                     type="primary" if is_active else "secondary"):
            st.session_state.halaman_aktif = nama
            st.rerun()


# ============================================================
# LAZY LOAD — cuma import file yang dipilih
# ============================================================
def load_page(path):
    """Load file .py secara dinamis → hanya saat dibutuhkan."""
    if not os.path.exists(path):
        st.error(f"File tidak ditemukan: {path}")
        return None

    # Buat modul unik supaya tidak bentrok
    mod_name = path.replace("/", "_").replace(".py", "").replace(" ", "_").replace("-", "_")
    if mod_name in sys.modules:
        # Sudah pernah di-load → pakai yang ada
        return sys.modules[mod_name]

    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        st.error(f"Gagal load file: {path}")
        return None

    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        st.error(f"Error saat load {path}: {e}")
        return None
    return module


# ============================================================
# RENDER HALAMAN YANG DIPILIH
# ============================================================
halaman_sekarang = st.session_state.halaman_aktif
path_sekarang = HALAMAN.get(halaman_sekarang)

if path_sekarang:
    load_page(path_sekarang)
else:
    st.error(f"Halaman tidak dikenal: {halaman_sekarang}")
