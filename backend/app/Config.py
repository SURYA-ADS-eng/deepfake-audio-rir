import os

# Audio Settings
SAMPLE_RATE = 16000
SUPPORTED_FORMATS = [".wav", ".mp3", ".flac", ".ogg"]

# Model Settings
MODEL_PATH = os.path.join("models", "deepfake_audio_model.pth")
DEVICE = "cpu"  # Change to "cuda" if GPU is available

# Prediction Settings
CONFIDENCE_THRESHOLD = 0.50

# Upload Settings
UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB

# Logging
LOG_FILE = "logs/app.log"
