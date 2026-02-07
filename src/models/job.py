from dataclasses import dataclass
from typing import List


@dataclass
class Job:
    title: str
    required_skills: List[str]
    preferred_skills: List[str]
    min_experience: int
    education: str
