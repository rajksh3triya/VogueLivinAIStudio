from pathlib import Path

NODE_ROOT = Path(r"C:\AI\ComfyUI\custom_nodes")

def scan_nodes():

    if not NODE_ROOT.exists():
        return []

    return sorted([
        folder.name
        for folder in NODE_ROOT.iterdir()
        if folder.is_dir()
    ])
