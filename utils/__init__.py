"""
__init__.py for utils package
"""

from .theme import apply_custom_theme, create_gradient_header, create_glass_card
from .session_manager import (
    initialize_session_state,
    add_to_history,
    get_history,
    clear_history,
    update_token_stats,
    get_token_stats,
    add_feedback,
    get_feedback_stats,
    reset_session
)
from .token_counter import (
    estimate_tokens,
    calculate_cost,
    format_token_count,
    format_cost,
    get_token_stats_display
)
from .security import (
    encrypt_api_key,
    decrypt_api_key,
    validate_api_key,
    store_api_key,
    get_api_key,
    clear_api_key
)
from .model_handler import (
    initialize_model,
    generate_response,
    stream_response,
    validate_response,
    get_response_text,
    prepare_prompt,
    check_safety_block
)
from .export_handler import (
    format_markdown_export,
    get_export_filename,
    create_download_button_config
)
from .response_renderer import (
    render_response_with_syntax,
    format_medical_response,
    create_collapsible_section
)

__all__ = [
    # Theme
    'apply_custom_theme',
    'create_gradient_header',
    'create_glass_card',
    # Session Management
    'initialize_session_state',
    'add_to_history',
    'get_history',
    'clear_history',
    'update_token_stats',
    'get_token_stats',
    'add_feedback',
    'get_feedback_stats',
    'reset_session',
    # Token Counter
    'estimate_tokens',
    'calculate_cost',
    'format_token_count',
    'format_cost',
    'get_token_stats_display',
    # Security
    'encrypt_api_key',
    'decrypt_api_key',
    'validate_api_key',
    'store_api_key',
    'get_api_key',
    'clear_api_key',
    # Model Handler
    'initialize_model',
    'generate_response',
    'stream_response',
    'validate_response',
    'get_response_text',
    'prepare_prompt',
    'check_safety_block',
    # Export
    'format_markdown_export',
    'get_export_filename',
    'create_download_button_config',
    # Response Renderer
    'render_response_with_syntax',
    'format_medical_response',
    'create_collapsible_section'
]
