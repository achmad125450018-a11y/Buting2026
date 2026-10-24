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
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.15);
    margin-bottom: 20px;
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
st.markdown("Pindahkan setiap unit data masuk ke dalam slot terminal kategori tipe data yang sesuai.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "items" not in st.session_state or not isinstance(st.session_state.items, list):
    st.session_state.items = []

def generate_items():
    types = ["Integer", "Float", "String", "Boolean", "Date"]
    new_items = []
    for i in range(3):
        t = random.choice(types)
        if t == "Integer":
            val = str(random.randint(-300, 300))
        elif t == "Float":
            val = str(round(random.uniform(-150, 150), 2))
        elif t == "String":
            val = random.choice(["CyberMatrix", "NeuralNet", "Protocol", "Quantum", "Vector"])
        elif t == "Boolean":
            val = str(random.choice([True, False]))
        elif t == "Date":
            val = str(date(random.randint(2025, 2028), random.randint(1, 12), random.randint(1, 28)))
        new_items.append({"id": random.randint(10000, 99999), "value": val, "type": t})
    return new_items

if not st.session_state.items:
    st.session_state.items = generate_items()

col_m1, col_m2 = st.columns(2)
col_m1.metric("Skor Total", st.session_state.score)
col_m2.metric("Ronde Sistem", st.session_state.round)

st.subheader("Terminal Antrian Data Masuk")

remaining_items = list(st.session_state.items)
action_triggered = False

for item in st.session_state.items:
    st.markdown(f"""
    <div class="data-card">
        <h3>Unit Data: <span style="color: #38bdf8;">{item['value']}</span></h3>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    
    chosen_target = None
    if c1.button("Integer", key=f"int_{item['id']}", use_container_width=True):
        chosen_target = "Integer"
    elif c2.button("Float", key=f"float_{item['id']}", use_container_width=True):
        chosen_target = "Float"
    elif c3.button("String", key=f"str_{item['id']}", use_container_width=True):
        chosen_target = "String"
    elif c4.button("Boolean", key=f"bool_{item['id']}", use_container_width=True):
        chosen_target = "Boolean"
    elif c5.button("Date", key=f"date_{item['id']}", use_container_width=True):
        chosen_target = "Date"
        
    if chosen_target is not None:
        if chosen_target == item['type']:
            st.session_state.score += 25
            st.success(f"Transfer berhasil ke terminal {chosen_target}.")
        else:
            st.session_state.score = max(0, st.session_state.score - 10)
            st.error(f"Transfer gagal. Unit seharusnya menuju terminal {item['type']}.")
        
        remaining_items = [i for i in remaining_items if i['id'] != item['id']]
        action_triggered = True
        break

if action_triggered:
    st.session_state.items = remaining_items
    st.rerun()

if not st.session_state.items:
    st.success("Semua unit data berhasil diproses. Memuat gelombang baru...")
    st.session_state.round += 1
    st.session_state.items = generate_items()
    st.rerun()

st.markdown("---")
if st.button("Reset Sistem Matrix"):
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.items = generate_items()
    st.rerun()
