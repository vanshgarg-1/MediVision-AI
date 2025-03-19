
# MediVision AI : Diagnose with Clarity, Treat with Confidence.

- [Live Link](https://medivision-ai.streamlit.app/)  & [Blog Link](https://vanshgarg.framer.website/works/medivision-ai)

# Problem Statement

Access to accurate and timely medical analysis remains a critical challenge in healthcare. Patients often face delays in preliminary diagnoses due to limited access to specialists, while healthcare providers struggle with high caseloads and resource constraints. Traditional symptom analysis and image interpretation rely heavily on manual expertise, leading to potential inconsistencies and bottlenecks. MediVision AI addresses these challenges by bridging the gap between technology and medical expertise, enabling faster, more accessible preliminary evaluations.

# Solution

MediVision AI is an advanced diagnostic assistant that combines generative AI with medical imaging analysis to deliver actionable insights. Built on Google’s Gemini AI and Streamlit, the platform offers:

- Multimodal Input: Analyze text-based symptoms, medical images (X-rays, scans), or both for comprehensive insights.

- Multilingual Support: Generate reports in English or Hindi to cater to diverse populations.

- Safety-Centric Design: Integrated content filters ensure medically appropriate responses.

- Ethical Guidance: Emphasizes consultation with licensed professionals and avoids definitive diagnoses.

The tool provides observational analysis, potential explanations, and recommended next steps—all while maintaining a patient-centric, cautious approach.

# Impact

- Enhanced Accessibility: Democratizes preliminary medical insights for underserved regions.

- Workflow Efficiency: Reduces burden on healthcare providers by prioritizing urgent cases.

- Patient Empowerment: Enables individuals to make informed decisions about seeking care.

- Standardized Analysis: Minimizes variability in initial symptom/image evaluations.
# Usage Guide
1. Select Input Mode (Text/Image/Combined) via the sidebar.

2. Upload Data:

- Describe symptoms in text format.

- Upload medical images (JPEG/PNG).

3. Choose Output Language: English or Hindi.

4. Click Generate Analysis to receive:

- Observational findings

- Potential medical correlations

- Recommended next steps

- Safety disclaimers
# Installation Guide
## Prerequisites

- Python 3.9 or higher

- Google API Key ( Obtain from Google AI Studio)

## Steps To Run Locally

1. Clone the Repository:

```bash
   git clone https://github.com/your-repo/medivision-ai.git  
   cd medivision-ai    
```
2. Create a Virtual Environment (recommended for dependency isolation):
```bash
   python -m venv venv  
   source venv/bin/activate  # For Windows: venv\Scripts\activate  
```
3. Install Dependencies:
```bash
   pip install -r requirements.txt  
```
4.  Launch the Application:

```bash
   streamlit run app.py  
```

```
5. Access the Interface:

- Open http://localhost:8501 in your browser.

- Enter your Google API key in the designated field.

- Note: Replace your-repo in the clone command with your repository URL.


## Key Considerations
- Not a Replacement for Professionals: Always consult licensed healthcare providers for final diagnoses.

- Data Privacy: No patient data is stored or transmitted beyond Google’s secure API.

- API Key Requirement: Users must provide their own Google API key for Gemini integration.

## Empower Your Healthcare Journey with Clarity and Confidence
MediVision AI: Where Technology Meets Compassionate Care 

## Authors

- [@Vansh Garg](https://github.com/vanshgarg-1)

