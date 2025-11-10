import pandas as pd
import numpy as np

# Load the raw CSV 
file_path = "raw_data.csv"
df = pd.read_csv(file_path)
print(" Raw data loaded successfully!")
print(f"Original shape: {df.shape}")

# Normalize schema
df.columns = (
    df.columns.str.strip()          
              .str.lower()          
              .str.replace(' ', '_')
              .str.replace('-', '_')
)
print("\n Normalized column names:")
print(df.columns.tolist())


#  Map obvious missing values to NaN 
missing_values = ["", " ", "-", "na", "n/a", "null", "none", "Na", "NA", "NaN"]
df.replace(missing_values, np.nan, inplace=True)

# Trim spaces and lowercase for string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.lower().replace("nan", np.nan)

#  Fix date format to yyyy-MM-dd 
if "trade_date" in df.columns:
    df["trade_date"] = pd.to_datetime(df["trade_date"], errors="coerce")
    df["trade_date"] = df["trade_date"].dt.strftime("%Y-%m-%d")

#  Define target schema 
# (dates, strings, ints, floats, bools)
target_schema = {
    "trade_date": "string",      
    "ticker": "string",
    "open_price": "float64",
    "close_price": "float64",
    "volume": "float64",
    "sector": "string",
    "validated": "string",      
    "currency": "string",
    "exchange": "string",
    "notes": "string"
}

# Apply type conversion
for col, dtype in target_schema.items():
    if col in df.columns:
        try:
            df[col] = df[col].astype(dtype)
        except Exception as e:
            print(f" Could not convert {col} to {dtype}: {e}")

# Deduplicate rows 
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)
print(f"\n Removed {before - after} duplicate rows")

# Null summary 
print("\n Null values per column after cleaning:")
print(df.isna().sum())

# Save as cleaned.parquet
output_path = "cleaned.parquet"
df.to_parquet(output_path, index=False)
print(f"\n Cleaned dataset saved successfully as '{output_path}'")
