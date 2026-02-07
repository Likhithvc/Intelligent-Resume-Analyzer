import os
import json


def read_text_file(filepath: str) -> str:
    """Read resume text file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def get_all_resumes(folder_path: str):
    """Return all .txt resumes."""
    files = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            files.append(os.path.join(folder_path, file))

    return files

def save_report(report_text: str, candidate_name: str):
    """Save report as text file."""

    filename = candidate_name.replace(" ", "_") + "_report.txt"
    filepath = f"data/outputs/reports/{filename}"

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(report_text)

    print(f"Report saved: {filepath}")



def save_match_scores(results: list):
    """Save all candidate scores to JSON."""

    filepath = "data/outputs/match_scores.json"

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print(f"\nMatch scores saved: {filepath}")

