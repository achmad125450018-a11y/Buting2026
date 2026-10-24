# ============================================================
# 🎨 SETUP SIDEBAR & HALAMAN UTAMA
# ============================================================
SIDEBAR_CSS = """
<style>
/* 1. Import Font ke dalam Sidebar */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #701c23 0%, #4e1318 100%) !important;
}

/* 2. Paksa Warna Putih & Terapkan Font */
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] svg {
    color: #ffffff !important;
    fill: #ffffff !important;
    font-family: 'Inter', sans-serif !important;
}

/* 3. Khusus Judul di Sidebar pakai Playfair */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] [data-testid="stSidebarNav"] strong {
    font-family: 'Playfair Display', serif !important;
}

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #f4f0eb; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #701c23, #a8323d);
    border-radius: 10px;
    border: 2px solid #f4f0eb;
}
</style>
"""

def setup_common():
    """Inject Sidebar CSS di semua halaman."""
    st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

def setup_halaman_utama_css(custom_css: str):
    """Inject Sidebar CSS + Custom CSS Halaman Utama."""
    setup_common()
    st.markdown(custom_css, unsafe_allow_html=True)
