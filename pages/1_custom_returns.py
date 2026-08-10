from datetime import date, timedelta

import pandas as pd
import streamlit as st

from api_client import api_get

# --------------------------------------
# -------Display YTD returns best-------
# --------------------------------------
st.write("-----------------------")
st.title("Display top returns for chosen period of time")

with st.form("top_stocks_custom_period"):
    starting_date_given_period = st.date_input(
        "You can change the date if you want",
        date.today() - timedelta(2),
        key="key_start_date_given_period",
    )
    ending_date_given_period = st.date_input(
        "You can change the date if you want",
        date.today() - timedelta(1),
        key="key_end_date_given_period",
    )
    custom_returns_best_worst = st.selectbox(
        "Best or Worst?",
        ["best", "worst"],
        index=0,
    )
    custom_returns_number_stocks = st.selectbox(
        "How many stocks to list?",
        [30, 50, 100],
        index=1,
    )
    submitted_custom_period_top = st.form_submit_button(
        "Submit YTD best", key="key_custom_period_returns"
    )

if submitted_custom_period_top:
    data = api_get(
        f"returns/period/{st.session_state.key_start_date_given_period}/{st.session_state.key_end_date_given_period}/{custom_returns_number_stocks}/{custom_returns_best_worst}"
    )

    if data:
        try:
            df = pd.DataFrame(data)
            df = df[["ticker", "pct_change"]]
            st.dataframe(df, hide_index=True)
        except KeyError:
            st.write("Wrong date, try again")
