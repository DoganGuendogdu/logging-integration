from pathlib import Path

import requests
import streamlit as st
from dotenv import dotenv_values

FRONTEND_DIR_PATH = Path(__file__).resolve().parent.parent.parent

try:
    config = dotenv_values(FRONTEND_DIR_PATH / ".env")
except FileNotFoundError as e:
    raise e

ENDPOINT_THRESHOLD_COST = config.get("ENDPOINT_THRESHOLD_COST")


def check_if_cost_thresholds_less_or_equal_than_total_threshold(total_cost_threshold: float,
                                                                vodafone_cost_threshold: float,
                                                                telekom_cost_threshold: float,
                                                                _1und1_cost_threshold: float):
    customer_cost_threshold_sum = vodafone_cost_threshold + telekom_cost_threshold + _1und1_cost_threshold

    if customer_cost_threshold_sum > total_cost_threshold:
        return False
    return True


with st.form("Set thresholds"):
    st.write("Enter threshold to set total cost limit for all customers")
    input_threshold_total_cost = st.number_input("Enter value - total cost threshold")

    st.write("Enter threshold to set the cost limit for customer Vodafone")
    input_threshold_vodafone = st.number_input("Enter value - Vodafone cost threshold ")

    st.write("Enter threshold to set the cost limit for customer Telekom")
    input_threshold_telekom = st.number_input("Enter value - Telekom cost threshold")

    st.write("Enter threshold to set the cost limit for customer 1und1")
    input_threshold_1und1 = st.number_input("Enter value - 1und1 cost threshold")

    submit_thresholds = st.form_submit_button("Submit")

if submit_thresholds:
    customer_threshold_check = check_if_cost_thresholds_less_or_equal_than_total_threshold(input_threshold_total_cost,
                                                                                           input_threshold_vodafone,
                                                                                           input_threshold_telekom,
                                                                                           input_threshold_1und1)

    if not customer_threshold_check:
        st.error("Please verify that the total cost threshold is not exceeded!")
    else:
        try:
            result = requests.post(ENDPOINT_THRESHOLD_COST, json={"total_costs": input_threshold_total_cost,
                                                                  "vodafone_cost": input_threshold_vodafone,
                                                                  "telekom_cost": input_threshold_telekom,
                                                                  "cost_1und1": input_threshold_1und1})

            # TODO: Handle error cases if status != 200
            if result.status_code == 200:
                st.success("Thresholds have been set!")
            else:
                st.error(f"Error while sending reques to endpint: {result.reason}")
        except requests.exceptions.RequestException as e:
            raise e
