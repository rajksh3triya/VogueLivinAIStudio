from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    client: str
    location: str
    resolution: str
