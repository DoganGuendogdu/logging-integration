import streamlit as st

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
        