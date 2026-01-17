from datetime import date, timedelta

import pandas as pd
import requests
import streamlit as st

from api_client import api_get

# --------------------------------------
# ------Display single stock data-------
# --------------------------------------
st.title("Show price for a single stock from a sepcific date")

st.markdown("Provide a ticker, choose a date and select OHCL")

with st.form("single_stock_form"):
    single_ticker = st.text_input(
        "Enter a ticker", placeholder="ticker here", key="key_single_ticker"
    )
    chosen_date = st.date_input("Pick a date", value=date.today() - timedelta(1))

    submitted = st.form_submit_button("Submit", key="single_ticker_ohcl_data")

if submitted:
    if not single_ticker or chosen_date is None:
        st.error("Please fill all fields before processing.")
    else:
        data = api_get(f"prices/{single_ticker}/{chosen_date}")
        if data:
            try:
                st.write(f"Close: {round(data['close'],2)}")
                st.write(f"Open:{round(data['open'],2)}")
                st.write(f"High:{round(data['high'],2)}")
                st.write(f"Low:{round(data['low'],2)}")
            except KeyError:
                st.error("Wrong date")
        else:
            print(f"Request failed with status code: {data}")

# --------------------------------------
# -------Display YTD returns best-------
# --------------------------------------
st.write("-----------------------")
st.title("YTD best stocks")

with st.form("ytd_best_form"):
    chosen_date_ytd_best = st.date_input(
        "You can change the date if you want",
        date.today() - timedelta(1),
        key="key_ytd_best_date",
    )
    submitted_ytd_best = st.form_submit_button("Submit YTD best", key="key_ytd_best")

if submitted_ytd_best:
    data = api_get(f"returns/ytd-best/{st.session_state.key_ytd_best_date}")
    if data:
        try:
            df = pd.DataFrame(data)
            df = df[["ticker", "pct_change"]]
            st.dataframe(df, hide_index=True)
        except KeyError:
            st.write("Wrong date, try again")

# --------------------------------------
# -------Display YTD returns worst------
# --------------------------------------
st.write("-----------------------")
st.title("YTD worst stocks")

with st.form("ytd_worst_form"):
    chosen_date_ytd_worst = st.date_input(
        "You can change the date if you want",
        date.today() - timedelta(1),
        key="key_ytd_worst_date",
    )
    submitted_ytd_worst = st.form_submit_button("Submit YTD worst", key="key_ytd_worst")

if submitted_ytd_worst:
    data = api_get(f"returns/ytd-worst/{st.session_state.key_ytd_worst_date}")
    if data:
        try:
            df = pd.DataFrame(data)
            df = df[["ticker", "pct_change"]]
            st.dataframe(df, hide_index=True)
        except KeyError:
            st.write("Wrong date, try again")

# TODO:
# create pages in streamlit
