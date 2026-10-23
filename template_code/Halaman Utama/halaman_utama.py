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


def display_images_with_data(gambar_urls, data_list):
  images = []
  for i, url in enumerate(gambar_urls):
    with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
      img = load_image(url)
      if img is not None:
        images.append(img)

  for i, img in enumerate(images):
    # menampilkan gambar di tengah
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      st.image(img, use_container_width=True)

    if i < len(data_list):
      st.write(f"Nama: {data_list[i]['nama']}")
      st.write(f"Sebagai: {data_list[i]['sebagai']}")
      st.write(f"NIM: {data_list[i]['nim']}")
      st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
      st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")
      st.write("---")  # Pembatas antar anggota


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

    # --- FITUR ALBUM COSVAL ---
    st.markdown(
        "<h2 style='text-align: center;'>📖 Album Dokumentasi Cosval</h2>",
        unsafe_allow_html=True,
    )

    # Inisialisasi state halaman album (0 = Tertutup, 1 = Hal 1, 2 = Hal 2, 3 = Hal 3)
    if "album_page" not in st.session_state:
      st.session_state.album_page = 0

    # Daftar 6 foto untuk 3 halaman album (masing-masing 2 foto per halaman)
    # Anda bisa mengganti URL di bawah ini dengan foto dokumentasi kelompok Anda
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
            <div style="border: 3px dashed #FCF0DA; padding: 40px; text-align: center; border-radius: 15px; background-color: #fdfbf7;">
                <h2> ALBUM COSVAL</h2>
                <p>Album kenangan dan dokumentasi kegiatan kelompok kami.</p>
                <p style="color: gray; font-size: 0.9em;">Klik tombol di bawah untuk membuka album.</p>
            </div>
            """,
          unsafe_allow_html=True,
      )
      st.write("")
      col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
      with col_btn2:
        if st.button("📖 Buka Album", use_container_width=True):
          st.session_state.album_page = 1
          st.rerun()

    # 2. KONDISI HALAMAN 1
    elif st.session_state.album_page == 1:
      st.markdown(
          "<h4 style='text-align: center; color: #555;'>Halaman 1 / 3</h4>",
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        st.image(
            load_image(album_photos[0]),
            caption="Dokumentasi 1",
            use_container_width=True,
        )
      with col2:
        st.image(
            load_image(album_photos[1]),
            caption="Dokumentasi 2",
            use_container_width=True,
        )

      st.write("")
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
          "<h4 style='text-align: center; color: #555;'>Halaman 2 / 3</h4>",
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        st.image(
            load_image(album_photos[2]),
            caption="Dokumentasi 3",
            use_container_width=True,
        )
      with col2:
        st.image(
            load_image(album_photos[3]),
            caption="Dokumentasi 4",
            use_container_width=True,
        )

      st.write("")
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
          "<h4 style='text-align: center; color: #555;'>Halaman 3 / 3 (Akhir)</h4>",
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        st.image(
            load_image(album_photos[4]),
            caption="Dokumentasi 5",
            use_container_width=True,
        )
      with col2:
        st.image(
            load_image(album_photos[5]),
            caption="Dokumentasi 6",
            use_container_width=True,
        )

      st.write("")
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

    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1CkTOku6mtZq-sryae2A1H_dx5moG-R1q",
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
                "Dengan bekingan doa ibu, jangankan kalah imbangpun saya tidak"
                " sudi!"
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
    display_images_with_data(gambar_urls, data_list)

  about_page()
