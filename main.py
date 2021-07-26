#!/usr/bin/python3

import pandas as pd
import numpy as np
from tensorflow import keras

from keras import (
    layers,
    models,
    optimizers
)


class NeuronNetworkRegression:

    def __init__(self, learning_rate: float, input_shape_val: int) -> None:
        self.learning_rate = learning_rate
        self.input_shape_val = input_shape_val

    def _define_model(self):
        model = models.Sequential()
        model.add(layers.Dense(64, activation="relu", input_shape=self.input_shape_val,))
        model.add(layers.Dense(64, activation="relu"))
        model.add(layers.Dense(1))

        return model

    def init_trainings(self):
        model = self._define_model()


def main():
    neuron_1 = NeuronNetworkRegression(learning_rate=0.02, input_shape_val=7)
    neuron_1.init_trainings()


if __name__ == "__main__":
    main()
