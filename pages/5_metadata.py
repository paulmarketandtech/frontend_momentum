from datetime import date, timedelta

import streamlit as st

from api_client import api_get

# --------------------------------------
# --------Display DB metadata--------
# --------------------------------------

st.title("Display tickers above given MC")

with st.form("ticker above mc"):
    market_cap = st.number_input(
        "Enter market cap", value=None, step=1, placeholder="Type above what MC?"
    )
    number_above_mc_tickers = st.form_submit_button("Number of all available tickers")
    tickers_above_mc = st.form_submit_button("List all nasdaq tickers")


if market_cap is not None:
    data_above_mc = api_get(f"meta_data/tickers_above_mc/{market_cap}")
    if number_above_mc_tickers and data_above_mc:
        st.write(
            f"Number of tickers above given MC: {data_above_mc['number_of_tickers']}"
        )

    if tickers_above_mc and data_above_mc:
        st.write(f"All tickers above given MC: {data_above_mc['tickers_above_mc']}")

st.write("-----------------------")

st.title("Display all available tickers")

with st.form("Ticker by exchange"):
    number_available_tickers = st.form_submit_button("Number of all available tickers")
    all_nasdaq_tickers = st.form_submit_button("List all nasdaq tickers")
    number_nasdaq_tickers = st.form_submit_button("Number of all nasdaq tickers")
    all_nyse_tickers = st.form_submit_button("List all nyse tickers")
    number_nyse_tickers = st.form_submit_button("Number of all nyse tickers")

data_exchange = api_get("meta_data/tickers_by_exchange")
if number_available_tickers:
    if data_exchange:
        st.write(
            f"Number of all available tickers: {data_exchange['total_combined_count']}"
        )
    else:
        st.error("Something went wrong")

if all_nasdaq_tickers:
    if data_exchange:
        st.write(f"List of all Nasdaq tickers: {data_exchange['nasdaq']['tickers']}")
    else:
        st.error("Something went wrong")

if number_nasdaq_tickers:
    if data_exchange:
        st.write(f"Number of all Nasdaq tickers: {data_exchange['nasdaq']['count']}")
    else:
        st.error("Something went wrong")

if all_nyse_tickers:
    if data_exchange:
        st.write(
            st.write(f"List of all Nyse tickers: {data_exchange['nyse']['tickers']}")
        )
    else:
        st.error("Something went wrong")

if number_nyse_tickers:
    if data_exchange:
        st.write(f"Number of all available tickers: {data_exchange['nyse']['count']}")
    else:
        st.error("Something went wrong")

st.write("-----------------------")

st.title("Display number of tickers processed in a given day")

with st.form("yesterday_number_of_tickers"):
    chosen_date = st.date_input("Pick a date", value=date.today() - timedelta(1))

    number_of_processed_tickers = st.form_submit_button("Show number of tickers")
    list_all_yesterday_processed_tickers = st.form_submit_button(
        "Show all of processed tickers"
    )

data_processed_tickers = api_get(f"meta_data/processed_tickers/{chosen_date}")
if number_of_processed_tickers:
    if data_processed_tickers:
        try:
            st.write(
                f"Number of processed tickers: {data_processed_tickers['number_processed_tickers']}"
            )
        except KeyError:
            st.error("Wrong date")
    else:
        print(f"Request failed with status code: {data_processed_tickers}")

if list_all_yesterday_processed_tickers:
    if data_processed_tickers:
        try:
            st.write(
                f"List of processed tickers: {data_processed_tickers['result_processed_data']}"
            )
        except KeyError:
            st.error("Wrong date")
    else:
        print(f"Request failed with status code: {data_processed_tickers}")

st.write("-----------------------")
