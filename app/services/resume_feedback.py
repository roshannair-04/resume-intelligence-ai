import json


with open("data/role_skill_map.json") as f:
    role_map = json.load(f)


def generate_feedback(resume_skills, missing_skills, predicted_roles):

    feedback = []

    if not predicted_roles:
        return ["Unable to determine role recommendations."]

    top_role = predicted_roles[0]["role"]

    feedback.append(
        f"Your profile aligns most with a {top_role} role."
    )

    # Suggest role skills
    if top_role in role_map:

        recommended = role_map[top_role]

        missing_role_skills = [
            skill for skill in recommended
            if skill.lower() not in [s.lower() for s in resume_skills]
        ]

        if missing_role_skills:

            feedback.append(
                f"To strengthen your {top_role} profile consider learning:"
            )

            for skill in missing_role_skills[:4]:
                feedback.append(f"• {skill}")

    # Missing skills from job description
    if missing_skills:

        feedback.append(
            "Important skills missing for this job:"
        )

        for skill in missing_skills[:4]:
            feedback.append(f"• {skill}")

    return feedback