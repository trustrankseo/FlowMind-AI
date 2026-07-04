from contextlib import asynccontextmanager
from fastapi import FastAPI

from backend.core.logger import logger
from backend.core.bootstrap import bootstrap
from backend.plugins.loader import plugin_loader


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("FlowMind Starting...")

    # Discover Plugins
    plugin_loader.discover()

    # Register Core Services
    bootstrap()

    logger.info(
        f"Loaded Plugins: {list(plugin_loader.all().keys())}"
    )

    yield

    logger.info("FlowMind Stopped.")