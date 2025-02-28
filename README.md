# CRONAI

CRONAI is a tool for scheduling and managing AI assistance sessions through cron. It provides a web interface for creating, managing, and executing AI commands on a schedule.

<!-- Image will be added once the interface is finalized -->

## Features

- **Web Interface**: Easy-to-use UI for managing your AI sessions
- **Scheduled Execution**: Schedule commands to run at specific intervals using cron
- **Real-time Output**: See the results of your commands in real-time
- **Configuration Management**: Create, edit, and manage multiple configuration profiles
- **Flexible Scheduling**: Options from "Manual Only" to daily, weekly, or monthly execution

## Requirements

- Python 3.6+
- Flask
- Modern web browser
- Unix-like operating system with crontab support
- [Goose](https://github.com/yourusername/goose) CLI tool (for AI session management)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/forayconsulting/cronai.git
   cd cronai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the application:
   ```bash
   cp config.example.sh config.sh
   # Edit config.sh with your specific paths and settings
   ```

4. Create example configurations:
   ```bash
   mkdir -p configs
   cp templates/configs/default.sh configs/
   ```

5. Start the application:
   ```bash
   python app.py
   ```

6. Access the web interface at `http://localhost:5001`

## Usage

### Creating a Configuration

1. From the CRONAI web interface, enter a name for your new configuration and click "Create"
2. Set your desired schedule (e.g., "Every day", "Manual Only")
3. Add the commands you want to execute in the AI session
4. Click "Save" to store your configuration

### Running a Session

1. Select a configuration from the left sidebar
2. Click the "Run" button to execute the commands immediately
3. View the output in real-time in the output panel
4. Use the "Stop" button to terminate a running session

### Scheduling Sessions

- For configurations with a schedule other than "Manual Only", CRONAI will update your crontab automatically
- Schedules are managed by the system's cron daemon
- To view your current cron jobs, use `crontab -l` in a terminal

## Customizing

### Custom Command Templates

Create reusable command templates by adding files to the `templates/configs/` directory:

```bash
# Example template for data analysis tasks
echo "Analyzing dataset..."
process_data --input $DATA_FILE --output $RESULTS_DIR
summarize_findings $RESULTS_DIR
```

### Environment Variables

You can use environment variables in your commands. These are processed at runtime:

```bash
analyze_text "$MY_TEXT_VAR"
```

## File Structure

```
cronai/
├── app.py                 # Main Flask application
├── config.sh              # Global configuration
├── session_scheduler.sh   # Script to execute commands
├── update_cron.sh         # Script to update crontab
├── configs/               # User configurations
│   ├── App Dev.sh         # Example configuration
│   └── ...
└── templates/             # Web UI templates
    ├── index.html         # Main UI
    └── configs/           # Template configurations
        └── default.sh     # Default configuration template
```

## Troubleshooting

### Cron Jobs Not Running

1. Check if the cron service is running: `systemctl status cron`
2. Verify permissions on the script files: `chmod +x *.sh`
3. Check the cron log: `grep CRON /var/log/syslog`

### Command Execution Issues

1. Verify that the `goose` CLI tool is installed and in your PATH
2. Check the syntax of your commands
3. Run the session manually to see detailed error output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask web framework
- Uses crontab for job scheduling
- Inspired by the need for automated AI assistance
