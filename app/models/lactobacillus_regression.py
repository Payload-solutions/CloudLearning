"""Neuron Network based in the lactobacillus species
The best model, has an accuracy of 
95.53%
"""

from tensorflow.keras import (
    models,
    layers,
    optimizers
)
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


class LactobacillusRegression:

    def __init__(self) -> None:
        self.data_master = pd.read_csv("train_Data/beta_dataset.csv")

    def spliting_data_lact(self):
        #y_strep = data_master["streptococcus_initial_strain_cfu_ml"]
        y_lact = self.data_master["lactobacillus_initial_strain_cfu_ml"]

        X = self.data_master.drop(["streptococcus_initial_strain_cfu_ml", "lactobacillus_initial_strain_cfu_ml", "quality_product", "ideal_temperature_c"], axis=1)

        X_train, X_test, train_label_lact, test_label_lact = train_test_split(X, y_lact, test_size=0.3, random_state=42)

        # Reshaping data
        train_data_lact, test_data_lact = X_train.to_numpy(), X_test.to_numpy()

        # Normalizing train data
        mean = train_data_lact.mean(axis = 0)
        train_data_lact = train_data_lact - mean
        standard = train_data_lact.std(axis = 0)
        train_data_lact = train_data_lact / standard
            
        # Normalizing test data
        test_data_lact = test_data_lact - mean
        test_data_lact = test_data_lact / standard

        return train_data_lact, test_data_lact, train_label_lact, test_label_lact

    def model_prediction(self, minimum_milk_proteins: float, titratable_acidity: float, pH_milk_sour: float, fat_milk_over_100mg_: float) -> str:

        """[summary]

        Returns:
            [minimum_milk_proteins]: [2.591]
            [titratable_acidity]: [0.992]
            [pH_milk_sour]: [4.415]
            [fat_milk_over_100mg_]: [3.1925]
        """
        lact_model, _ = self.defining_model_lact(4, 0.0155)
        pred_range_lact = lact_model.predict(np.array([minimum_milk_proteins, titratable_acidity, pH_milk_sour, fat_milk_over_100mg_]).reshape(1, -1))
        if pred_range_lact >5.196:
            return "{0:.2f}%".format((5.196/ pred_range_lact[0][0])*100)
        else:
            return "{0:.2f}%".format((pred_range_lact[0][0] /5.196)*100)

    def defining_model_lact(self, input_data: int, learning_rate_val: float):
        model = models.Sequential()
        model.add(layers.Dense(16, activation = "relu", input_shape = (input_data,)))
        model.add(layers.Dense(16, activation = "relu"))
        model.add(layers.Dense(4, activation = "relu"))
        model.add(layers.Dense(1))

        model.compile(optimizer=optimizers.RMSprop(learning_rate= learning_rate_val),
            loss="mse",
            metrics=["mae"])
        # model = defining_model(5, 0,00023)
        # model.fit(train_data, y_train, 
        #           epochs=120, batch_size = 16,
        #           validation_data=())
        k_fold_validations = 6


        train_data_lact,_, train_label_lact,_ = self.spliting_data_lact()

        num_val_samples = len(train_data_lact) // k_fold_validations
        num_epochs = 80
        all_histories = list()

        for i in range(k_fold_validations):
            print("Fold: %s"%i)
            val_data = train_data_lact[i*num_val_samples: (i+1)*num_val_samples]
            val_target = train_label_lact[i*num_val_samples: (i+1)*num_val_samples]

            partial_train_data = np.concatenate(
                [train_data_lact[:i * num_val_samples],
                train_data_lact[(i+1)*num_val_samples:]
                ], axis = 0)

            partial_train_target = np.concatenate(
                [train_label_lact[:i * num_val_samples],
                train_label_lact[(i+1)*num_val_samples:]
                ], axis = 0)
            # model = defining_model(5, 0.23) # that can be the right value
            history = model.fit(partial_train_data, partial_train_target, 
                    epochs=num_epochs, 
                    batch_size=16,
                    validation_data=(val_data, val_target),
                    verbose=False)

            all_histories.append(history.history["val_mae"])

        return model, all_histories