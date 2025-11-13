#  Stock Data Dashboard (Streamlit + Pandas + PyArrow)

A minimal project demonstrating data cleaning, aggregation, and visualization of stock market data using Python and Streamlit.

##  Objective
This project processes raw stock market data to:
1. Normalize and clean inconsistent values and formats.
2. Define and enforce a target schema (dates, strings, floats, bools).
3. Generate Parquet outputs for cleaned and aggregated data.
4. Visualize metrics interactively in Streamlit.

## 🚀 Key Features
- Data cleaning and preprocessing
- Aggregated datasets:
  • Daily average close per ticker
  • Average volume per sector
  • Daily returns per ticker
- Streamlit dashboard for data exploration
- Parquet outputs for efficient loading

##  Project Structure
stocks/
├── raw_data.csv
├── load_data.py
├── clean_data.py
├── aggregate_data.py
├── streamlit_app.py
├── cleaned.parquet
├── agg1.parquet
├── agg2.parquet
├── agg3.parquet
├── screenshot.zip
└── README.md

##  Data Description
raw_data.csv contains columns:
date, ticker, open, high, low, close, volume, sector

Outputs:
cleaned.parquet – cleaned dataset
agg1.parquet – daily avg close per ticker
agg2.parquet – avg volume by sector
agg3.parquet – daily returns

##  Pipeline Steps
1) Load Raw Data:
   python load_data.py

2) Clean Data:
   python clean_data.py

3) Create Aggregates:
   python aggregate_data.py

##  Run Dashboard
streamlit run streamlit_app.py

##  Screenshots
Screenshots available in screenshot.zip

##  How to Use
1. Add raw_data.csv
2. Run all three scripts
3. Launch Streamlit dashboard
4. Explore visualizations

## License
Open for personal and educational use.
