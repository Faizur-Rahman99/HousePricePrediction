from pathlib import Path
import joblib

# Get the project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Build the full path to the model
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"


def load_model():
    """Load the trained model."""
    return joblib.load(MODEL_PATH)