def generate_skill_gap(candidate_skills, job_skills):
    """Find missing skills."""
    missing = []

    for skill in job_skills:
        if skill not in candidate_skills:
            missing.append(skill)

    return missing


def hiring_recommendation(score):
    """Generate hiring decision."""

    if score >= 80:
        return "Strong Hire"
    elif score >= 60:
        return "Consider"
    elif score >= 40:
        return "Weak Fit"
    else:
        return "Reject"


def generate_report(candidate, job, score):
    """Generate full text report."""

    missing_required = generate_skill_gap(
        candidate.skills,
        job.required_skills
    )

    missing_preferred = generate_skill_gap(
        candidate.skills,
        job.preferred_skills
    )

    recommendation = hiring_recommendation(score)

    report = f"""
================ CANDIDATE REPORT ================

Name: {candidate.name}
Email: {candidate.email}

Experience: {candidate.experience} years
Education: {candidate.education}

---------------- SKILLS ----------------

Candidate Skills:
{", ".join(candidate.skills)}

Matched Required Skills:
{", ".join(set(candidate.skills) & set(job.required_skills))}

Missing Required Skills:
{", ".join(missing_required) if missing_required else "None"}

Missing Preferred Skills:
{", ".join(missing_preferred) if missing_preferred else "None"}

---------------- MATCH RESULT ----------------

Overall Match Score: {score} %

Hiring Recommendation: {recommendation}

=================================================
"""

    return report
