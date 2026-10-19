import base64
import json
import random
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CẤU HÌNH ỨNG DỤNG
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
st.set_page_config(
    page_title="Game Toán học",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# CSS: CHỮ TO, ĐẬM, TƯƠNG PHẢN CAO
# =========================================================
st.markdown(
    """
    <style>
    /* Cỡ chữ mặc định */
    html, body, [class*="css"] {
        font-size: 20px;
    }

    .stApp,
    [data-testid="stAppViewContainer"] {
        color: #FFFFFF !important;
    }

    /* Tiêu đề */
    h1 {
        color: #FFFFFF !important;
        font-size: 44px !important;
        font-weight: 900 !important;
        line-height: 1.25 !important;
        text-shadow: 3px 3px 6px #000000, 0 0 12px #000000 !important;
    }

    h2 {
        color: #FFFFFF !important;
        font-size: 34px !important;
        font-weight: 900 !important;
        line-height: 1.35 !important;
        text-shadow: 2px 2px 5px #000000, 0 0 8px #000000 !important;
    }

    h3 {
        color: #FFFFFF !important;
        font-size: 28px !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 5px #000000 !important;
    }

    /* Nội dung chữ */
    .stMarkdown p,
    .stMarkdown li,
    [data-testid="stCaptionContainer"] {
        color: #FFFFFF !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        line-height: 1.7 !important;
        text-shadow: 1px 1px 4px #000000 !important;
    }

    /* Nhãn các widget */
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label {
        color: #FFFFFF !important;
        font-size: 23px !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 4px #000000 !important;
    }

    /* Câu trả lời trắc nghiệm */
    [data-testid="stRadio"] label,
    [data-testid="stRadio"] label p {
        color: #FFFFFF !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        line-height: 1.6 !important;
        text-shadow: 1px 1px 3px #000000 !important;
    }

    [data-testid="stRadio"] > div {
        gap: 12px !important;
        padding: 18px 20px !important;
        background: rgba(10, 15, 30, 0.94) !important;
        border: 2px solid #60A5FA !important;
        border-radius: 16px !important;
