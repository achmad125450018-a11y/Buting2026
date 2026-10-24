# tools/KREASI.py
import streamlit as st
import random
import time

# ============================================================
# 🎨 SUPER PREMIUM UI — DATA CATCHER GAME
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #222222;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(112,28,35,0.06) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(217,195,163,0.18) 0%, transparent 50%),
        linear-gradient(180deg, #f4f0eb 0%, #efe8df 100%);
    background-attachment: fixed;
}

.title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 3em !important;
    letter-spacing: 1px;
    margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
    display: block;
}
.title::after {
    content: '';
    display: block;
    width: 90px;
    height: 3px;
    margin: 14px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent);
    border-radius: 3px;
}
.subtitle {
    text-align: center;
    font-family: 'Inter', sans-serif;
    color: #6b5a52;
    font-weight: 500;
    font-size: 0.95em !important;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 30px;
    margin-top: 8px;
}

/* Kartu Utama */
.game-card {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 30px 34px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(112,28,35,0.08);
    border: 1px solid rgba(217,195,163,0.55);
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    text-align: center;
}
.game-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}

/* Emoji Animasi */
.emoji-display {
    font-size: 100px;
    margin: 20px 0;
    display: inline-block;
    animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
@keyframes popIn {
    0% { transform: scale(0.5); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

/* Tombol Custom */
.stButton > button {
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 26px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    font-size: 16px !important;
    box-shadow: 0 6px 18px rgba(112,28,35,0.35) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    width: 100%;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 24px rgba(112,28,35,0.5) !important;
}
.stButton > button:active {
    transform: translateY(2px) !important;
}

/* Skor */
.score-box {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 20px;
}
.stat {
    background: rgba(217,195,163,0.15);
    border: 1px solid rgba(217,195,163,0.5);
    padding: 10px 20px;
    border-radius: 12px;
    font-weight: 700;
    color: #701c23;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# GAME LOGIC & STATE
# ============================================================
# Inisialisasi session state
if "game_state" not in st.session_state:
    st.session_state.game_state = "idle" # idle, playing, gameover
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.time_left = 20.0
    st.session_state.current_emoji = "🍎"
    st.session_state.current_type = "clean" # clean atau dirty
    st.session_state.last_time = time.time()

# Data Emoji
CLEAN_DATA = ["🍎", "🍌", "💎", "📁", "💾"] # Data bersih (harus dipencet)
DIRTY_DATA = ["🗑️", "💩", "🐛", "⚠️", "🦠"] # Data sampah (jangan dipencet!)

# ============================================================
# HEADER
# ============================================================
st.markdown("<h1 class='title'>DATA CATCHER</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>✦ Bersihkan Data, Kumpulkan Skor! ✦</p>", unsafe_allow_html=True)

# ============================================================
# GAME UI
# ============================================================
if st.session_state.game_state == "idle":
    st.markdown("""
    <div class="game-card">
        <h3 style="color: #701c23; margin-bottom: 10px;">Selamat Datang di Data Cleaning Simulator!</h3>
        <p style="color: #4e1318; line-height: 1.6;">
            Tugasmu adalah memungut <b>Data Bersih</b> (🍎, 💎, 📁) sebanyak mungkin, dan <b>JANGAN</b> menyentuh <b>Data Sampah</b> (🗑️, 💩, 🐛).<br>
            Kamu punya <b>3 Nyawa</b> dan waktu <b>20 detik</b>. Siap?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 MULAI GAME"):
        st.session_state.game_state = "playing"
        st.session_state.score = 0
        st.session_state.lives = 3
        st.session_state.time_left = 20.0
        st.session_state.last_time = time.time()
        # Generate emoji pertama
        is_clean = random.choice([True, False])
        st.session_state.current_type = "clean" if is_clean else "dirty"
        st.session_state.current_emoji = random.choice(CLEAN_DATA if is_clean else DIRTY_DATA)
        st.rerun()

elif st.session_state.game_state == "playing":
    # Hitung waktu yang berlalu
    now = time.time()
    elapsed = now - st.session_state.last_time
    st.session_state.time_left -= elapsed
    st.session_state.last_time = now

    # Cek Game Over (Waktu habis atau Nyawa habis)
    if st.session_state.time_left <= 0 or st.session_state.lives <= 0:
        st.session_state.game_state = "gameover"
        st.rerun()

    # Tampilkan Skor & Nyawa
    st.markdown(f"""
    <div class="score-box">
        <div class="stat">⏱️ Waktu: {max(0, int(st.session_state.time_left))}s</div>
        <div class="stat">🏆 Skor: {st.session_state.score}</div>
        <div class="stat">❤️ Nyawa: {st.session_state.lives}</div>
    </div>
    """, unsafe_allow_html=True)

    # Tampilkan Emoji Utama
    st.markdown(f"""
    <div class="game-card">
        <div class="emoji-display">{st.session_state.current_emoji}</div>
        <p style="color: #6b5a52; font-weight: 600;">
            {"✅ TANGKAP DATA BERSIH!" if st.session_state.current_type == "clean" else "⛔ HINDARI DATA SAMPAH!"}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Tombol Aksi
    col1, col2 = st.columns(2)
    
    # Logika ketika tombol TANGKAP ditekan
    if col1.button("👆 TANGKAP", use_container_width=True):
        if st.session_state.current_type == "clean":
            st.session_state.score += 10
        else:
            st.session_state.lives -= 1
            st.session_state.score = max(0, st.session_state.score - 5) # Penalti
            
        # Generate emoji baru
        is_clean = random.choice([True, False])
        st.session_state.current_type = "clean" if is_clean else "dirty"
        st.session_state.current_emoji = random.choice(CLEAN_DATA if is_clean else DIRTY_DATA)
        st.session_state.last_time = time.time() # Reset timer agar tidak terasa lambat
        st.rerun()

    # Logika ketika tombol LEWATI (Skip) ditekan
    if col2.button("⏭️ LEWATI", use_container_width=True):
        if st.session_state.current_type == "dirty":
            st.session_state.score += 5 # Dapat poin kecil karena berhasil menghindari
        else:
            st.session_state.lives -= 1 # Penalti karena melewatkan data bersih
            
        # Generate emoji baru
        is_clean = random.choice([True, False])
        st.session_state.current_type = "clean" if is_clean else "dirty"
        st.session_state.current_emoji = random.choice(CLEAN_DATA if is_clean else DIRTY_DATA)
        st.session_state.last_time = time.time()
        st.rerun()

elif st.session_state.game_state == "gameover":
    # Tampilkan hasil akhir
    st.markdown(f"""
    <div class="game-card" style="border: 2px solid #701c23;">
        <h2 style="color: #701c23; font-family: 'Playfair Display'; margin-bottom: 10px;">GAME OVER!</h2>
        <div style="font-size: 80px; margin: 10px 0;">🏆</div>
        <p style="font-size: 20px; font-weight: 700; color: #4e1318;">Skor Akhir Kamu: <span style="font-size: 28px; color: #a8323d;">{st.session_state.score}</span></p>
        <p style="color: #6b5a52; margin-top: 15px;">
            {"⏱️ Waktu Habis!" if st.session_state.time_left <= 0 else "💔 Nyawa Habis!"}
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 MAIN LAGI"):
        st.session_state.game_state = "idle"
        st.rerun()
