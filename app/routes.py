from app import app
from flask import (
    jsonify,
    request
)
import pandas as pd
from app.models.streptococcus_regression import (
    StreptococcusRegression,
    make_strep_predictions
)
from app.models.lactobacillus_regression import (
    LactobacillusRegression,
    make_lact_predictions
)

STREPTOCOCCUS_METRICS = StreptococcusRegression(path="data/beta_dataset.csv")
LACTOBACILLUS_METRICS = LactobacillusRegression(path="data/beta_dataset.csv")


"""
Individuals predictions
"""
@app.route("/strep", methods=["GET", "POST"])
def strep_pred():

    if request.method == "POST":
        strep_model = STREPTOCOCCUS_METRICS.model_prediction(values_list=[2.591, 0.992, 4.415, 3.1925], target_data=4.106)
        return jsonify({
            "message": "request successfully",
            "prediction": strep_model["prediction_range"],
            "mean_absolute_error": strep_model["mean_absolute_error"]})
        

@app.route("/lact", methods=["GET", "POST"])
def lact_pred():

    if request.method == "POST":
        lact_model = LACTOBACILLUS_METRICS.model_prediction(values_list=[2.591, 0.992, 4.415, 3.1925], target_data=5.196)
        return jsonify({
            "message": "request successfully",
            "prediction": lact_model["prediction_range"],
            "mean_absolute_error": lact_model["mean_absolute_error"]})

        

"""
Big predictions, for ploting
"""


@app.route("/list_strep", methods=["GET", "POST"])
def list_strep_pred():
    if request.method == "POST":
        list_pred = request.json["strep_values"]
        list_target = request.json["strep_target"]
        values_predicted = make_strep_predictions(list_pred, list_target)
        return jsonify(values_predicted)
    else:
        return jsonify({
            "message": "you will be redirect to another page!!"
        })


@app.route("/list_lact", methods=["GET", "POST"])
def list_lact_pred():
    if request.method == "POST":
        list_predict = request.json["lact_values"]
        list_target = request.json["strep_target"]
        values_predicted = make_lact_predictions(list_predict, list_target)
        return jsonify(values_predicted)
    else:
        return jsonify({
            "message": "you suck!!",
            "status_code": 404
        })



