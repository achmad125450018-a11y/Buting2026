import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="DataPulse Analytics", page_icon="⚡", layout="wide")

st.title("⚡ DataPulse: Interactive Analytics & ML Playground")
st.markdown("Platform eksplorasi data interaktif dan simulasi machine learning real-time.")

st.sidebar.header("Konfigurasi Parameter")
n_samples = st.sidebar.slider("Jumlah Data (N)", 100, 1000, 300, 50)
noise = st.sidebar.slider("Tingkat Noise", 0.1, 2.0, 0.5, 0.1)
n_clusters = st.sidebar.slider("Jumlah Cluster (K-Means)", 2, 6, 3)

np.random.seed(42)
x = np.random.rand(n_samples) * 10
y = x * 2 + np.random.normal(0, noise * 3, n_samples)
category = np.random.choice(["Kategori A", "Kategori B", "Kategori C"], n_samples)
df = pd.DataFrame({"Fitur_X": x, "Target_Y": y, "Kategori": category})

tab1, tab2, tab3 = st.tabs(["📊 Eksplorasi Data", "🤖 Clustering (K-Means)", "📈 Regresi Linear"])

with tab1:
    st.subheader("Ringkasan & Visualisasi Dataset")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Baris", df.shape[0])
    col2.metric("Rata-rata Fitur X", round(df["Fitur_X"].mean(), 2))
    col3.metric("Rata-rata Target Y", round(df["Target_Y"].mean(), 2))
    
    st.dataframe(df.head(10), use_container_width=True)
    
    fig = px.scatter(df, x="Fitur_X", y="Target_Y", color="Kategori", title="Sebaran Data Interaktif")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Analisis K-Means Clustering")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(df[["Fitur_X", "Target_Y"]])
    df["Cluster"] = [f"Cluster {c+1}" for c in clusters]
    
    fig_cluster = px.scatter(df, x="Fitur_X", y="Target_Y", color="Cluster", title="Hasil Clustering Data")
    st.plotly_chart(fig_cluster, use_container_width=True)

with tab3:
    st.subheader("Simulasi Linear Regression")
    model = LinearRegression()
    model.fit(df[["Fitur_X"]], df["Target_Y"])
    y_pred = model.predict(df[["Fitur_X"]])
    
    df_reg = df.copy()
    df_reg["Prediksi"] = y_pred
    
    fig_reg = px.scatter(df, x="Fitur_X", y="Target_Y", title="Garis Regresi Linear")
    fig_reg.add_scatter(x=df_reg["Fitur_X"], y=df_reg["Prediksi"], mode="lines", name="Model Regresi", line=dict(color="red", width=3))
    st.plotly_chart(fig_reg, use_container_width=True)
    
    st.info(f"Koefisien Regresi: {model.coef_[0]:.4f} | Intercept: {model.intercept_:.4f}")
