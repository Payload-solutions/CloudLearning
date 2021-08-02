
import numpy as np
import pandas as pd
from pandas.core.algorithms import mode
import seaborn as sns
from tensorflow.keras import (
    models,
    layers
)

import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import model_from_json
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import (
    to_categorical
)

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

    def _defining_data_split(self):
        X, y = self.data_master.drop("", axis = 1),  self.data_master[""]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        train_data, test_data = X_train.to_numpy(), X_test.to_numpy()
        train_labels, test_labels = to_categorical(y_train), to_categorical(y_test)

        return train_data, test_data, train_labels, test_labels
    
    def _defining_model(self):
        train_data, test_data, train_labels, test_labels = self._defining_data_split()

        x_val = train_data[:int(len(train_data) *0.32)]
        partial_x_train = train_data[int(len(train_data) *0.32):]


        y_val = train_labels[:int(len(train_labels) *0.32)]
        partial_y_train = train_labels[int(len(train_labels) *0.32):]

        model = models.Sequential()
        model.add(layers.Dense(64, activation="relu", input_shape=(self.input_shape_val, )))
        model.add(layers.Dense(64, activation="relu"))
        model.add(layers.Dense(self.output_shape_val, activation="softmax"))

        model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

        history = model.fit(partial_x_train, partial_y_train, 
            epochs=self.epochs_number,
            batch_size=512, verbose=False,
            validation_data=(x_val, y_val))

        return {
            "history": history,
            "test_data": test_data,
            "test_labels":test_labels,
            "model": model,
        }
    
    def get_metrics(self) -> float:
        metrics_vals = self._defining_model()
        data_test = metrics_vals["test_data"]
        label_test = metrics_vals["test_labels"]
        model = metrics_vals["model"]
        
        accuracy_metric = float("{0:.2f}%".format( model.evaluate(data_test, label_test)[1] *100))
        return accuracy_metric