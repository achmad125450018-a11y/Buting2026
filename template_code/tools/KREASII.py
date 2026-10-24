import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="Data Pipeline Sorter", layout="centered")

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

st.title("Data Pipeline: Interactive Batch Sorter")
st.markdown("Pindahkan dan klasifikasikan sekumpulan item data ke dalam kategori tipe data yang benar pada setiap wadah pemrosesan.")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.batch_items = []

def generate_batch():
    types = ["Integer", "Float", "String", "Boolean", "Date"]
    batch = []
    for _ in range(4):
        t = random.choice(types)
        if t == "Integer":
            val = str(random.randint(-100, 100))
        elif t == "Float":
            val = str(round(random.uniform(-50, 50), 2))
        elif t == "String":
            val = random.choice(["Dataset", "Python", "Streamlit", "Model", "Query"])
        elif t == "Boolean":
            val = str(random.choice([True, False]))
        elif t == "Date":
            val = str(date(random.randint(2023, 2026), random.randint(1, 12), random.randint(1, 28)))
        batch.append({"value": val, "type": t})
    return batch

if not st.session_state.batch_items:
    st.session_state.batch_items = generate_batch()

col1, col2 = st.columns(2)
col1.metric("Skor Total", st.session_state.score)
col2.metric("Ronde Aktif", st.session_state.round)

st.subheader("Kotak Masuk Data (Unsorted Batch)")
st.markdown("Tentukan kategori wadah yang tepat untuk setiap item data di bawah ini:")

user_choices = {}
type_options = ["Integer", "Float", "String", "Boolean", "Date"]

for idx, item in enumerate(st.session_state.batch_items):
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(f"**Item {idx+1}: {item['value']}**")
    with c2:
        user_choices[idx] = st.selectbox(f"Pilih Kategori Wadah Item {idx+1}", type_options, key=f"item_{st.session_state.round}_{idx}")

if st.button("Proses dan Pindahkan ke Kategori"):
    correct_count = 0
    for idx, item in enumerate(st.session_state.batch_items):
        if user_choices[idx] == item["type"]:
            correct_count += 1
    
    earned_score = correct_count * 10
    st.session_state.score += earned_score
    
    if correct_count == len(st.session_state.batch_items):
        st.success(f"Luar biasa! Semua {correct_count} item berhasil dipindahkan ke wadah yang tepat. Poin diperoleh: +{earned_score}.")
    else:
        st.warning(f"Berhasil memindahkan {correct_count} dari {len(st.session_state.batch_items)} item dengan benar. Poin diperoleh: +{earned_score}.")
    
    st.session_state.round += 1
    st.session_state.batch_items = generate_batch()
    st.rerun()

st.markdown("---")
if st.button("Reset Batch Permainan"):
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.batch_items = generate_batch()
    st.rerun()
