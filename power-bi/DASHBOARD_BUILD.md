# Power BI Dashboard — Build Specification

## Page 1 — Executive Overview
KPI cards: Total Revenue, Total Profit, Total Orders, Average Order Value, Profit Margin.

Visuals:
- Monthly Revenue line chart
- Revenue by Region clustered bar
- Revenue by Category donut
- Top 5 Products bar

Slicers: Order Date, Region, Category.

## Page 2 — Regional Performance
- Region revenue/profit matrix
- Revenue share by region
- Monthly regional trend
- Conditional formatting for profit margin

## Page 3 — Product & Category
- Category revenue and profit
- Top 10 products by revenue
- Quantity by product
- Discount vs profit scatter plot

## Page 4 — Trend Analysis
- Monthly revenue
- Monthly profit
- Monthly order count
- Month-over-month revenue change

## Data model
Single fact table: `retail_sales`.
Use `Order_Date` as the date field. For a production model, create a dedicated Date table and mark it as a date table.

## DAX
See `DAX_measures.txt`.

## Portfolio quality checklist
- Consistent number formatting
- Descriptive visual titles
- Slicers synchronized across pages where appropriate
- No 3D charts; prioritize readable business visuals
- Add a short insight text box to each page
