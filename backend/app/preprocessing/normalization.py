import librosa
import numpy as np


class AudioNormalizer:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def normalize(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=self.sample_rate)

        max_value = np.max(np.abs(audio))

        if max_value > 0:
            audio = audio / max_value

        return audio, sr

    def save_normalized(self, output_path, audio, sr):
        import soundfile as sf
        sf.write(output_path, audio, sr)
