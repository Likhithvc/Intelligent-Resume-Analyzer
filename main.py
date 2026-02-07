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

    job = load_job(JOB_FILE)
    resumes = get_all_resumes(RESUME_FOLDER)

    results = []

    for resume_path in resumes:

        print(f"\nProcessing: {resume_path}")

        text = read_text_file(resume_path)
        candidate = parse_resume(text)

        score = match_candidate(candidate, job)
        report = generate_report(candidate, job, score)

        print(report)

        # Save individual report
        save_report(report, candidate.name)

        # Store result summary
        results.append({
            "name": candidate.name,
            "email": candidate.email,
            "score": score
        })

    # Save all scores
    save_match_scores(results)


if __name__ == "__main__":
    main()
