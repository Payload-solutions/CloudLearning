import numpy as np
import pandas as pd
from tensorflow.keras import (
    models,
    layers,
    optimizers
)
from sklearn.model_selection import train_test_split


class NeuronNetworkRegression:

    def __init__(self, learning_rate: float, input_shape_val: int, path: str) -> None:
        self.learning_rate = learning_rate
        self.input_shape_val = input_shape_val
        self.data_master = pd.read_csv(path)


    def train_test_data(self):
        # data_master = pd.read_csv("train_data/beta_dataset.csv")

        y_strep = self.data_master["streptococcus_initial_strain_cfu_ml"]
        X = self.data_master.drop(["streptococcus_initial_strain_cfu_ml", 
            "lactobacillus_initial_strain_cfu_ml", 
            "quality_product"], axis=1)


        # y_lact = self.data_master["lactobacillus_initial_strain_cfu_ml"]
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
        

    def _define_model(self):
        model = models.Sequential()
        model.add(layers.Dense(64, activation="relu", input_shape=self.input_shape_val, ))
        model.add(layers.Dense(64, activation="relu"))
        model.add(layers.Dense(1))

        model.compile(optimizer=optimizers.RMSprop(learning_rate= self.learning_rate_val),
        loss="mse",
        metrics=["mae"])

        return model

    def init_trainings(self,k_fold_validations: int, num_epochs: int ):
        train_data, test_data, train_labels, test_labels = self.train_test_data()
        
        num_val_samples = len(train_data) // k_fold_validations
        all_histories = list()
        
        for i in range(k_fold_validations):
            print("Fold: %s"%i)
            val_data = train_data[i*num_val_samples: (i+1)*num_val_samples]
            val_target = train_labels[i*num_val_samples: (i+1)*num_val_samples]

            partial_train_data = np.concatenate(
                [train_data[:i * num_val_samples],
                train_data[(i+1)*num_val_samples:]
                ], axis = 0)

            partial_train_target = np.concatenate(
                [train_labels[:i * num_val_samples],
                train_labels[(i+1)*num_val_samples:]
                ], axis = 0)

            model = self._define_model()

            history = model.fit(partial_train_data, partial_train_target, 
                    epochs=num_epochs, 
                    batch_size=16,
                    validation_data=(val_data, val_target),
                    verbose=0)

            all_histories.append(history.history["val_mae"])


        return model.evaluate(test_labels)

        