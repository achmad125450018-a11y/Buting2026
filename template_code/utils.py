# ============================================================
# utils.py — Shared Utilities untuk Semua Halaman Poisson
# Taruh di root (sejajar dengan main.py)
# ============================================================

import streamlit as st
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html as html_lib


# ============================================================
# GOOGLE DRIVE HELPER
# ============================================================
def get_drive_file_id(url):
    """Ekstrak file ID dari berbagai format Google Drive URL."""
    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        if query.get("id"):
            return query["id"][0]
        parts = parsed.path.split("/")
        if "d" in parts:
            idx = parts.index("d")
            if idx + 1 < len(parts):
                return parts[idx + 1]
    except Exception:
        pass
    return None


def _fetch_image(url, max_dim=800):
    """Fetch gambar dari Drive → return PIL Image (atau None)."""
    file_id = get_drive_file_id(url)
    candidate_urls = []
    if file_id:
        candidate_urls.extend([
            f"https://drive.google.com/thumbnail?id={file_id}&sz=w{max_dim}",
            f"https://lh3.googleusercontent.com/d/{file_id}=w{max_dim}",
            f"https://drive.google.com/uc?export=download&id={file_id}",
        ])
    candidate_urls.append(url)
    headers = {"User-Agent": "Mozilla/5.0"}
    for candidate in dict.fromkeys(candidate_urls):
        try:
            response = requests.get(candidate, headers=headers, timeout=10, allow_redirects=True)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img = ImageOps.exif_transpose(img).convert("RGB")
            img.load()
            return img
        except Exception:
            continue
    return None


# ============================================================
# CACHE GLOBAL — Dipakai bersama seluruh app
# ============================================================
@st.cache_data(show_spinner=False, ttl=1800, max_entries=300)
def image_data_uri(url):
    """Return base64 data URI. TTL 30 menit, max 300 entries."""
    img = _fetch_image(url, max_dim=800)
    if img is None:
        return None
    img = img.copy()
    max_dim = 800
    if max(img.size) > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=75, optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


@st.cache_data(show_spinner=False, ttl=1800, max_entries=80)
def load_image(url):
    """Return PIL Image. TTL 30 menit, max 80 entries."""
    return _fetch_image(url, max_dim=800)
