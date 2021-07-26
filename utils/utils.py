import pandas as pd


class Utils:

    def __init__(self,) -> None:
        pass

    def load_from_csv(self, path: str) -> None:
        return pd.read_csv(path)

    def features_target(self, dataset, drop_cols, target_name):
        
        X = dataset.drop(drop_cols, axis = 1)
        y = dataset[target_name]

        return X, y

