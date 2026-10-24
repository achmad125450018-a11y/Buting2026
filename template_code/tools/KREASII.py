import streamlit as st
import random
import time

st.set_page_config(page_title="CyberAnomaly Time-Attack", layout="centered")

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
.stMetric {
    background-color: #0f172a;
    border: 1px solid #38bdf8;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
}
.stButton>button {
    background-color: #0f172a !important;
    color: #38bdf8 !important;
    border: 1px solid #38bdf8 !important;
    font-family: 'Courier New', monospace !important;
    font-weight: bold !important;
    font-size: 13px !important;
    width: 100%;
    padding: 12px;
    border-radius: 8px;
}
.stButton>button:hover {
    background-color: #1e293b !important;
    border-color: #00f0ff !important;
    color: #00f0ff !important;
}
</style>
""", unsafe_allow_html=True)

st.title("CyberAnomaly: Time-Attack Matrix")
st.markdown("Isolasi anomali data dalam matriks 4x4 yang kompleks sebelum batas waktu habis.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

TIME_LIMIT = 15

def generate_matrix_puzzle():
    types_pool = [
        ("Integer", [str(random.randint(100, 999)) for _ in range(15)]),
        ("Float", [str(round(random.uniform(10.0, 99.9), 2)) for _ in range(15)]),
        ("String", ["NodeA", "NodeB", "Alpha", "Beta", "Gamma", "Delta", "Omega", "Zero", "Core", "Nexus", "Vector", "Stream", "Buffer", "Packet", "Matrix"]),
        ("Boolean", ["True", "False"])
    ]
    
    dom_idx = random.randint(0, len(types_pool) - 1)
    dom_name, dom_vals = types_pool[dom_idx]
    
    anom_pool = [t for i, t in enumerate(types_pool) if i != dom_idx]
    anom_name, anom_vals = random.choice(anom_pool)
    
    grid_size = 16
    items = []
    for _ in range(grid_size - 1):
        items.append({"val": random.choice(dom_vals), "type": dom_name, "is_anom": False})
        
    items.append({"val": random.choice(anom_vals), "type": anom_name, "is_anom": True})
    random.shuffle(items)
    return dom_name, anom_name, items

if "puzzle_data" not in st.session_state or not isinstance(st.session_state.puzzle_data, tuple):
    st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_matrix_puzzle()
    st.session_state.start_time = time.time()

elapsed = time.time() - st.session_state.start_time
time_left = max(0, TIME_LIMIT - int(elapsed))

if time_left == 0:
    st.session_state.streak = 0
    st.session_state.score = max(0, st.session_state.score - 20)
    st.error("Waktu habis! Sanksi penalti waktu diberlakukan.")
    st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_matrix_puzzle()
    st.session_state.start_time = time.time()
    st.rerun()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Skor Total", st.session_state.score)
col2.metric("Streak", st.session_state.streak)
col3.metric("Ronde", st.session_state.round)
col4.metric("Waktu", f"{time_left}s")

st.markdown("---")
st.markdown(f"### Misi Matrix: Cari tipe <span style='color: #00f0ff;'>{st.session_state.anom_name}</span> di antara dominasi tipe <span style='color: #38bdf8;'>{st.session_state.dom_name}</span>!", unsafe_allow_html=True)

items = st.session_state.puzzle_items
for row in range(4):
    cols = st.columns(4)
    for col in range(4):
        idx = row * 4 + col
        if idx < len(items):
            item = items[idx]
            with cols[col]:
                if st.button(f"[{idx+1}] {item['val']}", key=f"btn_matrix_{idx}_{st.session_state.round}", use_container_width=True):
                    if item["is_anom"]:
                        st.session_state.score += 50
                        st.session_state.streak += 1
                        st.success(f"Akurat! Unit anomali {item['type']} terisolasi tepat waktu.")
                        st.session_state.round += 1
                        st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_matrix_puzzle()
                        st.session_state.start_time = time.time()
                        st.rerun()
                    else:
                        st.session_state.streak = 0
                        st.session_state.score = max(0, st.session_state.score - 15)
                        st.error(f"Salah! Unit tersebut adalah data normal {item['type']}.")

st.markdown("---")
if st.button("Reset Sistem Matrix", key="reset_time_btn"):
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.round = 1
    st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_matrix_puzzle()
    st.session_state.start_time = time.time()
    st.rerun()
