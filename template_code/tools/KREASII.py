import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Data Anomaly Pro", layout="centered")

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

st.title("Data Anomaly Pro: Cleaning Mission")
st.markdown("Bersihkan dataset dari data anomali atau outlier yang merusak analisis. Jaga nyawa Anda, tingkatkan level, dan kumpulkan skor tertinggi.")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.level = 1
    st.session_state.streak = 0
    st.session_state.game_over = False

def generate_data():
    base_val = random.randint(20, 50)
    size = min(5 + st.session_state.level, 10)
    data = [base_val + random.randint(-3, 3) for _ in range(size - 1)]
    outlier_factor = random.choice([-1, 1]) * random.randint(35 + st.session_state.level * 5, 60 + st.session_state.level * 5)
    outlier_val = base_val + outlier_factor
    data.append(outlier_val)
    random.shuffle(data)
    return data

if "dataset" not in st.session_state or st.session_state.get("new_round", False):
    st.session_state.dataset = generate_data()
    st.session_state.correct_outlier = max(st.session_state.dataset, key=lambda x: abs(x - sum(st.session_state.dataset)/len(st.session_state.dataset)))
    st.session_state.new_round = False

if not st.session_state.game_over:
    col1, col2, col3 = st.columns(3)
    col1.metric("Skor", st.session_state.score)
    col2.metric("Nyawa", st.session_state.lives)
    col3.metric("Level", st.session_state.level)

    st.markdown(f"Misi Level {st.session_state.level}: Temukan nilai data yang paling menyimpang (outlier) dari tabel sampel di bawah ini.")
    
    df_display = pd.DataFrame({"ID Baris": range(len(st.session_state.dataset)), "Nilai Sampel": st.session_state.dataset})
    st.dataframe(df_display, use_container_width=True, hide_index=True)

    selected_val = st.selectbox("Pilih Nilai Outlier yang Ingin Dihapus:", st.session_state.dataset, key="outlier_select")

    if st.button("Eksekusi Pembersihan Data"):
        if selected_val == st.session_state.correct_outlier:
            st.session_state.streak += 1
            bonus = st.session_state.streak * 5
            st.session_state.score += 15 + bonus
            st.success(f"Berhasil! Anomali dibersihkan. Bonus Streak: +{bonus}")
            if st.session_state.streak % 3 == 0:
                st.session_state.level += 1
            st.session_state.new_round = True
            st.rerun()
        else:
            st.session_state.lives -= 1
            st.session_state.streak = 0
            st.error("Gagal! Nilai tersebut adalah data normal.")
            if st.session_state.lives <= 0:
                st.session_state.game_over = True
                st.rerun()
else:
    st.error("Permainan Berakhir. Nyawa Anda habis.")
    st.metric("Skor Akhir Anda", st.session_state.score)
    if st.button("Mainkan Lagi"):
        st.session_state.score = 0
        st.session_state.lives = 3
        st.session_state.level = 1
        st.session_state.streak = 0
        st.session_state.game_over = False
        st.session_state.new_round = True
        st.rerun()
