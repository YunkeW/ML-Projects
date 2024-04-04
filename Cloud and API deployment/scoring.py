import json
import numpy as np
import os
from sklearn.externals import joblib


# The init() function is called once when the service starts up.
def init():
    global model
    # The AZUREML_MODEL_DIR environment variable indicates
    # a directory containing the model file registered.
    # This is the path to the model registered in Azure ML.
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model.pkl")
    model = joblib.load(model_path)


# The run() function is called each time a request is made to the scoring API.
def run(raw_data):
    try:
        # Receive the data as a JSON string and convert it to a numpy array.
        data = np.array(json.loads(raw_data)["data"])
        # Make prediction.
        result = model.predict(data)
        # You can return any JSON-serializable object.
        return result.tolist()
    except Exception as e:
        error = {"error": str(e)}
        return error
