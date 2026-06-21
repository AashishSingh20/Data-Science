# Aggregate Functions 
USE mlsql;

SELECT * FROM superstore;

SELECT avg(`sales`) as 'Average_Sales'
FROM superstore;

SELECT sum(`Profit`) as 'Total_Profit'
FROM superstore;

SELECT min(`Profit`) as 'Minimum_Profit'
FROM superstore;

SELECT max(`Profit`) as 'Maximum_Profit'
FROM superstore;

SELECT min(`Customer Name`)  # Gets us the name whose name starts with initial aphabetical characters
FROM superstore;


# Sorting the data

SELECT `Row ID`, `Customer Name` , `City`, `Sales`
FROM superstore
ORDER BY  `Sales` DESC;

SELECT `Row ID`, `Customer Name` , `City`, `Sales`
FROM superstore
ORDER BY  `Sales`;  -- Deafult order is Ascending


# Grouping the Data

SELECT `Region`, round(sum(Sales)) AS 'Total_Sales'  # Gets us region wise Total Sales after roundoff
FROM superstore
GROUP BY Region;

SELECT `Region`, round(sum(Sales)) AS 'Total_Sales'  # Gets us region wise Total Sales after roundoff
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC