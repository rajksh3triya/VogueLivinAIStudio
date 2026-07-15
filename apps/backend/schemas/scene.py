from pydantic import BaseModel

class SceneCreate(BaseModel):
    project_id: str
    filename: str
