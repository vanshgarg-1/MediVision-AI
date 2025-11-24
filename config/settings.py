"""
Configuration settings for MediVision AI
"""

# App Configuration
APP_TITLE = "MediVision AI"
APP_ICON = "🩺"
APP_LAYOUT = "wide"
APP_TAGLINE = "Diagnose with Clarity, Treat with Confidence"

# Model Configuration - FREE TIER ONLY
AVAILABLE_MODELS = {
    "Gemini 2.5 Pro": {
        "name": "gemini-2.5-pro",
        "provider": "google",
        "max_tokens": 8192,
        "description": "🧠 Advanced thinking, complex reasoning"
    },
    "Gemini 2.5 Flash": {
        "name": "gemini-2.5-flash",
        "provider": "google",
        "max_tokens": 8192,
        "description": "⚡ Best balance of speed & quality"
    },
    "Gemini 2.5 Flash-Lite": {
        "name": "gemini-2.5-flash-lite",
        "provider": "google",
        "max_tokens": 8192,
        "description": "🚀 Ultra fast, most cost-efficient"
    },
    "Gemini 2.0 Flash": {
        "name": "gemini-2.0-flash",
        "provider": "google",
        "max_tokens": 8192,
        "description": "💪 Workhorse with 1M context"
    },
    "Gemini 2.0 Flash-Lite": {
        "name": "gemini-2.0-flash-lite",
        "provider": "google",
        "max_tokens": 8192,
        "description": "⚙️ Small & efficient, 1M context"
    }
}

DEFAULT_MODEL = "Gemini 2.5 Flash-Lite"

# Generation Configuration
GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 4096,
}

# Safety Settings - Relaxed for medical content
SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
]

# Supported Languages
SUPPORTED_LANGUAGES = [
    "English",
    "Hindi",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Japanese",
    "Chinese",
    "Arabic",
    "Russian",
    "Korean"
]

# Input Modes
INPUT_MODES = ["Text Only", "Image Only", "Text + Image"]

# Supported Image Formats
SUPPORTED_IMAGE_FORMATS = ['png', 'jpg', 'jpeg']

# Session Configuration
MAX_HISTORY_ITEMS = 10
SESSION_TOKEN_KEY = "total_tokens"
SESSION_COST_KEY = "total_cost"
SESSION_HISTORY_KEY = "conversation_history"
SESSION_FEEDBACK_KEY = "feedback_stats"

# Cost Configuration (per 1M tokens) - FREE TIER
TOKEN_COST = {
    "input": 0.00,  # Free tier - no cost
    "output": 0.00  # Free tier - no cost
}

# Export Configuration
EXPORT_FORMAT = "markdown"

# Theme Colors (Royal Black Glassy Gradient)
THEME_COLORS = {
    "primary": "#1a1a2e",
    "secondary": "#16213e",
    "accent": "#0f3460",
    "highlight": "#533483",
    "text_primary": "#ffffff",
    "text_secondary": "#b4b4b4",
    "success": "#2ecc71",
    "error": "#e74c3c",
    "warning": "#f39c12"
}
