import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.title("AI Resume Analyzer & Job Matcher")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

job_description = st.text_area("Paste the job description")

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        files = {
            "resume": uploaded_file.getvalue()
        }

        response = requests.post(
            API_URL,
            files={"resume": uploaded_file},
            data={"job_description": job_description}
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Match Score")
            st.write(result["match_score"])

            st.subheader("Predicted Role")
            st.write(result["predicted_role"])

            st.subheader("Resume Skills")
            st.write(result["resume_skills"])

            st.subheader("Missing Skills")
            st.write(result["missing_skills"])

            st.subheader("AI Feedback")
            for f in result["feedback"]:
                st.write("-", f)

        else:
            st.error("Analysis failed")

    else:
        st.warning("Please upload a resume and paste a job description.")