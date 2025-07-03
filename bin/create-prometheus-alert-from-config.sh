#!/bin/bash

SCRIPT_PATH="$(readlink -f "$BASH_SOURCE")"
BIN_DIR="$(dirname "$SCRIPT_PATH")"
APP_HOME="$(dirname "$BIN_DIR")"
PROMETHEUS_DIR="$APP_HOME"/prometheus


data='{"thresholds":[{"total_cost": 33333.0,"vodafone_cost": 22.0,"telekom_cost": 0.0,"1und1_cost":3.0}]}'
thresholds=$(echo "$data" | jq '.thresholds[]')

total_cost=$(echo "$thresholds" | jq '.total_cost')
vodafone_cost=$(echo "$thresholds" | jq '.vodafone_cost')
telekom_cost=$(echo "$thresholds" | jq '.telekom_cost')
cost_1und1=$(echo "$thresholds" | jq '."1und1_cost"')

echo "$thresholds"
echo "$total_cost"
echo "$vodafone_cost"
echo "$telekom_cost"
echo "$cost_1und1"
