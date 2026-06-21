USE mlsql;

SELECT * FROM superstore;

SELECT * FROM superstore
WHERE `Order Date` < '11/11/2018';

SELECT *     # Gets us all data rows whose city is Los Angeles
FROM superstore
WHERE City = 'Los Angeles';

SELECT `Customer Name`, `Customer ID`, `Quantity` 
FROM superstore
WHERE `Ship Mode` = 'Second Class';

SELECT * 
FROM superstore
WHERE `City` = 'Philadelphia' OR `Ship Mode` = 'Standard Class';  # Ek bhi true hua toh chalega


SELECT * 
FROM superstore
WHERE `City` = 'Philadelphia' AND `Ship Mode` = 'Standard Class';  # Dono true hone chahiye


SELECT *
FROM superstore     # Here first convert Order Date from string to date then perform filtering to get order's between the said date
WHERE STR_TO_DATE(`Order Date`, '%m/%d/%Y')
BETWEEN '2018-06-12' AND '2018-11-08';

SELECT * 
FROM superstore
WHERE `Sales` BETWEEN  '120' AND '210';

SELECT * FROM students;

SELECT `Customer Name`
FROM superstore
WHERE `Customer Name` LIKE 'K%';   # K se start hone wale saare name aa jayenge Let it be one or more words in the name starting with k

SELECT `Customer Name`
FROM superstore
WHERE `Customer Name` LIKE 'Paul Gonzale_';  # Yaha last character mat do woh khud dhundh lega characters starting with the given name

SELECT * 
FROM superstore
WHERE `Sub-Category` in ("Chairs","Labels","Art")