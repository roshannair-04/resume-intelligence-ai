def generate_resume_improvements(resume_skills, missing_skills, predicted_roles):

    suggestions = []

    if predicted_roles:
        role = predicted_roles[0]["role"]

        suggestions.append(
            f"Your resume aligns with the {role} career path."
        )

    if missing_skills:

        suggestions.append(
            "Consider adding projects demonstrating these technologies:"
        )

        for skill in missing_skills[:3]:
            suggestions.append(
                f"• Build a project using {skill}"
            )

    # general resume improvements
    suggestions.append(
        "Include measurable achievements (accuracy, latency, performance improvements)."
    )

    suggestions.append(
        "Highlight real-world ML deployments or APIs if possible."
    )

    suggestions.append(
        "Add GitHub links to projects demonstrating your technical skills."
    )

    return suggestions