from enum import Enum

class GenerationState(str, Enum):
    CREATED = "created"
    VALIDATING = "validating"
    BUILDING_PROMPT = "building_prompt"
    LOADING_WORKFLOW = "loading_workflow"
    SUBMITTING = "submitting"
    QUEUED = "queued"
    RUNNING = "running"
    SAVING = "saving"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
