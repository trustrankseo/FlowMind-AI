from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.logger import logger
from backend.core.banner import startup_banner
from backend.core.bootstrap import bootstrap
from backend.plugins.loader import plugin_loader


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup Banner
    logger.info(startup_banner())

    logger.info("FlowMind Starting...")

    # Discover Plugins
    plugin_loader.discover()

    # Register Core Services
    bootstrap()

    logger.info(
        f"Loaded Plugins: {list(plugin_loader.all().keys())}"
    )

    logger.info("FlowMind Startup Completed Successfully.")

    yield

    logger.info("FlowMind Shutting Down...")

    logger.info("FlowMind Stopped.")