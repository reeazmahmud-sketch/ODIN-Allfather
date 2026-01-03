#!/usr/bin/env python3
"""
ODIN - The Allfather AI/Agent Orchestration System
Complete daemon with multi-agent orchestration, system monitoring, and multilingual support
"""
import os
import socket
import threading
import yaml
import psutil
from pathlib import Path
from datetime import datetime
import importlib.util

# Path configuration
ODIN_BASE = Path.home() / "Terminal-CLI" / "Odin" / "Odin"
SOCKET_PATH = ODIN_BASE / "daemon" / "odin.sock"
WORKSPACES_DIR = ODIN_BASE / "Workspaces"
AGENTS_DIR = ODIN_BASE / "Agents"
LOGS_DIR = ODIN_BASE / "Logs"

agents_registry = {}

# ============================================================
# LOGGING SYSTEM
# ============================================================
def log_action(action: str):
    """Log all actions with timestamps"""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / "actions.log"
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {action}\n")
    print(f"[ODIN LOG] {action}")

# ============================================================
# AGENT DISCOVERY & REGISTRATION
# ============================================================
def discover_agents():
    """
    Automatically discover and register all agents in the Agents folder.
    Each agent must have adapter.py with a class named <AgentName>
    """
    log_action("Starting agent discovery...")

    for agent_folder in AGENTS_DIR.iterdir():
        if agent_folder.is_dir():
            adapter_file = agent_folder / "adapter.py"
            if adapter_file.exists():
                try:
                    module_name = f"{agent_folder.name}_adapter"
                    spec = importlib.util.spec_from_file_location(module_name, adapter_file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Class name convention: capitalize folder name
                    class_name = agent_folder.name.capitalize()
                    agent_class = getattr(module, class_name, None)

                    if agent_class:
                        agents_registry[agent_folder.name.lower()] = agent_class
                        log_action(f"✓ Discovered agent: {agent_folder.name}")
                    else:
                        log_action(f"✗ No class '{class_name}' found in {agent_folder.name}/adapter.py")
                except Exception as e:
                    log_action(f"✗ Error loading agent {agent_folder.name}: {e}")

    log_action(f"Agent discovery complete. Total agents: {len(agents_registry)}")
    return agents_registry

# ============================================================
# MULTILINGUAL COMMAND PARSING (English + Bangla)
# ============================================================
LANG_MAP = {
    "en": {
        "create": "create",
        "list": "list",
        "delete": "delete",
        "integrate": "integrate",
        "status": "status",
        "install": "install",
        "help": "help"
    },
    "bn": {
        "নতুন": "create",
        "তৈরি": "create",
        "তালিকা": "list",
        "মুছে": "delete",
        "একত্রিত": "integrate",
        "স্থিতি": "status",
        "ইনস্টল": "install",
        "সাহায্য": "help"
    }
}

def parse_command(input_text):
    """
    Parse natural language commands in English or Bangla.
    Returns (command, args) tuple.
    """
    for lang, mapping in LANG_MAP.items():
        for word, cmd in mapping.items():
            if word in input_text.lower():
                args = input_text.replace(word, "").strip().split()
                return cmd, args

    # Fallback: try standard space-separated parsing
    parts = input_text.strip().split()
    if parts:
        return parts[0].lower(), parts[1:]
    return None, []

# ============================================================
# PROJECT MANAGEMENT HANDLERS
# ============================================================
def handle_create(args):
    """Create a new project sandbox"""
    project_name = args[0] if args else "NewProject"
    project_path = WORKSPACES_DIR / project_name

    if project_path.exists():
        return f"Project '{project_name}' already exists"

    project_path.mkdir(parents=True, exist_ok=True)
    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "assets").mkdir(exist_ok=True)

    # Create project metadata
    meta_file = project_path / ".odin-meta.yaml"
    meta = {
        "name": project_name,
        "root": str(project_path),
        "agents": {},
        "dependencies": {},
        "permissions": {
            "read": [],
            "write": []
        },
        "assets": [],
        "created": str(datetime.now()),
        "last_active": str(datetime.now())
    }

    with open(meta_file, "w") as f:
        yaml.dump(meta, f)

    log_action(f"Created project: {project_name} at {project_path}")
    return f"✓ Project '{project_name}' created successfully at {project_path}"

def handle_list(args):
    """List all projects in Workspaces"""
    if not WORKSPACES_DIR.exists():
        return "No workspaces directory found"

    projects = [p.name for p in WORKSPACES_DIR.iterdir() if p.is_dir() and (p / ".odin-meta.yaml").exists()]

    if not projects:
        return "No projects found"

    result = f"Found {len(projects)} project(s):\n"
    for proj in projects:
        result += f"  - {proj}\n"

    return result

def handle_integrate(args):
    """Integrate an agent into a project"""
    if len(args) < 2:
        return "Usage: integrate <agent_name> <project_name>"

    agent_name = args[0].lower()
    project_name = args[1]

    # Check if agent exists
    if agent_name not in agents_registry:
        available = ", ".join(agents_registry.keys())
        return f"Agent '{agent_name}' not found. Available agents: {available}"

    # Check if project exists
    project_path = WORKSPACES_DIR / project_name
    if not project_path.exists():
        return f"Project '{project_name}' not found"

    # Update project metadata
    meta_file = project_path / ".odin-meta.yaml"
    with open(meta_file, "r") as f:
        meta = yaml.safe_load(f)

    meta["agents"][agent_name] = "enabled"
    meta["last_active"] = str(datetime.now())

    with open(meta_file, "w") as f:
        yaml.dump(meta, f)

    log_action(f"Integrated agent '{agent_name}' into project '{project_name}'")
    return f"✓ Agent '{agent_name}' integrated into '{project_name}'"

