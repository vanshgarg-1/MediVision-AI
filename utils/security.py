"""
Security utilities for API key encryption and validation
"""

import streamlit as st
from cryptography.fernet import Fernet
import base64
import hashlib


def generate_key_from_session() -> bytes:
    """Generate encryption key from session"""
    # Use a deterministic key based on session
    # In production, use a proper key management system
    session_id = st.runtime.scriptrunner.get_script_run_ctx().session_id
    key = hashlib.sha256(session_id.encode()).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_api_key(api_key: str) -> str:
    """Encrypt API key for session storage"""
    try:
        key = generate_key_from_session()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(api_key.encode())
        return encrypted.decode()
    except Exception as e:
        st.error(f"Encryption error: {e}")
        return None


def decrypt_api_key(encrypted_key: str) -> str:
    """Decrypt API key from session storage"""
    try:
        key = generate_key_from_session()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_key.encode())
        return decrypted.decode()
    except Exception as e:
        st.error(f"Decryption error: {e}")
        return None


def validate_api_key(api_key: str) -> bool:
    """Validate Google API key format"""
    if not api_key:
        return False
    
    # Basic validation - Google API keys typically start with "AIza" and are 39 characters
    if api_key.startswith("AIza") and len(api_key) == 39:
        return True
    
    # Allow other formats but warn user
    return len(api_key) > 20


def store_api_key(api_key: str):
    """Securely store API key in session"""
    if validate_api_key(api_key):
        encrypted = encrypt_api_key(api_key)
        if encrypted:
            st.session_state.api_key_encrypted = encrypted
            return True
    return False


def get_api_key() -> str:
    """Retrieve and decrypt API key from session"""
    if "api_key_encrypted" in st.session_state:
        return decrypt_api_key(st.session_state.api_key_encrypted)
    return None


def clear_api_key():
    """Clear stored API key"""
    if "api_key_encrypted" in st.session_state:
        del st.session_state.api_key_encrypted
