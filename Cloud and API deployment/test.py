import requests
import json

# Endpoint URL
endpoint_url = (
    "http://36a5791e-a8eb-4def-92ae-c7386ce2e998.eastus2.azurecontainer.io/score"
)

# Example input data that matches the input schema expected by the model
input_data = json.dumps(
    {
        "data": [
            [
                8,
                41,
                7,
                1,
                500,
                2.5,
                37.88,
                -122.23,
            ]  # replace with actual feature values
        ]
    }
)

# Set the content type
headers = {"Content-Type": "application/json"}

# Make the request and display the response
response = requests.post(endpoint_url, data=input_data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Request failed: {response.status_code}, {response.text}")
