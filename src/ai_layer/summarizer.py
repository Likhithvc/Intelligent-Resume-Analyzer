from openai import OpenAI
client = OpenAI()

def summarize_resume(text):

    prompt = f"""
    Summarize this candidate resume in 5 bullet points:

    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
