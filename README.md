# AI Resume Intelligence Engine

An AI-powered resume analysis system that evaluates resumes against job descriptions using semantic embeddings and intelligent skill extraction.

The system performs:

• Resume parsing  
• Skill extraction using embeddings  
• Job description matching  
• Missing skill detection  
• Career role prediction (40+ roles)  
• ATS-style resume scoring  
• Evidence extraction from resumes  

---

# Features

### Resume Parsing
Extracts text from PDF resumes.

### Skill Detection
Uses semantic similarity to detect technical skills from resume text.

### Job Matching
Compares resume and job description using sentence embeddings.

### Missing Skill Detection
Identifies important skills absent from the resume.

### Career Role Prediction
Predicts top career roles based on semantic similarity across 40+ tech roles.

### ATS Resume Score
Calculates an ATS-style score based on skills, projects, and role alignment.

### Skill Evidence Extraction
Finds resume sentences that support detected skills.

---

# System Architecture

User Upload Resume
        │
        ▼
 Resume Parser
        │
        ▼
 Skill Extraction (Embeddings)
        │
        ├── Resume Skills
        ├── Job Skills
        │
        ▼
 Semantic Matching
        │
        ▼
 Career Role Prediction
        │
        ▼
 ATS Scoring + Evidence Extraction
        │
        ▼
 Interactive Dashboard

---

# Tech Stack

Backend
FastAPI  
Python  
Sentence Transformers  
Scikit-learn  

Frontend
HTML  
TailwindCSS  
Chart.js  

ML Components
Sentence Embeddings  
Cosine Similarity  
Semantic Skill Detection  

---

# Demo Dashboard

![Dashboard](screenshots/dashboard.png)

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/resume-intelligence-ai
cd resume-intelligence-ai
```

Create environment

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

Open in browser

```
http://127.0.0.1:8000
```

---

# Example Output

Match Score: 78%

Top Roles:
- Computer Vision Engineer
- Machine Learning Engineer
- AI Engineer

Missing Skills:
- Docker
- AWS

ATS Score:
- Skills: 30
- Role Fit: 24
- Projects: 18
- Education: 14

---

# Future Improvements

• LLM-based resume feedback  
• Real-time job scraping  
• Industry skill demand analysis  
• Multi-language resume support  

---

# Author

Roshan Nair  

