from sklearn.metrics.pairwise import cosine_similarity
from .embeddings import get_embedding

def semantic_match_score(resume_text, jd_text):
    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(jd_text)

    score = cosine_similarity([emb1], [emb2])[0][0]
    return float(score)
