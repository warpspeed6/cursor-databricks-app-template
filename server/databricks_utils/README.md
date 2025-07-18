# Databricks Utilities

This folder contains utility functions for working with Databricks APIs using the Databricks SDK for Python.

## Documentation

For complete documentation on the Databricks SDK for Python, visit:
**https://databricks-sdk-py.readthedocs.io/en/latest/**

## Available Utilities

### 🗂️ Workspace Utilities (`workspace_utils.py`)
- List and manage workspace files and directories
- Upload and download files from workspace
- Create and manage workspace folders
- Handle workspace permissions

### 🖥️ Cluster Utilities (`cluster_utils.py`)
- List and manage compute clusters
- Start, stop, and restart clusters
- Get cluster information and status
- Configure cluster settings

### 🔍 SQL Utilities (`sql_utils.py`)
- Execute SQL queries on SQL warehouses
- Manage SQL warehouse connections
- Handle query results and data export
- Work with Unity Catalog objects

### 📊 Jobs Utilities (`jobs_utils.py`)
- Create and manage Databricks jobs
- Run jobs and monitor execution
- Handle job parameters and scheduling
- Get job run history and results

## Usage

All utilities are designed to work with the main Databricks SDK client that's already configured in your FastAPI application. Import the utilities you need:

```python
from databricks_utils.workspace_utils import list_workspace_files, upload_file
from databricks_utils.cluster_utils import get_cluster_status, start_cluster
from databricks_utils.sql_utils import execute_sql_query, get_tables
```

## Authentication

The utilities use the same authentication configuration as your main application:
- Personal Access Token (PAT) via `DATABRICKS_TOKEN`
- Or Databricks CLI profile via `DATABRICKS_CONFIG_PROFILE`

## Error Handling

All utilities include proper error handling and logging. Check the FastAPI logs for detailed error messages when working with Databricks APIs.

## Dependencies

The utilities require the `databricks-sdk` package, which is already included in your project dependencies via `pyproject.toml`.