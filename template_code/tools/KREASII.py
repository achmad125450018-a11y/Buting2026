import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Data Pipeline Sorter", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #1e1b4b;
    color: #ffffff;
}
h1 {
    color: #facc15 !important;
    font-family: 'Courier New', monospace;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("DATA PIPELINE: TYPE SORTER")
st.markdown("<p style='text-align: center; color: #f8fafc;'>Sortir aliran data yang masuk ke dalam wadah tipe data yang sesuai secepat mungkin!</p>", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #1e1b4b;
        color: white;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 0;
        padding: 5px;
        overflow-x: hidden;
    }
    .stats {
        display: flex;
        justify-content: space-around;
        margin-bottom: 12px;
        font-size: 14px;
        font-weight: bold;
    }
    .stat-box {
        background: #312e81;
        border: 2px solid #facc15;
        padding: 6px 14px;
        border-radius: 8px;
        color: #facc15;
    }
    .conveyor {
        width: 100%;
        max-width: 480px;
        height: 110px;
        background: #0f172a;
        border: 3px dashed #38bdf8;
        border-radius: 12px;
        margin: 15px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        box-shadow: inset 0 0 15px rgba(56, 189, 248, 0.2);
    }
    .data-packet {
        background: #312e81;
        border: 3px solid #facc15;
        padding: 15px 25px;
        border-radius: 10px;
        font-size: 22px;
        font-weight: bold;
        color: #facc15;
        animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }
    .bins-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        max-width: 480px;
        margin: 15px auto;
    }
    .bin-btn {
        background-color: #312e81;
        color: #facc15;
        border: 2px solid #facc15;
        padding: 15px;
        font-size: 15px;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        font-family: 'Courier New', monospace;
        transition: background-color 0.2s, transform 0.1s;
    }
    .bin-btn:hover {
        background-color: #4338ca;
        border-color: #38bdf8;
        color: #38bdf8;
        transform: translateY(-2px);
    }
    .message {
        margin-top: 15px;
        font-size: 15px;
        font-weight: bold;
        height: 25px;
    }
    .start-btn {
        background-color: #facc15;
        color: #1e1b4b;
        border: none;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 10px;
        font-family: 'Courier New', monospace;
    }
    .start-btn:hover {
        background-color: #38bdf8;
    }
</style>
</head>
<body>

<div class="stats">
    <div class="stat-box">SKOR: <span id="score">0</span></div>
    <div class="stat-box">NYAWA: <span id="lives">3</span></div>
    <div class="stat-box">LEVEL: <span id="level">1</span></div>
</div>

<div class="conveyor" id="conveyor-area">
    <div id="packet-display" class="data-packet">Tekan Mulai</div>
</div>

<div class="bins-container" id="bins-area" style="display: none;">
    <button class="bin-btn" onclick="checkSort('Integer')">INTEGER</button>
    <button class="bin-btn" onclick="checkSort('Float')">FLOAT</button>
    <button class="bin-btn" onclick="checkSort('String')">STRING</button>
    <button class="bin-btn" onclick="checkSort('Boolean')">BOOLEAN</button>
</div>

<div class="message" id="message"></div>
<button class="start-btn" id="action-btn" onclick="startGame()">Mulai Pipeline</button>

<script>
    let score = 0;
    let lives = 3;
    let level = 1;
    let currentPacket = null;
    let gameActive = false;

    const dataPool = [
        { type: "Integer", vals: ["42", "108", "512", "999", "12", "7"] },
        { type: "Float", vals: ["3.14", "9.81", "0.55", "7.25", "4.19", "0.0"] },
        { type: "String", vals: ["NodeA", "Alpha", "Beta", "Core", "Stream", "Matrix"] },
        { type: "Boolean", vals: ["True", "False"] }
    ];

    function startGame() {
        score = 0;
        lives = 3;
        level = 1;
        gameActive = true;
        document.getElementById('action-btn').style.display = 'none';
        document.getElementById('bins-area').style.display = 'grid';
        nextPacket();
        updateStats();
    }

    function nextPacket() {
        if (!gameActive) return;
        let randomCategory = dataPool[Math.floor(Math.random() * dataPool.length)];
        let randomVal = randomCategory.vals[Math.floor(Math.random() * randomCategory.vals.length)];
        
        currentPacket = {
            val: randomVal,
            type: randomCategory.type
        };

        document.getElementById('packet-display').innerText = currentPacket.val;
        document.getElementById('message').innerText = "";
    }

    function checkSort(selectedType) {
        if (!gameActive) return;

        if (selectedType === currentPacket.type) {
            score += 50 * level;
            if (score % 200 === 0) level += 1;
            document.getElementById('message').style.color = "#4ade80";
            document.getElementById('message').innerText = "Berhasil Disortir!";
            updateStats();
            setTimeout(nextPacket, 400);
        } else {
            lives -= 1;
            document.getElementById('message').style.color = "#f87171";
            document.getElementById('message').innerText = `Salah! Ini adalah tipe ${currentPacket.type}.`;
            updateStats();

            if (lives <= 0) {
                gameActive = false;
                document.getElementById('bins-area').style.display = 'none';
                document.getElementById('packet-display').innerText = "PIPELINE GAGAL";
                document.getElementById('message').innerText = "Sistem mengalami overflow!";
                document.getElementById('action-btn').style.display = 'inline-block';
                document.getElementById('action-btn').innerText = "Main Lagi";
            } else {
                setTimeout(nextPacket, 800);
            }
        }
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

components.html(game_html, height=450)
