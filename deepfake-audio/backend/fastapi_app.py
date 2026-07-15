import io
from typing import Dict

import numpy as np
import torch
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from audio_processing import load_audio, extract_features, prepare_model_input
from model import load_model, predict

app = FastAPI(title="AcousticSpace API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cpu")
model = load_model(device)


class InferenceResponse(BaseModel):
    predicted_label: str
    confidence: float
    rir_features: Dict[str, float]
    breath_features: Dict[str, float]
    spectrogram_shape: tuple


@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)) -> InferenceResponse:
    raw_bytes = await file.read()
    y, sr = load_audio(raw_bytes)
    features = extract_features(y, sr)
    model_input = prepare_model_input(features)

    tensor = torch.from_numpy(model_input).unsqueeze(0)
    if tensor.ndim == 4:
        pass
    else:
        tensor = tensor.unsqueeze(1)

    probs = predict(model, tensor)
    score = float(probs[0, 1].item())
    label = "synthetic" if score > 0.5 else "real"

    return InferenceResponse(
        predicted_label=label,
        confidence=score,
        rir_features=features["rir"],
        breath_features=features["breath"],
        spectrogram_shape=features["mel_spectrogram"].shape,
    )


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}
