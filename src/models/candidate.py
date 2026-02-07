from dataclasses import dataclass, field
from typing import List


@dataclass
class Candidate:
    name: str
    email: str
    skills: List[str] = field(default_factory=list)
    experience: int = 0   # Years
    education: str = ""

    def to_dict(self):
        """Convert candidate object to dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education
        }
