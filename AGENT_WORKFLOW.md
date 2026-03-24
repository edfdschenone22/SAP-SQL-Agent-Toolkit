# Agent Workflow: SAP to SQL Pipeline Setup

This document outlines the **Standard Operating Procedure (SOP)** for creating and managing SAP to SQL pipelines. It emphasizes the importance of deep SAP context and a structured, replicable workflow.

---

## Workflow Overview

### 1. **The Analyst**
- **Goal:** Understand the business question and map it to SAP tables and relationships.
- **Actions:**
  - Explore SAP schemas using tools like `read_hana`.
  - Validate relationships between tables (e.g., `MARA` -> `MARD` -> `MSEG`).
  - Define the "Golden Query" that extracts the required data.
- **Output:** A validated SQL query.

### 2. **The Coder**
- **Goal:** Create a robust, reusable pipeline script.
- **Actions:**
  - Use `sap_pipeline_template.py` to generate a new pipeline script.
  - Implement the "Golden Query" in the `extract` method.
  - Add transformation logic in the `transform` method.
  - Define the target SQL table in the `load` method.
- **Output:** A `.py` file ready for execution.

### 3. **The Runner**
- **Goal:** Verify the pipeline script.
- **Actions:**
  - Execute the pipeline script.
  - Validate the output (e.g., CSV file or DataFrame).
- **Output:** Confirmed data ready for loading.

### 4. **The Loader**
- **Goal:** Persist the data in SQL Server.
- **Actions:**
  - Use the `load` method to write data to the target SQL table.
  - Ensure the table schema matches the business requirements.
- **Output:** Data stored in SQL Server.

### 5. **The Diagnostician**
- **Goal:** Analyze and validate the data.
- **Actions:**
  - Run diagnostic queries on the SQL table.
  - Identify anomalies, trends, or insights.
- **Output:** Validated business answers.

---

## Key Principles

1. **Deep SAP Context is Critical**
   - The Analyst must validate all assumptions about SAP relationships.
   - Example: `MARD` shows current stock, but `MARDH` is needed for historical data.

2. **Standardization**
   - All pipelines must inherit from `base_pipeline.py`.
   - Use `sap_pipeline_template.py` for consistency.

3. **Validation at Every Step**
   - Each role (Analyst, Coder, Runner, Loader, Diagnostician) must validate their output before passing it to the next stage.

---

## File Structure

- `base_pipeline.py`: Abstract base class for all pipelines.
- `sap_pipeline_template.py`: Template for creating new pipelines.
- `AGENT_WORKFLOW.md`: This document.

---

## Example Workflow

1. **Analyst Phase**
   - Business Question: "What is the inventory for Plant 'TEH' in 2024-2025?"
   - Golden Query: `SELECT WERKS, LGORT, LABST FROM ECCSLT.MARD WHERE WERKS = 'TEH' AND ERSDA BETWEEN '2024-01-01' AND '2025-12-31'`.

2. **Coder Phase**
   - Create `pipeline_teh_inventory.py` using `sap_pipeline_template.py`.
   - Implement the Golden Query in `extract`.

3. **Runner Phase**
   - Execute `pipeline_teh_inventory.py`.
   - Validate the output (e.g., `teh_inventory_2024_2025.csv`).

4. **Loader Phase**
   - Load the data into SQL Server.

5. **Diagnostician Phase**
   - Analyze the SQL table for trends or anomalies.

---

## Notes

- This workflow is designed to be **agnostic** of the specific task.
- Always prioritize **data validation** and **business context**.