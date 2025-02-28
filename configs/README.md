# Configuration Directory

This directory contains your CRONAI configuration files.

## How Configurations Work

Each `.sh` file in this directory represents a different configuration profile. These files are used to:

1. Define what commands to run
2. Set up scheduling using cron
3. Configure how sessions are executed

## Example Configuration

Here's a sample configuration file structure:

```bash
#!/bin/bash
# Cron schedule (in standard cron syntax)
cron_schedule="0 6 * * *"

# Commands to pipe into goose session
commands=(
"Generate a report based on yesterday's data"
"List three action items for today"
"Search for any anomalies in system logs"
)
```

## Creating New Configurations

You can create new configurations either through the web interface or by adding a .sh file to this directory.

## Important Notes

- Configuration files in this directory should NOT be committed to Git if they contain sensitive information
- The `.gitignore` file is set up to exclude these files by default
- Use template files in the `templates/configs/` directory as starting points
