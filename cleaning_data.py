import pandas as pd
import os
from preprocess_data import preprocess_data

# Show current working directory
print("Current Working Directory:", os.getcwd())

# Load data using FULL PATH
data = pd.read_csv(r"D:\AI recommendation\clean_data.csv")

# Clean data
cleaned_data = preprocess_data(data)

# Save cleaned data back to same file
cleaned_data.to_csv(r"D:\AI recommendation\cleaned_data.csv", index=False)

print("Data cleaned and saved to cleaned_data.csv successfully ✅")


# ---------------- VERIFICATION ----------------

print("\n----- VERIFICATION STARTED -----\n")

print("Missing Values:\n", cleaned_data.isnull().sum())

print("\nAny NaN in User's ID?:", cleaned_data["User's ID"].isnull().any())
print("Any NaN in ProdID?:", cleaned_data["ProdID"].isnull().any())

print("\nZero User's ID count:", (cleaned_data["User's ID"] == 0).sum())
print("Zero ProdID count:", (cleaned_data["ProdID"] == 0).sum())

print("\nData Types:\n", cleaned_data.dtypes)

print("\nDoes 'Unnamed: 0' exist?:", 'Unnamed: 0' in cleaned_data.columns)

for col in cleaned_data.columns:
    if 'image' in col.lower():
        print(f"\n'|' found in {col}?:",
              cleaned_data[col].str.contains('\|').any())

print("\nIndex starts from 0?:", cleaned_data.index[0] == 0)

print("\n----- VERIFICATION COMPLETED -----")
