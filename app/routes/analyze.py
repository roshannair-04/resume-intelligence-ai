from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os
from app.services.skill_recommender import recommend_skills
from app.services.resume_parser import parse_resume
from app.services.skill_extractor import load_skills, extract_skills
from app.services.matcher import calculate_match_score, find_missing_skills
from app.services.role_predictor import predict_roles
from app.services.resume_feedback import generate_feedback
from app.services.ats_scorer import calculate_ats_score
from app.services.evidence_extractor import extract_evidence
from app.services.resume_improver import generate_resume_improvements

router = APIRouter()




@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    temp_path = f"temp_{resume.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    resume_text = parse_resume(temp_path)

    os.remove(temp_path)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    match_score = calculate_match_score(resume_text, job_description)

    missing_skills = find_missing_skills(resume_skills, job_skills)

    predicted_roles = predict_roles(job_description)

    ats_score = calculate_ats_score(resume_skills, job_skills, predicted_roles)

    feedback = generate_feedback(
    resume_skills,
    missing_skills,
    predicted_roles
)
    improvements = generate_resume_improvements(
    resume_skills,
    missing_skills,
    predicted_roles
)

    recommended_skills = recommend_skills(resume_skills)

    evidence = extract_evidence(resume_text, resume_skills)

    return {
    "match_score": match_score,
    "predicted_roles": predicted_roles,
    "resume_skills": resume_skills,
    "missing_skills": missing_skills,
    "recommended_skills": recommended_skills,
    "feedback": feedback,
    "ats_score": ats_score,
    "evidence": evidence,
    "improvements": improvements
}