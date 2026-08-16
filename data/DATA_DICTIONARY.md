# Retail Sales Data Dictionary

| Column | Type | Description |
|---|---|---|
| Order_ID | Text | Unique transaction/order identifier |
| Order_Date | Date | Date of the order |
| Region | Category | Sales region |
| Category | Category | Product category |
| Product | Category | Product name |
| Quantity | Integer | Units sold |
| Unit_Price | Decimal | Price per unit before discount |
| Discount | Decimal | Discount rate applied to the order |
| Sales | Decimal | Net sales value after discount |
| Profit | Decimal | Estimated transaction profit |

## Data Quality Checks
- Validate date types.
- Check duplicate Order_ID values.
- Confirm Quantity is positive.
- Confirm Discount is between 0 and 1.
- Check Sales and Profit for unexpected negative values.
