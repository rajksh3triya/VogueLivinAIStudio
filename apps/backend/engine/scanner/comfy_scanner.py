from pathlib import Path

COMFY_ROOT = Path(r"C:\AI\ComfyUI")

def scan_comfy():

    return {
        "installed": COMFY_ROOT.exists(),
        "path": str(COMFY_ROOT),
        "models": (COMFY_ROOT / "models").exists(),
        "custom_nodes": (COMFY_ROOT / "custom_nodes").exists(),
        "input": (COMFY_ROOT / "input").exists(),
        "output": (COMFY_ROOT / "output").exists(),
        "server": (COMFY_ROOT / "server.py").exists(),
        "main": (COMFY_ROOT / "main.py").exists(),
        "execution": (COMFY_ROOT / "execution.py").exists(),
    }
