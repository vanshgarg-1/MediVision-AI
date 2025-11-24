"""
Page components for MediVision AI
"""

import streamlit as st


def render_main_page():
    """Render main analysis page"""
    from components.ui_components import (
        render_navbar,
        render_model_selector,
        render_prompt_style_selector,
        render_feedback_section,
        render_regenerate_options
    )
    from utils import (
        apply_custom_theme,
        create_gradient_header,
        initialize_session_state,
        get_api_key,
        store_api_key,
        validate_api_key
    )
    from config import APP_TAGLINE, INPUT_MODES, SUPPORTED_LANGUAGES, SUPPORTED_IMAGE_FORMATS
    
    # Apply theme
    apply_custom_theme()
    
    # Initialize session
    initialize_session_state()
    
    # Render navbar
    render_navbar()
    
    # Sidebar configuration (header rendered only on main page below)
    st.sidebar.header("⚙️ Configuration")
    
    # API Key input
    api_key_input = st.sidebar.text_input(
        "Enter Google API Key:",
        type="password",
        help="Your API key is encrypted and stored securely in session"
    )
    
    if api_key_input:
        if not store_api_key(api_key_input):
            st.sidebar.error("❌ Invalid API key format")
    
    stored_key = get_api_key()
    
    # Model selector
    selected_model = render_model_selector()
    
    # Input mode
    st.sidebar.markdown("### 📥 Input Mode")
    default_mode = st.session_state.get("input_mode", "Text Only")
    default_index = INPUT_MODES.index(default_mode) if default_mode in INPUT_MODES else 0
    option = st.sidebar.radio("Select input type:", INPUT_MODES, index=default_index)
    st.session_state.input_mode = option  # Store selection
    
    # Language selection
    st.sidebar.markdown("### 🌍 Language")
    language = st.sidebar.selectbox("Output Language:", SUPPORTED_LANGUAGES, label_visibility="collapsed")
    
    # Prompt style
    prompt_style = render_prompt_style_selector()
    
    # Check current page
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    
    # Route to appropriate page (render header only for main page)
    if st.session_state.current_page == "history":
        render_history_page()
        return
    else:
        create_gradient_header("MediVision AI 🩺", APP_TAGLINE)
    
    # Main content area
    st.markdown("---")
    
    # Input fields
    user_text = ""
    file_uploaded = None
    
    if option == "Text Only" or option == "Text + Image":
        user_text = st.text_area(
            "Enter symptoms, history, or medical reports:",
            height=150,
            help="Describe patient symptoms, medical history, or observations"
        )
    
    if option == "Image Only" or option == "Text + Image":
        file_uploaded = st.file_uploader(
            'Upload medical image for analysis',
            type=SUPPORTED_IMAGE_FORMATS,
            help="Upload X-rays, scans, or medical images"
        )
        if file_uploaded:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(file_uploaded, caption='Uploaded Medical Image', use_container_width=True)
    
    # Generate button
    st.markdown("---")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        submit = st.button("🔬 Generate Analysis", use_container_width=True, type="primary")
    
    # Process analysis
    if submit:
        if not stored_key:
            st.error("⚠️ Please enter your Google API key in the sidebar")
        elif not (file_uploaded or user_text):
            st.warning("⚠️ Please provide either text input or upload an image")
        else:
            process_analysis(
                api_key=stored_key,
                model_name=selected_model,
                user_text=user_text,
                file_uploaded=file_uploaded,
                language=language,
                input_mode=option,
                prompt_style=prompt_style
            )
    
    # Show regenerate options if response exists
    if st.session_state.get("current_response"):
        st.markdown("---")
        render_regenerate_options()
        
        # If regenerate was clicked
        if st.session_state.get("regenerate_instruction"):
            process_analysis(
                api_key=stored_key,
                model_name=selected_model,
                user_text=st.session_state.get("last_user_text", user_text),
                file_uploaded=st.session_state.get("last_file_uploaded", file_uploaded),
                language=language,
                input_mode=option,
                regenerate_instruction=st.session_state.regenerate_instruction
            )
            st.session_state.regenerate_instruction = None


