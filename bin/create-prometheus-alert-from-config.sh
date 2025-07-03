#!/bin/bash

SCRIPT_PATH="$(readlink -f "$BASH_SOURCE")"
BIN_DIR="$(dirname "$SCRIPT_PATH")"
APP_HOME="$(dirname "$BIN_DIR")"
PROMETHEUS_DIR="$APP_HOME"/prometheus


data=$(cat "$PROMETHEUS_DIR"/config.json)

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
