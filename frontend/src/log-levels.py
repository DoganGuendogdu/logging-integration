import streamlit as st
import yaml

try:
    with open("../config.yml") as config_file:
        config = yaml.safe_load(config_file)
except FileNotFoundError as e:
    raise e

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
        st.write("Info")
        st.session_state["info_level"] = False

    if st.session_state["debug_level"]:
        st.write("Debug")
        st.session_state["debug_level"] = False
    
    if st.session_state["warning_level"]:
        st.write("Warning")
        st.session_state["warning_level"] = False
    
    if st.session_state["error_level"]:
        st.write("Error")
        st.session_state["error_level"] = False

    if st.session_state["critical_level"]:
        st.write("Critical")
        st.session_state["critical_level"] = False
