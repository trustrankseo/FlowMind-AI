from contextlib import asynccontextmanager
from fastapi import FastAPI

from backend.core.logger import logger
from backend.plugins.loader import plugin_loader


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("FlowMind Starting...")

    plugin_loader.discover()

    logger.info(
        f"Loaded Plugins: {list(plugin_loader.all().keys())}"
    )

    yield

    logger.info("FlowMind Stopped.")