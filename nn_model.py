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
from pprint import pprint

def forming_data():
    pass

def implementing_data():
    data_master = pd.read_csv("data/beta_dataset.csv")

    y_strep = data_master["streptococcus_initial_strain_cfu_ml"]
    # y_lactobacillus = data_master["lactobacillus_initial_strain_cfu_ml"]

    X = data_master.drop(
        ["streptococcus_initial_strain_cfu_ml", "lactobacillus_initial_strain_cfu_ml", "quality_product"], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y_strep, test_size=0.3, random_state=42)

    # Reshaping data
    train_data, test_data = X_train.to_numpy(), X_test.to_numpy()

    # Normalizing train data
    mean = train_data.mean(axis=0)
    train_data = train_data - mean
    standard = train_data.std(axis=0)
    train_data = train_data / standard

    # Normalizing test data
    test_data = test_data - mean
    test_data = test_data / standard

    return train_data, test_data, y_train, y_test


def defining_model(input_data: int, learning_rate_val: float):
    model = models.Sequential()
    model.add(layers.Dense(64, activation="relu", input_shape=(input_data,)))
    model.add(layers.Dense(64, activation="relu"))

    # as this result is a regression; is a continuous number, that's lineal
    # doesn't need an activation layer
    model.add(layers.Dense(1))

    model.compile(optimizer=optimizers.RMSprop(learning_rate=learning_rate_val),
                  loss="mse",
                  metrics=["mae"])

    return model


def train_network():
    train_data, test_data, y_train, y_test = implementing_data()
    k_fold_validations = 4

    num_val_samples = len(train_data) // k_fold_validations
    num_epochs = 500
    all_histories = list()

    for i in range(k_fold_validations):
        print("Fold: %s" % i)
        val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
        val_target = y_train[i * num_val_samples: (i + 1) * num_val_samples]

        partial_train_data = np.concatenate(

            [train_data[:i * num_val_samples],
             train_data[(i + 1) * num_val_samples:]
             ], axis=0)

        partial_train_target = np.concatenate(

            [y_train[:i * num_val_samples],
             y_train[(i + 1) * num_val_samples:]
             ], axis=0)

        model = defining_model(5, 0.001)

        history = model.fit(partial_train_data, partial_train_target,
                            epochs=num_epochs,
                            batch_size=16,
                            validation_data=(val_data, val_target),
                            verbose=0
                            )

        all_histories.append(history.history["val_mae"])

    print("\n[*] All history: %s" % len(all_histories[0]))
    print("\n\n[*] Viewing all histories\n")
    pprint(all_histories)

    all_mae_avg = pd.DataFrame(all_histories).mean(axis=0)


def main():
    # data already normalized
    # getting the data
    train_network()


if __name__ == "__main__":
    main()
