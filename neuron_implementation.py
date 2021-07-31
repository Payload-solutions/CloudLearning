#!/usr/bin/python3

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras import (
    models,
    layers,
    optimizers
)


datamaster_2 = pd.read_csv("data/data_regression.csv")


def training_model():
    y_strep = datamaster_2["streptococcus_final_cfu_ml"]
    # y_lact = data_master["lactobacillus_initial_strain_cfu_ml"]

    X = datamaster_2.drop(["lactobacillus_initial_strain_cfu_ml","streptococcus_initial_strain_cfu_ml","streptococcus_final_cfu_ml", "lactobacillus_final_cfu_ml", "quality_product", "ideal_temperature_c"], axis=1)

    X_train, X_test, train_labels, test_labels = train_test_split(X, y_strep, test_size=0.3, random_state=42)

    # Reshaping data
    train_data, test_data = X_train.to_numpy(), X_test.to_numpy()

    # Normalizing train data
    mean = train_data.mean(axis = 0)
    train_data = train_data - mean
    standard = train_data.std(axis = 0)
    train_data = train_data / standard

    # Normalizing test data
    test_data = test_data - mean
    test_data = test_data / standard


    model = models.Sequential()
    model.add(layers.Dense(16, activation="relu", input_shape=(4,)))
    model.add(layers.Dense(16, activation="relu"))
    model.add(layers.Dense(4, activation="relu"))
    model.add(layers.Dense(1))

    # model.compile(optimizer=optimizers.Adam(learning_rate=0.00155), loss="mse",metrics=['mse', 'mae', 'mape'])
    model.compile(loss='mse', optimizer='adam', metrics=['mse', 'mae', 'mape'])
    history = model.fit(train_data, train_labels, epochs= 120, verbose=False )
    # print(history.history.keys())

    fig, ax = plt.subplots()
    fig.figsize=(12,7)
    ax.plot(history.history['mse'], "g-", label="mean squared error")
    ax.plot(history.history['mae'], "b-", label="mean absolute error")
    ax.plot(history.history['mape'], "r-",label="mean absolute percentage error" )
    # plt.plot(history.history['cosine_proximity'])
    leg = ax.legend()
    plt.show()

training_model()
