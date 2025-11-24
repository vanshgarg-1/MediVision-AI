"""
Token counting and cost estimation utilities
"""

from typing import Dict
from config.settings import TOKEN_COST


def estimate_tokens(text: str) -> int:
    """
    Estimate token count for text
    Rough estimation: ~4 characters per token
    """
    return len(text) // 4


def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Calculate cost based on token usage
    Returns cost in USD
    """
    input_cost = (input_tokens / 1000) * TOKEN_COST["input"]
    output_cost = (output_tokens / 1000) * TOKEN_COST["output"]
    return input_cost + output_cost


def format_token_count(tokens: int) -> str:
    """Format token count with K/M suffix"""
    if tokens >= 1_000_000:
        return f"{tokens / 1_000_000:.2f}M"
    elif tokens >= 1_000:
        return f"{tokens / 1_000:.1f}K"
    else:
        return str(tokens)


def format_cost(cost: float) -> str:
    """Format cost in USD"""
    if cost < 0.01:
        return f"${cost:.4f}"
    else:
        return f"${cost:.2f}"


def get_token_stats_display(total_tokens: int, total_cost: float) -> Dict[str, str]:
    """Get formatted token statistics for display"""
    return {
        "tokens": format_token_count(total_tokens),
        "cost": format_cost(total_cost)
    }
