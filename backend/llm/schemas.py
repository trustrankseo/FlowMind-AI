from pydantic import BaseModel


class ToolDecision(BaseModel):

    tool: str

    action: str

    input: str | None = None