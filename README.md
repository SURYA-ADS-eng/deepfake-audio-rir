# deepfake-audio-rir
Deepfake Audio Detection using Acoustic Room Impulse Response (RIR) – Data Science &amp; Machine Learning Internship Project at Infotact Solutions. 

Weekly Project Write-up
Project Title

AcousticSpace: Deepfake Detection via Room Impulse Response (RIR)

Objective

To develop an AI-based deepfake audio detection system that analyzes Room Impulse Response (RIR), environmental reverberation, and breathing patterns to distinguish genuine audio from AI-generated deepfake audio.

Week 1 – Project Setup and Data Collection
Objective

Establish the development environment and prepare the dataset for model training.

Work Done
Understood the problem statement and project requirements.
Installed required software:
Python
FastAPI
Librosa
PyTorch
React
VS Code
Git
Collected the ASVspoof dataset for deepfake audio.
Studied Room Impulse Response (RIR) and environmental acoustic features.
Developed an audio preprocessing pipeline using Librosa.
Extracted:
Spectrograms
MFCC features
RIR-related acoustic features
Created the FastAPI backend server.
Designed the React project structure.
Built the basic user interface containing:
Audio upload page
Dashboard layout
Outcome
Development environment successfully configured.
Audio preprocessing pipeline completed.
Basic frontend and backend established.
Week 2 – Baseline Model Development
Objective

Develop the first deepfake audio classification model.

Work Done
Preprocessed all audio samples.
Converted audio into spectrogram images.
Built a baseline CNN/Transformer model using PyTorch.
Trained the model using extracted acoustic features.
Evaluated model performance using:
Accuracy
Loss
Precision
Integrated WaveSurfer.js in React.
Displayed uploaded audio waveform.
Connected frontend with FastAPI APIs.
Mid-Project Review
Verified successful extraction of RIR features.
Tested preprocessing pipeline.
Measured initial model accuracy.
Fixed preprocessing and API integration issues.
Outcome
Functional baseline model developed.
Audio visualization completed.
Initial prediction system working.
Week 3 – Advanced AI Model Development
Objective

Improve detection accuracy using transformer-based deep learning.

Work Done
Fine-tuned Hugging Face Audio Spectrogram Transformer (AST).
Improved feature extraction.
Added breathing cadence analysis.
Compared:
Vocal rhythm
Environmental acoustics
Optimized feature engineering.
Developed the prediction result module.
Displayed:
Confidence score
Deepfake probability
Suspicious waveform regions
Improved API response speed.
Outcome
Advanced transformer model trained.
Better prediction accuracy achieved.
Interactive results dashboard completed.
Week 4 – Deployment and Final Integration
Objective

Deploy the complete deepfake detection system.

Work Done
Containerized the application using Docker.
Optimized FastAPI inference time.
Implemented CI/CD pipeline.
Improved React UI/UX.
Added:
Analysis history
State management
Better navigation
Connected all modules:
Frontend
Backend
Machine Learning model
Conducted system testing using multiple genuine and fake audio samples.
Final Project Review
Verified complete workflow.
Measured model performance.
Fixed remaining bugs.
Prepared project documentation.
Created final presentation and demonstration.
Outcome
Successfully developed a complete deepfake audio detection system.
System accurately detects AI-generated audio using Room Impulse Response rather than only voice characteristics.
Responsive analyst dashboard completed for real-time forensic analysis.
Technologies Used
Category	Technology
Programming Language	Python
Audio Processing	Librosa
Machine Learning	PyTorch
Transformer Model	Hugging Face AST
Backend	FastAPI
Frontend	React, TypeScript
Visualization	WaveSurfer.js
Deployment	Docker
Version Control	Git & GitHub
Dataset	ASVspoof
Final Deliverables
Audio preprocessing pipeline
Feature extraction module
Deepfake detection model
FastAPI backend
React analyst dashboard
Audio waveform visualization
Confidence score prediction
Docker deployment
Complete project documentation
Conclusion

The AcousticSpace project successfully demonstrates a novel approach to deepfake audio detection by analyzing Room Impulse Response (RIR) and environmental acoustic characteristics instead of relying solely on vocal features. Using advanced transformer models, audio signal processing, and an interactive React dashboard, the system provides accurate, real-time detection of synthetic audio. This approach improves the reliability of audio forensics and strengthens protection against AI-generated voice fraud.
