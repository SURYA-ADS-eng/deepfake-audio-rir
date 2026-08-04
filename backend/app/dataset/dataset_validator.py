from pathlib import Path


class DatasetValidator:
    def __init__(self, dataset_root):
        self.dataset_root = Path(dataset_root)

    def validate(self):
        required_dirs = [
            "ASVspoof2019_LA_train/flac",
            "ASVspoof2019_LA_dev/flac",
            "ASVspoof2019_LA_eval/flac",
        ]

        required_protocols = [
            "ASVspoof2019.LA.cm.train.trn.txt",
            "ASVspoof2019.LA.cm.dev.trl.txt",
            "ASVspoof2019.LA.cm.eval.trl.txt",
        ]

        missing = []

        for folder in required_dirs:
            if not (self.dataset_root / folder).exists():
                missing.append(folder)

        for protocol in required_protocols:
            if not (self.dataset_root / protocol).exists():
                missing.append(protocol)

        return {
            "valid": len(missing) == 0,
            "missing": missing
        }


if __name__ == "__main__":
    validator = DatasetValidator("data/ASVspoof2019_LA")
    print(validator.validate())
