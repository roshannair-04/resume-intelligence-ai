import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedder import get_embedding


skills_list = None
skill_embeddings = None


def load_skills(file_path="data/skills_list.csv"):

    global skills_list
    global skill_embeddings

    skills_df = pd.read_csv(file_path, header=None)

    skills_list = skills_df[0].str.lower().tolist()

    # Precompute embeddings once
    skill_embeddings = [get_embedding(skill) for skill in skills_list]

    return skills_list


def extract_skills(text, threshold=0.45):

    text_lower = text.lower()
    text_embedding = get_embedding(text)

    detected = []

    for skill, emb in zip(skills_list, skill_embeddings):

        # keyword match
        if skill in text_lower:
            detected.append(skill)
            continue

        # semantic match
        similarity = cosine_similarity(
            [text_embedding],
            [emb]
        )[0][0]

        if similarity > threshold:
            detected.append(skill)

    return list(set(detected))
