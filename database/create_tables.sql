create DATABASE STOCK_PIPELINE;
USE STOCK_PIPELINE;
CREATE TABLE stock_data (

    id INT AUTO_INCREMENT PRIMARY KEY,

    date DATETIME,

    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,

    volume BIGINT

);
select * from stock_data
limit 10;

