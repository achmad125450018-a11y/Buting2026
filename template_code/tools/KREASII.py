import streamlit as st
import random

st.set_page_config(page_title="DataOps Tycoon", layout="wide")

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
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    background-color: #141414;
    border-radius: 4px;
    color: #ffffff;
    border: 1px solid #ff2a85;
}
.stTabs [aria-selected="true"] {
    background-color: #ff2a85 !important;
    color: #0b0b0b !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("DataOps Tycoon: ML Pipeline Challenge")
st.markdown("Kelola pipeline data science Anda. Bersihkan dataset, rekayasa fitur, latih model, dan capai akurasi 95 persen sebelum anggaran atau energi habis.")

if "budget" not in st.session_state:
    st.session_state.budget = 1000
    st.session_state.energy = 100
    st.session_state.accuracy = 40.0
    st.session_state.cleanliness = 50
    st.session_state.features = 2
    st.session_state.epochs = 0
    st.session_state.game_status = "playing"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Anggaran", f"$ {st.session_state.budget}")
col2.metric("Energi", f"{st.session_state.energy} %")
col3.metric("Akurasi Model", f"{st.session_state.accuracy:.1f} %")
col4.metric("Epoch", st.session_state.epochs)

if st.session_state.game_status == "playing":
    st.subheader("Pilih Aksi Pipeline")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Pembersihan Data", "Rekayasa Fitur", "Latih Model", "Tuning Hyperparameter"])
    
    with tab1:
        st.markdown("Tingkatkan kualitas data untuk mengurangi error.")
        if st.button("Jalankan Data Cleaning (-$100, -15 Energi)"):
            if st.session_state.budget >= 100 and st.session_state.energy >= 15:
                st.session_state.budget -= 100
                st.session_state.energy -= 15
                st.session_state.cleanliness = min(100, st.session_state.cleanliness + 20)
                st.session_state.accuracy = min(95.0, st.session_state.accuracy + random.uniform(5, 12))
                st.success("Data berhasil dibersihkan.")
                st.rerun()
            else:
                st.error("Anggaran atau energi tidak mencukupi.")

    with tab2:
        st.markdown("Tambahkan fitur baru untuk memperkaya informasi model.")
        if st.button("Tambah Fitur Baru (-$150, -20 Energi)"):
            if st.session_state.budget >= 150 and st.session_state.energy >= 20:
                st.session_state.budget -= 150
                st.session_state.energy -= 20
                st.session_state.features += 1
                st.session_state.accuracy = min(95.0, st.session_state.accuracy + random.uniform(8, 15))
                st.success("Fitur baru berhasil diekstrak.")
                st.rerun()
            else:
                st.error("Anggaran atau energi tidak mencukupi.")

    with tab3:
        st.markdown("Latih model machine learning menggunakan data yang ada.")
        if st.button("Latih Epoch (-$50, -25 Energi)"):
            if st.session_state.budget >= 50 and st.session_state.energy >= 25:
                st.session_state.budget -= 50
                st.session_state.energy -= 25
                st.session_state.epochs += 1
                gain = (st.session_state.cleanliness / 100) * (st.session_state.features * 2.5)
                st.session_state.accuracy = min(95.0, st.session_state.accuracy + gain)
                st.success("Pelatihan epoch selesai.")
                st.rerun()
            else:
                st.error("Anggaran atau energi tidak mencukupi.")

    with tab4:
        st.markdown("Optimalkan parameter model untuk loncatan akurasi tinggi.")
        if st.button("Tuning Grid Search (-$200, -30 Energi)"):
            if st.session_state.budget >= 200 and st.session_state.energy >= 30:
                st.session_state.budget -= 200
                st.session_state.energy -= 30
                if random.random() > 0.3:
                    st.session_state.accuracy = min(95.0, st.session_state.accuracy + random.uniform(15, 25))
                    st.success("Tuning sukses besar.")
                else:
                    st.session_state.accuracy = max(10.0, st.session_state.accuracy - 10.0)
                    st.error("Overfitting terjadi, akurasi menurun.")
                st.rerun()
            else:
                st.error("Anggaran atau energi tidak mencukupi.")

    if st.session_state.accuracy >= 95.0:
        st.session_state.game_status = "won"
        st.rerun()
    elif st.session_state.budget <= 0 or st.session_state.energy <= 0:
        st.session_state.game_status = "lost"
        st.rerun()

elif st.session_state.game_status == "won":
    st.success("Selamat! Anda berhasil mencapai target akurasi 95% dan menyelesaikan proyek machine learning.")
    if st.button("Mulai Proyek Baru"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

else:
    st.error("Proyek Gagal. Anggaran atau energi Anda habis sebelum mencapai target akurasi.")
    if st.button("Coba Lagi"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
