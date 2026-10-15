

# Solar Cell Performance Prediction Using Machine Learning

import pandas as pd
import numpy as np

def load_dataset(file_path):
    """Load the solar-cell dataset."""
    data = pd.read_csv(file_path)
    return data

def inspect_dataset(data):
    """Display basic information about the dataset."""
    print("Dataset Shape:", data.shape)
    print("\nFirst Five Rows:")
    print(data.head())
    print("\nMissing Values:")
    print(data.isnull().sum())
    print("\nDataset Information:")
    print(data.info())
