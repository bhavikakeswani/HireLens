
import os
from dotenv import load_dotenv
from google import genai
import json

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL")

# Validate API key
if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured")

# Create Gemini API client
client = genai.Client(api_key=api_key)

# Define generation configuration
generation_config = {
    'max_output_tokens': 2000,
    'thinking_level': 'medium',
}

# Define the exact JSON structure that Gemini must return
resume_analysis_schema = {
    "type": "object",
    "properties": {
        "match_summary": {
            "type": "string",
            "description": "A concise assessment of the student's profile against the job description"
        },
        "matching_skills": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Skills present in the resume that match the job requirements"
        },
        "missing_skills": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Skills required by the job but not demonstrated in the resume"
        },
        "resume_improvements": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Suggestions to improve the resume for the target job"
        },
        "interview_topics": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Topics the student should prepare for the interview"
        }
    },
    "required": [
        "match_summary",
        "matching_skills",
        "missing_skills",
        "resume_improvements",
        "interview_topics"
    ]
}

def analyze_resume_job(resume_text, job_description):

    prompt = f"""
    ROLE:
    You are HireLens, an AI-powered job-hunting assistant.

    OBJECTIVE:
    Analyze how well a student's resume matches a given job description.

    TASK:
    Compare the resume with the job requirements and identify:
    1. Overall match summary
    2. Matching skills
    3. Missing skills
    4. Resume improvement suggestions
    5. Interview preparation topics

    RULES:
    - Only use information supported by the resume.
    - Do not invent skills, qualifications, or experience.
    - Do not assume a student has a skill if it is not mentioned.
    - Keep suggestions practical and concise.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}
    """

    response = client.interactions.create(
        model=gemini_model,
        input=prompt,
        generation_config=generation_config,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": resume_analysis_schema
        }
    )

    return json.loads(response.output_text)
