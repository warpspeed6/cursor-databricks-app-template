# MLflow Utilities

This directory contains utilities for working with MLflow in Databricks environments.

## Overview

MLflow is an open-source platform for managing the complete machine learning lifecycle. With the `mlflow[databricks]` integration, you get enhanced capabilities for:

- **Experiment Tracking**: Log parameters, metrics, and artifacts
- **Model Management**: Register, version, and deploy models
- **AI Agent Integration**: Build and deploy AI agents with LLMs
- **Databricks Integration**: Seamless workspace integration with Unity Catalog

## Modules

### `experiment_utils.py`
Utilities for managing MLflow experiments:
- Create and manage experiments
- Set experiment tags and permissions
- Search and filter experiments

### `model_utils.py` 
Utilities for model lifecycle management:
- Register models in MLflow Model Registry
- Manage model versions and stages
- Deploy models to endpoints

### `tracking_utils.py`
Utilities for experiment tracking:
- Start and end runs
- Log parameters, metrics, and artifacts
- Search and retrieve run data

## Usage

```python
from server.databricks_utils.mlflow_utils import (
    create_experiment,
    register_model,
    start_run,
    log_metric
)

# Create an experiment
experiment_id = create_experiment("/Users/user@company.com/my-experiment")

# Start a run and log metrics
run_id = start_run(experiment_id)
log_metric(run_id, "accuracy", 0.95)

# Register a model
model_version = register_model("my-model", "models:/my-model/1")
```

## Authentication

These utilities automatically use your Databricks authentication configured in the app:
- Personal Access Token (PAT)
- Databricks CLI profile
- Service principal (when deployed)

## Documentation

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow on Databricks](https://docs.databricks.com/mlflow/index.html)
- [Databricks AI Agents](https://docs.databricks.com/en/generative-ai/agents/index.html)