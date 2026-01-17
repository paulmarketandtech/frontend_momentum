import os

import requests
import streamlit as st

# API_URL = "http://localhost:8000"
API_URL = os.getenv("API_URL", "http://localhost:8000")


def api_get(endpoint: str):
    try:
        response = requests.get(f"{API_URL}/{endpoint}", timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error("something is wrong with the connection")
        # st.error(f"API error: {e}")
        return None
    except requests.exceptions.Timeout:
        # st.warning("something is wrong with the connection")
        st.error("Request timed out.")
        return None
    except requests.exceptions.ConnectionError:
        # st.warning("something is wrong with the connection")
        st.error("Failed to connect to the server.")
        return None
    except requests.exceptions.HTTPError as e:
        # st.warning("something is wrong with the connection")
        st.error(f"HTTP error occurred: {e}")
        return None


# TODO: add logs
