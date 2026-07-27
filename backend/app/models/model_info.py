import os
from datetime import datetime


class ModelInfo:

    def __init__(self, model_path):
        self.model_path = model_path

    def get_info(self):
        if not os.path.exists(self.model_path):
            return {
                "exists": False,
                "message": "Model not found."
            }

        return {
            "exists": True,
            "model_path": self.model_path,
            "size_kb": round(os.path.getsize(self.model_path) / 1024, 2),
            "last_modified": datetime.fromtimestamp(
                os.path.getmtime(self.model_path)
            ).isoformat()
        }


if __name__ == "__main__":
    info = ModelInfo("models/deepfake_model.pth")
    print(info.get_info())
