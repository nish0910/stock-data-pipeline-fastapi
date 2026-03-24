print("run_pipelineloaded")

import os

from app.fetch_data import fetch_stock_data
from app.transform_data import transform_stock_data
from database.load_to_db import load_data_to_mysql

def run_pipeline():

    print("Starting pipeline...")

    # Step 1 — Fetch Data
    df = fetch_stock_data("IBM")

    if df is None:
        print("Fetch failed")
        return

    os.makedirs("data", exist_ok=True)

    df.to_csv(
        "data/raw_stock_data.csv",
        index=False
    )

    print("Data fetched")

    # Step 2 — Transform
    df_clean = transform_stock_data(
        "data/raw_stock_data.csv"
    )

    df_clean.to_csv(
        "data/clean_stock_data.csv",
        index=False
    )

    print("Data transformed")

    # Step 3 — Load to MySQL
    load_data_to_mysql()

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()

