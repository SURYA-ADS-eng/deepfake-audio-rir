import torch
from transformers import ASTForAudioClassification


class ASTModel:
    def __init__(self, model_name="MIT/ast-finetuned-audioset-10-10-0.4593"):
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = ASTForAudioClassification.from_pretrained(
            model_name,
            num_labels=2,
            ignore_mismatched_sizes=True
        ).to(self.device)

    def get_model(self):
        return self.model

    def get_device(self):
        return self.device
