from fastapi import FastAPI

from src.schemas import HouseFeatures
from src.model_loader import load_model
from src.predict import predict_price

app = FastAPI(
    title="House Price Prediction API",
    description="Predict California house prices using a Random Forest model.",
    version="1.0.0"
)

model = load_model()


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running!"
    }


@app.post(
    "/predict",
    summary="Predict House Price",
    description="Predict the price of a California house based on housing features."
)
def predict(features: HouseFeatures):

    predicted_price = predict_price(model, features)

    return {
        "predicted_price": round(predicted_price, 2),
        "currency": "USD",
        "unit": "Hundreds of thousands of dollars",
        "model": "Random Forest Regressor"
    }