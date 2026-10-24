# tools/KREASI.py
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# 🎨 UI STREAMLIT 
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
    margin-bottom: 20px;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>DATA CATCHER</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>✦ Bersihkan Data, Kumpulkan Skor! ✦</p>", unsafe_allow_html=True)

# ============================================================
# 🎮 HTML/JS GAME (Desain Vertikal / Portrait)
# ============================================================
game_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    * { box-sizing: border-box; }
    body {
        margin: 0; padding: 0;
        font-family: 'Inter', sans-serif;
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    
    /* Desain Game Vertikal (Tinggi) */
    #game-container {
        width: 100%;
        max-width: 400px;
        height: 500px;
        background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(112,28,35,0.15);
        border: 1px solid rgba(217,195,163,0.55);
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    #hud {
        width: 100%;
        display: flex;
        justify-content: space-between;
        padding: 15px;
        z-index: 10;
        background: rgba(255,255,255,0.8);
        backdrop-filter: blur(5px);
    }
    .stat {
        font-weight: 700;
        color: #701c23;
        font-size: 14px;
        text-align: center;
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
        font-size: 55px;
        cursor: pointer;
        user-select: none;
        transition: transform 0.1s;
        animation: fall linear forwards;
    }
    .item:active { transform: scale(1.3); }
    
    @keyframes fall {
        0% { top: -80px; }
        100% { top: 100%; }
    }

    .screen {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 20;
        width: 90%;
        padding: 30px 20px;
        background: rgba(255,255,255,0.98);
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
        border: 1px solid rgba(217,195,163,0.8);
    }
    h2 {
        color: #701c23;
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        margin-top: 0; margin-bottom: 15px;
    }
    p {
        color: #4e1318;
        font-size: 14px;
        margin-bottom: 25px;
        line-height: 1.5;
    }
    button {
        background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 20px;
        font-weight: 700;
        font-size: 15px;
        cursor: pointer;
        box-shadow: 0 6px 18px rgba(112,28,35,0.35);
        transition: transform 0.15s;
        width: 100%;
    }
    button:hover {
        transform: translateY(-2px);
    }
    
    .score-pop {
        position: absolute;
        font-weight: 800;
        font-size: 22px;
        pointer-events: none;
        animation: popUp 0.6s ease-out forwards;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.8);
    }
    @keyframes popUp {
        0% { transform: translateY(0) scale(1); opacity: 1; }
        100% { transform: translateY(-70px) scale(1.5); opacity: 0; }
    }
</style>
</head>
<body>

<div id="game-container">
    <div id="hud">
        <div class="stat">⏱️ <span id="time">30</span>s</div>
        <div class="stat">🏆 <span id="score">0</span></div>
        <div class="stat">❤️ <span id="lives">3</span></div>
    </div>

    <div id="play-area"></div>

    <div id="start-screen" class="screen">
        <h2>Data Catcher</h2>
        <p>Klik <b>Data Bersih</b> (🍎, 💎, 📁) secepat mungkin.<br>Jangan klik <b>Data Sampah</b> (🗑️, 💩, 🐛)!</p>
        <button onclick="startGame()">🚀 MULAI GAME</button>
    </div>

    <div id="gameover-screen" class="screen" style="display:none;">
        <h2>Game Over!</h2>
        <p>Skor Akhir: <br><b style="font-size:40px; color:#a8323d;" id="final-score">0</b></p>
        <button onclick="startGame()">🔄 Main Lagi</button>
    </div>
</div>

<script>
    let score = 0;
    let lives = 3;
    let timeLeft = 30;
    let isPlaying = false;
    let spawnInterval, timerInterval;

    const cleanItems = ["🍎", "🍌", "💎", "📁", "💾"];
    const dirtyItems = ["🗑️", "💩", "🐛", "⚠️", "🦠"];

    const playArea = document.getElementById("play-area");
    const startScreen = document.getElementById("start-screen");
    const gameoverScreen = document.getElementById("gameover-screen");

    function startGame() {
        clearInterval(timerInterval);
        clearInterval(spawnInterval);
        
        score = 0;
        lives = 3;
        timeLeft = 30;
        isPlaying = true;
        
        document.getElementById("score").innerText = score;
        document.getElementById("lives").innerText = lives;
        document.getElementById("time").innerText = timeLeft;
        
        startScreen.style.display = "none";
        gameoverScreen.style.display = "none";
        playArea.style.display = "block";
        playArea.innerHTML = ""; 

        timerInterval = setInterval(() => {
            if (!isPlaying) return;
            timeLeft--;
            document.getElementById("time").innerText = timeLeft;
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
        
        item.style.left = Math.floor(Math.random() * 75 + 5) + "%";
        
        const duration = Math.random() * 2 + 2;
        item.style.animationDuration = duration + "s";

        item.onclick = (e) => {
            if (!isPlaying) return;
            item.style.pointerEvents = "none";

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
                lives--;
                document.getElementById("lives").innerText = lives;
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
        pop.style.left = x + "px";
        pop.style.top = y + "px";
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
</script>
</body>
</html>
"""

# Render menggunakan column tengah agar rapi
col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    components.html(game_html, height=520, scrolling=False)
