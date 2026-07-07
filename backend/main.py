from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from backend.core.lifespan import lifespan
from backend.core.health import system_health
from backend.core.middleware import LoggingMiddleware
from backend.core.error_handlers import global_exception_handler
from backend.core.version import VERSION
from backend.core.api_info import api_info

from backend.api.routes import router
from backend.api.history import router as history_router
from backend.api.auth import router as auth_router
from backend.api.github import router as github_router
from backend.api.testing import router as testing_router
from backend.api.images import router as images_router
from backend.api.video import router as video_router
from backend.api.voice import router as voice_router
from backend.api.deployment import router as deployment_router
from backend.api.logs import router as logs_router
from backend.api.files import router as files_router

from backend.database.base import Base
from backend.database.session import engine

# Import Database Models
from backend.database.models.conversation import Conversation
from backend.database.models.message import Message

# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FlowMind AI",
    description="Next Generation AI Operating System",
    version=VERSION,
    lifespan=lifespan
)

# --------------------------------------------------
# Middleware
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein specific domains use karenge
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)

# --------------------------------------------------
# Static Files (generated images/videos/audio)
# --------------------------------------------------

os.makedirs("generated", exist_ok=True)
app.mount("/generated", StaticFiles(directory="generated"), name="generated")

# --------------------------------------------------
# Exception Handlers
# --------------------------------------------------

app.add_exception_handler(
    Exception,
    global_exception_handler
)

# --------------------------------------------------
# API Routes
# --------------------------------------------------

app.include_router(router, prefix="/api")

app.include_router(
    history_router,
    prefix="/api"
)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    github_router,
    prefix="/api/github",
    tags=["GitHub"]
)

app.include_router(
    testing_router,
    prefix="/api/testing",
    tags=["Testing"]
)

app.include_router(
    images_router,
    prefix="/api/images",
    tags=["Images"]
)

app.include_router(
    video_router,
    prefix="/api/video",
    tags=["Video"]
)

app.include_router(
    voice_router,
    prefix="/api/voice",
    tags=["Voice"]
)

app.include_router(
    deployment_router,
    prefix="/api/deployment",
    tags=["Deployment"]
)

app.include_router(
    logs_router,
    prefix="/api/logs",
    tags=["Logs"]
)

app.include_router(
    files_router,
    prefix="/api/files",
    tags=["Files"]
)

# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
async def root():
    return api_info.info()

# --------------------------------------------------
# Health Endpoint
# --------------------------------------------------

@app.get("/health")
async def health():
    return system_health()