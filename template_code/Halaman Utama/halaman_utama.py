from io import BytesIO
from PIL import Image, ImageOps
import requests
import streamlit as st
from streamlit_option_menu import option_menu


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  img = ImageOps.exif_transpose(img)
  return img


# JANGAN DIUBAH

# Pengaturan Konfigurasi Halaman & Tema Global Futuristik
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Space+Grotesk:wght@400;600;700&display=swap');

    /* Global Styling */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #090d16 0%, #030712 100%);
        color: #e2e8f0;
        font-family: 'Space Grotesk', sans-serif;
    }

    .main-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00f3ff 0%, #7928ca 50%, #ff007f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(0, 243, 255, 0.4);
        margin-bottom: 0px;
    }

    .sub-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: 1.5rem;
        color: #94a3b8;
        letter-spacing: 3px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 class='main-title'>WEBSITE KATING</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p class='sub-title'>CEO HMSD ADYATAMA ITERA 2026</p>",
    unsafe_allow_html=True,
)

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
  col1, col2, col3 = st.columns([1, 2, 1])
  with col1:
    st.write("")
  with col2:
    st.image(load_image(url), use_container_width=True, width=350)
  with col3:
    st.write("")


layout(url)
layout(url1)


def streamlit_menu():
  selected = option_menu(
      menu_title=None,
      options=["Home", "About Us"],
      icons=["house-door", "hand-index"],
      default_index=0,
      orientation="horizontal",
      styles={
          "container": {
              "padding": "5px",
              "background-color": "rgba(15, 23, 42, 0.9)",
              "border": "1px solid rgba(0, 243, 255, 0.2)",
              "border-radius": "12px",
          },
          "icon": {"color": "#00f3ff", "font-size": "18px"},
          "nav-link": {
              "font-size": "15px",
              "font-family": "Space Grotesk, sans-serif",
              "text-align": "center",
              "margin": "0px 5px",
              "color": "#cbd5e1",
              "--hover-color": "rgba(0, 243, 255, 0.1)",
          },
          "nav-link-selected": {
              "background": (
                  "linear-gradient(135deg, rgba(0,243,255,0.2),"
                  " rgba(121,40,202,0.3))"
              ),
              "border": "1px solid #00f3ff",
              "color": "#ffffff",
              "font-weight": "700",
          },
      },
  )
  return selected


menu = streamlit_menu()

