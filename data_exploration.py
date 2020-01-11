
# %% Steps:

# get Data
# general info about the dataset
# description of the data
# Histogram of the data
# Split training test validation with hash and seed, stratified
# corr of the data to target
# zoom in some imp var from above to view details
# split the data: training, testing

#%% input data path
HOUSING_PATH = "Datasets/housing"

#%% import block
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#%% Loads data
def load_housing_data (housing_path):

    csv_path = os.path.join(housing_path,"housing.csv")
    data = pd.read_csv(csv_path)
    return data

housing_data = load_housing_data(housing_path = HOUSING_PATH)
housing_data.head()
housing_data.info()
# total_bedrooms has missing value
housing_data.describe()
