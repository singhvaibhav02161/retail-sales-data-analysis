-- MySQL Retail Sales Analysis
SELECT ROUND(SUM(Sales),2) AS total_revenue, ROUND(SUM(Profit),2) AS total_profit FROM retail_sales;
SELECT Region, ROUND(SUM(Sales),2) revenue, ROUND(SUM(Profit),2) profit, COUNT(DISTINCT Order_ID) orders
FROM retail_sales GROUP BY Region ORDER BY revenue DESC;
SELECT Category, ROUND(SUM(Sales),2) revenue, ROUND(SUM(Profit),2) profit
FROM retail_sales GROUP BY Category ORDER BY revenue DESC;
SELECT DATE_FORMAT(Order_Date,'%Y-%m') month, ROUND(SUM(Sales),2) revenue
FROM retail_sales GROUP BY DATE_FORMAT(Order_Date,'%Y-%m') ORDER BY month;
SELECT Product, ROUND(SUM(Sales),2) revenue FROM retail_sales
GROUP BY Product ORDER BY revenue DESC LIMIT 5;