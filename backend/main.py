from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router

app = FastAPI(
    title="FlowMind AI",
    description="Next Generation AI Operating System",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein specific domains use karenge
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {
        "app": "FlowMind AI",
        "status": "Running",
        "version": "1.0.0",
        "message": "Welcome to FlowMind AI 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
from backend.database.base import Base
from backend.database.session import engine

# Import models
from backend.database.models.conversation import Conversation
from backend.database.models.message import Message

Base.metadata.create_all(bind=engine)