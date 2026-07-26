import os
from pathlib import Path


class DatasetLoader:
    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)

    def get_audio_files(self):
        audio_extensions = [".wav", ".flac", ".mp3"]

        files = []

        for ext in audio_extensions:
            files.extend(self.dataset_path.rglob(f"*{ext}"))

        return sorted(files)

    def summary(self):
        files = self.get_audio_files()

        return {
            "dataset_path": str(self.dataset_path),
            "total_audio_files": len(files)
        }


if __name__ == "__main__":
    loader = DatasetLoader("data/raw")

    print(loader.summary())
