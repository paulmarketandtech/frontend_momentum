from datetime import date, timedelta

import streamlit as st

from api_client import api_get

# --------------------------------------
# ------Display 52 week highs/lows------
# --------------------------------------
st.title("Disply number of tickers processed yesterday")

with st.form("Metadata buttons"):
    all_available_tickers = st.form_submit_button("List all available tickers")

if all_available_tickers:
    data = api_get("meta_data/tickers_by_exchange")
    if data:
        try:
            st.write(f"Number of all available tickers: {data['total_combined_count']}")
        except KeyError:
            st.write("Wrong date, try again")

st.write("-----------------------")

with st.form("yesterday_number_of_tickers"):
    chosen_date = st.date_input("Pick a date", value=date.today() - timedelta(1))

    yesterday_number_of_tickers = st.form_submit_button("Show number of tickers")
    list_all_yesterday_processed_tickers = st.form_submit_button(
        "Show all of yesterday's tickers"
    )

if yesterday_number_of_tickers:
    data = api_get(f"meta_data/downloaded_tickers/{chosen_date}")
    if data:
        try:
            st.write(f"Number of processed tickers: {data['number_processed_tickers']}")
        except KeyError:
            st.error("Wrong date")
    else:
        print(f"Request failed with status code: {data}")

if list_all_yesterday_processed_tickers:
    data = api_get(f"meta_data/downloaded_tickers/{chosen_date}")
    if data:
        try:
            st.write(f"Number of processed tickers: {data['result_processed_data']}")
        except KeyError:
            st.error("Wrong date")
    else:
        print(f"Request failed with status code: {data}")
st.write("-----------------------")
