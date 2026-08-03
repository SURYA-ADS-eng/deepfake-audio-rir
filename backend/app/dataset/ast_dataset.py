import torch
from torch.utils.data import Dataset

from app.preprocessing.log_mel_extractor import LogMelExtractor


class ASTDataset(Dataset):
    def __init__(self, samples):
        self.samples = samples
        self.extractor = LogMelExtractor()

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        sample = self.samples[index]

        features = self.extractor.extract(sample["audio_path"])

        return {
            "features": torch.tensor(features, dtype=torch.float32),
            "label": sample["label"]
        }
