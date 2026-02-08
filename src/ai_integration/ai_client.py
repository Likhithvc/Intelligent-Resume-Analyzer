from transformers import pipeline

summarizer = pipeline(
    "text-generation",
    model="tiiuae/falcon-rw-1b",
    device=-1  # CPU
)


def summarize_resume(resume_text: str):

    if not resume_text.strip():
        return "Resume content unavailable."

    text = resume_text[:1200]

    prompt = f"""
You are an HR assistant.

Summarize the following resume for hiring evaluation.
Focus on skills, experience, and strengths.

Resume:
{text}

Summary:
"""

    result = summarizer(
        prompt,
        max_new_tokens=120,
        do_sample=False
    )

    generated = result[0]["generated_text"]

    summary = generated.split("Summary:")[-1].strip()

    return summary
