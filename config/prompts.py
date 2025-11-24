"""
System prompts and prompt templates for MediVision AI
"""

def get_system_prompt(language: str = "English") -> str:
    """Generate system prompt based on selected language"""
    return f"""
    You are an AI assistant providing educational insights into medical imaging and health symptoms. 
    Your responses should focus on general observations, avoid making definitive diagnoses, 
    and always advise consulting a medical professional.
    
    Your key responsibilities:
    1. Observational Analysis: Describe general patterns and visible abnormalities in the image.
    2. General Insights: Offer possible medical explanations while avoiding absolute conclusions.
    3. Consider Additional Information: Use the provided text (symptoms, history) to enhance analysis.
    4. Recommendations: Suggest next steps such as further tests or consulting a specialist.
    5. Cautionary Notes: Highlight when additional medical evaluation is necessary.
    
    Provide the response in {language}.
    
    Make Sure everything point is covered and Keep Everything Clear and in Detailed way. Don't Show or Say you are an AI Bot, Show Like You are a professional Doctor.
    Disclaimer: This is an AI-generated analysis for informational purposes only. Always consult a licensed medical professional.
    """

# Prompt Style Templates
PROMPT_STYLES = {
    "Professional & Detailed": {
        "suffix": "\n\nProvide a comprehensive, professional medical analysis with detailed explanations.",
        "description": "In-depth analysis with medical terminology"
    },
    "Simple & Clear": {
        "suffix": "\n\nProvide a simple, easy-to-understand explanation suitable for patients without medical background.",
        "description": "Patient-friendly language"
    },
    "Step-by-Step": {
        "suffix": "\n\nBreak down the analysis into clear, numbered steps with actionable recommendations.",
        "description": "Structured step-by-step format"
    },
    "Comparative Analysis": {
        "suffix": "\n\nCompare the findings with normal/healthy conditions and highlight the differences.",
        "description": "Comparison with normal cases"
    },
    "Educational Focus": {
        "suffix": "\n\nProvide educational insights about the condition, including possible causes, risk factors, and prevention.",
        "description": "Focus on learning and prevention"
    }
}

# Regeneration Tweaks
REGENERATION_OPTIONS = {
    "More Detailed": {
        "instruction": "Provide more comprehensive details and elaborate on each point.",
        "emoji": "📝"
    },
    "Simpler Language": {
        "instruction": "Use simpler, non-technical language that's easier to understand.",
        "emoji": "💡"
    },
    "Focus on Recommendations": {
        "instruction": "Emphasize actionable recommendations and next steps.",
        "emoji": "🎯"
    },
    "Add Risk Factors": {
        "instruction": "Include detailed information about risk factors and prevention strategies.",
        "emoji": "⚠️"
    },
    "Compare with Normal": {
        "instruction": "Compare the findings with normal/healthy conditions more explicitly.",
        "emoji": "🔄"
    }
}

# Example Query Templates
EXAMPLE_TEMPLATES = {
    "Chest X-Ray Analysis": {
        "text": "Patient presenting with persistent cough for 3 weeks, mild fever, and shortness of breath. No known allergies. Non-smoker.",
        "category": "Respiratory",
        "icon": "🫁"
    },
    "Skin Condition": {
        "text": "Red, itchy rash on forearm for 5 days. No recent travel or new medications. Worsens at night.",
        "category": "Dermatology",
        "icon": "🔬"
    },
    "Joint Pain Assessment": {
        "text": "Swelling and pain in right knee for 2 weeks. Difficulty walking. History of sports injury 5 years ago.",
        "category": "Orthopedics",
        "icon": "🦴"
    },
    "Neurological Symptoms": {
        "text": "Intermittent headaches for 1 month, accompanied by dizziness. No vision problems. Family history of migraines.",
        "category": "Neurology",
        "icon": "🧠"
    },
    "Abdominal Discomfort": {
        "text": "Upper abdominal pain after meals for 2 weeks. Occasional nausea. No vomiting or fever.",
        "category": "Gastroenterology",
        "icon": "🏥"
    }
}
