from datetime import date, timedelta

import pandas as pd
import streamlit as st

from api_client import api_get

# --------------------------------------
# ------Display 52 week highs/lows------
# --------------------------------------
st.write("-----------------------")
st.title("52 Week Highs/Lows")

with st.form("52_week_high_low"):
    yesterday_52week_highs = st.form_submit_button(
        "Display yesterday's 52week highs", key="key_ytd_best"
    )

    last_week_52week_highs = st.form_submit_button("Display last week 52week highs")
    yesterday_52week_lows = st.form_submit_button("Display yesterday's 52week lows")
    last_week_52week_lows = st.form_submit_button("Display last week 52week lows")

if yesterday_52week_highs:
    data = api_get("prices/year_high")
    if data:
        try:
            st.write(
                f"Number of new highs yestarday: {data['yesterday_new_highs_number']}"
            )
            df = pd.DataFrame(
                data["yesterday_new_highs_tickers"], columns=["Ticker", "Date"]
            )
            st.dataframe(df)
        except KeyError:
            st.write("Wrong date, try again")

if last_week_52week_highs:
    data = api_get("prices/year_high")
    if data:
        try:
            st.write(
                f"Number of new highs last week: {data['last_week_new_highs_number']}"
            )
            df = pd.DataFrame(
                data["last_week_new_highs_tickers"], columns=["Ticker", "Date"]
            )
            st.dataframe(df)
        except KeyError:
            st.write("Wrong date, try again")

if yesterday_52week_lows:
    data = api_get("prices/year_low")
    if data:
        try:
            st.write(
                f"Number of new lows yestarday: {data['yesterday_new_lows_number']}"
            )
            df = pd.DataFrame(
                data["yesterday_new_lows_tickers"], columns=["Ticker", "Date"]
            )
            st.dataframe(df)
        except KeyError:
            st.write("Wrong date, try again")

if last_week_52week_lows:
    data = api_get("prices/year_low")
    if data:
        try:
            st.write(
                f"Number of new lows last week: {data['last_week_new_lows_number']}"
            )
            df = pd.DataFrame(
                data["last_week_new_lows_tickers"], columns=["Ticker", "Date"]
            )
            st.dataframe(df)
        except KeyError:
            st.write("Wrong date, try again")
