"""
Theme and styling utilities for MediVision AI
Royal Black Glassy Gradient Theme with Glassmorphism
"""

import streamlit as st


def apply_custom_theme():
    """Apply royal black glassy gradient theme with glassmorphism effects"""
    st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background - Royal Black Gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #1a1a2e 100%);
        background-attachment: fixed;
    }
    
    /* Glassmorphism Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px 0 rgba(83, 52, 131, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Header Styling */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
        text-shadow: 0 0 20px rgba(83, 52, 131, 0.5);
    }
    
    h1 {
        background: linear-gradient(90deg, #ffffff 0%, #b4b4b4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(26, 26, 46, 0.95) 0%, rgba(15, 52, 96, 0.95) 100%);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #533483 0%, #0f3460 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 32px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(83, 52, 131, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(83, 52, 131, 0.5);
        background: linear-gradient(135deg, #6a4a9e 0%, #1a4a7d 100%);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        color: white;
        padding: 12px;
        backdrop-filter: blur(5px);
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border: 1px solid rgba(83, 52, 131, 0.5);
        box-shadow: 0 0 15px rgba(83, 52, 131, 0.3);
    }
    
    /* Radio Buttons */
    .stRadio > label {
        color: #ffffff !important;
        font-weight: 500;
    }
    
    .stRadio > div {
        background: rgba(255, 255, 255, 0.05);
        padding: 12px;
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.05);
        border: 2px dashed rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 20px;
        backdrop-filter: blur(5px);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.2) 50%, transparent 100%);
        margin: 24px 0;
    }
    
    /* Alert Boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border-left: 4px solid #533483;
    }
    
    /* Success Message */
    .stSuccess {
        background: rgba(46, 204, 113, 0.1);
        border-left: 4px solid #2ecc71;
    }
    
    /* Error Message */
    .stError {
        background: rgba(231, 76, 60, 0.1);
        border-left: 4px solid #e74c3c;
    }
    
    /* Warning Message */
    .stWarning {
        background: rgba(243, 156, 18, 0.1);
        border-left: 4px solid #f39c12;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        backdrop-filter: blur(5px);
        color: white !important;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }
    
    /* Code Block */
    .stCodeBlock {
        background: rgba(0, 0, 0, 0.3) !important;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #533483 0%, #0f3460 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #6a4a9e 0%, #1a4a7d 100%);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 4px;
        backdrop-filter: blur(5px);
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #b4b4b4;
        border-radius: 8px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #533483 0%, #0f3460 100%);
        color: white !important;
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 28px !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #b4b4b4 !important;
        font-size: 14px !important;
    }
    
    /* Images */
    img {
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stApp > header {
        animation: fadeIn 0.5s ease;
    }
    
    /* Link Styling */
    a {
        color: #8b7fb8 !important;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    a:hover {
        color: #b8a9d4 !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #533483 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def create_gradient_header(title: str, subtitle: str = None):
    """Create a gradient header with optional subtitle"""
    subtitle_html = ""
    if subtitle:
        subtitle_html = f'<p style="font-size: 20px; color: #b4b4b4; margin-top: 10px; font-weight: 300;">{subtitle}</p>'
    
    header_html = f'''<div style="text-align: center; padding: 40px 20px; background: linear-gradient(135deg, rgba(83, 52, 131, 0.2) 0%, rgba(15, 52, 96, 0.2) 100%); border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 30px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);"><h1 style="font-size: 48px; margin: 0; background: linear-gradient(90deg, #ffffff 0%, #b4b4b4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-shadow: none;">{title}</h1>{subtitle_html}</div>'''
    
    st.markdown(header_html, unsafe_allow_html=True)


def create_glass_card(content: str):
    """Create a glassmorphism card"""
    card_html = f'<div class="glass-card">{content}</div>'
    st.markdown(card_html, unsafe_allow_html=True)
