import librosa
import os


class AudioLoader:
    """
    Handles loading and basic validation of audio files.
    """

    SUPPORTED_FORMATS = (".wav", ".mp3", ".flac", ".ogg", ".m4a")

    @staticmethod
    def load_audio(file_path: str, sample_rate: int = 16000):
        """
        Load an audio file using librosa.

        Args:
            file_path (str): Path to the audio file.
            sample_rate (int): Target sample rate.

        Returns:
            tuple:
                audio_data (numpy.ndarray)
                sample_rate (int)
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = os.path.splitext(file_path)[1].lower()

        if extension not in AudioLoader.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported audio format: {extension}"
            )

        audio, sr = librosa.load(
            file_path,
            sr=sample_rate,
            mono=True
        )

        return audio, sr

    @staticmethod
    def get_audio_metadata(audio, sr):
        """
        Returns useful metadata about the audio.
        """

        duration = librosa.get_duration(y=audio, sr=sr)

        metadata = {
            "sample_rate": sr,
            "duration_seconds": round(duration, 2),
            "num_samples": len(audio)
        }

        return metadata
