#  Stock Data Dashboard (Streamlit + Pandas + PyArrow)

A minimal project demonstrating data cleaning, aggregation, and visualization of stock market data using Python and Streamlit.

##  Objective
This project processes raw stock market data to:
1. Normalize and clean inconsistent values and formats.
2. Define and enforce a target schema (dates, strings, floats, bools).
3. Generate Parquet outputs for cleaned and aggregated data.
4. Visualize metrics interactively in Streamlit.

## 🗂️ Folder Structure
stocks/
├── raw_data.csv          # Original CSV
├── load_data.py                # Loads the data      
├── clean_data.py               # Cleans and normalizes schema
├── aggregate_data.py           # Builds aggregates (avg close, avg volume, returns)
├── streamlit_app.py            # Interactive Streamlit dashboard
├── cleaned.parquet             # Cleaned dataset output
├── agg1.parquet                # Daily avg close by ticker
├── agg2.parquet                # Avg volume by sector
├── agg3.parquet                # Daily returns by ticker
├── screenshot.zip
└── README.md
