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

# Global Theme Styling: Inter & Courier New + Futuristic Green & Black + Sidebar Fix
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+New:wght@400;700&family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="st"] {
        font-family: 'Inter', sans-serif !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    
    .stApp {
        background-color: #030712;
        color: #f8fafc;
    }

    /* Perbaikan sidebar agar teks rapi, jelas, dan tidak menimpa */
    [data-testid="stSidebar"] {
        min-width: 310px !important;
        padding-top: 1rem;
        background-color: #060918 !important;
    }
    [data-testid="stSidebarNav"] {
        width: 100%;
    }
    [data-testid="stSidebarNav"] ul {
        display: flex;
        flex-direction: column;
        gap: 12px !important;
    }
    [data-testid="stSidebarNav"] li {
        margin: 4px 0 !important;
    }
    [data-testid="stSidebarNav"] a {
        display: flex !important;
        align-items: center !important;
        height: auto !important;
        min-height: 48px !important;
        padding: 10px 14px !important;
        line-height: 1.4 !important;
        white-space: normal !important;
        font-size: 0.95em !important;
        border-radius: 8px;
        transition: background 0.2s;
    }
    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(34, 197, 94, 0.15) !important;
    }
    [data-testid="stSidebarNav"] span {
        display: inline-block !important;
        white-space: normal !important;
        line-height: 1.4 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 4.2em; font-weight: 800; color: #4ade80; text-shadow: 0 0 25px rgba(74, 222, 128, 0.4); font-family: "Courier New", monospace; letter-spacing: 2px; margin-bottom: 0;'>WEBSITE KATING</h1>
        <p style='font-size: 1.5em; font-weight: 600; color: #94a3b8; letter-spacing: 3px; text-transform: uppercase; margin-top: 10px;'>CEO HMSD Adyatama ITERA 2026</p>
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
          "container": {
              "padding": "0!important",
              "background-color": "#0f172a",
              "border-radius": "12px",
              "border": "1px solid #22c55e",
          },
          "icon": {"color": "#4ade80", "font-size": "19px"},
          "nav-link": {
              "font-size": "15px",
              "text-align": "center",
              "margin": "0px",
              "color": "#f8fafc",
              "font-family": "Inter, sans-serif",
              "--hover-color": "#22c55e22",
          },
          "nav-link-selected": {
              "background-color": "#22c55e",
              "color": "#030712",
              "font-weight": "bold",
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
            font-family: 'Courier New', monospace;
            font-size: 2.3em;
            color: #4ade80;
            margin-bottom: 20px;
            font-weight: 700;
            text-shadow: 0 0 15px rgba(74, 222, 128, 0.3);
        }
        
        .photo-caption-box {
            background: linear-gradient(135deg, #0f172a, #030712);
            color: white;
            text-align: center;
            padding: 20px 15px;
            border-bottom-left-radius: 16px;
            border-bottom-right-radius: 16px;
            margin-bottom: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5);
            border: 1px solid #22c55e;
            border-top: none;
        }
        
        .badge-cosval {
            display: inline-block;
            background: #22c55e;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            margin-bottom: 10px;
            letter-spacing: 2px;
            font-weight: 700;
            color: #030712;
            box-shadow: 0 0 10px rgba(34,197,94,0.4);
        }
        
        .photo-text-title {
            margin: 0;
            font-family: 'Inter', sans-serif;
            font-size: 1.3em;
            font-weight: 700;
            line-height: 1.4;
            color: #f8fafc;
        }

        .desc-box {
            border: 2px solid #22c55e;
            background: #0f172a;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 8px 25px rgba(34, 197, 94, 0.15);
            margin-bottom: 30px;
            word-wrap: break-word;
        }
        
        .desc-heading {
            color: #4ade80;
            font-family: 'Courier New', monospace;
            margin-top: 0;
            margin-bottom: 15px;
            font-size: 1.5em;
            font-weight: 700;
        }
        
        .desc-content {
            color: #e2e8f0;
            font-family: 'Inter', sans-serif;
            line-height: 1.8;
            font-size: 1.05em;
            margin: 0;
            text-align: justify;
        }

        .book-cover {
            background: linear-gradient(135deg, #0f172a, #030712);
            color: white;
            padding: 50px 20px;
            text-align: center;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.6);
            border: 2px solid #22c55e;
            margin-bottom: 20px;
        }
        
        .book-spread {
            background: #0f172a;
            border: 2px solid #22c55e;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(34, 197, 94, 0.2);
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
        "<h2 style='text-align: center; color: #4ade80; font-family:"
        " \"Courier New\", monospace; font-weight: 700;'>Album Dokumentasi"
        " Cosval</h2>",
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
                <h1 style="color: #4ade80; font-family: 'Courier New', monospace; font-weight: 700;">ALBUM Kelompok COSVAL</h1>
                <p style="color: #94a3b8;">Album kenangan dan dokumentasi kegiatan kelompok kami.</p>
                <p style="color: #22c55e; font-size: 0.9em; margin-top: 15px; font-weight: 600;">Klik tombol di bawah untuk membuka lembaran buku album.</p>
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
                <h4 style='text-align: center; color: #4ade80; margin-top: 0;'>— Halaman 1 dari 3 —</h4>
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
                <h4 style='text-align: center; color: #4ade80; margin-top: 0;'>— Halaman 2 dari 3 —</h4>
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
                <h4 style='text-align: center; color: #4ade80; margin-top: 0;'>— Halaman 3 dari 3 (Akhir) —</h4>
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
        """<style>.centered-title {text-align: center; color: #4ade80; font-family:"Courier New", monospace; font-weight: 700;}</style>""",
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .about-photo img {
            border: 4px solid #22c55e !important;
            outline: 2px solid #030712 !important;
            border-radius: 12px !important;
            padding: 4px !important;
            background-color: #0f172a !important;
            box-shadow: 0 8px 20px rgba(34, 197, 94, 0.3) !important;
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
          " margin-bottom: 20px; color: #4ade80; font-family: \"Courier New\","
          " monospace; font-weight: 700;'>Kenalan Yuk Sama Cosval!</h2>",
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
                        background: linear-gradient(135deg, #0f172a 0%, #030712 100%), radial-gradient(circle at top right, rgba(34,197,94,0.12), transparent 50%); 
                        border: 2px solid #22c55e; 
                        padding: 24px; 
                        border-radius: 12px; 
                        box-shadow: 0 6px 20px rgba(34, 197, 94, 0.2); 
                        color: #f8fafc;
                        font-family: 'Inter', sans-serif;
                        word-wrap: break-word;
                        position: relative;
                        overflow: hidden;
                        margin-bottom: 20px;">
                        <div style="position: absolute; top: 0; right: 0; width: 70px; height: 70px; background: linear-gradient(135deg, transparent 50%, rgba(34,197,94,0.25) 50%); pointer-events: none;"></div>
                        <h3 style="margin-top: 0; color: #4ade80; border-bottom: 2px solid #22c55e; padding-bottom: 8px; font-family: 'Courier New', monospace;">{data['nama']}</h3>
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
