# tools/KREASI.py
import streamlit as st

# ============================================================
# 🎨 UI STREAMLIT & CSS 
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
    margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    text-align: center;
    color: #6b5a52;
    font-weight: 500;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

/* Desain Game */
.game-wrapper {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    height: 520px;
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(112,28,35,0.15);
    border: 1px solid rgba(217,195,163,0.55);
    position: relative;
    overflow: hidden;
}

#hud {
    position: absolute;
    top: 20px; left: 0;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 20px;
    z-index: 10;
}
.stat {
    background: rgba(255,255,255,0.9);
    border: 1px solid rgba(217,195,163,0.8);
    padding: 8px 25px;
    border-radius: 12px;
    font-weight: 700;
    color: #701c23;
    font-size: 18px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}

#play-area {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    display: none;
    overflow: hidden;
}

.item {
    position: absolute;
    font-size: 60px;
    cursor: pointer;
    user-select: none;
    transition: transform 0.1s;
    animation: fall linear forwards;
}
.item:active { transform: scale(1.3); }
@keyframes fall { 0% { top: -80px; } 100% { top: 100%; } }

.screen {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 20;
    width: 90%;
    max-width: 450px;
    padding: 40px;
    background: rgba(255,255,255,0.98);
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    border: 1px solid rgba(217,195,163,0.8);
}
h2 { color: #701c23; font-family: 'Playfair Display', serif; font-size: 32px; margin: 0 0 15px 0; }
p { color: #4e1318; font-size: 16px; margin-bottom: 25px; line-height: 1.6; }

.btn-start {
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: white; border: none; border-radius: 12px;
    padding: 15px 30px; font-weight: 700; font-size: 16px;
    cursor: pointer; box-shadow: 0 6px 18px rgba(112,28,35,0.35);
    transition: transform 0.15s; width: 100%;
}
.btn-start:hover { transform: translateY(-2px); }

.score-pop {
    position: absolute; font-weight: 800; font-size: 24px;
    pointer-events: none; animation: popUp 0.6s ease-out forwards;
    text-shadow: 1px 1px 3px rgba(255,255,255,0.8);
}
@keyframes popUp { 0% { transform: translateY(0) scale(1); opacity: 1; } 100% { transform: translateY(-70px) scale(1.5); opacity: 0; } }

/* 📱 Responsive HP */
@media (max-width: 768px) {
    .game-wrapper { height: 550px; border-radius: 0; border: none; }
    .stat { padding: 6px 12px; font-size: 14px; }
    .screen { padding: 30px 20px; }
    h2 { font-size: 26px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>DATA CATCHER</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>✦ Bersihkan Data, Kumpulkan Skor! ✦</p>", unsafe_allow_html=True)

# ============================================================
# 🎮 HTML & JS (Anti Bocor & Skor Sempurna)
# ============================================================
# PERHATIAN: Pastikan tidak ada spasi di awal baris HTML di bawah ini
game_html = """<div class="game-wrapper" id="game-container">
<div id="hud">
    <div class="stat">⏱️ <span id="time">30</span>s</div>
    <div class="stat">🏆 <span id="score">0</span></div>
    <div class="stat">❤️ <span id="lives">3</span></div>
</div>
<div id="play-area"></div>
<div id="start-screen" class="screen">
    <h2>Data Catcher</h2>
    <p>Klik <b>Data Bersih</b> (🍎, 💎, 📁) secepat mungkin.<br>Jangan klik <b>Data Sampah</b> (🗑️, 💩, 🐛)!</p>
    <button id="btn-start" class="btn-start">🚀 MULAI GAME</button>
</div>
<div id="gameover-screen" class="screen" style="display:none;">
    <h2>Game Over!</h2>
    <p>Skor Akhir: <br><b style="font-size:48px; color:#a8323d;" id="final-score">0</b></p>
    <button id="btn-restart" class="btn-start">🔄 Main Lagi</button>
</div>
</div>

<script>
setTimeout(() => {
    let score = 0, lives = 3, timeLeft = 30, isPlaying = false;
    let spawnInterval, timerInterval;
    const cleanItems = ["🍎", "🍌", "💎", "📁", "💾"];
    const dirtyItems = ["🗑️", "💩", "🐛", "⚠️", "🦠"];
    
    const playArea = document.getElementById("play-area");
    const startScreen = document.getElementById("start-screen");
    const gameoverScreen = document.getElementById("gameover-screen");
    const btnStart = document.getElementById("btn-start");
    const btnRestart = document.getElementById("btn-restart");

    function startGame() {
        clearInterval(timerInterval); clearInterval(spawnInterval);
        score = 0; lives = 3; timeLeft = 30; isPlaying = true;
        document.getElementById("score").innerText = score;
        document.getElementById("lives").innerText = lives;
        document.getElementById("time").innerText = timeLeft;
        startScreen.style.display = "none"; gameoverScreen.style.display = "none";
        playArea.style.display = "block"; playArea.innerHTML = ""; 

        timerInterval = setInterval(() => {
            if (!isPlaying) return;
            timeLeft--; document.getElementById("time").innerText = timeLeft;
            if (timeLeft <= 0) endGame();
        }, 1000);

        spawnInterval = setInterval(spawnItem, 600);
    }

    function spawnItem() {
        if (!isPlaying) return;
        const item = document.createElement("div");
        item.className = "item";
        const isClean = Math.random() > 0.4;
        item.innerText = isClean ? cleanItems[Math.floor(Math.random() * cleanItems.length)] : dirtyItems[Math.floor(Math.random() * dirtyItems.length)];
        item.style.left = Math.floor(Math.random() * 85 + 5) + "%";
        item.style.animationDuration = (Math.random() * 2 + 2) + "s";

        item.onclick = (e) => {
            if (!isPlaying) return; 
            item.style.pointerEvents = "none";
            
            // Ambil posisi X,Y yang benar (relatif ke dalam kotak game)
            const rect = playArea.getBoundingClientRect();
            const x = e.clientX - rect.left; 
            const y = e.clientY - rect.top;

            if (isClean) {
                score += 10; 
                showPop(x, y, "+10", "#28a745"); 
                item.innerText = "✨"; 
            } else {
                lives--; 
                score = Math.max(0, score - 5);
                showPop(x, y, "-5", "#dc3545"); 
                item.innerText = "💥";
                if (lives <= 0) endGame();
            }
            document.getElementById("score").innerText = score;
            document.getElementById("lives").innerText = lives;
            setTimeout(() => item.remove(), 100);
        };

        item.addEventListener("animationend", () => {
            if (isClean && isPlaying) {
                lives--; document.getElementById("lives").innerText = lives;
                if (lives <= 0) endGame();
            }
            item.remove();
        });
        playArea.appendChild(item);
    }

    function showPop(x, y, text, color) {
        const pop = document.createElement("div");
        pop.className = "score-pop"; 
        pop.innerText = text;
        
        // Kalkulasi agar tulisan +10 pas di tengah emoji
        pop.style.left = (x - 15) + "px"; 
        pop.style.top = (y - 20) + "px"; 
        pop.style.color = color;
        
        playArea.appendChild(pop); 
        setTimeout(() => pop.remove(), 600);
    }

    function endGame() {
        isPlaying = false; 
        clearInterval(spawnInterval); 
        clearInterval(timerInterval);
        playArea.style.display = "none"; 
        playArea.innerHTML = "";
        document.getElementById("final-score").innerText = score;
        gameoverScreen.style.display = "block";
    }

    if(btnStart) btnStart.addEventListener("click", startGame);
    if(btnRestart) btnRestart.addEventListener("click", startGame);

}, 200); 
</script>"""

# Tampilkan game
st.markdown(game_html, unsafe_allow_html=True)