if menu == "Home":

  def home_page():
    st.markdown(
        """
        <style>
        .deskripsi-title {
            text-align: center;
            font-family: 'Orbitron', sans-serif;
            font-size: 2.2em;
            color: #00f3ff;
            margin-bottom: 25px;
            font-weight: 700;
            text-shadow: 0 0 15px rgba(0, 243, 255, 0.3);
        }
        
        .photo-caption-box {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
            border: 1px solid rgba(0, 243, 255, 0.3);
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 25px;
            box-shadow: 0 0 25px rgba(0, 243, 255, 0.15);
        }
        
        .badge-cosval {
            display: inline-block;
            background: rgba(0, 243, 255, 0.15);
            border: 1px solid #00f3ff;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-bottom: 10px;
            letter-spacing: 2px;
            font-weight: 700;
            color: #00f3ff;
            box-shadow: 0 0 10px rgba(0, 243, 255, 0.3);
        }
        
        .photo-text-title {
            margin: 0;
            font-family: 'Orbitron', sans-serif;
            font-size: 1.2em;
            font-weight: 700;
            color: #f8fafc;
        }

        .desc-box {
            border: 2px solid rgba(0, 243, 255, 0.4);
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(0, 243, 255, 0.1);
            margin-bottom: 30px;
        }
        
        .desc-heading {
            color: #00f3ff;
            font-family: 'Orbitron', sans-serif;
            margin-top: 0;
            margin-bottom: 15px;
            font-size: 1.4em;
            font-weight: 700;
        }
        
        .desc-content {
            color: #cbd5e1;
            font-family: 'Space Grotesk', sans-serif;
            line-height: 1.8;
            font-size: 1.05em;
            margin: 0;
            text-align: justify;
        }

        .book-cover {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
            border: 2px solid #7928ca;
            color: white;
            padding: 50px 20px;
            text-align: center;
            border-radius: 15px;
            box-shadow: 0 0 35px rgba(121, 40, 202, 0.3);
            margin-bottom: 20px;
        }
        
        .book-spread {
            background: rgba(15, 23, 42, 0.9);
            border: 2px solid rgba(0, 243, 255, 0.3);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 0 25px rgba(0, 243, 255, 0.1);
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='deskripsi-title'>✦ Deskripsi Kelompok ✦</div>",
        unsafe_allow_html=True,
    )

    foto_kelompok_url = (
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B"
    )
    st.image(load_image(foto_kelompok_url), use_container_width=True)

    st.markdown(
        """
        <div class="photo-caption-box">
            <div class="badge-cosval">✦ KELUARGA COSVAL ✦</div>
            <p class="photo-text-title">COSVAL kuat, COSVAL tuntas, Semangat Terus Sampai Tuntas!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="desc-box">
            <h3 class="desc-heading">Selamat datang di portal resmi kelompok Cosval!</h3>
            <p class="desc-content">
                COSVAL adalah kelompok yang mengutamakan kerja sama, semangat, dan tanggung jawab dalam setiap proses belajar. 
                Dengan visi <b>“Cosval Kuat Semangat, Terus Sampai Tuntas,”</b> COSVAL berkomitmen untuk terus belajar, saling membantu, 
                dan tidak mudah menyerah saat menghadapi kesulitan. Bersama-sama, kami berusaha memberikan yang terbaik dan menyelesaikan 
                setiap tantangan sampai tuntas salah satunya penugasan Buku Kating ini. Di sini kami saling berkolaborasi dan berkerja sama satu sama lain, kami berproses bersama, belajar bersama, dan akan menghadapi semuanya bersama-sama.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("---")

    st.markdown(
        "<h2"
        " style='text-align: center; font-family: Orbitron; color:"
        " #00f3ff;'>Album Dokumentasi Cosval</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    if "album_page" not in st.session_state:
      st.session_state.album_page = 0

    album_photos = [
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
    ]

    if st.session_state.album_page == 0:
      st.markdown(
          """
            <div class="book-cover">
                <h1 style="font-family: Orbitron; color: #00f3ff;">ALBUM Kelompok COSVAL</h1>
                <p style="color: #94a3b8;">Album kenangan dan dokumentasi kegiatan kelompok kami.</p>
                <p style="color: #64748b; font-size: 0.9em; margin-top: 15px;">Klik tombol di bawah untuk membuka lembaran buku album.</p>
            </div>
            """,
          unsafe_allow_html=True,
      )
      col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
      with col_btn2:
        if st.button("Buka Album", use_container_width=True):
          st.session_state.album_page = 1
          st.rerun()

    elif st.session_state.album_page == 1:
      st.markdown(
          """
            <div class="book-spread">
                <h4 style='text-align: center; color: #00f3ff; margin-top: 0; font-family: Orbitron;'>— Halaman 1 dari 3 —</h4>
            """,
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        st.image(
            load_image(album_photos[0]),
            caption="Dokumentasi 1 (Halaman Kiri)",
            use_container_width=True,
        )
      with col2:
        st.image(
            load_image(album_photos[1]),
            caption="Dokumentasi 2 (Halaman Kanan)",
            use_container_width=True,
        )
      st.markdown("</div>", unsafe_allow_html=True)

      c1, c2, c3 = st.columns([1, 2, 1])
      with c1:
        if st.button("◀ Tutup Album"):
          st.session_state.album_page = 0
          st.rerun()
      with c3:
        if st.button("Selanjutnya ▶"):
          st.session_state.album_page = 2
          st.rerun()

    elif st.session_state.album_page == 2:
      st.markdown(
          """
            <div class="book-spread">
                <h4 style='text-align: center; color: #00f3ff; margin-top: 0; font-family: Orbitron;'>— Halaman 2 dari 3 —</h4>
            """,
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        st.image(
            load_image(album_photos[2]),
            caption="Dokumentasi 3 (Halaman Kiri)",
            use_container_width=True,
        )
      with col2:
        st.image(
            load_image(album_photos[3]),
            caption="Dokumentasi 4 (Halaman Kanan)",
            use_container_width=True,
        )
      st.markdown("</div>", unsafe_allow_html=True)

      c1, c2, c3 = st.columns([1, 2, 1])
      with c1:
        if st.button("◀ Sebelumnya"):
          st.session_state.album_page = 1
          st.rerun()
      with c3:
        if st.button("Selanjutnya ▶"):
          st.session_state.album_page = 3
          st.rerun()

    elif st.session_state.album_page == 3:
      st.markdown(
          """
            <div class="book-spread">
                <h4 style='text-align: center; color: #00f3ff; margin-top: 0; font-family: Orbitron;'>— Halaman 3 dari 3 (Akhir) —</h4>
            """,
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        st.image(
            load_image(album_photos[4]),
            caption="Dokumentasi 5 (Halaman Kiri)",
            use_container_width=True,
        )
      with col2:
        st.image(
            load_image(album_photos[5]),
            caption="Dokumentasi 6 (Halaman Kanan)",
            use_container_width=True,
        )
      st.markdown("</div>", unsafe_allow_html=True)

      c1, c2, c3 = st.columns([1, 2, 1])
      with c1:
        if st.button("◀ Sebelumnya"):
          st.session_state.album_page = 2
          st.rerun()
      with c3:
        if st.button("🔒 Tutup Album Kembali"):
          st.session_state.album_page = 0
          st.rerun()

  home_page()

elif menu == "About Us":

  def about_page():
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-family
