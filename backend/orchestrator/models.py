from pydantic import BaseModel
from typing import Any


class OrchestratorRequest(BaseModel):
    session_id: str
    message: str


class OrchestratorResponse(BaseModel):
    success: bool
    response: str
    data: Any = None