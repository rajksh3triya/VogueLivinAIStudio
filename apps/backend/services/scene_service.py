from pathlib import Path
import shutil
from uuid import uuid4

PROJECT_ROOT = Path("C:/AI/VogueLivinAIStudio/projects")

def save_scene(project_id: str, source_file: str):

    project = PROJECT_ROOT / project_id

    renders = project / "renders"

    renders.mkdir(parents=True, exist_ok=True)

    extension = Path(source_file).suffix

    filename = f"{uuid4()}{extension}"

    destination = renders / filename

    shutil.copy2(source_file, destination)

    return {
        "id": filename,
        "filename": filename,
        "path": str(destination)
    }
