"""Insights router for MLflow experiments and runs data."""

from typing import List, Optional

import mlflow
import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ExperimentSummary(BaseModel):
  """MLflow experiment summary information."""

  experiment_id: str
  name: str
  run_count: int
  artifact_location: str
  lifecycle_stage: str


class RunMetrics(BaseModel):
  """MLflow run metrics and metadata."""

  run_id: str
  experiment_id: str
  status: str
  start_time: Optional[int]
  end_time: Optional[int]
  metrics: dict
  params: dict
  tags: dict


@router.get('/experiments', response_model=List[ExperimentSummary])
async def get_experiments():
  """Get all MLflow experiments with summary information."""
  try:
    client = mlflow.tracking.MlflowClient()
    experiments = client.search_experiments()

    result = []
    for exp in experiments:
      runs = client.search_runs(experiment_ids=[exp.experiment_id], max_results=1000)

      result.append(
        ExperimentSummary(
          experiment_id=exp.experiment_id,
          name=exp.name,
          run_count=len(runs),
          artifact_location=exp.artifact_location,
          lifecycle_stage=exp.lifecycle_stage,
        )
      )

    return result
  except Exception as e:
    raise HTTPException(status_code=500, detail=f'Failed to fetch experiments: {str(e)}')


@router.get('/experiments/{experiment_id}/runs', response_model=List[RunMetrics])
async def get_experiment_runs(experiment_id: str, limit: int = 100):
  """Get runs for a specific experiment."""
  try:
    client = mlflow.tracking.MlflowClient()
    runs = client.search_runs(experiment_ids=[experiment_id], max_results=limit)

    result = []
    for run in runs:
      result.append(
        RunMetrics(
          run_id=run.info.run_id,
          experiment_id=run.info.experiment_id,
          status=run.info.status,
          start_time=run.info.start_time,
          end_time=run.info.end_time,
          metrics=run.data.metrics,
          params=run.data.params,
          tags=run.data.tags,
        )
      )

    return result
  except Exception as e:
    raise HTTPException(status_code=500, detail=f'Failed to fetch runs: {str(e)}')


@router.get('/experiments/{experiment_id}/insights')
async def get_experiment_insights(experiment_id: str):
  """Get insights and analytics for a specific experiment."""
  try:
    client = mlflow.tracking.MlflowClient()
    runs = client.search_runs(experiment_ids=[experiment_id], max_results=1000)

    if not runs:
      return {'message': 'No runs found for this experiment'}

    # Convert to DataFrame for analysis
    data = []
    for run in runs:
      row = {
        'run_id': run.info.run_id,
        'status': run.info.status,
        'start_time': run.info.start_time,
        'end_time': run.info.end_time,
        **run.data.metrics,
        **run.data.params,
      }
      data.append(row)

    df = pd.DataFrame(data)

    # Basic insights
    insights = {
      'total_runs': len(runs),
      'successful_runs': len(df[df['status'] == 'FINISHED']),
      'failed_runs': len(df[df['status'] == 'FAILED']),
      'running_runs': len(df[df['status'] == 'RUNNING']),
      'metrics_summary': {},
      'parameter_analysis': {},
    }

    # Metrics analysis
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
      if col not in ['start_time', 'end_time']:
        insights['metrics_summary'][col] = {
          'mean': float(df[col].mean()) if not df[col].isna().all() else None,
          'std': float(df[col].std()) if not df[col].isna().all() else None,
          'min': float(df[col].min()) if not df[col].isna().all() else None,
          'max': float(df[col].max()) if not df[col].isna().all() else None,
          'count': int(df[col].count()),
        }

    return insights
  except Exception as e:
    raise HTTPException(status_code=500, detail=f'Failed to generate insights: {str(e)}')
