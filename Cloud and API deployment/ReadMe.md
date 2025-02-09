# Cloud and API Deployment Project  

## Overview  
This project involves training a machine learning model using the California Housing dataset, saving the trained model, and deploying it as a web service using Azure Machine Learning.  

## Project Structure  
The project consists of the following files:  

- **`app.py`**: Python script for training a `GradientBoostingRegressor` model on the California Housing dataset and saving it as `model.pkl`.  
- **`model.pkl`**: Serialized trained model saved using `joblib`.  
- **`cloud and API deployment.pdf`**: Documentation outlining the cloud deployment process.  

## Steps to Run the Project  

### 1. Train the Model  
To train the model locally, run:  
```bash
python app.py
```
This will:  
- Load the California Housing dataset.  
- Split the dataset into training and testing sets.  
- Train a `GradientBoostingRegressor` model.  
- Save the trained model as `model.pkl`.  

### 2. Set Up Azure Machine Learning  
Follow the steps in `cloud and API deployment.pdf` to:  
- Create an Azure Machine Learning workspace.  
- Upload the trained model to Azure.  
- Deploy the model as a web service.  

### 3. Deploy as an API  
- Use Azure Machine Learning to create and deploy an API endpoint for serving predictions.  
- Test the deployed API with sample requests.  

## Requirements  
To run this project locally, install the required dependencies:  
```bash
pip install scikit-learn joblib
```
