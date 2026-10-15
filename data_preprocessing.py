
# Solar Cell Performance Prediction Using Machine Learning

import pandas as pd
import numpy as np

def load_dataset(file_path):
    """Load the solar-cell Excel dataset."""
    data = pd.read_excel(file_path)
    return data

def inspect_dataset(data):
    """Display basic information about the dataset."""
    print("Dataset Shape:", data.shape)

    print("\nFirst Five Rows:")
    print(data.head())

    print("\nColumn Names:")
    print(data.columns.tolist())

    print("\nMissing Values:")
    print(data.isnull().sum())

    print("\nDataset Information:")
    data.info()
