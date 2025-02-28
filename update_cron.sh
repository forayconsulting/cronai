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

# Get the absolute path of the config file and scheduler script
CONFIG_FILE_ABS="$(realpath "$CONFIG_FILE")"
SCRIPT_DIR="$(realpath "$(dirname "$0")")"
SESSION_SCRIPT="${SCRIPT_DIR}/session_scheduler.sh"

# Load configuration
source "$CONFIG_FILE"

# If no schedule is set (i.e. empty), skip updating the crontab.
if [ -z "$cron_schedule" ]; then
  echo "No cron schedule set, skipping cron update"
  exit 0
fi

# Create the cron entry with absolute paths
cron_entry="$cron_schedule $SESSION_SCRIPT $CONFIG_FILE_ABS"

# Create temporary files for crontab manipulation
tmpfile=$(mktemp)
tmpfile_filtered="${tmpfile}.filtered"

# Capture current cron jobs (if any)
crontab -l 2>/dev/null > "$tmpfile" || echo "" > "$tmpfile"

# Remove any existing entry for this config
grep -v "$CONFIG_FILE_ABS" "$tmpfile" > "$tmpfile_filtered"

# Append the new cron entry
echo "$cron_entry" >> "$tmpfile_filtered"

# Install the new cron file
crontab "$tmpfile_filtered"

# Clean up temporary files
rm -f "$tmpfile" "$tmpfile_filtered"

echo "Cron job updated successfully."
echo "Schedule: $cron_schedule"
echo "Command: $SESSION_SCRIPT $CONFIG_FILE_ABS"
