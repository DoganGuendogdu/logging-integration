import streamlit as st

st.set_page_config(
    page_title="Welcome"
)

st.title("Welcome to the POC app!")

st.markdown(
    """
    The goal of the POC app is to implement a way to observe an already running application.
    Moreover, it enables iteraction with specific application metrics like thresholds.  
    
    **👈 Select the** ***Cost Generator*** **page** to generate random customer costs, which will be then stored as metric data in Prometheus
    and visualized via Grafana.  

    **👈 Select the** ***Set Threshold*** **page** to define thresholds for customer costs. 
    """
)
