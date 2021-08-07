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
from app.models.neuron_classification import NeuronClassification

import unittest
import numpy as np


@app.cli.command()
def tst():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)



@app.run("/", methods=["GET"])
def index():

    return jsonify({
        
    })


@app.run("/bacteria_growth", methods=["GET"])
def bacteria_growth():

    bacteria_data = pd.read_csv("train/growth_curve.csv")



"""
Neuron Regression
"""


@app.route("/strep", methods=["GET", "POST"])
def strep_pred():
    streptococcus_metrics = StreptococcusRegression(
        path="data/beta_dataset.csv")
    if request.method == "POST":
        strep_model = streptococcus_metrics.model_prediction(
            values_list=[2.591, 0.992, 4.415, 3.1925], target_data=4.106)
        return jsonify({
            "data": {
                "message": "request successfully",
                "prediction": strep_model["prediction_range"],
                "mean_absolute_error": strep_model["mean_absolute_error"]
            }
        })


@app.route("/lact", methods=["GET", "POST"])
def lact_pred():
    lactobacillus_metrics = LactobacillusRegression(
        path="data/beta_dataset.csv")
    if request.method == "POST":
        lact_model = lactobacillus_metrics.model_prediction(
            values_list=[2.591, 0.992, 4.415, 3.1925], target_data=5.196)
        return jsonify({
            "data": {
                "message": "request successfully",
                "prediction": lact_model["prediction_range"],
                "mean_absolute_error": lact_model["mean_absolute_error"]
            }
        })


"""
Big predictions, for ploting
"""


@app.route("/list_strep", methods=["GET", "POST"])
def list_strep_pred():
    if request.method == "POST":
        list_pred = request.json["strep_values"]
        list_target = request.json["strep_target"]
        values_predicted = make_strep_predictions(list_pred, list_target)
        return jsonify({
            "data": values_predicted
        })
    else:
        return jsonify({
            "message": "you will be redirect to another page!!"
        })


@app.route("/list_lact", methods=["GET", "POST"])
def list_lact_pred():
    if request.method == "POST":
        list_predict = request.json["lact_values"]
        list_target = request.json["lact_target"]
        values_predicted = make_lact_predictions(list_predict, list_target)
        return jsonify({
            "data": values_predicted
        })
    else:
        return jsonify({
            "message": "you suck!!",
            "status_code": 404
        })


"""
Neuron classification
"""


@app.route("/classification", methods=["GET", "POST"])
def classification():

    model_class = NeuronClassification(file_path="train/classification_data.csv",
                                       epochs_number=1000,
                                       input_shape_val=9,
                                       output_shape_val=3)

    if request.method == "POST":
        features_data = request.json["features_data"]
        target_data = request.json["target_data"]
    else:
        pass


"""
{
    "strep_values": [[2.591, 0.992, 4.415, 3.1925], [2.591, 0.992, 4.415, 3.1925], [2.591, 0.992, 4.415, 3.1925], [2.591, 0.992, 4.415, 3.1925]],
    "strep_target": [4.106, 4.106, 4.106, 4.106]
}

{
    "lact_values": [[2.591, 0.992, 4.415, 3.1925], [2.591, 0.992, 4.415, 3.1925], [2.591, 0.992, 4.415, 3.1925], [2.591, 0.992, 4.415, 3.1925]],
    "lact_target": [4.106, 4.106, 4.106, 4.106]
}


# Lactobacillus testing

{
    "strep_values":[
        [2.654,1.015,4.488,1.0795]
        [2.65,1.096,4.459,2.444]
        [2.502,1.156,4.555,1.4788]
        [2.51,0.995,4.496,2.3514]
        [2.643,1.034,4.495,3.0312]
        [2.624,0.988,4.595,3.3141]
        [2.414,1.097,4.556,1.8533]
        [2.659,0.964,4.412,1.8671]
        [2.602,1.15,4.431,3.8777]
        [2.591,0.992,4.415,3.1925]
        [2.576,1.048,4.544,3.9445]]
    ,
    "strep_target":[4.833, 5.562, 4.466, 4.195, 4.688, 4.071, 4.889, 4.539, 5.245, 5.196, 4.194]
}

 

# Streptococcus testing
5.769,41.125,2.419,1.081,4.584,1.336
5.795,40.105,2.699,1.158,4.405,1.2108
4.936,40.463,2.405,1.121,4.501,2.5337
5.315,40.989,2.595,1.127,4.593,3.0811
5.95,,40.756,2.668,0.962,4.587,2.0685
4.314,41.549,2.64,0.975,4.597,3.7364
4.598,41.707,2.676,0.972,4.429,1.1644
5.078,41.547,2.519,1.022,4.568,1.429
5.301,41.254,2.552,1.024,4.527,3.7457
4.608,40.602,2.564,1.155,4.511,1.9436
5.591,40.761,2.434,1.112,4.554,3.3364
5.302,41.646,2.629,1.012,4.405,2.0494
4.457,41.61,2.658,1.007,4.446,1.0637




"""
