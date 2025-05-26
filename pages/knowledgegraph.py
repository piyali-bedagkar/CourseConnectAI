import streamlit as st
from utils.ui_utils import render_top_navbar
from utils.graph_utils import build_graph, visualize_graph
from utils.pdf_parser import parse_pdf_to_txt
import os

st.set_page_config(page_title="Knowledge Graph", layout="wide", initial_sidebar_state="collapsed")
render_top_navbar()
st.markdown("""
    <style>
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
        margin: 0 !important;
    }
    .main {
        padding: 0 !important;
        margin: 0 !important;
    }
    body, html {
        overflow: hidden !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Directly load PDF from the 'data' folder ---
pdf_path = "data/courses.pdf"  # 📌 Make sure this file exists in your project
output_txt = parse_pdf_to_txt(pdf_path)

with open(output_txt, "r", encoding="utf-8") as f:
    combined_text = f.read()

# Save into session for use in chatbot
st.session_state.raw_text = combined_text

# Extract entities and build graph if not already done
from utils.nlp import extract_entities
st.session_state.entities = extract_entities(st.session_state.raw_text)
st.session_state.G = build_graph(st.session_state.entities)

visualize_graph(st.session_state.G) 
