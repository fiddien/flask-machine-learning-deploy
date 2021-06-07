import json
import joblib
import numpy as np
from flask import Flask, request

app = Flask(__name__)

recommender_dnn = joblib.load("iris_decision_tree.joblib")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/predict", methods=["POST"])
def predict():
    request_json = request.json
    print("data: {}".format(request_json))
    print("type: {}".format(type(request_json)))
		input = request_json.get('data')
		input = [np.array(x) for x in input]
    prediction = recommender_dnn.predict(input)
    prediction_string = [str(d) for d in prediction]
    response_json = {
        "data" : request_json.get("data"),
        "prediction" : list(prediction_string)
    }

    return json.dumps(response_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
