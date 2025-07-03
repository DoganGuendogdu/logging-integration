#!/bin/bash

SCRIPT_PATH="$(readlink -f "$BASH_SOURCE")"
BIN_DIR="$(dirname "$SCRIPT_PATH")"
APP_HOME="$(dirname "$BIN_DIR")"
PROMETHEUS_DIR="$APP_HOME"/prometheus

echo "Creating alert rules (alert-rules.yml) for Prometheus."

echo "Reading configuration from 'config.json'."

data=$(cat "$PROMETHEUS_DIR"/config.json)

# if config file does not contain any data, raise error
# -z: Checks if length of string is zero
if [[ -z "$data" ]]; then
  echo "Failed to retrieve config data. File is empty."
  exit 1
fi

echo "Retrieving configuration for thresholds."

thresholds=$(echo "$data" | jq '.thresholds')
thresholds_array=$(echo "$thresholds" | jq '.[]')
total_cost=$(echo "$thresholds_array" | jq '.total_cost')
vodafone_cost=$(echo "$thresholds_array" | jq '.vodafone_cost')
telekom_cost=$(echo "$thresholds_array" | jq '.telekom_cost')
cost_1und1=$(echo "$thresholds_array" | jq '."1und1_cost"')

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

echo "Successfully retrieved thresholds."

#echo "Successfully created alert-rules.yml."

echo "$thresholds"
echo "$total_cost"
echo "$vodafone_cost"
echo "$telekom_cost"
echo "$cost_1und1"
