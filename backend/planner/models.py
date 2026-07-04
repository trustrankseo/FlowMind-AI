from enum import Enum
from pydantic import BaseModel
from typing import List


class PlanStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"


class PlanStep(BaseModel):
    id: int
    title: str
    agent: str


class ExecutionPlan(BaseModel):
    goal: str
    status: PlanStatus = PlanStatus.PENDING
    steps: List[PlanStep] = []