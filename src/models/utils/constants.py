HF_MODELS = ["vit", "dinov2"]
SSL_MODEL = "simclr"
ALL_MODEL_TYPES = HF_MODELS.append(SSL_MODEL)
SIMCLR_BACKBONE = "resnet50"
NUM_CLASSES = 8

# Filter constants
FILTERED_CLASSES = ["0", "1"]  # Classes to use after filtering
NUM_FILTERED_CLASSES = len(FILTERED_CLASSES)  # Number of classes after filtering
