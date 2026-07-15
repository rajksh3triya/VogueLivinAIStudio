from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.projects import router as project_router
from api.scenes import router as scene_router
from api.system import router as system_router

app = FastAPI(title="VogueLivin AI Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system_router)
app.include_router(project_router)
app.include_router(scene_router)

@app.get("/")
def root():
    return {
        "status": "ok",
        "app": "VogueLivin AI Studio"
    }

@app.get("/health")
def health():
    return {
        "healthy": True
    }
