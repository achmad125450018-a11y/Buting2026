import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cyber Hack: Terminal Override", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #030712;
    color: #ffffff;
}
h1 {
    color: #38bdf8 !important;
    font-family: 'Courier New', monospace;
    text-align: center;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

st.title("CYBER HACK: TERMINAL OVERRIDE")
st.markdown("<p style='text-align: center; color: #94a3b8;'>Ikuti pergerakan kotak data, lacak anomali target, dan bypass firewall sebelum sistem trace mendeteksi Anda!</p>", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #030712;
        color: #f8fafc;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 0;
        padding: 10px;
        overflow-x: hidden;
    }
    .stats-panel {
        display: flex;
        justify-content: space-around;
        margin-bottom: 15px;
    }
    .stat-box {
        background: #0f172a;
        border: 1px solid #38bdf8;
        padding: 8px 14px;
        border-radius: 8px;
        color: #38bdf8;
        font-size: 13px;
        font-weight: bold;
    }
    .trace-container {
        width: 100%;
        max-width: 480px;
        background: #1e293b;
        height: 10px;
        border-radius: 5px;
        margin: 0 auto 15px auto;
        overflow: hidden;
        border: 1px solid #38bdf8;
    }
    .trace-bar {
        width: 100%;
        height: 100%;
        background: #4ade80;
        transition: width 0.1s linear;
    }
    .mission-box {
        background: #0f172a;
        border: 2px dashed #38bdf8;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 20px;
        font-size: 15px;
    }
    .target-highlight {
        color: #38bdf8;
        font-weight: bold;
        font-size: 18px;
    }
    .grid-container {
        position: relative;
        margin: 20px auto;
        width: 480px;
        height: 120px;
        max-width: 100%;
    }
    .node-box {
        width: 105px;
        height: 110px;
        background: #0f172a;
        border: 2px solid #38bdf8;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: absolute;
        top: 0;
        transition: left 0.35s ease-in-out, border-color 0.2s;
        cursor: pointer;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.15);
    }
    .node-box:hover {
        border-color: #4ade80;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.4);
    }
    .node-val {
        font-size: 15px;
        font-weight: bold;
        color: #f8fafc;
    }
    .node-type {
        font-size: 10px;
        color: #94a3b8;
        margin-top: 4px;
        text-transform: uppercase;
    }
    .terminal-msg {
        margin-top: 20px;
        font-size: 14px;
        font-weight: bold;
        height: 25px;
    }
    .action-btn {
        background-color: #38bdf8;
        color: #030712;
        border: none;
        padding: 12px 26px;
        font-size: 15px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 15px;
        font-family: 'Courier New', monospace;
        transition: background 0.2s;
    }
    .action-btn:hover {
        background-color: #4ade80;
    }
</style>
</head>
<body>

<div class="stats-panel">
    <div class="stat-box">SCORE: <span id="score">0</span></div>
    <div class="stat-box">LIVES: <span id="lives">3</span></div>
    <div class="stat-box">LEVEL: <span id="level">1</span></div>
</div>

<div class="trace-container">
    <div class="trace-bar" id="trace-bar"></div>
</div>

<div class="mission-box" id="mission-text">
    Inisialisasi sistem... Tekan tombol di bawah untuk mulai.
</div>

<div class="grid-container" id="grid-container"></div>

<div class="terminal-msg" id="terminal-msg"></div>
<button class="action-btn" id="main-btn" onclick="startHack()">MULAI OVERRIDE</button>

