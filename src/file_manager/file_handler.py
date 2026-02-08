import os
import json
import pdfplumber


# =========================================================
# TEXT FILE READER
# =========================================================

def read_text_file(filepath: str) -> str:
    """Read resume text file."""

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        print(f"Error reading TXT {filepath}: {e}")
        return ""


# =========================================================
# PDF FILE READER (Improved Extraction)
# =========================================================

def read_pdf_file(filepath: str) -> str:
    """
    Extract text from PDF resume.
    Handles normal text + tables.
    """

    text = ""

    try:
        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:

                # 🔹 Extract standard text
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

                # 🔹 Extract tables (skills often inside)
                tables = page.extract_tables()

                for table in tables:
                    for row in table:
                        row_text = " ".join(
                            [cell for cell in row if cell]
                        )
                        text += row_text + "\n"

    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")

    return text


# =========================================================
# SMART RESUME READER (AUTO FORMAT DETECTION)
# =========================================================

def read_resume_file(filepath: str) -> str:
    """
    Reads TXT or PDF resume automatically.
    """

    if filepath.endswith(".txt"):
        return read_text_file(filepath)

    elif filepath.endswith(".pdf"):
        return read_pdf_file(filepath)

    else:
        print(f"Unsupported file format: {filepath}")
        return ""


# =========================================================
#  LOAD ALL RESUMES FROM FOLDER
# =========================================================

def get_all_resumes(folder_path: str):

    files = []

    for file in os.listdir(folder_path):

        if file.endswith(".txt") or file.endswith(".pdf"):
            files.append(os.path.join(folder_path, file))

    return files


# =========================================================
# SAVE INDIVIDUAL REPORT (NO OVERWRITE)
# =========================================================

def save_report(report: str, candidate_name: str):

    filename = f"{candidate_name}_report.txt"

    folder = "data/outputs/reports"
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, filename)

    # 🔹 Prevent overwrite
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(
            folder,
            f"{candidate_name}_report_{counter}.txt"
        )
        counter += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report saved: {filepath}")


# =========================================================
# SAVE MATCH SCORES JSON
# =========================================================

def save_match_scores(results: list):
    """Save all candidate scores to JSON."""

    folder = "data/outputs"
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, "match_scores.json")

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print(f"\nMatch scores saved: {filepath}")
