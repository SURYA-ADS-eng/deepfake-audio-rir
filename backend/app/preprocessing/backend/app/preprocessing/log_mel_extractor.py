import librosa
import numpy as np


class LogMelExtractor:
    def __init__(self, sample_rate=16000, n_mels=128):
        self.sample_rate = sample_rate
        self.n_mels = n_mels

    def extract(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=self.sample_rate)

        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=sr,
            n_mels=self.n_mels
        )

        log_mel = librosa.power_to_db(mel, ref=np.max)
        return log_mel
