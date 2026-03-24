import nest_asyncio
from fastmcp import FastMCP
from sqlalchemy import create_engine, text
import json
import os
import traceback

# --- Start of Error Logging ---
LOG_FILE = os.path.join(os.path.dirname(__file__), 'sql_prd_mcp.log')

def log_error(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{message}\n")

try:
# --- End of Error Logging ---

    nest_asyncio.apply()
    mcp = FastMCP("SQL-Server-PRD")

    # Your SQLAlchemy connection URL
    SQL_URL = "mssql+pyodbc://SDHQHOPSQL01/AOBAFin?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(SQL_URL)

    @mcp.tool()
    def read_sql(sql: str):
        """Read from the AOBAFin database."""
        try:
            with engine.connect() as conn:
                result = conn.execute(text(sql))
                return json.dumps([dict(r._mapping) for r in result], default=str)
        except Exception as e:
            log_error(f"SQL Read Error: {str(e)}\n{traceback.format_exc()}")
            return f"SQL Read Error: {str(e)}"

    @mcp.tool()
    def write_sql(sql: str):
        """Execute DDL/DML (CREATE, INSERT, UPDATE) on AOBAFin."""
        try:
            with engine.begin() as conn:
                result = conn.execute(text(sql))
                return f"Success: {result.rowcount} rows affected."
        except Exception as e:
            log_error(f"SQL Write Error: {str(e)}\n{traceback.format_exc()}")
            return f"SQL Write Error: {str(e)}"

    if __name__ == "__main__":
        mcp.run()

# --- Start of Error Logging ---
except Exception as e:
    log_error(f"Unhandled exception at script level: {str(e)}\n{traceback.format_exc()}")
# --- End of Error Logging ---