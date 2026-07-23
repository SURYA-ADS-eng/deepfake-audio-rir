import os
import torch


class ModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        self.model = torch.load(
            self.model_path,
            map_location=torch.device("cpu")
        )

        self.model.eval()
        return self.model

    def get_model(self):
        if self.model is None:
            self.load()

        return self.model
