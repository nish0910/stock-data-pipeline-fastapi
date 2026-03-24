import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_stock_data(symbol="IBM"):

    url = (
        f"https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_DAILY"
        f"&symbol={symbol}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    time_series = data.get("Time Series (Daily)", {})

    if not time_series:
        print("Error fetching data:")
        print(data)
        return None

    df = pd.DataFrame.from_dict(
        time_series,
        orient="index"
    )

    df.columns = [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    df.reset_index(inplace=True)

    df.rename(
        columns={"index": "date"},
        inplace=True
    )

    return df


if __name__ == "__main__":

    df = fetch_stock_data("IBM")

    if df is not None:

        print(df.head())

        os.makedirs("data", exist_ok=True)

        df.to_csv(
            "data/raw_stock_data.csv",
            index=False
        )

        print("Data fetched successfully")
