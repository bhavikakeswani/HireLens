# HireLens

HireLens is an AI-powered job-hunting assistant that helps students analyze job descriptions, compare their resumes with job requirements, identify skill gaps, and prepare for specific job roles using Google's Gemini API.

## Features

- Job Description Analysis
- Resume vs Job Description Analysis
- Skill Gap Analysis
- Resume Improvement Suggestions
- Interview Preparation

## Technologies Used

- Python
- Google Gemini API
- Streamlit
- JSON
- python-dotenv

## Project Structure

```text
HireLens/
│
├── app.py
├── streamlit_ui.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── notes.txt
```

## Setup and Installation
**1. Clone the repository**

```bash
git clone https://github.com/bhavikakeswani/HireLens.git
cd HireLens
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a .env file in the project directory:

```bash
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=your_model_name
```

**5. Run the Application**

```bash
streamlit run streamlit_ui.py
```
