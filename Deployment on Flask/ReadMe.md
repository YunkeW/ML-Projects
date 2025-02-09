# Deployment on Flask

## Overview
This project demonstrates how to deploy a machine learning model using Flask. The model predicts California housing prices based on input features. The Flask application provides an API endpoint for making predictions.

## Files
- `app.py`: The main Flask application that loads the trained model and provides a REST API for predictions.
- `model.pkl`: The trained Gradient Boosting Regressor model serialized using `joblib`.
- `Deployment_on_Flask.ipynb`: Jupyter Notebook detailing the steps of model training and deployment.
- `Deployment_on_Flask.pdf`: Documentation describing the deployment process.

## Requirements
To run this project, install the necessary dependencies:
```bash
pip install flask scikit-learn joblib
```

## Dataset
The model is trained on the **California Housing** dataset, which is included in `sklearn.datasets`.

## Model Training
The model is trained using a **Gradient Boosting Regressor** with the following steps:
1. Load the dataset.
2. Split into training and testing sets.
3. Train a `GradientBoostingRegressor` model.
4. Save the trained model as `model.pkl`.

## Running the Flask App
To start the Flask application, run:
```bash
python app.py
```
By default, the application runs on `http://127.0.0.1:5000/`.

## API Endpoints
### 1. Home Route
- **URL**: `/`
- **Method**: GET
- **Response**: A welcome message.

### 2. Prediction Endpoint
- **URL**: `/predict`
- **Method**: POST
- **Request Format**:
  ```json
  {
      "features": [8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]
  }
  ```
- **Response Format**:
  ```json
  {
      "prediction": [2.345]
  }
  ```

## Testing the API
Use `curl` or Postman to test the API:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]}'
```

## Deployment
For deploying on a cloud service, follow these steps:
1. Ensure `Flask` and dependencies are installed.
2. Use `gunicorn` for production:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
3. Deploy using platforms like **Heroku, AWS, or Google Cloud**.
