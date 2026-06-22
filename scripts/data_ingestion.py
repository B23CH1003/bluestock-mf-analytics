import pandas as pd
from pathlib import Path


data_path = Path("data/raw")


files = list(data_path.glob("*.csv"))


for file in files:
    print("\n==============================")
    print("File Name:", file.name)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())