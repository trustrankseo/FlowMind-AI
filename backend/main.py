from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.lifespan import lifespan
from backend.core.health import system_health
from backend.core.middleware import LoggingMiddleware
from backend.core.error_handlers import global_exception_handler

from backend.api.routes import router
from backend.api.history import router as history_router
from backend.api.auth import router as auth_router

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
    version="1.0.0",
    lifespan=lifespan
)

# ---------------------------
# Middleware
# ---------------------------

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein specific domains use karenge
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Logging
app.add_middleware(LoggingMiddleware)

# ---------------------------
# Exception Handlers
# ---------------------------

app.add_exception_handler(
    Exception,
    global_exception_handler
)

# ---------------------------
# API Routes
# ---------------------------

app.include_router(router, prefix="/api")
app.include_router(history_router, prefix="/api")

# Authentication Routes
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

# ---------------------------
# Root Endpoint
# ---------------------------

@app.get("/")
async def root():
    return {
        "app": "FlowMind AI",
        "status": "Running",
        "version": "1.0.0",
        "message": "Welcome to FlowMind AI 🚀"
    }

# ---------------------------
# Health Endpoint
# ---------------------------

@app.get("/health")
async def health():
    return system_health()