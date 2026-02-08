from src.file_manager.file_handler import (
    get_all_resumes,
    read_text_file,
    save_report,
    save_match_scores
)

from src.file_manager.job_loader import load_job
from src.parser.resume_parser import parse_resume
from src.matcher.matcher import match_candidate
from src.reporter.report_generator import generate_report


RESUME_FOLDER = "data/resumes"
JOB_FILE = "data/job_descriptions/software_engineer.json"


def main():

    # 🔹 Load job data
    job = load_job(JOB_FILE)

    # 🔹 Convert structured job → raw text for AI semantic scoring
    jd_text = f"""
    Job Role: Software Engineer

    Required Skills: {", ".join(job.required_skills)}
    Preferred Skills: {", ".join(job.preferred_skills)}

    Education Requirement: {job.education}
    Minimum Experience Required: {job.min_experience} years
    """

    # 🔹 Load all resumes
    resumes = get_all_resumes(RESUME_FOLDER)

    results = []

    for resume_path in resumes:

        print(f"\nProcessing: {resume_path}")

        # 🔹 Read resume raw text
        resume_text = read_text_file(resume_path)

        # 🔹 Parse structured candidate data
        candidate = parse_resume(resume_text)

        # 🔹 AI + Rule-based matching
        score_data = match_candidate(
            candidate,
            job,
            resume_text,
            jd_text
        )

        # 🔹 Generate report
        report = generate_report(
    candidate,
    job,
    score_data["final_score"]
)


        print(report)

        # 🔹 Save individual report
        save_report(report, candidate.name)

        # 🔹 Store summary result
        results.append({
            "name": candidate.name,
            "email": candidate.email,
            "final_score": score_data["final_score"],
            "semantic_score": score_data["semantic_score"]
        })

    # 🔹 Save all candidate scores
    save_match_scores(results)


if __name__ == "__main__":
    main()

