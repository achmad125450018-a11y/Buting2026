import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title="Data Defense Matrix", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: #ffffff;
}
h1, h2, h3 {
    color: #ff2a85 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
label, p, span, div {
    color: #ffffff !important;
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

st.title("Data Defense Matrix: Cyber Pipeline Security")
st.markdown("Sesuaikan parameter filter untuk mendeteksi dan menghancurkan anomali data korup sebelum integritas sistem runtuh.")

if "integrity" not in st.session_state:
    st.session_state.integrity = 100
    st.session_state.score = 0
    st.session_state.wave = 1
    st.session_state.threats_eliminated = 0
    st.session_state.game_over = False

if not st.session_state.game_over:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Integritas Sistem", f"{st.session_state.integrity} %")
    col2.metric("Skor Pertahanan", st.session_state.score)
    col3.metric("Gelombang", st.session_state.wave)
    col4.metric("Anomali Dibasmi", st.session_state.threats_eliminated)

    st.subheader("Kalibrasi Sensor Filter")
    threshold = st.slider("Ambang Batas Filter (Threshold)", 10.0, 100.0, 50.0, 1.0)
    sensitivity = st.slider("Sensitivitas Deteksi", 1, 10, 5, 1)

    if "matrix_data" not in st.session_state or st.session_state.get("refresh_matrix", False):
        np.random.seed()
        data_vals = [random.randint(5, 95) for _ in range(6)]
        corrupt_val = random.randint(120, 200)
        full_data = data_vals + [corrupt_val]
        random.shuffle(full_data)
        st.session_state.matrix_data = full_data
        st.session_state.actual_corrupt = corrupt_val
        st.session_state.refresh_matrix = False

    st.markdown("Matriks Aliran Data Aktif:")
    df_grid = pd.DataFrame({"ID Node": range(len(st.session_state.matrix_data)), "Nilai Signal": st.session_state.matrix_data})
    st.dataframe(df_grid, use_container_width=True, hide_index=True)

    target_node = st.selectbox("Pilih Node untuk Diisolasi dan Purge:", st.session_state.matrix_data)

    if st.button("Jalankan Purge Protocol"):
        if target_node == st.session_state.actual_corrupt:
            st.session_state.score += 50 * st.session_state.wave
            st.session_state.threats_eliminated += 1
            if st.session_state.threats_eliminated % 3 == 0:
                st.session_state.wave += 1
            st.success("Anomali korup berhasil diisolasi dan dihancurkan.")
            st.session_state.refresh_matrix = True
            st.rerun()
        else:
            st.session_state.integrity -= 25
            st.error("Gagal! Node yang dipilih adalah data normal. Integritas sistem menurun.")
            if st.session_state.integrity <= 0:
                st.session_state.game_over = True
                st.rerun()
            else:
                st.session_state.refresh_matrix = True
                st.rerun()
else:
    st.error("Sistem Runtuh! Integritas mencapai 0 persen.")
    st.metric("Skor Akhir Pertahanan", st.session_state.score)
    if st.button("Inisialisasi Ulang Sistem"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
