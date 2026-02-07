def match_skills(candidate_skills, job_skills):
    """Return skill match percentage."""

    if not job_skills:
        return 0

    matched = 0

    for skill in job_skills:
        if skill in candidate_skills:
            matched += 1

    return matched / len(job_skills)


def match_candidate(candidate, job):
    """Calculate overall match score."""

    # Skill scores
    required_score = match_skills(
        candidate.skills,
        job.required_skills
    )

    preferred_score = match_skills(
        candidate.skills,
        job.preferred_skills
    )

    # Experience score
    exp_score = min(
        candidate.experience / job.min_experience,
        1
    )

    # Education score
    edu_score = 1 if job.education in candidate.education else 0

    # Weighted final score
    final_score = (
        required_score * 0.5 +
        preferred_score * 0.2 +
        exp_score * 0.2 +
        edu_score * 0.1
    )

    return round(final_score * 100, 2)
