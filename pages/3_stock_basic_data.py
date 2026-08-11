from datetime import date, timedelta

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
