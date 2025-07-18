"""Workspace utilities for managing Databricks workspace files and directories."""

import logging
from typing import Optional

from databricks.sdk import WorkspaceClient
from databricks.sdk.errors import DatabricksError
from databricks.sdk.service.workspace import Language

from .models import WorkspaceFileInfo

logger = logging.getLogger(__name__)


class WorkspaceUtils:
  """Utilities for Databricks workspace operations."""

  def __init__(self, client: WorkspaceClient):
    self.client = client

  def list_workspace_files(self, path: str = '/') -> list[WorkspaceFileInfo]:
    """List files and directories in a workspace path.

    Args:
        path: Workspace path to list (default: "/")

    Returns:
        List of file/directory information objects
    """
    try:
      objects = list(self.client.workspace.list(path))
      return [
        WorkspaceFileInfo(
          path=obj.path,
          object_type=obj.object_type.name if obj.object_type else None,
          language=obj.language.name if obj.language else None,
          size=obj.size,
          created_at=obj.created_at,
          modified_at=obj.modified_at,
          object_id=obj.object_id,
        )
        for obj in objects
      ]
    except DatabricksError as e:
      logger.error(f'Failed to list workspace files at {path}: {e}')
      raise

  def upload_file(
    self,
    local_path: str,
    workspace_path: str,
    language: Optional[Language] = None,
    overwrite: bool = False,
  ) -> WorkspaceFileInfo:
    """Upload a file to Databricks workspace.

    Args:
        local_path: Path to local file
        workspace_path: Destination path in workspace
        language: Programming language of the file (auto-detected if None)
        overwrite: Whether to overwrite existing files

    Returns:
        Upload result information object
    """
    try:
      with open(local_path, 'rb') as file:
        content = file.read()

      self.client.workspace.upload(
        path=workspace_path, content=content, language=language, overwrite=overwrite
      )

      # Get the uploaded file info
      file_info = self.client.workspace.get_status(workspace_path)

      return WorkspaceFileInfo(
        path=file_info.path,
        object_type=file_info.object_type.name if file_info.object_type else None,
        language=file_info.language.name if file_info.language else None,
        size=file_info.size,
        created_at=file_info.created_at,
        modified_at=file_info.modified_at,
        object_id=file_info.object_id,
      )

    except DatabricksError as e:
      logger.error(f'Failed to upload file {local_path} to {workspace_path}: {e}')
      raise
    except FileNotFoundError:
      logger.error(f'Local file not found: {local_path}')
      raise

  def download_file(self, workspace_path: str, local_path: str) -> bool:
    """Download a file from Databricks workspace.

    Args:
        workspace_path: Path to file in workspace
        local_path: Destination path for downloaded file

    Returns:
        True if successful, False otherwise
    """
    try:
      response = self.client.workspace.download(workspace_path)

      with open(local_path, 'wb') as file:
        file.write(response.contents)

      logger.info(f'Successfully downloaded {workspace_path} to {local_path}')
      return True

    except DatabricksError as e:
      logger.error(f'Failed to download file {workspace_path}: {e}')
      return False
    except IOError as e:
      logger.error(f'Failed to write to local file {local_path}: {e}')
      return False

  def create_directory(self, path: str) -> bool:
    """Create a directory in the workspace.

    Args:
        path: Directory path to create

    Returns:
        True if successful, False otherwise
    """
    try:
      self.client.workspace.mkdirs(path)
      logger.info(f'Successfully created directory: {path}')
      return True

    except DatabricksError as e:
      logger.error(f'Failed to create directory {path}: {e}')
      return False

  def delete_file_or_directory(self, path: str, recursive: bool = False) -> bool:
    """Delete a file or directory from the workspace.

    Args:
        path: Path to delete
        recursive: Whether to delete recursively (for directories)

    Returns:
        True if successful, False otherwise
    """
    try:
      self.client.workspace.delete(path, recursive=recursive)
      logger.info(f'Successfully deleted: {path}')
      return True

    except DatabricksError as e:
      logger.error(f'Failed to delete {path}: {e}')
      return False

  def get_file_info(self, path: str) -> Optional[WorkspaceFileInfo]:
    """Get information about a workspace file or directory.

    Args:
        path: Workspace path to get info for

    Returns:
        File information object or None if not found
    """
    try:
      file_info = self.client.workspace.get_status(path)

      return WorkspaceFileInfo(
        path=file_info.path,
        object_type=file_info.object_type.name if file_info.object_type else None,
        language=file_info.language.name if file_info.language else None,
        size=file_info.size,
        created_at=file_info.created_at,
        modified_at=file_info.modified_at,
        object_id=file_info.object_id,
      )

    except DatabricksError as e:
      logger.error(f'Failed to get file info for {path}: {e}')
      return None

  def export_file(self, path: str, format: str = 'SOURCE') -> Optional[bytes]:
    """Export a file from the workspace.

    Args:
        path: Workspace path to export
        format: Export format (SOURCE, HTML, JUPYTER, DBC)

    Returns:
        File content as bytes or None if failed
    """
    try:
      response = self.client.workspace.export(path, format=format)
      return response.content

    except DatabricksError as e:
      logger.error(f'Failed to export file {path}: {e}')
      return None

  def search_files(self, query: str, max_results: int = 25) -> list[WorkspaceFileInfo]:
    """Search for files in the workspace.

    Args:
        query: Search query
        max_results: Maximum number of results to return

    Returns:
        List of matching file information objects
    """
    try:
      results = list(self.client.workspace.search(query, max_results=max_results))

      return [
        WorkspaceFileInfo(
          path=result.path,
          object_type=result.object_type.name if result.object_type else None,
          language=result.language.name if result.language else None,
          size=result.size,
          created_at=result.created_at,
          modified_at=result.modified_at,
          object_id=result.object_id,
        )
        for result in results
      ]

    except DatabricksError as e:
      logger.error(f"Failed to search files with query '{query}': {e}")
      return []


def get_workspace_utils(client: WorkspaceClient) -> WorkspaceUtils:
  """Factory function to create WorkspaceUtils instance.

  Args:
      client: Databricks WorkspaceClient instance

  Returns:
      WorkspaceUtils instance
  """
  return WorkspaceUtils(client)
