from fastapi import APIRouter

from engine.scanner.comfy_scanner import scan_comfy
from engine.scanner.model_scanner import scan_models
from engine.scanner.node_scanner import scan_nodes

router = APIRouter(
    prefix="/system",
    tags=["System"]
)

@router.get("/diagnostics")
def diagnostics():
    return {
        "comfy": scan_comfy(),
        "models": scan_models(),
        "nodes": scan_nodes()
    }
