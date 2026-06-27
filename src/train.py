from sklearn.datasets import fetch_california_housing
import pandas as pd


def load_data():
    housing = fetch_california_housing()
    df = pd.DataFrame(
        housing.data,
        columns=housing.feature_names
    )
    df["HousePrice"] = housing.target

    return df


def create_features_target(df):
    X = df.drop("HousePrice", axis=1)
    y = df["HousePrice"]

    return X, y

from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2, random_state=42):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size = test_size,
        random_state = random_state
    )

    return X_train, X_test, y_train, y_test

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

from sklearn.metrics import mean_absolute_error
def evaluate_model(model, X_test, y_test):

    '''This function is used to evaluate model performance '''

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return mae

import joblib
def save_model(model, model_path= "../models/house_price_model.pkl"):
    '''This function is used to save the model'''
    joblib.dump(model, model_path)

from sklearn.ensemble import RandomForestRegressor
def main():
    df = load_data()
    X, y = create_features_target(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model = train_model(model, X_train, y_train)

    mae = evaluate_model(model, X_test, y_test)

    print(f"MAE: {mae: .3f}")

    save_model(model, "../models/house_price_model.pkl")

if __name__ == "__main__":
    main()

