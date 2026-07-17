from app.preprocessing.rir import RIRExtractor
from app.preprocessing.breathing import BreathingAnalyzer

import sys
import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def load_audio(file_path: str, sr: int = 16000):
    """
    Load an audio file at a fixed sample rate.
    """
    audio, sample_rate = librosa.load(file_path, sr=sr)
    return audio, sample_rate


def extract_mel_spectrogram(audio: np.ndarray, sr: int):
    """
    Compute Mel Spectrogram in decibel scale.
    """
    mel_spec = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128
    )

    mel_spec_db = librosa.power_to_db(
        mel_spec,
        ref=np.max
    )

    return mel_spec_db


def extract_mfcc(audio: np.ndarray, sr: int, n_mfcc: int = 13):
    """
    Compute MFCC features.
    """
    return librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=n_mfcc
    )


def extract_all_features(audio: np.ndarray, sr: int):
    """
    Extract all audio features.
    """

    features = {}

    # MFCC
    mfcc = extract_mfcc(audio, sr)
    features["mfcc"] = np.mean(mfcc, axis=1).tolist()

    # Mel Spectrogram
    mel_spec = extract_mel_spectrogram(audio, sr)
    features["mel_spectrogram_shape"] = mel_spec.shape

    # RIR Features
    rir_features = RIRExtractor.extract_rir_features(audio, sr)

    # Breathing Features
    breathing_features = BreathingAnalyzer.extract_breathing_features(audio, sr)

    # Merge
    features.update(rir_features)
    features.update(breathing_features)

    return features, mel_spec


def plot_waveform_and_spectrogram(
    audio: np.ndarray,
    sr: int,
    mel_spec_db: np.ndarray,
    out_path: str
):
    """
    Save waveform and Mel Spectrogram.
    """

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    librosa.display.waveshow(
        audio,
        sr=sr,
        ax=axes[0]
    )

    axes[0].set_title("Waveform")

    img = librosa.display.specshow(
        mel_spec_db,
        sr=sr,
        x_axis="time",
        y_axis="mel",
        ax=axes[1]
    )

    axes[1].set_title("Mel Spectrogram (dB)")

    fig.colorbar(
        img,
        ax=axes[1],
        format="%+2.0f dB"
    )

    plt.tight_layout()
    plt.savefig(out_path)

    print(f"\nWaveform & Spectrogram saved to: {out_path}")


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python extract_features.py path/to/audio.wav")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    # Load Audio
    audio, sr = load_audio(file_path)

    print("\n========== AUDIO INFORMATION ==========")
    print(f"File : {file_path}")
    print(f"Duration : {len(audio)/sr:.2f} seconds")
    print(f"Sample Rate : {sr}")

    # Extract Features
    features, mel_spec_db = extract_all_features(audio, sr)

    print("\n========== EXTRACTED FEATURES ==========")

    for key, value in features.items():
        print(f"{key}: {value}")

    # Save Visualization
    output_image = (
        os.path.splitext(os.path.basename(file_path))[0]
        + "_features.png"
    )

    plot_waveform_and_spectrogram(
        audio,
        sr,
        mel_spec_db,
        output_image
    )

    print("\nFeature Extraction Completed Successfully.")


if __name__ == "__main__":
    main()
