import librosa


class AudioDurationFilter:
    def __init__(self, min_duration=2.0, max_duration=10.0):
        self.min_duration = min_duration
        self.max_duration = max_duration

    def validate(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=None)
        duration = librosa.get_duration(y=audio, sr=sr)

        if duration < self.min_duration:
            return False, "Audio is too short"

        if duration > self.max_duration:
            return False, "Audio is too long"

        return True, "Audio duration is valid"


if __name__ == "__main__":
    validator = AudioDurationFilter()
    print(validator.validate("sample.flac"))
