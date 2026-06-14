import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

class Experience(BaseModel):
    company: str
    role: str
    duration: str
    bullets: List[str]

class Education(BaseModel):
    institution: str
    degree: str
    year: str
    gpa_or_details: Optional[str] = None

class Project(BaseModel):
    title: str
    technologies: List[str]
    description: str

class ResumeSchema(BaseModel):
    name: str
    email: str
    linkedin: Optional[str] = "N/A"
    skills: List[str]
    experience: List[Experience]
    education: List[Education]
    projects: List[Project]

def generate_tailored_resume(raw_input: str, job_description: str) -> ResumeSchema:
    prompt = f"Map the user profile to the JSON schema and optimize bullet points to match the target job.\n\nPROFILE:\n{raw_input}\n\nJOB:\n{job_description}"
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ResumeSchema,
            temperature=0.2
        ),
    )
    return ResumeSchema.model_validate_json(response.text)
