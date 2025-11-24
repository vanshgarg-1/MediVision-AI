"""
UI Components for MediVision AI
"""

import streamlit as st
from config.prompts import EXAMPLE_TEMPLATES


def render_navbar():
    """Render top navigation bar with token stats"""
    from utils import get_token_stats, get_token_stats_display
    
    stats = get_token_stats()
    display_stats = get_token_stats_display(stats["total_tokens"], stats["total_cost"])
    
    # Navigation tabs
    col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
    
    with col1:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            # Switch to home without forcing full rerun so existing analysis stays visible
            st.session_state.current_page = "home"
            # Keep previous input mode; do not reset or rerun to preserve UI state
    
    with col2:
        if st.button("📜 History", key="nav_history", use_container_width=True):
            # History page benefits from a clean render; trigger rerun
            st.session_state.current_page = "history"
            st.rerun()
    
    with col3:
        st.markdown(f'<div style="text-align: center; padding: 8px;"><div style="color: #b4b4b4; font-size: 10px;">TOKENS</div><div style="color: #ffffff; font-weight: 600;">{display_stats["tokens"]}</div></div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown(f'<div style="text-align: center; padding: 8px;"><div style="color: #b4b4b4; font-size: 10px;">COST</div><div style="color: #2ecc71; font-weight: 600;">{display_stats["cost"]}</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")


def render_example_cards():
    """Render example query cards in side-by-side layout"""
    
    st.markdown("### 📚 Quick Start Examples")
    st.markdown("Click any example to use it as a template:")
    
    # Create 2 columns for side-by-side layout
    examples_list = list(EXAMPLE_TEMPLATES.items())
    
    for i in range(0, len(examples_list), 2):
        col1, col2 = st.columns(2)
        
        # First card
        with col1:
            if i < len(examples_list):
                name, details = examples_list[i]
                render_example_card(name, details)
        
        # Second card
        with col2:
            if i + 1 < len(examples_list):
                name, details = examples_list[i + 1]
                render_example_card(name, details)


def render_example_card(name: str, details: dict):
    """Render a single example card"""
    text_preview = details['text'][:100].replace('"', '&quot;').replace("'", "&#39;")
    card_html = f'<div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1); padding: 16px; margin-bottom: 16px; cursor: pointer; transition: all 0.3s ease; height: 140px; display: flex; flex-direction: column;" onmouseover="this.style.transform=\'translateY(-5px)\'; this.style.borderColor=\'rgba(83, 52, 131, 0.5)\';" onmouseout="this.style.transform=\'translateY(0)\'; this.style.borderColor=\'rgba(255, 255, 255, 0.1)\';"><div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;"><span style="font-size: 24px;">{details["icon"]}</span><div><div style="color: #ffffff; font-weight: 600; font-size: 14px;">{name}</div><div style="color: #b4b4b4; font-size: 11px;">{details["category"]}</div></div></div><div style="color: #b4b4b4; font-size: 12px; line-height: 1.4; flex-grow: 1; overflow: hidden;">{text_preview}...</div></div>'
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Button to use this example
    if st.button(f"Use {name}", key=f"btn_{name}", use_container_width=True):
        st.session_state.example_text = details['text']
        st.rerun()


def render_feedback_section(response_id: str = None):
    """Render feedback buttons"""
    from utils import add_feedback, get_feedback_stats
    
    st.markdown("---")
    st.markdown("### 💭 Was this analysis helpful?")
    
    col1, col2, col3 = st.columns([1, 1, 4])
    
    with col1:
        if st.button("👍 Helpful", key=f"feedback_pos_{response_id}", use_container_width=True):
            add_feedback(True)
            st.success("Thank you for your feedback!")
    
    with col2:
        if st.button("👎 Not Helpful", key=f"feedback_neg_{response_id}", use_container_width=True):
            add_feedback(False)
            st.info("Thank you! We'll work on improving.")
    
    # Show feedback stats
    stats = get_feedback_stats()
    total = stats["positive"] + stats["negative"]
    if total > 0:
        satisfaction = (stats["positive"] / total) * 100
        st.caption(f"📊 Satisfaction rate: {satisfaction:.1f}% ({stats['positive']}/{total})")


def render_model_selector():
    """Render model selection dropdown"""
    from config.settings import AVAILABLE_MODELS, DEFAULT_MODEL
    
    st.sidebar.markdown("### 🤖 AI Model")
    
    model_options = list(AVAILABLE_MODELS.keys())
    model_descriptions = [AVAILABLE_MODELS[m]["description"] for m in model_options]
    
    selected_model = st.sidebar.selectbox(
        "Select Model:",
        model_options,
        index=model_options.index(DEFAULT_MODEL),
        help="Choose AI model for analysis",
        label_visibility="collapsed"
    )
    
    # Show model info
    model_info = AVAILABLE_MODELS[selected_model]
    st.sidebar.caption(f"📝 {model_info['description']}")
    st.sidebar.caption(f"⚡ {model_info['max_tokens']:,} tokens")
    
    return selected_model


def render_prompt_style_selector():
    """Render prompt style selection"""
    from config.prompts import PROMPT_STYLES
    
    st.sidebar.markdown("### 🎨 Style")
    
    style_options = list(PROMPT_STYLES.keys())
    
    selected_style = st.sidebar.selectbox(
        "Select Style:",
        ["Default"] + style_options,
        help="Customize response format",
        label_visibility="collapsed"
    )
    
    if selected_style != "Default":
        style_info = PROMPT_STYLES[selected_style]
        st.sidebar.caption(f"ℹ️ {style_info['description']}")
        return style_info["suffix"]
    
    return None


def render_regenerate_options():
    """Render regeneration options"""
    from config.prompts import REGENERATION_OPTIONS
    
    st.markdown('<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1); padding: 24px; margin: 32px 0;"><div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;"><span style="font-size: 28px;">🔄</span><h3 style="margin: 0; color: #ffffff;">Refine This Analysis</h3></div><p style="color: #b4b4b4; margin-bottom: 24px;">Want a different perspective? Choose an option:</p></div>', unsafe_allow_html=True)
    
    cols = st.columns(len(REGENERATION_OPTIONS))
    
    for idx, (name, details) in enumerate(REGENERATION_OPTIONS.items()):
        with cols[idx]:
            if st.button(
                f"{details['emoji']} {name}",
                key=f"regen_{name}",
                help=details['instruction'],
                use_container_width=True
            ):
                st.session_state.regenerate_instruction = details['instruction']
                st.session_state.regenerate_count = st.session_state.get('regenerate_count', 0) + 1
                st.rerun()



