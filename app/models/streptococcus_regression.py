

from tensorflow.keras import (
    models,
    layers,
    optimizers
)
from tensorflow.keras.models import model_from_json
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os

class StreptococcusRegression:

    def __init__(self, path: str) -> None:
        self.data_master = pd.read_csv(path)

    def spliting_data(self):
        y_strep = self.data_master["streptococcus_initial_strain_cfu_ml"]

        X = self.data_master.drop(["streptococcus_initial_strain_cfu_ml", "lactobacillus_initial_strain_cfu_ml", "quality_product", "ideal_temperature_c"], axis=1)

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

    def model_prediction(self, minimum_milk_proteins: float, titratable_acidity: float, pH_milk_sour: float, fat_milk_over_100mg_: float, target_data: float) -> str:
        
        loaded_model_json = None
        pred_range = None
        if not os.path.exists("strep_model.json"):
            model,_ = self.defining_model(4, 0.0155)
            pred_range = model.predict(np.array([minimum_milk_proteins, titratable_acidity, pH_milk_sour, fat_milk_over_100mg_]).reshape(1, -1))
        else:
            with open("strep_model.json", "r") as json_file:
                loaded_model_json = json_file.read()
    
            model_loaded = model_from_json(loaded_model_json)

            # Loading weigths
            model_loaded.load_weights("strep_model.h5")

            # Making another evaluation
            model_loaded.compile(optimizer=optimizers.RMSprop(learning_rate= 0.0155),
                    loss="mse",
                    metrics=["mae"])
            # model_loaded.predict()
            pred_range = model_loaded.predict(np.array([minimum_milk_proteins, titratable_acidity, pH_milk_sour, fat_milk_over_100mg_]).reshape(1, -1))


        return "{0:.2f}%".format((target_data / pred_range[0][0])*100) if pred_range > target_data else "{0:.2f}%".format((pred_range[0][0] /target_data)*100)

    def defining_model(self, input_data: int, learning_rate_val: float):
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

        train_data,_ , y_train, _ = self.spliting_data()
        k_fold_validations = 6

        num_val_samples = len(train_data) // k_fold_validations
        num_epochs = 80
        all_histories = list()

        for i in range(k_fold_validations):
            val_data = train_data[i*num_val_samples: (i+1)*num_val_samples]
            val_target = y_train[i*num_val_samples: (i+1)*num_val_samples]

            partial_train_data = np.concatenate(
                [train_data[:i * num_val_samples],
                train_data[(i+1)*num_val_samples:]
                ], axis = 0)

            partial_train_target = np.concatenate(
                [y_train[:i * num_val_samples],
                y_train[(i+1)*num_val_samples:]
                ], axis = 0)

            # model = defining_model(5, 0.0001)
            # model = defining_model(5, 0.23) # that can be the right value
            # model = defining_model(4, 0.0155)
            history = model.fit(partial_train_data, partial_train_target,
                    epochs=num_epochs,
                    batch_size=16,
                    validation_data=(val_data, val_target),
                    verbose=False)

            all_histories.append(history.history["val_mae"])

        if not os.path.exists("strep_model.json"):
            # Serializing the model
            json_model = model.to_json()
            with open("strep_model.json", "w") as json_file:
                json_file.write(json_model)

            # Serializing the weights TO HDF5
            model.save_weights("strep_model.h5")
        return model, all_histories
