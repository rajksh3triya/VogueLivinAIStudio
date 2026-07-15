from pathlib import Path
import json
from uuid import uuid4

PROJECT_ROOT = Path("C:/AI/VogueLivinAIStudio/projects")

PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

def create_project(data):

    project_id = str(uuid4())

    folder = PROJECT_ROOT / project_id

    folder.mkdir(parents=True, exist_ok=True)

    (folder / "renders").mkdir(exist_ok=True)
    (folder / "generated").mkdir(exist_ok=True)
    (folder / "exports").mkdir(exist_ok=True)
    (folder / "cache").mkdir(exist_ok=True)
    (folder / "thumbnails").mkdir(exist_ok=True)

    project = {
        "id": project_id,
        "name": data.name,
        "client": data.client,
        "location": data.location,
        "resolution": data.resolution,
    }

    with open(folder / "project.json","w",encoding="utf-8") as f:
        json.dump(project,f,indent=4)

    return project
