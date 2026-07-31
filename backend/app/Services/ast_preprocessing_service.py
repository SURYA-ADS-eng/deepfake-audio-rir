import numpy as np
from app.preprocessing.log_mel_extractor import LogMelExtractor


class ASTPreprocessingService:
    def __init__(self):
        self.extractor = LogMelExtractor()

    def preprocess(self, audio_path):
        """
        Generate Log-Mel Spectrogram for AST input.
        """
        log_mel = self.extractor.extract(audio_path)

        # Normalize values
        log_mel = (log_mel - np.mean(log_mel)) / (np.std(log_mel) + 1e-8)

        return log_mel.astype("float32")
