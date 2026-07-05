from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "ask_your_data.png"

st.set_page_config(page_title="Ask Your Data", page_icon="🧠", layout="wide")

st.image(LOGO_PATH)

st.write(
    "Upload your documents, build your knowledge base and start asking questions in natural language."
)
