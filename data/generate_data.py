"""Generate the full synthetic portfolio dataset used by the project.
Run: python data/generate_data.py
"""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
OUT = Path(__file__).resolve().parent / "retail_sales_full.csv"
n = 10000
regions = ["North", "South", "East", "West", "Central"]
categories = ["Electronics", "Furniture", "Office Supplies", "Home Appliances", "Accessories"]
products = ["Laptop", "Monitor", "Keyboard", "Mouse", "Printer", "Desk", "Chair", "Phone", "Headphones", "Router", "Tablet", "Webcam"]
df = pd.DataFrame({
    "Order_ID": [f"ORD{100001+i}" for i in range(n)],
    "Order_Date": rng.choice(pd.date_range("2025-01-01", "2025-12-31"), n),
    "Region": rng.choice(regions, n, p=[.24,.18,.16,.28,.14]),
    "Category": rng.choice(categories, n),
    "Product": rng.choice(products, n),
    "Quantity": rng.integers(1, 8, n),
    "Unit_Price": rng.choice([25,40,55,75,90,120,150,200,300,450,650,900], n),
    "Discount": rng.choice([0,.05,.10,.15,.20], n, p=[.40,.20,.20,.15,.05])
})
df["Sales"] = (df["Quantity"] * df["Unit_Price"] * (1-df["Discount"])).round(2)
df["Profit"] = (df["Sales"] * rng.uniform(.08,.28,n)).round(2)
df.to_csv(OUT, index=False)
print(f"Created {len(df):,} rows: {OUT}")
