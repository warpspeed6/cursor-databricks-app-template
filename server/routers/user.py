"""User router for Databricks user information."""

from databricks.sdk import WorkspaceClient
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class UserInfo(BaseModel):
  """Databricks user information."""

  userName: str
  displayName: str | None = None
  active: bool


@router.get('/me', response_model=UserInfo)
async def get_current_user():
  """Get current user information from Databricks."""
  try:
    # Initialize Databricks client
    # It will use environment variables or configuration profiles
    w = WorkspaceClient()

    # Get current user info
    current_user = w.current_user.me()

    return UserInfo(
      userName=current_user.userName or 'unknown',
      displayName=current_user.displayName,
      active=current_user.active or False,
    )
  except Exception as e:
    raise HTTPException(status_code=500, detail=f'Failed to fetch user info: {str(e)}')
