import torch
from torch.utils.data import DataLoader

from app.models.ast_model import ASTModel
from app.dataset.ast_dataset import ASTDataset


def train():
    print("Initializing AST training pipeline...")

    dataset = ASTDataset(samples=[])

    dataloader = DataLoader(
        dataset,
        batch_size=8,
        shuffle=True
    )

    ast = ASTModel()

    model = ast.get_model()

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=1e-5
    )

    print("Training pipeline initialized successfully.")
    print(f"Total batches: {len(dataloader)}")


if __name__ == "__main__":
    train()
