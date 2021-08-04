import pandas as pd


def upload_file(file_name: str):
    return pd.read_csv(file_name)