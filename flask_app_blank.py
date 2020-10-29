import pickle
import numpy as np
import pandas as pd

from flask import Flask, request, jsonify


# load the model

# code for prepare_X
# predict_single - wrapper


def predict_single(car, lr):
    return 0.0

app = Flask('carprice')


@app.route('/predict', methods=['POST'])
def predict():
    car = request.get_json()
    print(car)

    prediction = predict_single(car, lr)

    result = {
        'predict': float(prediction),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)