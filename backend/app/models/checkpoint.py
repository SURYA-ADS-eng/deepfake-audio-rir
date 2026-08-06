import os
import torch


class ModelCheckpoint:
    def __init__(self, save_dir="models"):
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def save(self, model, optimizer, epoch, path="deepfake_ast_model.pth"):
        checkpoint = {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
        }

        torch.save(
            checkpoint,
            os.path.join(self.save_dir, path)
        )

    def load(self, model, optimizer, path="deepfake_ast_model.pth"):
        checkpoint = torch.load(
            os.path.join(self.save_dir, path),
            map_location="cpu"
        )

        model.load_state_dict(checkpoint["model_state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

        return checkpoint["epoch"]
