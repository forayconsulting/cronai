#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from flask import Flask, render_template, request, Response, redirect, url_for

app = Flask(__name__)

# Load configuration from config.sh
def load_config():
    config = {}
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.sh')
    
    if not os.path.exists(config_path):
        print("Error: config.sh not found. Please create it from config.example.sh")
        sys.exit(1)
    
    try:
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    # Remove quotes and whitespace
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    config[key] = value
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)
    
    return config

# Load configuration
config = load_config()

# Directory where configuration files are stored
CONFIG_DIR = config.get('CONFIG_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configs'))
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

# Paths for scripts
SESSION_SCRIPT = config.get('SESSION_SCRIPT', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'session_scheduler.sh'))
UPDATE_CRON_SCRIPT = config.get('UPDATE_CRON_SCRIPT', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'update_cron.sh'))

# Mapping natural language schedule options to cron expressions
NATURAL_TO_CRON = {
    "Manual Only": "",
    "Every 10 minutes": "*/10 * * * *",
    "Every 30 minutes": "*/30 * * * *",
    "Every hour": "0 * * * *",
    "Every day": "0 6 * * *",
    "Every week": "0 6 * * 1",
    "Every month": "0 6 1 * *"
}
CRON_TO_NATURAL = {v: k for k, v in NATURAL_TO_CRON.items()}

# Global variable to hold the running process
current_process = None

def get_config_filepath(config_name):
    if not config_name.endswith('.sh'):
        config_name += '.sh'
    return os.path.join(CONFIG_DIR, config_name)

def list_configs():
    files = [f for f in os.listdir(CONFIG_DIR) if f.endswith('.sh')]
    files.sort()
    return files

def parse_config(filepath):
    schedule = ""
    commands = []
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip().startswith("cron_schedule="):
                parts = line.split("=", 1)
                cron_expr = parts[1].strip().strip('"')
                schedule = CRON_TO_NATURAL.get(cron_expr, "Manual Only")
                break
        in_commands = False
        for line in lines:
            if line.strip().startswith("commands=("):
                in_commands = True
                continue
            if in_commands:
                if line.strip().startswith(")"):
                    in_commands = False
                    break
                cmd = line.strip().strip('"')
                commands.append(cmd)
    else:
        schedule = "Manual Only"
    return schedule, commands

def clean_line(line):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line).strip()

def is_garbage(line):
    exclude_patterns = [
        r'^starting session',
        r'^logging to',
        r'^Goose is running!',
        r'^───'
    ]
    for pattern in exclude_patterns:
        if re.match(pattern, line, re.IGNORECASE):
            return True
    return False

@app.route('/')
def index():
    config_name = request.args.get('config')
    configs = list_configs()
    if not config_name:
        if "default.sh" in configs:
            config_name = "default.sh"
        elif configs:
            config_name = configs[0]
        else:
            config_name = "default.sh"
    filepath = get_config_filepath(config_name)
    schedule, commands = parse_config(filepath)
    return render_template('index.html',
                           config_name=config_name,
                           configs=configs,
                           schedule=schedule,
                           commands=commands,
                           options=list(NATURAL_TO_CRON.keys()))

@app.route('/save_config', methods=['POST'])
def save_config():
    config_name = request.form.get('config_name', 'default.sh')
    natural_schedule = request.form.get('schedule', '').strip()
    cron_schedule = NATURAL_TO_CRON.get(natural_schedule, "")
    commands_list = request.form.getlist('commands')
    commands_list = [cmd for cmd in commands_list if cmd.strip()]
    config_content = "#!/bin/bash\n"
    config_content += "# Cron schedule (in standard cron syntax)\n"
    config_content += f'cron_schedule="{cron_schedule}"\n\n'
    config_content += "# Commands to pipe into goose session\n"
    config_content += "commands=(\n"
    for cmd in commands_list:
        config_content += f'"{cmd}"\n'
    config_content += ")\n"
    filepath = get_config_filepath(config_name)
    with open(filepath, 'w') as f:
        f.write(config_content)
    if cron_schedule:
        subprocess.Popen(['bash', UPDATE_CRON_SCRIPT, filepath])
    return "Config saved"

@app.route('/run_session', methods=['POST'])
def run_session():
    global current_process
    config_name = request.form.get('config_name', 'default.sh')
    filepath = get_config_filepath(config_name)
    current_process = subprocess.Popen(
        ['bash', SESSION_SCRIPT, filepath],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )
    def generate():
        global current_process
        try:
            for line in iter(current_process.stdout.readline, ''):
                cleaned = clean_line(line)
                if cleaned and not is_garbage(cleaned):
                    yield cleaned + "\n"
        finally:
            current_process.stdout.close()
            current_process.wait()
            current_process = None
    return Response(generate(), mimetype='text/plain')

@app.route('/stop_session', methods=['POST'])
def stop_session():
    global current_process
    if current_process is not None:
        current_process.terminate()
        current_process = None
        return "Session terminated", 200
    else:
        return "No session running", 400

@app.route('/create_config', methods=['POST'])
def create_config():
    new_name = request.form.get('new_config_name', '').strip()
    if not new_name:
        return "Config name required", 400
    if not new_name.endswith('.sh'):
        new_name += '.sh'
    filepath = get_config_filepath(new_name)
    if os.path.exists(filepath):
        return "Config already exists", 400
    default_content = "#!/bin/bash\n"
    default_content += "# Cron schedule (in standard cron syntax)\n"
    default_content += f'cron_schedule="{NATURAL_TO_CRON["Every day"]}"\n\n'
    default_content += "# Commands to pipe into goose session\n"
    default_content += "commands=(\n\"Write your command here\"\n)\n"
    with open(filepath, 'w') as f:
        f.write(default_content)
    return redirect(url_for('index', config=new_name))

@app.route('/rename_config', methods=['POST'])
def rename_config():
    old_name = request.form.get('old_config_name', '').strip()
    new_name = request.form.get('new_config_name', '').strip()
    if not old_name or not new_name:
        return "Old and new config names are required", 400
    if not old_name.endswith('.sh'):
        old_name += '.sh'
    if not new_name.endswith('.sh'):
        new_name += '.sh'
    old_path = get_config_filepath(old_name)
    new_path = get_config_filepath(new_name)
    if not os.path.exists(old_path):
        return "Config not found", 404
    if os.path.exists(new_path):
        return "A config with that name already exists", 400
    os.rename(old_path, new_path)
    return redirect(url_for('index', config=new_name))

@app.route('/delete_config', methods=['POST'])
def delete_config():
    config_name = request.form.get('config_name', '').strip()
    if not config_name:
        return "Config name required", 400
    if not config_name.endswith('.sh'):
        config_name += '.sh'
    filepath = get_config_filepath(config_name)
    if not os.path.exists(filepath):
        return "Config not found", 404
    os.remove(filepath)
    configs = list_configs()
    new_config = configs[0] if configs else "default.sh"
    return redirect(url_for('index', config=new_config))

if __name__ == '__main__':
    host = config.get('FLASK_HOST', '0.0.0.0')
    port = int(config.get('FLASK_PORT', 5001))
    app.run(debug=True, host=host, port=port)
