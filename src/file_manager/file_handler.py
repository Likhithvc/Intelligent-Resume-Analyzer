import os
import json
import pdfplumber


def read_text_file(filepath: str) -> str:
    """Read resume text file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def get_all_resumes(folder_path: str):

    files = []

    for file in os.listdir(folder_path):

        if file.endswith(".txt") or file.endswith(".pdf"):
            files.append(os.path.join(folder_path, file))

    return files


def save_report(report, candidate_name):

    filename = f"{candidate_name}_report.txt"

    filepath = os.path.join(
        "data/outputs/reports",
        filename
    )

    # Prevent overwrite
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(
            "data/outputs/reports",
            f"{candidate_name}_report_{counter}.txt"
        )
        counter += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report saved: {filepath}")




def save_match_scores(results: list):
    """Save all candidate scores to JSON."""

    filepath = "data/outputs/match_scores.json"

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print(f"\nMatch scores saved: {filepath}")


def read_pdf_file(filepath: str) -> str:
    """Extract text from PDF resume."""

    text = ""

    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")

    return text


