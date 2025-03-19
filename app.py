import streamlit as st
import google.generativeai as genai

# Streamlit App
st.set_page_config(page_title="MediVision AI", page_icon="🩺", layout="wide")
st.title("MediVsion AI 👨‍⚕️ 🩺 🏥")
st.subheader("Diagnose with Clarity, Treat with Confidence.")
st.divider()

# Sidebar for user selection
st.sidebar.header("Choose Input Mode")
option = st.sidebar.radio("Select input type:", ["Text Only", "Image Only", "Text + Image"])

# Sidebar for language selection
st.sidebar.header("Choose Output Language")
language = st.sidebar.radio("Select language:", ["English", "Hindi"])
api_key = st.text_input("Enter your Google API Key:", type="password")

user_text = ""
file_uploaded = None

if option == "Text Only" or option == "Text + Image":
    user_text = st.sidebar.text_area("Enter symptoms, history, or medical reports:")

if option == "Image Only" or option == "Text + Image":
    file_uploaded = st.file_uploader('Upload the image for analysis', type=['png', 'jpg', 'jpeg'])
    if file_uploaded:
        st.image(file_uploaded, width=200, caption='Uploaded Image')

# Prompt user to enter API key

if api_key:
    # Configure the API with user input
    genai.configure(api_key=api_key)

    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},  # Adjusted threshold
    ]

    system_prompt = f"""
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
    
    Make Sure everything point is covered and Keep Everything Clear and in Detailed way. Don't Show or Say you are an AI Bot , Show Like You are an professional Doctor.
    Disclaimer: This is an AI-generated analysis for informational purposes only. Always consult a licensed medical professional.
    """

    model = genai.GenerativeModel(model_name="gemini-2.0-flash",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    submit = st.button("Generate Analysis")

    if submit and (file_uploaded or user_text):
        prompt_parts = []
        if file_uploaded:
            image_data = file_uploaded.getvalue()
            image_parts = [{"mime_type": "image/jpg", "data": image_data}]
            prompt_parts.append(image_parts[0])
        if user_text:
            prompt_parts.append(user_text)
        prompt_parts.append(system_prompt)

        # Generate response with error handling
        try:
            response = model.generate_content(prompt_parts)

            if response and response.candidates and response.candidates[0].finish_reason != 3:
                st.title(f'Detailed Analysis Based on Selected Input ({language})')
                st.write(response.text)
            else:
                st.error("The response was blocked due to safety filters. Please try modifying the input.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter your Google API key to proceed.")
