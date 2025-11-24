"""
MediVision AI - Medical Image Analysis Assistant
Main application entry point
"""

import streamlit as st
from config import APP_TITLE, APP_ICON, APP_LAYOUT
from components import render_main_page

# Configure Streamlit page
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/MediVision-AI',
        'Report a bug': 'https://github.com/yourusername/MediVision-AI/issues',
        'About': f"""
        # {APP_TITLE}
        
        **Diagnose with Clarity, Treat with Confidence**
        
        An AI-powered medical image analysis assistant that provides educational 
        insights into medical imaging and health symptoms.
        
        ## Features
        - 🤖 Multi-model AI support (4 models)
        - 🌍 Multi-language output (12+ languages)
        - 📊 Real-time token tracking
        - 💾 Conversation history
        - 🔒 Encrypted API key storage
        - 📥 Markdown export
        
        ## Disclaimer
        This tool is for educational purposes only. Always consult qualified 
        healthcare professionals for medical advice.
        
        ---
        Version 2.0.0 | Built with Streamlit & Google Gemini
        """
    }
)

# Main application
if __name__ == "__main__":
    render_main_page()
