from dataclasses import dataclass
from engine.generation.state import GenerationState

@dataclass
class GenerationJob:
    id: str
    project_id: str
    scene_id: str
    provider: str
    workflow: str
    camera: str
    state: GenerationState = GenerationState.CREATED
    progress: int = 0
