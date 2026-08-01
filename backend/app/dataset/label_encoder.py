LABEL_MAP = {
    "bonafide": 0,
    "spoof": 1
}


def encode(label):
    return LABEL_MAP[label]


def decode(label):
    reverse = {0: "bonafide", 1: "spoof"}
    return reverse[label]
