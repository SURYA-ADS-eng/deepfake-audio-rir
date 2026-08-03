from pathlib import Path


class ProtocolParser:
    def __init__(self, protocol_file):
        self.protocol_file = Path(protocol_file)

    def parse(self):
        samples = []

        with open(self.protocol_file, "r") as file:
            for line in file:
                parts = line.strip().split()

                samples.append({
                    "speaker_id": parts[0],
                    "file_name": parts[1],
                    "attack_id": parts[3],
                    "label": parts[4]
                })

        return samples


if __name__ == "__main__":
    parser = ProtocolParser("ASVspoof2019.LA.cm.train.trn.txt")
    print(parser.parse()[:5])
