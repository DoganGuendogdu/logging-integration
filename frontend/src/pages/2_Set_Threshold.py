import streamlit as st 

with st.form("Total cost threshold"):
    st.write("Enter threshold to set total cost limit for all customers")
    input_threshold_total_cost = st.number_input("Enter value")
    submit_total_cost = st.form_submit_button("Submit")

with st.form("Vodafone cost threshold"):
    st.write("Enter threshold to set the cost limit for customer Vodafone")
    input_threshold_vodafone = st.number_input("Enter value")
    submit_cost_threshold_vodafone = st.form_submit_button("Submit")

with st.form("Telekom cost threshold"):
    st.write("Enter threshold to set the cost limit for customer Telekom")
    input_threshold_telekom = st.number_input("Enter value")
    submit_cost_threshold_telekom = st.form_submit_button("Submit")

with st.form("1und1 cost threshold"):
    st.write("Enter threshold to set the cost limit for customer 1und1")
    input_threshold_1und1 = st.number_input("Enter value")
    submit_cost_threshold_1und1 = st.form_submit_button("Submit")

if submit_total_cost:
    st.warning("HII")

if submit_cost_threshold_vodafone:
    pass

if submit_cost_threshold_telekom:
    pass

if submit_cost_threshold_1und1:
    pass