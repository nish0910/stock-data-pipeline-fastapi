import pandas as pd
import pymysql

def load_data_to_mysql():

    # Read cleaned data
    df = pd.read_csv("data/clean_stock_data.csv")

    # Connect to MySQL
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Hello2me@",
        database="stock_pipeline"
    )

    cursor = connection.cursor()

    # Insert data
    for _, row in df.iterrows():

        cursor.execute("""
            INSERT INTO stock_data
            (date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            row["date"],
            row["open"],
            row["high"],
            row["low"],
            row["close"],
            row["volume"]
        ))

    connection.commit()

    cursor.close()
    connection.close()

    print("Data loaded into MySQL successfully")


if __name__ == "__main__":

    load_data_to_mysql()
