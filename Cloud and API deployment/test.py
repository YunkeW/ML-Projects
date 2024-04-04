import requests
import json

# The endpoint URL provided for the deployed service
endpoint_url = (
    "http://36a5791e-a8eb-4def-92ae-c7386ce2e998.eastus2.azurecontainer.io/score"
)

data = {"data": [[8, 40, 7, 1, 500, 2.5, 37.85, -122.23]]}

# Convert to JSON string
input_data = json.dumps(data)

# Set the content type
headers = {"Content-Type": "application/json"}

# Send the POST request to the endpoint
response = requests.post(endpoint_url, data=input_data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Request failed: {response.status_code}, {response.text}")
