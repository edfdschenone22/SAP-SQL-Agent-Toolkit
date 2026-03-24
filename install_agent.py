import os
import subprocess
import json
import sys

def install_toolkit():
    """
    Installs the toolkit in editable mode.
    """
    print("Installing the SAP Agent Toolkit...")
    subprocess.check_call(["pip", "install", "-e", "."])
    print("Installation complete.")

def configure_mcp_servers():
    """
    Configures the MCP servers by writing to the Cline settings file.
    """
    print("Configuring MCP servers...")
    settings_path = os.path.expanduser("~\\AppData\\Roaming\\Code\\User\\globalStorage\\saoudrizwan.claude-dev\\settings\\cline_mcp_settings.json")
    
    if not os.path.exists(settings_path):
        print(f"Settings file not found at {settings_path}. Please ensure Cline is installed.")
        return

    with open(settings_path, "r") as file:
        settings = json.load(file)

    # Add MCP server configurations
    settings["mcpServers"] = {
        "sap-hana": {
"command": os.path.abspath(sys.executable),
"args": [os.path.abspath("src/sap_mcp.py")]
        },
        "sql-dev": {
            "command": sys.executable,
            "args": [os.path.abspath("src/sql_dev_mcp.py")]
        },
        "sql-prd": {
            "command": sys.executable,
            "args": [os.path.abspath("src/sql_prd_mcp.py")]
        }
    }

    with open(settings_path, "w") as file:
        json.dump(settings, file, indent=4)

    print("MCP servers configured successfully.")

if __name__ == "__main__":
    install_toolkit()
    configure_mcp_servers()
    print("Setup complete. Your SAP Agent Toolkit is ready to use!")