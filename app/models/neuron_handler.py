import os
from .regression_network import NeuronNetworkRegression

def checking_training():

    if not os.path.exists("train.pkl"):
        nn_1 = NeuronNetworkRegression(learning_rate= 0.001, 
                    input_shape_val=5, 
                    path = "train_data/beta_dataset.csv")