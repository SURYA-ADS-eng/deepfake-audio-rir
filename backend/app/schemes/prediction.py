from pydantic import BaseModel


class PredictionResponse(BaseModel):
    filename: str
    prediction: str
    confidence: float
    processing_time: float
