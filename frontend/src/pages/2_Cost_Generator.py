from pathlib import Path
from random import randint

import requests
import streamlit as st
from dotenv import dotenv_values

FRONTEND_DIR_PATH = Path(__file__).resolve().parent.parent.parent

try:
    config = dotenv_values(FRONTEND_DIR_PATH / ".env")
except FileNotFoundError as e:
    raise e

ENDPOINT_COST_VODAFONE = config.get("ENDPOINT_COST_VODAFONE")
ENDPOINT_COST_TELEKOM = config.get("ENDPOINT_COST_TELEKOM")
ENDPOINT_COST_1UND1 = config.get("ENDPOINT_COST_1UND1")
ENDPOINT_THRESHOLD_COST = config.get("ENDPOINT_THRESHOLD_COST")


def generate_random_value_between_5_and_20_as_str():
    return str(randint(5, 20))


with st.container():
    st.session_state["costs_vodafone"] = st.button("Generate random costs for Vodafone", type="primary")
    st.session_state["costs_telekom"] = st.button("Generate random costs for Telekom", type="primary")
    st.session_state["costs_1und1"] = st.button("Generate random costs for 1&1", type="primary")

    if st.session_state["costs_vodafone"]:
        try:
            requests.post(ENDPOINT_COST_VODAFONE, json={"cost": generate_random_value_between_5_and_20_as_str()})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["costs_vodafone"] = False

    if st.session_state["costs_telekom"]:
        try:
            requests.post(ENDPOINT_COST_TELEKOM, json={"cost": generate_random_value_between_5_and_20_as_str()})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["costs_telekom"] = False

    if st.session_state["costs_1und1"]:
        try:
            requests.post(ENDPOINT_COST_1UND1, json={"cost": generate_random_value_between_5_and_20_as_str()})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["costs_1und1"] = False
