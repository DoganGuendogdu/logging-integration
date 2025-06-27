from pathlib import Path

import requests
import streamlit as st
from dotenv import dotenv_values

FRONTEND_DIR_PATH = Path(__file__).resolve().parent.parent.parent

try:
    config = dotenv_values(FRONTEND_DIR_PATH / ".env")
except FileNotFoundError as e:
    raise e

ENDPOINT_INFO_LOG = config.get("ENDPOINT_INFO_LOG")
ENDPOINT_DEBUG_LOG = config.get("ENDPOINT_DEBUG_LOG")
ENDPOINT_WARNING_LOG = config.get("ENDPOINT_WARNING_LOG")
ENDPOINT_ERROR_LOG = config.get("ENDPOINT_ERROR_LOG")
ENDPOINT_CRITICAL_LOG = config.get("ENDPOINT_CRITICAL_LOG")

with st.container():
    st.session_state["info_level"] = st.button("Info")
    st.session_state["debug_level"] = st.button("Debug")
    st.session_state["warning_level"] = st.button("Warning")
    st.session_state["error_level"] = st.button("Error")
    st.session_state["critical_level"] = st.button("Critical")

    if st.session_state["info_level"]:
        try:
            requests.post(ENDPOINT_DEBUG_LOG, json={"message": "Hello from INFO message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["info_level"] = False

    if st.session_state["debug_level"]:
        try:
            requests.post(ENDPOINT_DEBUG_LOG, json={"message": "Hello from DEBUG message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["debug_level"] = False

    if st.session_state["warning_level"]:
        try:
            requests.post(ENDPOINT_WARNING_LOG, json={"message": "Hello from WARNING message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["warning_level"] = False

    if st.session_state["error_level"]:
        try:
            requests.post(ENDPOINT_ERROR_LOG, json={"message": "Hello from ERROR message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["error_level"] = False

    if st.session_state["critical_level"]:
        try:
            requests.post(ENDPOINT_CRITICAL_LOG, json={"message": "Hello from CRITICAL message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["critical_level"] = False
