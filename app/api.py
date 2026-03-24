from fastapi import FastAPI
import pymysql

app = FastAPI()

def get_connection():

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Hello2me@",
        database="stock_pipeline",
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection
@app.get("/stocks")
def get_all_stocks():

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        SELECT *
        FROM stock_data
        ORDER BY date DESC
        LIMIT 100
    """

    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results
@app.get("/latest")
def get_latest_stock():

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        SELECT *
        FROM stock_data
        ORDER BY date DESC
        LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

@app.get("/stats")
def get_statistics():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT 
            COUNT(*) as total_records,
            AVG(close) as avg_close_price,
            MAX(high) as highest_price,
            MIN(low) as lowest_price
        FROM stock_data
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

@app.get("/by-date/{date}")
def get_data_by_date(date: str):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT *
        FROM stock_data
        WHERE DATE(date) = %s
    """

    cursor.execute(query, (date,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

@app.get("/average-price")
def get_average_price():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT 
            AVG(open) as avg_open,
            AVG(close) as avg_close
        FROM stock_data
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result
