import streamlit as st
import requests
import os
from utils.ui_utils import render_top_navbar
from utils.pdf_parser import parse_pdf_to_txt
from markdown import markdown
import re

# --- Page Config and Navbar ---
st.set_page_config(page_title="CampusBot", layout="wide", initial_sidebar_state="collapsed")
render_top_navbar()

# --- Page Title and Intro ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.title("Ask About Your Courses")
st.markdown("""
<p style='color:#bbbbbb;'>Get instant answers to questions about course content, timings, or professors. Powered by LLM.</p>
""", unsafe_allow_html=True)

# --- Load Course Data from PDF ---
if "raw_text" not in st.session_state:
    try:
        pdf_path = "data/courses.pdf"
        output_txt = parse_pdf_to_txt(pdf_path)
        with open(output_txt, "r", encoding="utf-8") as f:
            st.session_state.raw_text = f.read()
    except Exception as e:
        st.error(f"❌ Failed to load course PDF: {e}")
        st.stop()

# --- Ask One Question ---
st.markdown("<br>", unsafe_allow_html=True)
user_question = st.text_input("Type your course-related question below:")

if user_question:

    prompt = f"""You are an expert university assistant. Use the course information below to answer the user's question.

Course Info:
{st.session_state.raw_text}

User Question: {user_question}
Answer:"""

    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300,
        "temperature": 0.5
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        if res.status_code == 200:
            reply = res.json()["choices"][0]["message"]["content"]
            
            st.markdown(f"""
            <div style="
                background-color: #1e4d2b;
                color: white;
                        padding: 16px 24px;
                border-radius: 10px;
                max-height: 220px;
                overflow-y: auto;
            ">
            {reply}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ LLM request failed.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
