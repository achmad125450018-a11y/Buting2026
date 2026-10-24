import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gradient Descent Master", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: #ffffff;
}
h1, h2, h3 {
    color: #ff2a85 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
label, p, span, div {
    color: #ffffff !important;
}
.stMetric {
    background-color: #141414;
    border: 1px solid #ff2a85;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #ff2a85 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Gradient Descent Master: Interactive Optimization")
st.markdown("Atur Learning Rate dan Iterasi untuk mengarahkan model machine learning menuju titik minimum loss global tanpa terjebak atau mengalami divergen.")

if "lr" not in st.session_state:
    st.session_state.lr = 0.05
    st.session_state.iterations = 50

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Kontrol Hyperparameter")
    lr = st.slider("Learning Rate", 0.001, 0.5, st.session_state.lr, 0.001)
    iterations = st.slider("Jumlah Iterasi", 10, 200, st.session_state.iterations, 5)
    
    if st.button("Jalankan Optimisasi"):
        st.session_state.lr = lr
        st.session_state.iterations = iterations
        st.rerun()

with col2:
    st.subheader("Kurva Loss & Jalur Optimizer")
    
    x = np.linspace(-3, 3, 200)
    y = x**4 - 3*x**2 + 2
    
    current_x = 2.5
    path_x = [current_x]
    path_y = [current_x**4 - 3*current_x**2 + 2]
    
    for _ in range(st.session_state.iterations):
        grad = 4 * (current_x**3) - 6 * current_x
        current_x = current_x - st.session_state.lr * grad
        current_x = max(-3.0, min(3.0, current_x))
        path_x.append(current_x)
        path_y.append(current_x**4 - 3*current_x**2 + 2)
        
    final_loss = path_y[-1]
    
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#0b0b0b')
    ax.set_facecolor('#141414')
    ax.plot(x, y, color="#ff2a85", linewidth=2, label="Loss Surface")
    ax.scatter(path_x, path_y, color="#ffffff", s=30, label="Jalur Optimizer", zorder=5)
    ax.scatter(path_x[-1], path_y[-1], color="#00ffcc", s=100, label="Posisi Akhir", zorder=6)
    
    ax.set_title("Visualisasi Gradien", color="#ff2a85")
    ax.set_xlabel("Parameter Bobot", color="#ffffff")
    ax.set_ylabel("Nilai Loss", color="#ffffff")
    ax.tick_params(colors="#ffffff")
    ax.spines['bottom'].set_color('#333333')
    ax.spines['top'].set_color('#333333')
    ax.spines['left'].set_color('#333333')
    ax.spines['right'].set_color('#333333')
    ax.legend(facecolor='#141414', edgecolor='#ff2a85', labelcolor='#ffffff')
    st.pyplot(fig)

    st.metric("Nilai Loss Akhir", f"{final_loss:.5f}")
    
    if final_loss < 0.05:
        st.success("Berhasil! Model mencapai titik minimum optimal dengan sempurna.")
    elif final_loss > 10:
        st.error("Gagal! Learning Rate terlalu besar, model mengalami divergen (meledak).")
    else:
        st.warning("Belum optimal. Sesuaikan kembali Learning Rate dan jumlah iterasi Anda.")
