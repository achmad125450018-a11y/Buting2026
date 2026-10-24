import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Data Bros Moving Shuffle", layout="centered")

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

st.title("DATA BROS: MOVING SHUFFLE QUEST")
st.markdown("<p style='text-align: center; color: #f8fafc;'>Perhatikan isi data pada kotak, lalu ikuti pergerakan kotak saat bergeser dan bertukar posisi!</p>", unsafe_allow_html=True)

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
        padding: 10px;
    }
    .stats {
        display: flex;
        justify-content: space-around;
        margin-bottom: 15px;
        font-size: 15px;
        font-weight: bold;
    }
    .stat-box {
        background: #312e81;
        border: 2px solid #facc15;
        padding: 8px 15px;
        border-radius: 8px;
        color: #facc15;
    }
    .instruction {
        font-size: 16px;
        margin-bottom: 20px;
        color: #38bdf8;
        font-weight: bold;
        min-height: 24px;
    }
    .container {
        position: relative;
        margin: 20px auto;
        width: 540px;
        height: 120px;
        max-width: 100%;
    }
    .box {
        width: 120px;
        height: 110px;
        background: #312e81;
        border: 3px solid #facc15;
        border-radius: 12px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: absolute;
        top: 0;
        transition: left 0.4s ease-in-out;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .box:hover {
        border-color: #38bdf8;
    }
    .box-val {
        font-size: 16px;
        font-weight: bold;
        color: #facc15;
    }
    .box-type {
        font-size: 11px;
        color: #38bdf8;
        margin-top: 5px;
    }
    .message {
        margin-top: 20px;
        font-size: 16px;
        font-weight: bold;
        height: 30px;
    }
    .btn {
        background-color: #facc15;
        color: #1e1b4b;
        border: none;
        padding: 12px 24px;
        font-size: 15px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 15px;
        font-family: 'Courier New', monospace;
    }
    .btn:hover {
        background-color: #38bdf8;
    }
</style>
</head>
<body>

<div class="stats">
    <div class="stat-box">SKOR: <span id="score">0</span></div>
    <div class="stat-box">NYAWA: <span id="lives">3</span></div>
    <div class="stat-box">RONDE: <span id="round">1</span></div>
</div>

<div class="instruction" id="instruction">Perhatikan isi kotak di bawah ini!</div>

<div class="container" id="box-container">
</div>

<div class="message" id="message"></div>
<button class="btn" id="action-btn" onclick="startShuffle()">Mulai Acak Posisi</button>

<script>
    let score = 0;
    let lives = 3;
    let round = 1;
    let boxes = [];
    let gameState = 'reveal'; 
    let targetType = '';

    const typesPool = [
        { name: "Integer", vals: ["42", "108", "512", "999", "12"] },
        { name: "Float", vals: ["3.14", "9.81", "0.55", "7.25", "4.19"] },
        { name: "String", vals: ["Koopa", "Goomba", "Peach", "Luigi", "Toad"] },
        { name: "Boolean", vals: ["True", "False"] }
    ];

    function initRound() {
        gameState = 'reveal';
        document.getElementById('message').innerText = "";
        document.getElementById('action-btn').style.display = 'inline-block';
        document.getElementById('action-btn').innerText = "Mulai Acak Posisi";

        let domIdx = Math.floor(Math.random() * typesPool.length);
        let domType = typesPool[domIdx];
        
        let anomPool = typesPool.filter((_, idx) => idx !== domIdx);
        let anomType = anomPool[Math.floor(Math.random() * anomPool.length)];

        targetType = anomType.name;
        document.getElementById('instruction').innerHTML = `Cari kotak tipe data: <span style="color: #facc15;">${targetType}</span>`;

        let rawBoxes = [];
        for(let i=0; i<3; i++) {
            let val = domType.vals[Math.floor(Math.random() * domType.vals.length)];
            rawBoxes.push({ val: val, type: domType.name, isAnom: false });
        }
        let anomVal = anomType.vals[Math.floor(Math.random() * anomType.vals.length)];
        rawBoxes.push({ val: anomVal, type: anomType.name, isAnom: true });

        shuffleArray(rawBoxes);
        
        boxes = rawBoxes.map((b, idx) => ({
            ...b,
            currentPos: idx
        }));

        renderBoxes(true);
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    function renderBoxes(showContent) {
        const container = document.getElementById('box-container');
        container.innerHTML = '';
        
        boxes.forEach((box, index) => {
            const el = document.createElement('div');
            el.className = 'box';
            el.style.left = (box.currentPos * 138) + 'px';
            el.onclick = () => handleBoxClick(index);

            if (showContent) {
                el.innerHTML = `
                    <div class="box-val">${box.val}</div>
                    <div class="box-type">${box.type}</div>
                `;
            } else {
                el.innerHTML = `
                    <div class="box-val" style="font-size: 24px;">[ ? ]</div>
                    <div class="box-type">Kotak ${box.currentPos + 1}</div>
                `;
            }
            container.appendChild(el);
        });
    }

    async function startShuffle() {
        if (gameState !== 'reveal') return;
        gameState = 'shuffling';
        document.getElementById('action-btn').style.display = 'none';
        document.getElementById('instruction').innerText = "Kotak sedang bergeser dan bertukar posisi...";

        renderBoxes(false);
        await sleep(600);

        let swaps = 5 + round;
        for(let s = 0; s < swaps; s++) {
            let pos1 = Math.floor(Math.random() * 4);
            let pos2;
            do {
                pos2 = Math.floor(Math.random() * 4);
            } while(pos1 === pos2);

            let box1 = boxes.find(b => b.currentPos === pos1);
            let box2 = boxes.find(b => b.currentPos === pos2);

            let temp = box1.currentPos;
            box1.currentPos = box2.currentPos;
            box2.currentPos = temp;

            renderBoxes(false);
            await sleep(450);
        }

        gameState = 'guessing';
        document.getElementById('instruction').innerHTML = `Pilih kotak yang berisi tipe data: <span style="color: #facc15;">${targetType}</span>!`;
    }

    function handleBoxClick(index) {
        if (gameState !== 'guessing') return;
        gameState = 'result';

        renderBoxes(true);

        const clickedBox = boxes[index];
        const msgEl = document.getElementById('message');

        if (clickedBox.isAnom) {
            score += 150;
            round += 1;
            msgEl.style.color = "#4ade80";
            msgEl.innerText = "Benar! Anomali berhasil ditemukan!";
        } else {
            lives -= 1;
            msgEl.style.color = "#f87171";
            msgEl.innerText = `Salah! Itu adalah ${clickedBox.type} (${clickedBox.val}).`;
            if (lives <= 0) {
                document.getElementById('instruction').innerText = "GAME OVER! Nyawa Habis.";
                document.getElementById('action-btn').style.display = 'inline-block';
                document.getElementById('action-btn').innerText = "Main Lagi";
                document.getElementById('action-btn').onclick = resetGame;
                updateStats();
                return;
            }
        }

        updateStats();
        setTimeout(initRound, 2500);
    }

    function updateStats() {
        document.getElementById('score').innerText = score;
        document.getElementById('lives').innerText = lives;
        document.getElementById('round').innerText = round;
    }

    function resetGame() {
        score = 0;
        lives = 3;
        round = 1;
        document.getElementById('action-btn').onclick = startShuffle;
        initRound();
    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    initRound();
</script>
</body>
</html>
"""

components.html(game_html, height=480)
