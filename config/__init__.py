"""
__init__.py for config package
"""

from .settings import *
from .prompts import *

__all__ = [
    'APP_TITLE',
    'APP_ICON',
    'APP_LAYOUT',
    'APP_TAGLINE',
    'AVAILABLE_MODELS',
    'DEFAULT_MODEL',
    'GENERATION_CONFIG',
    'SAFETY_SETTINGS',
    'SUPPORTED_LANGUAGES',
    'INPUT_MODES',
    'SUPPORTED_IMAGE_FORMATS',
    'MAX_HISTORY_ITEMS',
    'TOKEN_COST',
    'THEME_COLORS',
    'get_system_prompt',
    'PROMPT_STYLES',
    'REGENERATION_OPTIONS',
    'EXAMPLE_TEMPLATES'
]
