import os

BASE_DATASET = "data/ASVspoof2019_LA"

TRAIN_AUDIO = os.path.join(
    BASE_DATASET,
    "ASVspoof2019_LA_train",
    "flac"
)

DEV_AUDIO = os.path.join(
    BASE_DATASET,
    "ASVspoof2019_LA_dev",
    "flac"
)

EVAL_AUDIO = os.path.join(
    BASE_DATASET,
    "ASVspoof2019_LA_eval",
    "flac"
)

TRAIN_PROTOCOL = os.path.join(
    BASE_DATASET,
    "ASVspoof2019.LA.cm.train.trn.txt"
)

DEV_PROTOCOL = os.path.join(
    BASE_DATASET,
    "ASVspoof2019.LA.cm.dev.trl.txt"
)

EVAL_PROTOCOL = os.path.join(
    BASE_DATASET,
    "ASVspoof2019.LA.cm.eval.trl.txt"
)
