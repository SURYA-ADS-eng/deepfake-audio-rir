from fastapi import APIRouter

router = APIRouter()


@router.post("/predict")
def predict():
    """
    Placeholder for the ML model.
    """

    return {
        "prediction": "Model not integrated yet",
        "confidence": 0
    }