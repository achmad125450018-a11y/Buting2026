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

# Pengaturan Konfigurasi Tema Global Krim & Emas (Elegan & Bergrafik)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=Inter:wght@400;600;700&display=swap');

    /* Global Styling - Tema Krim & Elegan */
    .stApp {
        background: linear-gradient(135deg, #fcf8f2 0%, #f0e6d2 100%);
        color: #2c221e;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar hanya diubah warnanya menjadi krim hangat */
    [data-testid="stSidebar"] {
        background-color: #f5ede0 !important;
        border-right: 1px solid #d4af37;
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #2c221e !important;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        color: #5c3a21;
        text-shadow: 2px 2px 15px rgba(197, 160, 89, 0.3);
        margin-bottom: 0px;
    }

    .sub-title {
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 1.5rem;
        color: #8b5a2b;
        letter-spacing: 3px;
        font-weight: 600;
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
              "background-color": "#f4ecd8",
              "border": "1px solid #c5a059",
              "border-radius": "12px",
          },
          "icon": {"color": "#8b5a2b", "font-size": "18px"},
          "nav-link": {
              "font-size": "15px",
              "font-family": "Inter, sans-serif",
              "text-align": "center",
              "margin": "0px 5px",
              "color": "#3e2723",
              "font-weight": "600",
              "--hover-color": "rgba(197, 160, 89, 0.2)",
          },
          "nav-link-selected": {
              "background": (
                  "linear-gradient(135deg, #c5a059 0%, #d4af37 100%)"
              ),
              "border": "1px solid #8b5a2b",
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
            font-family: 'Playfair Display', serif;
            font-size: 2.2em;
            color: #5c3a21;
            margin-bottom: 25px;
            font-weight: 700;
            text-shadow: 1px 1px 10px rgba(197, 160, 89, 0.3);
        }
        
        .photo-caption-box {
            background: linear-gradient(135deg, #fdfbf7 0%, #f4ecd8 100%);
            border: 1px solid #c5a059;
            color: #3e2723;
            text-align: center;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 25px;
            box-shadow: 0 4px 20px rgba(139, 90, 43, 0.15);
        }
        
        .badge-cosval {
            display: inline-block;
            background: rgba(197, 160, 89, 0.2);
            border: 1px solid #c5a059;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-bottom: 10px;
            letter-spacing: 2px;
            font-weight: 700;
            color: #8b5a2b;
            box-shadow: 0 0 10px rgba(197, 160, 89, 0.2);
        }
        
        .photo-text-title {
            margin: 0;
            font-family: 'Playfair Display', serif;
            font-size: 1.25em;
            font-weight: 700;
            color: #2c221e;
        }

        .desc-box {
            border: 2px solid #c5a059;
            background: #fdfbf7;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 6px 25px rgba(139, 90, 43, 0.12);
            margin-bottom: 30px;
        }
        
        .desc-heading {
            color: #5c3a21;
            font-family: 'Playfair Display', serif;
            margin-top: 0;
            margin-bottom: 15px;
            font-size: 1.5em;
            font-weight: 700;
        }
        
        .desc-content {
            color: #2c221e;
            font-family: 'Inter', sans-serif;
            line-height: 1.8;
            font-size: 1.05em;
            margin: 0;
            text-align: justify;
        }

        .book-cover {
            background: linear-gradient(135deg, #fdfbf7 0%, #e9dcbe 100%);
            border: 2px solid #8b5a2b;
            color: #3e2723;
            padding: 50px 20px;
            text-align: center;
            border-radius: 15px;
            box-shadow: 0 8px 30px rgba(139, 90, 43, 0.2);
            margin-bottom: 20px;
        }
        
        .book-spread {
            background: #fdfbf7;
            border: 2px solid #c5a059;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 6px 20px rgba(139, 90, 43, 0.12);
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
        " style='text-align: center; font-family: Playfair Display; color:"
        " #5c3a21; font-weight: 700;'>Album Dokumentasi Cosval</h2>",
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
                <h1 style="font-family: Playfair Display; color: #5c3a21; font-weight: 700;">ALBUM Kelompok COSVAL</h1>
                <p style="color: #3e2723;">Album kenangan dan dokumentasi kegiatan kelompok kami.</p>
                <p style="color: #8b5a2b; font-size: 0.95em; margin-top: 15px; font-weight: 600;">Klik tombol di bawah untuk membuka lembaran buku album.</p>
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
                <h4 style='text-align: center; color: #5c3a21; margin-top: 0; font-family: Playfair Display;'>— Halaman 1 dari 3 —</h4>
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
                <h4 style='text-align: center; color: #5c3a21; margin-top: 0; font-family: Playfair Display;'>— Halaman 2 dari 3 —</h4>
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
                <h4 style='text-align: center; color: #5c3a21; margin-top: 0; font-family: Playfair Display;'>— Halaman 3 dari 3 (Akhir) —</h4>
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
        """<style>.centered-title {text-align: center; color: #5c3a21; font-family:'Playfair Display', serif; font-weight: 700;}</style>""",
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .about-photo img {
            border: 4px solid #c5a059 !important;
            outline: 2px solid #8b5a2b !important;
            border-radius: 12px !important;
            padding: 4px !important;
            background-color: #fdfbf7 !important;
            box-shadow: 0 8px 20px rgba(139, 90, 43, 0.25) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    filter_pilihan = st.radio(
        "Tampilkan Profil:",
        ["Semua", "Pak Lurah", "Bu Lurah", "Anggota"],
        horizontal=True,
    )

    if filter_pilihan == "Semua":
      st.markdown(
          "<h2 style='text-align: center; margin-top: 20px;"
          " margin-bottom: 20px; color: #5c3a21; font-family: \"Playfair"
          " Display\", serif; font-weight: 700;'>Kenalan Yuk Sama Cosval!</h2>",
          unsafe_allow_html=True,
      )

    st.write("")

    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1CkTOku6mtZq-sryae2A1H_dx5moG-R1q",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]

    data_list = [
        {
            "nama": "Herfan Hidayat",
            "sebagai": "Pak Lurah",
            "nim": "125450072",
            "fun_fact": (
                "Suka penasaran akan hal yang baru, yang penting cobain aja"
                " dulu"
            ),
            "motto_hidup": (
                "Dengan bekingan doa ibu, jangankan kalah imbangpun saya"
                " tidak sudi!"
            ),
        },
        {
            "nama": "Ester Friana Sitorus",
            "sebagai": "Bu Lurah",
            "nim": "122450000",
            "fun_fact": "nyemilin es bata",
            "motto_hidup": "Ya apa ya",
        },
        {
            "nama": "Nama Anggota 1",
            "sebagai": "Anggota",
            "nim": "122450083",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 2",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 3",
            "sebagai": "Anggota",
            "nim": "122450100",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 4",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 5",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 6",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 7",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 8",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 9",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
    ]

    if filter_pilihan == "Semua":
      indices = list(range(11))
    elif filter_pilihan == "Pak Lurah":
      indices = [0]
    elif filter_pilihan == "Bu Lurah":
      indices = [1]
    else:
      indices = list(range(2, 11))

    for idx in indices:
      if idx < len(data_list) and idx < len(gambar_urls):
        img = load_image(gambar_urls[idx])
        data = data_list[idx]

        col_img, col_bio = st.columns([1, 1.4], vertical_alignment="center")

        with col_img:
          st.image(img, use_container_width=True)

        with col_bio:
          st.markdown(
              f"""
                    <div style="
                        background: linear-gradient(135deg, #fdfbf7 0%, #f4ecd8 100%); 
                        border: 2px solid #c5a059; 
                        padding: 24px; 
                        border-radius: 15px; 
                        box-shadow: 0 6px 20px rgba(139, 90, 43, 0.15); 
                        color: #2c221e;
                        font-family: 'Inter', sans-serif;
                        position: relative;
                        overflow: hidden;
                        margin-bottom: 20px;">
                        <div style="position: absolute; top: 0; right: 0; width: 70px; height: 70px; background: linear-gradient(135deg, transparent 50%, rgba(197,160,89,0.25) 50%); pointer-events: none;"></div>
                        <h3 style="margin-top: 0; color: #5c3a21; border-bottom: 2px solid #c5a059; padding-bottom: 8px; font-family: 'Playfair Display', serif;">{data['nama']}</h3>
                        <p style="margin: 8px 0; font-size: 1.05em; color: #2c221e;"><b>Sebagai:</b> {data['sebagai']}</p>
                        <p style="margin: 8px 0; font-size: 1.05em; color: #2c221e;"><b>NIM:</b> {data['nim']}</p>
                        <p style="margin: 8px 0; font-size: 1.05em; color: #2c221e;"><b>Fun Fact:</b> {data['fun_fact']}</p>
                        <p style="margin: 8px 0; font-size: 1.05em; color: #2c221e;"><b>Motto Hidup:</b> <i>"{data['motto_hidup']}"</i></p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

        st.write("---")

  about_page()
