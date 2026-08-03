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

Week 1 – Completed Work
Initialized the GitHub repository and project structure.
Set up the FastAPI backend.
Implemented audio upload and health check APIs.
Developed the audio preprocessing pipeline:
Audio loading
Audio validation
Audio normalization
Audio segmentation
Implemented feature extraction using Librosa:
MFCC
Mel Spectrogram
Log-Mel Spectrogram
Chroma Features
Spectral Features
Room Impulse Response (RIR)
Breathing Features
Added backend utilities (logging, configuration, file handling, prediction framework).


Week 2 – Completed Work
Downloaded and organized the ASVspoof2019 LA dataset.
Implemented dataset loader and label handling.
Prepared the backend for Audio Spectrogram Transformer (AST) integration.
Developed the React frontend:
Audio upload page
Waveform visualization
Results dashboard
Integrated frontend structure with the backend API.
Planned the AST-based training and prediction pipeline for the next phase.
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
