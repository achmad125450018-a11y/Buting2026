import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Data Outlier Hunter", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: #f1f1f1;
}
h1, h2, h3 {
    color: #ff2a85 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
.stMetric {
    background-color: #141414;
    border: 1px solid #ff2a85;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #ff2a85 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Data Outlier Hunter")
st.markdown("Temukan dan identifikasi data anomali atau outlier dari sampel yang diberikan untuk membersihkan dataset.")

if "correct_outlier" not in st.session_state:
    normal_data = [random.randint(10, 30) for _ in range(4)]
    outlier_val = random.randint(80, 150)
    st.session_state.dataset = normal_data + [outlier_val]
    random.shuffle(st.session_state.dataset)
    st.session_state.correct_outlier = outlier_val
    st.session_state.score = 0
    st.session_state.round = 1

st.subheader(f"Misi Ronde {st.session_state.round}")
st.markdown("Berikut adalah tabel sampel data yang perlu dianalisis:")

df_display = pd.DataFrame({"Indeks": range(len(st.session_state.dataset)), "Nilai Data": st.session_state.dataset})
st.dataframe(df_display, use_container_width=True, hide_index=True)

selected_val = st.selectbox("Pilih Nilai yang Merupakan Outlier:", st.session_state.dataset)

if st.button("Verifikasi Data"):
    if selected_val == st.session_state.correct_outlier:
        st.success("Benar. Anda berhasil mendeteksi data anomali.")
        st.session_state.score += 10
        normal_data = [random.randint(10, 30) for _ in range(4)]
        outlier_val = random.randint(80, 150)
        st.session_state.dataset = normal_data + [outlier_val]
        random.shuffle(st.session_state.dataset)
        st.session_state.correct_outlier = outlier_val
        st.session_state.round += 1
        st.rerun()
    else:
        st.error("Salah. Nilai tersebut adalah data normal.")

st.metric("Skor Total", st.session_state.score)

if st.button("Reset Permainan"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
