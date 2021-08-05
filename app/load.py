#!/usr/bin/python3

import time
from app.models.streptococcus_regression import StreptococcusRegression


time_1 = time.time()


def print_arguments(**kwargs):
    print(kwargs["element"])
    # print(kwargs.element)
    print(type(kwargs))

def make_prediction():
    streptococcus_metrics = StreptococcusRegression(path="data/beta_dataset.csv")
    print(streptococcus_metrics.model_prediction(minimum_milk_proteins=2.591,
                                                titratable_acidity=0.992, pH_milk_sour=4.415,
                                                fat_milk_over_100mg_=3.1925,
                                                target_data=4.106))
time_2 = time.time()

print(time_2 - time_1)
