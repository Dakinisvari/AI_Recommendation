import pandas as pd
import numpy as np
def preprocess_data(data):
    # Replace invalid values with NaN
    data['ProdID'] = data['ProdID'].replace(-2147483648, np.nan)
    data["User's ID"] = data["User's ID"].replace(-2147483648, np.nan)
    # Drop rows where User's ID is missing
    data.dropna(subset=["User's ID"], inplace=True)
    # Convert to integer
    data["User's ID"] = data["User's ID"].astype('int64')
    # Drop rows where ProdID is missing
    data.dropna(subset=['ProdID'], inplace=True)
    # Convert to integer
    data['ProdID'] = data['ProdID'].astype('int64')
    # Remove rows where ID or ProdID is 0
    data.drop(data[(data["User's ID"] == 0) | (data["ProdID"] == 0)].index,inplace=True)
    # Drop unwanted column if exists
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)
    # Fill text columns with empty string
    text_columns = data.select_dtypes(include=['object']).columns
    data[text_columns] = data[text_columns].fillna('')
    # Remove "|" from image links
    for col in text_columns:
        if 'image' in col.lower():
            data[col] = data[col].str.replace('|', '', regex=False)
    # Reset index
    data.reset_index(drop=True, inplace=True)
    return data