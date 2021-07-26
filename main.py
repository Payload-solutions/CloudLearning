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


def main():
    # utilities = Utils()
    # print(utilities.load_from_csv("data/yogurt_dataset_nn.csv"))

    data_master = pd.read_csv("data/beta_dataset.csv")
    """
    Index(['streptococcus_initial_strain_cfu_ml',
       'lactobacillus_initial_strain_cfu_ml', 'ideal_temperature_c',
       'minimum_milk_proteins', 'titratable_acidity', 'pH_milk_sour_',
       'fat_milk_over_100mg_', 'quality_product'],
    """
    y_strep = data_master["streptococcus_initial_strain_cfu_ml"]
    y_lact = data_master["lactobacillus_initial_strain_cfu_ml"]

    X = data_master.drop(["streptococcus_initial_strain_cfu_ml", "lactobacillus_initial_strain_cfu_ml"], axis=1)


if __name__ == "__main__":
    main()
