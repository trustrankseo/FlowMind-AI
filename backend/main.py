# backend/main.py
import asyncio
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .events.bus import event_bus
from .llm.providers import get_provider
from .memory.memory_manager import MemoryManager
from .agents.chat_agent import ChatAgent
from .brain.brain import Brain
from .engine.executor import Executor

logger = logging.getLogger(__name__)

app = FastAPI(title="FlowMind-AI", version="0.1.0")

# CORS middleware (frontend se connect karne ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global instances (baad mein config se initialize karein)
llm_provider = None
memory_manager = None
chat_agent = None
brain = None
executor = None

@app.on_event("startup")
async def startup():
    global llm_provider, memory_manager, chat_agent, brain, executor

    # TODO: Config se values lein — abhi hardcode karein
    config = {
        "openai_api_key": "your-openai-key-here",  # .env se replace karein
        "database_url": "sqlite:///./flowmind.db"
    }

    # LLM Provider
    try:
        llm_provider = get_provider("openai", config)
        logger.info("LLM provider initialized")
    except Exception as e:
        logger.error(f"Failed to initialize LLM provider: {e}")
        return

    # Memory Manager
    try:
        memory_manager = MemoryManager(config["database_url"])
        logger.info("Memory manager initialized")
    except Exception as e:
        logger.error(f"Failed to initialize memory manager: {e}")
        return

    # Chat Agent
    try:
        chat_agent = ChatAgent(llm_provider, memory_manager)
        logger.info("Chat agent initialized")
    except Exception as e:
        logger.error(f"Failed to initialize chat agent: {e}")
        return

    # Executor
    try:
        executor = Executor()
        executor.register_agent("chat", chat_agent)
        # Baad mein: executor.register_agent("github", github_agent), etc.
        logger.info("Executor initialized")
    except Exception as e:
        logger.error(f"Failed to initialize executor: {e}")
        return

    # Brain
    try:
        brain = Brain(llm_provider)
        logger.info("Brain initialized")
    except Exception as e:
        logger.error(f"Failed to initialize brain: {e}")
        return

    # Event Bus background task start karein
    try:
        await event_bus.start()
        logger.info("Event bus started")
    except Exception as e:
        logger.error(f"Failed to start event bus: {e}")
        return

    logger.info("FlowMind-AI backend started successfully")

@app.on_event("shutdown")
async def shutdown():
    # Event bus gracefully stop karein
    try:
        await event_bus.stop()
        logger.info("Event bus stopped")
    except Exception as e:
        logger.error(f"Error stopping event bus: {e}")

@app.get("/")
def root():
    return {"message": "FlowMind-AI is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# TODO: /api/chat endpoint add karein (streaming response)
# @app.post("/api/chat")
# async def chat_endpoint(request: ChatRequest):
#     ...