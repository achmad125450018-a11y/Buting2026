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

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
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
          "container": {"padding": "0!important", "background-color": "#fafafa"},
          "icon": {"color": "black", "font-size": "19px"},
          "nav-link": {
              "font-size": "15px",
              "text-align": "left",
              "margin": "0px",
              "--hover-color": "#eee",
          },
          "nav-link-selected": {"background-color": "#FCF0DA"},
      },
  )
  return selected


menu = streamlit_menu()

if menu == "Home":

  def home_page():
    # CSS Styling
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');
        
        .deskripsi-title {
            text-align: center;
            font-family: 'Playfair Display', serif;
            font-size: 2.2em;
            color: #2c2c2c;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        /* Frame Foto Kelompok */
        .group-photo-frame {
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            background-color: #2c3e50;
            margin-bottom: 0px;
        }
        
        /* Teks Overlay Foto Kelompok */
        .photo-caption-box {
            background: linear-gradient(135deg, #2c3e50, #1a252f);
            color: white;
            text-align: center;
            padding: 18px 15px;
            border-bottom-left-radius: 18px;
            border-bottom-right-radius: 18px;
            margin-bottom: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }
        
        .badge-cosval {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            margin-bottom: 8px;
            letter-spacing: 1.5px;
            font-weight: 600;
            color: #f1c40f;
        }
        
        .photo-text-title {
            margin: 0;
            font-family: 'Playfair Display', serif;
            font-size: 1.25em;
            font-weight: 700;
            line-height: 1.4;
            color: #ffffff;
        }

        /* Kotak Deskripsi (Bingkai Emas, Judul Hijau Muda, Teks Hitam) */
        .desc-box {
            border: 3px solid #d4af37; /* Bingkai Emas */
            background: #fdfbf7;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }
        
        .desc-heading {
            color: #2ecc71; /* Judul Hijau Muda */
            font-family: 'Playfair Display', serif;
            margin-top: 0;
            margin-bottom: 15px;
            font-size: 1.5em;
            font-weight: 700;
        }
        
        .desc-content {
            color: #000000; /* Teks Hitam */
            font-family: 'Inter', sans-serif;
            line-height: 1.8;
            font-size: 1.05em;
            margin: 0;
            text-align: justify;
        }

        .book-cover {
            background: linear-gradient(135deg, #2c3e50, #1a252f);
            color: white;
            padding: 50px 20px;
            text-align: center;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            border-left: 15px solid #111;
            margin-bottom: 20px;
        }
        
        .book-spread {
            background: #fdfbf7;
            border: 2px solid #dcd6cd;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            border-left: 8px solid #d4c5b9;
            border-right: 8px solid #d4c5b9;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 1. Judul Deskripsi Kelompok
    st.markdown(
        "<div class='deskripsi-title'>✦ Deskripsi Kelompok ✦</div>",
        unsafe_allow_html=True,
    )

    # 2. Foto Kelompok (Pasti Muncul)
    foto_kelompok_url = (
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B"
    )
    st.image(load_image(foto_kelompok_url), use_container_width=True)

    # 3. Teks Keterangan Foto Gaya Poisson
    st.markdown(
        """
        <div class="photo-caption-box">
            <div class="badge-cosval">✦ KELUARGA COSVAL ✦</div>
            <p class="photo-text-title">COSVAL kuat, COSVAL tuntas, semangat membara sampai akhir batas!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 4. Kotak Deskripsi (Bingkai Emas, Judul Hijau Muda, Teks Hitam)
    st.markdown(
        """
        <div class="desc-box">
            <h3 class="desc-heading">Selamat datang di portal resmi kelompok Cosval!</h3>
            <p class="desc-content">
                COSVAL adalah kelompok yang mengutamakan kerja sama, semangat, dan tanggung jawab dalam setiap proses belajar. 
                Dengan visi <b>“Cosval Kuat Semangat, Terus Sampai Tuntas,”</b> COSVAL berkomitmen untuk terus belajar, saling membantu, 
                dan tidak mudah menyerah saat menghadapi kesulitan. Bersama-sama, kami berusaha memberikan yang terbaik dan menyelesaikan 
                setiap tantangan sampai tuntas dalam rangkaian kegiatan pengenalan kampus dan penugasan Buku Kating.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("---")

    # --- FITUR ALBUM COSVAL ---
    st.markdown(
        "<h2 style='text-align: center;'>Album Dokumentasi Cosval</h2>",
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
                <h1>ALBUM Kelompok COSVAL</h1>
                <p>Album kenangan dan dokumentasi kegiatan kelompok kami.</p>
                <p style="color: #bbb; font-size: 0.9em; margin-top: 15px;">Klik tombol di bawah untuk membuka lembaran buku album.</p>
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
                <h4 style='text-align: center; color: #7f8c8d; margin-top: 0;'>— Halaman 1 dari 3 —</h4>
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
                <h4 style='text-align: center; color: #7f8c8d; margin-top: 0;'>— Halaman 2 dari 3 —</h4>
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
                <h4 style='text-align: center; color: #7f8c8d; margin-top: 0;'>— Halaman 3 dari 3 (Akhir) —</h4>
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
        """<style>.centered-title {text-align: center;}</style>""",
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)

    # CSS Bingkai Foto About Us
    st.markdown(
        """
        <style>
        .about-photo img {
            border: 8px solid #c5a059 !important;
            outline: 3px solid #8b5a2b !important;
            border-radius: 12px !important;
            padding: 6px !important;
            background-color: #ffffff !important;
            box-shadow: 0 8px 16px rgba(0,0,0,0.25) !important;
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
          " margin-bottom: 20px; color: #5c3a21;'>Kenalan Yuk Sama"
          " Cosval!</h2>",
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
                        background-color: #f4ecd8; 
                        background-image: linear-gradient(to bottom, #f4ecd8, #e9dcbe);
                        border: 2px solid #b39b77; 
                        padding: 22px; 
                        border-radius: 8px; 
                        box-shadow: inset 0 0 15px rgba(139, 69, 19, 0.15), 0 4px 8px rgba(0,0,0,0.1); 
                        color: #3e2723;
                        font-family: serif;
                        margin-bottom: 20px;">
                        <h3 style="margin-top: 0; color: #5c3a21; border-bottom: 2px solid #b39b77; padding-bottom: 8px;">{data['nama']}</h3>
                        <p style="margin: 8px 0; font-size: 1.05em;"><b>Sebagai:</b> {data['sebagai']}</p>
                        <p style="margin: 8px 0; font-size: 1.05em;"><b>NIM:</b> {data['nim']}</p>
                        <p style="margin: 8px 0; font-size: 1.05em;"><b>Fun Fact:</b> {data['fun_fact']}</p>
                        <p style="margin: 8px 0; font-size: 1.05em;"><b>Motto Hidup:</b> <i>"{data['motto_hidup']}"</i></p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

        st.write("---")

  about_page()
