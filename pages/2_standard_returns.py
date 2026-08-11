from datetime import date, timedelta

import pandas as pd
import streamlit as st

from api_client import api_get

# --------------------------------------
# -------Display YTD returns best-------
# --------------------------------------
st.write("-----------------------")
st.title("YTD best/worst stocks")

with st.form("ytd_best_form"):
    chosen_date_ytd_best = st.date_input(
        "You can change the date if you want",
        date.today() - timedelta(1),
        key="key_ytd_best_date",
    )
    ytd_best_or_worst = st.selectbox(
        "Best or Worst?",
        ["ytd-best", "ytd-worst"],
        index=0,
    )
    submitted_ytd_best = st.form_submit_button("Submit YTD best", key="key_ytd_best")

if submitted_ytd_best:
    data = api_get(f"returns/{ytd_best_or_worst}/{st.session_state.key_ytd_best_date}")
    if data:
        try:
            df = pd.DataFrame(data)
            df = df[["ticker", "pct_change"]]
            st.dataframe(df, hide_index=True)
        except KeyError:
            st.write("Wrong date, try again")
