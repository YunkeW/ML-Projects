# create a flask app
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return "Welcome to my ML model API!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data["features"]])
    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    app.run(debug=True)
