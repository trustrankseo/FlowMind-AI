from fastapi import APIRouter

from backend.core.logger import memory_log_handler

router = APIRouter()


@router.get("/recent")
async def recent_logs(limit: int = 100):
    return {
        "logs": memory_log_handler.recent(limit)
    }
