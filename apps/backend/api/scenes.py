from fastapi import APIRouter, UploadFile, File, Form
from pathlib import Path
import shutil
from uuid import uuid4

router = APIRouter(
    prefix="/scenes",
    tags=["Scenes"]
)

UPLOAD_DIR = Path("C:/AI/VogueLivinAIStudio/uploads/temp")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def upload_scene(
    project_id: str = Form(...),
    file: UploadFile = File(...)
):

    extension = Path(file.filename).suffix

    filename = f"{uuid4()}{extension}"

    destination = UPLOAD_DIR / filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "success": True,
        "project_id": project_id,
        "filename": filename,
        "path": str(destination)
    }
