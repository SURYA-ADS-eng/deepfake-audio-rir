# AcousticSpace – Deepfake Audio Detection using Acoustic Room Impulse Response (RIR)

Deepfake Audio Detection using Acoustic Room Impulse Response (RIR) developed as part of the **Data Science & Machine Learning Internship** at **Infotact Solutions**.

---

## 🚀 Tech Stack

- Python
- FastAPI
- Librosa
- PyTorch
- Hugging Face Transformers
- Audio Spectrogram Transformer (AST)
- React
- TypeScript
- Vite

---

## 📌 Current Progress

### ✅ Backend
- FastAPI backend initialized.
- Modular project structure created.
- Audio upload service implemented.
- Health API added.
- Logging and configuration modules implemented.
- Utility modules for file handling and audio processing created.
- Prediction service framework developed.

### ✅ Audio Preprocessing
- Audio loading
- Audio validation
- Audio normalization
- Audio segmentation

### ✅ Feature Extraction
Implemented Librosa-based feature extraction pipeline including:

- MFCC
- Mel Spectrogram
- Log-Mel Spectrogram
- Chroma Features
- Spectral Contrast
- Zero Crossing Rate
- RMS Energy
- Spectral Centroid
- Spectral Bandwidth
- Spectral Roll-off
- Room Impulse Response (RIR)
- Breathing Feature Extraction
- Unified feature extraction pipeline

### ✅ Frontend
- React + TypeScript + Vite project setup
- Audio upload component
- Waveform visualization component
- Results dashboard UI
- Backend API integration structure

---

## 📝 Today's Work

Implemented:

- Log-Mel Spectrogram extraction module for Audio Spectrogram Transformer (AST).
- AST configuration module for model parameters.
- Updated preprocessing pipeline for future AST integration.

These modules prepare the project for transformer-based audio classification.

---

## 🔜 Upcoming Work

- Prepare ASVspoof2019 LA dataset
- Fine-tune Audio Spectrogram Transformer (AST)
- Model evaluation (Accuracy, Precision, Recall, F1-score)
- Integrate trained AST model with FastAPI
- Connect frontend with prediction API
- End-to-end system testing
- Docker deployment
- Final project documentation

---

## 📂 Project Workflow

```
User Uploads Audio
        │
        ▼
Audio Validation
        │
        ▼
Normalization
        │
        ▼
Segmentation
        │
        ▼
Feature Extraction
 ├── MFCC
 ├── Mel Spectrogram
 ├── Log-Mel Spectrogram
 ├── Chroma Features
 ├── Spectral Contrast
 ├── RIR
 └── Breathing Features
        │
        ▼
Audio Spectrogram Transformer (AST)
        │
        ▼
Prediction
(Real / Deepfake)
        │
        ▼
Confidence Score
        │
        ▼
FastAPI API
        │
        ▼
React Dashboard
```

---

## 📈 Project Status

- ✅ Backend Development – Completed
- ✅ Audio Preprocessing – Completed
- ✅ Feature Extraction – Completed
- ✅ Frontend UI – Completed
- 🔄 Dataset Preparation – In Progress
- ⏳ Audio Spectrogram Transformer (AST) Training – Pending
- ⏳ Backend–Model Integration – Pending
- ⏳ End-to-End Testing – Pending
- ⏳ Deployment – Pending
