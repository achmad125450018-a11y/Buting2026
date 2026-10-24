import streamlit as st
import random

st.set_page_config(page_title="CyberAnomaly Hunter", layout="centered")

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
    font-size: 16px !important;
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

st.title("CyberAnomaly: Data Type Hunter")
st.markdown("Temukan unit data anomali yang memiliki tipe berbeda di antara kumpulan data utama.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "round" not in st.session_state:
    st.session_state.round = 1

def generate_puzzle():
    types_pool = [
        ("String", ["DataNode", "NeuralCore", "MatrixStream", "VectorNode"]),
        ("Integer", [str(random.randint(10, 99)) for _ in range(4)]),
        ("Float", [str(round(random.uniform(1.0, 9.9), 2)) for _ in range(4)]),
        ("Boolean", ["True", "False"])
    ]
    
    dom_idx = random.randint(0, len(types_pool) - 1)
    dom_name, dom_vals = types_pool[dom_idx]
    
    anom_pool = [t for i, t in enumerate(types_pool) if i != dom_idx]
    anom_name, anom_vals = random.choice(anom_pool)
    
    items = []
    for _ in range(4):
        items.append({"val": random.choice(dom_vals), "type": dom_name, "is_anom": False})
        
    anom_val = random.choice(anom_vals)
    items.append({"val": anom_val, "type": anom_name, "is_anom": True})
    
    random.shuffle(items)
    return dom_name, anom_name, items

if "puzzle_data" not in st.session_state or not isinstance(st.session_state.puzzle_data, tuple):
    st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_puzzle()

col1, col2, col3 = st.columns(3)
col1.metric("Skor Total", st.session_state.score)
col2.metric("Streak", st.session_state.streak)
col3.metric("Ronde", st.session_state.round)

st.markdown("---")
st.markdown(f"### Misi: Temukan tipe data <span style='color: #00f0ff;'>{st.session_state.anom_name}</span> di antara kumpulan tipe <span style='color: #38bdf8;'>{st.session_state.dom_name}</span>!", unsafe_allow_html=True)

for idx, item in enumerate(st.session_state.puzzle_items):
    if st.button(f"Unit Data [{idx+1}] -> {item['val']}", key=f"btn_unit_{idx}_{st.session_state.round}"):
        if item["is_anom"]:
            st.session_state.score += 25
            st.session_state.streak += 1
            st.success(f"Berhasil! Unit tersebut adalah tipe {item['type']} (Anomali).")
            st.session_state.round += 1
            st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_puzzle()
            st.rerun()
        else:
            st.session_state.streak = 0
            st.session_state.score = max(0, st.session_state.score - 10)
            st.error(f"Gagal! Unit tersebut adalah data normal bertipe {item['type']}.")

st.markdown("---")
if st.button("Reset Sistem Matrix", key="reset_sys_btn"):
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.round = 1
    st.session_state.dom_name, st.session_state.anom_name, st.session_state.puzzle_items = generate_puzzle()
    st.rerun()
