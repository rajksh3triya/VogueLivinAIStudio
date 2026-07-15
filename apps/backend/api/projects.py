from fastapi import APIRouter

from schemas.project import ProjectCreate
from services.project_service import create_project

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("")
def new_project(project: ProjectCreate):
    return create_project(project)
