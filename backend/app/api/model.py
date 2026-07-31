from fastapi import APIRouter
import os

router = APIRouter(prefix="/model", tags=["Model"])


@router.get("/status")
def model_status():
    model_path = "models/deepfake_ast_model.pth"

    return {
        "model_exists": os.path.exists(model_path),
        "model_path": model_path,
        "status": "ready" if os.path.exists(model_path) else "model not trained"
    }
