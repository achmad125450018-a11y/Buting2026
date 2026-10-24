import streamlit as st
import random

st.set_page_config(page_title="Data Sorter Game", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #f8f9fa;
    color: #111111;
}
h1, h2, h3 {
    color: #1f77b4 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
label, p, span, div {
    color: #111111 !important;
}
.stMetric {
    background-color: #ffffff;
    border: 1px solid #dcdcdc;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #1f77b4 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Data Sorter: Klasifikasi Kategori Data")
st.markdown("Pilah nilai data yang muncul ke dalam kategori yang tepat berdasarkan rentang nilainya.")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_data = random.randint(1, 100)
    st.session_state.round = 1

st.subheader(f"Ronde {st.session_state.round}")
st.markdown("Nilai Data yang Harus Diklasifikasikan:")
st.markdown(f"<h1 style='text-align: center; color: #d62728;'>{st.session_state.current_data}</h1>", unsafe_allow_html=True)

st.markdown("Pilih Kategori yang Sesuai:")
col1, col2 = st.columns(2)

with col1:
    if st.button("Kategori Rendah (1 - 50)", use_container_width=True):
        if st.session_state.current_data <= 50:
            st.session_state.score += 10
            st.success("Benar. Data berhasil dikelompokkan ke Kategori Rendah.")
        else:
            st.error("Salah. Nilai ini seharusnya masuk ke Kategori Tinggi.")
        st.session_state.current_data = random.randint(1, 100)
        st.session_state.round += 1
        st.rerun()

with col2:
    if st.button("Kategori Tinggi (51 - 100)", use_container_width=True):
        if st.session_state.current_data > 50:
            st.session_state.score += 10
            st.success("Benar. Data berhasil dikelompokkan ke Kategori Tinggi.")
        else:
            st.error("Salah. Nilai ini seharusnya masuk ke Kategori Rendah.")
        st.session_state.current_data = random.randint(1, 100)
        st.session_state.round += 1
        st.rerun()

st.metric("Skor Anda", st.session_state.score)

if st.button("Reset Permainan"):
    st.session_state.score = 0
    st.session_state.current_data = random.randint(1, 100)
    st.session_state.round = 1
    st.rerun()