<script>
    let score = 0;
    let lives = 3;
    let level = 1;
    let nodes = [];
    let gameState = 'idle'; // idle, reveal, shuffling, guessing, gameover
    let targetType = '';
    let traceTimer = null;
    let traceLeft = 100;
    let shuffleInterval = null;

    const pool = [
        { name: "Integer", vals: ["42", "108", "512", "999", "12", "7", "256"] },
        { name: "Float", vals: ["3.14", "9.81", "0.55", "7.25", "4.19", "1.61"] },
        { name: "String", vals: ["Alpha", "Beta", "Core", "Nexus", "Vector", "Stream"] },
        { name: "Boolean", vals: ["True", "False"] }
    ];

    function startHack() {
        score = 0;
        lives = 3;
        level = 1;
        document.getElementById('main-btn').style.display = 'none';
        initRound();
    }

    function initRound() {
        gameState = 'reveal';
        document.getElementById('terminal-msg').innerText = "";
        
        let domIdx = Math.floor(Math.random() * pool.length);
        let domType = pool[domIdx];
        let anomPool = pool.filter((_, i) => i !== domIdx);
        let anomType = anomPool[Math.floor(Math.random() * anomPool.length)];

        targetType = anomType.name;
        document.getElementById('mission-text').innerHTML = `TARGET PROTOKOL: Cari tipe data <span class="target-highlight">${targetType}</span>`;

        let rawNodes = [];
        for(let i=0; i<3; i++) {
            let val = domType.vals[Math.floor(Math.random() * domType.vals.length)];
            rawNodes.push({ val: val, type: domType.name, isAnom: false });
        }
        let anomVal = anomType.vals[Math.floor(Math.random() * anomType.vals.length)];
        rawNodes.push({ val: anomVal, type: anomType.name, isAnom: true });

        // Shuffle initial order
        rawNodes.sort(() => Math.random() - 0.5);

        nodes = rawNodes.map((n, idx) => ({
            ...n,
            pos: idx
        }));

        renderNodes(true);

        setTimeout(() => {
            startShufflingPhase();
        }, 2200);
    }

    function renderNodes(showContent) {
        const container = document.getElementById('grid-container');
        container.innerHTML = '';
        
        nodes.forEach((node, index) => {
            const el = document.createElement('div');
            el.className = 'node-box';
            el.style.left = (node.pos * 122) + 'px';
            el.onclick = () => handleNodeClick(index);

            if (showContent) {
                el.innerHTML = `
                    <div class="node-val">${node.val}</div>
                    <div class="node-type">${node.type}</div>
                `;
            } else {
                el.innerHTML = `
                    <div class="node-val" style="color: #38bdf8;">[SECURE]</div>
                    <div class="node-type">NODE 0${node.pos + 1}</div>
                `;
            }
            container.appendChild(el);
        });
    }

    async function startShufflingPhase() {
        gameState = 'shuffling';
        renderNodes(false);
        document.getElementById('terminal-msg').innerText = "Firewall mengacak posisi node...";

        let totalSwaps = 4 + (level * 2);
        let currentSwap = 0;
        let speed = Math.max(200, 400 - (level * 30));

        shuffleInterval = setInterval(() => {
            let p1 = Math.floor(Math.random() * 4);
            let p2;
            do {
                p2 = Math.floor(Math.random() * 4);
            } while(p1 === p2);

            let node1 = nodes.find(n => n.pos === p1);
            let node2 = nodes.find(n => n.pos === p2);

            let temp = node1.pos;
            node1.pos = node2.pos;
            node2.pos = temp;

            renderNodes(false);
            currentSwap++;

            if (currentSwap >= totalSwaps) {
                clearInterval(shuffleInterval);
                startGuessingPhase();
            }
        }, speed);
    }

    function startGuessingPhase() {
        gameState = 'guessing';
        document.getElementById('terminal-msg').innerHTML = `<span style="color: #4ade80;">Pilih node yang menyembunyikan tipe ${targetType}!</span>`;
        
        traceLeft = 100;
        let maxTime = Math.max(3000, 8000 - (level * 500));
        let intervalTime = 50;
        let decrement = (intervalTime / maxTime) * 100;

        const bar = document.getElementById('trace-bar');
        bar.style.background = "#4ade80";

        clearInterval(traceTimer);
        traceTimer = setInterval(() => {
            traceLeft -= decrement;
            bar.style.width = traceLeft + '%';
            
            if (traceLeft < 40) bar.style.background = "#eab308";
            if (traceLeft < 20) bar.style.background = "#ef4444";

            if (traceLeft <= 0) {
                clearInterval(traceTimer);
                handleFailure("Waktu trace habis! Firewall mendeteksi akses Anda.");
            }
        }, intervalTime);
    }

    function handleNodeClick(index) {
        if (gameState !== 'guessing') return;
        clearInterval(traceTimer);
        gameState = 'result';

        renderNodes(true);
        const clickedNode = nodes[index];
        const msgEl = document.getElementById('terminal-msg');

        if (clickedNode.isAnom) {
            score += 200 * level;
            level += 1;
            msgEl.style.color = "#4ade80";
            msgEl.innerText = "BYPASS BERHASIL! Akses diberikan.";
            updateStats();
            setTimeout(initRound, 2000);
        } else {
            handleFailure(`Akses Ditolak! Node berisi ${clickedNode.type} (${clickedNode.val}).`);
        }
    }

    function handleFailure(reason) {
        clearInterval(traceTimer);
        lives -= 1;
        gameState = 'gameover';
        renderNodes(true);
        
        const msgEl = document.getElementById('terminal-msg');
        msgEl.style.color = "#ef4444";
        msgEl.innerText = reason;
        updateStats();

        if (lives <= 0) {
            document.getElementById('mission-text').innerHTML = `<span style="color: #ef4444; font-weight: bold;">SISTEM TERKUNCI PERMANEN (GAME OVER)</span>`;
            document.getElementById('main-btn').style.display = 'inline-block';
            document.getElementById('main-btn').innerText = "COBA LAGI";
            document.getElementById('main-btn').onclick = startHack;
        } else {
            setTimeout(initRound, 2500);
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

components.html(game_html, height=460)
