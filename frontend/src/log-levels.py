import streamlit as st
import yaml
import requests 
from pathlib import Path
from random import randint

ROOT_PATH = Path(__file__).resolve().parent.parent

try:
    with open(ROOT_PATH / "config.yml") as config_file:
        config = yaml.safe_load(config_file)
except FileNotFoundError as e:
    raise e

def generate_random_value_between_5_and_20():
    return randint(5, 20)

ENDPOINTS = config["backend"]["endpoints"]
INFO_ENDPOINT = ENDPOINTS["info"]
DEBUG_ENDPOINT = ENDPOINTS["debug"]
WARNING_ENDPOINT = ENDPOINTS["warning"]
ERROR_ENDPOINT = ENDPOINTS["error"]
CRITICAL_ENDPOINT = ENDPOINTS["critical"]

with st.container():
    st.session_state["info_level"] = st.button("Info")
    st.session_state["debug_level"] = st.button("Debug")
    st.session_state["warning_level"] = st.button("Warning")
    st.session_state["error_level"] = st.button("Error")
    st.session_state["critical_level"] = st.button("Critical")
    
    if st.session_state["info_level"]:
        requests.post(INFO_ENDPOINT, json={"message": "Hello from INFO message!"})
        st.session_state["info_level"] = False

    if st.session_state["debug_level"]:
        requests.post(DEBUG_ENDPOINT, json={"message": "Hello from DEBUG message!"})
        st.session_state["debug_level"] = False
    
    if st.session_state["warning_level"]:
        requests.post(WARNING_ENDPOINT,json={"message": "Hello from WARNING message!"} )
        st.session_state["warning_level"] = False
    
    if st.session_state["error_level"]:
        requests.post(ERROR_ENDPOINT,json={"message": "Hello from ERROR message!"} )
        st.session_state["error_level"] = False

    if st.session_state["critical_level"]:
        requests.post(CRITICAL_ENDPOINT,json={"message": "Hello from CRITICAL message!"} )
        st.session_state["critical_level"] = False

with st.container():
    st.session_state["costs_vodafone"] = st.button("Generate random costs for Vodafone", type="primary")
    st.session_state["costs_telekom"] = st.button("Generate random costs for Telekom", type="primary")
    st.session_state["costs_1und1"] = st.button("Generate random costs for 1&1", type="primary")

    if st.session_state["costs_vodafone"]:
        generate_random_value_between_5_and_20()
        st.session_state["costs_vodafone"] = False
    
    if st.session_state["costs_telekom"]:
        generate_random_value_between_5_and_20()
        st.session_state["costs_telekom"] = False

    if st.session_state["costs_1und1"]:
        generate_random_value_between_5_and_20()
        st.session_state["costs_1und1"] = False
