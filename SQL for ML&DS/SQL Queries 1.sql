CREATE DATABASE mlsql;
USE mlsql;

SELECT * FROM superstore;
SELECT * FROM students;

SELECT count('Order ID') FROM superstore;  -- Gets us number of order Id from superstore table

SELECT count(*) as total_records FROM superstore;  -- Gets us count of all records in superstore table

SELECT `Customer ID` FROM superstore;
SELECT `Customer Name` FROM superstore;   -- Gets us all Customer Name from superstore

SELECT count(DISTINCT(`Customer Name`)) as Unique_Customer_Name 
FROM superstore;

SELECT * 
FROM superstore 
LIMIT 5;   # Gets us 5 rows from the tables

SELECT `Order ID`, `Customer Name`, `Ship Date`
FROM superstore;