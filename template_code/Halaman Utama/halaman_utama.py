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
    st.markdown(
        """<style>.centered-title {text-align: center;}</style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 class='centered-title'>Kami Cosval!</h1>", unsafe_allow_html=True
    )
    st.markdown(
        """<div style="text-align: justify;">COSVAL adalah kelompok yang mengutamakan kerja sama, semangat, dan tanggung jawab dalam setiap proses belajar. Dengan visi “Cosval Kuat Semangat, Terus Sampai Tuntas,” COSVAL berkomitmen untuk terus belajar, saling membantu, dan tidak mudah menyerah saat menghadapi kesulitan. Bersama-sama, kami berusaha memberikan yang terbaik dan menyelesaikan setiap tantangan sampai tuntas.</div>""",
        unsafe_allow_html=True,
    )
    st.write(""" """)

    foto_kelompok = (
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B"
    )
    layout(foto_kelompok)
    st.markdown(
        """<div style="text-align: center; font-style: italic;">Melalui kerja sama dan tekad yang kuat.</div>""",
        unsafe_allow_html=True,
    )
    st.write("---")

    # --- CSS KHUSUS TAMPILAN BUKU ALBUM ---
    st.markdown(
        """
        <style>
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

    # Judul Album Tanpa Stiker Buku
    st.markdown(
        "<h2 style='text-align: center;'>Album Dokumentasi Cosval</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    # Inisialisasi state halaman album (0 = Tertutup, 1 = Hal 1, 2 = Hal 2, 3 = Hal 3)
    if "album_page" not in st.session_state:
      st.session_state.album_page = 0

    # Daftar 6 foto untuk 3 halaman album (2 foto per halaman)
    album_photos = [
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",  # Foto 1 (Hal 1)
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",  # Foto 2 (Hal 1)
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",  # Foto 3 (Hal 2)
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",  # Foto 4 (Hal 2)
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",  # Foto 5 (Hal 3)
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",  # Foto 6 (Hal 3)
    ]

    # 1. KONDISI ALBUM TERTUTUP (Cover)
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

    # 2. KONDISI HALAMAN 1
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

    # 3. KONDISI HALAMAN 2
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

    # 4. KONDISI HALAMAN 3 (AKHIR)
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

    # Pilihan Filter Tampilan
    filter_pilihan = st.radio(
        "Tampilkan Profil:",
        ["Semua", "Pak Lurah", "Bu Lurah", "Anggota"],
        horizontal=True,
    )
    st.write("")

    gambar_urls = [
        (  # Pak Lurah (Indeks 0)
            "https://drive.google.com/uc?export=view&id=1CkTOku6mtZq-sryae2A1H_dx5moG-R1q"
        ),
        (  # Bu Lurah (Indeks 1)
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ),
        (  # Anggota 3 (Indeks 2)
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ),
        (  # Anggota 4 (Indeks 3)
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ),
        (  # Anggota 5 (Indeks 4)
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ),
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
            "nama": "Nama Anggota 3",
            "sebagai": "Anggota",
            "nim": "122450083",
            "fun_fact": "nyemilin es bata",
            "motto_hidup": "mantap",
        },
        {
            "nama": "Nama Anggota 4",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "nyemilin",
            "motto_hidup": "jalanin dulu aja",
        },
        {
            "nama": "Nama Anggota 5",
            "sebagai": "Anggota",
            "nim": "122450100",
            "fun_fact": "nyemilin es bata, kiko",
            "motto_hidup": "jalanin dulu keles",
        },
    ]

    # Menentukan indeks yang akan ditampilkan berdasarkan filter
    if filter_pilihan == "Semua":
      indices = [0, 1, 2, 3, 4]
    elif filter_pilihan == "Pak Lurah":
      indices = [0]
    elif filter_pilihan == "Bu Lurah":
      indices = [1]
    else:  # Anggota
      indices = [2, 3, 4]

    images = [load_image(u) for u in gambar_urls]

    for idx in indices:
      if idx < len(data_list) and idx < len(images):
        img = images[idx]
        data = data_list[idx]

        # Membuat tata letak: Foto di Kiri (Bingkai Emas), Biodata di Kanan (Old Paper)
        col_img, col_bio = st.columns([1, 1.5], vertical_alignment="center")

        with col_img:
          # Bingkai Emas untuk Foto
          st.markdown(
              """
                    <div style="
                        border: 6px solid #d4af37; 
                        padding: 6px; 
                        background: white; 
                        box-shadow: 0 6px 15px rgba(0,0,0,0.25); 
                        border-radius: 6px;
                        margin-bottom: 15px;">
                    """,
              unsafe_allow_html=True,
          )
          st.image(img, use_container_width=True)
          st.markdown("</div>", unsafe_allow_html=True)

        with col_bio:
          # Gaya Kertas Tua (Old Paper Style)
          st.markdown(
              f"""
                    <div style="
                        background-color: #f4ecd8; 
                        background-image: linear-gradient(to bottom, #f4ecd8, #e9dcbe);
                        border: 2px solid #b39b77; 
                        padding: 20px; 
                        border-radius: 8px; 
                        box-shadow: inset 0 0 15px rgba(139, 69, 19, 0.15), 0 4px 8px rgba(0,0,0,0.1); 
                        color: #3e2723;
                        font-family: serif;
                        margin-bottom: 15px;">
                        <h3 style="margin-top: 0; color: #5c3a21; border-bottom: 1px solid #b39b77; padding-bottom: 8px;">{data['nama']}</h3>
                        <p style="margin: 6px 0;"><b>Sebagai:</b> {data['sebagai']}</p>
                        <p style="margin: 6px 0;"><b>NIM:</b> {data['nim']}</p>
                        <p style="margin: 6px 0;"><b>Fun Fact:</b> {data['fun_fact']}</p>
                        <p style="margin: 6px 0;"><b>Motto Hidup:</b> <i>"{data['motto_hidup']}"</i></p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

        st.write("---")

  about_page()
