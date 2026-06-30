from pathlib import Path

import joblib

from src.logger import logger
from src.train import build_and_train_model

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"


def load_model():
    """
    Load the trained model.
    If it doesn't exist, train and save one automatically.
    """

    if not MODEL_PATH.exists():
        logger.info("Model not found. Training a new model...")
        return build_and_train_model()

    logger.info("Loading existing model...")
    return joblib.load(MODEL_PATH)
