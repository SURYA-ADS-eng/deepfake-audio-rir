import os
from torch.utils.data import Dataset


class ASVSpoofDataset(Dataset):
    def __init__(self, protocol_file, audio_dir):
        self.audio_dir = audio_dir
        self.samples = []

        with open(protocol_file, "r") as file:
            for line in file:
                parts = line.strip().split()

                file_name = parts[1]
                label = parts[-1]

                self.samples.append(
                    (
                        file_name,
                        0 if label == "bonafide" else 1
                    )
                )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        file_name, label = self.samples[index]

        audio_path = os.path.join(
            self.audio_dir,
            file_name + ".flac"
        )

        return audio_path, label
