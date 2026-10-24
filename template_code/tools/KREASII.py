import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="CosWave Challenge", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: #e5e5e5;
}
[data-testid="stSidebar"] {
    background-color: #141414;
    color: #d4af37;
}
h1, h2, h3 {
    color: #ffd700 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
.stMetric {
    background-color: #161616;
    border: 1px solid #d4af37;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #ffd700 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("CosWave Target Challenge")
st.markdown("Sesuaikan sudut untuk mencocokkan nilai target cosinus yang ditentukan.")

if "target_cos" not in st.session_state:
    st.session_state.target_cos = round(random.uniform(-1, 1), 2)

col1, col2 = st.columns(2)
with col1:
    st.metric("Target Nilai Cosinus", st.session_state.target_cos)
with col2:
    if st.button("Acak Target Baru"):
        st.session_state.target_cos = round(random.uniform(-1, 1), 2)
        st.rerun()

angle_deg = st.slider("Pilih Sudut (Derajat)", 0, 360, 0, 1)
angle_rad = np.radians(angle_deg)
current_cos = round(float(np.cos(angle_rad)), 2)

diff = round(abs(current_cos - st.session_state.target_cos), 2)

st.metric("Nilai Cosinus Anda", current_cos, delta=f"Selisih: {diff}", delta_color="inverse")

if diff <= 0.03:
    st.success("Target Berhasil Dicapai")
else:
    st.warning("Geser sudut untuk mendekati nilai target")

x = np.linspace(0, 360, 361)
y = np.cos(np.radians(x))
chart_data = {"Sudut": x, "Cosinus": y}
st.line_chart(chart_data, x="Sudut", y="Cosinus", color=["#ffd700"])
