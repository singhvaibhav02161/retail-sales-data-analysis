import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("../data/retail_sales.csv",parse_dates=["Order_Date"])
df["Month"]=df["Order_Date"].dt.to_period("M").astype(str)
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
monthly=df.groupby("Month",as_index=False)["Sales"].sum()
monthly.plot(x="Month",y="Sales",kind="line",figsize=(12,5),title="Monthly Revenue")
plt.xticks(rotation=45); plt.tight_layout(); plt.show()