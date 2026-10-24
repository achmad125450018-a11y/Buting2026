import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="Data Type Sorter Pro", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #f8f9fa;
    color: #111111;
}
h1, h2, h3 {
    color: #1f77b4 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
label, p, span, div {
    color: #111111 !important;
}
.stMetric {
    background-color: #ffffff;
    border: 1px solid #dcdcdc;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #1f77b4 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Data Type Sorter Pro: Multi-Type Classification")
st.markdown("Klasifikasikan berbagai jenis item data ke dalam tipe data yang tepat (Integer, Float, String, Boolean, atau Date).")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.round = 1
    st.session_state.current_item = None
    st.session_state.current_type = None

def generate_item():
    types = ["Integer", "Float", "String", "Boolean", "Date"]
    chosen_type = random.choice(types)
    if chosen_type == "Integer":
        val = str(random.randint(-500, 500))
    elif chosen_type == "Float":
        val = str(round(random.uniform(-100, 100), 2))
    elif chosen_type == "String":
        words = ["Python", "Streamlit", "Dataset", "Analytics", "DataFrame", "Pandas"]
        val = random.choice(words)
    elif chosen_type == "Boolean":
        val = str(random.choice([True, False]))
    elif chosen_type == "Date":
        val = str(date(random.randint(2020, 2026), random.randint(1, 12), random.randint(1, 28)))
    return val, chosen_type

if st.session_state.current_item is None:
    st.session_state.current_item, st.session_state.current_type = generate_item()

col1, col2 = st.columns(2)
col1.metric("Skor", st.session_state.score)
col2.metric("Nyawa", st.session_state.lives)

st.subheader(f"Ronde {st.session_state.round}")
st.markdown("Tentukan Tipe Data untuk Nilai Berikut:")
st.markdown(f"<h1 style='text-align: center; color: #d62728; background-color: #ffffff; padding: 25px; border-radius: 10px; border: 1px solid #ddd;'>{st.session_state.current_item}</h1>", unsafe_allow_html=True)

st.markdown("Pilih Tipe Data yang Sesuai:")

col_a, col_b, col_c, col_d, col_e = st.columns(5)

selected_choice = None

if col_a.button("Integer", use_container_width=True):
    selected_choice = "Integer"
if col_b.button("Float", use_container_width=True):
    selected_choice = "Float"
if col_c.button("String", use_container_width=True):
    selected_choice = "String"
if col_d.button("Boolean", use_container_width=True):
    selected_choice = "Boolean"
if col_e.button("Date", use_container_width=True):
    selected_choice = "Date"

if selected_choice is not None:
    if selected_choice == st.session_state.current_type:
        st.session_state.score += 15
        st.success(f"Benar! Ini adalah tipe data {selected_choice}.")
    else:
        st.session_state.lives -= 1
        st.error(f"Salah! Nilai tersebut adalah tipe data {st.session_state.current_type}.")
        
    if st.session_state.lives <= 0:
        st.error("Permainan Berakhir. Nyawa Anda habis.")
        if st.button("Main Lagi"):
            st.session_state.score = 0
            st.session_state.lives = 3
            st.session_state.round = 1
            st.session_state.current_item, st.session_state.current_type = generate_item()
            st.rerun()
    else:
        st.session_state.round += 1
        st.session_state.current_item, st.session_state.current_type = generate_item()
        st.rerun()

st.markdown("---")
if st.button("Reset Total Permainan"):
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.round = 1
    st.session_state.current_item, st.session_state.current_type = generate_item()
    st.rerun()
