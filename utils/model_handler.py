"""
AI model handler and streaming utilities
"""

import streamlit as st
import google.generativeai as genai
from typing import Generator, Optional
from config.settings import AVAILABLE_MODELS, GENERATION_CONFIG, SAFETY_SETTINGS


def initialize_model(api_key: str, model_name: str):
    """Initialize Google Generative AI model"""
    try:
        genai.configure(api_key=api_key)
        
        model_config = AVAILABLE_MODELS.get(model_name)
        if not model_config:
            st.error(f"Model {model_name} not found")
            return None
        
        model = genai.GenerativeModel(
            model_name=model_config["name"],
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS
        )
        
        return model
    except Exception as e:
        st.error(f"Model initialization error: {e}")
        return None


def generate_response(model, prompt_parts: list, stream: bool = True):
    """Generate response from model"""
    try:
        if stream:
            response = model.generate_content(prompt_parts, stream=True)
            return response
        else:
            response = model.generate_content(prompt_parts)
            return response
    except Exception as e:
        st.error(f"Generation error: {e}")
        return None


def stream_response(response_stream) -> Generator[str, None, None]:
    """Stream response text"""
    try:
        for chunk in response_stream:
            # Check if chunk has valid parts
            if hasattr(chunk, 'parts') and chunk.parts:
                # Extract text from parts
                for part in chunk.parts:
                    if hasattr(part, 'text') and part.text:
                        yield part.text
            elif hasattr(chunk, 'text') and chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"\n\n⚠️ Error during streaming: {e}"


def validate_response(response) -> bool:
    """Validate model response"""
    try:
        if not response:
            return False
        
        if not hasattr(response, 'candidates'):
            return False
        
        if not response.candidates:
            return False
        
        # Check if blocked by safety filters
        if response.candidates[0].finish_reason == 3:
            return False
        
        return True
    except Exception:
        return False


def get_response_text(response) -> Optional[str]:
    """Extract text from response"""
    try:
        if validate_response(response):
            return response.text
        return None
    except Exception as e:
        st.error(f"Error extracting response text: {e}")
        return None


def prepare_prompt(
    system_prompt: str,
    user_text: str = None,
    image_data: bytes = None,
    prompt_style: str = None,
    regenerate_instruction: str = None
) -> list:
    """Prepare prompt parts for model"""
    prompt_parts = []
    
    # Add image if provided
    if image_data:
        image_parts = [{"mime_type": "image/jpeg", "data": image_data}]
        prompt_parts.append(image_parts[0])
    
    # Add user text if provided
    if user_text:
        prompt_parts.append(user_text)
    
    # Add style or regeneration instruction
    if regenerate_instruction:
        prompt_parts.append(f"\n\n{regenerate_instruction}")
    elif prompt_style:
        prompt_parts.append(prompt_style)
    
    # Add system prompt
    prompt_parts.append(system_prompt)
    
    return prompt_parts


def check_safety_block(response) -> bool:
    """Check if response was blocked by safety filters"""
    try:
        if response and response.candidates:
            return response.candidates[0].finish_reason == 3
        return False
    except Exception:
        return False
