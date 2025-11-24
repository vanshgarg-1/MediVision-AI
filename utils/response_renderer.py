"""
Response rendering utilities with syntax highlighting
"""

import streamlit as st
import re


def render_response_with_syntax(response_text: str):
    """Render response with proper formatting and syntax highlighting"""
    
    # Split response into sections
    sections = split_response_sections(response_text)
    
    for section in sections:
        if section["type"] == "code":
            # Render code block with syntax highlighting
            language = section.get("language", "python")
            st.code(section["content"], language=language)
        elif section["type"] == "text":
            # Render regular text with markdown
            st.markdown(section["content"])


def split_response_sections(text: str) -> list:
    """Split response into code and text sections"""
    sections = []
    
    # Pattern to match code blocks with optional language
    code_pattern = r"```(\w+)?\n(.*?)```"
    
    last_end = 0
    for match in re.finditer(code_pattern, text, re.DOTALL):
        # Add text before code block
        if match.start() > last_end:
            text_content = text[last_end:match.start()].strip()
            if text_content:
                sections.append({
                    "type": "text",
                    "content": text_content
                })
        
        # Add code block
        language = match.group(1) if match.group(1) else "python"
        code_content = match.group(2).strip()
        sections.append({
            "type": "code",
            "language": language,
            "content": code_content
        })
        
        last_end = match.end()
    
    # Add remaining text
    if last_end < len(text):
        remaining_text = text[last_end:].strip()
        if remaining_text:
            sections.append({
                "type": "text",
                "content": remaining_text
            })
    
    # If no sections were found, treat entire text as text section
    if not sections:
        sections.append({
            "type": "text",
            "content": text
        })
    
    return sections


def format_medical_response(response: str) -> str:
    """Format response with medical-specific styling"""
    
    # Add icons to common medical sections
    response = response.replace("**Observational Analysis:**", "🔍 **Observational Analysis:**")
    response = response.replace("**General Insights:**", "💡 **General Insights:**")
    response = response.replace("**Recommendations:**", "📋 **Recommendations:**")
    response = response.replace("**Cautionary Notes:**", "⚠️ **Cautionary Notes:**")
    response = response.replace("**Disclaimer:**", "⚕️ **Disclaimer:**")
    
    # Highlight important warnings
    response = response.replace("consult a medical professional", "**consult a medical professional**")
    response = response.replace("seek immediate medical attention", "**⚠️ SEEK IMMEDIATE MEDICAL ATTENTION**")
    
    return response


def create_collapsible_section(title: str, content: str, expanded: bool = False):
    """Create a collapsible section"""
    with st.expander(title, expanded=expanded):
        st.markdown(content)
