import logging
import os


class TrainingLogger:
    def __init__(self, log_dir="logs"):
        os.makedirs(log_dir, exist_ok=True)

        self.logger = logging.getLogger("training")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            handler = logging.FileHandler(
                os.path.join(log_dir, "training.log")
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log_epoch(self, epoch, loss, accuracy):
        self.logger.info(
            f"Epoch={epoch} Loss={loss:.4f} Accuracy={accuracy:.4f}"
        )

    def log(self, message):
        self.logger.info(message)
