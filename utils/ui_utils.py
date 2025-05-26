import streamlit as st
import base64

def render_top_navbar():
    # Load logos
    with open("umd logo.svg", "rb") as f:
        svg_data = f.read()
        svg_base64 = base64.b64encode(svg_data).decode("utf-8")

    with open("testudo.jpg", "rb") as f:
        banner_base64 = base64.b64encode(f.read()).decode("utf-8")



    # Inject CSS + Navbar HTML
    st.markdown(f"""
<style>
html, body, [data-testid="stApp"], .main, .block-container {{
    background-color: black !important;
    color: white;
    overflow: hidden !important;
    height: 100vh !important;
}}

[data-testid="stAppViewContainer"] {{
    background-color: rgba(0, 0, 0, 0.85) !important;
}}
                
#below-navbar-banner {{
    position: fixed;
    width: 100%;
    height: 270px;
    left: 0;
    margin: 0;
    padding: 0;
    background: url("data:image/jpg;base64,{banner_base64}") no-repeat center center;
    background-size: cover;
    border-top: 1px solid #333;
    border-bottom: 1px solid #333;
}}


.glass-block {{
    background: rgba(40, 40, 70, 0.25);
    padding: 30px 25px;
    border-radius: 40px;
    backdrop-filter: blur(20px);
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
}}
.glass-block h3 {{
    color: #ffffff;
}}
.glass-block p {{
    color: #dddddd;
    font-size: 15px;
}}

html, body, [data-testid="stApp"] > div:first-child {{
    padding-top: 130px !important;
}}

#umd-bar-wrapper {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    z-index: 10000 !important;
}}

#top-bar {{
    background-color: #c60000;
    height: 40px;
    line-height: 40px;
    color: white;
    font-family: 'Georgia', serif;
    font-size: 14px;
    padding-left: 85px;
    letter-spacing: 0.5px;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    z-index: 999999;
}}

#nav-bar {{
    background-color: #1a1a1a;
    padding: 14px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    top: 40px;
    left: 0;
    width: 100vw;
    z-index: 999998;
}}

#nav-left {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

#branding-block {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

#umd-logo {{
    height: 50px;
    filter: brightness(100%) contrast(110%);
}}

#testudo-logo {{
    height: 48px;
    border-radius: 50%;
    box-shadow: 0 0 5px rgba(0,0,0,0.4);
}}

#nav-right {{
    display: flex;
    align-items: center;
    gap: 22px;
}}

.nav-link {{
    color: white !important;
    text-decoration: none !important;
    font-size: 15px;
    font-family: 'Segoe UI', sans-serif;
}}

.nav-link:hover {{
    color: #ffcc00 !important;
}}
</style>

<div id="top-bar">UNIVERSITY OF MARYLAND</div>
<div id="nav-bar">
    <div id="nav-left">
        <div id="branding-block">
            <img id="umd-logo" src="data:image/svg+xml;base64,{svg_base64}">
        </div>
    </div>
    <div id="nav-right">
        <a class="nav-link" href="/home" target="_self">Home</a>
        <a class="nav-link" href="/knowledgegraph" target="_self">Knowledge Graph</a>
        <a class="nav-link" href="/chatbot" target="_self">Chatbot</a>
    </div>
</div>
<div id="below-navbar-banner"></div>
""", unsafe_allow_html=True)
