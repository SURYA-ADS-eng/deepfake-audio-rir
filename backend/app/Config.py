import os

# Project Root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Audio Settings
SAMPLE_RATE = 16000
SUPPORTED_AUDIO_FORMATS = [
    ".wav",
    ".mp3",
    ".flac",
    ".ogg"
]

# Model Settings
MODEL_NAME = "Deepfake Audio Detector"
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "deepfake_model.pth")

# Prediction
PREDICTION_THRESHOLD = 0.5

# Upload Directory
UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
