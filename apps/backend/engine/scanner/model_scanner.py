from pathlib import Path

MODEL_ROOT = Path(r"C:\AI\ComfyUI\models")

def scan_models():

    folders = [
        "checkpoints",
        "diffusion_models",
        "text_encoders",
        "vae",
        "loras",
        "clip"
    ]

    report = {}

    for folder in folders:

        path = MODEL_ROOT / folder

        files = []

        if path.exists():
            files = [f.name for f in path.rglob("*") if f.is_file()]

        report[folder] = {
            "exists": path.exists(),
            "count": len(files),
            "files": files
        }

    return report
