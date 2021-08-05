from app import app
from flask import (
    jsonify,
    request
)
import pandas as pd
from app.models.streptococcus_regression import (
    StreptococcusRegression,
    make_predictions
)
from app.models.lactobacillus_regression import LactobacillusRegression

STREPTOCOCCUS_METRICS = StreptococcusRegression(path="data/beta_dataset.csv")


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Working!!",
        "status_code": 200
    })


# For specific predictions
@app.route("/strep", methods=["GET", "POST"])
def strep_pred():
    dataset = pd.read_csv("data/data_regression_set.csv")
    user_ip = request.remote_addr

    if request.method == "GET":

        return jsonify({
            "message": "your ip address: {}".format(user_ip),
            "columns": [x for x in dataset.columns]
        })
    else:
        strep_model = STREPTOCOCCUS_METRICS.model_prediction(values_list=[2.591, 0.992, 4.415, 3.1925], target_data=4.106)
        return jsonify({
            "message": "your ip address: {}".format(user_ip),
            "prediction": strep_model["prediction_range"],
            "mean_absolute_error": strep_model["mean_absolute_error"]})


@app.route("/list_strep", methods=["GET", "POST"])
def list_strep_pred():
    if request.method == "POST":
        list_pred = request.json["strep_values"]
        list_target = request.json["strep_target"]
        values_predicted = make_predictions(list_pred, list_target)
        return jsonify(values_predicted)
    else:
        return jsonify({
            "message": "you will be redirect to another page!!"
        })


@app.route("/lact", methods=["GET", "POST"])
def lact_pred():
    dataset = pd.read_csv("data/data_regression_set.csv")
    # return response

    if request.method == "GET":

        return jsonify({
            "message": "your ip address 127.0.0.1",
            "columns": [x for x in dataset.columns]
        })
    else:
        lactobacillus_metrics = LactobacillusRegression(path="data/beta_dataset.csv")
        prediction = lactobacillus_metrics.model_prediction(minimum_milk_proteins=2.591,
                                                            titratable_acidity=0.992,
                                                            pH_milk_sour=4.415,
                                                            fat_milk_over_100mg_=3.1925,
                                                            target_data=5.196)
        return jsonify({
            "columns": [x for x in range(0, 10)],
            "prediction": prediction})


@app.route("/neuron", methods=["GET", "POST"])
def neuron_test():
    return "Something"


@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({
        "data": [x for x in range(1, 10)]
    })
