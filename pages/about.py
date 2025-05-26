# --------------------------------------
# pages/About.py
import streamlit as st
from utils.ui_utils import render_top_navbar


st.set_page_config(page_title="About", layout="wide", initial_sidebar_state="collapsed")
render_top_navbar()

st.title("📖 About the Campus Knowledge Graph")
st.markdown("""
This platform allows university students to:
- Explore course-professor-topic relationships visually
- Ask questions about available courses
- Upload PDFs or text and instantly get structured insights

Built with ❤️ using Streamlit, PyVis, and OpenRouter LLM.
""")