from src.ai_layer.scorer import semantic_match_score
from fuzzywuzzy import fuzz


def fuzzy_skill_match(candidate_skill, required_skill, threshold=85):
    """Check similarity between skills."""

    ratio = fuzz.ratio(
        candidate_skill.lower(),
        required_skill.lower()
    )

    return ratio >= threshold


def match_skills(candidate_skills, job_skills):
    """Fuzzy skill match percentage."""

    if not job_skills:
        return 0

    matched = 0

    for req_skill in job_skills:
        for cand_skill in candidate_skills:
            if fuzzy_skill_match(cand_skill, req_skill):
                matched += 1
                break

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

    # 🔹 Rule-based score (WITHOUT semantic)
    rule_score = (
        required_score * 0.5 +
        preferred_score * 0.2 +
        exp_score * 0.2 +
        edu_score * 0.1
    )

    # 🔹 AI Semantic Score
    semantic_score = semantic_match_score(
        resume_text,
        jd_text
    )

    # 🔹 Final Hybrid Score
    final_score = (
        rule_score * 0.8 +
        semantic_score * 0.2
    )

    return {
        "required_skill_score": required_score,
        "preferred_skill_score": preferred_score,
        "experience_score": exp_score,
        "education_score": edu_score,

        #IMPORTANT — Added for strategy layer
        "rule_score": rule_score * 100,
        "semantic_score": semantic_score * 100,

        "final_score": round(final_score * 100, 2)
    }
