from backend.core.logger import logger


async def log_event(event):

    logger.info(
        f"Event: {event.name}"
    )