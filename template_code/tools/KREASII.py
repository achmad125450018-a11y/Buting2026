import streamlit as st
import random

st.set_page_config(page_title="CyberData Scanner", layout="centered")

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

st.title("CyberData: Neural Node Scanner")
st.markdown("Gunakan probe pemindai untuk menemukan node anomali tipe data tersembunyi di dalam matriks jaringan tanpa batas waktu.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "level" not in st.session_state:
    st.session_state.level = 1
if "scans_left" not in st.session_state:
    st.session_state.scans_left = 3
if "cleared_nodes" not in st.session_state:
    st.session_state.cleared_nodes = []

def generate_puzzle():
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
    
    items = []
    for i in range(16):
        items.append({"id": i, "val": random.choice(dom_vals), "type": dom_name, "is_anom": False})
    
    anom_idx = random.randint(0, 15)
    items[anom_idx] = {"id": anom_idx, "val": random.choice(anom_vals), "type": anom_name, "is_anom": True}
    return dom_name, anom_name, items

if "puzzle_items" not in st.session_state:
    dom, anom, items = generate_puzzle()
    st.session_state.dom_name = dom
    st.session_state.anom_name = anom
    st.session_state.puzzle_items = items
    st.session_state.cleared_nodes = []

col1, col2, col3 = st.columns(3)
col1.metric("Skor Total", st.session_state.score)
col2.metric("Level Jaringan", st.session_state.level)
col3.metric("Probe Tersisa", st.session_state.scans_left)

st.markdown("---")
st.markdown(f"### Target Pemindaian: Cari tipe <span style='color: #00f0ff;'>{st.session_state.anom_name}</span> di antara dominasi tipe <span style='color: #38bdf8;'>{st.session_state.dom_name}</span>!", unsafe_allow_html=True)

items = st.session_state.puzzle_items
for row in range(4):
    cols = st.columns(4)
    for col in range(4):
        idx = row * 4 + col
        if idx < len(items):
            item = items[idx]
            with cols[col]:
                if idx in st.session_state.cleared_nodes:
                    st.button(f"[{idx+1}] TERKUNCI", key=f"disabled_{idx}", disabled=True, use_container_width=True)
                else:
                    if st.button(f"[{idx+1}] {item['val']}", key=f"scan_{idx}_{st.session_state.level}", use_container_width=True):
                        if item["is_anom"]:
                            st.session_state.score += 100 * st.session_state.level
                            st.session_state.level += 1
                            st.session_state.scans_left = 3
                            dom, anom, new_items = generate_puzzle()
                            st.session_state.dom_name = dom
                            st.session_state.anom_name = anom
                            st.session_state.puzzle_items = new_items
                            st.session_state.cleared_nodes = []
                            st.success("Anomali berhasil diisolasi! Level jaringan meningkat.")
                            st.rerun()
                        else:
                            st.session_state.scans_left -= 1
                            st.session_state.cleared_nodes.append(idx)
                            if st.session_state.scans_left <= 0:
                                st.error("Probe habis! Jaringan mereset target baru.")
                                dom, anom, new_items = generate_puzzle()
                                st.session_state.dom_name = dom
                                st.session_state.anom_name = anom
                                st.session_state.puzzle_items = new_items
                                st.session_state.scans_left = 3
                                st.session_state.cleared_nodes = []
                                st.rerun()
                            else:
                                st.warning(f"Node normal. Probe tersisa: {st.session_state.scans_left}")
                                st.rerun()

st.markdown("---")
if st.button("Reset Sistem Jaringan", key="reset_scanner_btn"):
    st.session_state.score = 0
    st.session_state.level = 1
    st.session_state.scans_left = 3
    dom, anom, new_items = generate_puzzle()
    st.session_state.dom_name = dom
    st.session_state.anom_name = anom
    st.session_state.puzzle_items = new_items
    st.session_state.cleared_nodes = []
    st.rerun()
