from pathlib import Path

from backend.logging_config import setup_logging

import streamlit as st

setup_logging()
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "ask_your_data.png"

st.set_page_config(page_title="Ask Your Data", page_icon="🧠", layout="wide")

st.image(LOGO_PATH)

st.write(
    "Upload your documents, build your knowledge base and start asking questions in natural language."
)
