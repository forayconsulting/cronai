#!/bin/bash
# Default template configuration for CRONAI

# Cron schedule (in standard cron syntax)
# This example runs daily at 6:00 AM
cron_schedule="0 6 * * *"

# Commands to pipe into goose session
commands=(
"Generate a daily summary of yesterday's activities"
"List the top priorities for today"
"Suggest three productivity tips based on my work patterns"
)
