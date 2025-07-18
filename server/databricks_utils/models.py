"""Pydantic models for Databricks API responses."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class WorkspaceFileInfo(BaseModel):
  """Information about a workspace file or directory."""

  path: str
  object_type: Optional[str] = None
  language: Optional[str] = None
  size: Optional[int] = None
  created_at: Optional[datetime] = None
  modified_at: Optional[datetime] = None
  object_id: Optional[str] = None


class ClusterInfo(BaseModel):
  """Information about a Databricks cluster."""

  cluster_id: str
  cluster_name: str
  state: Optional[str] = None
  state_message: Optional[str] = None
  driver_node_type_id: Optional[str] = None
  node_type_id: Optional[str] = None
  num_workers: Optional[int] = None
  spark_version: Optional[str] = None
  creator_user_name: Optional[str] = None
  start_time: Optional[datetime] = None
  terminated_time: Optional[datetime] = None
  last_state_loss_time: Optional[datetime] = None
  last_activity_time: Optional[datetime] = None
  cluster_memory_mb: Optional[int] = None
  cluster_cores: Optional[float] = None
  default_tags: Optional[dict[str, str]] = None
  cluster_log_conf: Optional[dict[str, Any]] = None
  init_scripts: Optional[list[dict[str, Any]]] = None
  spark_conf: Optional[dict[str, str]] = None
  aws_attributes: Optional[dict[str, Any]] = None
  ssh_public_keys: Optional[list[str]] = None
  custom_tags: Optional[dict[str, str]] = None
  spark_env_vars: Optional[dict[str, str]] = None
  autotermination_minutes: Optional[int] = None
  enable_elastic_disk: Optional[bool] = None
  disk_spec: Optional[dict[str, Any]] = None
  cluster_source: Optional[str] = None
  policy_id: Optional[str] = None


class ClusterEvent(BaseModel):
  """Information about a cluster event."""

  cluster_id: str
  timestamp: Optional[datetime] = None
  type: Optional[str] = None
  details: Optional[dict[str, Any]] = None


class WarehouseInfo(BaseModel):
  """Information about a SQL warehouse."""

  id: str
  name: str
  state: Optional[str] = None
  cluster_size: Optional[str] = None
  min_num_clusters: Optional[int] = None
  max_num_clusters: Optional[int] = None
  auto_stop_mins: Optional[int] = None
  creator_name: Optional[str] = None
  jdbc_url: Optional[str] = None
  odbc_params: Optional[dict[str, str]] = None
  tags: Optional[dict[str, str]] = None
  spot_instance_policy: Optional[str] = None
  enable_photon: Optional[bool] = None
  enable_serverless_compute: Optional[bool] = None
  warehouse_type: Optional[str] = None
  num_clusters: Optional[int] = None
  num_active_sessions: Optional[int] = None


class QueryResult(BaseModel):
  """Result of a SQL query execution."""

  statement_id: str
  status: Optional[str] = None
  manifest: Optional[dict[str, Any]] = None
  result: Optional[dict[str, Any]] = None
  error: Optional[dict[str, Any]] = None


class CatalogInfo(BaseModel):
  """Information about a Unity Catalog catalog."""

  name: str
  comment: Optional[str] = None
  storage_root: Optional[str] = None
  owner: Optional[str] = None
  created_at: Optional[datetime] = None
  updated_at: Optional[datetime] = None
  created_by: Optional[str] = None
  updated_by: Optional[str] = None
  metastore_id: Optional[str] = None
  full_name: Optional[str] = None
  catalog_type: Optional[str] = None
  provisioning_info: Optional[dict[str, Any]] = None
  securable_kind: Optional[str] = None
  securable_type: Optional[str] = None


class SchemaInfo(BaseModel):
  """Information about a Unity Catalog schema."""

  name: str
  catalog_name: str
  comment: Optional[str] = None
  storage_root: Optional[str] = None
  owner: Optional[str] = None
  created_at: Optional[datetime] = None
  updated_at: Optional[datetime] = None
  created_by: Optional[str] = None
  updated_by: Optional[str] = None
  metastore_id: Optional[str] = None
  full_name: Optional[str] = None
  schema_type: Optional[str] = None
  provisioning_info: Optional[dict[str, Any]] = None
  securable_kind: Optional[str] = None
  securable_type: Optional[str] = None


class TableInfo(BaseModel):
  """Information about a Unity Catalog table."""

  name: str
  catalog_name: str
  schema_name: str
  table_type: Optional[str] = None
  data_source_format: Optional[str] = None
  storage_location: Optional[str] = None
  storage_credential_name: Optional[str] = None
  owner: Optional[str] = None
  comment: Optional[str] = None
  created_at: Optional[datetime] = None
  updated_at: Optional[datetime] = None
  created_by: Optional[str] = None
  updated_by: Optional[str] = None
  metastore_id: Optional[str] = None
  full_name: Optional[str] = None
  properties: Optional[dict[str, str]] = None
  sql_path: Optional[str] = None
  columns: Optional[list[dict[str, Any]]] = None
  partitions: Optional[list[dict[str, Any]]] = None
  view_definition: Optional[str] = None
  view_dependencies: Optional[list[dict[str, Any]]] = None
  delta_runtime_properties_kvpairs: Optional[dict[str, str]] = None
  effective_auto_maintenance_flag: Optional[bool] = None
  enable_predictive_optimization: Optional[bool] = None
  pipeline_id: Optional[str] = None
  table_constraints: Optional[list[dict[str, Any]]] = None
  table_id: Optional[str] = None
