from pathlib import Path
import json

WORKFLOW_DIR = Path("C:/AI/VogueLivinAIStudio/workflows")

def load_workflow(name: str):

    workflow = WORKFLOW_DIR / f"{name}.json"

    if not workflow.exists():
        raise FileNotFoundError(f"Workflow '{name}' not found")

    with open(workflow, "r", encoding="utf-8") as f:
        return json.load(f)
