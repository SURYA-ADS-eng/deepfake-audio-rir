# AcousticSpace – Deepfake Audio Detection using Acoustic Room Impulse Response (RIR)

Deepfake Audio Detection using **Acoustic Room Impulse Response (RIR)** developed as part of the **Data Science & Machine Learning Internship at Infotact Solutions**.

## Tech Stack
- Python
- FastAPI
- Librosa
- PyTorch
- Hugging Face Transformers
- React

## Current Progress
- ✅ Project repository and folder structure created.
- ✅ FastAPI backend initialized.
- ✅ Audio loading module implemented.
- ✅ **Feature extraction module (`extract_features.py`) completed.**

### Today's Work
Implemented `extract_features.py` to extract essential audio features for deepfake detection, including:
- MFCC
- Mel Spectrogram
- Chroma Features
- Spectral Contrast
- Zero Crossing Rate
- RMS Energy
- Spectral Centroid
- Spectral Bandwidth
- Spectral Roll-off

These extracted features will be used as input for the deep learning model in the next development phase.

## Upcoming Work
- Room Impulse Response (RIR) extraction
- Breathing pattern analysis
- CNN & Audio Spectrogram Transformer (AST) model
- FastAPI prediction API
- React dashboard integration
- Docker deployment
