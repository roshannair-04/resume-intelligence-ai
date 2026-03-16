skill_map = {
    "machine learning": ["pytorch", "tensorflow"],
    "computer vision": ["opencv", "yolo"],
    "backend engineer": ["docker", "kubernetes"],
    "data scientist": ["pandas", "numpy", "scikit-learn"],
}


def recommend_skills(resume_skills):

    recommendations = set()

    for skill in resume_skills:
        if skill in skill_map:
            recommendations.update(skill_map[skill])

    return list(recommendations)