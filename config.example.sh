#!/bin/bash
# CRONAI - Example Configuration File
# Make a copy of this file named config.sh and adjust the values for your environment

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

# Command line tool configuration
# Set the path to your CLI tool if it's not in PATH
GOOSE_PATH=""  # Leave empty if in PATH, otherwise specify full path
