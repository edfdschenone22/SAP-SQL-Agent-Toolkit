# SAP Agent Toolkit

## Introduction
The SAP Agent Toolkit is designed to streamline the creation of agentic workflows that integrate SAP and SQL Server data pipelines. It provides a modular structure for reusable components and specific project implementations, making it easy to share and extend.

## Architecture
The toolkit is organized into two main parts:
- **Core Toolkit (`src/`)**: Contains reusable MCP servers (`sap-hana`, `sql-dev`) and pipeline templates.
- **Projects (`projects/`)**: Houses specific implementations, such as dashboards or reports, built using the core toolkit.

This separation ensures that the core logic remains clean and reusable while allowing flexibility for project-specific customizations.

## Installation Guide
Follow these steps to set up the toolkit:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment** (Recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Run the Installer**:
   ```bash
   python install_agent.py
   ```
   This script will:
   - Install the toolkit in editable mode.
   - Configure the MCP servers in your `cline_mcp_settings.json` file.

## Usage Guide
### Using MCP Servers
Once installed, the MCP servers (`sap-hana` and `sql-dev`) are available in Cline. You can:
- Query SAP data using `sap-hana`.
- Read and write to SQL Server using `sql-dev`.

### Building New Pipelines
To create a new project:
1. Create a new folder under `projects/`.
2. Use the templates in `src/` to build your pipeline logic.
3. Leverage the MCP servers for data access.

## Capabilities
### `sap-hana`
- **Purpose**: Read-only access to SAP HANA.
- **Use Case**: Extract data for analysis or reporting.

### `sql-dev`
- **Purpose**: Read and write access to SQL Server.
- **Use Case**: Automate data transformations, updates, and reporting.

### Pipeline Templates
- **Base Pipeline**: Provides a consistent structure for building new workflows.

## Why This Toolkit?
This toolkit was designed to:
- Simplify the integration of SAP and SQL Server data.
- Enable reusable, modular workflows.
- Provide a seamless setup experience for teams.

## Sharing with Coworkers
To share this toolkit:
1. Provide them with the repository link or a zipped folder.
2. Instruct them to follow the installation guide above.

For any questions or issues, feel free to reach out!