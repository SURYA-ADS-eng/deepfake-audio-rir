import librosa
import numpy as np


class BreathingAnalyzer:
    """
    Basic breathing pattern analysis.
    """

    @staticmethod
    def extract_breathing_features(audio, sr):

        zero_crossing_rate = np.mean(
            librosa.feature.zero_crossing_rate(audio)
        )

        energy = np.mean(
            librosa.feature.rms(y=audio)
        )

        tempo, _ = librosa.beat.beat_track(
            y=audio,
            sr=sr
        )

        breathing_features = {
            "zero_crossing_rate": float(zero_crossing_rate),
            "average_energy": float(energy),
            "estimated_breathing_tempo": float(tempo)
        }

        return breathing_features
