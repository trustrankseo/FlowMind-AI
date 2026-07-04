from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.agents.manager import manager
from backend.models.chat import ChatRequest
from backend.services.chat_service import chat_service

router = APIRouter()


@router.get("/agents")
async def get_agents():
    return manager.get_agents()


@router.get("/agents/{name}")
async def get_agent(name: str):
    return manager.get_agent(name)


@router.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    return await chat_service.process(
        db,
        request.session_id,
        request.message
    )