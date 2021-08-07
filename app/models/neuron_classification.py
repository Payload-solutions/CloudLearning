import json
from typing import Any
from numpy.core.fromnumeric import shape
import pandas as pd
from tensorflow.keras import (
    models,
    layers
)
from tensorflow.keras.models import model_from_json
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import (
    to_categorical
)
import os
import numpy as np


class NeuronClassification:

    def __init__(self, file_path: str, epochs_number: int, input_shape_val: int, output_shape_val: int) -> None:
        """[summary]

        Args:
            file_path (str): [description]
            epochs_number (int): [1000 it's the best for the model, to avoid overfitting and underfitting]
            input_shape_val (int): [description]
            output_shape_val (int): [description]
        """
        self.data_master = pd.read_csv(file_path)
        self.epochs_number = epochs_number
        self.input_shape_val = input_shape_val
        self.output_shape_val = output_shape_val
        self.train_data, self.test_data, self.train_labels, self.test_labels = self._defining_data_split()

        """
        The values are transformed from plain text to numeric categorical
        using this function:
            y_train = LabelEncoder().fit_transform(y_train)
            y_test = LabelEncoder().fit_transform(y_test)

            train_labels, test_labels = to_categorical(y_train), to_categorical(y_test)
            # now the data is ready to be transformed, because the data is floating
        """

        if not os.path.exists("model_training/classification_model.json"):
            self._defining_model()

    def _defining_data_split(self):
        X, y = self.data_master.drop(["quality_product", "quality_product_"], axis=1), self.data_master[
            "quality_product_"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        train_data, test_data = X_train.to_numpy(), X_test.to_numpy()
        train_labels, test_labels = to_categorical(y_train), to_categorical(y_test)

        return train_data, test_data, train_labels, test_labels

    def _defining_model(self) -> None:

        x_val = self.train_data[:int(len(self.train_data) * 0.32)]
        partial_x_train = self.train_data[int(len(self.train_data) * 0.32):]

        y_val = self.train_labels[:int(len(self.train_labels) * 0.32)]
        partial_y_train = self.train_labels[int(len(self.train_labels) * 0.32):]

        model = models.Sequential()
        model.add(layers.Dense(64, activation="relu", input_shape=(self.input_shape_val,)))
        model.add(layers.Dense(64, activation="relu"))
        model.add(layers.Dense(self.output_shape_val, activation="softmax"))

        model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

        history = model.fit(partial_x_train, partial_y_train,
                            epochs=self.epochs_number,
                            batch_size=512, verbose=False,
                            validation_data=(x_val, y_val))
        json_model = model.to_json()
        print(history.history)

        # saving the classification model
        with open("model_training/classification_model.json", "w") as json_file:
            json_file.write(json_model)

        # serializing the data
        model.save_weights("model_training/classification_weights.h5")

        # saving the history variable
        with open("model_training/classification_history.json", "w") as history_file:
            json.dump(history.history, history_file)

    def measure_predictions(self, features_value: np.ndarray, target_value: np.ndarray) -> Any:

        try:

            if features_value.shape == (len(features_value), 9) or features_value.shape == (1, 9):

                with open("model_training/classification_model.json") as json_file:
                    loaded_model = json_file.read()

                model_loaded = model_from_json(loaded_model)

                # Loading weights
                model_loaded.load_weights("model_training/classification_weights.h5")

                # making another evaluation
                model_loaded.compile(optimizer="rmsprop",
                                    loss="categorical_crossentropy",
                                    metrics=["accuracy"])

                # accuracy prediction
                accuracy_metric = float("{0:.2f}".format(model_loaded.evaluate(np.array(features_value), np.array(target_value))[1] * 100))

                return {
                    "accuracy_metrics": accuracy_metric,
                }

            else:
                raise ValueError("The dimension in the features is not the right")
        except ValueError as e:
            return {
                "message": "Error by: {}".format(str(e))
            }
