from flask.templating import render_template
from werkzeug.utils import redirect
from app import app
from flask import (
    jsonify,
    request,
    make_response,
    redirect
)
import os
import pandas as pd
import numpy as np
from app.models.streptococcus_regression import StreptococcusRegression
from app.models.lactobacillus_regression import LactobacillusRegression
import time


@app.route("/strep", methods=["GET", "POST"])
def strep_pred():
    dataset = pd.read_csv("data/data_regression_set.csv")
    user_ip = request.remote_addr

    response = make_response(redirect("/test"))
    # return response

    if request.method == "GET":

        return jsonify({
            "message": "your ip address: {}".format(user_ip),
            "columns": [x for x in dataset.columns]
        })
    else:
        streptococcus_metrics = StreptococcusRegression(path="data/beta_dataset.csv")
        strep_model = streptococcus_metrics.model_prediction(minimum_milk_proteins=2.591,
                                                            titratable_acidity=0.992,
                                                            pH_milk_sour=4.415,
                                                            fat_milk_over_100mg_=3.1925,
                                                            target_data=4.106)
        return jsonify({
            "message": "your ip address: {}".format(user_ip),
            "columns": [x for x in range(0,10)],
            "prediction": strep_model["prediction_range"],
            "mean_absolute_error": strep_model["mean_absolute_error"] })



@app.route("/lact", methods=["GET", "POST"])
def lact_pred():
    time_1 = time.time()
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
        time_2 = time.time()
        print(time_2 - time_1)
        return jsonify({
            "columns": [x for x in range(0,10)],
            "prediction": prediction})





@app.route("/neuron", methods=["GET", "POST"])
def neuron_test():
    return "Something"


@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({
        "data": [x for x in range(1, 10)]
    })
