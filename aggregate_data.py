import pandas as pd

# Load the cleaned dataset 
file_path = "cleaned.parquet"
df = pd.read_parquet(file_path)

print("Cleaned parquet loaded successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Ensure numeric columns are numeric
df["close_price"] = pd.to_numeric(df["close_price"], errors="coerce")
df["open_price"] = pd.to_numeric(df["open_price"], errors="coerce")
df["volume"] = pd.to_numeric(df["volume"], errors="coerce")

# Ensure trade_date is datetime
df["trade_date"] = pd.to_datetime(df["trade_date"], errors="coerce")

# Drop rows missing key columns
df = df.dropna(subset=["trade_date", "ticker", "close_price"])

# Aggregation 1 — Daily average close by ticker 
agg1 = (
    df.groupby(["trade_date", "ticker"], as_index=False)
      .agg(avg_close_price=("close_price", "mean"))
)
agg1.to_parquet("agg1.parquet", index=False)
print("\n Saved agg1.parquet → Daily avg close price by ticker")

#  Aggregation 2 — Average volume by sector 
agg2 = (
    df.groupby("sector", as_index=False)
      .agg(avg_volume=("volume", "mean"))
      .sort_values("avg_volume", ascending=False)
)
agg2.to_parquet("agg2.parquet", index=False)
print(" Saved agg2.parquet → Average volume by sector")

#  Aggregation 3 — Simple daily return by ticker
# Formula: (current_close - previous_close) / previous_close
df = df.sort_values(["ticker", "trade_date"])
df["daily_return"] = (
    df.groupby("ticker")["close_price"].pct_change()
)

agg3 = df[["trade_date", "ticker", "daily_return"]].dropna()
agg3.to_parquet("agg3.parquet", index=False)
print(" Saved agg3.parquet → Simple daily return by ticker")

# === Step 5: Confirm all done ===
print("\n Aggregations complete!")
print("Generated files: agg1.parquet, agg2.parquet, agg3.parquet")
