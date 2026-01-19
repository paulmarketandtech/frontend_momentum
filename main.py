import streamlit as st

custom_returns = st.Page("custom_returns.py", title="custom returns")
standard_returns = st.Page("standard_returns.py", title="standard returns")
ticker_basic_data = st.Page("stock_basic_data.py", title="Stock basic data")

pg = st.navigation([custom_returns, standard_returns, ticker_basic_data])
pg.run()
