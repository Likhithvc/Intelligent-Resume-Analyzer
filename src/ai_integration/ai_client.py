from transformers import pipeline

summarizer = pipeline(
    "text-generation",
    model="google/flan-t5-small"
)


def summarize_resume(resume_text: str):

    if not resume_text.strip():
        return "Resume content unavailable."

    text = resume_text[:1500]

    prompt = f"""
    Provide a professional hiring summary for this candidate:

    {text}

    Summary:
    """

    result = summarizer(
        prompt,
        max_new_tokens=120,
        do_sample=False
    )

    generated = result[0]["generated_text"]

    # Remove prompt part
    summary = generated.split("Summary:")[-1].strip()

    return summary
