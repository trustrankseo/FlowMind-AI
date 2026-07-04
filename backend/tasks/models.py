from enum import Enum
from pydantic import BaseModel
from typing import Optional


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task(BaseModel):
    id: str
    name: str
    status: TaskStatus = TaskStatus.PENDING
    data: Optional[dict] = None