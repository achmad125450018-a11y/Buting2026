import streamlit as st
import random

st.set_page_config(page_title="Data Bros Platformer", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #1e1b4b;
    color: #ffffff;
}
h1, h2, h3 {
    color: #facc15 !important;
    font-family: 'Courier New', monospace;
    text-transform: uppercase;
    letter-spacing: 2px;
}
label, p, span, div {
    color: #f8fafc !important;
}
.stMetric {
    background-color: #312e81;
    border: 2px solid #facc15;
    padding: 15px;
    border-radius: 12px;
}
[data-testid="stMetricValue"] {
    color: #facc15 !important;
}
.stButton>button {
    background-color: #312e81 !important;
    color: #facc15 !important;
    border: 2px solid #facc15 !important;
    font-family: 'Courier New', monospace !important;
    font-weight: bold !important;
    font-size: 16px !important;
    width: 100%;
    padding: 20px;
    border-radius: 12px;
}
.stButton>button:hover {
    background-color: #4338ca !important;
    border-color: #38bdf8 !important;
    color: #38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Data Bros: Platformer Anomaly Quest")
st.markdown("Bantu Mario menjelajahi dunia digital dengan memukul blok misteri yang tepat untuk menemukan anomali tipe data.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "coins" not in st.session_state:
    st.session_state.coins = 0
if "lives" not in st.session_state:
    st.session_state.lives = 3
if "world" not in st.session_state:
    st.session_state.world = 1
if "stage" not in st.session_state:
    st.session_state.stage = 1

def generate_mario_puzzle():
    types_pool = [
        ("Integer", [str(random.randint(1, 99)) for _ in range(3)]),
        ("Float", [str(round(random.uniform(1.0, 9.9), 2)) for _ in range(3)]),
        ("String", ["Koopa", "Goomba", "Peach", "Luigi", "Toad"]),
        ("Boolean", ["True", "False"])
    ]
    dom_idx = random.randint(0, len(types_pool) - 1)
    dom_name, dom_vals = types_pool[dom_idx]
    anom_pool = [t for i, t in enumerate(types_pool) if i != dom_idx]
    anom_name, anom_vals = random.choice(anom_pool)
    
    blocks = []
    for _ in range(3):
        blocks.append({"val": random.choice(dom_vals), "type": dom_name, "is_anom": False})
    blocks.append({"val": random.choice(anom_vals), "type": anom_name, "is_anom": True})
    random.shuffle(blocks)
    return dom_name, anom_name, blocks

if "mario_puzzle" not in st.session_state or "blocks" not in st.session_state:
    d, a, b = generate_mario_puzzle()
    st.session_state.dom_name = d
    st.session_state.anom_name = a
    st.session_state.blocks = b

col1, col2, col3, col4 = st.columns(4)
col1.metric("World", f"{st.session_state.world}-{st.session_state.stage}")
col2.metric("Coins", st.session_state.coins)
col3.metric("Score", st.session_state.score)
col4.metric("Lives", st.session_state.lives)

st.markdown("---")
st.markdown(f"### MISI MARIO: Pukul blok misteri yang berisi tipe data <span style='color: #38bdf8;'>{st.session_state.anom_name}</span> di antara blok tipe <span style='color: #facc15;'>{st.session_state.dom_name}</span>!", unsafe_allow_html=True)

if st.session_state.lives > 0:
    cols = st.columns(4)
    for idx, block in enumerate(st.session_state.blocks):
        with cols[idx]:
            if st.button(f"[ ? ]\nBlok {idx+1}", key=f"mario_block_{idx}_{st.session_state.world}_{st.session_state.stage}"):
                if block["is_anom"]:
                    st.session_state.score += 100
                    st.session_state.coins += 1
                    st.success(f"Berhasil! Blok berisi {block['val']} ({block['type']}). Mario maju ke stage berikutnya!")
                    st.session_state.stage += 1
                    if st.session_state.stage > 3:
                        st.session_state.stage = 1
                        st.session_state.world += 1
                    d, a, b = generate_mario_puzzle()
                    st.session_state.dom_name = d
                    st.session_state.anom_name = a
                    st.session_state.blocks = b
                    st.rerun()
                else:
                    st.session_state.lives -= 1
                    st.session_state.score = max(0, st.session_state.score - 50)
                    if st.session_state.lives <= 0:
                        st.error("Game Over! Mario kehabisan nyawa.")
                        st.rerun()
                    else:
                        st.error(f"Trap! Blok berisi {block['val']} ({block['type']}). Mario kehilangan 1 nyawa!")
                        d, a, b = generate_mario_puzzle()
                        st.session_state.dom_name = d
                        st.session_state.anom_name = a
                        st.session_state.blocks = b
                        st.rerun()
else:
    st.error("Permainan Berakhir. Tekan tombol reset di bawah untuk memulai ulang petualangan Mario.")

st.markdown("---")
if st.button("Reset Permainan Mario"):
    st.session_state.score = 0
    st.session_state.coins = 0
    st.session_state.lives = 3
    st.session_state.world = 1
    st.session_state.stage = 1
    d, a, b = generate_mario_puzzle()
    st.session_state.dom_name = d
    st.session_state.anom_name = a
    st.session_state.blocks = b
    st.rerun()
