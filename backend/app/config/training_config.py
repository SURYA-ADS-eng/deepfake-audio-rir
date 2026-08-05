class TrainingConfig:
    # Dataset
    TRAIN_BATCH_SIZE = 16
    VALID_BATCH_SIZE = 16

    # Training
    EPOCHS = 20
    LEARNING_RATE = 1e-4
    WEIGHT_DECAY = 1e-5

    # Audio
    SAMPLE_RATE = 16000
    N_MELS = 128

    # Model
    MODEL_NAME = "Audio Spectrogram Transformer"

    # Output
    MODEL_SAVE_PATH = "models/deepfake_ast_model.pth"
