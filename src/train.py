from pathlib import Path

import joblib
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from src.logger import logger


def load_data():
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df["HousePrice"] = housing.target

    return df


def create_features_target(df):
    X = df.drop("HousePrice", axis=1)
    y = df["HousePrice"]

    return X, y


def split_data(X, y, test_size=0.2, random_state=42):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """This function is used to evaluate model performance"""

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return mae


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Full path to the models folder
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"


def save_model(model):
    """Save the trained model."""

    # Create the models directory if it doesn't exist
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_PATH)


def build_and_train_model():
    """Train a Random Forest model and save it."""

    df = load_data()
    X, y = create_features_target(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model = train_model(model, X_train, y_train)

    mae = evaluate_model(model, X_test, y_test)

    logger.info("Model trained successfully.")
    logger.info(f"Model MAE: {mae:.3f}")

    save_model(model)

    return model


def main():
    build_and_train_model()


if __name__ == "__main__":
    main()
