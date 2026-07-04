from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("FlowMind Starting...")

    yield

    logger.info("FlowMind Stopped.")