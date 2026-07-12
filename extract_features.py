
import sys
import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def load_audio(file_path: str, sr: int = 16000):
    """Load an audio file at a fixed sample rate."""
    audio, sample_rate = librosa.load(file_path, sr=sr)
    return audio, sample_rate


def extract_mel_spectrogram(audio: np.ndarray, sr: int):
    """Compute a mel-spectrogram in decibel scale."""
    mel_spec = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    return mel_spec_db


def extract_mfcc(audio: np.ndarray, sr: int, n_mfcc: int = 13):
    """Compute MFCCs (standard voice-content features)."""
    return librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)


def plot_waveform_and_spectrogram(audio: np.ndarray, sr: int, mel_spec_db: np.ndarray, out_path: str):
    """Save a side-by-side plot of waveform and mel-spectrogram."""
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    librosa.display.waveshow(audio, sr=sr, ax=axes[0])
    axes[0].set_title("Waveform")

    img = librosa.display.specshow(mel_spec_db, sr=sr, x_axis="time", y_axis="mel", ax=axes[1])
    axes[1].set_title("Mel-Spectrogram (dB)")
    fig.colorbar(img, ax=axes[1], format="%+2.0f dB")

    plt.tight_layout()
    plt.savefig(out_path)
    print(f"Saved plot to {out_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_features.py path/to/sample.wav")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    audio, sr = load_audio(file_path)
    print(f"Loaded '{file_path}' — duration: {len(audio) / sr:.2f}s, sample rate: {sr}")

    mel_spec_db = extract_mel_spectrogram(audio, sr)
    mfcc = extract_mfcc(audio, sr)
    print(f"Mel-spectrogram shape: {mel_spec_db.shape}")
    print(f"MFCC shape: {mfcc.shape}")

    out_name = os.path.splitext(os.path.basename(file_path))[0] + "_features.png"
    plot_waveform_and_spectrogram(audio, sr, mel_spec_db, out_name)


if __name__ == "__main__":
    main()
