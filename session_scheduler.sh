#!/bin/bash
# Check if config file was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <config_file>"
  exit 1
fi

CONFIG_FILE="$1"

# Check if config file exists
if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: Config file $CONFIG_FILE not found!"
  exit 1
fi

# Load configuration
source "$CONFIG_FILE"

# Check if GOOSE_PATH is set in config.sh, use it if available
if [ -f "$(dirname "$0")/config.sh" ]; then
  source "$(dirname "$0")/config.sh"
fi

# Determine the goose command to use
GOOSE_CMD="goose"
if [ ! -z "$GOOSE_PATH" ]; then
  GOOSE_CMD="$GOOSE_PATH"
fi

# Execute the commands using the goose command
echo "Starting session with configuration: $(basename "$CONFIG_FILE")"
$GOOSE_CMD session <<EOF
$(for cmd in "${commands[@]}"; do echo "$cmd"; done)
EOF

exit 0
