import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="Data Pipeline Matrix", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #f8fafc;
    color: #0f172a;
}
h1, h2, h3 {
    color: #1e3a8a !important;
    font-family: 'Inter', sans-serif;
}
label, p, span, div {
    color: #0f172a !important;
}
.data-card {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    margin-bottom: 15px;
}
.stMetric {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}
[data-testid="stMetricValue"] {
    color: #2563eb !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Data Pipeline: Interactive Transfer Matrix")
st.markdown("Pindahkan setiap item data dari aliran masuk ke dalam wadah kategori tipe data yang sesuai secara interaktif.")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.items = []
    st.session_state.round = 1

def generate_items():
    types = ["Integer", "Float", "String", "Boolean", "Date"]
    items = []
    for i in range(3):
        t = random.choice(types)
        if t == "Integer":
            val = str(random.randint(-200, 200))
        elif t == "Float":
            val = str(round(random.uniform(-100, 100), 2))
        elif t == "String":
            val = random.choice(["Streamlit", "Analytics", "Pipeline", "Dataset", "Tensor"])
        elif t == "Boolean":
            val = str(random.choice([True, False]))
        elif t == "Date":
            val = str(date(random.randint(2024, 2026), random.randint(1, 12), random.randint(1, 28)))
        items.append({"id": i, "value": val, "type": t})
    return items

if not st.session_state.items:
    st.session_state.items = generate_items()

col_m1, col_m2 = st.columns(2)
col_m1.metric("Skor Total", st.session_state.score)
col_m2.metric("Ronde Aktif", st.session_state.round)

st.subheader("Aliran Data Masuk (Incoming Stream)")

remaining_items = []
for item in st.session_state.items:
    st.markdown(f"""
    <div class="data-card">
        <h4>Item Data: <b>{item['value']}</b></h4>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    
    moved = False
    target = None
    if c1.button("Integer", key=f"int_{item['id']}_{st.session_state.round}", use_container_width=True):
        target = "Integer"
        moved = True
    if c2.button("Float", key=f"float_{item['id']}_{st.session_state.round}", use_container_width=True):
        target = "Float"
        moved = True
    if c3.button("String", key=f"str_{item['id']}_{st.session_state.round}", use_container_width=True):
        target = "String"
        moved = True
    if c4.button("Boolean", key=f"bool_{item['id']}_{st.session_state.round}", use_container_width=True):
        target = "Boolean"
        moved = True
    if c5.button("Date", key=f"date_{item['id']}_{st.session_state.round}", use_container_width=True):
        target = "Date"
        moved = True
        
    if moved:
        if target == item['type']:
            st.session_state.score += 20
            st.success(f"Berhasil memindahkan {item['value']} ke wadah {target}.")
        else:
            st.session_state.score = max(0, st.session_state.score - 10)
            st.error(f"Gagal! {item['value']} seharusnya masuk ke wadah {item['type']}.")
    else:
        remaining_items.append(item)

st.session_state.items = remaining_items

if not st.session_state.items:
    st.success("Semua item batch ini selesai dipindahkan. Memuat batch baru...")
    st.session_state.round += 1
    st.session_state.items = generate_items()
    st.rerun()

st.markdown("---")
if st.button("Reset Permainan"):
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.items = generate_items()
    st.rerun()
