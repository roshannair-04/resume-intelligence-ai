from app.services.resume_parser import parse_resume
from app.services.skill_extractor import load_skills, extract_skills
from app.services.matcher import calculate_match_score, find_missing_skills
from app.services.role_predictor import predict_role
from app.services.resume_feedback import generate_feedback


resume_path = "/Users/zangetsu/Desktop/Codes/resumeanalyzer/tests/rerosh.pdf"

job_description = """
Looking for a Computer Vision Engineer with experience in Python,
OpenCV, YOLO, Docker, AWS, and machine learning for real-time video analysis.
"""

resume_text = parse_resume(resume_path)

skills_db = load_skills()

resume_skills = extract_skills(resume_text, skills_db)
job_skills = extract_skills(job_description, skills_db)

score = calculate_match_score(resume_text, job_description)

missing_skills = find_missing_skills(resume_skills, job_skills)

predicted_role = predict_role(resume_text)

feedback = generate_feedback(resume_skills, missing_skills)


print("\nPredicted Role:")
print(predicted_role)

print("\nMatch Score:")
print(score)

print("\nResume Skills:")
print(resume_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nAI Feedback:")
for f in feedback:
    print("-", f)


   