import torch
import torch.nn as nn


class SimpleAudioClassifier(nn.Module):
    def __init__(self, num_classes: int = 2):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 32 * 32, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        x = self.conv(x)
        x = self.classifier(x)
        return x


def load_model(device: torch.device = torch.device("cpu")) -> nn.Module:
    model = SimpleAudioClassifier(num_classes=2)
    model.to(device)
    model.eval()
    return model


def predict(model: nn.Module, input_tensor: torch.Tensor) -> torch.Tensor:
    with torch.inference_mode():
        logits = model(input_tensor)
        probs = torch.softmax(logits, dim=-1)
    return probs
