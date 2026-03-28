'''
Load  dataset return the dataframe
'''
import pandas as pd
def load_data():
    df = pd.read_csv("data/cleaned_data.csv")
    return df



