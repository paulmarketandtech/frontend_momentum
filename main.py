import streamlit as st

custom_returns = st.Page("custom_returns.py", title="custom returns")
standard_returns = st.Page("standard_returns.py", title="standard returns")
ticker_basic_data = st.Page("stock_basic_data.py", title="Stock basic data")
year_high = st.Page("year_high.py", title="52 week highs and lows")
# metadata = st.Page("foo.py", title="DB Metadata")

pg = st.navigation(
    [custom_returns, standard_returns, ticker_basic_data, year_high, metadata]
)
pg.run()
