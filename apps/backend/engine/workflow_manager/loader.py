import json
from pathlib import Path

WORKFLOW_DIR = Path(r"C:\AI\VogueLivinAIStudio\workflows")

class WorkflowLoader:

    @staticmethod
    def load(name: str) -> dict:
        path = WORKFLOW_DIR / f"{name}.json"

        if not path.exists():
            raise FileNotFoundError(f"Workflow '{name}' not found")

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def list():
        return sorted([
            f.stem
            for f in WORKFLOW_DIR.glob("*.json")
        ])
