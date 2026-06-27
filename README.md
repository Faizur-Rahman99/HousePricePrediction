# 🏠 House Price Prediction API

An end-to-end Machine Learning project that predicts California house prices using a Random Forest Regressor and serves predictions through a FastAPI REST API.

## 🚀 Features

- Predict house prices using 8 housing features
- REST API built with FastAPI
- Automatic request validation using Pydantic
- Trained Random Forest model
- Modular project structure
- Interactive API documentation with Swagger UI

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- Pydantic
- Joblib
- Uvicorn

---

## 📂 Project Structure

```
HousePricePrediction/
│
├── data/
├── models/
├── notebooks/
├── screenshots/
├── src/
│   ├── api.py
│   ├── train.py
│   ├── predict.py
│   ├── schemas.py
│   ├── model_loader.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

California Housing Dataset from Scikit-learn.

Features:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

Target:

- Median House Value

---

## 🤖 Machine Learning Workflow

1. Load Dataset
2. Explore Data
3. Create Features and Target
4. Train/Test Split
5. Train Random Forest Model
6. Evaluate using MAE
7. Save Model using Joblib
8. Serve Model through FastAPI

---

## ▶ Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn src.api:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## 📈 Example Request

```json
{
  "MedInc": 8.3,
  "HouseAge": 60,
  "AveRooms": 5.5,
  "AveBedrms": 1.0,
  "Population": 1000,
  "AveOccup": 2.5,
  "Latitude": 34.2,
  "Longitude": -118.4
}
```

---

## 📌 Future Improvements

- Deploy on Render
- Build a frontend
- Add Docker support
- Add unit tests
- Add CI/CD pipeline