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

def generate_random_value_between_5_and_20_as_str():
    return str(randint(5, 20))

ENDPOINTS = config["backend"]["endpoints"]

INFO_ENDPOINT = ENDPOINTS["info"]
DEBUG_ENDPOINT = ENDPOINTS["debug"]
WARNING_ENDPOINT = ENDPOINTS["warning"]
ERROR_ENDPOINT = ENDPOINTS["error"]
CRITICAL_ENDPOINT = ENDPOINTS["critical"]

COST_VODAFONE_ENDPOINT = ENDPOINTS["cost_vodafone"]
COST_TELEKOM_ENDPOINT = ENDPOINTS["cost_telekom"]
COST_1UND1_ENDPOINT = ENDPOINTS["cost_1und1"]

with st.container():
    st.session_state["info_level"] = st.button("Info")
    st.session_state["debug_level"] = st.button("Debug")
    st.session_state["warning_level"] = st.button("Warning")
    st.session_state["error_level"] = st.button("Error")
    st.session_state["critical_level"] = st.button("Critical")
    
    if st.session_state["info_level"]:
        try:
         requests.post(INFO_ENDPOINT, json={"message": "Hello from INFO message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["info_level"] = False

    if st.session_state["debug_level"]:
        try:
            requests.post(DEBUG_ENDPOINT, json={"message": "Hello from DEBUG message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["debug_level"] = False
    
    if st.session_state["warning_level"]:
        try:
            requests.post(WARNING_ENDPOINT,json={"message": "Hello from WARNING message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["warning_level"] = False
    
    if st.session_state["error_level"]:
        try:
            requests.post(ERROR_ENDPOINT,json={"message": "Hello from ERROR message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["error_level"] = False

    if st.session_state["critical_level"]:
        try:
            requests.post(CRITICAL_ENDPOINT,json={"message": "Hello from CRITICAL message!"})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["critical_level"] = False

with st.container():
    st.session_state["costs_vodafone"] = st.button("Generate random costs for Vodafone", type="primary")
    st.session_state["costs_telekom"] = st.button("Generate random costs for Telekom", type="primary")
    st.session_state["costs_1und1"] = st.button("Generate random costs for 1&1", type="primary")

    if st.session_state["costs_vodafone"]:
        try:
            requests.post(COST_VODAFONE_ENDPOINT, json={"cost": generate_random_value_between_5_and_20_as_str()})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["costs_vodafone"] = False
    
    if st.session_state["costs_telekom"]:
        try:
            requests.post(COST_TELEKOM_ENDPOINT, json={"cost": generate_random_value_between_5_and_20_as_str()})
        except requests.exceptions.RequestException as e:
            raise e
        st.session_state["costs_telekom"] = False

    if st.session_state["costs_1und1"]:
        try:
            requests.post(COST_1UND1_ENDPOINT, json={"cost": generate_random_value_between_5_and_20_as_str()})
        except requests.exceptions.RequestException as e: 
            raise e
        st.session_state["costs_1und1"] = False
