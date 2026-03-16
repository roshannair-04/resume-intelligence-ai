from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.services.skill_extractor import load_skills
from app.services.role_predictor import load_roles
from app.routes.analyze import router as analyze_router
from app.services.role_predictor import load_roles


load_skills()
load_roles()
app = FastAPI(title="AI Resume Analyzer")

app.include_router(analyze_router)

# Serve frontend folder
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def home():
    return FileResponse("frontend/index.html")