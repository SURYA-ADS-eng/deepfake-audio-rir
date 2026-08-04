import librosa


class AudioMetadata:

    @staticmethod
    def extract(audio_path):
        audio, sr = librosa.load(audio_path, sr=None)

        return {
            "sample_rate": sr,
            "duration": librosa.get_duration(y=audio, sr=sr),
            "samples": len(audio),
            "channels": 1
        }


if __name__ == "__main__":
    metadata = AudioMetadata.extract("sample.flac")
    print(metadata)
