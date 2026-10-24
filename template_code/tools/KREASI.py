import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# 🎨 UI STREAMLIT UNTUK GAME OUTLIER HUNTER
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

.title-outlier {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 2.8em !important;
    margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle-outlier {
    text-align: center;
    color: #6b5a52;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-outlier'>OUTLIER HUNTER</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-outlier'>✦ Temukan & Klik Data Anomali yang Menyimpang! ✦</p>", unsafe_allow_html=True)

# ============================================================
# 🎮 HTML & JS MINI-GAME OUTLIER HUNTER
# ============================================================
outlier_game_html = """
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
        height: 100vh;
    }
    
    #game-container {
        width: 100%;
        max-width: 900px;
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
        top: 15px; left: 0;
        width: 100%;
        display: flex;
        justify-content: center;
        gap: 20px;
        z-index: 10;
    }
    .stat {
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(217,195,163,0.8);
        padding: 6px 20px;
        border-radius: 12px;
        font-weight: 700;
        color: #701c23;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    #grid-area {
        position: absolute;
        top: 70px; left: 20px; right: 20px; bottom: 20px;
        display: none;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(4, 1fr);
        gap: 12px;
        padding: 10px;
    }

    .data-point {
        background: #f4f0eb;
        border: 2px solid #d9c3a3;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        cursor: pointer;
        transition: all 0.1s ease;
        user-select: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
    }
    .data-point:hover {
        transform: scale(1.03);
        border-color: #701c23;
    }
    .data-point:active {
        transform: scale(0.95);
    }

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
    h2 { color: #701c23; font-family: 'Playfair Display', serif; font-size: 30px; margin: 0 0 10px 0; }
    p { color: #4e1318; font-size: 15px; margin-bottom: 25px; line-height: 1.5; }
    
    .btn-start {
        background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
        color: white; border: none; border-radius: 12px;
        padding: 14px 30px; font-weight: 700; font-size: 16px;
        cursor: pointer; box-shadow: 0 6px 18px rgba(112,28,35,0.35);
        transition: transform 0.15s; width: 100%;
    }
    .btn-start:hover { transform: translateY(-2px); }
</style>
</head>
<body>
<div id="game-container">
    <div id="hud">
        <div class="stat">⏱️ <span id="time">20</span>s</div>
        <div class="stat">🏆 Skor: <span id="score">0</span></div>
    </div>
    
    <div id="grid-area"></div>

    <div id="start-screen" class="screen">
        <h2>Outlier Hunter</h2>
        <p>Di antara data normal, ada satu <b>Data Anomali (Outlier)</b> yang berbeda simbol/ikonnya!<br>Temukan dan klik secepat mungkin sebelum waktu habis.</p>
        <button id="btn-start" class="btn-start">🔍 MULAI BERBURU</button>
    </div>

    <div id="gameover-screen" class="screen" style="display:none;">
        <h2>Waktu Habis!</h2>
        <p>Total Outlier yang Ditemukan: <br><b style="font-size:42px; color:#a8323d;" id="final-score">0</b></p>
        <button id="btn-restart" class="btn-start">🔄 Main Lagi</button>
    </div>
</div>

<script>
    let score = 0, timeLeft = 20, isPlaying = false;
    let timerInterval;
    
    // Kumpulan tema data (Normal vs Outlier)
    const themes = [
        { normal: "📊", outlier: "📈" },
        { normal: "🔵", outlier: "🔴" },
        { normal: "📁", outlier: "🗑️" },
        { normal: "💻", outlier: "🔥" },
        { normal: "📦", outlier: "⚠️" }
    ];

    const gridArea = document.getElementById("grid-area");
    const startScreen = document.getElementById("start-screen");
    const gameoverScreen = document.getElementById("gameover-screen");
    const btnStart = document.getElementById("btn-start");
    const btnRestart = document.getElementById("btn-restart");

    function startGame() {
        clearInterval(timerInterval);
        score = 0; timeLeft = 20; isPlaying = true;
        document.getElementById("score").innerText = score;
        document.getElementById("time").innerText = timeLeft;
        startScreen.style.display = "none"; 
        gameoverScreen.style.display = "none";
        gridArea.style.display = "grid"; 

        nextRound();

        timerInterval = setInterval(() => {
            if (!isPlaying) return;
            timeLeft--; 
            document.getElementById("time").innerText = timeLeft;
            if (timeLeft <= 0) endGame();
        }, 1000);
    }

    function nextRound() {
        if (!isPlaying) return;
        gridArea.innerHTML = "";

        // Pilih tema acak
        const theme = themes[Math.floor(Math.random() * themes.length)];
        
        // Tentukan jumlah kotak (mulai dari 16 kotak / 4x4)
        const totalBoxes = 16;
        const outlierIndex = Math.floor(Math.random() * totalBoxes);

        for (let i = 0; i < totalBoxes; i++) {
            const box = document.createElement("div");
            box.className = "data-point";
            
            if (i === outlierIndex) {
                box.innerText = theme.outlier;
                box.onclick = () => {
                    if (!isPlaying) return;
                    score += 1;
                    document.getElementById("score").innerText = score;
                    nextRound(); // Lanjut ke ronde berikutnya secara instan
                };
            } else {
                box.innerText = theme.normal;
                box.onclick = () => {
                    if (!isPlaying) return;
                    // Penalti waktu jika salah klik data normal (-1 detik)
                    timeLeft = Math.max(0, timeLeft - 1);
                    document.getElementById("time").innerText = timeLeft;
                    if (timeLeft <= 0) endGame();
                };
            }
            gridArea.appendChild(box);
        }
    }

    function endGame() {
        isPlaying = false; 
        clearInterval(timerInterval);
        gridArea.style.display = "none"; 
        gridArea.innerHTML = "";
        document.getElementById("final-score").innerText = score;
        gameoverScreen.style.display = "block";
    }

    if(btnStart) btnStart.addEventListener("click", startGame);
    if(btnRestart) btnRestart.addEventListener("click", startGame);
</script>
</body>
</html>
"""

components.html(outlier_game_html, height=540, scrolling=False)
