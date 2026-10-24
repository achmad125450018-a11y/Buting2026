# tools/KREASI.py
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# 🎨 UI STREAMLIT (Pembungkus Game)
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
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>DATA CATCHER</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>✦ Bersihkan Data, Kumpulkan Skor! ✦</p>", unsafe_allow_html=True)

# ============================================================
# 🎮 HTML/JS GAME (Interaktif & Mulus)
# ============================================================
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    }
    #game-container {
        width: 100%;
        max-width: 600px;
        height: 450px;
        background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(112,28,35,0.08);
        border: 1px solid rgba(217,195,163,0.55);
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    /* Header UI */
    #hud {
        position: absolute;
        top: 15px;
        width: 90%;
        display: flex;
        justify-content: space-between;
        font-weight: 700;
        color: #701c23;
        font-size: 16px;
        z-index: 10;
    }
    .stat {
        background: rgba(217,195,163,0.15);
        border: 1px solid rgba(217,195,163,0.5);
        padding: 8px 15px;
        border-radius: 10px;
    }

    /* Area Main */
    #play-area {
        position: relative;
        width: 100%;
        height: 100%;
        display: none;
    }

    /* Emoji Jatuh */
    .item {
        position: absolute;
        font-size: 50px;
        cursor: pointer;
        user-select: none;
        transition: transform 0.1s;
        animation: fall linear forwards;
    }
    .item:active {
        transform: scale(1.3);
    }
    
    @keyframes fall {
        0% { top: -60px; }
        100% { top: 450px; }
    }

    /* Layar Start & Game Over */
    .screen {
        text-align: center;
        z-index: 20;
        padding: 20px;
    }
    h2 {
        color: #701c23;
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        margin-bottom: 10px;
    }
    p {
        color: #4e1318;
        font-size: 14px;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    button {
        background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 30px;
        font-weight: 700;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 0 6px 18px rgba(112,28,35,0.35);
        transition: transform 0.15s;
    }
    button:hover {
        transform: translateY(-2px);
    }
    
    /* Efek Skor Muncul */
    .score-pop {
        position: absolute;
        font-weight: 800;
        font-size: 20px;
        pointer-events: none;
        animation: popUp 0.5s ease-out forwards;
    }
    @keyframes popUp {
        0% { transform: translateY(0) scale(1); opacity: 1; }
        100% { transform: translateY(-50px) scale(1.5); opacity: 0; }
    }
</style>
</head>
<body>

<div id="game-container">
    <!-- HUD (Skor, Nyawa, Waktu) -->
    <div id="hud">
        <div class="stat">⏱️ Waktu: <span id="time">30</span>s</div>
        <div class="stat">🏆 Skor: <span id="score">0</span></div>
        <div class="stat">❤️ Nyawa: <span id="lives">3</span></div>
    </div>

    <!-- Area Permainan -->
    <div id="play-area"></div>

    <!-- Layar Start -->
    <div id="start-screen" class="screen">
        <h2>Selamat Datang!</h2>
        <p>Klik <b>Data Bersih</b> (🍎, 💎, 📁) secepat mungkin.<br>Jangan klik <b>Data Sampah</b> (🗑️, 💩, 🐛)!</p>
        <button onclick="startGame()">🚀 MULAI GAME</button>
    </div>

    <!-- Layar Game Over -->
    <div id="gameover-screen" class="screen" style="display:none;">
        <h2>Game Over!</h2>
        <p>Skor Akhir Kamu: <b style="font-size:24px; color:#a8323d;" id="final-score">0</b></p>
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
        playArea.innerHTML = ""; // Bersihkan sisa emoji

        // Timer mundur
        timerInterval = setInterval(() => {
            timeLeft--;
            document.getElementById("time").innerText = timeLeft;
            if (timeLeft <= 0) endGame();
        }, 1000);

        // Spawn emoji secara acak
        spawnInterval = setInterval(spawnItem, 700);
    }

    function spawnItem() {
        if (!isPlaying) return;

        const item = document.createElement("div");
        item.className = "item";
        
        // 60% peluang data bersih, 40% data sampah
        const isClean = Math.random() > 0.4;
        item.innerText = isClean ? cleanItems[Math.floor(Math.random() * cleanItems.length)] : dirtyItems[Math.floor(Math.random() * dirtyItems.length)];
        
        // Posisi X acak
        item.style.left = Math.floor(Math.random() * 85) + "%";
        // Durasi jatuh acak
        const duration = Math.random() * 1.5 + 1.5; 
        item.style.animationDuration = duration + "s";

        // Logika saat diklik
        item.onclick = (e) => {
            if (!isPlaying) return;
            item.style.pointerEvents = "none"; // Matikan klik ganda

            const rect = playArea.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            if (isClean) {
                score += 10;
                showPop(x, y, "+10", "#28a745");
                item.innerText = "✨"; // Efek hancur
            } else {
                lives--;
                score = Math.max(0, score - 5);
                showPop(x, y, "-5", "#dc3545");
                item.innerText = "💥";
                if (lives <= 0) endGame();
            }

            document.getElementById("score").innerText = score;
            document.getElementById("lives").innerText = lives;
            
            // Hancurkan elemen setelah animasi kecil
            setTimeout(() => item.remove(), 100);
        };

        // Jika emoji berhasil menghindari klik (jatuh ke bawah)
        item.addEventListener("animationend", () => {
            if (isClean && isPlaying) {
                // Penalti jika melewatkan data bersih
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
        setTimeout(() => pop.remove(), 500);
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

# Render game di dalam Streamlit
components.html(game_html, height=470, scrolling=False)
