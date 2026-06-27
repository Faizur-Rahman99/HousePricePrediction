import pandas as pd

def prepare_input(features):

    input_data = pd.DataFrame([{
        "MedInc": features.MedInc,
        "HouseAge": features.HouseAge,
        "AveRooms": features.AveRooms,
        "AveBedrms": features.AveBedrms,
        "Population": features.Population,
        "AveOccup": features.AveOccup,
        "Latitude": features.Latitude,
        "Longitude": features.Longitude
    }])

    return input_data


def predict_price(model, features):

    input_data = prepare_input(features)

    prediction = model.predict(input_data)

    return float(prediction[0])