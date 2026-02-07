import json
from src.models.job import Job


def load_job(filepath: str) -> Job:
    """Load job description from JSON."""

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Job(
        title=data["title"],
        required_skills=data["required_skills"],
        preferred_skills=data["preferred_skills"],
        min_experience=data["min_experience"],
        education=data["education"]
    )
