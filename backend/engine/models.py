from pydantic import BaseModel


class EngineRequest(BaseModel):
    session_id: str
    message: str


class EngineResponse(BaseModel):
    success: bool
    response: str