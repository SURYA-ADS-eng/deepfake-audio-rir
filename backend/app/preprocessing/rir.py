import librosa
import numpy as np


class RIRExtractor:
    """
    Room Impulse Response (RIR) Feature Extraction
    """

    @staticmethod
    def extract_rir_features(audio, sr):
        """
        Extract room acoustic related features.
        """

        spectral_centroid = np.mean(
            librosa.feature.spectral_centroid(
                y=audio,
                sr=sr
            )
        )

        spectral_bandwidth = np.mean(
            librosa.feature.spectral_bandwidth(
                y=audio,
                sr=sr
            )
        )

        spectral_rolloff = np.mean(
            librosa.feature.spectral_rolloff(
                y=audio,
                sr=sr
            )
        )

        rms_energy = np.mean(
            librosa.feature.rms(y=audio)
        )

        rir_features = {
            "spectral_centroid": float(spectral_centroid),
            "spectral_bandwidth": float(spectral_bandwidth),
            "spectral_rolloff": float(spectral_rolloff),
            "rms_energy": float(rms_energy)
        }

        return rir_features
