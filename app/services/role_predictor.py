import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedder import get_embedding


roles = None
role_embeddings = None


def load_roles():

    global roles
    global role_embeddings

    with open("data/job_roles.json") as f:
        roles = json.load(f)

    role_embeddings = [get_embedding(role) for role in roles]


def predict_roles(text, top_k=5):

    text_embedding = get_embedding(text)

    scores = []

    for role, emb in zip(roles, role_embeddings):

        sim = cosine_similarity(
            [text_embedding],
            [emb]
        )[0][0]

        scores.append((role, sim))

    scores.sort(key=lambda x: x[1], reverse=True)

    return [
        {"role": role, "score": float(score)}
        for role, score in scores[:top_k]
    ]