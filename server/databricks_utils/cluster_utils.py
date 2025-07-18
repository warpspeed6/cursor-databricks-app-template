"""Cluster utilities for managing Databricks compute clusters."""

import logging
from typing import Optional

from databricks.sdk import WorkspaceClient
from databricks.sdk.errors import DatabricksError

from .models import ClusterEvent, ClusterInfo

logger = logging.getLogger(__name__)


class ClusterUtils:
  """Utilities for Databricks cluster operations."""

  def __init__(self, client: WorkspaceClient):
    self.client = client

  def list_clusters(self, can_use_client: Optional[str] = None) -> list[ClusterInfo]:
    """List all clusters in the workspace.

    Args:
        can_use_client: Filter clusters by client type

    Returns:
        List of cluster information dictionaries
    """
    try:
      clusters = list(self.client.clusters.list(can_use_client=can_use_client))
      return [
        {
          'cluster_id': cluster.cluster_id,
          'cluster_name': cluster.cluster_name,
          'state': cluster.state.name if cluster.state else None,
          'driver_node_type_id': cluster.driver_node_type_id,
          'node_type_id': cluster.node_type_id,
          'num_workers': cluster.num_workers,
          'spark_version': cluster.spark_version,
          'creator_user_name': cluster.creator_user_name,
          'start_time': cluster.start_time,
          'terminated_time': cluster.terminated_time,
          'last_state_loss_time': cluster.last_state_loss_time,
          'last_activity_time': cluster.last_activity_time,
          'cluster_memory_mb': cluster.cluster_memory_mb,
          'cluster_cores': cluster.cluster_cores,
          'default_tags': cluster.default_tags,
          'cluster_log_conf': cluster.cluster_log_conf,
          'init_scripts': cluster.init_scripts,
          'spark_conf': cluster.spark_conf,
          'aws_attributes': cluster.aws_attributes,
          'ssh_public_keys': cluster.ssh_public_keys,
          'custom_tags': cluster.custom_tags,
          'spark_env_vars': cluster.spark_env_vars,
          'autotermination_minutes': cluster.autotermination_minutes,
          'enable_elastic_disk': cluster.enable_elastic_disk,
          'disk_spec': cluster.disk_spec,
          'cluster_source': cluster.cluster_source,
          'policy_id': cluster.policy_id,
        }
        for cluster in clusters
      ]
    except DatabricksError as e:
      logger.error(f'Failed to list clusters: {e}')
      raise

  def get_cluster(self, cluster_id: str) -> Optional[ClusterInfo]:
    """Get information about a specific cluster.

    Args:
        cluster_id: The cluster ID

    Returns:
        Cluster information dictionary or None if not found
    """
    try:
      cluster = self.client.clusters.get(cluster_id)
      return ClusterInfo(
        cluster_id=cluster.cluster_id,
        cluster_name=cluster.cluster_name,
        state=cluster.state.name if cluster.state else None,
        state_message=cluster.state_message,
        driver_node_type_id=cluster.driver_node_type_id,
        node_type_id=cluster.node_type_id,
        num_workers=cluster.num_workers,
        spark_version=cluster.spark_version,
        creator_user_name=cluster.creator_user_name,
        start_time=cluster.start_time,
        terminated_time=cluster.terminated_time,
        last_state_loss_time=cluster.last_state_loss_time,
        last_activity_time=cluster.last_activity_time,
        cluster_memory_mb=cluster.cluster_memory_mb,
        cluster_cores=cluster.cluster_cores,
        default_tags=cluster.default_tags,
        cluster_log_conf=cluster.cluster_log_conf,
        init_scripts=cluster.init_scripts,
        spark_conf=cluster.spark_conf,
      )
    except DatabricksError as e:
      logger.error(f'Failed to get cluster {cluster_id}: {e}')
      return None

  def start_cluster(self, cluster_id: str) -> bool:
    """Start a cluster.

    Args:
        cluster_id: The cluster ID to start

    Returns:
        True if successful, False otherwise
    """
    try:
      self.client.clusters.start(cluster_id)
      logger.info(f'Successfully started cluster {cluster_id}')
      return True
    except DatabricksError as e:
      logger.error(f'Failed to start cluster {cluster_id}: {e}')
      return False

  def restart_cluster(self, cluster_id: str) -> bool:
    """Restart a cluster.

    Args:
        cluster_id: The cluster ID to restart

    Returns:
        True if successful, False otherwise
    """
    try:
      self.client.clusters.restart(cluster_id)
      logger.info(f'Successfully restarted cluster {cluster_id}')
      return True
    except DatabricksError as e:
      logger.error(f'Failed to restart cluster {cluster_id}: {e}')
      return False

  def terminate_cluster(self, cluster_id: str) -> bool:
    """Terminate a cluster.

    Args:
        cluster_id: The cluster ID to terminate

    Returns:
        True if successful, False otherwise
    """
    try:
      self.client.clusters.delete(cluster_id)
      logger.info(f'Successfully terminated cluster {cluster_id}')
      return True
    except DatabricksError as e:
      logger.error(f'Failed to terminate cluster {cluster_id}: {e}')
      return False

  def get_cluster_status(self, cluster_id: str) -> Optional[str]:
    """Get the current status of a cluster.

    Args:
        cluster_id: The cluster ID

    Returns:
        Cluster state as string or None if not found
    """
    try:
      cluster = self.client.clusters.get(cluster_id)
      return cluster.state.name if cluster.state else None
    except DatabricksError as e:
      logger.error(f'Failed to get cluster status for {cluster_id}: {e}')
      return None

  def wait_for_cluster_state(
    self, cluster_id: str, target_state: str, timeout_minutes: int = 10
  ) -> bool:
    """Wait for a cluster to reach a specific state.

    Args:
        cluster_id: The cluster ID
        target_state: The target state to wait for
        timeout_minutes: Maximum time to wait in minutes

    Returns:
        True if cluster reaches target state, False if timeout
    """
    try:
      if target_state.upper() == 'RUNNING':
        self.client.clusters.wait_get_cluster_running(cluster_id, timeout=timeout_minutes * 60)
      elif target_state.upper() == 'TERMINATED':
        self.client.clusters.wait_get_cluster_terminated(cluster_id, timeout=timeout_minutes * 60)
      else:
        # For other states, we'll poll manually
        import time

        start_time = time.time()
        while time.time() - start_time < timeout_minutes * 60:
          current_state = self.get_cluster_status(cluster_id)
          if current_state == target_state.upper():
            return True
          time.sleep(30)  # Check every 30 seconds
        return False

      return True
    except DatabricksError as e:
      logger.error(f'Failed to wait for cluster {cluster_id} to reach state {target_state}: {e}')
      return False

  def get_cluster_events(
    self,
    cluster_id: str,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
    limit: int = 50,
  ) -> list[ClusterEvent]:
    """Get events for a cluster.

    Args:
        cluster_id: The cluster ID
        start_time: Start time for events (Unix timestamp)
        end_time: End time for events (Unix timestamp)
        limit: Maximum number of events to return

    Returns:
        List of cluster event dictionaries
    """
    try:
      events = list(
        self.client.clusters.events(
          cluster_id=cluster_id, start_time=start_time, end_time=end_time, limit=limit
        )
      )

      return [
        {
          'cluster_id': event.cluster_id,
          'timestamp': event.timestamp,
          'type': event.type.name if event.type else None,
          'details': event.details,
        }
        for event in events
      ]
    except DatabricksError as e:
      logger.error(f'Failed to get cluster events for {cluster_id}: {e}')
      return []


def get_cluster_utils(client: WorkspaceClient) -> ClusterUtils:
  """Factory function to create ClusterUtils instance.

  Args:
      client: Databricks WorkspaceClient instance

  Returns:
      ClusterUtils instance
  """
  return ClusterUtils(client)
