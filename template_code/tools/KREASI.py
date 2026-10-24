import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Math Matrix: Sum Cracker", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #09090b;
    color: #ffffff;
}
h1 {
    color: #f97316 !important;
    font-family: 'Courier New', monospace;
    text-align: center;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

st.title("MATH MATRIX: SUM CRACKER")
st.markdown("<p style='text-align: center; color: #fdba74;'>Uji skill berhitung cepat! Pilih kombinasi angka di dalam matriks 4x4 yang jumlah totalnya pas dengan target.</p>", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #09090b;
        color: #ffffff;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 0;
        padding: 10px;
        overflow-x: hidden;
    }
    .stats-panel {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 15px;
    }
    .stat-box {
        background: #18181b;
        border: 1px solid #f97316;
        padding: 8px 16px;
        border-radius: 8px;
        color: #f97316;
        font-size: 13px;
        font-weight: bold;
        box-shadow: 0 0 10px rgba(249, 115, 22, 0.2);
    }
    .timer-container {
        width: 100%;
        max-width: 500px;
        background: #18181b;
        height: 10px;
        border-radius: 5px;
        margin: 0 auto 15px auto;
        overflow: hidden;
        border: 1px solid #f97316;
    }
    .timer-bar {
        width: 100%;
        height: 100%;
        background: #f97316;
        transition: width 0.1s linear;
    }
    .mission-box {
        background: #18181b;
        border: 2px dashed #f97316;
        padding: 12px;
        border-radius: 8px;
        margin: 0 auto 15px auto;
        max-width: 500px;
        font-size: 15px;
        color: #fdba74;
    }
    .target-highlight {
        color: #ffffff;
        background: #c2410c;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 18px;
    }
    .current-sum {
        color: #4ade80;
        font-weight: bold;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin: 15px auto;
        width: 100%;
        max-width: 500px;
    }
    .node-box {
        background: #18181b;
        border: 2px solid #f97316;
        border-radius: 8px;
        height: 80px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform 0.2s ease, background-color 0.2s, border-color 0.2s, box-shadow 0.2s;
        box-shadow: 0 0 8px rgba(249, 115, 22, 0.15);
    }
    .node-box.selected {
        background: #c2410c;
        border-color: #ffffff;
        box-shadow: 0 0 15px rgba(249, 115, 22, 0.8);
    }
    .node-box:hover {
        background: #27272a;
        border-color: #fb923c;
        transform: scale(1.03);
    }
    .node-val {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
    }
    .terminal-msg {
        margin-top: 15px;
        font-size: 14px;
        font-weight: bold;
        height: 24px;
        color: #fdba74;
    }
    .action-btn {
        background-color: #f97316;
        color: #09090b;
        border: none;
        padding: 12px 28px;
        font-size: 15px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 12px;
        font-family: 'Courier New', monospace;
        transition: background 0.2s, transform 0.1s;
        box-shadow: 0 0 15px rgba(249, 115, 22, 0.4);
    }
    .action-btn:hover {
        background-color: #fb923c;
        transform: translateY(-2px);
    }
</style>
</head>
<body>

<div class="stats-panel">
    <div class="stat-box">SKOR: <span id="score">0</span></div>
    <div class="stat-box">NYAWA: <span id="lives">3</span></div>
    <div class="stat-box">LEVEL: <span id="level">1</span></div>
</div>

<div class="timer-container">
    <div class="timer-bar" id="timer-bar"></div>
</div>

<div class="mission-box" id="mission-text">
    Tekan tombol di bawah untuk mulai menghitung!
</div>

<div class="grid-container" id="grid-container"></div>

<div class="terminal-msg" id="terminal-msg"></div>
<button class="action-btn" id="main-btn" onclick="startMathGame()">MULAI BERHITUNG</button>

<script>
    let score = 0;
    let lives = 3;
    let level = 1;
    let nodes = [];
    let targetSum = 0;
    let currentSelectedSum = 0;
    let gameActive = false;
    let timerInterval = null;
    let timeLeft = 100;

    function startMathGame() {
        score = 0;
        lives = 3;
        level = 1;
        document.getElementById('main-btn').style.display = 'none';
        gameActive = true;
        initRound();
    }

    function initRound() {
        currentSelectedSum = 0;
        document.getElementById('terminal-msg').innerText = "";

        // Buat 16 angka acak (1 s.d 25)
        nodes = [];
        for (let i = 0; i < 16; i++) {
            let val = Math.floor(Math.random() * (12 + level * 3)) + 2;
            nodes.push({ val: val, selected: false, id: i });
        }

        // Pilih 2 sampai 4 angka secara acak dari matriks untuk dijadikan target pasti
        let countToPick = Math.random() < 0.5 ? 2 : (Math.random() < 0.8 ? 3 : 4);
        let shuffledIndices = [...Array(16).keys()].sort(() => Math.random() - 0.5);
        
        targetSum = 0;
        let solutionIndices = shuffledIndices.slice(0, countToPick);
        solutionIndices.forEach(idx => {
            targetSum += nodes[idx].val;
        });

        updateMissionText();
        renderGrid();
        startTimer();
    }

    function updateMissionText() {
        document.getElementById('mission-text').innerHTML = `TARGET: <span class="target-highlight">${targetSum}</span> | PILIHAN ANDA: <span class="current-sum" id="sum-display">${currentSelectedSum}</span>`;
    }

    function renderGrid() {
        const container = document.getElementById('grid-container');
        container.innerHTML = '';
        
        nodes.forEach((node, index) => {
            const el = document.createElement('div');
            el.className = 'node-box' + (node.selected ? ' selected' : '');
            el.onclick = () => handleNodeClick(index);

            el.innerHTML = `<div class="node-val">${node.val}</div>`;
            container.appendChild(el);
        });
    }

    function handleNodeClick(index) {
        if (!gameActive) return;

        nodes[index].selected = !nodes[index].selected;
        
        // Hitung ulang total pilihan
        currentSelectedSum = nodes.reduce((sum, n) => sum + (n.selected ? n.val : 0), 0);
        updateMissionText();
        renderGrid();

        if (currentSelectedSum === targetSum) {
            clearInterval(timerInterval);
            score += 250 * level;
            level += 1;
            document.getElementById('terminal-msg').style.color = "#4ade80";
            document.getElementById('terminal-msg').innerText = "BENAR! Kalkulasi tepat.";
            gameActive = false;
            setTimeout(initRound, 1500);
        } else if (currentSelectedSum > targetSum) {
            clearInterval(timerInterval);
            lives -= 1;
            document.getElementById('terminal-msg').style.color = "#dc2626";
            document.getElementById('terminal-msg').innerText = "OVERLOAD! Jumlah melebihi target.";
            updateStats();
            gameActive = false;

            if (lives <= 0) {
                document.getElementById('mission-text').innerHTML = `<span style="color: #dc2626; font-weight: bold;">SYSTEM LOCKED: GAME OVER</span>`;
                document.getElementById('main-btn').style.display = 'inline-block';
                document.getElementById('main-btn').innerText = "COBA LAGI";
                document.getElementById('main-btn').onclick = startMathGame;
            } else {
                setTimeout(initRound, 2000);
            }
        }
    }

    function startTimer() {
        timeLeft = 100;
        let maxTime = Math.max(4000, 12000 - (level * 600));
        let intervalTime = 50;
        let decrement = (intervalTime / maxTime) * 100;

        const bar = document.getElementById('timer-bar');
        bar.style.background = "#f97316";

        clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            if (!gameActive) return;
            timeLeft -= decrement;
            bar.style.width = timeLeft + '%';
            
            if (timeLeft < 40) bar.style.background = "#ea580c";
            if (timeLeft < 20) bar.style.background = "#dc2626";

            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                gameActive = false;
                lives -= 1;
                document.getElementById('terminal-msg').style.color = "#dc2626";
                document.getElementById('terminal-msg').innerText = "WAKTU HABIS! Kalkulasi terlambat.";
                updateStats();

                if (lives <= 0) {
                    document.getElementById('mission-text').innerHTML = `<span style="color: #dc2626; font-weight: bold;">SYSTEM LOCKED: GAME OVER</span>`;
                    document.getElementById('main-btn').style.display = 'inline-block';
                    document.getElementById('main-btn').innerText = "COBA LAGI";
                    document.getElementById('main-btn').onclick = startMathGame;
                } else {
                    setTimeout(initRound, 2000);
                }
            }
        }, intervalTime);
    }

    function updateStats() {
        document.getElementById('score').innerText = score;
        document.getElementById('lives').innerText = lives;
        document.getElementById('level').innerText = level;
    }
</script>
</body>
</html>
"""

components.html(game_html, height=580)
