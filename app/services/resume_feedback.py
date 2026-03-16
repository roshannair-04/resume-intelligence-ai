def generate_feedback(resume_skills, missing_skills):

    feedback = []

    if len(missing_skills) > 0:
        feedback.append(
            f"You may improve your resume by learning: {', '.join(missing_skills)}"
        )

    if "docker" not in resume_skills:
        feedback.append("Consider learning Docker for modern ML deployments.")

    if "aws" not in resume_skills:
        feedback.append("Cloud skills like AWS can improve job matching.")

    if "machine learning" in resume_skills and "deep learning" not in resume_skills:
        feedback.append(
            "Adding deep learning frameworks like PyTorch or TensorFlow could strengthen your profile."
        )

    if len(resume_skills) < 5:
        feedback.append("Try adding more technical skills to your resume.")

    return feedback