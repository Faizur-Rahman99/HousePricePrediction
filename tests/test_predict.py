from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


def test_predict_valid():
    payload = {
        "MedInc": 8.5,
        "HouseAge": 35,
        "AveRooms": 6.2,
        "AveBedrms": 1.1,
        "Population": 1200,
        "AveOccup": 3.2,
        "Latitude": 34.05,
        "Longitude": -118.25,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "predicted_price" in data
    assert "currency" in data
    assert "unit" in data
    assert "model" in data


def test_predict_missing_field():
    payload = {
        "MedInc": 8.5,
        "HouseAge": 35,
        "AveRooms": 6.2,
        "AveBedrms": 1.1,
        "Population": 1200,
        "AveOccup": 3.2,
        "Latitude": 34.05,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_invalid_datatype():
    payload = {
        "MedInc": "abc",
        "HouseAge": 35,
        "AveRooms": 6.2,
        "AveBedrms": 1.1,
        "Population": 1200,
        "AveOccup": 3.2,
        "Latitude": 34.05,
        "Longitude": -118.25,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_invalid_latitude():
    payload = {
        "MedInc": 8.5,
        "HouseAge": 35,
        "AveRooms": 6.2,
        "AveBedrms": 1.1,
        "Population": 1200,
        "AveOccup": 3.2,
        "Latitude": 120,
        "Longitude": -118.25,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
