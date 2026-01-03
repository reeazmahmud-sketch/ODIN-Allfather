"""
ODIN Agent Template
Base template for creating new AI agents in the ODIN ecosystem.

To create a new agent:
1. Copy this folder and rename it
2. Rename the class to match the folder name (capitalized)
3. Implement the methods for your agent's capabilities
"""

class Template_agent:
    """Base template for ODIN agents"""

    def __init__(self, workspace_path):
        """
        Initialize the agent with a workspace path.

        Args:
            workspace_path (Path): Path to the project workspace
        """
        self.workspace = workspace_path
        self.name = self.__class__.__name__

    def analyze_project(self):
        """
        Analyze the project workspace and provide insights.

        Returns:
            str: Analysis summary
        """
        return f"[{self.name}] Analyzing project at {self.workspace}"

    def install_dependencies(self, deps):
        """
        Install project dependencies safely in the sandbox.

        Args:
            deps (list): List of dependencies to install
        """
        print(f"[{self.name}] Installing dependencies: {deps}")
        # Implement your dependency installation logic here
        return f"Installed: {', '.join(deps)}"

    def execute_command(self, command: str):
        """
        Execute a command safely within the project context.

        Args:
            command (str): Command to execute

        Returns:
            str: Execution result
        """
        print(f"[{self.name}] Executing: {command}")
        # Implement safe command execution here
        return f"Executed: {command}"

    def monitor_system(self, alert_type=None, data=None):
        """
        React to system monitoring alerts.

        Args:
            alert_type (str): Type of alert (disk_alert, memory_alert, cpu_alert)
            data: Alert data
        """
        if alert_type == "disk_alert":
            print(f"[{self.name}] ⚠️  Disk usage alert: {data}% in {self.workspace}")
            # Implement disk cleanup logic

        elif alert_type == "memory_alert":
            print(f"[{self.name}] ⚠️  Memory usage alert: {data}% in {self.workspace}")
            # Implement memory optimization logic

        elif alert_type == "cpu_alert":
            print(f"[{self.name}] ⚠️  CPU alert: {data} in {self.workspace}")
            # Implement CPU management logic

    def analyze_asset(self, asset):
        """
        Analyze a dropped file/asset in the project.

        Args:
            asset (dict): Asset metadata with keys: name, type, path, tags
        """
        file_type = asset.get("type")
        path = asset.get("path")

        if file_type in ["pdf", "docx", "txt", "md"]:
            print(f"[{self.name}] 📄 Extracting text from {path}")
            # Implement text extraction logic

        elif file_type in ["png", "jpg", "jpeg", "gif"]:
            print(f"[{self.name}] 🖼️  Processing image {path}")
            # Implement image processing logic

        elif file_type in ["py", "js", "ts", "cpp", "java"]:
            print(f"[{self.name}] 💻 Analyzing code file {path}")
            # Implement code analysis logic
