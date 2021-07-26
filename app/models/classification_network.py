
import pandas as pd
from tensorflow.keras import (
    models,
    layers,
    optimizers
)


class NeuronClassification:

    def __init__(self, learning_rate: float, input_shape_val: int, path: str) -> None:
        self.learning_rate = learning_rate
        self.input_shape_val = input_shape_val
        self.dataset = pd.read_csv(path)

    def _define_model(self):
        model = models.Sequential()
        model.add(layers.Dense(64, activation="relu", input_shape=self.input_shape_val, ))
        model.add(layers.Dense(64, activation="relu"))
        model.add(layers.Dense(1))

        return model

    def init_trainings(self):
        model = self._define_model()