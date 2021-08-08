from app import app
from flask import (
    jsonify,
    request,
    make_response,
    redirect
)
import pandas as pd
from app.models.streptococcus_regression import (
    list_strep_predictions,
    single_strep_predictions
)
from app.models.lactobacillus_regression import (
    single_lact_predictions,
    list_lact_predictions
)
from app.models.neuron_classification import (
    measure_single_predictions,
    measure_list_predictions
)

import unittest
import numpy as np

"""In every GET petitions the data trained and 
    the history metrics will be sent"""


@app.cli.command()
def tst():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.route("/bacteria_growth", methods=["GET"])
def bacteria_growth():
    bacteria_data = pd.read_csv("data/growth_curve.csv")
    return jsonify({
        "data": {
            "message": "Something",
            "growth_time": bacteria_data["time"].to_list(),
            "growth_log": bacteria_data["growth_log"].to_list()
        }
    })


"""
Neuron Regression
"""


@app.route("/strep", methods=["GET", "POST"])
def strep_pred():
    strep_model = single_strep_predictions(
        values_list=[2.591, 0.992, 4.415, 3.1925], target_data=4.106)
    if request.method == "POST":
        return jsonify({
            "data": {
                "message": "request successfully",
                "prediction": strep_model["prediction_range"],
                "mean_absolute_error": strep_model["mean_absolute_error"]
            }
        })
    elif request.method == "GET":
        return jsonify({
            "data": {
                "message": "request successfully",
                "mean_absolute_error": strep_model["mean_absolute_error"]
            }
        })


@app.route("/lact", methods=["GET", "POST"])
def lact_pred():
    lact_model = single_lact_predictions(
        values_list=[2.591, 0.992, 4.415, 3.1925], target_data=5.196)
    if request.method == "POST":
        return jsonify({
            "data": {
                "message": "request successfully",
                "prediction": lact_model["prediction_range"],
                "mean_absolute_error": lact_model["mean_absolute_error"]
            }
        })
    elif request.method == "GET":
        return jsonify({
            "data": {
                "message": "request successfully",
                "mean_absolute_error": lact_model["mean_absolute_error"]
            }
        })


"""
Big predictions, for plotting
"""


@app.route("/list_strep", methods=["GET", "POST"])
def list_strep_pred():
    if request.method == "POST":
        list_pred = request.json["strep_values"]
        list_target = request.json["strep_target"]
        values_predicted = list_strep_predictions(list_pred, list_target)
        return jsonify({
            "data": values_predicted
        })
    elif request.method == "GET":
        response = make_response(redirect("/bacteria_growth"))
        return response


@app.route("/list_lact", methods=["GET", "POST"])
def list_lact_pred():
    if request.method == "POST":
        list_predict = request.json["lact_values"]
        list_target = request.json["lact_target"]
        values_predicted = list_lact_predictions(list_predict, list_target)
        return jsonify({
            "data": values_predicted
        })
    elif request.method == "GET":
        response = make_response(redirect("/bacteria_growth"))
        return response


"""
Neuron classification
"""


@app.route("/classification_single", methods=["GET", "POST"])
def classification_single():
    """In this endpoint the goal is sent a single values"""

    if request.method == "POST":
        features_data = np.array(request.json["classification_data"]).reshape(1, -1)
        # target_data = np.array(request.json["target_data"])
        model_class = measure_single_predictions(features_data)
        return jsonify({
            "message": "successfully",
            "status_code": 200,
            "predictions": model_class
        })
    elif request.method == "GET":
        return jsonify({
            "data": measure_single_predictions()
        })


@app.route("/classification_multiple", methods=["GET", "POST"])
def classification_multiple():
    if request.method == "POST":
        features_data = request.json["classification_data"]
        target_data = request.json["predictions"]

        model_class = measure_list_predictions(features_value=features_data, targets_value=target_data)
        return jsonify({
            "message": "successfully",
            "status_code": 200,
            "predictions": model_class
        })
    elif request.method == "GET":
        return jsonify({
            "message": "successfully",
            "status_code": 200,
            "predictions": measure_list_predictions()
        })
