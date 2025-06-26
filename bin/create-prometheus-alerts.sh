#!/bin/bash

SCRIPT_PATH="$(readlink -f "$BASH_SOURCE")"      
BIN_DIR="$(dirname "$SCRIPT_PATH")"               
APP_HOME="$(dirname "$BIN_DIR")"

PROMETHEUS_DIR="$APP_HOME"/prometheus

echo "Creating alert rules (alert-rules.yml) from template file for Prometheus."

if [[ ! -e ${PROMETHEUS_DIR} ]]; then
    echo "Failed to create aler rules."
    echo "dir '${PROMETHEUS_DIR}' does not exist."
    exit 1 
fi

# grep -v '^#': grep contents from .env file while line does not match char '#' to ignore comments
# | xargs: redirect env variables (as key-value pairs) to convert those into a single line argument list 
# export: export env variables in shell by providing all vairables as a single line 
export $(grep -v '^#' "$APP_HOME"/.env | xargs)

# envsubst: environment variable substitution by providing template files as input. Here, env var replaces by env var in shell
# explicitily tell which env var to use to prevent unindentend overwriting of vars 
# '>': redirect output to alert configuration file
envsubst '${THRESHOLD_TOTAL_COST} ${THRESHOLD_COST_VODAFONE} ${THRESHOLD_COST_TELEKOM} ${THRESHOLD_COST_1UND1}'\
< "$PROMETHEUS_DIR"/alert-rules-template.yml > "$PROMETHEUS_DIR"/alert-rules.yml

echo "Successfully created alert-rules.yml."
