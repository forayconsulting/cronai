#!/bin/bash
# CRONAI Session Scheduler
# This script connects to MCP Servers via the Goose CLI tool
# and executes the configured AI commands

# Check if config file was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <config_file>"
  echo "Error: No configuration file specified"
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
  echo "Loaded global configuration"
fi

# Determine the goose command to use for MCP Server connection
GOOSE_CMD="goose"
if [ ! -z "$GOOSE_PATH" ]; then
  GOOSE_CMD="$GOOSE_PATH"
  echo "Using custom Goose path: $GOOSE_PATH"
fi

# Execute the commands via Goose CLI to connect to MCP Server
echo "Starting AI session with configuration: $(basename "$CONFIG_FILE")"
echo "Connecting to MCP Server via Goose..."

# Start the session with the configured commands
$GOOSE_CMD session <<EOF
$(for cmd in "${commands[@]}"; do echo "$cmd"; done)
EOF

# Check the exit status
if [ $? -eq 0 ]; then
  echo "AI session completed successfully"
else
  echo "AI session encountered an error"
fi

exit 0
