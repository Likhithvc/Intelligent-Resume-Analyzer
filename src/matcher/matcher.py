from src.ai_layer.scorer import semantic_match_score


def match_skills(candidate_skills, job_skills):
    """Return skill match percentage."""

    if not job_skills:
        return 0

    matched = 0

    for skill in job_skills:
        if skill in candidate_skills:
            matched += 1

    return matched / len(job_skills)


def match_candidate(candidate, job, resume_text, jd_text):
    """Calculate overall match score with AI layer."""

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

    # 🔹 NEW — AI Semantic Score
    semantic_score = semantic_match_score(
        resume_text,
        jd_text
    )

    # 🔹 Updated weighted final score
    final_score = (
        required_score * 0.4 +
        preferred_score * 0.15 +
        exp_score * 0.15 +
        edu_score * 0.1 +
        semantic_score * 0.2
    )

    return {
        "required_skill_score": required_score,
        "preferred_skill_score": preferred_score,
        "experience_score": exp_score,
        "education_score": edu_score,
        "semantic_score": semantic_score,
        "final_score": round(final_score * 100, 2)
    }
