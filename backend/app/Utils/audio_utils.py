import librosa
import numpy as np

SAMPLE_RATE = 16000

def load_audio(file_path):
    audio, sr = librosa.load(file_path, sr=SAMPLE_RATE)
    return audio, sr

def extract_mfcc(audio, sr, n_mfcc=40):
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=n_mfcc
    )
    return np.mean(mfcc.T, axis=0)

def extract_mel(audio, sr):
    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)
    return np.mean(mel_db.T, axis=0)
