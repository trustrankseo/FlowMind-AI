from enum import Enum
from pydantic import BaseModel
from typing import List


class WorkflowStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"


class WorkflowStep(BaseModel):
    name: str
    agent: str


class Workflow(BaseModel):
    name: str
    status: WorkflowStatus = WorkflowStatus.PENDING
    steps: List[WorkflowStep] = []