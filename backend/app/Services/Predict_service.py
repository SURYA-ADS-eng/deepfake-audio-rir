import numpy as np

from app.preprocessing.extract_features import FeatureExtractor


class PredictionService:
    def __init__(self):
        self.feature_extractor = FeatureExtractor()

    def load_model(self):
        """
        Placeholder for loading the trained model.
        Replace with actual PyTorch model loading.
        """
        self.model = None

    def predict(self, audio_path):
        """
        Extract features and return a prediction.
        """

        features = self.feature_extractor.extract(audio_path)

        # TODO: Replace this dummy prediction with model inference
        confidence = np.random.uniform(0.75, 0.99)

        prediction = (
            "Fake"
            if confidence > 0.5
            else "Real"
        )

        return {
            "prediction": prediction,
            "confidence": round(float(confidence), 4),
            "features": features
        }


if __name__ == "__main__":
    service = PredictionService()
    service.load_model()

    result = service.predict("sample.wav")

    print(result)
