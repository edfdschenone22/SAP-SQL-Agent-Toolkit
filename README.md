# AP Agent Toolkit

## Introduction
The AP Agent Toolkit is designed to streamline the creation of agentic workflows that integrate SAP and SQL Server data pipelines. It provides a modular structure for reusable components and specific project implementations, making it easy to share and extend.

## Prerequisites
1. Install **Visual Studio Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Install the **Cline Extension** from the VS Code Marketplace.

## Architecture
The toolkit is organized into two main parts:
- **Core Toolkit (`src/`)**: Contains reusable MCP servers (`sap-hana`, `sql-dev`, `sql-prd`) and pipeline templates.
- **Projects (`projects/`)**: Houses specific implementations, such as dashboards or reports, built using the core toolkit.

This separation ensures that the core logic remains clean and reusable while allowing flexibility for project-specific customizations.

## Installation Guide
Follow these steps to set up the toolkit:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/edfdschenone22/AP-Agent-Toolkit.git
   cd AP-Agent-Toolkit
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
Once installed, the MCP servers (`sap-hana`, `sql-dev`, and `sql-prd`) are available in Cline. You can:
- Query SAP data using `sap-hana`.
- Read and write to SQL Server using `sql-dev` and `sql-prd`.

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
- **Purpose**: Read and write access to SQL Server (Development).
- **Use Case**: Automate data transformations, updates, and reporting.

### `sql-prd`
- **Purpose**: Read and write access to SQL Server (Production).
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