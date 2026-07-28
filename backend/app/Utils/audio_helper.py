import librosa


class AudioHelper:

    @staticmethod
    def get_duration(audio_path):
        return librosa.get_duration(path=audio_path)

    @staticmethod
    def get_sample_rate(audio_path):
        _, sr = librosa.load(audio_path, sr=None)
        return sr

    @staticmethod
    def get_audio_info(audio_path):
        return {
            "duration": AudioHelper.get_duration(audio_path),
            "sample_rate": AudioHelper.get_sample_rate(audio_path)
        }


if __name__ == "__main__":
    info = AudioHelper.get_audio_info("sample.wav")
    print(info)
