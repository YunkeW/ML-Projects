import json
import numpy as np
import os
import joblib


def init():
    global model
    # Load the model from the file specified in the environment variable
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model.pkl")
    model = joblib.load(model_path)


def run(raw_data):
    try:
        # Parse the raw data into a JSON format
        data = json.loads(raw_data)
        # Predict using the model and the input data
        result = model.predict(data["data"])
        # Return the prediction as a JSON string
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
