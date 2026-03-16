from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedder import get_embedding


def calculate_match_score(resume_text, job_description):

    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    score = round(float(round(similarity * 100, 2)))

    return score


def find_missing_skills(resume_skills, job_skills):

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    missing = job_set - resume_set

    return list(missing)