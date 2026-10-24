import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Bayesian Mystery", page_icon="🔎", layout="wide")

SUSPECTS = ["Andi", "Bima", "Citra"]
PRIOR = {"Andi": 0.40, "Bima": 0.35, "Citra": 0.25}
SOLUTION = "Bima"

# Angka kemungkinan bukti adalah data simulasi untuk permainan edukasi.
CLUES = [
    {
        "title": "Petunjuk 1 — Catatan akses ruangan",
        "story": (
            "Catatan akses menunjukkan bahwa orang yang masuk ke ruang "
            "penyimpanan pada waktu kejadian lebih mungkin adalah Bima."
        ),
        "likelihood": {"Andi": 0.20, "Bima": 0.70, "Citra": 0.30},
    },
    {
        "title": "Petunjuk 2 — Serat kain di dekat lemari",
        "story": (
            "Serat kain yang ditemukan lebih cocok dengan jaket yang biasa "
            "dipakai Citra. Bukti ini mendukung Citra, tetapi tidak memastikan "
            "bahwa ia mengambil piala."
        ),
        "likelihood": {"Andi": 0.25, "Bima": 0.35, "Citra": 0.65},
    },
    {
        "title": "Petunjuk 3 — Kesaksian penjaga",
        "story": (
            "Penjaga mengingat seseorang dengan ciri yang lebih sesuai dengan "
            "Andi. Kesaksian bisa keliru, sehingga bukti ini perlu dinilai "
            "bersama petunjuk lainnya."
        ),
        "likelihood": {"Andi": 0.75, "Bima": 0.30, "Citra": 0.20},
    },
]


def update_bayes(prior, likelihood):
    """Menghitung posterior menggunakan Teorema Bayes."""
    weighted = {
        name: prior[name] * likelihood[name]
        for name in SUSPECTS
    }
    total = sum(weighted.values())
    if total == 0:
        return prior.copy()
    return {name: weighted[name] / total for name in SUSPECTS}


def calculate_posterior(number_of_clues):
    posterior = PRIOR.copy()
    for clue in CLUES[:number_of_clues]:
        posterior = update_bayes(posterior, clue["likelihood"])
    return posterior


def reset_game():
    st.session_state.prediction = None
    st.session_state.clues_opened = 0
    st.session_state.final_guess = None
    st.session_state.game_finished = False


if "prediction" not in st.session_state:
    reset_game()

st.markdown(
    """
    <style>
    .stApp {background: linear-gradient(180deg, #101827 0%, #151b2c 100%);}
    .main-title {font-size: 2.7rem; font-weight: 800; color: #f4f0ff;}
    .subtitle {color: #b9c2d8; font-size: 1.05rem; margin-bottom: 1.5rem;}
    .case-box {
        padding: 1.1rem 1.25rem; border: 1px solid #343d56;
        border-radius: 14px; background: rgba(30, 39, 60, 0.8);
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🔎 Bayesian Mystery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Every clue changes the odds. '
    'Gunakan bukti, perbarui probabilitas, pecahkan misterinya.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("🕵️ Panduan Investigasi")
    st.write("1. Baca kasus dan kenali tersangka.")
    st.write("2. Kunci prediksi awal sebelum membuka petunjuk.")
    st.write("3. Buka petunjuk satu per satu.")
    st.write("4. Amati perubahan probabilitas.")
    st.write("5. Tetapkan jawaban akhir dan lihat skor.")
    st.divider()
    st.caption(
        "Semua probabilitas adalah data simulasi untuk belajar Bayes, "
        "bukan tuduhan terhadap orang nyata."
    )
    if st.button("🔄 Mulai ulang permainan", use_container_width=True):
        reset_game()
        st.rerun()

st.markdown(
    """
    <div class="case-box">
        <h3>📁 Kasus: Piala yang Hilang</h3>
        <p>Piala penghargaan organisasi kampus menghilang dari lemari
        penyimpanan setelah rapat sore. Tiga anggota memiliki akses ke area
        tersebut: Andi, Bima, dan Citra.</p>
        <p>Kamu adalah detektif. Tugasmu bukan sekadar menebak, tetapi menilai
        bagaimana setiap bukti mengubah kemungkinan dari tiap hipotesis.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("🧍 Para tersangka")
details = {
    "Andi": ("🧑‍💼", "Bertugas mengurus inventaris."),
    "Bima": ("🧑‍🔧", "Membantu persiapan ruangan."),
    "Citra": ("🧑‍🎓", "Hadir dalam rapat sore."),
}
cols = st.columns(3)
for col, name in zip(cols, SUSPECTS):
    emoji, description = details[name]
    with col:
        st.markdown(f"### {emoji} {name}")
        st.write(description)
        st.metric("Probabilitas awal", f"{PRIOR[name] * 100:.0f}%")

st.divider()
st.subheader("1. Buat prediksi awal")
st.write("Sebelum melihat bukti, siapa yang menurutmu paling mungkin mengambil piala?")

if st.session_state.prediction is None:
    choice = st.radio("Pilih prediksi awal:", SUSPECTS, horizontal=True)
    if st.button("🔒 Kunci prediksi awal", type="primary"):
        st.session_state.prediction = choice
        st.rerun()
else:
    st.success(f"Prediksi awalmu sudah dikunci: **{st.session_state.prediction}**")

st.subheader("2. Kumpulkan bukti")
if st.session_state.prediction is None:
    st.info("Kunci prediksi awal terlebih dahulu untuk membuka petunjuk.")
else:
    opened = st.session_state.clues_opened
    if opened < len(CLUES):
        st.write(f"Petunjuk berikutnya: **{CLUES[opened]['title']}**")
        if st.button("🧩 Buka petunjuk", type="primary"):
            st.session_state.clues_opened += 1
            st.rerun()
    else:
        st.success("Semua petunjuk telah dibuka.")

    for i, clue in enumerate(CLUES[:st.session_state.clues_opened]):
        with st.expander(clue["title"], expanded=(i == st.session_state.clues_opened - 1)):
            st.write(clue["story"])

opened = st.session_state.clues_opened
posterior = calculate_posterior(opened)

st.subheader("3. Perubahan probabilitas")
st.write(
    f"Petunjuk terbuka: **{opened} dari {len(CLUES)}**. "
    "Bandingkan probabilitas sebelum dan sesudah bukti."
)

rows = []
for name in SUSPECTS:
    rows.append({"Tersangka": name, "Probabilitas": PRIOR[name] * 100, "Tahap": "Sebelum bukti"})
    rows.append({"Tersangka": name, "Probabilitas": posterior[name] * 100, "Tahap": "Setelah bukti"})
df = pd.DataFrame(rows)

fig = px.bar(
    df, x="Tersangka", y="Probabilitas", color="Tahap", barmode="group",
    text_auto=".1f", range_y=[0, 100], title="Probabilitas tersangka (%)",
    color_discrete_map={"Sebelum bukti": "#8b9bb4", "Setelah bukti": "#b69cff"},
)
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="#f4f0ff", legend_title_text="", yaxis_title="Probabilitas (%)",
    xaxis_title="",
)
st.plotly_chart(fig, use_container_width=True)

