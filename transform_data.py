import pandas as pd

def transform_stock_data(input_file):

    # Read raw data
    df = pd.read_csv(input_file)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert datatypes
    df["date"] = pd.to_datetime(df["date"])

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(int)

    # Sort by date
    df.sort_values(
        by="date",
        ascending=True,
        inplace=True
    )

    return df


if __name__ == "__main__":

    input_file = "data/raw_stock_data.csv"

    df_clean = transform_stock_data(input_file)

    print(df_clean.head())

    # Save cleaned data
    df_clean.to_csv(
        "data/clean_stock_data.csv",
        index=False
    )

    print("Data transformation completed")