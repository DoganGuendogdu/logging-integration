#!/bin/bash

SCRIPT_PATH="$(readlink -f "$BASH_SOURCE")"
BIN_DIR="$(dirname "$SCRIPT_PATH")"
BACKEND_DIR="$(dirname "$BIN_DIR")"
CONFIG_DIR="$BACKEND_DIR"/config

echo "Creating alert rules (alert-rules.yml) for Prometheus."

echo "Reading configuration from 'config.json'."

config_data=$(cat "$CONFIG_DIR"/config.json)

thresholds=$(echo "$config_data" | jq '.thresholds')
thresholds_array=$(echo "$thresholds" | jq '.[]')
total_cost=$(echo "$thresholds_array" | jq '.total_cost')
vodafone_cost=$(echo "$thresholds_array" | jq '.vodafone_cost')
telekom_cost=$(echo "$thresholds_array" | jq '.telekom_cost')
cost_1und1=$(echo "$thresholds_array" | jq '."1und1_cost"')

# if config file does not contain any data, raise error
# -z: Checks if length of string is zero
if [[ -z "$config_data" ]]; then
  echo "Failed to retrieve config data. File is empty."
  exit 1
fi

echo "Retrieving configuration for thresholds."

if [[ "$thresholds" == 'null' || -z "$thresholds" ]]; then
  echo "Error: 'thresholds' is missing or null or empty."
  exit 1
fi

if [[ "$thresholds_array" == 'null' || -z "$thresholds_array" ]]; then
  echo "Error: 'thresholds' array is missing or null or empty."
  exit 1
fi

if [[ "$total_cost" == "null" || -z "$total_cost" ]]; then
  echo "Error: 'total_cost' is missing or null or empty."
  exit 1
fi

if [[ "$vodafone_cost" == "null" || -z "$vodafone_cost" ]]; then
  echo "Error: 'vodafone_cost' is missing or null or empty."
  exit 1
fi

if [[ "$telekom_cost" == "null" || -z "$telekom_cost" ]]; then
  echo "Error: 'telekom_cost' is missing or null or empty."
  exit 1
fi

if [[ "$cost_1und1" == "null" || -z "$cost_1und1" ]]; then
  echo "Error: '1und1_cost' is missing or null or empty."
  exit 1
fi

export THRESHOLD_TOTAL_COST=$total_cost
export THRESHOLD_COST_VODAFONE=$vodafone_cost
export THRESHOLD_COST_TELEKOM=$telekom_cost
export THRESHOLD_COST_1UND1=$cost_1und1

echo "Successfully retrieved thresholds."

echo "Creating alert-rules-template.yml"

envsubst '${THRESHOLD_TOTAL_COST} ${THRESHOLD_COST_VODAFONE} ${THRESHOLD_COST_TELEKOM} ${THRESHOLD_COST_1UND1}'\
< "$CONFIG_DIR"/alert-rules-template.yml > "$CONFIG_DIR"/alert-rules.yml

echo "Successfully created alert-rules.yml."