def handle_status(args):
    """Show system and agent status"""
    disk = psutil.disk_usage(str(WORKSPACES_DIR))
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)

    status = f"""
ODIN System Status:
==================
Agents Registered: {len(agents_registry)}
  {', '.join(agents_registry.keys()) if agents_registry else 'None'}

System Resources:
  CPU Usage: {cpu}%
  Memory Usage: {mem.percent}%
  Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)

Workspaces: {len(list(WORKSPACES_DIR.iterdir())) if WORKSPACES_DIR.exists() else 0} projects
"""
    return status

def handle_help(args):
    """Show help information"""
    return """
ODIN - The Allfather AI/Agent Orchestration System

Available Commands:
  create <name>              - Create a new project
  list                       - List all projects
  integrate <agent> <project> - Integrate an agent into a project
  status                     - Show system status
  help                       - Show this help message

Multilingual Support:
  All commands work in English and Bangla

Examples:
  odin create MyProject
  odin integrate claude MyProject
  odin list
  odin status
"""

# Command mapping
COMMAND_MAP = {
    "create": handle_create,
    "list": handle_list,
    "integrate": handle_integrate,
    "status": handle_status,
    "help": handle_help,
}

# ============================================================
# SYSTEM MONITORING
# ============================================================
def monitor_system():
    """
    Background thread continuously monitoring system resources.
    Alerts agents when thresholds are exceeded.
    """
    log_action("System monitoring started")

    while True:
        try:
            # Disk monitoring
            disk = psutil.disk_usage(str(WORKSPACES_DIR))
            if disk.percent > 90:
                log_action(f"[ALERT] Disk usage high: {disk.percent}%")
                notify_agents("disk_alert", disk.percent)

            # Memory monitoring
            mem = psutil.virtual_memory()
            if mem.percent > 90:
                log_action(f"[ALERT] Memory usage high: {mem.percent}%")
                notify_agents("memory_alert", mem.percent)

            # CPU / infinite loop detection
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    if proc.info['cpu_percent'] > 95:
                        log_action(f"[ALERT] High CPU: PID {proc.info['pid']} ({proc.info['name']})")
                        notify_agents("cpu_alert", proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

        except Exception as e:
            log_action(f"[ERROR] Monitoring error: {e}")

        import time
        time.sleep(5)

def notify_agents(alert_type, data):
    """Send system alerts to all enabled agents in active projects"""
    if not WORKSPACES_DIR.exists():
        return

    for project_folder in WORKSPACES_DIR.iterdir():
        if project_folder.is_dir():
            meta_file = project_folder / ".odin-meta.yaml"
            if not meta_file.exists():
                continue

            try:
                with open(meta_file) as f:
                    meta = yaml.safe_load(f)

                for agent_name, status in meta.get("agents", {}).items():
                    if status == "enabled" and agent_name in agents_registry:
                        agent_instance = agents_registry[agent_name](project_folder)
                        if hasattr(agent_instance, "monitor_system"):
                            agent_instance.monitor_system(alert_type, data)
            except Exception as e:
                log_action(f"[ERROR] Failed to notify agents in {project_folder.name}: {e}")

# ============================================================
# CLIENT CONNECTION HANDLER
# ============================================================
def handle_client(conn):
    """Handle incoming client connections and execute commands"""
    with conn:
        try:
            command_line = conn.recv(2048).decode().strip()
            log_action(f"Received command: {command_line}")

            # Parse command (supports multilingual)
            cmd, args = parse_command(command_line)

            if not cmd:
                response = "Invalid command. Type 'help' for usage."
            else:
                handler = COMMAND_MAP.get(cmd)
                if handler:
                    response = handler(args)
                else:
                    response = f"Unknown command: {cmd}. Type 'help' for usage."

            conn.sendall(response.encode())
        except Exception as e:
            error_msg = f"Error processing command: {e}"
            log_action(f"[ERROR] {error_msg}")
            conn.sendall(error_msg.encode())

# ============================================================
# DAEMON STARTUP
# ============================================================
def start_daemon():
    """Initialize and start the ODIN daemon"""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║              ODIN - The Allfather                        ║
║        AI/Agent Orchestration & System Guardian               ║
╚═══════════════════════════════════════════════════════════════╝
""")

    # Create necessary directories
    WORKSPACES_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    SOCKET_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Discover and register agents
    discover_agents()

    # Start system monitoring thread
    threading.Thread(target=monitor_system, daemon=True).start()

    # Remove old socket if exists
    if SOCKET_PATH.exists():
        os.remove(SOCKET_PATH)

    # Start daemon socket server
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.bind(str(SOCKET_PATH))
        s.listen()
        log_action(f"✓ ODIN daemon listening on {SOCKET_PATH}")
        log_action(f"✓ Multi-agent orchestration ready")
        log_action(f"✓ System monitoring active")
        log_action(f"✓ Multilingual support (English + Bangla) enabled")

        print("\n[ODIN] Ready for commands...")

        while True:
            try:
                conn, _ = s.accept()
                threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
            except KeyboardInterrupt:
                log_action("ODIN daemon shutting down...")
                break
            except Exception as e:
                log_action(f"[ERROR] Connection error: {e}")

if __name__ == "__main__":
    start_daemon()
