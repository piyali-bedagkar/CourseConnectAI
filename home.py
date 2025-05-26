import streamlit as st
from utils.ui_utils import render_top_navbar


st.set_page_config(page_title="Campus Knowledge Graph", layout="wide", initial_sidebar_state="collapsed")
render_top_navbar()
st.markdown("<br><br>", unsafe_allow_html=True)
st.title("Welcome to CampusBuddy")
st.markdown("<p style='color:#bbbbbb;'>Explore your courses like never before. AI-powered tools to make course discovery smarter and smoother.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-block">
        <h3>🏛️ Smith School</h3>
        <p>
        The Robert H. Smith School of Business is a hub for innovation, leadership, and analytics-driven decision making. 
        This platform taps into that spirit by giving students an intuitive way to explore course offerings and plan their academic path.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-block">
        <h3>🔗 Knowledge Graph</h3>
        <p>
        Visualize relationships between courses, professors, and key topics. 
        Discover patterns that help with elective planning and academic exploration.
        <div id="nav-right">
            <a class="nav-link" href="/knowledgegraph" target="_self">Go to <u>Knowledge Graph</u></a>
        </div> 
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-block">
        <h3>🤖 CampusBot</h3>
        <p>
        Got questions about course timings, professors, or what a class is about?
        Ask our smart assistant and get instant, AI-generated answers.
        <div id="nav-right">
            <a class="nav-link" href="/chatbot" target="_self" style="text-decoration: underline; color: #ffcc00;">Go to <u>Chatbot</u></a>
        </div>         
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.info("✨ Ready to explore? Head to 'Knowledge Graph' or 'Chatbot' from the top navigation.")


