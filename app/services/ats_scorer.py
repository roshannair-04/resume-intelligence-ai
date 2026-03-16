import random

def calculate_ats_score(resume_skills, job_skills, predicted_roles):

    skill_match = min(len(set(resume_skills) & set(job_skills)) * 10, 40)

    role_score = int(predicted_roles[0]["score"] * 30)

    project_score = random.randint(15,25)

    education_score = random.randint(10,20)

    total = skill_match + role_score + project_score + education_score

    return {
        "skills": skill_match,
        "role": role_score,
        "projects": project_score,
        "education": education_score,
        "total": total
    }