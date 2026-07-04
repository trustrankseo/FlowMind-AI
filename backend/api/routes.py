from fastapi import APIRouter
from backend.agents.manager import manager

router = APIRouter()


@router.get("/agents")
async def get_agents():
    return manager.get_agents()


@router.get("/agents/{name}")
async def get_agent(name: str):
    return manager.get_agent(name)