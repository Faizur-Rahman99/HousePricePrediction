# 🏠 House Price Prediction

A full-stack Machine Learning web application that predicts California house prices using a **Random Forest Regression** model. The application features a responsive web interface, a FastAPI backend, and is fully deployed on Render.

---

# 🌐 Live Demo

### Frontend

https://house-price-predictor-ui-xk1f.onrender.com

### Backend API

https://housepriceprediction-lyyr.onrender.com

### Interactive API Documentation

https://housepriceprediction-lyyr.onrender.com/docs

---

# 📸 Screenshots

## 🏠 Home Page

![Home Page](screenshots/frontend.png)

---

## 📈 Prediction Result

![Prediction Result](screenshots/prediction.png)

---

## 📚 API Documentation (Swagger UI)

![Swagger UI](screenshots/swagger.png)


# 📖 Project Overview

This project predicts California house prices based on eight housing characteristics from the California Housing Dataset.

Users can either:

* Use the interactive web application
* Send requests directly to the REST API

The machine learning model is trained using Scikit-learn and served through FastAPI.

---

# ✨ Features

* End-to-end Machine Learning application
* Random Forest Regression model
* FastAPI REST API
* Interactive web interface
* Frontend validation
* Backend validation using Pydantic
* Structured logging
* Error handling
* Interactive Swagger documentation
* Fully deployed frontend and backend on Render

---

# 🛠 Tech Stack

## Machine Learning

* Python
* Scikit-learn
* Pandas
* NumPy
* Joblib

## Backend

* FastAPI
* Pydantic
* Uvicorn

## Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

## Deployment

* Git
* GitHub
* Render

---

# 📂 Project Structure

```text
HousePricePrediction/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── house_price_model.pkl
│
├── src/
│   ├── api.py
│   ├── logger.py
│   ├── model_loader.py
│   ├── predict.py
│   ├── schemas.py
│   ├── train.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

This project uses the **California Housing Dataset** provided by Scikit-learn.

## Features

* Median Income
* House Age
* Average Rooms
* Average Bedrooms
* Population
* Average Occupancy
* Latitude
* Longitude

## Target

* Median House Value

---

# 🏗 System Architecture

```text
                 Browser
                     │
                     ▼
      HTML / CSS / JavaScript Frontend
                     │
             Fetch API Request
                     │
                     ▼
          FastAPI Backend (Render)
                     │
          Pydantic Validation
                     │
        Random Forest Regression
                     │
                     ▼
             Predicted House Price
                     │
                     ▼
                 Browser
```

---

# 🤖 Machine Learning Workflow

1. Load California Housing Dataset
2. Prepare features and target
3. Split training and testing data
4. Train Random Forest Regression model
5. Evaluate using Mean Absolute Error (MAE)
6. Save trained model with Joblib
7. Load model through FastAPI
8. Serve predictions through REST API

---

# 📡 API Endpoint

## POST /predict

Predicts the price of a California house.

### Example Request

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

### Example Response

```json
{
  "predicted_price": 4.73,
  "currency": "USD",
  "unit": "Hundreds of thousands of dollars",
  "model": "Random Forest Regressor"
}
```

---

# ⚙️ Running the Project Locally

## Clone the repository

```bash
git clone https://github.com/Faizur-Rahman99/HousePricePrediction.git
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the backend

```bash
uvicorn src.api:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run the frontend

```bash
cd frontend
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

---

# 🚀 Deployment

The project is deployed using **Render**.

* Frontend: Static Site
* Backend: FastAPI Web Service

---

# 📈 Future Improvements

* Docker support
* Automated testing with Pytest
* GitHub Actions CI/CD
* Improved mobile responsiveness
* Prediction history
* Feature importance visualization
* Support for additional machine learning models

---

# 👨‍💻 Author

**Faizur Rahman**

Built as a portfolio project to demonstrate Machine Learning, FastAPI, frontend development, REST APIs, and cloud deployment.
