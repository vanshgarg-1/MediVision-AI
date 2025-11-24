"""
Session and state management utilities
"""

import streamlit as st
from datetime import datetime
from typing import Dict, List, Any
from config.settings import MAX_HISTORY_ITEMS, SESSION_HISTORY_KEY, SESSION_TOKEN_KEY, SESSION_COST_KEY, SESSION_FEEDBACK_KEY


def initialize_session_state():
    """Initialize all session state variables"""
    if SESSION_HISTORY_KEY not in st.session_state:
        st.session_state[SESSION_HISTORY_KEY] = []
    
    if SESSION_TOKEN_KEY not in st.session_state:
        st.session_state[SESSION_TOKEN_KEY] = 0
    
    if SESSION_COST_KEY not in st.session_state:
        st.session_state[SESSION_COST_KEY] = 0.0
    
    if SESSION_FEEDBACK_KEY not in st.session_state:
        st.session_state[SESSION_FEEDBACK_KEY] = {"positive": 0, "negative": 0}
    
    if "current_response" not in st.session_state:
        st.session_state.current_response = None
    
    if "regenerate_count" not in st.session_state:
        st.session_state.regenerate_count = 0


def add_to_history(query: str, response: str, input_mode: str, language: str, model: str, tokens: int):
    """Add a conversation to history with a meaningful title"""
    if SESSION_HISTORY_KEY not in st.session_state:
        st.session_state[SESSION_HISTORY_KEY] = []

    chat_name = generate_chat_title(query=query, input_mode=input_mode, language=language)

    history_item = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "chat_name": chat_name,
        "query": query,
        "response": response,
        "input_mode": input_mode,
        "language": language,
        "model": model,
        "tokens": tokens
    }

    st.session_state[SESSION_HISTORY_KEY].insert(0, history_item)
    if len(st.session_state[SESSION_HISTORY_KEY]) > MAX_HISTORY_ITEMS:
        st.session_state[SESSION_HISTORY_KEY] = st.session_state[SESSION_HISTORY_KEY][:MAX_HISTORY_ITEMS]


def generate_chat_title(query: str, input_mode: str, language: str, max_length: int = 60) -> str:
    """Generate a richer, user-friendly chat title.

    Logic:
    - Image only: return 'Image Analysis' with language.
    - If medical keywords found: combine up to two and append 'Assessment'.
    - Else: Use first 8 words of the query as summary.
    - Always truncate gracefully and title-case first word.
    """
    # Image-only case with no text
    if (not query or query.strip() == "") and ("Image" in input_mode):
        return f"Image Analysis ({language[:2].upper()})"

    if not query:
        return f"Medical Analysis ({language[:2].upper()})"

    medical_keywords = [
        "chest", "x-ray", "cough", "fever", "pain", "headache", "rash",
        "swelling", "fracture", "injury", "scan", "mri", "ct", "ultrasound",
        "heart", "lung", "brain", "knee", "shoulder", "back", "abdomen",
        "diabetes", "infection", "wound", "tumor", "lesion", "fracture"
    ]

    q_lower = query.lower()
    found = []
    for kw in medical_keywords:
        if kw in q_lower and kw not in found:
            found.append(kw)
        if len(found) == 2:
            break

    if found:
        title = " & ".join([w.title() for w in found]) + " Assessment"
    else:
        words = query.strip().split()
        snippet = " ".join(words[:8])
        if len(words) > 8:
            snippet += "..."
        title = snippet[:max_length]

    # Append language code for clarity
    return f"{title} ({language[:2].upper()})"


def get_history() -> List[Dict[str, Any]]:
    """Get conversation history"""
    if SESSION_HISTORY_KEY not in st.session_state:
        return []
    return st.session_state[SESSION_HISTORY_KEY]


def clear_history():
    """Clear conversation history"""
    st.session_state[SESSION_HISTORY_KEY] = []


def update_token_stats(tokens: int, cost: float):
    """Update token and cost statistics"""
    if SESSION_TOKEN_KEY not in st.session_state:
        st.session_state[SESSION_TOKEN_KEY] = 0
    if SESSION_COST_KEY not in st.session_state:
        st.session_state[SESSION_COST_KEY] = 0.0
    
    st.session_state[SESSION_TOKEN_KEY] += tokens
    st.session_state[SESSION_COST_KEY] += cost


def get_token_stats() -> Dict[str, Any]:
    """Get current token statistics"""
    return {
        "total_tokens": st.session_state.get(SESSION_TOKEN_KEY, 0),
        "total_cost": st.session_state.get(SESSION_COST_KEY, 0.0)
    }


def add_feedback(is_positive: bool):
    """Record user feedback"""
    if SESSION_FEEDBACK_KEY not in st.session_state:
        st.session_state[SESSION_FEEDBACK_KEY] = {"positive": 0, "negative": 0}
    
    if is_positive:
        st.session_state[SESSION_FEEDBACK_KEY]["positive"] += 1
    else:
        st.session_state[SESSION_FEEDBACK_KEY]["negative"] += 1


def get_feedback_stats() -> Dict[str, int]:
    """Get feedback statistics"""
    if SESSION_FEEDBACK_KEY not in st.session_state:
        return {"positive": 0, "negative": 0}
    return st.session_state[SESSION_FEEDBACK_KEY]


def reset_session():
    """Reset all session data"""
    keys_to_keep = ["api_key_encrypted"]  # Keep encrypted API key
    for key in list(st.session_state.keys()):
        if key not in keys_to_keep:
            del st.session_state[key]
    initialize_session_state()
