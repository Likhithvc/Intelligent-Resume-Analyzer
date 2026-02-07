import re
from src.models.candidate import Candidate


# Predefined skills database
SKILL_DB = [
    "Python", "Java", "C++", "SQL",
    "Machine Learning", "AI",
    "React", "Node.js",
    "HTML", "CSS", "JavaScript"
]


def extract_name(text: str) -> str:
    """Assume first line is candidate name."""
    lines = text.strip().split("\n")
    return lines[0] if lines else "Unknown"


def extract_email(text: str) -> str:
    """Extract email using regex."""
    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )
    return match.group(0) if match else "Not Found"


def extract_skills(text: str):
    """Find matching skills from database."""
    found_skills = []

    for skill in SKILL_DB:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def extract_experience(text: str) -> int:
    """Extract years of experience."""
    match = re.search(r"(\d+)\+?\s+years?", text.lower())
    return int(match.group(1)) if match else 0


def extract_education(text: str) -> str:
    """Simple education extraction."""
    degrees = ["B.Tech", "B.E", "M.Tech", "MBA", "BSc", "MSc"]

    for degree in degrees:
        if degree.lower() in text.lower():
            return degree

    return "Not Found"


def parse_resume(text: str) -> Candidate:
    """Main parser function."""

    name = extract_name(text)
    email = extract_email(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    education = extract_education(text)

    return Candidate(
        name=name,
        email=email,
        skills=skills,
        experience=experience,
        education=education
    )