cols = st.columns(3)
for col, name in zip(cols, SUSPECTS):
    with col:
        st.metric(
            f"Probabilitas {name}",
            f"{posterior[name] * 100:.1f}%",
            delta=f"{(posterior[name] - PRIOR[name]) * 100:+.1f} poin persentase",
        )

with st.expander("📘 Bagaimana Teorema Bayes bekerja?"):
    st.write(
        "Probabilitas awal dikalikan dengan kemungkinan bukti muncul jika "
        "hipotesis benar. Hasilnya lalu dinormalisasi agar total probabilitas "
        "menjadi 100%."
    )
    st.latex(r"P(H_i\mid E)=\frac{P(E\mid H_i)P(H_i)}{\sum_j P(E\mid H_j)P(H_j)}")
    st.dataframe(
        pd.DataFrame({
            "Tersangka": SUSPECTS,
            "Probabilitas (%)": [round(posterior[n] * 100, 2) for n in SUSPECTS],
        }),
        hide_index=True,
        use_container_width=True,
    )

st.subheader("4. Tetapkan keputusan akhir")
if st.session_state.prediction is None:
    st.info("Kunci prediksi awal terlebih dahulu.")
elif opened < len(CLUES):
    st.info("Buka semua petunjuk sebelum menetapkan keputusan akhir.")
elif not st.session_state.game_finished:
    final_choice = st.radio("Setelah melihat semua bukti, siapa pilihan akhirmu?", SUSPECTS)
    if st.button("🧾 Selesaikan investigasi", type="primary"):
        st.session_state.final_guess = final_choice
        st.session_state.game_finished = True
        st.rerun()

if st.session_state.game_finished:
    final_guess = st.session_state.final_guess
    final_correct = final_guess == SOLUTION
    initial_correct = st.session_state.prediction == SOLUTION
    score = (60 if final_correct else 0) + (20 if initial_correct else 0) + 20

    st.divider()
    st.subheader("🏁 Hasil investigasi")
    if final_correct:
        st.success(f"Benar! Pilihan akhirmu adalah **{SOLUTION}**.")
    else:
        st.warning(
            f"Pilihan akhirmu adalah **{final_guess}**. "
            f"Solusi cerita yang ditetapkan adalah **{SOLUTION}**."
        )

    c1, c2, c3 = st.columns(3)
    c1.metric("Skor", f"{score}/100")
    c2.metric("Prediksi awal", "Benar" if initial_correct else "Belum tepat")
    c3.metric("Prediksi akhir", "Benar" if final_correct else "Belum tepat")

    st.markdown("### 🧠 Pembahasan")
    st.write(
        "Dalam cerita simulasi ini, Bima ditetapkan sebagai pelaku. "
        "Setiap petunjuk hanya mengubah tingkat keyakinan; tidak ada bukti "
        "yang memberi kepastian mutlak."
    )
    st.write(
        f"Posterior akhir model: Andi **{posterior['Andi'] * 100:.1f}%**, "
        f"Bima **{posterior['Bima'] * 100:.1f}%**, "
        f"Citra **{posterior['Citra'] * 100:.1f}%**."
    )
    st.caption(
        "Catatan: likelihood bukti di atas merupakan angka simulasi. "
        "Untuk kasus yang lebih realistis, pastikan likelihood konsisten "
        "dengan cerita dan solusi."
    )
    if st.button("🔁 Main lagi", type="primary"):
        reset_game()
        st.rerun()

st.divider()
st.caption("Bayesian Mystery • Kreasi Streamlit Kelompok Bayesian • Game edukasi probabilitas")
