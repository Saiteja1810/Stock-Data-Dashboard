import streamlit as st
import pandas as pd

st.set_page_config(page_title=" Stock Dashboard", layout="wide")

st.title(" Stock Data Dashboard")
st.write("Visualizing daily average close, volume by sector, and daily returns.")

#  Load aggregated parquet files 
@st.cache_data
def load_parquets():
    agg1 = pd.read_parquet("agg1.parquet")
    agg2 = pd.read_parquet("agg2.parquet")
    agg3 = pd.read_parquet("agg3.parquet")
    return agg1, agg2, agg3

agg1, agg2, agg3 = load_parquets()

#  Filters
# Convert trade_date to datetime
agg1["trade_date"] = pd.to_datetime(agg1["trade_date"], errors="coerce")
agg3["trade_date"] = pd.to_datetime(agg3["trade_date"], errors="coerce")

tickers = sorted(agg1["ticker"].dropna().unique().tolist())
selected_ticker = st.sidebar.selectbox("Select Ticker", tickers)

min_date = agg1["trade_date"].min()
max_date = agg1["trade_date"].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

start_date, end_date = pd.to_datetime(date_range)

# Filter data 
filtered_agg1 = agg1[
    (agg1["ticker"] == selected_ticker)
    & (agg1["trade_date"].between(start_date, end_date))
]

filtered_agg3 = agg3[
    (agg3["ticker"] == selected_ticker)
    & (agg3["trade_date"].between(start_date, end_date))
]

#  Charts 
tab1, tab2, tab3 = st.tabs([" Daily Average Close", " Volume by Sector", " Daily Returns"])

with tab1:
    st.subheader(f"Daily Average Close — {selected_ticker}")
    st.line_chart(filtered_agg1.set_index("trade_date")["avg_close_price"])

with tab2:
    st.subheader("Average Volume by Sector")
    st.bar_chart(agg2.set_index("sector")["avg_volume"])

with tab3:
    st.subheader(f"Daily Return (%) — {selected_ticker}")
    st.line_chart(filtered_agg3.set_index("trade_date")["daily_return"])

# Data preview 
with st.expander(" View Raw Data"):
    st.write("### Aggregated Data Samples")
    st.write("**agg1 — Daily Avg Close**")
    st.dataframe(filtered_agg1)
    st.write("**agg2 — Avg Volume by Sector**")
    st.dataframe(agg2)
    st.write("**agg3 — Daily Return**")
    st.dataframe(filtered_agg3)

st.success(" Dashboard loaded successfully!")
