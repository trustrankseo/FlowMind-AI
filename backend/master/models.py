from enum import Enum
from pydantic import BaseModel


class AgentType(str, Enum):
    CODING = "coding"
    BROWSER = "browser"
    GITHUB = "github"
    MEMORY = "memory"
    VISION = "vision"
    CHAT = "chat"


class AgentTask(BaseModel):
    agent: AgentType
    action: str
    payload: dict = {}