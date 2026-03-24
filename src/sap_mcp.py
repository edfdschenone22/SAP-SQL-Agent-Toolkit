import nest_asyncio
from fastmcp import FastMCP
import pyodbc
import json
import os
import traceback

# --- Start of Error Logging ---
LOG_FILE = os.path.join(os.path.dirname(__file__), 'sap_mcp.log')

def log_error(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{message}\n")

try:
# --- End of Error Logging ---

    nest_asyncio.apply()
    mcp = FastMCP("SAP-HANA-Source")

    # Your exact connection string
    HANA_CONN_STR = "DRIVER=HDBODBC;SERVERNODE=CAWSHANADBPRD01:30041;DATABASE=HQC;integratedsecurity=1"

    @mcp.tool()
    def read_hana(sql: str):
        """Executes a SELECT query on SAP HANA (Read-Only)."""
        if not sql.strip().lower().startswith("select"):
            return "Error: This tool is restricted to SELECT statements."
        try:
            with pyodbc.connect(HANA_CONN_STR) as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                columns = [column[0] for column in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return json.dumps(results, default=str)
        except Exception as e:
            log_error(f"HANA Connection/Query Error: {str(e)}\n{traceback.format_exc()}")
            return f"HANA Error: {str(e)}"

    if __name__ == "__main__":
        mcp.run()

# --- Start of Error Logging ---
except Exception as e:
    log_error(f"Unhandled exception at script level: {str(e)}\n{traceback.format_exc()}")
# --- End of Error Logging ---