def process_analysis(
    api_key: str,
    model_name: str,
    user_text: str,
    file_uploaded,
    language: str,
    input_mode: str,
    prompt_style: str = None,
    regenerate_instruction: str = None
):
    """Process medical analysis request"""
    from utils import (
        initialize_model,
        generate_response,
        stream_response,
        validate_response,
        check_safety_block,
        prepare_prompt,
        estimate_tokens,
        calculate_cost,
        update_token_stats,
        add_to_history,
        format_medical_response,
        format_markdown_export,
        get_export_filename
    )
    from config import get_system_prompt
    
    # Store for regeneration
    st.session_state.last_user_text = user_text
    st.session_state.last_file_uploaded = file_uploaded
    
    # Initialize model
    with st.spinner("🔄 Initializing AI model..."):
        model = initialize_model(api_key, model_name)
    
    if not model:
        st.error("❌ Failed to initialize model")
        return
    
    # Prepare prompt
    system_prompt = get_system_prompt(language)
    
    image_data = None
    if file_uploaded:
        image_data = file_uploaded.getvalue()
    
    prompt_parts = prepare_prompt(
        system_prompt=system_prompt,
        user_text=user_text,
        image_data=image_data,
        prompt_style=prompt_style,
        regenerate_instruction=regenerate_instruction
    )
    
    # Generate response with streaming
    st.markdown(f"## 🏥 Medical Analysis ({language})")
    st.markdown("---")
    
    response_placeholder = st.empty()
    full_response = ""
    
    try:
        with st.spinner("🔬 Analyzing..."):
            response = generate_response(model, prompt_parts, stream=True)
            
            if response:
                for chunk in stream_response(response):
                    full_response += chunk
                    formatted_response = format_medical_response(full_response)
                    response_placeholder.markdown(formatted_response)
        
        # Store response
        st.session_state.current_response = full_response
        
        # Calculate tokens and cost
        input_tokens = estimate_tokens(str(prompt_parts))
        output_tokens = estimate_tokens(full_response)
        total_tokens = input_tokens + output_tokens
        cost = calculate_cost(input_tokens, output_tokens)
        
        # Update stats
        update_token_stats(total_tokens, cost)
        
        # Add to history
        add_to_history(
            query=user_text or "Image Analysis",
            response=full_response,
            input_mode=input_mode,
            language=language,
            model=model_name,
            tokens=total_tokens
        )
        
        # Show token info
        st.info(f"📊 Tokens used: {total_tokens:,} | Estimated cost: ${cost:.4f}")
        
        # Export button
        st.markdown("---")
        export_content = format_markdown_export(
            query=user_text or "Image Analysis",
            response=full_response,
            input_mode=input_mode,
            language=language,
            model=model_name
        )
        
        st.download_button(
            label="📥 Download Analysis Report",
            data=export_content,
            file_name=get_export_filename(),
            mime="text/markdown",
            use_container_width=True
        )
        
        # Feedback section
        from components.ui_components import render_feedback_section
        render_feedback_section(response_id=str(total_tokens))
        
    except Exception as e:
        st.error(f"❌ An error occurred during analysis: {e}")


def render_history_page():
    """Render history page with all conversations"""
    from utils import get_history, create_gradient_header
    
    create_gradient_header("📜 Analysis History", "Review your past medical analyses")
    
    history = get_history()
    
    if not history:
        st.info("📭 No analysis history yet. Start by creating your first analysis!")
        if st.button("➕ Create New Analysis"):
            st.switch_page("app.py")
        return
    
    # Stats
    st.markdown("### 📊 Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Analyses", len(history))
    
    with col2:
        total_tokens = sum(item.get("tokens", 0) for item in history)
        st.metric("Total Tokens", f"{total_tokens:,}")
    
    with col3:
        languages = set(item.get("language", "Unknown") for item in history)
        st.metric("Languages Used", len(languages))
    
    with col4:
        models = set(item.get("model", "Unknown") for item in history)
        st.metric("Models Used", len(models))
    
    st.markdown("---")
    st.markdown("### 📋 Conversation History")
    
    # Display each history item
    for idx, item in enumerate(history):
        with st.expander(
            f"**{item['chat_name']}** - {item['timestamp']}",
            expanded=(idx == 0)
        ):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**Model:** {item['model']}")
                st.markdown(f"**Language:** {item['language']}")
                st.markdown(f"**Input Mode:** {item['input_mode']}")
            
            with col2:
                st.metric("Tokens", f"{item['tokens']:,}")
            
            st.markdown("---")
            st.markdown("**Query:**")
            st.info(item['query'])
            
            st.markdown("**Analysis:**")
            st.markdown(item['response'])
            
            # Export this item
            from utils import format_markdown_export, get_export_filename
            export_content = format_markdown_export(
                query=item['query'],
                response=item['response'],
                input_mode=item['input_mode'],
                language=item['language'],
                model=item['model'],
                timestamp=item['timestamp']
            )
            
            st.download_button(
                label="📥 Download This Analysis",
                data=export_content,
                file_name=get_export_filename(f"MediVision_{idx}"),
                mime="text/markdown",
                key=f"download_{idx}"
            )
