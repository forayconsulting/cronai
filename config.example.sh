#!/bin/bash
# CRONAI - Example Configuration File
# Make a copy of this file named config.sh and adjust the values for your environment
# This configuration is designed for integrating with MCP Servers via Goose CLI

# Base directory for the application
# This should be the directory where the CRONAI app is installed
CRONAI_BASE_DIR="/path/to/your/cronai"

# Directory where configuration files are stored
CONFIG_DIR="${CRONAI_BASE_DIR}/configs"

# Path to the session scheduler script
SESSION_SCRIPT="${CRONAI_BASE_DIR}/session_scheduler.sh"

# Path to the cron update script
UPDATE_CRON_SCRIPT="${CRONAI_BASE_DIR}/update_cron.sh"

# Flask app configuration
FLASK_HOST="0.0.0.0"  # Set to localhost for local access only
FLASK_PORT="5001"     # The port the web interface will run on

# Default schedule for new configurations
# Options: "*/10 * * * *" (every 10 min), "0 * * * *" (hourly), etc.
DEFAULT_CRON_SCHEDULE="0 6 * * *" # daily at 6 AM

# MCP Server Connection Configuration
# -----------------------------------

# Goose CLI path for connecting to MCP Servers
# Leave empty if Goose is in your PATH, otherwise specify the full path
GOOSE_PATH=""  

# MCP Server configuration settings
# Uncomment and set these values if you need specific MCP Server configurations
# MCP_SERVER_URL=""
# MCP_API_KEY=""
# MCP_DEFAULT_MODEL=""

# AI Session Parameters
# --------------------
# AI_TIMEOUT="300"      # Maximum time (in seconds) for AI sessions
# AI_OUTPUT_FORMAT="text" # Output format (text, json, markdown)
# AI_DEFAULT_CONTEXT="You are an assistant helping with daily tasks."
