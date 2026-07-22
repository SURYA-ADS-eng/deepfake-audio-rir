import librosa
import numpy as np


class AudioValidator:
    def __init__(self, min_duration=1.0):
        self.min_duration = min_duration

    def validate(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=16000)

        duration = librosa.get_duration(y=audio, sr=sr)

        if duration < self.min_duration:
            return False, "Audio is too short."

        if np.max(np.abs(audio)) < 0.001:
            return False, "Audio is almost silent."

        return True, "Audio is valid."


if __name__ == "__main__":
    validator = AudioValidator()

    status, message = validator.validate("sample.wav")

    print(status)
    print(message)
