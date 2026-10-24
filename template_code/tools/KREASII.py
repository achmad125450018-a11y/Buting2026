import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="CyberData Matrix", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #030712;
    color: #ffffff;
}
h1, h2, h3 {
    color: #38bdf8 !important;
    font-family: 'Courier New', monospace;
    text-transform: uppercase;
    letter-spacing: 2px;
}
label, p, span, div {
    color: #f1f5f9 !important;
}
.data-card {
    background-color: #0f172a;
    border: 1px solid #00f0ff;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
    margin-bottom: 25px;
    text-align: center;
}
.stMetric {
    background-color: #0f172a;
    border: 1px solid #38bdf8;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("CyberData: Interactive Transfer Matrix")
st.markdown("Transfer unit data yang masuk ke terminal tipe data yang tepat.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

def get_new_item():
    types = ["Integer", "Float", "String", "Boolean", "Date"]
    t = random.choice(types)
    if t == "Integer":
        val = str(random.randint(-500, 500))
    elif t == "Float":
        val = str(round(random.uniform(-250, 250), 2))
    elif t == "String":
        val = random.choice(["CyberNode", "NeuralCore", "MatrixProtocol", "QuantumBit", "VectorStream"])
    elif t == "Boolean":
        val = str(random.choice([True, False]))
    elif t == "Date":
        val = str(date(random.randint(2025, 2030), random.randint(1, 12), random.randint(1, 28)))
    return {"value": val, "type": t}

if "current_item" not in st.session_state or not isinstance(st.session_state.current_item, dict):
    st.session_state.current_item = get_new_item()

col1, col2 = st.columns(2)
col1.metric("Skor Total", st.session_state.score)
col2.metric("Streak Beruntun", st.session_state.streak)

st.subheader("Unit Data Aktif")
item = st.session_state.current_item

st.markdown(f"""
<div class="data-card">
    <h2 style="color: #00f0ff; font-size: 36px; margin: 0;">{item['value']}</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("Pilih Terminal Kategori Tujuan untuk Mentransfer Unit Data Ini:")

c1, c2, c3, c4, c5 = st.columns(5)

chosen = None
if c1.button("Integer", use_container_width=True):
    chosen = "Integer"
elif c2.button("Float", use_container_width=True):
    chosen = "Float"
elif c3.button("String", use_container_width=True):
    chosen = "String"
elif c4.button("Boolean", use_container_width=True):
    chosen = "Boolean"
elif c5.button("Date", use_container_width=True):
    chosen = "Date"

if chosen is not None:
    if chosen == item["type"]:
        st.session_state.score += 20
        st.session_state.streak += 1
        st.success(f"Transfer sukses ke terminal {chosen}.")
    else:
        st.session_state.streak = 0
        st.session_state.score = max(0, st.session_state.score - 10)
        st.error(f"Transfer gagal. Unit tersebut adalah tipe data {item['type']}.")
    
    st.session_state.current_item = get_new_item()
    st.rerun()

st.markdown("---")
if st.button("Reset Sistem"):
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.current_item = get_new_item()
    st.rerun()
