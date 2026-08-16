-- MySQL Retail Sales Analysis

-- 1. Overall KPIs
SELECT ROUND(SUM(Sales), 2) AS total_revenue,
       ROUND(SUM(Profit), 2) AS total_profit,
       COUNT(DISTINCT Order_ID) AS total_orders,
       ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS profit_margin_pct
FROM retail_sales;

-- 2. Region-wise performance
SELECT Region,
       ROUND(SUM(Sales), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit,
       COUNT(DISTINCT Order_ID) AS orders,
       ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS profit_margin_pct
FROM retail_sales
GROUP BY Region
ORDER BY revenue DESC;

-- 3. Category-wise performance
SELECT Category,
       ROUND(SUM(Sales), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit,
       ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS profit_margin_pct
FROM retail_sales
GROUP BY Category
ORDER BY revenue DESC;

-- 4. Monthly revenue and profit trend
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS month,
       ROUND(SUM(Sales), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY month;

-- 5. Top 5 products by revenue
SELECT Product,
       ROUND(SUM(Sales), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY Product
ORDER BY revenue DESC
LIMIT 5;

-- 6. Discount impact
SELECT Discount,
       COUNT(*) AS order_lines,
       ROUND(SUM(Sales), 2) AS revenue,
       ROUND(SUM(Profit), 2) AS profit
FROM retail_sales
GROUP BY Discount
ORDER BY Discount;
