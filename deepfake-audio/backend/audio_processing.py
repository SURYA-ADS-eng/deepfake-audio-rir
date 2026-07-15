import io
from typing import Dict, Tuple

import librosa
import numpy as np


def load_audio(file_bytes: bytes, sr: int = 22050) -> Tuple[np.ndarray, int]:
    audio_buffer = io.BytesIO(file_bytes)
    y, sr = librosa.load(audio_buffer, sr=sr, mono=True)
    return y, sr


def estimate_rir(y: np.ndarray, sr: int) -> Dict[str, float]:
    # Heuristic RIR / reverb proxy using autocorrelation and spectral decay
    rir = librosa.autocorrelate(y, max_size=sr // 2)
    if np.max(np.abs(rir)) > 0:
        rir = rir / np.max(np.abs(rir))

    early_decay = float(np.mean(np.abs(rir[: sr // 10])))
    tail_energy = float(np.mean(np.abs(rir[sr // 10 : sr // 5])))
    reverb_score = max(0.0, min(1.0, tail_energy - early_decay))

    return {
        "rir_strength": reverb_score,
        "rir_curve_sample": [float(v) for v in rir[:200]],
    }


def extract_breath_pattern(y: np.ndarray, sr: int) -> Dict[str, float]:
    energy = librosa.feature.rms(y=y)[0]
    if len(energy) == 0:
        return {"breath_events": 0.0, "breath_rate": 0.0}

    peaks = librosa.util.peak_pick(energy, pre_max=2, post_max=2, pre_avg=3, post_avg=3, delta=0.02, wait=20)
    duration = max(1.0, librosa.get_duration(y=y, sr=sr))
    breath_rate = len(peaks) / duration

    return {
        "breath_events": float(len(peaks)),
        "breath_rate": float(breath_rate),
    }


def extract_features(y: np.ndarray, sr: int) -> Dict[str, object]:
    melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    melspec_db = librosa.power_to_db(melspec, ref=np.max)

    rir = estimate_rir(y, sr)
    breath = extract_breath_pattern(y, sr)

    return {
        "mel_spectrogram": melspec_db.astype(np.float32),
        "rir": rir,
        "breath": breath,
    }


def prepare_model_input(features: Dict[str, object]) -> np.ndarray:
    x = features["mel_spectrogram"]
    if x.ndim == 2:
        x = np.expand_dims(x, axis=0)
    return x
