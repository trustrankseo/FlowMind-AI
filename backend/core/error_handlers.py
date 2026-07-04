from fastapi import Request
from fastapi.responses import JSONResponse

from backend.core.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(str(exc))

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error",
            "message": str(exc)
        }
    )