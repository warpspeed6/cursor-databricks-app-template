"""SQL utilities for managing Databricks SQL warehouses and queries."""

import logging

from databricks.sdk import WorkspaceClient
from databricks.sdk.errors import DatabricksError

logger = logging.getLogger(__name__)


class SQLUtils:
  """Utilities for Databricks SQL warehouse operations."""

  def __init__(self, client: WorkspaceClient):
    self.client = client

  def list_warehouses(self):
    """List all SQL warehouses in the workspace.

    Returns:
        List of warehouse information
    """
    try:
      warehouses = list(self.client.warehouses.list())
      return [
        {
          'id': warehouse.id,
          'name': warehouse.name,
          'state': warehouse.state.name if warehouse.state else None,
          'cluster_size': warehouse.cluster_size,
          'min_num_clusters': warehouse.min_num_clusters,
          'max_num_clusters': warehouse.max_num_clusters,
          'auto_stop_mins': warehouse.auto_stop_mins,
          'creator_name': warehouse.creator_name,
          'jdbc_url': warehouse.jdbc_url,
          'odbc_params': warehouse.odbc_params,
          'tags': warehouse.tags,
          'spot_instance_policy': warehouse.spot_instance_policy,
          'enable_photon': warehouse.enable_photon,
          'enable_serverless_compute': warehouse.enable_serverless_compute,
          'warehouse_type': warehouse.warehouse_type,
          'num_clusters': warehouse.num_clusters,
          'num_active_sessions': warehouse.num_active_sessions,
        }
        for warehouse in warehouses
      ]
    except DatabricksError as e:
      logger.error(f'Failed to list warehouses: {e}')
      raise

  def get_warehouse(self, warehouse_id: str):
    """Get information about a specific warehouse.

    Args:
        warehouse_id: The warehouse ID

    Returns:
        Warehouse information or None if not found
    """
    try:
      warehouse = self.client.warehouses.get(warehouse_id)
      return {
        'id': warehouse.id,
        'name': warehouse.name,
        'state': warehouse.state.name if warehouse.state else None,
        'cluster_size': warehouse.cluster_size,
        'min_num_clusters': warehouse.min_num_clusters,
        'max_num_clusters': warehouse.max_num_clusters,
        'auto_stop_mins': warehouse.auto_stop_mins,
        'creator_name': warehouse.creator_name,
        'jdbc_url': warehouse.jdbc_url,
        'odbc_params': warehouse.odbc_params,
        'tags': warehouse.tags,
        'spot_instance_policy': warehouse.spot_instance_policy,
        'enable_photon': warehouse.enable_photon,
        'enable_serverless_compute': warehouse.enable_serverless_compute,
        'warehouse_type': warehouse.warehouse_type,
        'num_clusters': warehouse.num_clusters,
        'num_active_sessions': warehouse.num_active_sessions,
      }
    except DatabricksError as e:
      logger.error(f'Failed to get warehouse {warehouse_id}: {e}')
      return None

  def execute_query(self, warehouse_id: str, query: str, timeout_seconds: int = 300):
    """Execute a SQL query on a warehouse.

    Args:
        warehouse_id: The warehouse ID to execute on
        query: The SQL query to execute
        timeout_seconds: Query timeout in seconds

    Returns:
        Query execution result
    """
    try:
      response = self.client.statement_execution.execute_statement(
        warehouse_id=warehouse_id, statement=query, wait_timeout=f'{timeout_seconds}s'
      )

      return {
        'statement_id': response.statement_id,
        'status': response.status.state.name if response.status and response.status.state else None,
        'manifest': response.manifest,
        'result': response.result,
        'error': response.status.error if response.status else None,
      }
    except DatabricksError as e:
      logger.error(f'Failed to execute query on warehouse {warehouse_id}: {e}')
      raise

  def get_query_result(self, statement_id: str):
    """Get the result of a previously executed query.

    Args:
        statement_id: The statement ID from execute_query

    Returns:
        Query result or None if not found
    """
    try:
      response = self.client.statement_execution.get_statement(statement_id)

      return {
        'statement_id': response.statement_id,
        'status': response.status.state.name if response.status and response.status.state else None,
        'manifest': response.manifest,
        'result': response.result,
        'error': response.status.error if response.status else None,
      }
    except DatabricksError as e:
      logger.error(f'Failed to get query result for statement {statement_id}: {e}')
      return None

  def cancel_query(self, statement_id: str) -> bool:
    """Cancel a running query.

    Args:
        statement_id: The statement ID to cancel

    Returns:
        True if successful, False otherwise
    """
    try:
      self.client.statement_execution.cancel_execution(statement_id)
      logger.info(f'Successfully cancelled query {statement_id}')
      return True
    except DatabricksError as e:
      logger.error(f'Failed to cancel query {statement_id}: {e}')
      return False

  def list_catalogs(self):
    """List all catalogs in Unity Catalog.

    Returns:
        List of catalog information
    """
    try:
      catalogs = list(self.client.catalogs.list())
      return [
        {
          'name': catalog.name,
          'comment': catalog.comment,
          'storage_root': catalog.storage_root,
          'owner': catalog.owner,
          'created_at': catalog.created_at,
          'updated_at': catalog.updated_at,
          'created_by': catalog.created_by,
          'updated_by': catalog.updated_by,
          'metastore_id': catalog.metastore_id,
          'full_name': catalog.full_name,
          'catalog_type': catalog.catalog_type,
          'provisioning_info': catalog.provisioning_info,
          'securable_kind': catalog.securable_kind,
          'securable_type': catalog.securable_type,
        }
        for catalog in catalogs
      ]
    except DatabricksError as e:
      logger.error(f'Failed to list catalogs: {e}')
      return []

  def list_schemas(self, catalog_name: str):
    """List all schemas in a catalog.

    Args:
        catalog_name: The catalog name

    Returns:
        List of schema information
    """
    try:
      schemas = list(self.client.schemas.list(catalog_name))
      return [
        {
          'name': schema.name,
          'catalog_name': schema.catalog_name,
          'comment': schema.comment,
          'storage_root': schema.storage_root,
          'owner': schema.owner,
          'created_at': schema.created_at,
          'updated_at': schema.updated_at,
          'created_by': schema.created_by,
          'updated_by': schema.updated_by,
          'metastore_id': schema.metastore_id,
          'full_name': schema.full_name,
          'schema_type': schema.schema_type,
          'provisioning_info': schema.provisioning_info,
          'securable_kind': schema.securable_kind,
          'securable_type': schema.securable_type,
        }
        for schema in schemas
      ]
    except DatabricksError as e:
      logger.error(f'Failed to list schemas in catalog {catalog_name}: {e}')
      return []

  def list_tables(self, catalog_name: str, schema_name: str):
    """List all tables in a schema.

    Args:
        catalog_name: The catalog name
        schema_name: The schema name

    Returns:
        List of table information
    """
    try:
      tables = list(self.client.tables.list(catalog_name, schema_name))
      return [
        {
          'name': table.name,
          'catalog_name': table.catalog_name,
          'schema_name': table.schema_name,
          'table_type': table.table_type,
          'data_source_format': table.data_source_format,
          'storage_location': table.storage_location,
          'storage_credential_name': table.storage_credential_name,
          'owner': table.owner,
          'comment': table.comment,
          'created_at': table.created_at,
          'updated_at': table.updated_at,
          'created_by': table.created_by,
          'updated_by': table.updated_by,
          'metastore_id': table.metastore_id,
          'full_name': table.full_name,
          'properties': table.properties,
          'sql_path': table.sql_path,
          'columns': table.columns,
          'partitions': table.partitions,
          'view_definition': table.view_definition,
          'view_dependencies': table.view_dependencies,
          'delta_runtime_properties_kvpairs': table.delta_runtime_properties_kvpairs,
          'effective_auto_maintenance_flag': table.effective_auto_maintenance_flag,
          'enable_predictive_optimization': table.enable_predictive_optimization,
          'pipeline_id': table.pipeline_id,
          'table_constraints': table.table_constraints,
          'table_id': table.table_id,
        }
        for table in tables
      ]
    except DatabricksError as e:
      logger.error(f'Failed to list tables in {catalog_name}.{schema_name}: {e}')
      return []

  def get_table_info(self, full_name: str):
    """Get detailed information about a table.

    Args:
        full_name: The full table name (catalog.schema.table)

    Returns:
        Table information or None if not found
    """
    try:
      table = self.client.tables.get(full_name)
      return {
        'name': table.name,
        'catalog_name': table.catalog_name,
        'schema_name': table.schema_name,
        'table_type': table.table_type,
        'data_source_format': table.data_source_format,
        'storage_location': table.storage_location,
        'storage_credential_name': table.storage_credential_name,
        'owner': table.owner,
        'comment': table.comment,
        'created_at': table.created_at,
        'updated_at': table.updated_at,
        'created_by': table.created_by,
        'updated_by': table.updated_by,
        'metastore_id': table.metastore_id,
        'full_name': table.full_name,
        'properties': table.properties,
        'sql_path': table.sql_path,
        'columns': table.columns,
        'partitions': table.partitions,
        'view_definition': table.view_definition,
        'view_dependencies': table.view_dependencies,
        'delta_runtime_properties_kvpairs': table.delta_runtime_properties_kvpairs,
        'effective_auto_maintenance_flag': table.effective_auto_maintenance_flag,
        'enable_predictive_optimization': table.enable_predictive_optimization,
        'pipeline_id': table.pipeline_id,
        'table_constraints': table.table_constraints,
        'table_id': table.table_id,
      }
    except DatabricksError as e:
      logger.error(f'Failed to get table info for {full_name}: {e}')
      return None


def get_sql_utils(client: WorkspaceClient) -> SQLUtils:
  """Factory function to create SQLUtils instance.

  Args:
      client: Databricks WorkspaceClient instance

  Returns:
      SQLUtils instance
  """
  return SQLUtils(client)
