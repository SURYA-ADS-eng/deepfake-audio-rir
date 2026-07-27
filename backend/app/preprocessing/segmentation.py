import librosa


class AudioSegmenter:
    def __init__(self, sample_rate=16000, segment_duration=3):
        self.sample_rate = sample_rate
        self.segment_duration = segment_duration

    def split(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=self.sample_rate)

        segment_length = self.segment_duration * sr
        segments = []

        for i in range(0, len(audio), segment_length):
            segment = audio[i:i + segment_length]

            if len(segment) == segment_length:
                segments.append(segment)

        return segments


if __name__ == "__main__":
    segmenter = AudioSegmenter()

    segments = segmenter.split("sample.wav")

    print(f"Total Segments: {len(segments)}")
