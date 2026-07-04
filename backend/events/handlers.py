
from backend.core.logger import logger


async def log_event(event):

    logger.info(
        f"[EVENT] {event.name}"
    )


async def task_completed(event):

    logger.info(
        f"[TASK COMPLETED] {event.payload}"
    )