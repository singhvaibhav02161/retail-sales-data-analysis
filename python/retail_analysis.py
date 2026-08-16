import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "../data/retail_sales.csv"

def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["Order_Date"])
    df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

    print("Dataset shape:", df.shape)
    print("\nMissing values:\n", df.isna().sum())
    print("\nDuplicate Order IDs:", df["Order_ID"].duplicated().sum())

    region_summary = (
        df.groupby("Region", as_index=False)
          .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order_ID", "nunique"))
          .sort_values("Revenue", ascending=False)
    )
    print("\nRegion performance:\n", region_summary.round(2))

    category_summary = (
        df.groupby("Category", as_index=False)
          .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
          .sort_values("Revenue", ascending=False)
    )
    print("\nCategory performance:\n", category_summary.round(2))

    monthly = df.groupby("Month", as_index=False).agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))

    ax = monthly.plot(x="Month", y="Revenue", kind="line", figsize=(12, 5), title="Monthly Revenue")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
