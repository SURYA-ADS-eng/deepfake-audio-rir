import csv
import os
from datetime import datetime


class PredictionHistory:

    def __init__(self, file_path="logs/predictions.csv"):
        self.file_path = file_path

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Timestamp",
                    "Audio File",
                    "Prediction",
                    "Confidence"
                ])

    def save(self, filename, prediction, confidence):
        with open(self.file_path, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                datetime.now(),
                filename,
                prediction,
                confidence
            ])
