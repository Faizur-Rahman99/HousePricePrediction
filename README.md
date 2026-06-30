# 🏠 House Price Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?logo=fastapi&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7-F7931E?logo=scikitlearn&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A full-stack Machine Learning web application that predicts California house prices using a **Random Forest Regression** model. The application features a responsive web interface, a FastAPI backend, and is fully deployed on Render.

**Current Version:** v1.0.0
---

## 🌐 Live Demo

### Frontend

https://house-price-predictor-ui-xk1f.onrender.com

### Backend API

https://housepriceprediction-lyyr.onrender.com

### Swagger Documentation

https://housepriceprediction-lyyr.onrender.com/docs

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/frontend.png)

---

### 📈 Prediction Result

![Prediction Result](screenshots/prediction.png)

---

### 📚 API Documentation

![Swagger UI](screenshots/swagger.png)

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Model Performance](#-model-performance)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Running with Docker](#-running-with-docker)
- [Running Tests](#-running-tests)
- [API Endpoints](#-api-endpoints)
- [Example Request](#-example-request)
- [Example Response](#-example-response)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

## 📖 Project Overview

This project predicts California house prices using a Machine Learning model trained on the California Housing Dataset from Scikit-learn.

The backend is built with **FastAPI**, which exposes REST API endpoints for prediction. The frontend is built using **HTML, CSS and vanilla JavaScript**, allowing users to enter housing features and instantly receive a predicted house price.

The project demonstrates an end-to-end Machine Learning workflow including:

- Data loading
- Model training
- Model serialization
- REST API development
- Frontend integration
- Cloud deployment

---

## ✨ Features

- 🤖 Predict California house prices using Random Forest Regression
- 🌐 Responsive frontend built with HTML, CSS and JavaScript
- ⚡ REST API built with FastAPI
- ✅ Input validation using Pydantic
- 📄 Interactive Swagger API documentation
- 🛡️ Error handling and structured logging
- 💾 Automatic model loading
- ☁️ Fully deployed on Render
- 🔄 Frontend connected to deployed backend API
- 🐳 Docker support
- 🧪 Automated API testing with Pytest
- ⚙️ Continuous Integration with GitHub Actions
- 🎨 Code formatting with Black
- 🔍 Static analysis with Ruff
- 📦 Import sorting with isort

---

## 🏗️ System Architecture

```
                User
                  │
                  ▼
      HTML / CSS / JavaScript
             (Frontend)
                  │
          POST /predict
                  │
                  ▼
           FastAPI Backend
                  │
                  ▼
     Random Forest Regressor
                  │
                  ▼
        Predicted House Price
                  │
                  ▼
         Displayed on Frontend
```

---

## 🧠 Machine Learning Pipeline

```
California Housing Dataset
            │
            ▼
      Data Preparation
            │
            ▼
     Train/Test Split
            │
            ▼
Random Forest Regressor
            │
            ▼
      Model Evaluation
            │
            ▼
   Save Model (Joblib)
            │
            ▼
     FastAPI Prediction API
            │
            ▼
      Frontend Application
```

---

## 🛠️ Technology Stack

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Frontend

- HTML5
- CSS3
- JavaScript

### Testing

- Pytest

### DevOps & Code Quality

- Docker
- GitHub Actions
- Pytest
- Black
- Ruff
- isort
- pre-commit

### Deployment

- Render

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
HousePricePrediction/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── data/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│
├── screenshots/
│   ├── frontend.png
│   ├── prediction.png
│   └── swagger.png
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
├── tests/
│   ├── test_health.py
│   ├── test_home.py
│   └── test_predict.py
│
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── render.yaml
├── requirements.txt
├── runtime.txt
├── LICENSE
└── README.md
```

---

## 📊 Dataset

The project uses the **California Housing Dataset** provided by Scikit-learn.

### Features

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

### Target

Median House Value

---

## 📈 Model Performance

### Model

Random Forest Regressor

### Evaluation Metric

Mean Absolute Error (MAE)

### Result

```
MAE ≈ 0.328
```

The model predicts California house prices with an average absolute error of approximately 0.328 in the dataset's target units. Lower MAE indicates better prediction accuracy.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Faizur-Rahman99/HousePricePrediction.git
```

Move into the project directory

```bash
cd HousePricePrediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Start the FastAPI server

```bash
uvicorn src.api:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

To run the frontend locally

```bash
cd frontend
python -m http.server 8000
```

Open

```
http://localhost:8000
```
## 🐳 Running with Docker

Build the image:

```bash
docker compose build
```

Run the application:

```bash
docker compose up
```

The API will be available at:

```
http://localhost:8000
```

## 🧪 Running Tests

Run the test suite:

```bash
pytest
```

Format code:

```bash
black .
```

Sort imports:

```bash
isort .
```

Lint the project:

```bash
ruff check .
```
---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home endpoint |
| GET | /health | Health check |
| POST | /predict | Predict house price |

---

## 📤 Example Request

```json
{
  "MedInc": 8.5,
  "HouseAge": 35,
  "AveRooms": 6.2,
  "AveBedrms": 1.1,
  "Population": 1200,
  "AveOccup": 3.2,
  "Latitude": 34.05,
  "Longitude": -118.25
}
```

---

## 📥 Example Response

```json
{
  "predicted_price": 4.82,
  "currency": "USD",
  "unit": "Hundreds of thousands of dollars",
  "model": "Random Forest Regressor"
}
```

---

## 🎯 Future Improvements

- [ ] User authentication
- [ ] Database integration
- [ ] Model versioning
- [ ] Explainable AI (SHAP)
- [ ] Multiple ML model comparison
- [ ] Interactive prediction visualizations
- [ ] Dark mode
- [ ] Kubernetes deployment
- [ ] Automated model retraining pipeline
---

## 👨‍💻 Author

**Faizur Rahman**

GitHub: https://github.com/Faizur-Rahman99

LinkedIn: *www.linkedin.com/in/faizur-rahman99*

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.