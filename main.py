#!/usr/bin/python3

import pandas as pd
import numpy as np

from tensorflow.keras import (
    layers,
    models,
    optimizers
)

from sklearn.model_selection import train_test_split
from utils.utils import Utils


def implementing_data():
    # utilities = Utils()
    # print(utilities.load_from_csv("data/yogurt_dataset_nn.csv"))

    data_master = pd.read_csv("data/beta_dataset.csv")

    y_strep = data_master["streptococcus_initial_strain_cfu_ml"]
    # y_lact = data_master["lactobacillus_initial_strain_cfu_ml"]

    X = data_master.drop(["streptococcus_initial_strain_cfu_ml", "lactobacillus_initial_strain_cfu_ml", "quality_product"], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y_strep, test_size=0.3, random_state=42)

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


    return train_data, test_data, y_train, y_test

def defining_model(input_data: int, learning_rate_val: float):
    
    model = models.Sequential()
    model.add(layers.Dense(64, activation = "relu", input_shape = (input_data)))
    model.add(layers.Dense(64, activation = "relu"))

    # as this result is a regression; is a continuous number, that's lineal
    # doesn't need an activation layer
    model.add(layers.Dense(1))

    model.compile(optimizer=optimizers.RMSprop(learning_rate= learning_rate_val),
        loss="mse",
        metrics=["mae"])

    return model


def train_network(train_data_size: int):
    k_fold_validations = 4
    num_val_samples = train_data_size // k_fold_validations
    epochs = 80
    all_histories = list()


def main():
    
    # data already normalized
    train_data, test_data, y_train, y_test = implementing_data()




if __name__ == "__main__":
    main()
