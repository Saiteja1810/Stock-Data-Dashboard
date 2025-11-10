import pandas as pd

# Load CSV
file_path = "raw_data.csv"
df = pd.read_csv(file_path)

# Inspect dataset
print("\n----- Dataset Shape -----")
print(df.shape)

print("\n----- Preview (First 5 Rows) -----")
print(df.head())

print("\n---- Column Names -----")
print(df.columns.tolist())

#Schema and Data Types
print("\n----- Data Types (Schema) -----")
print(df.dtypes)

#  Missing / Null Values Summary 
print("\n----- Missing Values per Column -----")
print(df.isna().sum())

# Quick Statistics
# Numeric-only statistics
print("\n----- Summary Statistics (Numeric Columns) -----")
print(df.describe())

# Non-numeric summary (categorical/text columns)
print("\n----- Summary Statistics (Categorical Columns) -----")
print(df.describe(include=['object']))
