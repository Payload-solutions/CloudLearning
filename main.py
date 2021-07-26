#!/usr/bin/python3

import pandas as pd
import numpy as np
from tensorflow import keras

from keras import (
    layers,
    models,
    optimizers
)

from sklearn.model_selection import train_test_split
from utils.utils import Utils

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
    # utilities = Utils()
    # print(utilities.load_from_csv("data/yogurt_dataset_nn.csv"))
    
    datamaster = pd.read_csv("data/beta_dataset.csv")
    """
    Index(['streptococcus_initial_strain_cfu_ml',
       'lactobacillus_initial_strain_cfu_ml', 'ideal_temperature_c',
       'minimum_milk_proteins', 'titratable_acidity', 'pH_milk_sour_',
       'fat_milk_over_100mg_', 'quality_product'],
    """
    y_strep = datamaster["streptococcus_initial_strain_cfu_ml"]
    y_lact =  datamaster["lactobacillus_initial_strain_cfu_ml"]

    X = datamaster.drop(["streptococcus_initial_strain_cfu_ml", "lactobacillus_initial_strain_cfu_ml"], axis = 1)
    print(datamaster.columns)



if __name__ == "__main__":
    main()
