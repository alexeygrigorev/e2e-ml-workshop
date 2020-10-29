import pickle
import numpy as np
import pandas as pd

from flask import Flask, request, jsonify


with open('price-model.bin', 'rb') as f_in:
    lr = pickle.load(f_in)


app = Flask('carprice')

base = ['engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg']

def prepare_X(df):
    df = df.copy()
    features = base.copy()

    df['age'] = 2017 - df.year
    features.append('age')

    df_num = df[features]
    df_num = df_num.fillna(0)
    X = df_num.values

    return X


def predict_single(car, lr):
    X_test = prepare_X(pd.DataFrame([car]))
    y_pred = lr.predict(X_test)[0]
    return np.expm1(y_pred).round(2)


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